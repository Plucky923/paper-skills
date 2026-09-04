# Direct Composition and Revision Protocol

Use this protocol for the ordinary writer-first path. It shares one evidence and output contract while routing composition and revision through different starting states.

## 1. Freeze scope and authority

Record internally:

```text
Editable text or file objects:
Explicit exclusions and unavailable context:
Compose or revise:
Requested unit and reader obligation:
Source and output language:
Author's intended claim or outcome:
Permitted restructuring depth:
Authoritative evidence:
Protected technical content:
Missing evidence, context, source, or author choice:
```

Interpret scope narrowly:

| Input | Authorized action |
|---|---|
| Pasted prose | Revise only that prose and return it in chat. |
| Notes or evidence plus a requested passage | Compose only that passage from the supplied material. |
| Named paragraph, section, file, or file set | Edit only those objects. |
| Named `main.tex` | Treat included files, bibliography, figures, and build configuration as unavailable unless separately named. |
| Explicit whole LaTeX project | Freeze the manuscript dependency set needed for that paper; unrelated repository files remain outside scope. |
| PDF without editable source | Return proposed prose or blockers; the PDF itself remains unchanged. |

When an antecedent, definition, citation, figure, experiment, or fact lies outside scope, either write a locally safe formulation or name the exact missing context. Accessibility is not authorization.

Rank evidence as follows: an explicit author correction or decision; in-scope manuscript or artifact evidence; a permitted and verified primary source; a clearly marked inference from established premises. Reviewer feedback establishes that an objection exists, not that its factual suggestion is correct.

Treat review and venue-audit output as editorial metadata unless authorized evidence independently establishes the proposition. Do not import severity labels, evidence-state labels, venue taxonomy, pillar mappings, reviewer hypotheses, or repair directions into manuscript prose merely because they appear in an upstream review. A claim marked missing, blocked, unsupported, or unresolved must not reappear as a positive fit, novelty, causality, or compliance statement during revision.

Keep established, inferred, planned, and blocked propositions distinct. Fluency does not promote a plan, hypothesis, placeholder, or plausible mechanism into completed work.

## 2. Route the writing mode

### Compose from evidence or notes

Use this branch when the requested prose does not yet exist.

1. Identify the section or paragraph contract in [writing-core.md](writing-core.md). When contribution type controls the contract, route through [paper-archetypes.md](paper-archetypes.md).
2. Extract the strongest supported answer, the premises required to understand it, the evidence that changes its credibility, and its material boundary.
3. Build the shortest dependency outline that completes the reader obligation. Select evidence by function; do not preserve note order or include every true detail.
4. Draft one manuscript-ready version. Add an inferential bridge only when it follows from established premises; otherwise narrow the claim or expose the missing item.

Composition is complete when the requested unit performs its section role, each material claim has support, and omitted notes do not change the decision case.

### Revise existing prose

Use this branch when prose already exists.

1. Recover the passage's governing claim or question, supported answer, evidence, boundary, and deliberate voice.
2. Diagnose the earliest broken dependency: false or overbroad claim, missing premise, imprecise abstraction, misplaced evidence, unstable paragraph center, ambiguous sentence, or surface error.
3. Choose the smallest coherent repair scale: phrase, sentence, paragraph, section, or the complete authorized argument. `Smallest` means the least scope that closes the root cause, not the fewest changed words.
4. Rewrite coherently. Reorder, split, merge, delete, demote, or add supported material as required by the repair; avoid polishing text that the repair removes.

Revision is complete when the root cause is closed across the entire scoped passage and the repair introduces no semantic or rhetorical regression.

## 3. Resolve structural uncertainty before prose

Use [revision-strategies.md](revision-strategies.md) when theses compete, the contribution contract is wrong, mechanisms do not follow from requirements, headline evidence does not support the central claim, or several findings interact.

When two defensible versions imply different technical meanings, contribution hierarchies, assumptions, audiences, or trade-offs, present the alternatives and request an author decision. Ordinary wording choices should resolve to one conservative draft.

## 4. Write at the right level

Apply [writing-core.md](writing-core.md) as the single source for argument, high-level exposition, paragraphs, sentences, wording, section contracts, and concision. Apply [chinese-writing.md](chinese-writing.md) when the source or output prose is Chinese or when translating from Chinese.

For file edits and fragile technical content, take the preservation snapshot and run the checks in [change-safety.md](change-safety.md). Edit figures, tables, code, data, or scripts only when the user explicitly includes those objects. A correction that changes experimental output leaves dependent manuscript claims unverified until the relevant evidence is regenerated and checked.

## 5. Run the lightweight gate

Re-read the complete frozen scope, not only changed sentences. Confirm:

1. the requested section or paragraph obligation is discharged;
2. the problem, intellectual move, realization, evidence, and boundary form the appropriate dependency chain;
3. every high-level claim passes distinction, prediction, falsification, and evidence tests;
4. each paragraph has one discoverable and resolved obligation without a forced opening or ending template;
5. each sentence has one dominant assertion, valid logical relations, explicit scope, unique referents, and stable terminology;
6. the result is the shortest complete argument, with no lost premise, causal bridge, evidence scope, cost, or limitation;
7. facts, numbers, units, citations, equations, identifiers, macros, and evidence status remain correct.
8. review labels, venue-audit language, and unresolved propositions have not leaked into manuscript prose as facts.

Compile, render, lint, or test only when the relevant dependencies are explicitly in scope and the action is authorized. State what a tool actually checked; a clean tool result does not establish publication readiness.

Use [convergence-loop.md](convergence-loop.md) instead of repeating ad hoc paraphrases when the user explicitly requests iteration or interacting edits require a fixed-point search.

## 6. Return the deliverable first

For pasted material, lead with the manuscript-ready prose. For file edits, name the exact edited objects. Then report only:

- a consequential claim, structure, or content deletion/change;
- validation actually performed;
- a blocker that requires evidence, context, source verification, or author choice.

Keep internal maps and diagnostics private unless requested. Do not create a separate report file unless the user asks for one.
