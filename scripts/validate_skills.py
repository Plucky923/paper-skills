#!/usr/bin/env python3
"""Deterministic structural validation for the PaperSkills bundle.

This validator deliberately checks packaging and routing invariants rather than
the wording of generated paper prose.  It uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import stat
import sys
from collections import deque
from pathlib import Path
from urllib.parse import unquote


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / "skills"
BUNDLE_MANIFEST = REPO_ROOT / "benchmarks" / "bundle.json"
FIXTURES_ROOT = REPO_ROOT / "benchmarks" / "fixtures"
TASK_INPUT_AUTHORITY_PATH = "benchmarks/task-input-authority.json"

PAPER_SKILLS = ["systems-paper-review", "systems-paper-revise"]
EXPECTED_SKILLS = PAPER_SKILLS + ["systems-paper-grill"]
EXPECTED_INSTALL_MAPPINGS = [
    {
        "source": "skills/systems-paper-grill",
        "install_path": "skills/systems-paper-grill",
        "kind": "directory",
    },
    {
        "source": "skills/systems-paper-review",
        "install_path": "skills/systems-paper-review",
        "kind": "directory",
    },
    {
        "source": "skills/systems-paper-revise",
        "install_path": "skills/systems-paper-revise",
        "kind": "directory",
    },
    {
        "source": "research/systems-paper-writing-requirements.md",
        "install_path": "research/systems-paper-writing-requirements.md",
        "kind": "file",
    },
]
EXPECTED_PROVENANCE_FILES = [
    {
        "source": "research/systems-paper-writing-requirements.md",
        "install_path": "research/systems-paper-writing-requirements.md",
        "consumers": EXPECTED_SKILLS,
        "preservation": "byte_exact",
        "sha256": "ef89a56dfb648657dbb89545c008f41d35dd6c38c9768684bb719fd319945263",
    }
]
EXPECTED_ACCEPTANCE = {
    "fixture_count": 49,
    "minimum_score_per_fixture": 10,
    "allow_regression": False,
    "require_all_hard_gates": True,
    "improvement_required": "higher_total_or_closed_observed_failure",
    "require_closure_record": True,
}
FIXTURE_BASE_FIELDS = {
    "id",
    "title",
    "skills",
    "material_origin",
    "scope",
    "evidence",
    "protected_tokens",
    "forbidden_actions",
    "hard_gates",
    "expected_behavior",
    "rubric",
}
INTEGRATED_FIXTURE_ID = "venue-integrated-review-revise"
WORKFLOW_FIXTURE_ID = "paper-discussion-workflow"
COVERAGE_WORKFLOW_FIXTURE_ID = "coverage-closure-workflow"
WORKFLOW_FIXTURE_NUMBERS = {
    WORKFLOW_FIXTURE_ID: 20,
    COVERAGE_WORKFLOW_FIXTURE_ID: 23,
    "decision-lineage-promotion-workflow": 39,
}
OBSERVED_FAILURE_FIXTURE_NUMBERS = {
    "property-proof-category": 24,
    "related-work-root-cause": 25,
    "payoff-and-role-review": 26,
    "evidence-derived-conclusion": 27,
    "mixed-evaluation-challenge": 28,
    "structural-question-authority": 29,
    "limitation-introduction-placement": 30,
    "safe-local-repair-frontier": 31,
    "cold-review-trigger-checkpoint": 32,
    "missing-result-placeholder-block": 33,
    "intellectual-move-fanout-grounding": 34,
    "revise-interactive-finding-queue": 35,
    "boundary-distinct-question": 36,
    "interface-axis-revision": 37,
    "decision-history-pending-head": 38,
    "decision-lineage-promotion-workflow": 39,
    "decision-conflict-prose-receipt": 40,
    "positioning-observation-review": 41,
    "positioning-observation-revision": 42,
}
WORKFLOW_STAGES = ("review", "grill_open", "grill_confirm", "revise", "rereview")
WORKFLOW_SKILLS = ["systems-paper-review", "systems-paper-grill", "systems-paper-revise"]
COVERAGE_CONTRACT_PATH = "skills/systems-paper-revise/references/coverage-contract.md"
COVERAGE_CONTRACT_ENTRY = {
    "path": COVERAGE_CONTRACT_PATH,
    "consumers": EXPECTED_SKILLS,
}
INTERFACE_BOUNDARY_CONTRACT_PATH = (
    "skills/systems-paper-revise/references/interface-boundaries.md"
)
INTERFACE_BOUNDARY_CONTRACT_ENTRY = {
    "path": INTERFACE_BOUNDARY_CONTRACT_PATH,
    "consumers": PAPER_SKILLS,
}
POSITIONING_INSIGHT_CONTRACT_PATH = (
    "skills/systems-paper-revise/references/positioning-and-insight.md"
)
POSITIONING_INSIGHT_CONTRACT_ENTRY = {
    "path": POSITIONING_INSIGHT_CONTRACT_PATH,
    "consumers": PAPER_SKILLS,
}
DECISION_RECORD_PATH = "skills/systems-paper-grill/references/decision-record.md"
DECISION_RECORD_ENTRY = {
    "path": DECISION_RECORD_PATH,
    "consumers": EXPECTED_SKILLS,
}

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
CODE_MD_POINTER_RE = re.compile(r"`([^`\n]*?\.md(?:#[^`\s]*)?)`")
RULE_FAMILIES = ("PA", "TH", "RC", "DD", "TS", "EV", "ER", "AR", "SS", "PT", "FL", "VO", "CS")
RULE_ID_RE = re.compile(r"\b(" + "|".join(RULE_FAMILIES) + r")-(\d+)([A-Z]?)\b")
RULE_DEF_RE = re.compile(
    r"^#{2,6}\s+(" + "|".join(RULE_FAMILIES) + r")-(\d+)([A-Z]?)\b",
    re.MULTILINE,
)
RULE_RANGE_RE = re.compile(
    r"\b(" + "|".join(RULE_FAMILIES) + r")-(\d+)\s*[–—-]\s*(?:\1-)?(\d+)\b"
)
STATUS_ID_RE = re.compile(r"\b([EB][1-9])\b")
STATUS_RANGE_RE = re.compile(r"\b([EB])(\d+)\s*[–—-]\s*(?:\1)?(\d+)\b")
STATUS_BULLET_DEF_RE = re.compile(r"^\s*[-*]\s+`([EB][1-9])\s+[—-]", re.MULTILINE)
STATUS_TABLE_DEF_RE = re.compile(
    r"^\s*\|\s*`?(?:blocked-)?([EB][1-9])`?\s*\|", re.MULTILINE
)
SOURCE_DEF_RE = re.compile(r"^#{2,6}\s+\[([A-Z][A-Z0-9-]{2,})\]\s*$", re.MULTILINE)
SOURCE_REF_RE = re.compile(r"\[([A-Z][A-Z0-9-]{2,})\](?!\()")


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError:
        return str(path)


def parse_scalar(raw: str) -> str:
    value = raw.strip()
    if not value:
        return ""
    if value[0:1] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(value)
            return parsed if isinstance(parsed, str) else str(parsed)
        except (SyntaxError, ValueError):
            return value.strip("'\"")
    return value


def parse_frontmatter(path: Path, report: Report) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        report.error(f"{rel(path)}: missing YAML frontmatter opener")
        return {}
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        report.error(f"{rel(path)}: missing YAML frontmatter closer")
        return {}
    result: dict[str, str] = {}
    for line in parts[1].splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            result[match.group(1)] = parse_scalar(match.group(2))
    return result


def markdown_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    if re.match(r"^(?:https?://|mailto:|data:|#)", target):
        return None
    target = unquote(target.split("#", 1)[0])
    if not target:
        return None
    return (source.parent / target).resolve()


def is_markdown_reachable(entrypoint: Path, target: Path) -> bool:
    queue: deque[Path] = deque([entrypoint.resolve()])
    visited: set[Path] = set()
    while queue:
        current = queue.popleft()
        if current in visited or not current.is_file():
            continue
        if current == target.resolve():
            return True
        visited.add(current)
        if current.suffix != ".md":
            continue
        for raw_target in MARKDOWN_LINK_RE.findall(current.read_text(encoding="utf-8")):
            linked = markdown_target(current, raw_target)
            if linked is not None and linked.is_file() and linked.suffix == ".md":
                queue.append(linked)
    return False


def check_bundle(
    report: Report,
) -> tuple[list[Path], list[Path], list[Path], dict[str, object]]:
    if not BUNDLE_MANIFEST.is_file():
        report.error(f"{rel(BUNDLE_MANIFEST)}: missing bundle manifest")
        return [], [], [], {}
    try:
        manifest = json.loads(BUNDLE_MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.error(f"{rel(BUNDLE_MANIFEST)}: invalid JSON: {exc}")
        return [], [], [], {}

    if not isinstance(manifest, dict):
        report.error(f"{rel(BUNDLE_MANIFEST)}: root must be an object")
        return [], [], [], {}

    expected_manifest_fields = {
        "schema_version",
        "installation_mode",
        "required_skills",
        "install_mappings",
        "provenance_files",
        "behavioral_acceptance",
        "canonical_references",
    }
    if "task_input_authority" in manifest:
        expected_manifest_fields.add("task_input_authority")
    actual_manifest_fields = set(manifest)
    if actual_manifest_fields != expected_manifest_fields:
        report.error(
            f"{rel(BUNDLE_MANIFEST)}: fields must be exactly "
            f"{sorted(expected_manifest_fields)!r}; got {sorted(actual_manifest_fields)!r}"
        )

    required_skills = manifest.get("required_skills")
    install_mappings = manifest.get("install_mappings")
    provenance_files = manifest.get("provenance_files")
    canonical_references = manifest.get("canonical_references")
    if manifest.get("schema_version") != 1:
        report.error(f"{rel(BUNDLE_MANIFEST)}: schema_version must be 1")
    if manifest.get("installation_mode") != "bundle":
        report.error(f"{rel(BUNDLE_MANIFEST)}: installation_mode must be 'bundle'")
    if manifest.get("behavioral_acceptance") != EXPECTED_ACCEPTANCE:
        report.error(
            f"{rel(BUNDLE_MANIFEST)}: behavioral_acceptance must be "
            f"{EXPECTED_ACCEPTANCE!r}"
        )
    if required_skills != EXPECTED_SKILLS:
        report.error(
            f"{rel(BUNDLE_MANIFEST)}: required_skills must be exactly "
            f"{EXPECTED_SKILLS!r}"
        )
        required_skills = []
    if install_mappings != EXPECTED_INSTALL_MAPPINGS:
        report.error(
            f"{rel(BUNDLE_MANIFEST)}: install_mappings must be exactly "
            f"{EXPECTED_INSTALL_MAPPINGS!r}"
        )
        install_mappings = []
    if provenance_files != EXPECTED_PROVENANCE_FILES:
        report.error(
            f"{rel(BUNDLE_MANIFEST)}: provenance_files must be exactly "
            f"{EXPECTED_PROVENANCE_FILES!r}"
        )
        provenance_files = []
    if not isinstance(canonical_references, list) or not canonical_references:
        report.error(f"{rel(BUNDLE_MANIFEST)}: canonical_references must be a non-empty list")
        canonical_references = []
    elif COVERAGE_CONTRACT_ENTRY not in canonical_references:
        report.error(
            f"{rel(BUNDLE_MANIFEST)}: canonical_references must include the shared "
            "coverage contract for all three skills"
        )
    if (
        isinstance(canonical_references, list)
        and INTERFACE_BOUNDARY_CONTRACT_ENTRY not in canonical_references
    ):
        report.error(
            f"{rel(BUNDLE_MANIFEST)}: canonical_references must include the shared "
            "interface-boundary contract for Review and Revise"
        )
    if (
        isinstance(canonical_references, list)
        and POSITIONING_INSIGHT_CONTRACT_ENTRY not in canonical_references
    ):
        report.error(
            f"{rel(BUNDLE_MANIFEST)}: canonical_references must include the shared "
            "positioning-and-insight contract for Review and Revise"
        )
    if (
        isinstance(canonical_references, list)
        and DECISION_RECORD_ENTRY not in canonical_references
    ):
        report.error(
            f"{rel(BUNDLE_MANIFEST)}: canonical_references must include the "
            "decision-record contract for all three skills"
        )

    public_skill_dirs = sorted(
        path.name
        for path in SKILLS_ROOT.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    ) if SKILLS_ROOT.is_dir() else []
    if public_skill_dirs != sorted(EXPECTED_SKILLS):
        report.error(
            f"{rel(SKILLS_ROOT)}: public skill directories must be exactly "
            f"{sorted(EXPECTED_SKILLS)!r}; got {public_skill_dirs!r}"
        )

    skill_dirs: list[Path] = []
    for name in required_skills:
        if not isinstance(name, str):
            report.error(f"{rel(BUNDLE_MANIFEST)}: skill names must be strings")
            continue
        skill_dir = SKILLS_ROOT / name
        if not (skill_dir / "SKILL.md").is_file():
            report.error(f"bundle requires missing skill: {rel(skill_dir / 'SKILL.md')}")
        else:
            skill_dirs.append(skill_dir)

    mapping_pairs: set[tuple[str, str]] = set()
    for item in install_mappings if isinstance(install_mappings, list) else []:
        source = item["source"]
        install_path = item["install_path"]
        kind = item["kind"]
        mapping_pairs.add((source, install_path))
        source_path = (REPO_ROOT / source).resolve()
        try:
            source_path.relative_to(REPO_ROOT.resolve())
        except ValueError:
            report.error(f"install source escapes repository: {source}")
            continue
        if kind == "directory" and not source_path.is_dir():
            report.error(f"missing install source directory: {source}")
        elif kind == "file" and not source_path.is_file():
            report.error(f"missing install source file: {source}")

    canonical_paths: list[Path] = []
    seen_canonical_paths: set[str] = set()
    for item in canonical_references:
        if not isinstance(item, dict):
            report.error(f"{rel(BUNDLE_MANIFEST)}: canonical references must be objects")
            continue
        if set(item) != {"path", "consumers"}:
            report.error(
                f"{rel(BUNDLE_MANIFEST)}: canonical reference fields must be exactly "
                "path and consumers"
            )
        item_path = item.get("path")
        consumers = item.get("consumers")
        if not isinstance(item_path, str) or not item_path.strip():
            report.error(f"{rel(BUNDLE_MANIFEST)}: canonical reference needs a path")
            continue
        if item_path in seen_canonical_paths:
            report.error(f"duplicate canonical reference path: {item_path}")
        seen_canonical_paths.add(item_path)
        if (
            not isinstance(consumers, list)
            or not consumers
            or any(not isinstance(consumer, str) or not consumer for consumer in consumers)
            or len(consumers) != len(set(consumers))
        ):
            report.error(
                f"{rel(BUNDLE_MANIFEST)}: canonical reference {item_path} needs "
                "unique non-empty-string consumers"
            )
            consumers = []
        path = (REPO_ROOT / item_path).resolve()
        try:
            path.relative_to(REPO_ROOT.resolve())
        except ValueError:
            report.error(f"canonical reference escapes repository: {item_path}")
            continue
        if not path.is_file():
            report.error(f"missing canonical reference: {item_path}")
        else:
            canonical_paths.append(path)
            for consumer in consumers:
                if consumer not in required_skills:
                    report.error(
                        f"canonical reference {item_path} names non-bundle consumer {consumer!r}"
                    )
                    continue
                entrypoint = SKILLS_ROOT / consumer / "SKILL.md"
                if entrypoint.is_file() and not is_markdown_reachable(entrypoint, path):
                    report.error(
                        f"canonical reference {item_path} is not reachable from "
                        f"{rel(entrypoint)}"
                    )

    provenance_paths: list[Path] = []
    for item in provenance_files if isinstance(provenance_files, list) else []:
        source = item["source"]
        install_path = item["install_path"]
        consumers = item["consumers"]
        path = (REPO_ROOT / source).resolve()
        if (source, install_path) not in mapping_pairs:
            report.error(f"provenance file lacks an exact install mapping: {source}")
        if not path.is_file():
            report.error(f"missing provenance file: {source}")
            continue
        provenance_paths.append(path)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item["sha256"]:
            report.error(
                f"{source}: SHA-256 {digest} does not match declared unchanged "
                f"provenance digest {item['sha256']}"
            )
        for consumer in consumers:
            if consumer not in required_skills:
                report.error(f"provenance file {source} names unknown consumer {consumer!r}")
                continue
            entrypoint = SKILLS_ROOT / consumer / "SKILL.md"
            if entrypoint.is_file() and not is_markdown_reachable(entrypoint, path):
                report.error(
                    f"provenance file {source} is not reachable from {rel(entrypoint)}"
                )

    check_grill_sources(report)
    return skill_dirs, canonical_paths, provenance_paths, manifest


def check_grill_sources(report: Report) -> None:
    """Verify attribution for the adapted paper-specific interview skill."""
    source_file = REPO_ROOT / "benchmarks" / "grill-source.json"
    try:
        source = json.loads(source_file.read_text(encoding="utf-8"))
        if source["repository"] != "https://github.com/mattpocock/skills":
            raise ValueError("unexpected upstream repository")
        if not re.fullmatch(r"[0-9a-f]{40}", source["commit"]):
            raise ValueError("missing immutable upstream commit")
        if source["license"] != "MIT":
            raise ValueError("unexpected upstream license")
        if source["adapted_skill"] != "skills/systems-paper-grill":
            raise ValueError("unexpected adapted skill")
        if source["upstream_path"] != "skills/productivity/grilling/SKILL.md":
            raise ValueError("unexpected upstream interview source")
        if not re.fullmatch(r"[0-9a-f]{64}", source["upstream_sha256"]):
            raise ValueError("missing upstream content digest")
        license_path = REPO_ROOT / "skills/systems-paper-grill/LICENSE"
        if hashlib.sha256(license_path.read_bytes()).hexdigest() != source["license_sha256"]:
            raise ValueError("upstream license was changed")
        if not isinstance(source["adaptation"], str) or not source["adaptation"].strip():
            raise ValueError("missing adaptation description")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        report.error(f"{rel(source_file)}: {exc}")


def check_skill_structure(skill_dir: Path, report: Report) -> None:
    skill_file = skill_dir / "SKILL.md"
    frontmatter = parse_frontmatter(skill_file, report)
    if frontmatter.get("name") != skill_dir.name:
        report.error(
            f"{rel(skill_file)}: frontmatter name {frontmatter.get('name')!r} "
            f"does not match directory {skill_dir.name!r}"
        )
    if not frontmatter.get("description"):
        report.error(f"{rel(skill_file)}: missing non-empty description")

    metadata = skill_dir / "agents" / "openai.yaml"
    if not metadata.is_file():
        report.error(f"{rel(metadata)}: missing UI metadata")
        return
    text = metadata.read_text(encoding="utf-8")
    prompt_match = re.search(r"^\s*default_prompt:\s*(.+)$", text, re.MULTILINE)
    if not prompt_match:
        report.error(f"{rel(metadata)}: missing interface.default_prompt")
    elif prompt_match:
        prompt = parse_scalar(prompt_match.group(1))
        if f"${skill_dir.name}" not in prompt:
            report.error(
                f"{rel(metadata)}: default_prompt must mention ${skill_dir.name}"
            )
    short_match = re.search(r"^\s*short_description:\s*(.+)$", text, re.MULTILINE)
    if not short_match:
        report.error(f"{rel(metadata)}: missing interface.short_description")
    else:
        length = len(parse_scalar(short_match.group(1)))
        if not 25 <= length <= 64:
            report.error(
                f"{rel(metadata)}: short_description length {length} is outside 25-64"
            )


def check_links_and_reachability(skill_dir: Path, report: Report) -> None:
    markdown_files = sorted(skill_dir.rglob("*.md"))
    graph: dict[Path, set[Path]] = {path.resolve(): set() for path in markdown_files}
    all_repo_markdown = sorted(REPO_ROOT.rglob("*.md"))

    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        linked_targets: set[Path] = set()
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = markdown_target(source, raw_target)
            if target is None:
                continue
            linked_targets.add(target)
            if not target.exists():
                report.error(f"{rel(source)}: broken relative link -> {raw_target}")
                continue
            if target.suffix == ".md":
                graph.setdefault(source.resolve(), set()).add(target)

        for pointer in CODE_MD_POINTER_RE.findall(text):
            pointer_path = pointer.split("#", 1)[0]
            candidates = [
                (source.parent / pointer_path).resolve(),
                (skill_dir / pointer_path).resolve(),
                (REPO_ROOT / pointer_path).resolve(),
                (SKILLS_ROOT / pointer_path).resolve(),
            ]
            existing = next((candidate for candidate in candidates if candidate.is_file()), None)
            if existing is None:
                basename_matches = [path for path in all_repo_markdown if path.name == Path(pointer_path).name]
                hint = f"; possible target: {rel(basename_matches[0])}" if len(basename_matches) == 1 else ""
                report.error(
                    f"{rel(source)}: unresolved code-form Markdown pointer `{pointer}`{hint}"
                )
            elif existing not in linked_targets and pointer_path != "SKILL.md":
                report.warn(
                    f"{rel(source)}: `{pointer}` is reachable but not a Markdown context pointer"
                )

    entrypoint = (skill_dir / "SKILL.md").resolve()
    reachable: set[Path] = set()
    queue: deque[Path] = deque([entrypoint])
    while queue:
        current = queue.popleft()
        if current in reachable:
            continue
        reachable.add(current)
        queue.extend(graph.get(current, ()))

    references_dir = skill_dir / "references"
    if references_dir.is_dir():
        for reference in sorted(references_dir.rglob("*.md")):
            if reference.resolve() not in reachable:
                report.error(
                    f"{rel(reference)}: orphan reference is not reachable from {rel(entrypoint)}"
                )


def expand_rule_ranges(text: str) -> set[str]:
    expanded: set[str] = set()
    for family, start_raw, end_raw in RULE_RANGE_RE.findall(text):
        start, end = int(start_raw), int(end_raw)
        width = max(len(start_raw), len(end_raw))
        if start <= end and end - start <= 100:
            expanded.update(f"{family}-{value:0{width}d}" for value in range(start, end + 1))
    return expanded


def expand_status_ranges(text: str) -> set[str]:
    expanded: set[str] = set()
    for family, start_raw, end_raw in STATUS_RANGE_RE.findall(text):
        start, end = int(start_raw), int(end_raw)
        if start <= end and end - start <= 20:
            expanded.update(f"{family}{value}" for value in range(start, end + 1))
    return expanded


def check_identifier_definitions(skill_dirs: list[Path], report: Report) -> None:
    files = sorted(path for skill_dir in skill_dirs for path in skill_dir.rglob("*.md"))
    combined = "\n".join(path.read_text(encoding="utf-8") for path in files)

    rule_definitions = {
        f"{family}-{number}{suffix}"
        for family, number, suffix in RULE_DEF_RE.findall(combined)
    }
    rule_references = {
        f"{family}-{number}{suffix}"
        for family, number, suffix in RULE_ID_RE.findall(combined)
    }
    rule_references.update(expand_rule_ranges(combined))
    for identifier in sorted(rule_references - rule_definitions):
        locations = [
            f"{rel(path)}:{line_number}"
            for path in files
            for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
            if identifier in line
        ]
        report.error(
            f"undefined rule ID {identifier}; referenced at {', '.join(locations) or 'a range'}"
        )

    status_definitions = set(STATUS_BULLET_DEF_RE.findall(combined))
    status_definitions.update(STATUS_TABLE_DEF_RE.findall(combined))
    status_references = set(STATUS_ID_RE.findall(combined))
    status_references.update(expand_status_ranges(combined))
    for identifier in sorted(status_references - status_definitions):
        report.error(f"undefined revision status/repair ID {identifier}")

    source_definitions = set(SOURCE_DEF_RE.findall(combined))
    source_references = set(SOURCE_REF_RE.findall(combined))
    for identifier in sorted(source_references - source_definitions):
        report.error(f"undefined source key [{identifier}]")


def check_cross_skill_links(skill_dirs: list[Path], report: Report) -> None:
    required_names = {path.name for path in skill_dirs}
    for skill_dir in skill_dirs:
        for source in skill_dir.rglob("*.md"):
            text = source.read_text(encoding="utf-8")
            for raw_target in MARKDOWN_LINK_RE.findall(text):
                target = markdown_target(source, raw_target)
                if target is None or not target.exists():
                    continue
                try:
                    relative = target.relative_to(SKILLS_ROOT.resolve())
                except ValueError:
                    continue
                target_skill = relative.parts[0]
                if target_skill != skill_dir.name and target_skill not in required_names:
                    report.error(
                        f"{rel(source)}: cross-skill dependency {target_skill!r} "
                        "is absent from bundle required_skills"
                    )


def check_coverage_contract(report: Report) -> None:
    """Verify the mandatory coverage protocol and direct entrypoint routing."""
    contract = (REPO_ROOT / COVERAGE_CONTRACT_PATH).resolve()
    if not contract.is_file():
        report.error(f"missing shared coverage contract: {COVERAGE_CONTRACT_PATH}")
        return
    text = contract.read_text(encoding="utf-8")
    required_literals = (
        "`pass`",
        "`finding`",
        "`unresolved`",
        "`not assessable`",
        "paper-level thesis",
        "every section",
        "every paragraph",
        "every sentence",
        "every lexical occurrence",
        "bottom-up consistency",
        "signaled/intended role",
        "payoff/handoff, information gain",
        "Argument role/organization",
        "reviewer-hypothesized",
        "Intellectual-move dependencies",
        "causal layer",
        "Unreviewed: 0",
    )
    for literal in required_literals:
        if literal not in text:
            report.error(
                f"{COVERAGE_CONTRACT_PATH}: missing required coverage marker {literal!r}"
            )

    for skill_name in EXPECTED_SKILLS:
        entrypoint = REPO_ROOT / "skills" / skill_name / "SKILL.md"
        if not entrypoint.is_file():
            continue
        direct_targets = {
            markdown_target(entrypoint, raw_target)
            for raw_target in MARKDOWN_LINK_RE.findall(
                entrypoint.read_text(encoding="utf-8")
            )
        }
        if contract not in direct_targets:
            report.error(
                f"{rel(entrypoint)}: must link directly to the shared coverage contract"
            )


def check_interactive_clarification_contract(report: Report) -> None:
    """Verify Review-to-Revise action routing and its non-terminal question gate."""
    required_by_path = {
        "skills/systems-paper-revise/references/review-revise-contract.md": (
            "`direct repair`",
            "`author clarification`",
            "`author evidence`",
            "`external blocker`",
            "`optional/not applied`",
            "`pending clarification`",
            "Continue the same revision automatically",
        ),
        "skills/systems-paper-review/SKILL.md": (
            "next-action class",
            "`author evidence`",
        ),
        "skills/systems-paper-revise/SKILL.md": (
            "primary repair queue",
            "give one Grill-style round for each prerequisite-ready",
            "do not give a terminal closure map",
        ),
        "skills/systems-paper-grill/SKILL.md": (
            "embedded clarification loop",
            "continue the same revision without a second request",
        ),
    }
    for relative, literals in required_by_path.items():
        path = REPO_ROOT / relative
        if not path.is_file():
            report.error(f"missing interactive clarification contract file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for literal in literals:
            if literal not in text:
                report.error(
                    f"{relative}: missing interactive clarification marker {literal!r}"
                )


def check_interface_boundary_contract(report: Report) -> None:
    """Verify the shared interface, authority, and execution-path reasoning branch."""
    required_by_path = {
        INTERFACE_BOUNDARY_CONTRACT_PATH: (
            "Semantic commitments",
            "Protection and authority",
            "Execution path",
            "actor, artifact, stage, and control",
            "`negative gap`",
            "`distinct question`",
            "show a path fact or prediction",
            "claim strength",
        ),
        "skills/systems-paper-review/SKILL.md": (
            "interface-boundary contract",
            "direct or delegated execution paths",
        ),
        "skills/systems-paper-revise/SKILL.md": (
            "references/interface-boundaries.md",
            "direct/delegated path claim",
        ),
        "skills/systems-paper-review/references/review-protocol.md": (
            "For different questions, make sure that the map is parallel and the question is bounded",
            "semantic-commitment, protection/authority, and execution-path ledger",
        ),
        "skills/systems-paper-revise/references/revision-strategies.md": (
            "three-axis ledger",
            "claim strength",
        ),
    }
    for relative, literals in required_by_path.items():
        path = REPO_ROOT / relative
        if not path.is_file():
            report.error(f"missing interface-boundary contract file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for literal in literals:
            if literal not in text:
                report.error(
                    f"{relative}: missing interface-boundary marker {literal!r}"
                )


def check_positioning_insight_contract(report: Report) -> None:
    """Verify evidence distillation, conjunctive-gap, and Observation routing."""
    required_by_path = {
        POSITIONING_INSIGHT_CONTRACT_PATH: (
            "source evidence",
            "artifact-to-capability distillation",
            "conjunctive gap",
            "Evidence observation",
            "Find an inference beyond actor renaming, term explanation, or premise repetition",
            "prediction",
            "`author evidence`",
            "`author clarification`",
        ),
        "skills/systems-paper-review/SKILL.md": (
            "positioning and intellectual-move contract",
            "prior-work positioning with artifact evidence",
        ),
        "skills/systems-paper-revise/SKILL.md": (
            "references/positioning-and-insight.md",
            "Artifact-backed prior-work comparison",
        ),
        "skills/systems-paper-review/references/review-protocol.md": (
            "artifact-to-capability distillation",
            "conjunctive-gap test",
            "observation ladder",
        ),
        "skills/systems-paper-review/references/structure-and-sections.md": (
            "SS-09B",
            "Promised observations and insights",
        ),
        "skills/systems-paper-review/references/prose-and-terminology.md": (
            "PT-10B",
            "Evidence provenance",
        ),
        "skills/systems-paper-revise/references/revision-protocol.md": (
            "artifact-to-capability check",
            "each promised Observation/Insight",
        ),
        "skills/systems-paper-revise/references/revision-strategies.md": (
            "artifact-to-capability distillation",
            "Fluent requirement prose is not an",
        ),
    }
    for relative, literals in required_by_path.items():
        path = REPO_ROOT / relative
        if not path.is_file():
            report.error(f"missing positioning-and-insight contract file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for literal in literals:
            if literal not in text:
                report.error(
                    f"{relative}: missing positioning-and-insight marker {literal!r}"
                )


def check_decision_history_contract(report: Report) -> None:
    """Verify versioned decision authority, persistence, and accounting routes."""
    required_by_path = {
        DECISION_RECORD_PATH: (
            "versioned full snapshot",
            "`pending`",
            "`confirmed`",
            "`rejected`",
            "`superseded`",
            "`Proposes replacement for`",
            "Keep the confirmed head effective while a pending candidate is present",
            "one atomic record update",
            "**All versions:**",
            "**Effective heads:**",
            "**Applicable heads:**",
            "**Executable heads:**",
            "Duplicate IDs",
            "Nonreciprocal confirmed supersession",
            "Unaccounted decisions: 0",
            "zero history",
        ),
        "skills/systems-paper-grill/assets/paper-decisions-template.md": (
            "## D1.v1",
            "Lineage: D1",
            "Proposes replacement for:",
            "Supersedes:",
            "Superseded by:",
            "Decision and allowed edit:",
            "Confirmation basis:",
        ),
        "skills/systems-paper-grill/SKILL.md": (
            "full authorized history",
            "Keep the effective confirmed head while candidates are pending",
            "update the two supersession links in one write",
            "Before you complete a changed decision, save it at the authorized path",
            "Read the changed entries again",
            "Read their reciprocal links again",
            "Read unrelated records again",
        ),
        "skills/systems-paper-revise/references/review-revise-contract.md": (
            "Read each decision version",
            "all, effective, applicable, and executable",
            "Unaccounted decisions: 0",
            "prose-only Revise",
        ),
        "skills/systems-paper-review/SKILL.md": (
            "find the effective, applicable, and executable decision sets",
            "Unaccounted decisions: 0",
        ),
        "skills/systems-paper-revise/SKILL.md": (
            "Read each decision version",
            "the author's confirmation of no history",
            "one-line decision coverage",
        ),
    }
    for relative, literals in required_by_path.items():
        path = REPO_ROOT / relative
        if not path.is_file():
            report.error(f"missing decision-history contract file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for literal in literals:
            if literal not in text:
                report.error(
                    f"{relative}: missing decision-history marker {literal!r}"
                )

    shared_contract = (
        REPO_ROOT
        / "skills/systems-paper-revise/references/review-revise-contract.md"
    ).resolve()
    decision_record = (REPO_ROOT / DECISION_RECORD_PATH).resolve()
    if shared_contract.is_file() and decision_record.is_file():
        direct_targets = {
            markdown_target(shared_contract, raw_target)
            for raw_target in MARKDOWN_LINK_RE.findall(
                shared_contract.read_text(encoding="utf-8")
            )
        }
        if decision_record not in direct_targets:
            report.error(
                "shared workflow contract must link directly to decision-record rules"
            )


def check_nonempty_string_list(
    value: object, field: str, path: Path, report: Report, *, unique: bool = True
) -> list[str]:
    if (
        not isinstance(value, list)
        or not value
        or any(not isinstance(item, str) or not item.strip() for item in value)
    ):
        report.error(f"{rel(path)}: {field} must be a non-empty list of non-empty strings")
        return []
    if unique and len(value) != len(set(value)):
        report.error(f"{rel(path)}: {field} entries must be unique")
    return value


def check_nonempty_text_tree(value: object, field: str, path: Path, report: Report) -> None:
    if isinstance(value, str):
        if not value.strip():
            report.error(f"{rel(path)}: {field} contains an empty string")
        return
    if isinstance(value, list):
        if not value:
            report.error(f"{rel(path)}: {field} contains an empty list")
            return
        for index, item in enumerate(value):
            check_nonempty_text_tree(item, f"{field}[{index}]", path, report)
        return
    if isinstance(value, dict):
        if not value:
            report.error(f"{rel(path)}: {field} contains an empty object")
            return
        for key, item in value.items():
            if not isinstance(key, str) or not key.strip():
                report.error(f"{rel(path)}: {field} contains an empty or non-string key")
                continue
            check_nonempty_text_tree(item, f"{field}.{key}", path, report)
        return
    report.error(
        f"{rel(path)}: {field} must contain only objects, lists, and non-empty strings"
    )


def check_workflow_case(fixture: dict, path: Path, report: Report) -> None:
    """Validate the explicit multi-turn fixture, without exposing later replies."""
    stages = fixture.get("stage_prompts")
    if not isinstance(stages, dict) or set(stages) != set(WORKFLOW_STAGES):
        report.error(f"{rel(path)}: workflow stages must be exactly {WORKFLOW_STAGES!r}")
    elif any(not isinstance(value, str) or not value.strip() for value in stages.values()):
        report.error(f"{rel(path)}: every workflow stage must have a non-empty prompt")
    files = fixture.get("initial_files")
    if not isinstance(files, dict) or set(files) != {"manuscript.md", "paper-decisions.md"}:
        report.error(f"{rel(path)}: workflow initial files must be manuscript.md and paper-decisions.md")
    elif any(not isinstance(value, str) or not value.strip() for value in files.values()):
        report.error(f"{rel(path)}: workflow initial files must contain non-empty text")
    if fixture.get("skills") != WORKFLOW_SKILLS:
        report.error(f"{rel(path)}: workflow must route Review, Grill, Revise in that order")


def check_task_input_authority(
    manifest: dict[str, object], report: Report, authoring_case_count: int = 6
) -> dict[str, object]:
    """Check a declared prompt-only amendment against its original fixture bytes."""
    if "task_input_authority" not in manifest:
        return {"status": "legacy_without_marker", "record_count": 0}
    result: dict[str, object] = {"status": "invalid", "record_count": 0}
    if manifest["task_input_authority"] != TASK_INPUT_AUTHORITY_PATH:
        report.error(f"task_input_authority must name {TASK_INPUT_AUTHORITY_PATH!r}")
        return result
    path = REPO_ROOT / TASK_INPUT_AUTHORITY_PATH
    try:
        path.resolve().relative_to(REPO_ROOT.resolve())
        raw = path.read_bytes()
    except (OSError, ValueError) as exc:
        report.error(f"{rel(path)}: required task-input authority record unavailable: {exc}")
        return result
    result["record_sha256"] = hashlib.sha256(raw).hexdigest()
    initial_errors = len(report.errors)

    def strict_json(text: str | bytes) -> object:
        def unique_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
            obj: dict[str, object] = {}
            for key, value in pairs:
                if key in obj:
                    raise ValueError(f"duplicate JSON field {key!r}")
                obj[key] = value
            return obj

        def invalid_constant(value: str) -> object:
            raise ValueError(f"invalid JSON constant {value}")

        return json.loads(text, object_pairs_hook=unique_object, parse_constant=invalid_constant)

    def non_prompt_hash(fixture: dict[str, object]) -> str:
        canonical = json.dumps(
            {key: value for key, value in fixture.items() if key != "prompt"},
            ensure_ascii=False, sort_keys=True, separators=(",", ":"),
        ).encode("utf-8")
        return hashlib.sha256(canonical).hexdigest()

    try:
        authority = strict_json(raw)
    except (UnicodeError, ValueError) as exc:
        report.error(f"{rel(path)}: invalid authority JSON: {exc}")
        return result
    fields = {"schema_version", "revision", "created_at_utc", "manuscript_case_count",
              "authoring_case_count", "changed_cases", "unchanged_contract_fields",
              "scope", "author_priority", "records"}
    if not isinstance(authority, dict) or set(authority) != fields:
        report.error(f"{rel(path)}: authority fields must be exactly {sorted(fields)!r}")
        return result
    expected_count = EXPECTED_ACCEPTANCE["fixture_count"]
    for field, expected in (("schema_version", 1), ("manuscript_case_count", expected_count),
                            ("authoring_case_count", authoring_case_count)):
        if type(authority[field]) is not int or authority[field] != expected:
            report.error(f"{rel(path)}: {field} must be {expected}")
    for field in ("revision", "created_at_utc", "scope", "author_priority"):
        if not isinstance(authority[field], str) or not authority[field].strip():
            report.error(f"{rel(path)}: {field} must be a non-empty string")
    contract_fields = authority["unchanged_contract_fields"]
    expected_contract_fields = FIXTURE_BASE_FIELDS - {"material_origin"}
    if (not isinstance(contract_fields, list)
            or any(not isinstance(field, str) for field in contract_fields)
            or len(contract_fields) != len(set(contract_fields))
            or set(contract_fields) != expected_contract_fields):
        report.error(f"{rel(path)}: unchanged_contract_fields must list the complete contract")
    changed = authority["changed_cases"]
    if (not isinstance(changed, list)
            or any(type(number) is not int or not 1 <= number <= expected_count for number in changed)
            or len(changed) != len(set(changed))):
        report.error(f"{rel(path)}: changed_cases must contain unique fixture numbers")
        changed = []
    records = authority["records"]
    if not isinstance(records, list) or len(records) != expected_count:
        report.error(f"{rel(path)}: records must contain all {expected_count} fixtures")
        return result
    result["record_count"] = len(records)
    expected_paths = {fixture.relative_to(REPO_ROOT).as_posix()
                      for fixture in FIXTURES_ROOT.glob("*.json")}
    seen_numbers: set[int] = set()
    seen_paths: set[str] = set()
    seen_ids: set[str] = set()
    actual_changed: set[int] = set()
    original_byte_checks = 0
    base_fields = {"number", "case_id", "path", "original_file_sha256", "current_file_sha256",
                   "changed_fields", "non_prompt_fields_sha256"}
    for entry in records:
        if not isinstance(entry, dict):
            report.error(f"{rel(path)}: each authority record must be an object")
            continue
        changed_fields = entry.get("changed_fields")
        if changed_fields not in ([], ["prompt"]):
            report.error(f"{rel(path)}: changed_fields permits only prompt")
            continue
        amended = changed_fields == ["prompt"]
        entry_fields = base_fields | ({"original_prompt", "current_prompt", "reason", "original_fixture_text"} if amended else set())
        if set(entry) != entry_fields:
            report.error(f"{rel(path)}: unexpected or missing authority entry fields")
            continue
        number, fixture_path, case_id = entry["number"], entry["path"], entry["case_id"]
        if (type(number) is not int or not 1 <= number <= expected_count
                or not isinstance(fixture_path, str) or fixture_path not in expected_paths
                or not isinstance(case_id, str) or not case_id):
            report.error(f"{rel(path)}: invalid fixture identity in authority record")
            continue
        if number in seen_numbers or fixture_path in seen_paths or case_id in seen_ids:
            report.error(f"{rel(path)}: duplicate fixture authority entry")
        seen_numbers.add(number)
        seen_paths.add(fixture_path)
        seen_ids.add(case_id)
        fixture_file = REPO_ROOT / fixture_path
        if not fixture_file.name.startswith(f"{number:02d}-"):
            report.error(f"{fixture_path}: authority number does not match filename")
        for field in ("original_file_sha256", "current_file_sha256", "non_prompt_fields_sha256"):
            if not isinstance(entry[field], str) or not re.fullmatch(r"[0-9a-f]{64}", entry[field]):
                report.error(f"{fixture_path}: invalid {field}")
        try:
            fixture_file.resolve().relative_to(REPO_ROOT.resolve())
            current_bytes = fixture_file.read_bytes()
            current = strict_json(current_bytes)
            if not isinstance(current, dict):
                raise ValueError("fixture JSON root must be an object")
            if current.get("id") != case_id:
                report.error(f"{fixture_path}: authority case_id does not match fixture")
            if hashlib.sha256(current_bytes).hexdigest() != entry["current_file_sha256"]:
                report.error(f"{fixture_path}: current fixture SHA mismatch")
            if non_prompt_hash(current) != entry["non_prompt_fields_sha256"]:
                report.error(f"{fixture_path}: non-prompt canonical SHA mismatch")
            if not amended:
                if entry["original_file_sha256"] != entry["current_file_sha256"]:
                    report.error(f"{fixture_path}: unrecorded fixture change")
                continue
            actual_changed.add(number)
            for field in ("original_prompt", "current_prompt", "reason", "original_fixture_text"):
                if not isinstance(entry[field], str) or not entry[field]:
                    raise ValueError(f"{field} must be a non-empty string")
            if current.get("prompt") != entry["current_prompt"]:
                report.error(f"{fixture_path}: current prompt does not match authority")
            if entry["original_prompt"] == entry["current_prompt"]:
                report.error(f"{fixture_path}: recorded prompt change is empty")
            original_bytes = entry["original_fixture_text"].encode("utf-8")
            if hashlib.sha256(original_bytes).hexdigest() != entry["original_file_sha256"]:
                report.error(f"{fixture_path}: original fixture SHA mismatch")
            else:
                original_byte_checks += 1
            original = strict_json(original_bytes)
            if not isinstance(original, dict) or original.get("prompt") != entry["original_prompt"]:
                raise ValueError("original prompt does not match original fixture text")
            if non_prompt_hash(original) != non_prompt_hash(current):
                report.error(f"{fixture_path}: amendment changed non-prompt fixture fields")
        except (OSError, UnicodeError, ValueError, TypeError) as exc:
            report.error(f"{fixture_path}: invalid task-input authority: {exc}")
    if seen_numbers != set(range(1, expected_count + 1)) or seen_paths != expected_paths:
        report.error(f"{rel(path)}: authority records do not cover every fixture exactly once")
    if actual_changed != set(changed):
        report.error(f"{rel(path)}: changed_cases does not match recorded prompt amendments")
    result["changed_cases"] = sorted(actual_changed)
    result["original_byte_checks"] = original_byte_checks
    if len(report.errors) == initial_errors:
        result["status"] = "checked"
    return result


def check_fixtures(report: Report) -> int:
    fixture_files = sorted(FIXTURES_ROOT.glob("*.json")) if FIXTURES_ROOT.is_dir() else []
    expected_count = EXPECTED_ACCEPTANCE["fixture_count"]
    if len(fixture_files) != expected_count:
        report.error(f"expected exactly {expected_count} benchmark fixtures, found {len(fixture_files)}")

    seen_ids: set[str] = set()
    seen_numbers: set[int] = set()
    for path in fixture_files:
        try:
            fixture = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            report.error(f"{rel(path)}: invalid JSON: {exc}")
            continue
        if not isinstance(fixture, dict):
            report.error(f"{rel(path)}: root must be an object")
            continue

        fixture_id = fixture.get("id")
        if (
            not isinstance(fixture_id, str)
            or not fixture_id.strip()
            or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", fixture_id)
        ):
            report.error(f"{rel(path)}: id must be a non-empty string")
        elif fixture_id in seen_ids:
            report.error(f"{rel(path)}: duplicate fixture id {fixture_id!r}")
        else:
            seen_ids.add(fixture_id)

        filename_match = re.fullmatch(r"(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)\.json", path.name)
        if not filename_match:
            report.error(f"{rel(path)}: filename must be NN-<fixture-id>.json")
        else:
            number = int(filename_match.group(1))
            seen_numbers.add(number)
            if isinstance(fixture_id, str) and filename_match.group(2) != fixture_id:
                report.error(
                    f"{rel(path)}: filename id {filename_match.group(2)!r} does not "
                    f"match fixture id {fixture_id!r}"
                )
            if fixture_id == INTEGRATED_FIXTURE_ID and number != 12:
                report.error(f"{rel(path)}: integrated fixture must be fixture 12")
            if number == 12 and fixture_id != INTEGRATED_FIXTURE_ID:
                report.error(
                    f"{rel(path)}: fixture 12 id must be {INTEGRATED_FIXTURE_ID!r}"
                )
            expected_workflow_number = WORKFLOW_FIXTURE_NUMBERS.get(fixture_id)
            if expected_workflow_number is not None and number != expected_workflow_number:
                report.error(
                    f"{rel(path)}: workflow fixture {fixture_id!r} must be fixture "
                    f"{expected_workflow_number}"
                )
            expected_workflow_id = next(
                (
                    workflow_id
                    for workflow_id, workflow_number in WORKFLOW_FIXTURE_NUMBERS.items()
                    if workflow_number == number
                ),
                None,
            )
            if expected_workflow_id is not None and fixture_id != expected_workflow_id:
                report.error(
                    f"{rel(path)}: fixture {number} id must be {expected_workflow_id!r}"
                )
            expected_observed_number = OBSERVED_FAILURE_FIXTURE_NUMBERS.get(fixture_id)
            if expected_observed_number is not None and number != expected_observed_number:
                report.error(
                    f"{rel(path)}: observed-failure fixture {fixture_id!r} must be fixture "
                    f"{expected_observed_number}"
                )
            expected_observed_id = next(
                (
                    observed_id
                    for observed_id, observed_number in OBSERVED_FAILURE_FIXTURE_NUMBERS.items()
                    if observed_number == number
                ),
                None,
            )
            if expected_observed_id is not None and fixture_id != expected_observed_id:
                report.error(
                    f"{rel(path)}: fixture {number} id must be {expected_observed_id!r}"
                )

        expected_fields = set(FIXTURE_BASE_FIELDS)
        if fixture_id in WORKFLOW_FIXTURE_NUMBERS:
            expected_fields.update({"stage_prompts", "initial_files"})
        elif fixture_id == INTEGRATED_FIXTURE_ID:
            expected_fields.add("stage_prompts")
        else:
            expected_fields.add("prompt")
        if set(fixture) != expected_fields:
            report.error(
                f"{rel(path)}: fields must be exactly {sorted(expected_fields)!r}; "
                f"got {sorted(fixture)!r}"
            )

        for field in ("id", "title", "material_origin"):
            value = fixture.get(field)
            if not isinstance(value, str) or not value.strip():
                report.error(f"{rel(path)}: {field} must be a non-empty string")
        if fixture.get("material_origin") != "synthetic":
            report.error(f"{rel(path)}: material_origin must be 'synthetic'")

        if fixture_id in WORKFLOW_FIXTURE_NUMBERS:
            check_workflow_case(fixture, path, report)
        elif fixture_id == INTEGRATED_FIXTURE_ID:
            stage_prompts = fixture.get("stage_prompts")
            if not isinstance(stage_prompts, dict) or set(stage_prompts) != {"review", "revise"}:
                report.error(
                    f"{rel(path)}: stage_prompts must contain exactly review and revise"
                )
            else:
                for stage in ("review", "revise"):
                    prompt = stage_prompts[stage]
                    if not isinstance(prompt, str) or not prompt.strip():
                        report.error(
                            f"{rel(path)}: stage_prompts.{stage} must be a non-empty string"
                        )
                if stage_prompts.get("review") == stage_prompts.get("revise"):
                    report.error(f"{rel(path)}: review and revise stage prompts must differ")
        else:
            prompt = fixture.get("prompt")
            if not isinstance(prompt, str) or not prompt.strip():
                report.error(f"{rel(path)}: prompt must be a non-empty string")

        skills = fixture.get("skills")
        valid_skills = check_nonempty_string_list(skills, "skills", path, report)
        for skill in valid_skills:
            if skill not in EXPECTED_SKILLS:
                report.error(f"{rel(path)}: fixture names non-bundle skill {skill!r}")
        if fixture_id in WORKFLOW_FIXTURE_NUMBERS:
            pass  # Validated with its staged contract above.
        elif fixture_id == INTEGRATED_FIXTURE_ID:
            if skills != PAPER_SKILLS:
                report.error(
                    f"{rel(path)}: fixture 12 must route Review and Revise in bundle order"
                )
        elif isinstance(skills, list) and len(skills) != 1:
            report.error(f"{rel(path)}: single-stage fixtures must route exactly one skill")

        scope = fixture.get("scope")
        if not isinstance(scope, dict) or set(scope) != {"authorized", "excluded", "output_language"}:
            report.error(
                f"{rel(path)}: scope must contain exactly authorized, excluded, and output_language"
            )
        else:
            check_nonempty_string_list(scope["authorized"], "scope.authorized", path, report)
            check_nonempty_string_list(scope["excluded"], "scope.excluded", path, report)
            if not isinstance(scope["output_language"], str) or not scope["output_language"].strip():
                report.error(f"{rel(path)}: scope.output_language must be a non-empty string")

        evidence = fixture.get("evidence")
        if not isinstance(evidence, dict) or not evidence:
            report.error(f"{rel(path)}: evidence must be a non-empty object")
        else:
            check_nonempty_text_tree(evidence, "evidence", path, report)

        for field in (
            "protected_tokens",
            "forbidden_actions",
            "hard_gates",
            "expected_behavior",
        ):
            check_nonempty_string_list(fixture.get(field), field, path, report)

        rubric = fixture.get("rubric")
        if not isinstance(rubric, list) or len(rubric) != 12:
            report.error(f"{rel(path)}: rubric must contain exactly 12 items")
            continue
        expected_rubric_ids = [f"R{index}" for index in range(1, 13)]
        actual_rubric_ids: list[object] = []
        for index, item in enumerate(rubric, 1):
            if not isinstance(item, dict) or set(item) != {"id", "criterion", "points"}:
                report.error(
                    f"{rel(path)}: rubric item {index} must contain exactly id, criterion, points"
                )
                actual_rubric_ids.append(None)
                continue
            actual_rubric_ids.append(item["id"])
            if not isinstance(item["id"], str) or not item["id"].strip():
                report.error(f"{rel(path)}: rubric item {index} id must be a non-empty string")
            if not isinstance(item["criterion"], str) or not item["criterion"].strip():
                report.error(
                    f"{rel(path)}: rubric item {index} criterion must be a non-empty string"
                )
            if type(item["points"]) is not int or item["points"] != 1:
                report.error(f"{rel(path)}: rubric item {index} must be worth integer 1")
        if actual_rubric_ids != expected_rubric_ids:
            report.error(
                f"{rel(path)}: rubric ids must be exactly R1 through R12 in order"
            )

    if seen_numbers != set(range(1, expected_count + 1)):
        report.error(
            f"fixture filename prefixes must be exactly 01 through {expected_count}; got "
            f"{sorted(seen_numbers)!r}"
        )
    return len(fixture_files)


def safe_install_path(install_root: Path, raw_path: str, report: Report) -> Path | None:
    if not isinstance(raw_path, str) or not raw_path:
        report.error("install path must be a non-empty string")
        return None
    root = install_root.resolve()
    relative = Path(raw_path)
    if relative.is_absolute() or ".." in relative.parts:
        report.error(f"install path must be relative and cannot contain '..': {raw_path}")
        return None
    target = root / relative
    resolved_target = target.resolve()
    try:
        resolved_target.relative_to(root)
    except ValueError:
        report.error(f"install path escapes --install-root: {raw_path}")
        return None
    return target


def byte_inventory(path: Path) -> dict[str, tuple[str, bytes | str | None]] | None:
    if not os.path.lexists(path):
        return None

    def describe(entry: Path) -> tuple[str, bytes | str | None]:
        mode = os.lstat(entry).st_mode
        if stat.S_ISLNK(mode):
            return ("symlink", os.readlink(entry))
        if stat.S_ISDIR(mode):
            return ("directory", None)
        if stat.S_ISREG(mode):
            return ("file", entry.read_bytes())
        return ("unsupported", None)

    root_description = describe(path)
    inventory: dict[str, tuple[str, bytes | str | None]] = {".": root_description}
    if root_description[0] != "directory":
        return inventory
    for entry in sorted(path.rglob("*")):
        inventory[entry.relative_to(path).as_posix()] = describe(entry)
    return inventory


def report_inventory_difference(
    source: Path,
    installed: Path,
    source_inventory: dict[str, tuple[str, bytes | str | None]],
    installed_inventory: dict[str, tuple[str, bytes | str | None]],
    report: Report,
) -> None:
    source_entries = set(source_inventory)
    installed_entries = set(installed_inventory)
    missing = sorted(source_entries - installed_entries)
    extra = sorted(installed_entries - source_entries)
    changed = sorted(
        entry
        for entry in source_entries & installed_entries
        if source_inventory[entry] != installed_inventory[entry]
    )
    details: list[str] = []
    if missing:
        details.append(f"missing={missing[:3]!r}")
    if extra:
        details.append(f"extra={extra[:3]!r}")
    if changed:
        details.append(f"changed={changed[:3]!r}")
    report.error(
        f"installed mapping differs byte-for-byte: {rel(source)} -> {installed}"
        + (f" ({'; '.join(details)})" if details else "")
    )


def source_to_install_path(
    source_path: str,
    install_root: Path,
    mappings: list[dict[str, str]],
    report: Report,
) -> Path | None:
    source = Path(source_path)
    matches: list[Path] = []
    for mapping in mappings:
        mapping_source = Path(mapping["source"])
        try:
            remainder = source.relative_to(mapping_source)
        except ValueError:
            continue
        target = safe_install_path(
            install_root,
            (Path(mapping["install_path"]) / remainder).as_posix(),
            report,
        )
        if target is not None:
            matches.append(target)
    if len(matches) != 1:
        report.error(
            f"source path {source_path} must resolve through exactly one install mapping; "
            f"found {len(matches)}"
        )
        return None
    return matches[0]


def install_label(path: Path, install_root: Path) -> str:
    try:
        return "<install-root>/" + path.absolute().relative_to(
            install_root.resolve()
        ).as_posix()
    except ValueError:
        return str(path)


def check_installed_skill_links(
    skill_dir: Path, install_root: Path, report: Report
) -> None:
    if not skill_dir.is_dir():
        report.error(f"{install_label(skill_dir, install_root)}: missing installed skill")
        return
    markdown_files = sorted(skill_dir.rglob("*.md"))
    for source in markdown_files:
        for raw_target in MARKDOWN_LINK_RE.findall(source.read_text(encoding="utf-8")):
            target = markdown_target(source, raw_target)
            if target is not None and not target.exists():
                report.error(
                    f"{install_label(source, install_root)}: broken installed relative "
                    f"link -> {raw_target}"
                )

    entrypoint = skill_dir / "SKILL.md"
    references_dir = skill_dir / "references"
    if references_dir.is_dir():
        for reference in sorted(references_dir.rglob("*.md")):
            if not is_markdown_reachable(entrypoint, reference):
                report.error(
                    f"{install_label(reference, install_root)}: installed reference is "
                    f"not reachable from {install_label(entrypoint, install_root)}"
                )


def check_install_root(
    install_root: Path, manifest: dict[str, object], report: Report
) -> int:
    if not install_root.is_dir():
        report.error(f"--install-root is not a directory: {install_root}")
        return 0
    mappings_value = manifest.get("install_mappings")
    if mappings_value != EXPECTED_INSTALL_MAPPINGS:
        report.error("cannot validate installation with an invalid install_mappings contract")
        return 0
    mappings: list[dict[str, str]] = EXPECTED_INSTALL_MAPPINGS

    for mapping in mappings:
        source = (REPO_ROOT / mapping["source"]).resolve()
        installed = safe_install_path(install_root, mapping["install_path"], report)
        if installed is None:
            continue
        source_inventory = byte_inventory(source)
        installed_inventory = byte_inventory(installed)
        if source_inventory is None:
            report.error(f"missing mapping source: {rel(source)}")
            continue
        if installed_inventory is None:
            report.error(
                f"missing installed mapping target: {install_label(installed, install_root)}"
            )
            continue
        expected_root_kind = mapping["kind"]
        if source_inventory["."][0] != expected_root_kind:
            report.error(
                f"{rel(source)}: declared kind {expected_root_kind!r} does not match source"
            )
        if installed_inventory["."][0] != expected_root_kind:
            report.error(
                f"{install_label(installed, install_root)}: declared kind "
                f"{expected_root_kind!r} does not match installed target"
            )
        if source_inventory != installed_inventory:
            report_inventory_difference(
                source, installed, source_inventory, installed_inventory, report
            )

    for skill in EXPECTED_SKILLS:
        installed_skill = safe_install_path(install_root, f"skills/{skill}", report)
        if installed_skill is not None:
            check_installed_skill_links(installed_skill, install_root, report)

    canonical_references = manifest.get("canonical_references")
    if isinstance(canonical_references, list):
        for item in canonical_references:
            if not isinstance(item, dict):
                continue
            source_path = item.get("path")
            consumers = item.get("consumers")
            if not isinstance(source_path, str) or not isinstance(consumers, list):
                continue
            installed_reference = source_to_install_path(
                source_path, install_root, mappings, report
            )
            if installed_reference is None or not installed_reference.is_file():
                if installed_reference is not None:
                    report.error(
                        f"missing installed canonical reference: "
                        f"{install_label(installed_reference, install_root)}"
                    )
                continue
            for consumer in consumers:
                if not isinstance(consumer, str):
                    continue
                entrypoint = safe_install_path(
                    install_root, f"skills/{consumer}/SKILL.md", report
                )
                if (
                    entrypoint is not None
                    and entrypoint.is_file()
                    and not is_markdown_reachable(entrypoint, installed_reference)
                ):
                    report.error(
                        f"installed canonical reference "
                        f"{install_label(installed_reference, install_root)} is not reachable "
                        f"from {install_label(entrypoint, install_root)}"
                    )

    provenance_files = manifest.get("provenance_files")
    if isinstance(provenance_files, list):
        for item in provenance_files:
            if not isinstance(item, dict):
                continue
            source_path = item.get("source")
            install_path = item.get("install_path")
            consumers = item.get("consumers")
            declared_digest = item.get("sha256")
            if (
                not isinstance(source_path, str)
                or not isinstance(install_path, str)
                or not isinstance(consumers, list)
                or not isinstance(declared_digest, str)
            ):
                continue
            installed_provenance = safe_install_path(install_root, install_path, report)
            if installed_provenance is None or not installed_provenance.is_file():
                if installed_provenance is not None:
                    report.error(
                        f"missing installed provenance file: "
                        f"{install_label(installed_provenance, install_root)}"
                    )
                continue
            installed_digest = hashlib.sha256(installed_provenance.read_bytes()).hexdigest()
            if installed_digest != declared_digest:
                report.error(
                    f"{install_label(installed_provenance, install_root)}: SHA-256 "
                    f"{installed_digest} does not match {declared_digest}"
                )
            for consumer in consumers:
                if not isinstance(consumer, str):
                    continue
                entrypoint = safe_install_path(
                    install_root, f"skills/{consumer}/SKILL.md", report
                )
                if (
                    entrypoint is not None
                    and entrypoint.is_file()
                    and not is_markdown_reachable(entrypoint, installed_provenance)
                ):
                    report.error(
                        f"installed provenance file "
                        f"{install_label(installed_provenance, install_root)} is not reachable "
                        f"from {install_label(entrypoint, install_root)}"
                    )
    return len(mappings)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--install-root",
        type=Path,
        help="optional staged or installed Codex root containing skills/ and research/",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = Report()
    skill_dirs, canonical_paths, provenance_paths, manifest = check_bundle(report)
    for skill_dir in skill_dirs:
        check_skill_structure(skill_dir, report)
        check_links_and_reachability(skill_dir, report)
    if skill_dirs:
        check_identifier_definitions(skill_dirs, report)
        check_cross_skill_links(skill_dirs, report)
        check_coverage_contract(report)
        check_interactive_clarification_contract(report)
        check_interface_boundary_contract(report)
        check_positioning_insight_contract(report)
        check_decision_history_contract(report)
    fixture_count = check_fixtures(report)
    from ste_benchmarks import validate_suites
    try:
        ste_manuscript_count, ste_authoring_count = validate_suites(REPO_ROOT)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        report.error(f"STE benchmark packaging: {exc}")
        ste_manuscript_count, ste_authoring_count = 0, 0
    task_input_authority = check_task_input_authority(manifest, report, ste_authoring_count)
    installed_mapping_count = 0
    if args.install_root is not None:
        installed_mapping_count = check_install_root(args.install_root, manifest, report)

    for message in report.warnings:
        print(f"WARNING: {message}")
    for message in report.errors:
        print(f"ERROR: {message}")
    print(
        f"Checked {len(skill_dirs)} skills, {len(canonical_paths)} canonical references, "
        f"{len(provenance_paths)} provenance file, and {fixture_count} benchmark fixtures "
        f"({ste_manuscript_count} STE manuscript cases); {ste_authoring_count} separate STE authoring cases"
        + (
            f"; byte-checked {installed_mapping_count} installed mappings."
            if args.install_root is not None
            else "."
        )
    )
    if task_input_authority["status"] == "legacy_without_marker":
        print("Task-input authority: legacy bundle without marker; record check not required.")
    else:
        print(
            f"Task-input authority: {task_input_authority['status']}; "
            f"{task_input_authority['record_count']} records; "
            f"sha256={task_input_authority.get('record_sha256', 'unavailable')}; "
            f"original byte checks={task_input_authority.get('original_byte_checks', 0)}."
        )
    if report.errors:
        print(f"FAILED with {len(report.errors)} error(s) and {len(report.warnings)} warning(s).")
        return 1
    print(f"PASS with {len(report.warnings)} warning(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
