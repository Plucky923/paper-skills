"""Admission and durable-result contracts; original synthetic text only."""

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import external_benchmarks as cli
from paperbench.registry import BenchmarkError, digest, load_registry, select_sources, stable_hash, write_json, write_jsonl


def case(case_id="one"):
    return {"id": case_id, "source": "pararev", "task": "revision", "group_id": "group-" + case_id,
            "input": {"prompt": "Clarify this paragraph.", "material": "The synthetic system retries once.",
                      "scope": "Only this paragraph."},
            "reference": {"author_revision": "Synthetic reference, never a candidate input."}, "metadata": {}}


class AdmissionTests(unittest.TestCase):
    def test_only_two_evidence_aligned_sources_are_active(self):
        sources = load_registry(cli.REPO)
        self.assertEqual(set(sources), {"pararev", "parareval"})
        self.assertEqual({s["id"] for s in select_sources(sources, ["all"])}, set(sources))
        self.assertEqual(sources["parareval"]["admission"]["task"], "judge_calibration")
        with self.assertRaises(BenchmarkError):
            select_sources(sources, ["unadmitted-synthetic"])

    def test_unadmitted_source_blocked_before_any_model_launch(self):
        with patch.object(cli, "load_batch", return_value=({"source": "unadmitted-synthetic"}, [])), \
                patch.object(cli, "run_one") as model:
            with self.assertRaisesRegex(BenchmarkError, "not admitted"):
                cli.run(SimpleNamespace(batch="unadmitted-batch"))
            model.assert_not_called()

    def test_admission_and_task_mismatched_batches_are_blocked(self):
        source = load_registry(cli.REPO)["pararev"]
        manifest = {"source": "pararev", "source_registry_sha256": stable_hash(source)}
        for admission_hash in (None, "mismatched-synthetic"):
            manifest["admission_sha256"] = admission_hash
            with self.subTest(admission_hash=admission_hash):
                with self.assertRaisesRegex(BenchmarkError, "Batch admission does not match"):
                    cli.require_admitted_batch(manifest, [case()])
        manifest["admission_sha256"] = stable_hash(source["admission"])
        changed = case()
        changed["task"] = "judge_calibration"
        with self.assertRaisesRegex(BenchmarkError, "purpose"):
            cli.require_admitted_batch(manifest, [changed])


class DurableRunTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.base = Path(self.temp.name)
        self.patch = patch.object(cli, "BASE", self.base)
        self.patch.start()
        self.cases = [case("one"), case("two")]
        self.source = load_registry(cli.REPO)["pararev"]
        batch = self.base / "work/synthetic"
        write_jsonl(batch / "inputs.jsonl", [{k: c[k] for k in ("id", "source", "task", "group_id", "input")} for c in self.cases])
        write_jsonl(batch / "references.jsonl", [{k: c[k] for k in ("id", "reference", "metadata")} for c in self.cases])
        self.batch_manifest = {
            "source": "pararev", "source_registry_sha256": stable_hash(self.source),
            "admission_sha256": stable_hash(self.source["admission"]),
            "files": {name: digest(batch / name) for name in ("inputs.jsonl", "references.jsonl")},
        }
        write_json(batch / "manifest.json", self.batch_manifest)
        self.run_path = self.base / "runs/synthetic"
        self.controls = {
            "schema_version": 2, "batch": "synthetic", "source": "pararev", "cases": 2,
            "condition": "both", "calls": 4,
            "schedule": cli.run_schedule(self.cases, ["no-skill", "skill"]),
            "batch_manifest_sha256": digest(batch / "manifest.json"),
            "admission_sha256": stable_hash(self.source["admission"]),
        }
        write_json(self.run_path / "manifest.json", self.controls)

    def tearDown(self):
        self.patch.stop()
        self.temp.cleanup()

    def record(self, index=0, **changes):
        expected = self.controls["schedule"][index]
        result = {k: expected[k] for k in ("case_id", "source", "task", "condition", "input_sha256")}
        result.update(status="completed_unscored", elapsed_seconds=0, diagnostics={})
        result.update(changes)
        write_json(self.run_path / expected["directory"] / "result.json", result)
        return dict(result, directory=expected["directory"])

    def test_missing_aggregate_recovers_completed_prefix_without_writing(self):
        expected = self.record()
        _, _, results = cli.evaluation_context(self.run_path)
        self.assertEqual(results, [expected])
        self.assertFalse((self.run_path / "results.json").exists())
        with redirect_stdout(io.StringIO()):
            report = cli.report(self.run_path)
        self.assertEqual(report["calls"], 1)
        self.assertEqual(report["unfinished_calls"], 3)

    def test_report_score_and_export_reject_unsupported_run_schema(self):
        actions = {
            "report": lambda: cli.report(self.run_path),
            "score": lambda: cli.score(SimpleNamespace(name="synthetic")),
            "export": lambda: cli.export_blind(SimpleNamespace(name="synthetic", seed=1)),
        }
        for controls in ({}, {"schema_version": 999}):
            for name, action in actions.items():
                with self.subTest(controls=controls, command=name), \
                        patch.object(cli, "read_json", return_value=controls) as read, \
                        patch.object(cli, "load_batch") as batch, \
                        patch.object(cli, "run_one") as model:
                    with self.assertRaisesRegex(BenchmarkError, "Unsupported run schema"):
                        action()
                    read.assert_called_once_with(self.run_path / "manifest.json")
                    batch.assert_not_called()
                    model.assert_not_called()

    def test_duplicate_or_condition_modified_aggregate_rejected(self):
        original = self.record()
        corrupted = dict(original, condition="skill")
        write_json(self.run_path / "results.json", [corrupted, corrupted])
        with self.assertRaisesRegex(BenchmarkError, "Aggregate"):
            cli.evaluation_context(self.run_path)

    def test_dropped_aggregate_row_rejected_against_per_call_evidence(self):
        self.record()
        write_json(self.run_path / "results.json", [])
        with self.assertRaisesRegex(BenchmarkError, "Aggregate"):
            cli.evaluation_context(self.run_path)

    def test_per_call_identity_change_rejected(self):
        self.record(condition="skill")
        with self.assertRaisesRegex(BenchmarkError, "schedule"):
            cli.evaluation_context(self.run_path)

    def test_evidence_gap_rejected(self):
        self.record(index=1)
        with self.assertRaisesRegex(BenchmarkError, "gap"):
            cli.evaluation_context(self.run_path)

    def test_schedule_cannot_be_relabelled_by_manifest_alone(self):
        self.controls["condition"] = "no-skill"
        with patch.object(cli, "read_json", side_effect=lambda path: self.controls if path.name == "manifest.json" and path.parent == self.run_path else json.loads(path.read_text())):
            with self.assertRaisesRegex(BenchmarkError, "schedule"):
                cli.evaluation_context(self.run_path)

    def test_keyboard_interrupt_preserves_prior_calls_and_records_failure(self):
        args = SimpleNamespace(batch="synthetic", limit=2, timeout=10, codex=sys.executable,
                               condition="both", name="interrupted", model="synthetic-no-inference",
                               effort="medium", max_prompt_chars=10000)
        count = [0]

        def fake_run(case, condition, bundle, model, effort, binary, directory, timeout, max_chars):
            count[0] += 1
            if count[0] == 2:
                raise KeyboardInterrupt()
            result = {"case_id": case["id"], "source": case["source"], "task": case["task"],
                      "condition": condition, "input_sha256": stable_hash(case["input"]),
                      "status": "completed_unscored", "elapsed_seconds": 0, "diagnostics": {}}
            write_json(directory / "result.json", result)
            return result

        with patch.object(cli, "run_one", side_effect=fake_run), \
                patch.object(cli, "snapshot_bundle", return_value={}), redirect_stdout(io.StringIO()):
            code = cli.run(args)
            report = cli.report(self.base / "runs/interrupted")
        self.assertEqual(code, 130)
        self.assertEqual(report["completed_unscored"], 1)
        self.assertEqual(report["failed"], 1)
        self.assertEqual(report["unfinished_calls"], 2)
        self.assertEqual(count[0], 2)


if __name__ == "__main__":
    unittest.main()
