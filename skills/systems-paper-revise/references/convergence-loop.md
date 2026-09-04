# Evidence-Safe Convergence Loop

Use this loop only when the user explicitly requests iterative revision or when several interacting edits make a single writer-first pass unsafe. An ordinary composition or bounded rewrite ends after the lightweight gate in [revision-protocol.md](revision-protocol.md).

## Invariant

```text
freeze scope and evidence
  → establish a baseline diagnosis
  → select one dependency-safe writing batch
  → revise through the sole writer
  → check meaning and protected content
  → re-read the complete scope
  → repeat only while a specific supported repair remains
  → hand the final working tree to the human
```

The root agent is the sole writer. Reviewer subagents, when used, remain read-only. From the baseline through the final gate, no agent invokes Git or a source-control API, and no agent creates a backup, branch, commit, stash, tag, patch, or diff report. Git review belongs to the human after the loop.

## Establish the baseline

1. Freeze the editable objects, explicit exclusions, evidence, author intent, language, and protected content through [revision-protocol.md](revision-protocol.md) and [change-safety.md](change-safety.md).
2. For existing prose, identify every materially distinct actionable defect in scope. For missing prose, identify every reader obligation the requested unit must discharge.
3. Separate items that prose can repair from items requiring a new experiment, data, proof, implementation fact, source, outside context, or author choice.
4. Order actionable items by scientific dependency: truth and claim strength; argument and evidence alignment; structure; terminology and protected content; sentence-level expression.

Use the sibling [systems-paper-review](../../systems-paper-review/SKILL.md) for an explicitly requested adversarial gate or a full-scope scientific/submission judgment. Otherwise perform the focused internal diagnosis needed for the requested revision.

## Run one edit round

### Select a coherent batch

Choose the highest-impact repair that is not blocked and include interacting edits only when their combined meaning can be audited. A useful batch may calibrate a claim before reorganizing evidence, define a model before explaining mechanisms, or settle terminology before sentence revision.

For a structural rebuild, first route the contribution with [paper-archetypes.md](paper-archetypes.md) and apply [revision-strategies.md](revision-strategies.md). For a local defect, repair directly without constructing unnecessary paper-wide maps.

### Write once

The root writes one coherent version through [writing-core.md](writing-core.md). While writing:

- remain inside the frozen scope;
- add only established facts or warranted inferences;
- preserve material premises, evidence, costs, and limitations;
- select or demote secondary detail according to its contribution to the decision case;
- keep every reviewer subagent idle or read-only.

### Check preservation and regression

Run [change-safety.md](change-safety.md), then re-read the complete frozen scope. Record internally:

- which obligation or root cause closed and why;
- which actionable item remains;
- which item is blocked and by what;
- any newly introduced or reopened problem;
- which preservation and tool checks actually passed.

When independent review is warranted, follow [multi-agent-revision.md](multi-agent-revision.md) and wait for all applicable reviewers before the next write.

## Continue only on observable progress

Run another round only when a named repair remains and the previous round did at least one of the following:

- discharged a reader obligation;
- closed a predeclared resolution test;
- narrowed an overbroad claim or reduced the scope of a defect;
- exposed a premise or dependency needed for the next repair;
- removed a regression while preserving the earlier improvement.

A larger draft, a lower word count, or smoother wording alone is not progress. After an unsuccessful approach, try a distinct evidence-safe repair only when its mechanism and expected resolution test are clear.

## Stop precisely

### Locally complete

Stop as locally complete when every requested obligation is discharged, every actionable in-scope defect is closed, the complete scope has passed its final re-read, preservation checks pass, and no required evidence/context/source/author choice remains unresolved.

This status describes only the frozen scope. It does not establish novelty over all literature, artifact correctness in every environment, completion of missing experiments, acceptance, or publication readiness.

### Blocked

Stop as blocked when no evidence-safe prose edit remains and the outstanding issue requires evidence, context, source verification, or author choice. State the affected claim, the missing item, why prose cannot supply it, and the observable condition that would unblock it.

### No progress or oscillation

Stop when successive admissible revisions recreate the same semantic defect, improve one equal-or-higher-impact problem only by reopening another, or encode different author intent. Restore only the current unsafe edit through direct editing and report the decision needed.

No round count, reviewer score, linter result, or word-count target proves convergence. Once a true fixed point is reached, optional paraphrases do not keep the loop alive.

## Handoff

Lead with the final manuscript text or exact edited files. Report the scope, consequential changes, actual checks, loop outcome, and blockers compactly. Confirm that the loop used no Git operation and is ready for the human's Git diff review.
