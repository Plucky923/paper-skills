---
name: systems-paper-revise
description: "Draft or revise explicitly scoped computer-systems paper prose. Use to make an argument more problem-driven, high-level, concise, logically precise, evidence-bounded, and publication-quality in wording without changing supported technical meaning or inventing research content."
---

# Systems Paper Revise

Write the requested material as one precise scientific argument. The default result is manuscript-ready prose that is shorter, more specific, and easier to retell—not an account of the editing process.

## Contract

- Work only on the passage or files the user names. Do not inspect neighboring material without permission.
- Preserve supported facts, conditions, numbers, citations, equations, identifiers, macros, terminology, and author intent. Never convert plans, hypotheses, or plausible mechanisms into completed work.
- Use the source language unless translation is requested. Preserve deliberate voice; remove generic academic filler.
- Return prose in chat for pasted material and edit explicitly named source files directly. Treat PDFs as read-only without editable source.
- Do not create backups or use Git during an automated review-revise loop.
- Expose missing evidence, context, sources, or author choices as blockers; prose cannot repair them.

## Load references proportionally

Read [revision-protocol.md](references/revision-protocol.md). Read [change-safety.md](references/change-safety.md) for file edits or prose containing technical values, equations, citations, macros, or other fragile tokens. Read [revision-strategies.md](references/revision-strategies.md) only for structural or multi-finding problems.

Use [convergence-loop.md](references/convergence-loop.md) only when iteration is requested or interacting edits warrant it, and [multi-agent-revision.md](references/multi-agent-revision.md) only for a sufficiently large authorized scope. Use the sibling [systems-paper-review](../systems-paper-review/SKILL.md) gate for substantial argument, evidence, or submission judgments; a narrow wording edit needs only the relevant local checks.

## Writing method

### 1. Fix the intellectual job before the words

State internally, in one sentence, the question this scope must answer and the exact answer supported by the evidence. For a paragraph, this is its local obligation. For a section or paper, recover the controlling thesis and only the dependencies needed to support it.

Begin from the reader's unresolved problem or inference. Do not begin from the system name, component list, or a generic claim that the topic is important unless that sentence also identifies the consequential tension.

### 2. Write at the highest informative level

`High-level` means causal compression, not vagueness. Express the smallest relation that explains the design or finding:

```text
binding constraint -> leverage or changed assumption -> action/abstraction -> resulting property and boundary
```

This is a reasoning test, not a mandatory sentence template. Concrete mechanisms should instantiate that relation; they should not replace it.

Apply three tests:

- **Substitution:** If unrelated system and component names could replace the current names without changing the sentence, it is too generic.
- **Prediction:** The principle-level account should explain why the major mechanisms or study choices are necessary. If it cannot, it is too weak or too detached from the design.
- **Boundary:** State what follows, under which condition, and what does not follow. Do not collapse a mechanism, capability, guarantee, and measured result into one claim.

### 3. Build the paragraph as a dependency chain

The first sentence establishes the paragraph's decision-relevant claim, tension, or question. Each middle sentence performs one necessary role—reason, mechanism, evidence, qualification, example, or transition—and connects given information to one new proposition. Order prerequisites before consequences and evidence before the inference it licenses.

The last sentence delivers the supported answer, implication, limitation, or next necessary question. It must pay off the opening without merely repeating it. Move trailing implementation detail earlier or delete it when it strands the paragraph.

### 4. Make every sentence exact and economical

- Put the main actor and action early unless the object is intentionally the focus.
- Prefer a precise verb over a noun phrase plus a weak verb. Name what is mapped, isolated, delayed, enforced, measured, or compared.
- Keep one principal assertion per sentence; attach only the conditions needed to interpret it.
- Place quantifiers, conditions, comparisons, and epistemic strength next to the claim they bound.
- Use a transition only when the underlying relation—cause, contrast, consequence, condition, or example—is real.
- Delete a sentence if removing it loses no necessary inference, definition, evidence, boundary, or handoff. Between equally precise versions, choose the shorter one.

### 5. Gate the prose, not the process

Read the result once as a skeptical systems reviewer. Verify that the problem licenses the principle, the principle predicts the mechanism, the evidence licenses the conclusion, and every paragraph opening is paid off by its ending. Then check terminology and grammar without weakening the logic.

## Output

Lead with the revised or newly drafted manuscript text. Do not expose internal outlines, ledgers, archetype labels, rule IDs, or review rounds unless the user asks. After the prose, report only material blockers or a compact note about consequential changes and validation. Do not bury the deliverable under process narration.
