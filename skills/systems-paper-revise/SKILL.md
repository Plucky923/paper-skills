---
name: systems-paper-revise
description: "Revise computer-systems paper prose within each original paragraph, preserving its purpose, technical meaning, and manuscript format while improving precision and logical flow. Compose from author-supplied material only when drafting is requested."
---

# Systems Paper Revise

Correct identifiable problems in the supplied prose while preserving the author's text. A passage that already meets the request may remain unchanged. Use the OSDI-calibrated writing standard to assess the paragraph's existing role, not to complete or expand its argument automatically.

## Contract

- Work only on the passage, files, or source material the user names. Treat unavailable context as unavailable rather than silently inspecting neighboring material.
- Preserve factual truth, technical meaning, conditions, numbers, citations, equations, identifiers, macros, terminology, evidence status, and author intent. A polished sentence cannot turn a plan, hypothesis, or plausible mechanism into completed work.
- Use the manuscript language unless translation is requested. Preserve deliberate voice and exact technical repetition.
- Return prose in chat for pasted material. Edit explicitly named editable files directly. Treat a PDF as read-only unless editable source is also in scope.
- For existing prose, preserve paragraph count, order, boundaries, and content ownership. A section or whole paper is a set of paragraph-local edits, not permission to restructure it. Follow the paragraph-local contract in [revision-protocol.md](references/revision-protocol.md); a diagnosis or review suggestion does not override it.
- Every direct edit must address a concrete defect in grammar, reference, precision, redundancy, or supported local logic. Keep adequate sentences, emphasis, and cadence. A different academic phrasing alone is not a defect.
- Return one conservative revision. Clearly better but optional wording belongs after the manuscript under `可选写法` (or `Optional wording`), with the original anchor, alternative, and one short reason. Follow the output rules in [revision-protocol.md](references/revision-protocol.md).
- If a scientific claim needs missing evidence, a new premise, or a change of strength, keep that passage unchanged and flag the exact gap separately. Complete other safe edits. An unsupported claim remains flagged, not endorsed or silently weakened.

## Load the writing rules

Always read [writing-core.md](references/writing-core.md), the [shared review and revision contract](references/review-revise-contract.md), and [revision-protocol.md](references/revision-protocol.md). Apply Review's same quality standard; use the shared contract to discuss uncertain logic through Grill before applying the disputed repair.

Load only the branch that the request needs:

- Read [paper-archetypes.md](references/paper-archetypes.md) when contribution type affects the argument: titles, abstracts, introductions, contribution framing, section or whole-paper structure, measurement/experience/formal work, or hybrid papers.
- Read [chinese-writing.md](references/chinese-writing.md) for Chinese prose or Chinese-to-English translation.
- Read [revision-strategies.md](references/revision-strategies.md) for structural, evaluation, figure/table, venue, or multi-finding repairs.
- Read [change-safety.md](references/change-safety.md) before editing files or prose with technical values, citations, equations, notation, identifiers, macros, figures, tables, or other fragile content.
- Read [convergence-loop.md](references/convergence-loop.md) only when the user explicitly requests iteration/fixed-point revision or when several interacting edits make a single pass unsafe.
- Read [multi-agent-revision.md](references/multi-agent-revision.md) only when a sufficiently large authorized scope benefits from independent read-only checks during such a loop.

Use the sibling [systems-paper-review](../systems-paper-review/SKILL.md) when the user explicitly requests a review before revision or when a full-scope scientific or submission judgment is required. Its findings are internal input to this writing task; this skill's scope, writing authority, and deliverable-first output contract remain controlling.

## Route automatically

### Compose from evidence or notes

Choose this mode when no manuscript prose exists for the requested unit or the user asks to draft it. Recover the section or paragraph obligation, select only evidence that serves it, and write a complete dependency chain. Missing support remains a named blocker; notes are inputs, not sentences that all need to survive.

### Revise existing prose

Choose this mode when manuscript prose already exists. Identify each original paragraph's role, claim, support, and boundary internally, then repair only that paragraph. Sentence reordering, splitting, or merging may occur inside it. Changing paragraph boundaries, moving content between paragraphs, or replacing the paragraph's purpose requires an explicit author request.

Infer the mode from the supplied material. Ask the author only when the choice would change the scientific contribution or technical meaning.

## Existing-prose workflow

1. Freeze scope, language, author intent, evidence, and protected technical content; read the authorized paper decision record and recover confirmed Grill decisions through the shared contract before choosing edits. A directly requested revision needs no record when no discussion has occurred.
2. Identify each paragraph's existing reader obligation and trace its sentence links; use supplied neighboring paragraphs to understand the handoff, not as a pool of content to move.
3. Fix only identified local defects using [writing-core.md](references/writing-core.md). An equivalent abstraction must follow directly from the paragraph and address the requested repair; otherwise keep the original or offer it as optional wording. Add no purpose, cause, benefit, mechanism, or planned experiment to make the prose sound complete.
4. Check every edited paragraph and its in-scope neighbors: verify sentence links, paragraph handoffs, content ownership, terminology, claim strength, and protected content. A loop cannot expand the editing boundary.
5. Stop when the requested local repairs are complete. If a sentence or paragraph link needs new evidence or cross-paragraph restructuring, identify both endpoints and the blocker outside the manuscript instead of silently completing the argument.

## Output

Lead with the manuscript text in its original paragraph layout, headings, lists, emphasis, citations, and markup. For file edits, name the edited objects. Keep diagnostics and alternatives outside the manuscript and out of source files. Offer optional wording only for a clear benefit; ordinary synonym swaps need no alternative. When the user requests only prose, omit optional wording and routine commentary; the sole exception is a minimal note locating an unresolved issue that affects scientific meaning. State its missing evidence without adding a replacement argument. See [revision-protocol.md](references/revision-protocol.md) for the complete output contract.
