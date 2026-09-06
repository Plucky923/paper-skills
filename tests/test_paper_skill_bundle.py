"""Packaging and attribution invariants, not model writing-quality tests."""

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import validate_skills as validator


class PaperSkillBundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = json.loads((validator.REPO_ROOT / "benchmarks/grill-source.json").read_text())
        self.license = b"synthetic license for isolated validator tests\n"
        self.source["license_sha256"] = hashlib.sha256(self.license).hexdigest()
        self.source_path = self.root / "benchmarks/grill-source.json"
        self.source_path.parent.mkdir(parents=True)
        self.license_path = self.root / "skills/systems-paper-grill/LICENSE"
        self.license_path.parent.mkdir(parents=True)
        self.license_path.write_bytes(self.license)

    def check(self):
        self.source_path.write_text(json.dumps(self.source))
        with patch.object(validator, "REPO_ROOT", self.root):
            report = validator.Report()
            validator.check_grill_sources(report)
        return report

    def test_valid_adaptation_attribution(self):
        self.assertEqual(self.check().errors, [])

    def test_changed_license_is_rejected(self):
        self.license_path.write_bytes(b"changed license")
        self.assertTrue(self.check().errors)

    def test_missing_license_is_rejected(self):
        self.license_path.unlink()
        self.assertTrue(self.check().errors)

    def test_unpinned_upstream_is_rejected(self):
        self.source["commit"] = "main"
        self.assertTrue(self.check().errors)

    def test_missing_adaptation_description_is_rejected(self):
        self.source["adaptation"] = ""
        self.assertTrue(self.check().errors)

    def test_three_self_contained_skill_install_mappings(self):
        mappings = [item for item in validator.EXPECTED_INSTALL_MAPPINGS if item["kind"] == "directory"]
        self.assertEqual({item["source"] for item in mappings}, {
            "skills/systems-paper-review", "skills/systems-paper-revise", "skills/systems-paper-grill"
        })
        self.assertTrue(all(item["source"] == item["install_path"] for item in mappings))


class WorkflowFixtureTests(unittest.TestCase):
    def setUp(self):
        self.path = validator.REPO_ROOT / "benchmarks/fixtures/20-paper-discussion-workflow.json"
        self.fixture = json.loads(self.path.read_text())

    def check(self):
        report = validator.Report()
        validator.check_workflow_case(self.fixture, self.path, report)
        return report.errors

    def test_valid_workflow(self):
        self.assertEqual(self.check(), [])

    def test_missing_stage(self):
        del self.fixture["stage_prompts"]["grill_confirm"]
        self.assertTrue(self.check())

    def test_empty_stage(self):
        self.fixture["stage_prompts"]["revise"] = " "
        self.assertTrue(self.check())

    def test_wrong_skill_order(self):
        self.fixture["skills"].reverse()
        self.assertTrue(self.check())

    def test_unexpected_initial_path(self):
        self.fixture["initial_files"]["../outside.md"] = "not authorized"
        self.assertTrue(self.check())

    def test_empty_initial_file(self):
        self.fixture["initial_files"]["manuscript.md"] = ""
        self.assertTrue(self.check())


class CoverageContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        paths = [
            validator.COVERAGE_CONTRACT_PATH,
            *[f"skills/{skill}/SKILL.md" for skill in validator.EXPECTED_SKILLS],
        ]
        for relative in paths:
            source = validator.REPO_ROOT / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())

    def check(self):
        with patch.object(validator, "REPO_ROOT", self.root):
            report = validator.Report()
            validator.check_coverage_contract(report)
        return report.errors

    def test_valid_contract_and_direct_routes(self):
        self.assertEqual(self.check(), [])

    def test_missing_completion_marker_is_rejected(self):
        path = self.root / validator.COVERAGE_CONTRACT_PATH
        path.write_text(path.read_text().replace("Unreviewed: 0", "Unreviewed: zero"))
        self.assertTrue(self.check())

    def test_missing_promised_role_marker_is_rejected(self):
        path = self.root / validator.COVERAGE_CONTRACT_PATH
        path.write_text(path.read_text().replace("signaled/intended role", "role"))
        self.assertTrue(self.check())

    def test_missing_independent_dimension_marker_is_rejected(self):
        path = self.root / validator.COVERAGE_CONTRACT_PATH
        path.write_text(path.read_text().replace("argument role/organization", "argument"))
        self.assertTrue(self.check())

    def test_missing_reviewer_hypothesis_marker_is_rejected(self):
        path = self.root / validator.COVERAGE_CONTRACT_PATH
        path.write_text(
            path.read_text().replace("reviewer-hypothesized", "reviewer-supplied")
        )
        self.assertTrue(self.check())

    def test_missing_intellectual_move_ledger_is_rejected(self):
        path = self.root / validator.COVERAGE_CONTRACT_PATH
        path.write_text(
            path.read_text().replace(
                "Intellectual-move dependencies", "Central dependencies"
            )
        )
        self.assertTrue(self.check())

    def test_indirect_or_missing_skill_route_is_rejected(self):
        path = self.root / "skills/systems-paper-grill/SKILL.md"
        path.write_text(
            path.read_text().replace(
                "../systems-paper-revise/references/coverage-contract.md",
                "../systems-paper-revise/references/writing-core.md",
            )
        )
        self.assertTrue(self.check())


class InteractiveClarificationContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.paths = [
            "skills/systems-paper-revise/references/review-revise-contract.md",
            "skills/systems-paper-review/SKILL.md",
            "skills/systems-paper-revise/SKILL.md",
            "skills/systems-paper-grill/SKILL.md",
        ]
        for relative in self.paths:
            source = validator.REPO_ROOT / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())

    def check(self):
        with patch.object(validator, "REPO_ROOT", self.root):
            report = validator.Report()
            validator.check_interactive_clarification_contract(report)
        return report.errors

    def test_valid_interactive_contract(self):
        self.assertEqual(self.check(), [])

    def test_missing_author_evidence_class_is_rejected(self):
        path = self.root / "skills/systems-paper-revise/references/review-revise-contract.md"
        path.write_text(path.read_text().replace("`author evidence`", "`missing input`"))
        self.assertTrue(self.check())

    def test_missing_nonterminal_gate_is_rejected(self):
        path = self.root / "skills/systems-paper-revise/SKILL.md"
        path.write_text(
            path.read_text().replace(
                "Do not issue a terminal closure map",
                "Issue a closure map",
            )
        )
        self.assertTrue(self.check())

    def test_missing_same_revision_resume_is_rejected(self):
        path = self.root / "skills/systems-paper-grill/SKILL.md"
        path.write_text(
            path.read_text().replace(
                "resume the same revision automatically",
                "start another revision",
            )
        )
        self.assertTrue(self.check())


class CoverageWorkflowFixtureTests(unittest.TestCase):
    def setUp(self):
        self.path = (
            validator.REPO_ROOT
            / "benchmarks/fixtures/23-coverage-closure-workflow.json"
        )
        self.fixture = json.loads(self.path.read_text())

    def check(self):
        report = validator.Report()
        validator.check_workflow_case(self.fixture, self.path, report)
        return report.errors

    def test_valid_coverage_workflow(self):
        self.assertEqual(self.check(), [])

    def test_coverage_workflow_keeps_all_five_stages(self):
        del self.fixture["stage_prompts"]["rereview"]
        self.assertTrue(self.check())


if __name__ == "__main__":
    unittest.main()
