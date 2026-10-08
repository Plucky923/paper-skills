"""Fixture amendments preserve the registered scientific task and oracle."""

import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_skills as validator


class TaskInputAuthorityTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.fixtures = self.root / "benchmarks/fixtures"
        shutil.copytree(validator.FIXTURES_ROOT, self.fixtures)
        self.path = self.root / validator.TASK_INPUT_AUTHORITY_PATH
        self.authority = json.loads((validator.REPO_ROOT / validator.TASK_INPUT_AUTHORITY_PATH).read_text())
        self.manifest = {"task_input_authority": validator.TASK_INPUT_AUTHORITY_PATH}

    def entry(self, number):
        return next(item for item in self.authority["records"] if item["number"] == number)

    def check(self):
        self.path.write_text(json.dumps(self.authority, ensure_ascii=False, indent=2) + "\n")
        with patch.object(validator, "REPO_ROOT", self.root), patch.object(validator, "FIXTURES_ROOT", self.fixtures):
            report = validator.Report()
            result = validator.check_task_input_authority(self.manifest, report)
        return report.errors, result

    def amend_current(self, number, change, update_canonical=False):
        entry = self.entry(number)
        path = self.root / entry["path"]
        fixture = json.loads(path.read_text())
        change(fixture)
        path.write_text(json.dumps(fixture, ensure_ascii=False, indent=2) + "\n")
        entry["current_file_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        if update_canonical:
            fields = {key: value for key, value in fixture.items() if key != "prompt"}
            entry["non_prompt_fields_sha256"] = hashlib.sha256(
                json.dumps(fields, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest()

    def test_complete_current_record_and_exact_original_bytes(self):
        manifest = json.loads((validator.REPO_ROOT / "benchmarks/bundle.json").read_text())
        self.assertEqual(manifest.get("task_input_authority"), validator.TASK_INPUT_AUTHORITY_PATH)
        errors, result = self.check()
        self.assertEqual(errors, [])
        self.assertEqual(result["status"], "checked")
        self.assertEqual(result["record_count"], 49)
        self.assertEqual(result["original_byte_checks"], 5)
        self.assertEqual(result["changed_cases"], [13, 16, 17, 18, 40])
        self.assertEqual(result["record_sha256"], hashlib.sha256(self.path.read_bytes()).hexdigest())

    def test_marker_requires_record_but_legacy_bundle_does_not(self):
        with patch.object(validator, "REPO_ROOT", self.root):
            report = validator.Report()
            required = validator.check_task_input_authority(self.manifest, report)
            self.assertTrue(report.errors)
            self.assertEqual(required["status"], "invalid")
            legacy_report = validator.Report()
            legacy = validator.check_task_input_authority({}, legacy_report)
            self.assertEqual(legacy_report.errors, [])
            self.assertEqual(legacy["status"], "legacy_without_marker")

    def test_marker_does_not_authorize_another_path(self):
        self.manifest["task_input_authority"] = "../other.json"
        errors, _ = self.check()
        self.assertTrue(any("must name" in error for error in errors))

    def test_current_prompt_mismatch_rejected_even_with_refreshed_file_hash(self):
        self.amend_current(13, lambda fixture: fixture.update(prompt="Unregistered prompt"))
        errors, _ = self.check()
        self.assertTrue(any("current prompt does not match" in error for error in errors))

    def test_current_raw_byte_hash_mismatch_is_rejected(self):
        path = self.root / self.entry(13)["path"]
        path.write_bytes(path.read_bytes() + b"\n")
        errors, _ = self.check()
        self.assertTrue(any("current fixture SHA mismatch" in error for error in errors))

    def test_oracle_and_scientific_fields_cannot_be_rehashed_into_prompt_amendment(self):
        baseline = json.loads(json.dumps(self.authority))
        for field in ("hard_gates", "rubric", "evidence", "protected_tokens", "scope", "hidden_extra_field"):
            with self.subTest(field=field):
                self.authority = json.loads(json.dumps(baseline))
                path = self.root / self.entry(13)["path"]
                path.write_text(self.entry(13)["original_fixture_text"])
                original = json.loads(path.read_text())
                original["prompt"] = self.entry(13)["current_prompt"]
                path.write_text(json.dumps(original, ensure_ascii=False, indent=2) + "\n")
                self.amend_current(13, lambda fixture: fixture.update({field: "altered"}), update_canonical=True)
                errors, _ = self.check()
                self.assertTrue(any("changed non-prompt fixture fields" in error for error in errors))

    def test_non_prompt_canonical_hash_is_checked(self):
        self.entry(13)["non_prompt_fields_sha256"] = "0" * 64
        errors, _ = self.check()
        self.assertTrue(any("non-prompt canonical SHA mismatch" in error for error in errors))

    def test_unchanged_entry_does_not_hide_a_new_prompt(self):
        self.amend_current(1, lambda fixture: fixture.update(prompt="Unrecorded change"))
        errors, _ = self.check()
        self.assertTrue(any("unrecorded fixture change" in error for error in errors))

    def test_missing_and_duplicate_entries_are_rejected(self):
        original = json.loads(json.dumps(self.authority))
        self.authority["records"].pop()
        self.assertTrue(self.check()[0])
        self.authority = original
        self.authority["records"][-1] = json.loads(json.dumps(self.authority["records"][0]))
        errors, _ = self.check()
        self.assertTrue(any("duplicate fixture authority" in error for error in errors))
        self.assertTrue(any("cover every fixture" in error for error in errors))

    def test_changed_set_and_changed_fields_must_agree(self):
        self.authority["changed_cases"].remove(13)
        self.assertTrue(any("changed_cases does not match" in error for error in self.check()[0]))
        self.authority["changed_cases"].append(13)
        self.entry(13)["changed_fields"].append("hard_gates")
        self.assertTrue(any("permits only prompt" in error for error in self.check()[0]))

    def test_original_prompt_and_original_bytes_are_both_checked(self):
        self.entry(40)["original_prompt"] = "Invented original prompt"
        self.assertTrue(any("original prompt does not match" in error for error in self.check()[0]))
        self.entry(40)["original_prompt"] = json.loads(self.entry(40)["original_fixture_text"])["prompt"]
        self.entry(40)["original_fixture_text"] += "\n"
        self.assertTrue(any("original fixture SHA mismatch" in error for error in self.check()[0]))

    def test_hidden_record_field_and_missing_original_are_rejected(self):
        self.entry(13)["new_authority"] = "not registered"
        self.assertTrue(any("entry fields" in error for error in self.check()[0]))
        del self.entry(13)["new_authority"]
        del self.entry(13)["original_fixture_text"]
        self.assertTrue(any("entry fields" in error for error in self.check()[0]))

    def test_duplicate_json_fields_are_rejected_even_when_original_sha_is_updated(self):
        entry = self.entry(13)
        original = entry["original_fixture_text"]
        entry["original_fixture_text"] = original.replace("{", '{"prompt":"hidden",', 1)
        entry["original_file_sha256"] = hashlib.sha256(entry["original_fixture_text"].encode()).hexdigest()
        errors, _ = self.check()
        self.assertTrue(any("duplicate JSON field" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
