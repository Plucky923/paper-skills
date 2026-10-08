# Evidence-Safe Convergence Loop

Use this loop only for a clear iteration request or when interacting edits give one writer-first pass unresolved preservation risks.
Usual composition or bounded revision ends after the gate in [revision-protocol.md](revision-protocol.md).

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

The root agent is the sole writer.
Reviewer subagents stay read-only.
From the baseline through the last gate, do not use Git or a source-control API.
Do not make a backup, branch, commit, stash, tag, patch, or diff report.
The human does the Git review after the loop.

## Show the baseline

1. Give the editable objects, exclusions, evidence, author intent, language, and protected content through [revision-protocol.md](revision-protocol.md) and [change-safety.md](change-safety.md).
2. Keep that scope and evidence unchanged.
3. For existing prose, inventory the full scope through the [coverage contract](coverage-contract.md).
4. Do the full audit.
5. Find each defect that changes scientific content and has a permitted repair.
6. For missing prose, find each reader obligation of the requested unit.
7. Divide prose repairs from items with external input requirements.

External inputs include an experiment, data, proof, implementation fact, source, context not in scope, or author choice.
Order items with permitted repairs by scientific dependency:

1. Truth and claim strength
2. Argument and evidence alignment
3. Structure
4. Terms and protected content
5. Sentence expression.

For a clear adversarial gate or full-scope scientific/submission judgment, use [systems-paper-review](../../systems-paper-review/SKILL.md).
If that condition does not hold, do the focused internal diagnosis necessary for the requested revision.

## Run one edit round

### Select a batch with clear dependencies

Select the highest-impact repair that the paragraph-local contract gives permission for.
Include interacting edits only when each stays in its initial paragraph.
Iteration does not give restructuring permission.
A batch can make an existing condition clear before its consequence.
It can also settle terms before sentence revision.

For a clear structural rebuild, first select the contribution type through [paper-archetypes.md](paper-archetypes.md).
Then apply [revision-strategies.md](revision-strategies.md).
If that condition does not hold, give the cross-paragraph dependency as a blocker.
Complete the permitted meaning-preserving local repairs.

### Write once

Write one version with clear dependencies through [writing-core.md](writing-core.md).
Obey these limits:

- Stay in each initial paragraph unless the author clearly gives permission for restructuring.
- Make only its existing propositions, supported relations, or a clear author correction clear.
- Keep important premises, evidence, costs, and limitations.
- Keep paragraph count, order, roles, and content ownership.
- During usual revision, remove only verbal redundancy.
- Keep each reviewer subagent idle or read-only.

### Check preservation and regression

1. Do the [change-safety.md](change-safety.md) checks.
2. Audit the full scope again from the highest assessable level through lexical occurrences.
3. Reconcile the result from lexical occurrences up to the highest level.
4. Include unchanged paragraphs in all subsequent rounds.

Record these items internally:

- The closed obligation or root cause and the reason for closure
- Each remaining item with a permitted repair
- Each blocker and its missing input
- Each new or reopened problem
- The preservation and tool checks that passed
- Each received finding's closure state or `pending clarification` state
- At a terminal run, coverage totals, last-unit states, and the unreviewed count.

If independent review is necessary, use [multi-agent-revision.md](multi-agent-revision.md).
Before the next edit, wait for all applicable reviewers.

## Continue only on observable progress

Run another round only when a named repair stays and the preceding round made observable progress.
Progress has at least one of these results:

- The text completes a reader obligation.
- A resolution test declared before the edit passes.
- The text applies a clear author correction or a specified wording repair.
- A premise or dependency necessary for the next repair is clear.
- The repair removes a regression and keeps the improvement from the round before this one.

A larger draft, lower word count, or smoother wording alone is not progress.
After an unsuccessful approach, try another permitted repair that keeps evidence status only with a clear mechanism and resolution test.

## Stop with a specified status

### Locally complete

Stop as locally complete only when all these conditions hold:

- The text completes each requested obligation.
- Each received finding has a clear terminal closure state.
- No item stays `pending clarification`.
- Each defect with a permitted repair in scope is closed.
- The full scope passes its last top-down and bottom-up audit with `Unreviewed: 0`.
- Preservation checks pass.
- No required evidence, context, source, or author choice stays unresolved.

This status applies only to the frozen scope.
It does not show novelty over all literature or artifact correctness in each environment.
It also does not show experiment completion, acceptance, or publication readiness.

### Blocked

Stop as blocked when no permitted meaning-preserving prose edit is available and a required input is unavailable.
Give the affected claim and the missing evidence, context, source verification, or author choice.
Give the reason that prose cannot supply it.
Give the observable condition for continuation.
For author-input items, apply the shared contract's terminal-blocker rule.

### No progress or oscillation

Stop when successive permitted revisions recreate the same semantic defect.
Also stop when one improvement reopens an equal-or-higher-impact problem or changes author intent.
Correct only the last edit that violates the preservation contract directly.
Give the decision necessary for continuation.

A round count, reviewer score, linter result, or word-count target does not prove convergence.
After a true fixed point, optional paraphrases do not justify another round.

## Handoff

Obey the output contract in [revision-protocol.md](revision-protocol.md).
Include optional wording and the minimal scientific-issue exception for prose-only requests when applicable.
Keep loop records internal unless the user requests them.
