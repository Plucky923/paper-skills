# Change Safety and Meaning Preservation

Use this reference before and after edits to files or protected technical content.
For existing prose, obey the paragraph-local limits in [revision-protocol.md](revision-protocol.md).
Compression and sentence order changes must keep each paragraph's purpose, content, and structure.

## Record the permitted object

1. Record each passage, range, file, figure, table, or other object that the user gives you permission to change.
2. Record each clear exclusion.
3. Read only that scope.
4. Edit only that scope.

A named root file does not include its dependencies unless the user adds them.
Keep unrelated user work and the working state at the start of this task.
During an automated review–revise loop, do not make these objects in the source tree:

- A backup
- A branch
- A commit
- A stash
- A patch file
- Generated output.

If scientific context for an edit is unavailable, keep the affected passage.
Give the specified dependency in a different issue note.
If a qualification changes claim strength, get the author's permission for that change.
Filesystem access does not give edit permission.

## Keep paragraph purpose and propositions

Before revision of existing prose, record these items:

```text
Controlling claim or local obligation:
Original paragraph boundaries, order, and content ownership:
Required premises and causal links:
Evidence and its scope:
Assumptions, costs, limitations, and failure cases:
Canonical terminology and deliberate voice:
Verbal redundancy removable without dropping a proposition:
```

After revision, compare each initial paragraph with its corresponding output paragraph.
A comparison of all facts in the document is not sufficient.
Keep each paragraph's scientific propositions, evidence, and limitations in that paragraph.
Keep their relations correct.
New words can make an existing relation clear.
For a new technical explanation, transferred fact, or changed paragraph role, get author input.

Remove repeated words only when each substantive detail stays.
For composition from notes, use the same list before you write.
Select only the material necessary for the requested argument.
Not each note must appear in the manuscript.

## Keep claim strength and evidence status

Do not increase these properties beyond the evidence:

- Universality or certainty
- Causality or novelty
- Performance or practicality
- Security or maturity.

Keep these distinctions:

- An observed property and a guaranteed property
- An association and a controlled causal effect
- Evaluated instances and a general population
- A prototype, simulation, implementation, deployment, and production use
- A planned experiment or mechanism and completed work
- A specified prior-work delta and `first` or `only`.

Keep the author's claim strength when evidence supports it.
If evidence is missing, keep the affected assertion unchanged.
If a correction changes the assertion, keep it unchanged until the author decides.
Give the missing evidence or decision in a different issue note.
Neither claim strengthening nor claim weakening is a usual wording repair.
A clear author correction can resolve the issue.

## Protect numbers and comparisons

For each important number, keep these attributes:

- Value, sign, unit, and precision
- Denominator, aggregation, baseline, and percentile
- Time window, hardware, and configuration
- Uncertainty.

Do a check of each applicable distinction:

- Percentage and percentage points
- Rate and total
- Mean and median
- Speedup and reduction
- Matched comparison conditions.

Recalculate a simple transformation only with authoritative inputs and an authoritative intended interpretation.
If values conflict, keep the issue open until a source resolves it.

## Protect citations and attribution

1. Do not change citation keys, links, author attribution, or quotations.
2. Before sentence movement or combination, record the proposition that each citation supports.
3. Make sure that a moved citation does not apply to a broader claim.
4. If external verification is permitted, use a primary source.

If support is missing, give the source gap.
Get the author's decision for the affected claim.
Do not invent a citation or a placeholder that looks like a supplied result.

## Protect equations, notation, and identifiers

Do not change these objects:

- Symbols, domains, indices, operators, and equations
- Algorithm steps, invariants, and complexity
- Code spans, system names, component names, APIs, and functions
- Files, flags, commands, and configuration keys
- Workload names, dataset names, hardware models, and versions
- Spelling, case, and punctuation.

Do a check of these relations and syntax:

- Definition order and dimensional consistency
- Prose–equation correspondence
- Braces and math-mode syntax
- Literal and display forms.

For a technical correction, get its own evidence.
A style revision does not give permission for a semantics change.

## Protect Markdown, LaTeX, figures, and tables

Keep these syntax objects unless the requested repair targets them:

- Commands, environments, comments, labels, references, and macros
- Escaping, links, headings, lists, and code fences
- Project conventions.

Keep these figure and table attributes:

- Values, categories, uncertainty, and missing results
- Labels, units, baselines, and normalization
- Order and visual semantics.

Keep a limitation near the claim or visual that it limits.
Compile or render only when all required dependencies are in scope.
Put writable output in a different directory from the source tree.
Do not change data, exclusion rules, scripts, or visual encodings to get a preferred result.

If a permitted scientific correction changes an output, give each dependent manuscript claim the unverified status.
Keep that status until the experiment or analysis runs again and passes an audit.

## Keep author intent and voice that helps the argument

Keep examples, counterexamples, principles, result framings, accurate boundaries, and deliberate voice when they help the reasoning.
Remove ambiguity, hype, and inconsistent synonyms without giving each passage the same rhythm.

If alternatives imply different scientific choices, keep the initial passage.
Give the choice to the author.
These choices include contribution hierarchy, audience, threat model, deployment setting, baseline, and trade-off.

For meaning-equivalent alternatives with a clear benefit, obey the optional-wording rules in [revision-protocol.md](revision-protocol.md).
Keep sufficient initial wording in the primary text.

## Final preservation check

Compare the full scoped result with the frozen record.
Make sure that each condition holds:

1. Each claim keeps each necessary premise, causal link, condition, and limitation.
2. Paragraph count, order, boundaries, roles, and content ownership stay unchanged, except for clear author changes.
3. Removed words do not remove a substantive proposition.
4. Evidence verbs, quantifiers, comparisons, and maturity labels keep their initial scientific strength.
5. An unchanged claim with missing support has a different issue note for the author.
6. Keep numbers, citations, equations, identifiers, terms, and document syntax the same.
   Apply a correction only with permission and its own evidence.
7. Only clearly permitted manuscript objects changed.
8. Decision records and other objects not in scope stay unchanged.
9. Each tool-result statement gives only the test that the tool did.

Correct an edit that violates the preservation contract directly.
During an automated loop, do not use Git for recovery.
