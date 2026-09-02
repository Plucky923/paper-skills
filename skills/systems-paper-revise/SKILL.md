---
name: systems-paper-revise
description: "Directly revise explicitly scoped computer-systems research prose or LaTeX after reviewer feedback or at an author's request. Use when the user asks to polish, rewrite, restructure, strengthen, fix review findings, or iterate a systems manuscript. May change sentences, paragraphs, section order, narrative, and claim strength while preserving evidence, technical meaning, citations, numbers, macros, and author intent. Never fabricate facts, literature, data, experiments, or completed work. After each edit, apply the systems-paper-review gate and repeat without Git operations until no actionable in-scope issues remain or missing evidence or author decisions block progress."
---

# Systems Paper Revise

Revise the requested systems-paper material directly and drive it to an evidence-safe fixed point. Solve argument and evidence problems before polishing wording.

## Non-negotiable contract

1. Edit only the scope named by the user. Do not inspect or change neighboring files for context unless they are explicitly added to scope. A named `main.tex` means only that file; a full LaTeX dependency closure is editable only when the user explicitly scopes the whole LaTeX project or names its files.
2. For pasted text, return revised text in chat. For editable Markdown or LaTeX files, edit them directly. Treat PDFs as read-only unless the user also supplies an editable source.
3. Do not create backup copies. Preserve unrelated user changes.
4. Neither the root nor any subagent may run `git status`, `git diff`, `git add`, `git commit`, `git restore`, or any other Git command during the automated review-revise loop. The human examines the Git diff only after the loop.
5. Never fabricate or imply nonexistent facts, citations, implementation, experiments, measurements, comparisons, guarantees, or completed future work.
6. Preserve supported technical meaning, numbers, units, equations, citations, labels, references, commands, code identifiers, and custom macros unless a requested change requires otherwise and evidence supports it.
7. A missing experiment, source, implementation fact, or author choice is a blocker. Narrow or qualify a claim when justified; do not write around missing evidence.

## Load the right references

Always read:

- [revision-protocol.md](references/revision-protocol.md)
- [convergence-loop.md](references/convergence-loop.md)
- [change-safety.md](references/change-safety.md)

Read [revision-strategies.md](references/revision-strategies.md) for structural or multi-finding revisions.

For a full paper, multiple substantial sections, or manuscript-plus-artifact loop, also read [multi-agent-revision.md](references/multi-agent-revision.md). Use specialized subagents only for read-only review and verification. The root agent is the sole writer for pasted text and the only agent permitted to modify in-scope files.

This skill uses the sibling `systems-paper-review` skill as its gate. Read that skill's `SKILL.md`, `references/review-protocol.md`, `references/source-registry.md`, and every domain reference relevant to the current scope. Resolve the sibling from the common `skills/` directory; if it is unavailable, state that the required review gate is missing and do not claim convergence.

## Revision workflow

### 1. Freeze scope and invariants

Record the exact editable object, source language, user goal, permitted restructuring depth, immutable technical tokens, and missing context. Follow the source language unless translation is requested; keep deliberately mixed-language material mixed.

### 2. Establish the initial defect ledger

Apply `systems-paper-review` without editing. When the scope warrants parallel review and collaboration tools are available, delegate the applicable reviewer roles under the sibling skill's orchestration protocol, wait for all roles, and synthesize their findings. Convert the resulting in-scope confirmed defects and actionable unresolved risks into a working ledger. Style preferences enter the ledger only when the user requests that style or they materially impair clarity.

### 3. Choose the smallest evidence-safe repair

Repair in this order:

1. unsupported, contradictory, or overbroad claims;
2. missing argument links and system/evaluation logic;
3. section and paragraph organization;
4. terminology, figure/table/LaTeX consistency;
5. sentence-level clarity and grammar;
6. optional style preferences.

For each item, choose among adding already available evidence, making reasoning explicit, qualifying the claim, deleting the unsupported claim, reorganizing the scoped material, or marking an author/evidence blocker. Do not manufacture support.

### 4. Edit directly

The root agent is the sole writer. Do not delegate file or pasted-text mutation and do not allow multiple agents to edit shared content concurrently. Make coherent batches of changes rather than repeatedly paraphrasing isolated sentences. Structural edits may reorder or split in-scope sentences, paragraphs, or sections when allowed. Maintain the preservation checks in [change-safety.md](references/change-safety.md).

### 5. Re-run the full in-scope gate

Review the complete revised scope, not only changed lines. A fix may create a new terminology mismatch, dangling reference, evidence gap, or repetition. Use the same rule set, reviewer roles, and venue overlay as the initial pass. In multi-agent mode, send each reviewer the full revised scope, wait for every applicable role, then let the root reconcile regressions, duplicates, and conflicting judgments before the next edit.

### 6. Iterate to a fixed point

Follow [convergence-loop.md](references/convergence-loop.md). Continue while an evidence-safe edit can resolve an actionable issue. Stop only when:

- no actionable in-scope issue and no `B1`–`B4` blocker remains, producing a locally clean fixed point; or
- no actionable edit remains and at least one issue requires missing evidence, unavailable context, a new experiment, a new citation decision, or an author decision, producing a blocked fixed point; or
- further edits oscillate or cease making measurable progress.

Blocked takes precedence over locally clean whenever any `B1`–`B4` item remains.

There is no fixed number of rounds and no score threshold. A locally clean fixed point is not proof of publication readiness.

## Output contract

After file edits or a returned text revision, report in the user's language:

1. exact scope revised;
2. substantive changes grouped by argument, evidence, structure, and prose;
3. preserved invariants and validation performed;
4. loop outcome and number of completed review-revise rounds;
5. unresolved blockers, with the precise evidence or decision needed;
6. human-review handoff, explicitly stating that Git was not used during the loop.

Do not emit a separate report file unless the user asks for one. Do not claim `all problems are solved` outside the frozen scope.
