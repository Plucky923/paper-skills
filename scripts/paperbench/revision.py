"""Read-only adapters for the pinned ParaRev and ParaReval JSONL releases.

Only ``case['input']`` is candidate-visible. In particular, author revisions,
human judgments, model identities, and selection decisions are harness data.
Selection is a conservative triage heuristic, NOT proof of semantic fidelity.
The module uses only the Python 3.9 standard library and never writes files.
"""

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Tuple


PARAREV_FILE = "pararev_manual_annot_subset.jsonl"
PARAREVAL_FILE = "parareval.jsonl"
PARAREVAL_SECOND_FILE = "parareval_second_annotation.jsonl"
PARAREV_POLICY = "pararev-conservative-two-annotation-v1"

_ALLOWED_LABELS = frozenset(
    ("Rewriting_light", "Rewriting_medium", "Rewriting_heavy", "Concision")
)
# These deliberately over-exclude: even a legitimate request to remove a
# redundant word is deferred rather than certified as meaning-preserving.
_INSTRUCTION_RISKS = (
    (
        "explicit_deletion_or_omission_instruction",
        re.compile(r"\b(?:remove|removing|delete|deleting|omit|omitting|drop|"
                   r"discard|eliminate|eliminating)\b", re.IGNORECASE),
    ),
    (
        "explicit_addition_or_replacement_instruction",
        re.compile(r"\b(?:add|adding|insert|inserting|include|including|"
                   r"introduce|introducing|extend|expand|develop|update|"
                   r"updating|replace|replacing|substitute|substituting)\b",
                   re.IGNORECASE),
    ),
    (
        "protected_content_change_instruction",
        re.compile(r"\b(?:change|alter|correct|fix)\b[^.!?]*\b"
                   r"(?:citations?|references?|numbers?|values?|results?|"
                   r"equations?|formulas?|claims?|assumptions?|evidence|"
                   r"negative|positive)\b", re.IGNORECASE),
    ),
    (
        "external_information_instruction",
        re.compile(r"https?://|\b(?:browse|download|search|look\s+up)\b",
                   re.IGNORECASE),
    ),
)

_CATEGORY_QUESTIONS = {
    "Rewriting_light": "Which revision most improves academic wording and English?",
    "Rewriting_medium": "Which revision most improves readability and structure?",
    "Rewriting_heavy": "Which revision most improves readability and clarity?",
    "Concision": "Which revision is shorter while retaining all important ideas?",
}


def _read_jsonl(path: Path) -> List[Tuple[int, Dict[str, Any]]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as error:
                # Do not echo third-party manuscript text into diagnostics.
                raise ValueError("{}:{}: invalid JSON".format(path.name, line_number)) from error
            if not isinstance(row, dict):
                raise ValueError("{}:{}: expected an object".format(path.name, line_number))
            rows.append((line_number, row))
    return rows


def _text(row: Dict[str, Any], key: str, context: str) -> str:
    value = row.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError("{}: {} must be a nonempty string".format(context, key))
    return value


def _candidate_text(row: Dict[str, Any], key: str, context: str) -> str:
    # An empty output is an observed model failure, not missing benchmark data.
    value = row.get(key)
    if not isinstance(value, str):
        raise ValueError("{}: {} must be a string (empty is allowed)".format(context, key))
    return value


def _labels(value: Any, context: str) -> List[str]:
    if not isinstance(value, list) or any(not isinstance(label, str) for label in value):
        raise ValueError("{}: labels must be a list of strings".format(context))
    return list(value)


def _annotation(row: Dict[str, Any], slot: str, context: str) -> Dict[str, Any]:
    annotation = row.get(slot)
    if annotation is None:
        return {"labels": [], "instruction": "", "annotator": None, "missing": True}
    if not isinstance(annotation, dict):
        raise ValueError("{}: {} must be an object or null".format(context, slot))
    instruction = annotation.get("instruction")
    if not isinstance(instruction, str):
        raise ValueError("{}: {}.instruction must be a string".format(context, slot))
    return {
        "labels": _labels(annotation.get("annotation"), context + ":" + slot),
        "instruction": instruction,
        "annotator": annotation.get("annotator"),
        "missing": False,
    }


def _pararev_build(source_dir: Path) -> Tuple[List[dict], dict]:
    cases, decisions = [], []
    seen_ids = set()
    rows = _read_jsonl(Path(source_dir) / PARAREV_FILE)
    two_instruction_paragraphs = 0
    for line_number, row in rows:
        context = "{}:{}".format(PARAREV_FILE, line_number)
        paragraph_id = _text(row, "id_paragraph", context)
        if paragraph_id in seen_ids:
            raise ValueError(context + ": duplicate paragraph identifier")
        seen_ids.add(paragraph_id)
        original = _text(row, "parag_1", context)
        author_revision = _text(row, "parag_2", context)
        source_id = _text(row, "id_source", context)
        annotations = [_annotation(row, slot, context) for slot in ("annot_1", "annot_2")]
        both_instructions = all(item["instruction"].strip() for item in annotations)
        two_instruction_paragraphs += int(both_instructions)
        shared_reasons = []
        if not both_instructions:
            shared_reasons.append("outside_official_two_instruction_subset")
        for index, annotation in enumerate(annotations, 1):
            if not annotation["labels"]:
                shared_reasons.append("annot_{}:missing_labels".format(index))
            for label in annotation["labels"]:
                if label not in _ALLOWED_LABELS:
                    shared_reasons.append("annot_{}:excluded_label:{}".format(index, label))
            for reason, pattern in _INSTRUCTION_RISKS:
                if pattern.search(annotation["instruction"]):
                    shared_reasons.append("annot_{}:{}".format(index, reason))

        # Both annotators must pass, so an unsafe interpretation of the same
        # author revision cannot be hidden by selecting the other instruction.
        for index, annotation in enumerate(annotations, 1):
            slot = "annot_{}".format(index)
            reasons = list(shared_reasons)
            if annotation["missing"]:
                reasons.append("missing_annotation")
            if not annotation["instruction"].strip():
                reasons.append("missing_instruction")
            reasons = sorted(set(reasons))
            decisions.append({
                "paragraph_id": paragraph_id,
                "annotation_slot": slot,
                "source_line": line_number,
                "included": not reasons,
                "reasons": reasons,
            })
            if reasons:
                continue
            cases.append({
                "id": "pararev:{}:{}".format(paragraph_id, slot),
                "source": "pararev",
                "task": "revision",
                "group_id": "openreview:" + source_id,
                "input": {
                    "prompt": annotation["instruction"],
                    "material": {"paragraph": original},
                    "scope": {
                        "authorized": ["material.paragraph"],
                        "allowed_actions": ["revise the supplied paragraph"],
                        "excluded": ["other manuscript sections", "external research"],
                        "constraints": [
                            "Preserve supported technical meaning, material premises, results, and boundaries.",
                            "Preserve numbers, citations, equations, and evidence status.",
                            "Do not invent evidence or assume unavailable context.",
                        ],
                    },
                },
                "reference": {
                    "kind": "author_revision_not_verified_meaning_preserving",
                    "text": author_revision,
                    "use": "comparison context only; not exact-match or factual-correctness gold",
                },
                "metadata": {
                    "paragraph_id": paragraph_id,
                    "annotation_slot": slot,
                    "annotator": annotation["annotator"],
                    "labels": annotation["labels"],
                    "both_annotation_labels": [item["labels"] for item in annotations],
                    "source_file": PARAREV_FILE,
                    "source_line": line_number,
                    "selection_policy": PARAREV_POLICY,
                    "needs_human_semantic_check": True,
                    "instruction_origin": "human retrospective instruction from before/after paragraphs",
                    "official_split": "paper evaluation subset; HF split name is train",
                },
            })
    reason_counts = Counter(reason for decision in decisions for reason in decision["reasons"])
    report = {
        "source": "pararev",
        "policy": PARAREV_POLICY,
        "source_rows": len(rows),
        "annotation_slots": len(decisions),
        "official_two_instruction_paragraphs": two_instruction_paragraphs,
        "selected_cases": len(cases),
        "selected_paragraphs": len({case["metadata"]["paragraph_id"] for case in cases}),
        "excluded_annotation_slots": sum(not decision["included"] for decision in decisions),
        "exclusion_reason_counts": dict(sorted(reason_counts.items())),
        "decisions": decisions,
        "limitations": [
            "Heuristics conservatively reject explicit removal, addition, replacement, and external lookup instructions.",
            "Allowed labels and passing text checks do not prove preservation of important claims.",
            "Author revisions are not verified factual or exact-wording gold.",
            "The two instructions share a paragraph; split and bootstrap by paper, not by case.",
        ],
    }
    return cases, report


def load_pararev(source_dir: Path) -> List[dict]:
    """Return only conservative candidates; call the report function for exclusions."""
    return _pararev_build(source_dir)[0]


def pararev_selection_report(source_dir: Path) -> dict:
    """Return counts and every annotation-slot decision without manuscript text."""
    return _pararev_build(source_dir)[1]


def _pair_id(row: Dict[str, Any], context: str) -> int:
    pairing = row.get("id_pairing")
    if isinstance(pairing, bool) or not isinstance(pairing, int):
        raise ValueError(context + ": id_pairing must be an integer")
    return pairing


def _human_annotation(row: Dict[str, Any], context: str, origin: str) -> dict:
    annotator = _text(row, "annotator_eval", context)
    judgments = row.get("eval_annotation")
    if not isinstance(judgments, dict) or not judgments:
        raise ValueError(context + ": eval_annotation must be a nonempty object")
    return {"annotator": annotator, "origin": origin, "judgments": dict(judgments)}


def load_parareval(source_dir: Path) -> List[dict]:
    """Return fixed A/B judge tasks, merging second annotations by pairing ID.

    Human disagreement is retained, never collapsed into a fabricated consensus.
    The original author's reference paragraph is deliberately omitted from the
    task, as are the original generator names. Both JSONL files are required.
    """
    source_dir = Path(source_dir)
    primary = _read_jsonl(source_dir / PARAREVAL_FILE)
    secondary = _read_jsonl(source_dir / PARAREVAL_SECOND_FILE)
    cases, by_id, primary_rows = [], {}, {}
    for line_number, row in primary:
        context = "{}:{}".format(PARAREVAL_FILE, line_number)
        pairing = _pair_id(row, context)
        if pairing in by_id:
            raise ValueError(context + ": duplicate primary pairing identifier")
        paragraph_id = _text(row, "id_paragraph", context)
        components = paragraph_id.split(".")
        if len(components) != 3 or not all(components):
            raise ValueError(context + ": cannot derive source-paper group from paragraph identifier")
        labels = _labels(row.get("labels"), context)
        categories = {label: _CATEGORY_QUESTIONS[label] for label in labels if label in _CATEGORY_QUESTIONS}
        case = {
            "id": "parareval:{}".format(pairing),
            "source": "parareval",
            "task": "judge_calibration",
            "group_id": "openreview:" + components[0],
            "input": {
                "prompt": (
                    "Compare the fixed revisions A and B with the original paragraph and its instruction; "
                    "do not rewrite either candidate. Return JSON with relatedness_A and relatedness_B "
                    "(Yes strictly / Yes with additional modifications / No), acceptable "
                    "(Both / A only / B only / None), preference (Both / A / B / None), "
                    "and each category key supplied in material.category_questions "
                    "(Both / A / B / None). Acceptability is an author's editorial judgment, "
                    "not independent verification of the research facts."
                ),
                "material": {
                    "original_paragraph": _text(row, "original_paragraph", context),
                    "instruction": _text(row, "instruction", context),
                    "revision_A": _candidate_text(row, "model_A_paragraph", context),
                    "revision_B": _candidate_text(row, "model_B_paragraph", context),
                    "category_questions": categories,
                },
                "scope": {
                    "authorized": ["material"],
                    "allowed_actions": ["evaluate the supplied fixed A/B revisions"],
                    "excluded": ["new revision generation", "external research", "author reference revision", "human judgments"],
                },
            },
            "reference": {
                "kind": "human_pairwise_judgments",
                "human_annotations": [_human_annotation(row, context, "primary")],
            },
            "metadata": {
                "paragraph_id": paragraph_id,
                "pairing_id": pairing,
                "pararev_annotation_slot": _text(row, "pararev_annot", context),
                "labels": labels,
                "models": {"A": _text(row, "model_A", context), "B": _text(row, "model_B", context)},
                "source_file": PARAREVAL_FILE,
                "source_line": line_number,
                "fixed_ab_order": True,
                "author_revision_omitted": True,
                "correctness_means": "human editorial acceptability, not independent factual verification",
                "official_split": "no independent train/dev/test supplied; group by source paper",
                "secondary_annotation_count": 0,
                "empty_candidates": [
                    letter for letter in ("A", "B")
                    if not row["model_{}_paragraph".format(letter)].strip()
                ],
            },
        }
        cases.append(case)
        by_id[pairing] = case
        primary_rows[pairing] = row

    seen_secondary = set()
    identity_fields = (
        "id_paragraph", "instruction", "original_paragraph", "model_A_paragraph",
        "model_B_paragraph", "model_A", "model_B", "labels", "pararev_annot",
    )
    for line_number, row in secondary:
        context = "{}:{}".format(PARAREVAL_SECOND_FILE, line_number)
        pairing = _pair_id(row, context)
        if pairing not in by_id:
            raise ValueError(context + ": second annotation has no primary pairing")
        if pairing in seen_secondary:
            raise ValueError(context + ": duplicate secondary pairing identifier")
        seen_secondary.add(pairing)
        if any(row.get(field) != primary_rows[pairing].get(field) for field in identity_fields):
            raise ValueError(context + ": second annotation does not match the fixed primary A/B task")
        annotation = _human_annotation(row, context, "second_annotation")
        case = by_id[pairing]
        if annotation["annotator"] == case["reference"]["human_annotations"][0]["annotator"]:
            raise ValueError(context + ": second annotation repeats the primary annotator")
        case["reference"]["human_annotations"].append(annotation)
        case["metadata"]["secondary_annotation_count"] += 1
    return cases


def score_parareval(output_text: str, reference: dict) -> dict:
    """Score flat-JSON field agreement against every supplied human annotation.

    This is a LOCAL diagnostic, not the paper's metric or generation quality.
    Derived correctness booleans and extended_choice are excluded to avoid
    counting the same human decision repeatedly. Disagreement is retained;
    the reported empirical ceiling need not be 1.0. Invalid output has no score.
    """
    basic_choices = {
        "relatedness_A": {"Yes strictly", "Yes with additional modifications", "No"},
        "relatedness_B": {"Yes strictly", "Yes with additional modifications", "No"},
        "acceptable": {"Both", "A only", "B only", "None"},
        "preference": {"Both", "A", "B", "None"},
    }
    all_choices = dict(basic_choices)
    all_choices.update({key: {"Both", "A", "B", "None"} for key in _CATEGORY_QUESTIONS})
    if not isinstance(reference, dict):
        raise ValueError("Expected a human pairwise-judgment reference object")
    annotations = reference.get("human_annotations")
    if reference.get("kind") != "human_pairwise_judgments" or not isinstance(annotations, list) or not annotations:
        raise ValueError("Expected nonempty human pairwise judgments, not revision references")
    expected_fields = set(basic_choices)
    validated_annotations = []
    for annotation in annotations:
        if not isinstance(annotation, dict) or not isinstance(annotation.get("judgments"), dict):
            raise ValueError("Malformed human annotation")
        judgments = annotation["judgments"]
        if not set(basic_choices).issubset(judgments):
            raise ValueError("Human annotation lacks a required judgment")
        included = {key: value for key, value in judgments.items() if key in all_choices}
        if any(not isinstance(value, str) or value not in all_choices[key] for key, value in included.items()):
            raise ValueError("Human annotation contains an unsupported judgment value")
        expected_fields.update(included)
        validated_annotations.append((annotation, included))
    result = {
        "metric": "local_parareval_field_agreement_v1",
        "is_official_metric": False,
        "measures": "agreement with human editorial judgments, not factual truth or generated revision quality",
        "valid": False,
        "errors": [],
        "field_agreement": None,
        "matched_fields": 0,
        "compared_fields": 0,
        "per_annotation": [],
        "per_field": {},
    }

    def unique_object(pairs):
        parsed = {}
        for key, value in pairs:
            if key in parsed:
                raise ValueError("duplicate JSON key")
            parsed[key] = value
        return parsed

    try:
        prediction = json.loads(output_text, object_pairs_hook=unique_object)
    except (ValueError, TypeError):
        result["errors"].append("Output must be a single valid JSON object with no duplicate keys or code fences")
        return result
    if not isinstance(prediction, dict):
        result["errors"].append("Output must be a JSON object")
        return result
    if set(prediction) != expected_fields:
        result["errors"].append("Output keys must be exactly: " + ", ".join(sorted(expected_fields)))
    for key in sorted(expected_fields & set(prediction)):
        value = prediction[key]
        if not isinstance(value, str) or value not in all_choices[key]:
            result["errors"].append("Invalid categorical value for " + key)
    if result["errors"]:
        return result

    expected_values = {key: Counter() for key in expected_fields}
    for annotation, judgments in validated_annotations:
        matches = {key: prediction[key] == value for key, value in judgments.items()}
        for key, value in judgments.items():
            expected_values[key][value] += 1
        matched, compared = sum(matches.values()), len(matches)
        result["matched_fields"] += matched
        result["compared_fields"] += compared
        result["per_annotation"].append({
            "annotator": annotation.get("annotator"),
            "origin": annotation.get("origin"),
            "matched_fields": matched,
            "compared_fields": compared,
            "field_agreement": matched / compared,
            "matches": matches,
        })
    result["valid"] = True
    result["field_agreement"] = result["matched_fields"] / result["compared_fields"]
    result["per_field"] = {
        key: {
            "prediction": prediction[key],
            "human_value_counts": dict(sorted(values.items())),
            "matched_annotations": values[prediction[key]],
            "compared_annotations": sum(values.values()),
            "has_human_disagreement": len(values) > 1,
        }
        for key, values in sorted(expected_values.items())
    }
    result["empirical_human_agreement_ceiling"] = sum(max(values.values()) for values in expected_values.values()) / result["compared_fields"]
    return result
