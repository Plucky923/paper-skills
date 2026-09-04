---
name: systems-paper-revise
description: "Compose or revise explicitly scoped computer-systems paper prose from author-supplied text, notes, or evidence. Use for problem-driven, high-level, concise, logically precise, evidence-bounded manuscript writing while preserving supported technical meaning and author intent."
---

# Systems Paper Revise

Produce the shortest complete scientific argument that the available evidence supports. The deliverable is manuscript-ready prose, not an account of the writing process.

## Contract

- Work only on the passage, files, or source material the user names. Treat unavailable context as unavailable rather than silently inspecting neighboring material.
- Preserve factual truth, technical meaning, conditions, numbers, citations, equations, identifiers, macros, terminology, evidence status, and author intent. A polished sentence cannot turn a plan, hypothesis, or plausible mechanism into completed work.
- Use the manuscript language unless translation is requested. Preserve deliberate voice and exact technical repetition.
- Return prose in chat for pasted material. Edit explicitly named editable files directly. Treat a PDF as read-only unless editable source is also in scope.
- Within the authorized scope, omit or demote true but nonessential detail when it does not change the decision case. Preserve every material premise, causal link, result, cost, and boundary; report consequential deletion or reframing.
- Supply one conservative version by default. Present alternatives only when they encode different technical meanings, contribution priorities, assumptions, or trade-offs that require the author's choice.

## Load the writing rules

Always read [writing-core.md](references/writing-core.md) and [revision-protocol.md](references/revision-protocol.md).

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

Choose this mode when manuscript prose already exists. Recover what the passage is trying to establish, find the earliest broken dependency, and make the smallest coherent repair. A coherent repair may rewrite, reorder, split, merge, delete, or add an evidence-supported bridge within scope; it is not limited to word substitution.

Infer the mode from the supplied material. Ask the author only when the choice would change the scientific contribution or technical meaning.

## Writer-first workflow

1. Freeze scope, language, author intent, evidence, and protected technical content.
2. State internally the reader obligation and the strongest supported answer. At section or paper scale, recover the controlling thesis and its necessary support hierarchy.
3. Draft one coherent version using [writing-core.md](references/writing-core.md). Prefer a supported inference over an inventory, and a precise relation over an academic-sounding phrase.
4. Run a lightweight gate over the complete scoped result: verify causal and evidential logic, paragraph obligations, terminology, claim strength, and protected content. Use a full review–revise loop only through the conditional routing above.
5. Stop when the requested obligation is discharged as precisely and economically as the evidence permits, or when the remaining gap requires evidence, context, source verification, or an author decision.

## Output

Lead with the revised or newly composed manuscript text. For file edits, name the exact edited objects. Follow with only consequential changes, validations actually performed, and unresolved blockers. Keep internal outlines, maps, labels, reviewer roles, and loop state out of the manuscript and out of the response unless the user asks for them.
