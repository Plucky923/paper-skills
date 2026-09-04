#!/usr/bin/env python3
"""Download, prepare and run scoped external paper-skill evaluations.

Run --help. Only fetch accesses upstream data; run uses an explicitly named
Codex model. No command installs or executes code from a benchmark download.
"""

import argparse
import importlib
import json
from pathlib import Path
import random
import shutil
import subprocess
import sys

from paperbench.registry import (
    BenchmarkError, digest, fetch_source, inside, load_registry, read_json, read_jsonl,
    safe_name, select_sources, stable_hash, verify_source, write_json, write_jsonl,
)
from paperbench.runner import PROTOCOL, choose_cases, now, run_one, snapshot_bundle, validate_case, verified_output
from paperbench.runner import cancellation_signals


REPO = Path(__file__).resolve().parents[1]
BASE = REPO / "benchmarks/external"
ADAPTERS = {
    "pararev": ("paperbench.revision", "load_pararev"),
    "parareval": ("paperbench.revision", "load_parareval"),
}


def emit(value):
    print(json.dumps(value, ensure_ascii=False, indent=2), flush=True)


def batch_path(name):
    return BASE / "work" / safe_name(name)


def run_path(name):
    return BASE / "runs" / safe_name(name)


def load_batch(name):
    path = batch_path(name)
    manifest = read_json(path / "manifest.json")
    if set(manifest["files"]) != {"inputs.jsonl", "references.jsonl"}:
        raise BenchmarkError("Unexpected batch file inventory")
    for filename, expected in manifest["files"].items():
        if digest(path / filename) != expected:
            raise BenchmarkError("Prepared batch was modified: " + filename)
    inputs = read_jsonl(path / "inputs.jsonl")
    reference_rows = read_jsonl(path / "references.jsonl")
    references = {x["id"]: x for x in reference_rows}
    if (len(references) != len(reference_rows) or len({c["id"] for c in inputs}) != len(inputs)
            or set(references) != {c["id"] for c in inputs}):
        raise BenchmarkError("Batch identities are duplicated or not aligned with references")
    cases = [dict(case, reference=references[case["id"]]["reference"],
                  metadata=references[case["id"]]["metadata"]) for case in inputs]
    for case in cases:
        validate_case(case)
    return manifest, cases


def require_admitted_batch(manifest, cases):
    source = load_registry(REPO).get(manifest["source"])
    if source is None:
        raise BenchmarkError("Source is not admitted for evaluation: " + manifest["source"])
    if manifest.get("admission_sha256") != stable_hash(source["admission"]):
        raise BenchmarkError("Batch admission does not match the current policy: prepare a new batch")
    if manifest.get("source_registry_sha256") != stable_hash(source):
        raise BenchmarkError("Source registry changed: prepare a newly verified batch")
    if any(c["source"] != source["id"] or c["task"] != source["admission"]["task"] for c in cases):
        raise BenchmarkError("Batch task does not match the admitted purpose")
    return source


def run_schedule(cases, conditions):
    schedule = []
    for index, case in enumerate(cases):
        order = conditions if index % 2 == 0 else list(reversed(conditions))
        for condition in order:
            schedule.append({"directory": "{:04d}-{}".format(index, condition),
                             "case_id": case["id"], "source": case["source"], "task": case["task"],
                             "condition": condition, "input_sha256": stable_hash(case["input"])})
    return schedule


def read_call_result(directory, expected):
    """Read the one exclusively published outcome for a scheduled invocation."""
    evidence = [p for p in (directory / "result.json", directory / "failure.json") if p.is_file()]
    if not evidence:
        return None
    if len(evidence) != 1:
        raise BenchmarkError("Per-call evidence has conflicting records")
    result = read_json(evidence[0])
    if not isinstance(result, dict):
        raise BenchmarkError("Invalid per-call record")
    for key in ("case_id", "source", "task", "condition", "input_sha256"):
        if result.get(key) != expected[key]:
            raise BenchmarkError("Per-call evidence differs from schedule: " + key)
    if result.get("status") not in {"completed_unscored", "failed"}:
        raise BenchmarkError("Unknown per-call status")
    if "directory" in result and result["directory"] != expected["directory"]:
        raise BenchmarkError("Per-call directory identity differs")
    return dict(result, directory=expected["directory"])


def collect_results(path, controls):
    """Recover an immutable per-call prefix and check any aggregate against it.

    A killed outer harness may not have written results.json. Completed calls
    remain usable without issuing another model request or rewriting evidence.
    """
    planned = {entry["directory"] for entry in controls["schedule"]}
    for directory in path.iterdir():
        if directory.is_dir() and directory.name not in planned and any(
                (directory / name).is_file() for name in ("result.json", "failure.json")):
            raise BenchmarkError("Per-call evidence outside the recorded schedule: " + directory.name)
    results, gap = [], False
    for expected in controls["schedule"]:
        directory = inside(path, expected["directory"])
        result = read_call_result(directory, expected)
        if result is None:
            gap = True
            continue
        if gap:
            raise BenchmarkError("Per-call evidence has a gap")
        results.append(result)
    aggregate = path / "results.json"
    if aggregate.is_file() and read_json(aggregate) != results:
        raise BenchmarkError("Aggregate results differ from the scheduled per-call evidence")
    return results


def evaluation_context(path):
    controls = read_json(path / "manifest.json")
    if controls.get("schema_version") != 2:
        raise BenchmarkError("Unsupported run schema")
    if digest(batch_path(controls["batch"]) / "manifest.json") != controls["batch_manifest_sha256"]:
        raise BenchmarkError("Batch manifest changed after the run")
    batch_manifest, cases = load_batch(controls["batch"])
    source = require_admitted_batch(batch_manifest, cases)
    if controls.get("admission_sha256") != stable_hash(source["admission"]):
        raise BenchmarkError("Run admission does not match the admitted batch")
    count = controls.get("cases")
    if type(count) is not int or not 1 <= count <= len(cases):
        raise BenchmarkError("Invalid scheduled case count")
    condition = controls.get("condition")
    if condition not in {"both", "skill", "no-skill"}:
        raise BenchmarkError("Invalid scheduled condition")
    conditions = ["no-skill", "skill"] if condition == "both" else [condition]
    if source["admission"]["task"] == "judge_calibration" and conditions != ["no-skill"]:
        raise BenchmarkError("Judge calibration cannot be scheduled as a writing-skill condition")
    expected = run_schedule(cases[:count], conditions)
    if controls.get("schedule") != expected or controls.get("calls") != len(expected):
        raise BenchmarkError("Run schedule does not match frozen cases/conditions/counts")
    by_id = {case["id"]: case for case in cases}
    results = collect_results(path, controls)
    for result in results:
        if result["case_id"] not in by_id:
            raise BenchmarkError("Result does not belong to the frozen batch")
        if result["input_sha256"] != stable_hash(by_id[result["case_id"]]["input"]):
            raise BenchmarkError("Result input does not match the frozen batch")
    return controls, cases, results


def prepare(args, sources):
    source = sources.get(args.source)
    if source is None:
        raise BenchmarkError("Unknown source: " + args.source)
    adapter = source.get("adapter")
    for alias, (module_name, function_name) in ADAPTERS.items():
        if adapter == module_name + ":" + function_name:
            adapter = alias
            break
    if adapter not in ADAPTERS:
        raise BenchmarkError("This is an upstream-only resource; no text adapter: " + args.source)
    verified = verify_source(BASE / "cache", source)
    if verified["status"] != "verified":
        raise BenchmarkError("Fetch and verify all pinned files before preparing this source")
    module_name, function_name = ADAPTERS[adapter]
    module = importlib.import_module(module_name)
    loader = getattr(module, function_name)
    cases = loader(BASE / "cache" / source["id"])
    stats = module.pararev_selection_report(BASE / "cache" / source["id"]) if adapter == "pararev" else {}
    if any(c["source"] != source["id"] or c["task"] != source["admission"]["task"] for c in cases):
        raise BenchmarkError("Adapter output does not match its admitted task")
    selected = choose_cases(cases, args.limit, args.seed)
    if not selected:
        raise BenchmarkError("Adapter returned no eligible cases; inspect the upstream schema")
    path = batch_path(args.batch)
    path.mkdir(parents=True, exist_ok=False)
    write_jsonl(path / "inputs.jsonl", [{k: c[k] for k in ("id", "source", "task", "group_id", "input")} for c in selected])
    write_jsonl(path / "references.jsonl", [{k: c[k] for k in ("id", "reference", "metadata")} for c in selected])
    manifest = {
        "schema_version": 1, "created_at": now(), "batch": args.batch,
        "source": source["id"], "source_revision": source.get("revision"),
        "source_registry_sha256": stable_hash(source), "seed": args.seed,
        "admission_sha256": stable_hash(source["admission"]), "admission": source["admission"],
        "requested_limit": args.limit, "eligible_cases": len(cases),
        "selected_cases": len(selected), "sampling": "group_hash_then_case_hash_v2",
        "selection_report": stats, "source_verification": verified,
        "files": {n: digest(path / n) for n in ("inputs.jsonl", "references.jsonl")},
        "protocol": "adapted_text_tasks_not_upstream_leaderboard",
    }
    write_json(path / "manifest.json", manifest)
    emit({"batch": str(path), "eligible_cases": len(cases), "selected_cases": len(selected),
          "gold_separated": True, "sampling": manifest["sampling"]})


def run(args):
    manifest, cases = load_batch(args.batch)
    source = require_admitted_batch(manifest, cases)
    if args.limit < 1 or args.timeout < 1:
        raise BenchmarkError("Limits and timeout must be positive")
    binary = shutil.which(args.codex)
    if not binary:
        raise BenchmarkError("Codex CLI not found: " + args.codex)
    selected = cases[:args.limit]
    conditions = ["no-skill", "skill"] if args.condition == "both" else [args.condition]
    if any(c["task"] == "judge_calibration" for c in selected) and "skill" in conditions:
        raise BenchmarkError("Use --condition no-skill for judge calibration, not the writing skill")
    path = run_path(args.name)
    path.mkdir(parents=True, exist_ok=False)
    bundle = snapshot_bundle(REPO, source["admission"]["task"])
    write_json(path / "skill-snapshot.json", bundle)
    version = subprocess.run([binary, "--version"], capture_output=True, text=True, check=True).stdout.strip()
    controls = {
        "schema_version": 2, "started_at": now(), "batch": args.batch,
        "batch_manifest_sha256": digest(batch_path(args.batch) / "manifest.json"),
        "source": manifest["source"], "model": args.model, "effort": args.effort,
        "codex_version": version, "condition": args.condition, "cases": len(selected),
        "available_batch_cases": len(cases), "calls": len(selected) * len(conditions),
        "timeout_per_call_seconds": args.timeout, "max_prompt_characters": args.max_prompt_chars,
        "skill_snapshot_sha256": stable_hash(bundle), "protocol": PROTOCOL,
        "admission_sha256": stable_hash(source["admission"]),
        "schedule": run_schedule(selected, conditions),
        "harness_files_sha256": {p.relative_to(REPO).as_posix(): digest(p) for p in
                                 [Path(__file__).resolve()] + sorted((REPO / "scripts/paperbench").glob("*.py"))},
        "limitations": ["No native lazy skill loading, external tools, or live venue checks",
                        "No upstream leaderboard score; no acceptance decision",
                        "Configured user plugins, memories, shell and known skills disabled for the invocation",
                        "Text supplied to the user's Codex inference provider; authentication is not copied"],
    }
    write_json(path / "manifest.json", controls)
    results = []
    by_id = {case["id"]: case for case in selected}
    interrupted = False
    for index, entry in enumerate(controls["schedule"]):
        case = by_id[entry["case_id"]]
        condition = entry["condition"]
        print("Running call {}/{} {} {} (timeout {}s)".format(index + 1, controls["calls"], case["id"], condition, args.timeout), flush=True)
        case_dir = path / entry["directory"]
        try:
            result = run_one(case, condition, bundle, args.model, args.effort, binary,
                             case_dir, args.timeout, args.max_prompt_chars)
        except (OSError, ValueError, subprocess.SubprocessError, KeyboardInterrupt) as error:
            interrupted = isinstance(error, KeyboardInterrupt)
            # Cancellation can arrive immediately after atomic publication. A
            # complete, identity-checked outcome takes precedence over a new failure.
            result = read_call_result(case_dir, entry)
            if result is None:
                result = {k: entry[k] for k in ("case_id", "source", "task", "condition", "input_sha256")}
                result.update({"status": "failed", "error": "Interrupted" if interrupted else str(error),
                               "elapsed_seconds": None})
                case_dir.mkdir(parents=True, exist_ok=True)
                write_json(case_dir / "failure.json", result)
        result["directory"] = case_dir.name
        results.append(result)
        print("  {} in {}s".format(result["status"], result["elapsed_seconds"]), flush=True)
        if interrupted:
            break
    write_json(path / "results.json", results)
    report(path)
    return 130 if interrupted else (1 if any(x["status"] == "failed" for x in results) else 0)


def report(path):
    controls, _, results = evaluation_context(path)
    summary = {
        "run": str(path), "calls": len(results),
        "scheduled_calls": controls["calls"], "unfinished_calls": controls["calls"] - len(results),
        "admission_status": "current_admission",
        "completed_unscored": sum(x["status"] == "completed_unscored" for x in results),
        "failed": sum(x["status"] == "failed" for x in results),
        "quality_acceptance": "not_evaluated", "official_benchmark_score": False,
        "usage": [x.get("usage") for x in results],
    }
    emit(summary)
    return summary


def score(args):
    path = run_path(args.name)
    _, cases, results = evaluation_context(path)
    by_id = {case["id"]: case for case in cases}
    scores = []
    for result in results:
        item = {"case_id": result["case_id"], "condition": result["condition"],
                "official_benchmark_score": False}
        if result["status"] != "completed_unscored":
            item["status"] = "execution_failed"
        elif result["task"] == "judge_calibration":
            from paperbench.revision import score_parareval
            output = verified_output(path, result)
            item.update(score_parareval(output, by_id[result["case_id"]]["reference"]))
        else:
            verified_output(path, result)
            item.update({"status": "needs_human_or_validated_judge", "diagnostics": result["diagnostics"]})
        scores.append(item)
    write_json(path / "scores.json", scores)
    emit(scores)


def export_blind(args):
    path = run_path(args.name)
    controls, cases, results = evaluation_context(path)
    if any(case["task"] != "revision" for case in cases):
        raise BenchmarkError("Blind new-output evaluation is only admitted for ParaRev revisions")
    if controls["condition"] != "both":
        raise BenchmarkError("Blind comparison requires a paired skill/no-skill schedule")
    packet, mapping, references, unpaired = [], [], [], []
    randomizer = random.Random(args.seed)
    for case in cases[:controls["cases"]]:
        pair = [r for r in results if r["case_id"] == case["id"] and r["status"] == "completed_unscored"]
        if len(pair) != 2 or {r["condition"] for r in pair} != {"skill", "no-skill"}:
            unpaired.append({"id": case["id"], "reason": "failed_or_unfinished_pair"})
            continue
        if len({r["input_sha256"] for r in pair}) != 1:
            raise BenchmarkError("Mismatched candidate inputs")
        randomizer.shuffle(pair)
        rubric = {
            "input_sufficiency": "Can the requested edit be assessed from the supplied paragraph? Mark unresolved if missing context matters; do not guess.",
            "fidelity": "Are material claims, conditions and evidence status preserved?",
            "instruction_following": "Does the revision address the requested edit without unsupported additions?",
            "logic": "Does the text make the relevant supported relations clear?",
            "organization": "Does the opening establish the paragraph's role, the middle support it, and the ending close or connect the supported argument? Do not require a formulaic structure.",
            "precision": "Are terms, actors, quantities and causal claims precise?",
            "concision": "Is removable redundancy reduced without losing necessary support? Shorter is not automatically better; use no fixed word count.",
        }
        public = {"id": case["id"], "task": case["task"], "input": case["input"],
                  "protocol": "pararev-blind-human-adapted-v2",
                  "rubric": rubric,
                  "assessment": {"annotator_id": None, "input_sufficiency": None,
                                 "A_fidelity": None, "B_fidelity": None,
                                 "A_instruction_following": None, "B_instruction_following": None,
                                 "preference": None, "rationale": None, "evidence_spans": []},
                  "allowed_gate_values": ["pass", "fail", "unresolved"],
                  "allowed_preferences": ["A", "B", "tie", "neither", "unresolved"],
                  "warning": "Judge independently against the supplied input. A failed fidelity gate cannot win on style; unresolved evidence is not a pass. Author revision and condition identities stay hidden until first-pass judgments are frozen."}
        for label, result in zip(("A", "B"), pair):
            public[label] = verified_output(path, result)
        packet.append(public)
        mapping.append({"id": case["id"], "A": pair[0]["condition"], "B": pair[1]["condition"]})
        references.append({"id": case["id"], "reference_context": case["reference"],
                           "use": "Optional post-judgment context, not exact-match or factual-correctness gold."})
    if not packet:
        raise BenchmarkError("No completed matched skill/no-skill pairs to export")
    destination = path / "blind"
    destination.mkdir(exist_ok=False)
    write_jsonl(destination / "judge-packet.jsonl", packet)
    write_jsonl(destination / "reference-context.jsonl", references)
    write_json(destination / "private-labels.json", {"seed": args.seed, "labels": mapping})
    write_json(destination / "export-summary.json", {
        "protocol": "pararev-blind-human-adapted-v2", "scheduled_cases": controls["cases"],
        "exported_pairs": len(packet), "unpaired_cases": unpaired,
        "human_protocol_sha256": digest(REPO / "benchmarks/external/human-evaluation.md"),
        "warning": "Report unpaired cases and execution failures, not just completed-pair preferences.",
    })
    emit({"packet": str(destination / "judge-packet.jsonl"), "pairs": len(packet),
          "unpaired_cases": len(unpaired),
          "warning": "Give evaluators only judge-packet.jsonl and the human protocol. Keep private-labels.json and reference-context.jsonl hidden until first-pass judgments are frozen."})


def main():
    with cancellation_signals():
        try:
            return _main()
        except KeyboardInterrupt:
            print("Interrupted; published per-call evidence is preserved for recovery.", file=sys.stderr)
            return 130


def _main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="List pinned sources; no network")
    commands.add_parser("admission", help="Show admitted sources, supported purposes and evidence")
    for name in ("fetch", "verify"):
        sub = commands.add_parser(name)
        sub.add_argument("--source", action="append", help="Repeat for admitted IDs; all includes only admitted sources")
        sub.add_argument("--summary", action="store_true", help="Show counts and failures instead of every verified file")
    sub = commands.add_parser("prepare", help="Normalize a deterministic pilot and separate gold")
    sub.add_argument("--source", required=True)
    sub.add_argument("--batch", required=True)
    sub.add_argument("--limit", type=int, default=3)
    sub.add_argument("--seed", type=int, default=20260904)
    sub = commands.add_parser("run", help="Explicitly invoke a model; uses account/API quota")
    sub.add_argument("--batch", required=True)
    sub.add_argument("--name", required=True)
    sub.add_argument("--model", required=True)
    sub.add_argument("--effort", choices=("minimal", "low", "medium", "high", "xhigh"), default="medium")
    sub.add_argument("--condition", choices=("skill", "no-skill", "both"), default="both")
    sub.add_argument("--limit", type=int, default=1, help="Maximum cases (both makes two calls per case)")
    sub.add_argument("--timeout", type=int, default=180)
    sub.add_argument("--max-prompt-chars", type=int, default=600000)
    sub.add_argument("--codex", default="codex")
    for name in ("report", "score"):
        sub = commands.add_parser(name)
        sub.add_argument("--name", required=True)
    sub = commands.add_parser("export-blind")
    sub.add_argument("--name", required=True)
    sub.add_argument("--seed", type=int, default=20260904)
    args = parser.parse_args()
    try:
        sources = load_registry(REPO)
        if args.command == "list":
            emit([{"id": s["id"], "role": s.get("role"), "adapter": s.get("adapter"),
                   "default_fetch": s.get("default_fetch"), "revision": s.get("revision"),
                   "license": s.get("license"), "admission": s["admission"], "files": len(s.get("files", [])),
                   "bytes": sum(f["size_bytes"] for f in s.get("files", []))} for s in sources.values()])
        elif args.command == "admission":
            emit(read_json(BASE / "admission.json"))
        elif args.command in {"fetch", "verify"}:
            selected = select_sources(sources, args.source)
            results, failed = [], False
            for source in selected:
                try:
                    result = fetch_source(BASE / "cache", source) if args.command == "fetch" else verify_source(BASE / "cache", source)
                    results.append(result)
                    failed |= result["status"] != "verified"
                except (OSError, ValueError) as error:
                    failed = True
                    results.append({"source": source["id"], "status": "failed", "error": str(error)})
            if args.summary:
                results = [{k: v for k, v in result.items() if k != "files"} | {
                    "files": len(result.get("files", [])),
                    "bytes": sum(f["size_bytes"] for f in result.get("files", [])),
                    "file_failures": [f for f in result.get("files", []) if f["status"] != "verified"],
                } for result in results]
            emit(results)
            return int(failed)
        elif args.command == "prepare":
            prepare(args, sources)
        elif args.command == "run":
            return run(args)
        elif args.command == "report":
            report(run_path(args.name))
        elif args.command == "score":
            score(args)
        elif args.command == "export-blind":
            export_blind(args)
        return 0
    except (BenchmarkError, OSError, ValueError, KeyError) as error:
        print("Error: {}".format(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
