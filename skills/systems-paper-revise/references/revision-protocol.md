# Direct Revision Protocol

This protocol converts an adversarial finding ledger into direct, evidence-safe edits within a frozen scope. Revision may change wording, paragraph structure, section structure, and claim strength, but may not create scientific support that does not exist.

## 1. Freeze the revision contract

Record before editing:

```text
Editable scope:
Explicitly out of scope:
Input form: pasted text | Markdown | LaTeX | other editable text | PDF only
Source language:
Requested output language:
Named venue/cycle/track:
Requested depth: surface | sentence | paragraph | section | full scoped material
Review feedback supplied:
External verification permitted:
Technical tokens/invariants to preserve:
Known missing context/evidence:
```

Interpret scope narrowly:

| User supplies | Revision behavior |
|---|---|
| Pasted passage | Revise only that passage and return it in chat |
| Named paragraph/section in a file | Edit only that range; do not read or edit other ranges unless added to scope |
| Named file | Edit that file; imported/included files remain out of scope |
| Named `main.tex` or LaTeX root file | Edit only that root file; dependency names may be enumerated but dependency contents remain out of scope |
| Named file set | Edit only those files |
| Explicit whole LaTeX project | Freeze the authorized transitive manuscript dependency manifest before editing; unrelated repository files remain out of scope |
| PDF only | Review and propose a revision/blocker; do not pretend the PDF is an editable source |
| Whole paper/project | Revise the explicitly included manuscript/artifact scope; preserve unrelated repository content |

If an edit needs an antecedent, definition, citation, figure, experiment, or fact outside scope, do not open it. Either make a safe local qualification or report the exact context needed.

## 2. Establish authoritative evidence

Rank evidence for revision:

1. Explicit user correction or decision.
2. In-scope primary manuscript/artifact evidence.
3. Externally verified primary/official source, when permitted.
4. Reasoned inference labeled as such.

Reviewer feedback is evidence of a reader objection, not automatically evidence that its proposed fact or solution is correct. Verify factual suggestions before incorporating them.

Never use:

- plausible-looking numbers;
- invented citations or bibliographic metadata;
- assumed implementation behavior;
- hypothetical experiments written in past tense;
- future work described as completed;
- placeholder claims silently converted into facts;
- a linter or language model's confidence as scientific evidence.

## 3. Convert findings into a revision ledger

For each in-scope finding, record:

| Finding | Root cause | Affected claim | Status | Evidence available | Permitted repair | Blocker | Resolution test |
|---|---|---|---|---|---|---|---|

Classify the repair:

- `E1 — direct correction`: grammar, typo, broken reference, local contradiction with a known authoritative value;
- `E2 — explicit reasoning`: make an already supported premise, causal link, definition, or boundary visible;
- `E3 — structural repair`: reorder, split, merge, or refocus in-scope material without adding facts;
- `E4 — claim calibration`: narrow quantifier, verb, scope, generality, causality, guarantee, novelty, or magnitude to match evidence;
- `E5 — supported addition`: add information already present in the in-scope evidence or an allowed verified source;
- `B1 — evidence blocker`: new measurement, result, implementation fact, raw data, or proof required;
- `B2 — source blocker`: citation choice/support or factual verification unresolved;
- `B3 — context blocker`: necessary material lies outside scope;
- `B4 — author decision`: multiple technically meaningful choices cannot be selected without intent.

Only `E1`–`E5` authorize an edit. `B1`–`B4` remain visible and stop false convergence.

## 4. Prioritize by scientific dependency

Edit in this order:

1. Correct facts, contradictions, and unsupported central claims.
2. Align problem, contribution, assumptions, mechanism, and evidence.
3. Repair claim-to-evidence and section-promise mappings.
4. Repair section/paragraph dependency order.
5. Normalize terms, notation, figures/tables, citations, and LaTeX.
6. Improve sentence grammar, concision, rhythm, and optional style.

Do not polish text scheduled for deletion or disguise a missing argument with more fluent prose.

## 5. Make coherent direct edits

### Pasted text

- Preserve its boundaries and return only the revised passage plus concise change/blocker notes.
- Do not invent surrounding transitions. If the first/last sentence depends on missing context, retain it or flag the risk.
- Preserve source language unless translation is requested.

### Markdown and plain text

- Preserve heading level, links, code spans/blocks, citations, identifiers, comments, and intentional formatting.
- Do not reflow unrelated lines merely for formatting.

### LaTeX

- Preserve commands, labels, citation keys, math, environments, comments, custom macros, escaping, and file encoding unless the change explicitly targets them.
- Edit prose inside commands/environments only with correct brace and mode awareness.
- Do not replace project conventions with preferred packages or macros.
- Compile/render only when the relevant project inputs are in scope and the toolchain exists; no unsolicited installation.

### Figures, tables, code, data, and scripts

- Edit them only when each object is explicitly in scope and the user requested direct revision.
- Never alter data or analysis merely to obtain a favorable result.
- A visual redesign must preserve quantitative values and encodings or clearly document an evidence-backed correction.
- A code/script fix may change experimental results; then previous manuscript claims become unverified until rerun with authorization and evidence.

## 6. Batch and validate each revision

Use coherent batches by root cause. After each batch:

1. Re-read the whole frozen scope.
2. Check preserved technical tokens and evidence values.
3. Reapply all relevant sibling `systems-paper-review` rules.
4. Compile/render/lint/test only where authorized and relevant. In multi-agent mode, only the root may run command-producing validation, serialized between reviewer waves with writable output isolated outside the source tree.
5. Update the ledger: `resolved`, `improved but open`, `blocked`, `regressed`, or `new`.

Do not accept a local rewrite if it creates a new unsupported claim, changes a number's denominator, breaks a cross-reference, moves a limitation away from its claim, or makes terminology less stable.

## 7. Output and handoff

Report:

### Scope revised

Name exact passage/file/range/object. Explicitly state out-of-scope context was not inspected.

### Substantive changes

Group by:

- argument and claim calibration;
- technical/evidence alignment;
- structure and flow;
- terminology/figures/LaTeX;
- sentence-level prose.

### Verification

State review rule families re-run, compilation/render/lint/test actually performed, and limits. Do not say `validated` without naming what was validated.

### Loop result

State rounds and exactly one status:

- `fixed point — no actionable issue remains within scope`;
- `blocked — only evidence/context/source/author decisions remain`;
- `stopped — edits oscillate or no longer reduce the ledger`.

### Blockers

For each blocker, give the claim/location, missing item, why prose cannot solve it, and the observable condition that unblocks it.

### Human review handoff

State that no Git command was used during the loop. Invite the human to inspect the final Git diff and provide feedback. Do not run Git unless the user separately asks after the loop.

## 8. Revision anti-patterns

Never:

- broaden scope to “make the story consistent” without permission;
- accept reviewer assertions as facts;
- strengthen novelty, causality, guarantees, or generality for rhetorical effect;
- add a fake citation placeholder that looks real;
- rewrite exact measurements into a different metric without data;
- remove limitations merely because they weaken the pitch;
- silently change equation, algorithm, code identifier, or macro semantics;
- treat optional style preferences as convergence blockers;
- create `.bak`, “original,” or version-copy files;
- use Git during the automated loop;
- claim publication readiness from local automatic convergence.

## Sources

This protocol uses the evidence and review standards in the sibling `systems-paper-review` references, especially `review-protocol.md` and `source-registry.md`, and workflow patterns from [OPENAI-SKILL-CREATOR], [YSLAB-REVISION], [BRANDON-EVIDENCE], and [SIMCHOWITZ-WRITING]. Source keys are defined in the sibling registry. Last reconciled 2026-09-01.
