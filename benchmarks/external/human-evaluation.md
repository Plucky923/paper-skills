# Human assessment of new ParaRev revisions

Protocol: `pararev-blind-human-adapted-v2`. This is a local, adapted assessment,
not the official ParaRev or ParaReval score. ParaReval's published distinction
between instruction relatedness, author acceptability and comparative writing
quality informs the questions; this project adds an explicit technical-meaning
gate. Labels for its fixed candidates never transfer to newly generated outputs.
[ParaReval, §§3.3–3.4](https://arxiv.org/html/2506.04772v1)

## Freeze the evaluation before judging

Freeze the source revision, selected paper groups, instruction filter, model,
runtime, skill snapshot and this protocol. Designate development and held-out
papers before using their judgments for changes. A different seed is not a new
independent test: ParaRev and ParaReval share papers and paragraphs.

Use `export-blind` on a current admitted paired run. Give each evaluator only
`judge-packet.jsonl` and this protocol. Keep `private-labels.json`, run logs,
prompts and `reference-context.jsonl` hidden. The author revision can anchor a
judge on one wording and is not verified meaning-preserving gold; any later
reference-assisted assessment must be recorded separately.

Keep at least two independent assessments for a quality comparison; one is
exploratory. Evaluators need the technical competence to distinguish a changed
claim from an editorial change. Do not use the same writing skill as the judge.
Preserve each evaluator's original decisions before any adjudication.

## Judge the input and each output

First assess whether the supplied paragraph and instruction are sufficient.
Missing context that matters makes the case `unresolved`, not a success or a
candidate error. Do not open the rest of the paper to silently expand this
paragraph-only task. The conservative instruction filter is only triage;
non-editable requests can still survive it.

For each output, record `pass`, `fail` or `unresolved` for both gates:

- **Technical meaning:** preserve material claims, actors, conditions,
  quantifiers, numbers, citations, equations, comparisons, limitations and
  evidence status. No invented explanation or stronger causal/general claim.
  Removing redundant words is allowed; losing a necessary premise is not.
- **Requested edit:** address the instruction within the supplied scope. A
  legitimate clarification request is not fabricated prose, but it also is not
  a completed revision. Distinguish missing input from a failed edit.

Then compare observable writing quality: precise terms and referents, explicit
logical relations, coherent sentence progression, an opening that establishes
the paragraph's role and an ending that completes or connects its supported
argument. Favor the abstraction level that explains the relevant principle or
design reason without hiding the necessary mechanism. Do not reward invented
motivation, a stock topic/conclusion formula, elaborate vocabulary or minimum
length. Concision means no avoidable burden **while retaining necessary
support**, not simply fewer words.

Record preference as `A`, `B`, `tie`, `neither` or `unresolved`, with short reasons
and the relevant input/output spans. A candidate with either failed gate cannot
win on style. If both fail, choose `neither`; if material uncertainty prevents
the comparison, choose `unresolved`. When both pass, use the quality comparison;
ties need not be broken. These judgments assess preservation of the supplied
research meaning, not whether the underlying research is scientifically true.

## Report without hiding failures

Freeze first-pass judgments before revealing condition identities. Report
scheduled cases and paper groups, failed/unfinished calls, exported pairs,
input-unresolved cases, per-condition gate failures and conditional pairwise
preferences separately. `export-summary.json` records unpaired scheduled cases;
do not discard that denominator when reporting completed-pair preferences.

Retain disagreements and any adjudicator's explanation alongside the original
annotations. If computing uncertainty over a larger sample, resample by source
paper, not by instruction, paragraph or annotator. Report sample size and split
exposure; do not turn a pilot into a superiority or acceptance claim. No
automatic human-label importer, aggregate preference scorer or acceptance
decision is implemented here. Systems-venue skill acceptance still uses the
[systems-specific procedure](../README.md).
