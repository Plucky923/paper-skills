#!/usr/bin/env python3
"""Validate STE test packaging and export candidate inputs without judge controls.

This tool neither calls a model nor certifies STE conformance of its output.
"""

import argparse
from copy import deepcopy
import json
from pathlib import Path
import re
import sys

from paperbench.registry import BenchmarkError, inside, read_json, write_json


REPO = Path(__file__).resolve().parents[1]
CASE_FIELDS = {
    "id", "title", "kind", "material_origin", "prompt", "scope", "evidence",
    "protected_tokens", "forbidden_actions", "hard_gates", "expected_behavior", "rubric",
}
CONTROL_LISTS = ("protected_tokens", "forbidden_actions", "hard_gates", "expected_behavior")
OFFICIAL_URL = "https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf"
OFFICIAL_SHA256 = "d1f4ea9e7cd6e46b47aa9057209f99e78c0e9cfc4e27a5b07895b05c1a166431"


def require(condition, message):
    if not condition:
        raise BenchmarkError(message)


def text_tree(value):
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value) and all(text_tree(item) for item in value)
    if isinstance(value, dict):
        return bool(value) and all(isinstance(key, str) and key.strip() and text_tree(item)
                                   for key, item in value.items())
    return False


def string_list(value):
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and item.strip() for item in value)


def validate_single_case(case, authoring=True):
    fields = CASE_FIELDS if authoring else (CASE_FIELDS - {"kind"}) | {"skills"}
    require(isinstance(case, dict) and set(case) == fields, "Invalid STE case fields")
    if authoring:
        require(case["kind"] == "ste-authoring", "Authoring case has the wrong text type")
    else:
        require(case["skills"] == ["systems-paper-revise"], "Invalid manuscript routing")
    require(case["material_origin"] == "synthetic", "STE test material must be synthetic")
    require(isinstance(case["id"], str) and re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case["id"]),
            "Invalid STE case id")
    for field in ("title", "prompt"):
        require(isinstance(case[field], str) and case[field].strip(), "Empty " + field)
    scope = case["scope"]
    require(isinstance(scope, dict) and set(scope) == {"authorized", "excluded", "output_language"},
            "Invalid STE scope")
    require(string_list(scope["authorized"]) and string_list(scope["excluded"])
            and isinstance(scope["output_language"], str) and scope["output_language"].strip(),
            "Empty STE scope")
    require(isinstance(case["evidence"], dict) and text_tree(case["evidence"]), "Invalid evidence")
    for field in CONTROL_LISTS:
        require(string_list(case[field]), "Empty or invalid " + field)
    rubric = case["rubric"]
    require(isinstance(rubric, list) and len(rubric) == 12, "Rubric must have twelve items")
    for number, item in enumerate(rubric, 1):
        require(isinstance(item, dict) and set(item) == {"id", "criterion", "points"}
                and item["id"] == "R" + str(number)
                and isinstance(item["criterion"], str) and item["criterion"].strip()
                and type(item["points"]) is int and item["points"] == 1,
                "Invalid rubric item " + str(number))


def validate_authoring_case(case):
    validate_single_case(case, authoring=True)


def candidate_input(case):
    """Use an allowlist: new evaluator metadata cannot enter the model prompt."""
    return deepcopy({field: case[field] for field in ("prompt", "scope", "evidence")})


def load_authoring(repo=REPO):
    root = Path(repo) / "benchmarks/ste-authoring"
    suite = read_json(root / "suite.json")
    require(suite.get("schema_version") == 1 and suite.get("kind") == "ste-authoring",
            "Invalid STE authoring suite")
    source = suite.get("source", {})
    require(isinstance(source, dict) and source.get("url") == OFFICIAL_URL and source.get("issue") == 9
            and source.get("release_date") == "2025-01-15"
            and source.get("sha256") == OFFICIAL_SHA256, "Unpinned authoring source")
    require(suite.get("minimum_score") == 10 and suite.get("require_all_hard_gates") is True,
            "Invalid authoring acceptance gates")
    filenames = suite.get("cases")
    require(string_list(filenames) and len(filenames) == 6 and len(set(filenames)) == 6,
            "Authoring suite must register six unique cases")
    require(set(filenames) == {path.name for path in (root / "cases").glob("*.json")},
            "Authoring files and registered cases differ")
    cases = []
    ids = set()
    for number, filename in enumerate(filenames, 1):
        path = inside(root / "cases", filename)
        case = read_json(path)
        validate_authoring_case(case)
        require(case["id"].startswith("ste-authoring-")
                and filename == "{:02d}-{}.json".format(number, case["id"][len("ste-authoring-"):]),
                "Authoring filename must match its number and id")
        require(case["id"] not in ids, "Duplicate authoring id")
        ids.add(case["id"])
        cases.append((number, path, case))
    return cases


def load_manuscript(repo=REPO):
    root = Path(repo)
    manifest = read_json(root / "benchmarks/ste-manuscript.json")
    require(manifest.get("schema_version") == 1 and manifest.get("kind") == "ste-manuscript",
            "Invalid STE manuscript registry")
    source = manifest.get("source", {})
    require(isinstance(source, dict) and source.get("url") == OFFICIAL_URL and source.get("issue") == 9
            and source.get("release_date") == "2025-01-15"
            and source.get("sha256") == OFFICIAL_SHA256, "Unpinned manuscript source")
    entries = manifest.get("fixtures")
    require(isinstance(entries, list) and len(entries) == 7, "Register all seven STE manuscript fixtures")
    cases = []
    for number, entry in zip(range(43, 50), entries):
        require(isinstance(entry, dict) and set(entry) == {"path", "rules", "purpose"},
                "Invalid manuscript registry entry")
        path = inside(root, entry["path"])
        case = read_json(path)
        validate_single_case(case, authoring=False)
        require(entry["path"] == "benchmarks/fixtures/{:02d}-{}.json".format(number, case["id"]),
                "Manuscript fixture filename mismatch")
        require(string_list(entry["rules"]) and isinstance(entry["purpose"], str)
                and entry["purpose"].strip(), "Missing rule mapping")
        cases.append((number, path, case))
    return cases


def validate_suites(repo=REPO):
    return len(load_manuscript(repo)), len(load_authoring(repo))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate")
    listing = commands.add_parser("list")
    listing.add_argument("--suite", choices=("manuscript", "authoring"), required=True)
    export = commands.add_parser("export")
    export.add_argument("--suite", choices=("manuscript", "authoring"), required=True)
    export.add_argument("--case", type=int, required=True)
    export.add_argument("--output", type=Path, help="New JSON file; existing files are never replaced")
    args = parser.parse_args(argv)
    try:
        if args.command == "validate":
            manuscript, authoring = validate_suites()
            print("PASS: {} manuscript and {} authoring STE cases; packaging only.".format(manuscript, authoring))
            return 0
        cases = load_manuscript() if args.suite == "manuscript" else load_authoring()
        if args.command == "list":
            for number, _, case in cases:
                print("{:02d} {}".format(number, case["id"]))
            return 0
        selected = [case for number, _, case in cases if number == args.case]
        require(len(selected) == 1, "Case is not registered in this suite")
        payload = candidate_input(selected[0])
        if args.output:
            write_json(args.output, payload)
        else:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0
    except (BenchmarkError, OSError, ValueError, KeyError, TypeError) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
