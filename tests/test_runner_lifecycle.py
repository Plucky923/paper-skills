"""Synthetic runner regressions: no network, benchmark text, or model calls."""

from contextlib import redirect_stderr, redirect_stdout
import copy
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import external_benchmarks as cli
from paperbench import registry, runner
from paperbench.registry import BenchmarkError, digest, read_json, stable_hash, write_json


def sample(case_id="a", group="g"):
    return {
        "id": case_id, "source": "synthetic", "task": "revision", "group_id": group,
        "input": {"prompt": "Clarify this sentence.", "material": "One writer appends a record.",
                  "scope": "Only the supplied sentence."},
        "reference": {}, "metadata": {},
    }


@unittest.skipUnless(os.name == "posix", "Runner owns a POSIX process group")
class RunnerLifecycleTests(unittest.TestCase):
    def exercise_child_lifecycle(self, mode):
        with tempfile.TemporaryDirectory(prefix="paperbench-lifecycle-test-") as temporary:
            root = Path(temporary)
            marker, ready = root / "child-escaped", root / "child-ready"
            directory = root / "call"
            output = directory / "output.txt"
            child = (
                "import pathlib,signal,time; "
                "signal.signal(signal.SIGTERM, signal.SIG_IGN); "
                "pathlib.Path(" + repr(str(ready)) + ").write_text('ready'); "
                "time.sleep(0.8); pathlib.Path(" + repr(str(marker)) + ").write_text('escaped')"
            )
            wrapper = (
                "import json,pathlib,subprocess,sys,time\n"
                "subprocess.Popen([sys.executable, '-B', '-c', " + repr(child) + "])\n"
                "deadline = time.monotonic() + 2\n"
                "while not pathlib.Path(" + repr(str(ready)) + ").exists():\n"
                "    if time.monotonic() >= deadline: sys.exit(9)\n"
                "    time.sleep(0.01)\n"
                "sys.stdin.read()\n"
                "pathlib.Path(" + repr(str(output)) + ").write_bytes(b'Synthetic output.\\n')\n"
                "print(json.dumps({'type':'turn.completed'}), flush=True)\n"
                + ("time.sleep(10)\n" if mode in {"timeout", "interrupt"} else "")
                + "sys.exit(" + ("1" if mode == "nonzero" else "0") + ")\n"
            )
            original_popen = subprocess.Popen
            original_sigterm = signal.getsignal(signal.SIGTERM)
            owned = []

            class InterruptedProcess:
                """Raise once like Ctrl-C, then allow the real cleanup to run."""
                def __init__(self, process):
                    self.process = process
                    self.interrupted = False

                def __getattr__(self, name):
                    return getattr(self.process, name)

                def communicate(self, *args, **kwargs):
                    if not self.interrupted:
                        self.interrupted = True
                        deadline = time.monotonic() + 2
                        while not ready.exists() and time.monotonic() < deadline:
                            time.sleep(0.01)
                        raise KeyboardInterrupt
                    return self.process.communicate(*args, **kwargs)

            def track_process(*args, **kwargs):
                process = original_popen(*args, **kwargs)
                owned.append(process)
                return InterruptedProcess(process) if mode == "interrupt" else process

            try:
                with patch.object(runner, "build_command", return_value=[sys.executable, "-B", "-c", wrapper]), \
                        patch.object(runner, "disabled_skill_paths", return_value=[]), \
                        patch.object(runner.subprocess, "Popen", side_effect=track_process):
                    if mode == "interrupt":
                        with self.assertRaises(KeyboardInterrupt):
                            runner.run_one(sample(), "no-skill", {}, "fake", "medium", sys.executable,
                                           directory, 3, 10000)
                    else:
                        timeout = 0.3 if mode == "timeout" else 3
                        result = runner.run_one(sample(), "no-skill", {}, "fake", "medium", sys.executable,
                                                directory, timeout, 10000)
                        self.assertEqual(result["status"], "completed_unscored" if mode == "zero" else "failed")
                        if mode == "timeout":
                            self.assertTrue(result["timed_out"])
                        else:
                            self.assertEqual(result["returncode"], 0 if mode == "zero" else 1)
                self.assertIs(signal.getsignal(signal.SIGTERM), original_sigterm)
                self.assertTrue(ready.exists(), "The synthetic descendant must have installed its signal handler")
                self.assertFalse(marker.exists(), "The child wrote before artifacts were frozen")
                time.sleep(0.9)
                self.assertFalse(marker.exists(), "A descendant survived the completed runner invocation")
            finally:
                # Keep a failing regression test from leaving synthetic orphans.
                for process in owned:
                    try:
                        os.killpg(process.pid, signal.SIGKILL)
                    except ProcessLookupError:
                        pass
                    process.wait(timeout=3)

    def test_zero_exit_stops_sigterm_ignoring_child(self):
        self.exercise_child_lifecycle("zero")

    def test_nonzero_exit_stops_sigterm_ignoring_child(self):
        self.exercise_child_lifecycle("nonzero")

    def test_timeout_stops_sigterm_ignoring_child(self):
        self.exercise_child_lifecycle("timeout")

    def test_interrupt_stops_sigterm_ignoring_child(self):
        self.exercise_child_lifecycle("interrupt")

    def test_crlf_output_hash_and_roundtrip_preserve_bytes(self):
        with tempfile.TemporaryDirectory(prefix="paperbench-crlf-test-") as temporary:
            root = Path(temporary)
            directory = root / "call"
            output = directory / "output.txt"
            original = b"Line one.\r\nLine two.\r\n"
            command = [sys.executable, "-B", "-c",
                       "import json,pathlib,sys; sys.stdin.read(); pathlib.Path(" + repr(str(output)) +
                       ").write_bytes(" + repr(original) +
                       "); print(json.dumps({'type':'turn.completed'}), flush=True)"]
            with patch.object(runner, "build_command", return_value=command), \
                    patch.object(runner, "disabled_skill_paths", return_value=[]):
                result = runner.run_one(sample(), "no-skill", {}, "fake", "medium", sys.executable,
                                        directory, 3, 10000)
            self.assertEqual(result["status"], "completed_unscored")
            self.assertEqual(result["output_sha256"], digest(output))
            result["directory"] = directory.name
            self.assertEqual(runner.verified_output(root, result).encode("utf-8"), original)
            self.assertEqual(result["protocol"], "closed-book-selected-skill-v2")

    def test_outer_sigterm_cleans_child_and_restores_handler(self):
        with tempfile.TemporaryDirectory(prefix="paperbench-sigterm-test-") as temporary:
            root = Path(temporary)
            ready, marker = root / "child.pid", root / "child-escaped"
            child = (
                "import os,pathlib,signal,time; signal.signal(signal.SIGTERM,signal.SIG_IGN); "
                "pathlib.Path(" + repr(str(ready)) + ").write_text(str(os.getpgrp())); "
                "time.sleep(0.8); pathlib.Path(" + repr(str(marker)) + ").write_text('escaped')"
            )
            wrapper = ("import subprocess,sys,time; subprocess.Popen([sys.executable,'-B','-c',"
                       + repr(child) + "]); time.sleep(10)")
            outer = (
                "import signal,sys,tempfile\nfrom pathlib import Path\nfrom unittest.mock import patch\n"
                "tempfile.tempdir = " + repr(str(root)) + "\n"
                "sys.path.insert(0," + repr(str(Path(__file__).resolve().parents[1] / "scripts")) + ")\n"
                "from paperbench.runner import run_one\n"
                "original_handler = signal.getsignal(signal.SIGTERM)\n"
                "try:\n"
                "    with patch('paperbench.runner.build_command',return_value=[sys.executable,'-B','-c',"
                + repr(wrapper) + "]),patch('paperbench.runner.disabled_skill_paths',return_value=[]):\n"
                "        run_one(" + repr(sample()) + ",'no-skill',{},'fake','medium',sys.executable,Path("
                + repr(str(root / "call")) + "),10,10000)\n"
                "except KeyboardInterrupt:\n"
                "    assert signal.getsignal(signal.SIGTERM) == original_handler\n"
                "    sys.exit(73)\n"
            )
            process = subprocess.Popen([sys.executable, "-B", "-c", outer], start_new_session=True,
                                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            child_pid = None
            try:
                deadline = time.monotonic() + 3
                while not ready.exists() and time.monotonic() < deadline:
                    time.sleep(0.01)
                self.assertTrue(ready.exists(), "The synthetic child must start before cancellation")
                child_pid = int(ready.read_text())
                process.terminate()
                process.wait(timeout=3)
                time.sleep(0.9)
                self.assertFalse(marker.exists(), "SIGTERM bypassed owned-process cleanup")
                self.assertEqual(process.returncode, 73, "SIGTERM must become a cleanable interruption")
            finally:
                for pid in (child_pid, process.pid):
                    if pid is not None:
                        try:
                            os.killpg(pid, signal.SIGKILL)
                        except ProcessLookupError:
                            pass
                process.wait(timeout=3)

    def test_cli_sigterm_handler_is_restored_after_cancellation(self):
        original = signal.getsignal(signal.SIGTERM)
        with patch.object(cli, "_main", side_effect=lambda: signal.raise_signal(signal.SIGTERM)), \
                redirect_stderr(io.StringIO()):
            self.assertEqual(cli.main(), 130)
        self.assertIs(signal.getsignal(signal.SIGTERM), original)


class RunnerSamplingAndBundleTests(unittest.TestCase):
    def test_group_order_is_independent_of_case_multiplicity(self):
        base = [sample("base-" + group, group) for group in ("g", "h", "i", "j")]
        expanded = base + [sample("extra-{}".format(index), "g") for index in range(100)]
        for seed in (1, 2, 42, 20260904):
            for limit in (1, 2, 4, 100):
                with self.subTest(seed=seed, limit=limit):
                    expected = [case["group_id"] for case in runner.choose_cases(base, limit, seed)]
                    actual = [case["group_id"] for case in runner.choose_cases(expanded, limit, seed)]
                    self.assertEqual(actual, expected)
                    self.assertEqual(runner.choose_cases(expanded, limit, seed),
                                     runner.choose_cases(list(reversed(expanded)), limit, seed))

    def test_revision_bundle_contains_only_selected_skill_markdown(self):
        repo = Path(__file__).resolve().parents[1]
        bundle = runner.snapshot_bundle(repo, "revision")
        expected = {path.relative_to(repo).as_posix()
                    for path in (repo / "skills/systems-paper-revise").rglob("*.md")}
        self.assertEqual(set(bundle), expected)
        self.assertIn("skills/systems-paper-revise/SKILL.md", bundle)
        self.assertEqual(runner.snapshot_bundle(repo), bundle)

    def test_judge_bundle_is_empty_without_reading_skill_files(self):
        with patch.object(Path, "read_text", side_effect=AssertionError("Judge must not read skills")):
            self.assertEqual(runner.snapshot_bundle(Path("/not-a-repository"), "judge_calibration"), {})

    def test_unadmitted_tasks_cannot_load_a_bundle_or_construct_a_prompt(self):
        repo = Path(__file__).resolve().parents[1]
        for task in ("review", "review_critique", "compose", "unknown"):
            with self.subTest(task=task):
                with self.assertRaises(BenchmarkError):
                    runner.snapshot_bundle(repo, task)
                with self.assertRaises(BenchmarkError):
                    runner.make_prompt(sample()["input"], task, "no-skill", {})


class AtomicEvidenceTests(unittest.TestCase):
    def test_interrupted_json_serialization_publishes_no_partial_record(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "result.json"

            def interrupt_dump(value, handle, **kwargs):
                handle.write('{"partial":')
                raise KeyboardInterrupt

            with patch.object(registry.json, "dump", side_effect=interrupt_dump):
                with self.assertRaises(KeyboardInterrupt):
                    write_json(path, {"complete": True})
            self.assertFalse(path.exists())
            self.assertEqual(list(Path(temporary).iterdir()), [])

    def test_json_publication_preserves_existing_destination(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "result.json"
            write_json(path, {"original": True})
            original = path.read_bytes()
            with self.assertRaises(FileExistsError):
                write_json(path, {"replacement": True})
            self.assertEqual(path.read_bytes(), original)
            self.assertEqual(list(Path(temporary).iterdir()), [path])


class RecoveryBoundaryTests(unittest.TestCase):
    def setUp(self):
        # Reuse the original synthetic admitted-batch fixture, not corpus data.
        import test_admission_and_runs as fixtures
        self.fixture = fixtures.DurableRunTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)

    def test_recovery_rejects_existing_conditions_outside_shrunken_schedule(self):
        fixture = self.fixture
        for index in range(4):
            fixture.record(index)
        controls = copy.deepcopy(fixture.controls)
        controls.update(condition="no-skill", calls=2,
                        schedule=cli.run_schedule(fixture.cases, ["no-skill"]))
        original_read = cli.read_json

        def changed_manifest(path):
            return controls if Path(path) == fixture.run_path / "manifest.json" else original_read(path)

        with patch.object(cli, "read_json", side_effect=changed_manifest):
            with self.assertRaisesRegex(BenchmarkError, "outside.*schedule|Unexpected.*evidence"):
                cli.evaluation_context(fixture.run_path)

    def test_interrupt_after_result_publication_preserves_result_without_failure(self):
        fixture = self.fixture
        args = SimpleNamespace(batch="synthetic", limit=2, timeout=10, codex=sys.executable,
                               condition="both", name="published-interrupted", model="synthetic-no-inference",
                               effort="medium", max_prompt_chars=10000)
        calls = [0]

        def publish_then_interrupt(case, condition, bundle, model, effort, binary, directory, timeout, max_chars):
            calls[0] += 1
            result = {"case_id": case["id"], "source": case["source"], "task": case["task"],
                      "condition": condition, "input_sha256": stable_hash(case["input"]),
                      "status": "completed_unscored", "elapsed_seconds": 0, "diagnostics": {}}
            write_json(directory / "result.json", result)
            if calls[0] == 2:
                raise KeyboardInterrupt
            return result

        with patch.object(cli, "run_one", side_effect=publish_then_interrupt), \
                patch.object(cli, "snapshot_bundle", return_value={}), redirect_stdout(io.StringIO()):
            self.assertEqual(cli.run(args), 130)
            report = cli.report(fixture.base / "runs/published-interrupted")
        call = fixture.base / "runs/published-interrupted/0000-skill"
        self.assertEqual(read_json(call / "result.json")["status"], "completed_unscored")
        self.assertFalse((call / "failure.json").exists())
        self.assertEqual(report["completed_unscored"], 2)
        self.assertEqual(report["failed"], 0)
        self.assertEqual(report["unfinished_calls"], 2)


if __name__ == "__main__":
    unittest.main()
