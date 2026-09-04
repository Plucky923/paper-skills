"""Original synthetic fixtures only: no third-party benchmark text or answers."""

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from paperbench.revision import (
    PARAREV_FILE,
    PARAREVAL_FILE,
    PARAREVAL_SECOND_FILE,
    load_pararev,
    load_parareval,
    pararev_selection_report,
    score_parareval,
)


def pararev_row(paragraph="paperA.versionA.01", paper="paperA"):
    return {
        "id_paragraph": paragraph,
        "id_source": paper,
        "parag_1": "A synthetic queue serves two workers.",
        "parag_2": "AUTHOR_REVISION_REFERENCE_NOT_CANDIDATE_INPUT",
        "annot_1": {
            "annotation": ["Rewriting_light"],
            "instruction": "Improve the wording while preserving its meaning.",
            "annotator": "first synthetic annotator",
        },
        "annot_2": {
            "annotation": ["Concision"],
            "instruction": "Make this paragraph concise without losing any information.",
            "annotator": "second synthetic annotator",
        },
    }


def judgments(preference="A"):
    return {
        "relatedness_A": "Yes strictly",
        "relatedness_B": "Yes with additional modifications",
        "acceptable": "Both",
        "preference": preference,
        "Concision": "A",
        # These are redundant source decisions, not extra scored fields.
        "correctness_A": True,
        "correctness_B": True,
        "extended_choice": "A",
    }


def parareval_row(pairing=1, paragraph="paperA.versionA.01"):
    return {
        "id_pairing": pairing,
        "id_paragraph": paragraph,
        "labels": ["Concision"],
        "original_paragraph": "A synthetic queue serves two workers.",
        "instruction": "State the same fact concisely.",
        "model_A_paragraph": "The synthetic queue serves two workers.",
        "model_B_paragraph": "Two workers use this synthetic queue.",
        "model_A": "GENERATOR_ID_MUST_BE_HIDDEN_A",
        "model_B": "GENERATOR_ID_MUST_BE_HIDDEN_B",
        "pararev_annot": "annot_1",
        "annotator_eval": "HUMAN_ANNOTATOR_MUST_BE_HIDDEN",
        "eval_annotation": judgments(),
        "author_revision": "AUTHOR_REVISION_MUST_BE_HIDDEN",
    }


def prediction():
    return {key: value for key, value in judgments().items()
            if key not in {"correctness_A", "correctness_B", "extended_choice"}}


def reference(second=None):
    annotations = [{"annotator": "first", "origin": "primary", "judgments": judgments()}]
    if second is not None:
        annotations.append({"annotator": "second", "origin": "second_annotation", "judgments": second})
    return {"kind": "human_pairwise_judgments", "human_annotations": annotations}


class RevisionAdaptersTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def write_rows(self, name, rows):
        # Test-generated synthetic files are ephemeral; no downloaded source data.
        (self.root / name).write_text(
            "".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")

    def write_parareval(self, rows, second=()):
        self.write_rows(PARAREVAL_FILE, rows)
        self.write_rows(PARAREVAL_SECOND_FILE, second)

    def test_pararev_preserves_grouping_and_separates_author_reference(self):
        rows = [pararev_row(), pararev_row("paperA.versionA.02")]
        self.write_rows(PARAREV_FILE, rows)
        cases = load_pararev(self.root)
        self.assertEqual(len(cases), 4)
        self.assertEqual(len({case["id"] for case in cases}), 4)
        self.assertEqual({case["group_id"] for case in cases}, {"openreview:paperA"})
        for case in cases:
            serialized_input = json.dumps(case["input"])
            self.assertNotIn("AUTHOR_REVISION_REFERENCE", serialized_input)
            self.assertNotIn("annotator", serialized_input)
            self.assertIn("AUTHOR_REVISION_REFERENCE", case["reference"]["text"])
            self.assertTrue(case["metadata"]["needs_human_semantic_check"])
        report = pararev_selection_report(self.root)
        self.assertEqual(report["selected_paragraphs"], 2)
        self.assertNotIn("synthetic queue", json.dumps(report))

    def test_unsafe_second_annotation_excludes_both_cases(self):
        for field, value, reason in (
            ("annotation", ["Rewriting_light", "Content_change"], "excluded_label"),
            ("instruction", "Remove the failure condition.", "explicit_deletion"),
            ("instruction", "Add a new speedup result.", "explicit_addition"),
            ("instruction", "Correct the latency values.", "protected_content"),
            ("instruction", "Search for more related work.", "external_information"),
        ):
            with self.subTest(field=field, value=value):
                row = pararev_row()
                row["annot_2"][field] = value
                self.write_rows(PARAREV_FILE, [row])
                self.assertEqual(load_pararev(self.root), [])
                report = pararev_selection_report(self.root)
                self.assertEqual(report["excluded_annotation_slots"], 2)
                self.assertTrue(all(any(reason in entry for entry in decision["reasons"])
                                    for decision in report["decisions"]))

    def test_single_instruction_and_missing_annotation_excluded(self):
        for value in (None, {"annotation": ["Concision"], "instruction": ""}):
            with self.subTest(value=value):
                row = pararev_row()
                row["annot_2"] = value
                self.write_rows(PARAREV_FILE, [row])
                self.assertEqual(load_pararev(self.root), [])
                report = pararev_selection_report(self.root)
                self.assertEqual(report["official_two_instruction_paragraphs"], 0)

    def test_pararev_duplicate_ids_and_invalid_schema_rejected(self):
        row = pararev_row()
        self.write_rows(PARAREV_FILE, [row, copy.deepcopy(row)])
        with self.assertRaisesRegex(ValueError, "duplicate paragraph"):
            load_pararev(self.root)
        row["annot_1"]["annotation"] = "Concision"
        self.write_rows(PARAREV_FILE, [row])
        with self.assertRaisesRegex(ValueError, "labels must be a list"):
            load_pararev(self.root)

    def test_129_secondary_annotations_merge_without_adding_tasks(self):
        rows = [parareval_row(index, "paper{}.versionA.01".format(index)) for index in range(130)]
        second = copy.deepcopy(rows[:129])
        for row in second:
            row["annotator_eval"] = "SECOND_HUMAN_ANNOTATOR"
            row["eval_annotation"]["preference"] = "B"
        self.write_parareval(rows, second)
        cases = load_parareval(self.root)
        self.assertEqual(len(cases), 130)
        self.assertEqual(sum(case["metadata"]["secondary_annotation_count"] for case in cases), 129)
        self.assertEqual(sum(len(case["reference"]["human_annotations"]) for case in cases), 259)
        self.assertEqual(cases[0]["reference"]["human_annotations"][1]["judgments"]["preference"], "B")

    def test_parareval_hides_gold_and_models_but_retains_empty_candidate(self):
        first = parareval_row()
        first["model_B_paragraph"] = ""
        second = parareval_row(2)
        self.write_parareval([first, second])
        cases = load_parareval(self.root)
        self.assertEqual({case["group_id"] for case in cases}, {"openreview:paperA"})
        serialized_input = json.dumps(cases[0]["input"])
        for marker in ("GENERATOR_ID", "HUMAN_ANNOTATOR", "AUTHOR_REVISION", "eval_annotation", "extended_choice"):
            self.assertNotIn(marker, serialized_input)
        self.assertEqual(cases[0]["input"]["material"]["revision_B"], "")
        self.assertEqual(cases[0]["metadata"]["empty_candidates"], ["B"])
        self.assertEqual(cases[0]["task"], "judge_calibration")

    def test_parareval_rejects_secondary_mismatch_unknown_and_duplicate(self):
        primary = parareval_row()
        second = copy.deepcopy(primary)
        second["annotator_eval"] = "second"
        mismatched = copy.deepcopy(second)
        mismatched["model_A_paragraph"] = "An unrelated synthetic candidate."
        unknown = copy.deepcopy(second)
        unknown["id_pairing"] = 404
        for secondary, message in (([mismatched], "does not match"), ([unknown], "no primary"),
                                   ([second, second], "duplicate secondary"), ([primary], "repeats the primary")):
            with self.subTest(message=message):
                self.write_parareval([primary], secondary)
                with self.assertRaisesRegex(ValueError, message):
                    load_parareval(self.root)

    def test_parareval_rejects_boolean_ids_malformed_groups_missing_candidates(self):
        for field, value, message in (("id_pairing", True, "must be an integer"),
                                      ("id_paragraph", "not-a-source-id", "derive source-paper"),
                                      ("model_A_paragraph", None, "must be a string")):
            with self.subTest(field=field):
                row = parareval_row()
                row[field] = value
                self.write_parareval([row])
                with self.assertRaisesRegex(ValueError, message):
                    load_parareval(self.root)

    def test_scorer_ignores_derived_fields_and_reports_per_annotator_disagreement(self):
        result = score_parareval(json.dumps(prediction()), reference(judgments(preference="B")))
        self.assertTrue(result["valid"])
        self.assertFalse(result["is_official_metric"])
        self.assertEqual(result["matched_fields"], 9)
        self.assertEqual(result["compared_fields"], 10)
        self.assertEqual(result["field_agreement"], 0.9)
        self.assertEqual(result["empirical_human_agreement_ceiling"], 0.9)
        self.assertEqual(len(result["per_annotation"]), 2)
        self.assertEqual(result["per_annotation"][0]["field_agreement"], 1.0)
        self.assertEqual(result["per_annotation"][1]["field_agreement"], 0.8)
        self.assertTrue(result["per_field"]["preference"]["has_human_disagreement"])
        self.assertEqual(result["per_field"]["preference"]["human_value_counts"], {"A": 1, "B": 1})
        self.assertNotIn("correctness_A", result["per_field"])

    def test_scorer_invalid_json_and_non_objects_have_no_score(self):
        for output in (None, "not JSON", "[]", "null", "```json\n{}\n```", '{"acceptable":"Both","acceptable":"None"}'):
            with self.subTest(output=output):
                result = score_parareval(output, reference())
                self.assertFalse(result["valid"])
                self.assertIsNone(result["field_agreement"])
                self.assertEqual(result["compared_fields"], 0)
                self.assertTrue(result["errors"])

    def test_scorer_missing_extra_wrong_case_and_non_string_fields_rejected(self):
        missing = prediction()
        del missing["preference"]
        extra = dict(prediction(), correctness_A=True)
        wrong_case = dict(prediction(), acceptable="both")
        wrong_type = dict(prediction(), preference=["A"])
        for output in (missing, extra, wrong_case, wrong_type):
            with self.subTest(output=output):
                result = score_parareval(json.dumps(output), reference())
                self.assertFalse(result["valid"])
                self.assertIsNone(result["field_agreement"])

    def test_scorer_rejects_invalid_references(self):
        malformed = reference()
        del malformed["human_annotations"][0]["judgments"]["acceptable"]
        unsupported = reference()
        unsupported["human_annotations"][0]["judgments"]["acceptable"] = "A"
        for value in (None, [], {}, {"kind": "human_pairwise_judgments", "human_annotations": []},
                      malformed, unsupported):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    score_parareval(json.dumps(prediction()), value)


if __name__ == "__main__":
    unittest.main()
