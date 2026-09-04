"""Blind human packets contain original synthetic examples, not upstream labels."""

from contextlib import redirect_stdout
import io
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import external_benchmarks as cli
from paperbench.registry import BenchmarkError, digest, read_json, read_jsonl, stable_hash


class BlindExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.base_patch = patch.object(cli, "BASE", self.root)
        self.base_patch.start()
        self.run = self.root / "runs/synthetic"
        self.run.mkdir(parents=True)
        self.case = {
            "id": "synthetic-one", "task": "revision", "source": "pararev",
            "input": {"prompt": "Clarify this paragraph.",
                      "material": "The synthetic system retries once.", "scope": "Only this paragraph."},
            "reference": {"text": "HIDDEN_AUTHOR_REFERENCE", "kind": "context_only"},
        }
        self.results = []
        for condition in ("skill", "no-skill"):
            directory = self.run / ("0000-" + condition)
            directory.mkdir()
            output = directory / "output.txt"
            output.write_text("A synthetic output for " + condition, encoding="utf-8")
            self.results.append({"case_id": self.case["id"], "condition": condition,
                                 "status": "completed_unscored", "directory": directory.name,
                                 "input_sha256": stable_hash(self.case["input"]),
                                 "output_sha256": digest(output)})

    def tearDown(self):
        self.base_patch.stop()
        self.temp.cleanup()

    def export(self, cases=None, results=None, condition="both"):
        cases = [self.case] if cases is None else cases
        results = self.results if results is None else results
        controls = {"cases": len(cases), "condition": condition}
        with patch.object(cli, "evaluation_context", return_value=(controls, cases, results)), \
                redirect_stdout(io.StringIO()):
            cli.export_blind(SimpleNamespace(name="synthetic", seed=42))

    def test_first_pass_hides_reference_and_condition_mapping(self):
        self.export()
        packet = read_jsonl(self.run / "blind/judge-packet.jsonl")[0]
        self.assertNotIn("reference_context", packet)
        self.assertNotIn("HIDDEN_AUTHOR_REFERENCE", str(packet))
        self.assertIn("unresolved", packet["allowed_gate_values"])
        self.assertIn("unresolved", packet["allowed_preferences"])
        self.assertIn("no fixed word count", packet["rubric"]["concision"])
        references = read_jsonl(self.run / "blind/reference-context.jsonl")
        self.assertEqual(references[0]["reference_context"]["text"], "HIDDEN_AUTHOR_REFERENCE")
        labels = read_json(self.run / "blind/private-labels.json")["labels"][0]
        self.assertEqual({labels["A"], labels["B"]}, {"skill", "no-skill"})
        summary = read_json(self.run / "blind/export-summary.json")
        self.assertEqual(summary["human_protocol_sha256"], digest(cli.REPO / "benchmarks/external/human-evaluation.md"))

    def test_unfinished_pairs_remain_in_export_denominator(self):
        self.export(cases=[self.case, dict(self.case, id="synthetic-two")])
        summary = read_json(self.run / "blind/export-summary.json")
        self.assertEqual(summary["scheduled_cases"], 2)
        self.assertEqual(summary["exported_pairs"], 1)
        self.assertEqual(summary["unpaired_cases"], [{"id": "synthetic-two", "reason": "failed_or_unfinished_pair"}])

    def test_no_completed_pair_does_not_create_a_packet(self):
        with self.assertRaisesRegex(BenchmarkError, "No completed"):
            self.export(results=[])
        self.assertFalse((self.run / "blind").exists())

    def test_one_condition_cannot_be_exported_as_a_comparison(self):
        with self.assertRaisesRegex(BenchmarkError, "paired"):
            self.export(condition="skill")
        self.assertFalse((self.run / "blind").exists())


if __name__ == "__main__":
    unittest.main()
