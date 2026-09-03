# Direct Revision Protocol

Use one evidence-safe path for both existing prose and explicitly requested missing prose. Diagnose the scientific or rhetorical obligation first; write only after the intended claim and its support are clear.

## 1. Freeze scope and authority

Record internally:

```text
Editable object and explicit exclusions:
User's intended claim or outcome:
Source and output language:
Permitted restructuring depth:
Authoritative evidence:
Technical tokens and argument assets to preserve:
Missing context, evidence, source, or author decision:
```

Interpret scope narrowly:

| Input | Authorized action |
|---|---|
| Pasted passage | Return only its revised version |
| Notes/evidence plus a requested passage | Draft only that passage from the supplied material |
| Named paragraph, section, file, or file set | Edit only those objects |
| Named `main.tex` | Do not assume included files, figures, bibliography, or build configuration are in scope |
| Explicit whole LaTeX project | Freeze the authorized manuscript dependency set; exclude unrelated repository files |
| PDF without editable source | Propose changes or blockers; do not pretend to edit the PDF source |

Do not open out-of-scope material to repair an antecedent, definition, citation, figure, experiment, or fact. Make a safe local qualification or state exactly what context is needed.

Evidence authority is, in order: explicit author correction or decision; in-scope manuscript/artifact evidence; permitted primary-source verification; clearly labeled inference. Reviewer feedback proves that an objection exists, not that its factual suggestion is correct.

Classify every proposition as established, inferred, planned, or blocked. Never invent numbers or citations, assume implementation behavior, describe future experiments in the past tense, or use fluency as evidence.

## 2. Recover the one writing obligation

For existing prose, reduce symptoms to the earliest broken dependency: unsupported claim, missing premise, imprecise abstraction, misplaced evidence, unstable paragraph center, ambiguous sentence, or surface error. For missing prose, identify the local promise, supported answer, required premises/evidence, and final implication or handoff.

Do not build a paper-wide story model for a local passage. At larger scope, recover only the contribution contract, controlling thesis, and claim dependencies that govern the requested material.

For a nontrivial revision, preserve a compact internal map of the strongest existing assets: precise problem statement, counterexample, principle sentence, running example, decisive result, honest boundary, stable terminology, and distinctive voice. Preserve an asset because it performs a reasoning job, not merely because it sounds polished.

## 3. Choose the repair scale

Use the smallest coherent scope that closes the root cause:

- **Local:** The thesis and section role are sound; repair a bounded claim, dependency, paragraph, term, or sentence.
- **Structural:** Rebuild the authorized organization when theses compete, the contribution contract is wrong, mechanisms do not follow from problem-derived requirements, headline evidence does not support the main claim, or local edits retain contradictory promises.

For structural work, construct only the shortest supported dependency chain before drafting: problem → binding constraint → principle → realization → evidence → bounded implication. If different chains imply different scientific contributions, audiences, assumptions, or claims, stop for an author decision.

Repair in scientific-dependency order: factual support and claim strength; problem/principle/mechanism/evidence alignment; section and paragraph order; terminology and technical consistency; sentence economy and grammar. Do not polish material scheduled for deletion.

Permitted moves are: correct from authoritative evidence, expose an already warranted inference, reorganize supported material, calibrate or delete an unsupported claim, or add supported content. Missing evidence, source verification, context, or author intent remains a blocker.

## 4. Write and preserve meaning

Apply the writing method in `SKILL.md`. In particular, high-level prose must be both abstract and discriminating: it should name the exact constraint, change, consequence, and boundary rather than replacing mechanism detail with broad verbs such as `supports`, `enables`, or `improves`.

For Markdown or plain text, preserve heading levels, links, code spans, citations, identifiers, comments, and intentional formatting. For LaTeX, preserve commands, labels, citation keys, math, environments, comments, custom macros, escaping, encoding, and project conventions unless the requested correction targets them. Do not reflow unrelated lines.

Edit figures, tables, code, data, or scripts only when the user explicitly includes them. Never change data or analysis to obtain a favorable result. If a code or analysis correction changes outputs, manuscript claims that depend on the old outputs become unverified until the experiment is rerun and checked.

## 5. Validate the result

Re-read the complete frozen scope, not only edited sentences. Check:

1. the opening claim or question is answered;
2. each sentence adds a necessary proposition;
3. causal, conditional, comparative, and evidential relations are valid;
4. the high-level account passes substitution, prediction, and boundary tests;
5. each paragraph ending pays off or deliberately transfers its opening obligation;
6. facts, numbers, units, citations, identifiers, equations, macros, terminology, limitations, and evidence status remain correct.

Compile, render, lint, or test only when relevant dependencies are in scope and the action is authorized. Name what was actually checked; never use a clean tool result to claim publication readiness.

## 6. Return the deliverable first

For pasted material, output manuscript-ready prose before any commentary. For file edits, state the exact edited objects. Then mention only consequential claim/structure changes, validations actually performed, and unresolved blockers. Do not expose the internal maps or a long checklist unless requested.

If the user requested an iterative loop, report its final state compactly: locally clean within scope, blocked by a named missing item, or stopped because distinct edits no longer reduce the same defect. Confirm that Git was not used during the loop.

## Sources

This protocol applies the evidence and review standards in the sibling `systems-paper-review` references and the OSDI/SOSP corpus calibration recorded in its `source-registry.md`. Source keys include [OSDI-SOSP-CORPUS], [OSDI-BEST-SAMPLE], [SOSP-BEST-SAMPLE], [YSLAB-REVISION], [BRANDON-EVIDENCE], and [SIMCHOWITZ-WRITING]. Last reconciled 2026-09-03.
