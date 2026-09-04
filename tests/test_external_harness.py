"""Only original synthetic examples; no upstream benchmark answers in tests."""

import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from paperbench.registry import BenchmarkError, digest, fetch_file, inside, load_registry, safe_name, verify_source
from paperbench.runner import build_command, choose_cases, inspect_events, make_prompt, run_one, validate_case, verified_output
import external_benchmarks as cli


def sample(case_id="a", group="g"):
    return {"id": case_id, "source": "synthetic", "group_id": group, "task": "revision",
            "input": {"prompt": "Clarify this paragraph.", "material": {"paragraph": "A test sentence."}, "scope": "Only this paragraph"},
            "reference": "GOLD_MUST_NEVER_REACH_CANDIDATE", "metadata": {"hidden": "META_SECRET"}}


class HarnessTests(unittest.TestCase):
    def test_projection_does_not_leak_gold(self):
        case = sample()
        for condition in ("skill", "no-skill"):
            prompt = make_prompt(case["input"], case["task"], condition, {"SKILL.md": "Short synthetic instruction."})
            self.assertNotIn(case["reference"], prompt)
            self.assertNotIn("META_SECRET", prompt)
            self.assertIn("A test sentence.", prompt)
        self.assertNotIn("Short synthetic instruction.", make_prompt(case["input"], "revision", "no-skill", {"SKILL.md": "Short synthetic instruction."}))

    def test_gold_key_in_input_rejected(self):
        case = sample()
        case["input"]["reference"] = "bad"
        with self.assertRaises(BenchmarkError):
            validate_case(case)

    def test_empty_material_and_identity_rejected(self):
        for field in ("material", "scope"):
            case = sample()
            case["input"][field] = "  "
            with self.assertRaises(BenchmarkError):
                validate_case(case)
        case = sample(group="")
        with self.assertRaises(BenchmarkError):
            validate_case(case)

    def test_output_integrity_before_scoring(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "case"
            path.mkdir()
            output = path / "output.txt"
            output.write_text("Original output")
            result = {"directory": "case", "output_sha256": digest(output)}
            self.assertEqual(verified_output(Path(temp), result), "Original output")
            output.write_text("Edited output")
            with self.assertRaises(BenchmarkError):
                verified_output(Path(temp), result)

    def test_batch_manifest_change_rejected_before_evaluation(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(cli, "BASE", Path(temp)):
            batch = Path(temp) / "work/batch"
            batch.mkdir(parents=True)
            manifest = batch / "manifest.json"
            manifest.write_text('{"original": true}')
            run = Path(temp) / "runs/run"
            run.mkdir(parents=True)
            (run / "manifest.json").write_text(json.dumps({"schema_version": 2, "batch": "batch", "batch_manifest_sha256": digest(manifest)}))
            manifest.write_text('{"original": false}')
            with self.assertRaisesRegex(BenchmarkError, "changed after"):
                cli.evaluation_context(run)

    def test_judge_is_not_writing_skill(self):
        with self.assertRaises(BenchmarkError):
            make_prompt(sample()["input"], "judge_calibration", "skill", {})

    def test_grouped_reproducible_sampling(self):
        cases = [sample("a", "g"), sample("b", "g"), sample("c", "h")]
        selected = choose_cases(cases, 10, 42)
        self.assertEqual(len(selected), 2)
        self.assertEqual(selected, choose_cases(list(reversed(cases)), 10, 42))
        with self.assertRaises(BenchmarkError):
            choose_cases([cases[0], cases[0]], 1, 42)

    def test_path_and_name_safety(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "root"
            root.mkdir()
            (root / "escape").symlink_to(Path(temp))
            for name in ("../x", "/tmp/x", "escape/x", "a\\b"):
                with self.assertRaises(BenchmarkError):
                    inside(root, name)
        for name in ("../x", "/root", "a/b", "", ".", ".."):
            with self.assertRaises(BenchmarkError):
                safe_name(name)

    def test_cached_fetch_and_mismatch_never_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "sample.txt"
            path.write_text("original", encoding="utf-8")
            item = {"path": "sample.txt", "url": "https://example.org/pinned/sample.txt",
                    "sha256": digest(path), "size_bytes": 8}
            with patch("paperbench.registry.urlopen") as network:
                self.assertEqual(fetch_file(Path(temp), item), "cached")
                network.assert_not_called()
            item["sha256"] = "0" * 64
            with self.assertRaises(BenchmarkError):
                fetch_file(Path(temp), item)
            self.assertEqual(path.read_text(), "original")

    def test_verify_missing_is_not_success(self):
        with tempfile.TemporaryDirectory() as temp:
            source = {"id": "test", "revision": "pinned", "files": [
                {"path": "x", "size_bytes": 1, "sha256": "0" * 64}]}
            self.assertEqual(verify_source(Path(temp), source)["status"], "incomplete")

    def test_tool_events_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events.jsonl"
            path.write_text(json.dumps({"type": "item.completed", "item": {"id": "1", "type": "command_execution"}}) + "\n" +
                            json.dumps({"type": "turn.completed", "usage": {"input_tokens": 10}}) + "\n")
            events = inspect_events(path)
            self.assertTrue(events["turn_completed"])
            self.assertEqual(events["unexpected_items"][0]["type"], "command_execution")

    def test_malformed_event_objects_fail_without_crashing_batch(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events.jsonl"
            path.write_text('null\n[]\n{"type": 7}\n{"type":"item.completed","item":null}\n'
                            '{"type":"item.completed","item":{"type":[]}}\n'
                            '{"type":"item.completed","item":{"type":{}}}\n')
            events = inspect_events(path)
            self.assertFalse(events["turn_completed"])
            self.assertEqual(len(events["errors"]), 6)

    @unittest.skipUnless(os.name == "posix", "POSIX process groups")
    def test_timeout_stops_wrapper_and_sigterm_ignoring_child(self):
        with tempfile.TemporaryDirectory() as temp:
            marker = Path(temp) / "orphan-wrote-after-timeout"
            child = ("import pathlib,signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); "
                     "time.sleep(1); pathlib.Path(" + repr(str(marker)) + ").write_text('escaped')")
            wrapper = ("import subprocess,sys,time; subprocess.Popen([sys.executable,'-c'," + repr(child) +
                       "]); time.sleep(60)")
            with patch("paperbench.runner.build_command", return_value=[sys.executable, "-c", wrapper]), \
                    patch("paperbench.runner.disabled_skill_paths", return_value=[]):
                result = run_one(sample(), "no-skill", {}, "fake-model", "medium", sys.executable,
                                 Path(temp) / "run", 0.3, 10000)
            self.assertEqual(result["status"], "failed")
            self.assertTrue(result["timed_out"])
            time.sleep(1.1)
            self.assertFalse(marker.exists(), "A native child survived the bounded run")

    def test_runner_arguments_are_controlled(self):
        command = build_command("codex", "explicit-model", "medium", Path("/tmp/work"), Path("/tmp/out"), ["/tmp/a skill"])
        self.assertIn("--ignore-user-config", command)
        self.assertIn("read-only", command)
        self.assertIn("features.shell_tool=false", command)
        self.assertIn('web_search="disabled"', command)
        self.assertNotIn("--dangerously-bypass-approvals-and-sandbox", command)
        self.assertEqual(command[-1], "-")


if __name__ == "__main__":
    unittest.main()
