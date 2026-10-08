"""STE suite packaging and candidate-input isolation, without model calls."""

from contextlib import redirect_stderr, redirect_stdout
from copy import deepcopy
import io
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import ste_benchmarks as ste
from paperbench.registry import BenchmarkError


class STEBenchmarkTests(unittest.TestCase):
    def test_registered_cases_are_valid_and_separate(self):
        self.assertEqual(ste.validate_suites(), (7, 6))
        manuscript = ste.load_manuscript()
        authoring = ste.load_authoring()
        self.assertEqual([number for number, _, _ in manuscript], list(range(43, 50)))
        self.assertEqual([number for number, _, _ in authoring], list(range(1, 7)))
        self.assertTrue(all(case["skills"] == ["systems-paper-revise"] for _, _, case in manuscript))
        self.assertTrue(all("skills" not in case for _, _, case in authoring))

    def test_every_export_hides_evaluator_controls_and_does_not_alias_original(self):
        for _, _, original in ste.load_manuscript() + ste.load_authoring():
            with self.subTest(case=original["id"]):
                case = deepcopy(original)
                for field in set(case) - {"prompt", "scope", "evidence"}:
                    case[field] = "HIDDEN_CONTROL_" + field
                case["future_evaluator_field"] = "HIDDEN_NEW_METADATA"
                payload = ste.candidate_input(case)
                self.assertEqual(set(payload), {"prompt", "scope", "evidence"})
                self.assertNotIn("HIDDEN_", json.dumps(payload))
                payload["scope"]["authorized"].append("new value")
                self.assertNotIn("new value", case["scope"]["authorized"])

    def test_invalid_rubric_or_empty_gate_cannot_pass_packaging(self):
        original = ste.load_authoring()[0][2]
        for mutate in (
            lambda case: case["rubric"].pop(),
            lambda case: case["rubric"][0].update(points=True),
            lambda case: case["rubric"][0].update(id="R2"),
            lambda case: case.update(hard_gates=[]),
            lambda case: case.update(evidence={}),
            lambda case: case.update(skills=["systems-paper-revise"]),
        ):
            case = deepcopy(original)
            mutate(case)
            with self.assertRaises(BenchmarkError):
                ste.validate_authoring_case(case)

    def test_manuscript_export_rejects_incomplete_gates(self):
        case = deepcopy(ste.load_manuscript()[0][2])
        case["hard_gates"] = []
        with self.assertRaises(BenchmarkError):
            ste.validate_single_case(case, authoring=False)

    def test_authoring_source_and_registry_must_match_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            repo = Path(temporary)
            root = repo / "benchmarks/ste-authoring"
            shutil.copytree(ste.REPO / "benchmarks/ste-authoring", root)
            manifest = root / "suite.json"
            original = json.loads(manifest.read_text())
            for mutate in (
                lambda suite: suite["source"].update(sha256="0" * 64),
                lambda suite: suite["cases"].__setitem__(0, "../outside.json"),
                lambda suite: suite["cases"].__setitem__(1, suite["cases"][0]),
                lambda suite: suite.update(require_all_hard_gates=False),
            ):
                suite = deepcopy(original)
                mutate(suite)
                manifest.write_text(json.dumps(suite))
                with self.assertRaises(BenchmarkError):
                    ste.load_authoring(repo)
            manifest.write_text(json.dumps(original))
            (root / "cases/unregistered.json").write_text("{}")
            with self.assertRaises(BenchmarkError):
                ste.load_authoring(repo)

    def test_cli_exports_only_candidate_input_and_preserves_existing_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "input.json"
            with redirect_stdout(io.StringIO()):
                status = ste.main(["export", "--suite", "manuscript", "--case", "48",
                                   "--output", str(output)])
            self.assertEqual(status, 0)
            self.assertEqual(set(json.loads(output.read_text())), {"prompt", "scope", "evidence"})
            before = output.read_bytes()
            with redirect_stderr(io.StringIO()):
                status = ste.main(["export", "--suite", "authoring", "--case", "1",
                                   "--output", str(output)])
            self.assertEqual(status, 1)
            self.assertEqual(output.read_bytes(), before)

    def test_cli_does_not_export_case_from_other_suite(self):
        with redirect_stdout(io.StringIO()) as stdout, redirect_stderr(io.StringIO()):
            self.assertEqual(ste.main(["export", "--suite", "authoring", "--case", "48"]), 1)
        self.assertEqual(stdout.getvalue(), "")


if __name__ == "__main__":
    unittest.main()
