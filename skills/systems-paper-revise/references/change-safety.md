# Change Safety and Meaning Preservation

Use this reference before and after editing files or fragile technical content. Revision may select, compress, and reorganize material; it must preserve the scientific meaning and document structure on which the selected argument depends.

## Freeze the authorized object

- Record the exact passage, range, file, figure, table, or other object that may change and every explicit exclusion.
- Read and edit only that scope. A named root file does not include its dependencies unless the user adds them.
- Preserve unrelated user work and working state. During an automated review–revise loop, create no backup, branch, commit, stash, patch file, or generated output inside the source tree.

If an edit needs unavailable context, make a safe local qualification or report the exact dependency. Never infer authorization from filesystem access.

## Preserve the decision case, not every sentence

Before revising existing prose, record:

```text
Controlling claim or local obligation:
Required premises and causal links:
Evidence and its scope:
Assumptions, costs, limitations, and failure cases:
Canonical terminology and deliberate voice:
True but secondary details eligible for deletion or demotion:
```

After revision, compare semantic propositions rather than word overlap. Every element required for the resulting claim must remain present and correctly related. A supported but nonessential detail may be omitted when it does not change scientific interpretation; report an omission that changes emphasis, reproducibility, or the apparent contribution.

For composition from notes, use the same list prospectively: select only material required by the requested argument rather than treating every note as content that must appear.

## Preserve claim strength and evidence status

Revision cannot increase universality, certainty, causality, novelty, performance, practicality, security, or maturity beyond the evidence. Keep the following distinctions intact:

- observed property versus guaranteed property;
- association versus controlled causal effect;
- evaluated instances versus a general population;
- prototype, simulation, implementation, deployment, and production use;
- planned experiment or mechanism versus completed work;
- exact prior-work delta versus `first` or `only`.

Choose the strongest formulation the evidence supports, not automatically the most forceful or the most hedged. A qualifier cannot substitute for evidence when the claim would become empty.

## Protect numbers and comparisons

For every material number, preserve its value, sign, unit, precision, denominator, aggregation, baseline, percentile, time window, hardware or configuration, and uncertainty. Check percentage versus percentage points, rate versus total, mean versus median, speedup versus reduction, and matched comparison conditions.

Recompute a simple transformation only when its inputs and intended interpretation are authoritative. Conflicting values remain a blocker until a source resolves them.

## Protect citations and attribution

- Keep citation keys, links, author attribution, and quoted material exact.
- Record which proposition each citation supports before moving or merging sentences.
- Ensure a relocated citation has not acquired a broader claim.
- Verify externally only when permitted, using a primary source. Missing support requires qualification or a named source gap; never invent a citation or placeholder that looks real.

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

When several versions remain accurate but imply different contribution hierarchies, audiences, threat models, deployment settings, baselines, or trade-offs, stop at the choice and present its consequences. Resolve ordinary stylistic alternatives to one conservative version.

## Final preservation check

Verify the complete scoped result against the frozen record:

1. the resulting claims retain every necessary premise, causal link, condition, and limitation;
2. omitted material is nonessential or has been reported as a consequential deletion;
3. evidence verbs, quantifiers, comparisons, and maturity labels remain calibrated;
4. numbers, citations, equations, identifiers, terminology, and document syntax remain exact;
5. no out-of-scope or persistent object changed;
6. every tool result is described only for what it actually tested.

An unsafe edit should be corrected directly. During an automated loop, do not use Git as the recovery mechanism.
