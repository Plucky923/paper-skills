# External benchmark admission

A source is admitted only when its task matches the skill, candidate-visible
inputs are sufficient, references remain isolated, evaluation is interpretable,
and the intended use respects the source's terms. The
[machine-readable policy](../benchmarks/external/admission.json) admits only
ParaRev paragraph revision and ParaReval judge calibration. Neither is an
official leaderboard replica or a systems-venue acceptance test.

## ParaRev: restricted paragraph revision

The released manual subset supplies original paragraphs, author revisions and
human edit instructions. Instructions are retrospective annotations over the
before/after pair, not independent requests from the original authors. The
candidate receives only the original paragraph and one instruction.
[Paper](https://aclanthology.org/2025.wraicogs-1.4/),
[pinned data](https://huggingface.co/datasets/taln-ls2n/pararev/blob/e61dc8a43ae067513208e75f79b49f9928dcbec3/pararev_manual_annot_subset.jsonl)

The adapter requires two instructions for a paragraph, with both annotations
restricted to rewriting or concision. It excludes explicit deletion, addition,
replacement, protected-content modification and external-lookup instructions.
This is conservative triage, not proof that every surviving edit preserves
meaning. The selection report records exclusions; if a task needs unavailable
context, its assessment remains unresolved.

The author revision is optional comparison context, not exact-match or
factual-correctness gold. New outputs need fresh, blinded assessments against
the supplied input, with technical-meaning and instruction-following gates
before style preference. The first-pass packet hides the author revision and
skill-condition labels. Follow the
[human assessment protocol](../benchmarks/external/human-evaluation.md), retaining
ties, neither-acceptable outcomes, uncertainty and evaluator disagreement.

This evaluates scoped paragraph editing. It does not establish full-paper
argument quality, soundness of the underlying research, figure understanding
or LaTeX preservation. Lexical similarity, shorter output and successful
execution cannot substitute for editorial and semantic assessment.

## ParaReval: independent judge calibration

The release supplies fixed A/B revisions, their original paragraph and edit
instruction, and human judgments. Its 1,548 primary comparisons and 129 second
annotations form 1,548 tasks, not 1,677 independent cases. An empty candidate
output is retained as an observed failure rather than replaced.
[Primary annotations](https://github.com/JourdanL/parareval/blob/1465234acae83a213b9121735a5c23c175197172/parareval.jsonl),
[second annotations](https://github.com/JourdanL/parareval/blob/1465234acae83a213b9121735a5c23c175197172/parareval_second_annotation.jsonl)

The questions distinguish instruction relatedness, editorial acceptability,
preference and relevant rewriting/concision quality. Acceptability is an
author-side editorial judgment, not independent scientific-fact verification.
Human labels, generator names and the author's reference paragraph stay outside
judge input.
[Question definitions](https://github.com/JourdanL/parareval/blob/1465234acae83a213b9121735a5c23c175197172/README.md),
[paper](https://aclanthology.org/2025.acl-long.335/)

The local scorer measures categorical agreement separately for each annotator,
excluding derived fields. It does not invent consensus, reproduce an official
aggregate score, or score newly generated revisions. Only the no-skill condition
is admitted: this task evaluates the judge, not the writing skill. One
comparison does not validate that judge; A/B-order robustness requires its own
correctly relabeled check.

## Usage and coverage limits

ParaRev declares CC BY-NC-SA 4.0 in its data card; ParaReval's repository declares
CC0. These declarations do not clear all underlying article rights. Keep source
text and derived outputs in ignored local directories for the stated
noncommercial research use; redistribution needs a separate rights check.
[ParaRev notice](https://huggingface.co/datasets/taln-ls2n/pararev/blob/e61dc8a43ae067513208e75f79b49f9928dcbec3/README.md),
[ParaReval license](https://github.com/JourdanL/parareval/blob/1465234acae83a213b9121735a5c23c175197172/LICENSE)

The datasets share papers and paragraphs. Define development and held-out groups
by paper across both sources before using judgments to tune a skill or judge.
Do not count related instructions or annotations as independent evidence.
Public-corpus training contamination remains unknown.

There is no admitted external systems-paper-review benchmark. These mainly
ML/NLP paragraph tasks cannot establish OSDI, SOSP, EuroSys, ATC or ASPLOS writing
quality on their own. The [systems-specific fixtures and acceptance
procedure](../benchmarks/README.md) remain necessary, with actual gate outcomes
and human assessments rather than inferred success.

## Execution boundary

Use the [external evaluation guide](../benchmarks/external/README.md) to download,
verify and prepare data. Source revisions and SHA-256 digests, admission/task
checks, candidate/reference separation, frozen skill content and ordered
per-call evidence are required for reproducibility. The runner supplies only
the selected revise instructions for paragraph editing and no writing skill for
judge calibration. Expanding this set requires the same input, scope, rights
and evaluation checks before enabling another adapter.
