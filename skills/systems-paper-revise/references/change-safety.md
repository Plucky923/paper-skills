# Change Safety and Meaning Preservation

Use this reference before and after editing files or fragile technical content. For existing prose, apply the paragraph-local boundary in [revision-protocol.md](revision-protocol.md); compression and sentence reordering must preserve each paragraph's purpose, content, and document structure.

## Freeze the authorized object

- Record the exact passage, range, file, figure, table, or other object that may change and every explicit exclusion.
- Read and edit only that scope. A named root file does not include its dependencies unless the user adds them.
- Preserve unrelated user work and working state. During an automated review–revise loop, create no backup, branch, commit, stash, patch file, or generated output inside the source tree.

If an edit needs unavailable scientific context, preserve the affected passage and report the exact dependency. A changed qualification requires author authority when it changes claim strength. Never infer authorization from filesystem access.

## Preserve paragraph purpose and propositions

Before revising existing prose, record:

```text
Controlling claim or local obligation:
Original paragraph boundaries, order, and content ownership:
Required premises and causal links:
Evidence and its scope:
Assumptions, costs, limitations, and failure cases:
Canonical terminology and deliberate voice:
Verbal redundancy removable without dropping a proposition:
```

After revision, compare each original paragraph with its corresponding output paragraph, not just the document-wide set of facts. Its substantive propositions, evidence, and limitations must remain correctly related and in that paragraph. New wording may clarify those relations; a new technical explanation, transferred fact, or changed paragraph role requires author input. Deleting repeated wording is not permission to discard a substantive detail.

For composition from notes, use the same list prospectively: select only material required by the requested argument rather than treating every note as content that must appear.

## Preserve claim strength and evidence status

Revision cannot increase universality, certainty, causality, novelty, performance, practicality, security, or maturity beyond the evidence. Keep the following distinctions intact:

- observed property versus guaranteed property;
- association versus controlled causal effect;
- evaluated instances versus a general population;
- prototype, simulation, implementation, deployment, and production use;
- planned experiment or mechanism versus completed work;
- exact prior-work delta versus `first` or `only`.

Retain the author's supported claim strength. If support is missing or a correction would change the assertion, keep the affected passage unchanged and flag it for the author's decision. Neither strengthening nor weakening a scientific claim is a routine wording fix. An explicit author correction may resolve it.

## Protect numbers and comparisons

For every material number, preserve its value, sign, unit, precision, denominator, aggregation, baseline, percentile, time window, hardware or configuration, and uncertainty. Check percentage versus percentage points, rate versus total, mean versus median, speedup versus reduction, and matched comparison conditions.

Recompute a simple transformation only when its inputs and intended interpretation are authoritative. Conflicting values remain a blocker until a source resolves them.

## Protect citations and attribution

- Keep citation keys, links, author attribution, and quoted material exact.
- Record which proposition each citation supports before moving or merging sentences.
- Ensure a relocated citation has not acquired a broader claim.
- Verify externally only when permitted, using a primary source. Missing support requires a named source gap and an author decision; never invent a citation or placeholder that looks real.

## Protect equations, notation, and identifiers

Preserve symbols, domains, indices, operators, equations, algorithm steps, invariants, complexity, code spans, system and component names, APIs, functions, files, flags, commands, configuration keys, workload and dataset names, hardware models, versions, spelling, case, and punctuation.

Check definition order, dimensional consistency, prose–equation correspondence, brace and math-mode integrity, and literal versus display forms. A technical correction needs its own evidence; stylistic revision is not authority to alter semantics.

## Protect Markdown, LaTeX, figures, and tables

- Preserve commands, environments, comments, labels, references, macros, escaping, links, headings, lists, code fences, and project conventions unless the requested repair targets them.
- Preserve plotted and tabulated values, categories, uncertainty, missing results, labels, units, baselines, normalization, order, and visual semantics.
- Keep a limitation close enough to the claim or visual it constrains.
- Compile or render only when all required dependencies are in scope and writable output can be isolated outside the source tree.

Never change data, exclusion rules, scripts, or visual encodings to obtain a favorable result. When an authorized scientific correction changes an output, mark every dependent manuscript claim unverified until the experiment or analysis is rerun and audited.

## Preserve author intent and useful voice

Retain strong examples, counterexamples, principle statements, result framings, honest boundaries, and deliberate voice when they perform a reasoning job. Remove ambiguity, hype, and synonym drift without flattening every passage into the same cadence.

When alternatives imply different contribution hierarchies, audiences, threat models, deployment settings, baselines, or trade-offs, preserve the original passage and present the choice. Clearly beneficial meaning-equivalent alternatives follow the optional-wording contract in [revision-protocol.md](revision-protocol.md); adequate original wording remains in the main text.

## Final preservation check

Verify the complete scoped result against the frozen record:

1. the resulting claims retain every necessary premise, causal link, condition, and limitation;
2. paragraph count, order, boundaries, roles, and content ownership are preserved unless explicitly changed by the author; removed wording does not remove a substantive proposition;
3. evidence verbs, quantifiers, comparisons, and maturity labels remain calibrated, or an unchanged original claim is separately flagged for author resolution;
4. numbers, citations, equations, identifiers, terminology, and document syntax remain exact;
5. only explicitly authorized manuscript objects changed; decision records and other out-of-scope objects remain unchanged;
6. every tool result is described only for what it actually tested.

An unsafe edit should be corrected directly. During an automated loop, do not use Git as the recovery mechanism.
