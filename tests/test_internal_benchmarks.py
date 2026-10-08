"""Synthetic runner checks; these do not make model-quality claims."""

import argparse
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import internal_benchmarks as runner
from benchmark_access_server import AccessServer
from paperbench.registry import BenchmarkError


REPO = Path(__file__).resolve().parents[1]
UUID = "d4559c5c-79fb-489f-aa72-ed32f9c7ce00"


def fixture(number):
    return json.loads(next((REPO / "benchmarks/fixtures").glob("{:02d}-*.json".format(number))).read_text())


class InternalRunnerTests(unittest.TestCase):
    def test_selection_defaults_ranges_and_invalid(self):
        self.assertEqual(runner.select_cases("all", {1, 2, 3}), [1, 2, 3])
        self.assertEqual(runner.select_cases("1,3-5,4", set(range(1, 6))), [1, 3, 4, 5])
        for expression in ("", "2-1", "1;2", "6"):
            with self.assertRaises(BenchmarkError):
                runner.select_cases(expression, set(range(1, 6)))

    def test_projection_hides_judge_fields_and_cold_review_hints(self):
        case = fixture(32)
        case["rubric"] = "HIDDEN_GOLD"
        case["expected_behavior"] = "HIDDEN_EXPECTED"
        case["evidence"]["visible_structure"] = "HIDDEN_COLD_STRUCTURE"
        projected = runner.candidate_input(case, 32)
        self.assertEqual(set(projected), {"prompt", "scope", "evidence"})
        text = json.dumps(projected)
        for hidden in ("HIDDEN_GOLD", "HIDDEN_EXPECTED", "HIDDEN_COLD_STRUCTURE"):
            self.assertNotIn(hidden, text)
        self.assertIn("visible_structure", case["evidence"])

    def test_workflow_future_facts_only_arrive_with_author_reply(self):
        for number in (23, 39):
            case = fixture(number)
            case["evidence"]["confirmed_after_grill"] = ["HIDDEN_FUTURE_FACT"]
            case["evidence"]["required_findings"] = ["HIDDEN_FINDING"]
            for stage in runner.STAGES:
                text = json.dumps(runner.candidate_input(case, number, stage, Path("/tmp/project")))
                self.assertNotIn("HIDDEN_FINDING", text)
                self.assertEqual("HIDDEN_FUTURE_FACT" in text, stage in ("grill_confirm", "revise", "rereview"))
                self.assertNotIn("{project}", text)
            if number == 39:
                self.assertIn("historical_initial_context", runner.candidate_input(case, number, "revise")["evidence"])
        case = fixture(20)
        expected = dict(case["evidence"])
        case["evidence"]["future_author_reply"] = "HIDDEN_FUTURE_FACT"
        for stage in runner.STAGES:
            self.assertEqual(runner.candidate_input(case, 20, stage)["evidence"], expected)

    def test_inline_cases_have_no_automatic_followup(self):
        for number in (18, 19, 22, 29, 35, 38, 40):
            projected = runner.candidate_input(fixture(number), number)
            self.assertEqual(set(projected), {"prompt", "scope", "evidence"})
            self.assertIn("prompt", projected)
        prompt = runner.make_prompt(runner.candidate_input(fixture(19), 19), {}, "manuscript")
        self.assertIn(b"ask and stop; do not invent the reply", prompt)

    def test_handoff_bytes_are_exact_and_separate(self):
        raw = "第一阶段\r\n  exact whitespace \n\n".encode()
        payload = {"prompt": "Use the preceding review", "scope": {}, "evidence": {}}
        prompt = runner.make_prompt(payload, {}, "manuscript", mode="venue", handoff=raw)
        self.assertIn(b"<stage_1_output>\n" + raw + b"\n</stage_1_output>", prompt)
        self.assertNotIn("stage_1_output", payload)

    def test_tool_flags_and_grill_resume_uuid(self):
        args = ("codex", "fixed-model", "high", Path("/tmp/project"), Path("/tmp/output"), [])
        text = runner.invocation_command(*args)
        self.assertIn("--ignore-user-config", text)
        self.assertIn("--ephemeral", text)
        self.assertIn("features.shell_tool=false", text)
        self.assertIn("features.view_image=false", text)
        self.assertNotIn("tools.view_image=false", text)
        self.assertIn("features.skip_host_skill_discovery=true", text)
        self.assertIn("features.code_mode_host=false", text)
        self.assertIn('web_search="disabled"', text)
        review = runner.invocation_command(*args, mode="workflow", stage="review")
        self.assertIn("features.shell_tool=true", review)
        self.assertIn("features.code_mode_host=true", review)
        self.assertIn("features.code_mode=false", review)
        self.assertIn("features.code_mode_only=false", review)
        self.assertEqual(review[review.index("--sandbox") + 1], "read-only")
        opened = runner.invocation_command(*args, mode="workflow", stage="grill_open")
        self.assertNotIn("--ephemeral", opened)
        self.assertEqual(opened[opened.index("--sandbox") + 1], "workspace-write")
        resumed = runner.invocation_command(*args, mode="workflow", stage="grill_confirm", resume=UUID)
        self.assertEqual(resumed[-3:], ["resume", UUID, "-"])
        self.assertNotIn("--last", resumed)
        self.assertNotIn("--ephemeral", resumed)
        for invalid in (None, "--last", "some-thread-name"):
            with self.assertRaises(BenchmarkError):
                runner.invocation_command(*args, mode="workflow", stage="grill_confirm", resume=invalid)
        venue = runner.invocation_command(*args, mode="venue", stage="review")
        self.assertIn('web_search="live"', venue)
        self.assertIn("features.shell_tool=false", venue)
        self.assertIn("features.unified_exec=false", venue)
        self.assertIn("features.code_mode_host=true", venue)
        self.assertIn("features.code_mode=false", venue)
        self.assertIn("features.code_mode_only=false", venue)

    def test_event_parser_uuid_and_unexpected_actions_fail_closed(self):
        events = [{"type": "thread.started", "thread_id": UUID},
                  {"type": "item.completed", "item": {"type": "command_execution", "command": "cat manuscript.md"}},
                  {"type": "turn.completed", "usage": {"input_tokens": 2}}]
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events.jsonl"
            path.write_text("\n".join(json.dumps(event) for event in events))
            text = runner.parse_events(path, "text")
            self.assertEqual(text["thread_uuid"], UUID)
            self.assertIn("unexpected_tool:command_execution", text["event_errors"])
            workflow = runner.parse_events(path, "workflow")
            self.assertFalse(workflow["event_errors"])
            self.assertEqual(workflow["tool_audit"], [events[1]])
            self.assertIn("not a complete", workflow["access_audit_limit"])
            path.write_text('{"type":"thread.started","thread_id":"bad"}\n{"type":"error"}')
            errors = runner.parse_events(path, "workflow")["event_errors"]
            self.assertIn("invalid_thread_uuid", errors)
            self.assertIn("error", errors)

    def test_known_runtime_warning_is_retained_separately(self):
        warning = {"type": "item.completed", "item": {"type": "error", "message": next(iter(runner.KNOWN_RUNTIME_WARNINGS))}}
        unknown = {"type": "item.completed", "item": {"type": "error", "message": "Unknown failure"}}
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events.jsonl"
            path.write_text(json.dumps(warning))
            result = runner.parse_events(path, "text")
            self.assertEqual(result["runtime_warnings"], [warning])
            self.assertFalse(result["tool_audit"])
            self.assertFalse(result["event_errors"])
            path.write_text(json.dumps(unknown))
            self.assertIn("unexpected_tool:error", runner.parse_events(path, "text")["event_errors"])

    def test_exact_skill_discovery_startup_warning_is_not_a_candidate_action(self):
        template = ("Under-development features enabled: skip_host_skill_discovery. "
                    "Under-development features are incomplete and may behave unpredictably. "
                    "To suppress this warning, set `suppress_unstable_features_warning = true` "
                    "in {home}/.codex/config.toml.")
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events.jsonl"
            for home in ("/Users/plucky", "/home/synthetic-user", "/root"):
                warning = {"type": "item.completed", "item": {"type": "error", "message": template.format(home=home)}}
                path.write_text(json.dumps(warning))
                result = runner.parse_events(path, "text")
                self.assertEqual(result["runtime_warnings"], [warning])
                self.assertFalse(result["tool_audit"])
                self.assertFalse(result["event_errors"])
            for message in (template.format(home="/root").replace("skip_host_skill_discovery", "another_feature"),
                            template.format(home="/root") + " Additional failure.", "Unknown startup error"):
                event = {"type": "item.completed", "item": {"type": "error", "message": message}}
                path.write_text(json.dumps(event))
                result = runner.parse_events(path, "text")
                self.assertFalse(result["runtime_warnings"])
                self.assertIn("unexpected_tool:error", result["event_errors"])

    def test_actual_call_retains_evidence_and_refuses_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp) / "case"
            output_text = "Corrected sentence.\n"
            def fake_command(*args, **kwargs):
                output = args[4]
                script = "import json,pathlib;pathlib.Path({!r}).write_text({!r});print(json.dumps({{'type':'turn.completed','usage':{{'input_tokens':3}}}}))".format(str(output), output_text)
                return [sys.executable, "-c", script]
            instance = runner.InvocationRunner("unused", "fixed", "high", 10, [])
            with patch.object(runner, "invocation_command", side_effect=fake_command):
                result = instance.call(directory, {"prompt": "Revise", "scope": {}, "evidence": {}}, {}, "manuscript")
            self.assertEqual(result["status"], "completed_unscored")
            self.assertEqual((directory / "output.txt").read_text(), output_text)
            self.assertTrue((directory / "invocation.json").is_file())
            self.assertIn("events.jsonl", result["artifact_sha256"])
            with self.assertRaises(FileExistsError):
                instance.call(directory, {}, {}, "manuscript")
            self.assertEqual((directory / "output.txt").read_text(), output_text)

    def test_failed_call_retains_result_without_retry(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp) / "case"
            instance = runner.InvocationRunner("missing", "fixed", "high", 10, [])
            with patch.object(runner, "invocation_command", return_value=["/definitely-missing-cli"]):
                result = instance.call(directory, {"prompt": "Revise", "scope": {}, "evidence": {}}, {}, "manuscript")
            self.assertEqual(result["status"], "failed")
            self.assertIn("FileNotFoundError", result["invocation_error"])
            self.assertEqual(json.loads((directory / "result.json").read_text())["status"], "failed")

    def test_wall_deadline_expires_even_when_monotonic_clock_is_suspended(self):
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp) / "case"
            instance = runner.InvocationRunner("unused", "fixed", "high", 10, [])
            with patch.object(runner, "invocation_command", return_value=[sys.executable, "-c", "import time; time.sleep(30)"]), \
                    patch.object(runner.time, "monotonic", return_value=0.0), \
                    patch.object(runner.time, "time", side_effect=[100.0, 200.0, 200.0]):
                result = instance.call(directory, {"prompt": "task", "scope": {}, "evidence": {}}, {}, "manuscript")
            self.assertEqual(result["status"], "failed")
            self.assertTrue(result["timed_out"])
            self.assertTrue(result["wall_budget_exceeded"])
            self.assertEqual(result["elapsed_seconds"], 100.0)
            self.assertEqual(result["monotonic_elapsed_seconds"], 0.0)

    def test_project_snapshots_detect_unauthorized_mutations(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            project = root / "project"
            project.mkdir()
            (project / "manuscript.md").write_bytes(b"original\r\n")
            before = runner.snapshot_project(project, root / "before")
            (project / "manuscript.md").write_bytes(b"revised\n")
            after = runner.snapshot_project(project, root / "after")
            changed, violations = runner.project_changes(before, after, "review")
            self.assertEqual(changed, ["manuscript.md"])
            self.assertEqual(violations, ["unauthorized_project_change:manuscript.md"])
            self.assertEqual(runner.project_changes(before, after, "revise")[1], [])
            self.assertEqual((root / "before/manuscript.md").read_bytes(), b"original\r\n")

    def test_five_stage_workflow_harness_publishes_review_and_resumes(self):
        class FakeRunner:
            calls = []
            def call(self, directory, payload, documents, suite, **kwargs):
                directory.mkdir()
                stage = kwargs["stage"]
                self.calls.append((stage, payload, kwargs))
                (directory / "output.txt").write_bytes(b"Complete review\r\n" if stage == "review" else b"response\n")
                return {"status": "completed_unscored", "stage": stage, "thread_uuid": UUID if stage == "grill_open" else None}
        with tempfile.TemporaryDirectory() as temp:
            fake = FakeRunner()
            result = runner.run_case(23, fixture(23), Path(temp) / "case", fake, {}, "manuscript")
            self.assertEqual(result["status"], "completed_unscored")
            self.assertEqual([entry[0] for entry in fake.calls], list(runner.STAGES))
            self.assertEqual(fake.calls[2][2]["resume"], UUID)
            self.assertEqual((Path(temp) / "case/project/review.md").read_bytes(), b"Complete review\r\n")
            self.assertNotIn("confirmed_after_grill", fake.calls[1][1]["evidence"])

    def test_venue_two_fresh_stages_handoff(self):
        class FakeRunner:
            calls = []
            def call(self, directory, payload, documents, suite, **kwargs):
                directory.mkdir()
                self.calls.append(kwargs)
                (directory / "output.txt").write_bytes(b"full review\r\n\n")
                return {"status": "completed_unscored", "stage": kwargs["stage"]}
        with tempfile.TemporaryDirectory() as temp:
            fake = FakeRunner()
            runner.run_case(12, fixture(12), Path(temp) / "case", fake, {}, "manuscript")
            self.assertIsNone(fake.calls[0]["handoff"])
            self.assertEqual(fake.calls[1]["handoff"], b"full review\r\n\n")
            self.assertNotIn("resume", fake.calls[1])

    def test_frozen_authoring_supplies_only_selected_guidance(self):
        documents = runner.frozen_documents(REPO, "authoring")
        self.assertEqual(list(documents), ["STE authoring guidance"])
        content = next(iter(documents.values()))
        self.assertIn("maximum of 20 words", content)
        self.assertNotIn("## Sentence information structure", content)
        full = runner.frozen_documents(REPO, "manuscript")
        for name in runner.SKILLS:
            self.assertIn("skills/" + name + "/SKILL.md", full)
        self.assertIn("research/systems-paper-writing-requirements.md", full)

    def test_formal_prompt_is_progressive_and_keeps_exact_handoffs(self):
        payload = {"prompt": "Inspect current material", "scope": {}, "evidence": {}}
        first = b"original review\r\n  exact \n"
        revise = b"whole revision receipt\r\n\n"
        prompt = runner.formal_prompt(payload, ["bundle:skills/test/SKILL.md"], handoff=first, revision_handoff=revise)
        self.assertIn(b"Read the named entrypoint with read_file", prompt)
        self.assertNotIn(b"<frozen_documents>", prompt)
        self.assertIn(b"<stage_1_output>\n" + first + b"\n</stage_1_output>", prompt)
        self.assertIn(b"<revision_audit_output>\n" + revise + b"\n</revision_audit_output>", prompt)
        self.assertEqual(set(payload), {"prompt", "scope", "evidence"})

    def test_formal_prompt_authoring_closes_provenance_read_boundary(self):
        payload = {"prompt": "Edit the supplied draft.", "scope": {"authorized": ["draft", "context", "local evidence"]},
                   "evidence": {"provenance": "[registry](source-registry.md) and https://example.invalid/reference"}}
        prompt = runner.formal_prompt(payload, ["bundle:STE-authoring-guidance.md"], authoring=True)
        self.assertIn(b"Read only the named STE authoring guidance with read_file.", prompt)
        self.assertIn(b"The exact STE section and supplied draft, context, and local evidence are the complete instruction inputs.", prompt)
        self.assertIn(b"Hyperlinks record provenance and do not authorize further reads.", prompt)
        self.assertIn(b"Do not follow linked source registries, other paper references, or URLs.", prompt)
        self.assertIn(b"No additional dictionary lookup is authorized or required.", prompt)
        self.assertNotIn(b"then read its linked references as its workflow requires", prompt)
        self.assertIn(b"<task_input>\n" + json.dumps(payload, ensure_ascii=False, indent=2).encode() + b"\n</task_input>", prompt)
        self.assertNotIn(b"<frozen_documents>", prompt)
        self.assertNotIn(b"call list_files", prompt)
        self.assertEqual(hashlib.sha256(prompt).hexdigest(),
                         "11170e378d4315a119329c6fb4a93bac2385f4afd0f9b5def447526b54c144ef")

    def test_formal_prompt_namespaces_follow_actual_project_presence(self):
        payload = {"prompt": "Inspect manuscript.md in the supplied material.", "scope": {}, "evidence": {}}
        entries = ["bundle:skills/systems-paper-review/SKILL.md"]
        for stage in (None, "review", "revise"):
            with self.subTest(stage=stage):
                inline = runner.formal_prompt(payload, entries, stage=stage, handoff=b"exact prior output\r\n")
                self.assertIn(b"Enabled file namespace: bundle only. No project namespace is enabled.", inline)
                self.assertIn(b"Read task material from the supplied payload and authorized handoffs; do not use project namespace or probe local files.", inline)
                self.assertNotIn(b"Enabled file namespaces: bundle and project.", inline)
                self.assertNotIn(b"Authorized project:", inline)
                project = runner.formal_prompt(payload, entries, project=Path("/isolated/project"), stage=stage)
                self.assertIn(b"Enabled file namespaces: bundle and project.", project)
                self.assertIn(b"Use project only for the actual authorized project and declared project reads and writes below.", project)
                self.assertNotIn(b"No project namespace is enabled.", project)
                self.assertIn(b"Authorized project: /isolated/project.", project)

    def test_formal_prompt_manuscript_bytes_match_v6_except_access_pointer(self):
        # Only the administrative access instructions may differ from the pinned v6 bytes.
        payload = {"prompt": "Review supplied material only.\nKeep Ω and literal links.",
                   "scope": {"authorized": ["named manuscript"], "excluded": ["external sources"]},
                   "evidence": {"fact": "Replica count is supplied."}}
        entries = ["bundle:skills/systems-paper-review/SKILL.md"]
        variants = [
            ({}, "efef7eeb1be92498c1b5d2669e4eb6f58f8ffab95f0246a5e768cc8df2a4236f"),
            ({"project": Path("/isolated/project"), "stage": "review"},
             "1101b4e7b17504bae117f193852bfed1e6fb30bbc84f21ce970bfe2834087ab1"),
            ({"project": Path("/isolated/project"), "stage": "grill_confirm"},
             "7e22999398e15505a7d557dfd5106fd4aa06afc539944d57b2d67b0a740cc30a"),
            ({"project": Path("/isolated/project"), "stage": "rereview", "handoff": b"initial review\r\n  exact\n",
              "revision_handoff": b"complete revision receipt\r\n\n"},
             "9fc0563144fa1617b4fd7995f7a6e16ea64c148ee40ed4ea8d3da57da044bfb4"),
        ]
        for kwargs, expected in variants:
            with self.subTest(kwargs=kwargs):
                prompt = runner.formal_prompt(payload, entries, **kwargs)
                pointer = (b"Read the named entrypoint with read_file. Before following linked references, call list_files with namespace bundle. "
                           b"Resolve each relative Markdown link from the parent directory of the file containing it, then read only its exact declared canonical bundle path from the returned list, using the bundle: prefix. "
                           b"Do not guess or insert path prefixes. Read its linked references as its workflow requires. ")
                self.assertEqual(prompt.count(pointer), 1)
                normalized = prompt.replace(pointer, b"Read the named entrypoint with read_file, then read its linked references as its workflow requires. ", 1)
                namespace = (b"Enabled file namespaces: bundle and project. Use project only for the actual authorized project and declared project reads and writes below. " if kwargs.get("project") else
                             b"Enabled file namespace: bundle only. No project namespace is enabled. Read task material from the supplied payload and authorized handoffs; do not use project namespace or probe local files. ")
                self.assertEqual(normalized.count(namespace), 1)
                normalized = normalized.replace(namespace, b"", 1)
                self.assertEqual(hashlib.sha256(normalized).hexdigest(), expected)
                self.assertNotIn(b"Hyperlinks record provenance", prompt)

    def test_complete_bundle_install_preserves_declared_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "installed"
            inventory = runner.install_frozen_bundle(REPO, root)
            for name in runner.SKILLS:
                self.assertEqual((root / "skills" / name / "SKILL.md").read_bytes(), (REPO / "skills" / name / "SKILL.md").read_bytes())
            self.assertIn("research/systems-paper-writing-requirements.md", inventory)
            self.assertFalse((root / "benchmarks").exists())

    def access_server(self, temp, writes=(), web=False):
        root = Path(temp)
        bundle, project = root / "bundle", root / "project"
        bundle.mkdir()
        project.mkdir()
        (bundle / "SKILL.md").write_bytes(b"first\r\nsecond\n")
        (bundle / "hidden.txt").write_text("not declared")
        (project / "manuscript.md").write_bytes(b"initial\r\n")
        (project / "review.md").write_text("original report")
        policy = root / "policy.json"
        policy.write_text(json.dumps({"bundle_root": str(bundle), "bundle_files": ["SKILL.md"],
                                     "project_root": str(project), "project_reads": ["manuscript.md", "review.md"],
                                     "project_writes": list(writes), "official_web": web, "evidence_root": str(root / "audit")}))
        return AccessServer(policy), policy, bundle, project

    def test_access_server_rejects_escape_hidden_inputs_symlink_and_out_of_stage_write(self):
        with tempfile.TemporaryDirectory() as temp:
            server, policy, bundle, project = self.access_server(temp)
            for path in ("bundle:hidden.txt", "bundle:../policy.json", str(policy), "project:missing.md"):
                self.assertTrue(server.call("read_file", {"path": path})["isError"])
            (bundle / "SKILL.md").unlink()
            (bundle / "SKILL.md").symlink_to(bundle / "hidden.txt")
            self.assertTrue(server.call("read_file", {"path": "bundle:SKILL.md"})["isError"])
            self.assertTrue(server.call("write_file", {"path": "manuscript.md", "content": "changed"})["isError"])
            self.assertEqual((project / "manuscript.md").read_bytes(), b"initial\r\n")
            audit = runner.access_audit(server.log, {"read_file", "list_files"})
            self.assertTrue(audit["access_errors"])

    def test_access_read_write_records_exact_bytes_and_readback(self):
        with tempfile.TemporaryDirectory() as temp:
            server, _, _, project = self.access_server(temp, writes=["manuscript.md"])
            read = server.call("read_file", {"path": "bundle:SKILL.md", "start_line": 2, "max_lines": 1})
            result = json.loads(read["content"][0]["text"])
            self.assertEqual(result["content"], "second\n")
            self.assertEqual((server.evidence / result["file"]["artifact"]).read_bytes(), b"first\r\nsecond\n")
            content = "修订\r\nexact\n"
            self.assertFalse(server.call("write_file", {"path": "project:manuscript.md", "content": content})["isError"])
            self.assertFalse(server.call("read_file", {"path": "manuscript.md"})["isError"])
            self.assertEqual((project / "manuscript.md").read_bytes(), content.encode())
            audit = runner.access_audit(server.log, {"read_file", "list_files", "write_file"})
            self.assertFalse(audit["access_errors"])
            self.assertEqual(len(audit["access_events"]), 3)
            lines = server.log.read_text().splitlines()
            altered = json.loads(lines[0])
            altered["status"] = "denied"
            lines[0] = json.dumps(altered)
            server.log.write_text("\n".join(lines))
            self.assertIn("access_hash_chain_invalid", runner.access_audit(server.log, {"read_file", "list_files", "write_file"})["access_errors"])

    def test_official_fetch_rejects_other_origins_before_network(self):
        with tempfile.TemporaryDirectory() as temp:
            server, _, _, _ = self.access_server(temp, web=True)
            with patch("benchmark_access_server.urllib.request.build_opener") as opener:
                for url in ("https://example.com/", "file:///etc/passwd", "http://www.asplos-conference.org/", "https://user:password@www.asplos-conference.org/", "https://www.asplos-conference.org:444/"):
                    self.assertTrue(server.call("read_url", {"url": url})["isError"])
                self.assertFalse(opener.return_value.open.called)

    def test_allowed_official_unavailability_preserves_unresolved_path(self):
        import urllib.error
        with tempfile.TemporaryDirectory() as temp:
            server, _, _, _ = self.access_server(temp, web=True)
            with patch("benchmark_access_server.urllib.request.build_opener") as opener:
                opener.return_value.open.side_effect = urllib.error.URLError("temporary transport unavailable")
                response = server.call("read_url", {"url": "https://www.asplos-conference.org/asplos2027/cfp/"})
            self.assertFalse(response["isError"])
            body = json.loads(response["content"][0]["text"])
            self.assertFalse(body["available"])
            self.assertIn("unresolved", body["verification_status"])
            self.assertFalse(runner.access_audit(server.log, {"read_url"})["access_errors"])

    def test_formal_command_preserves_legacy_disabling_and_exact_resume(self):
        with tempfile.TemporaryDirectory() as temp:
            server, policy, _, project = self.access_server(temp, writes=["manuscript.md"])
            command = runner.formal_command("codex", "fixed-model", "high", project, Path(temp) / "output", policy, [], stage="grill_confirm", resume=UUID)
            self.assertEqual(command[-3:], ["resume", UUID, "-"])
            self.assertIn("features.shell_tool=false", command)
            self.assertIn("features.unified_exec=false", command)
            self.assertIn('web_search="disabled"', command)
            self.assertIn("mcp_servers.benchmark_access.required=true", command)
            self.assertNotIn("--ephemeral", command)
            catalog = Path(temp) / "catalog.json"
            pinned = runner.formal_command("codex", "fixed-model", "high", project, Path(temp) / "output", policy, [], model_catalog=catalog)
            self.assertIn("model_catalog_json=" + json.dumps(str(catalog.resolve())), pinned)

    def test_formal_workflow_preserves_original_review_and_whole_revision_handoff(self):
        class FakeRunner:
            def __init__(self, environment):
                self.environment = environment
                self.calls = []

            def call(self, directory, payload, documents, suite, **kwargs):
                directory.mkdir()
                stage = kwargs["stage"]
                self.calls.append((stage, payload, documents, kwargs))
                content = b"complete original review\r\n\n" if stage == "review" else b"whole revision audit\r\n  exact \n" if stage == "revise" else b"stage output\n"
                (directory / "output.txt").write_bytes(content)
                return {"status": "completed_unscored", "stage": stage, "thread_uuid": UUID if stage == "grill_open" else None}
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake = FakeRunner(root / "environment")
            result = runner.formal_case(23, fixture(23), root / "case", fake, "manuscript", {"skills/test/SKILL.md"})
            self.assertEqual(result["status"], "completed_unscored")
            self.assertEqual([entry[0] for entry in fake.calls], list(runner.STAGES))
            self.assertEqual(fake.calls[2][3]["resume"], UUID)
            self.assertEqual(fake.calls[4][3]["revision_handoff"], b"whole revision audit\r\n  exact \n")
            project = fake.calls[0][3]["project"]
            self.assertEqual((project / "review.md").read_bytes(), b"complete original review\r\n\n")
            self.assertNotIn("confirmed_after_grill", fake.calls[1][1]["evidence"])

    def test_formal_unknown_events_and_tools_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events"
            permitted = {"type": "item.completed", "item": {"type": "mcp_tool_call", "server": "benchmark_access", "tool": "read_file", "status": "completed", "result": {}}}
            path.write_text(json.dumps(permitted) + '\n{"type":"turn.completed","usage":{}}')
            self.assertFalse(runner.formal_event_audit(path, {"read_file"})["event_errors"])
            for extra in ({"type": "unknown"}, {"type": "item.completed", "item": {"type": "command_execution"}},
                          {"type": "item.completed", "item": {"type": "mcp_tool_call", "server": "ambient", "tool": "read_file"}}):
                path.write_text(json.dumps(extra))
                self.assertTrue(runner.formal_event_audit(path, {"read_file"})["event_errors"])

    def test_formal_completed_mcp_requires_valid_status_and_result(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events"
            for status, result in (("in_progress", {}), ("unknown", {}), ("completed", None), (None, {})):
                path.write_text(json.dumps({"type": "item.completed", "item": {"type": "mcp_tool_call", "server": "benchmark_access", "tool": "read_file", "status": status, "result": result}}))
                self.assertIn("malformed_mcp_status:read_file", runner.formal_event_audit(path, {"read_file"})["event_errors"])

    def test_access_audit_rejects_missing_or_changed_nested_raw_blobs(self):
        with tempfile.TemporaryDirectory() as temp:
            server, _, _, _ = self.access_server(temp)
            response = server.call("read_file", {"path": "bundle:SKILL.md"})
            body = json.loads(response["content"][0]["text"])
            raw = server.evidence / body["file"]["artifact"]
            self.assertFalse(runner.access_audit(server.log, {"read_file"})["access_errors"])
            raw.write_bytes(b"changed")
            self.assertIn("access_blob_invalid", runner.access_audit(server.log, {"read_file"})["access_errors"])
            raw.unlink()
            self.assertIn("access_blob_invalid", runner.access_audit(server.log, {"read_file"})["access_errors"])


if __name__ == "__main__":
    unittest.main()
