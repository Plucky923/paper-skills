# Multi-Agent Review–Revise Loop

Use this protocol only when independent checks help resolve important risks in a large permitted convergence scope.
Use [convergence-loop.md](convergence-loop.md) for that loop.
Keep a sentence, paragraph, narrow local repair, or strongly sequential argument single-agent.

## Ownership model

```text
read-only reviewers inspect independent questions in parallel
  → root consolidates one evidence-backed diagnosis
  → root alone writes one coherent revision
  → read-only reviewers inspect the complete revised scope
  → root decides whether another supported edit remains
```

The root controls scope, evidence, author-intent choices, synthesis, edits, and validation commands.
It also controls stopping decisions and the last response.
Reviewer subagents examine and give findings.
They do not write replacement prose or change any shared object.

Give each agent these limits:

- Examine only the specified frozen scope and permitted primary sources.
- Keep manuscript evidence, artifact evidence, external verification, and inference as different categories.
- Do not use Git or a source-control API.
- Do not make a branch, commit, stash, tag, patch, diff report, or backup.
- Leave each state-changing command to the root.

State-changing commands include compilation, rendering, lint, tests, benchmarks, scripts, and installations.
The root runs them only with separate permission.

If collaboration tools are unavailable, do the independent checks that help answer their assigned questions in the root context.
Do not invent reviewers or agreement.

## Select reviewers by question

Use only roles that can make independent progress on the scoped material:

- Contribution and coherence for broad readers
- Domain assumptions, design derivation, correctness, or closest work
- Claim-to-evidence alignment, baselines, measurement, and uncertainty
- Paragraphs, terms, figures, and local logic
- Paper–artifact consistency, when artifacts are clearly in scope
- Bounded verification of primary sources or venue rules.

If concurrency is limited, schedule different questions in waves.
Do not combine questions about different scientific content only to fit that limit.
Add agents only for a new question without shared prerequisites or failed coverage.
A difficult finding alone does not justify another agent.

## Baseline wave

First, the root records these items and keeps them unchanged during the wave:

```text
authorized objects and explicit exclusions
current complete content
reader obligations and contribution contract
available evidence and unavailable dependencies
protected technical content
questions assigned to each reviewer
```

Give each reviewer the same scope boundary and content for this round.
Supply only the references necessary for its question.
Request a read-only result with evidence, location, consequence, repair direction or blocker, and coverage limits.

Wait for each applicable reviewer.
Examine each finding against the evidence.
Combine true duplicates without losing affected locations.
Resolve disagreements from evidence rather than a majority vote.
Reject a stronger claim when evidence cannot support it.
Reject a style deletion when it removes an important limitation.

If scoped content changes during review, the judgments apply to an old version.
Stop the wave.
If necessary, get the user's decision about the intended content for this round.
Run affected checks again before edits.

## Root-only synthesis and writing

1. Order the combined problems by scientific dependency.
2. Apply [revision-protocol.md](revision-protocol.md), [paper-archetypes.md](paper-archetypes.md), and [revision-strategies.md](revision-strategies.md) where applicable.
3. Record the preservation snapshot in [change-safety.md](change-safety.md).
4. Write one draft with clear dependencies through [writing-core.md](writing-core.md).

Reviewer suggestions are diagnoses, not manuscript text to paste.
For different technical meanings, contribution priorities, assumptions, or trade-offs, get an author decision.
For usual wording, use one conservative version.

Keep reviewers read-only while the root writes.
Run each permitted output-producing command through the root.
Put writable output in a different directory from the source tree.
Make sure that commands cause no unintended changes to scoped content or the source tree.

## Regression wave

After preservation checks, give each applicable reviewer the full revised scope.
A review of changed lines alone is insufficient.
Supply the content for this round and the findings that the edits intended to close.
Request these results:

- Each assigned issue's state: closed, open, regressed, or blocked, with evidence
- Each new issue that changes scientific content
- The question examined and the part that stayed not assessable.

Wait for all applicable roles.
Make sure that each examined the content for this round.
Combine the findings again.
One clean role cannot close another role's concern when evidence supports that concern.
A fatal minority finding stays open until evidence resolves it.

## Iterate and stop

Return to root-only edits only when a specified permitted repair that keeps evidence status stays.
Obey the progress and stopping conditions in [convergence-loop.md](convergence-loop.md).
For a locally complete multi-agent gate, make sure that these additional conditions hold:

- Each applicable role finishes after the last edit.
- No actionable issue or required evidence, context, source, or author choice stays.
- Disagreements are resolved or visible as blockers.
- The root independently passes [change-safety.md](change-safety.md).
- No reviewer changes shared state.
- No agent uses Git.

If a required role fails, repeat its check only in the permitted scope.
If no such repeat is possible, give the reviewer coverage as incomplete.
Do not claim exhaustive convergence.

## Final handoff

Start with the revised manuscript or specified edited files.
Give only the roles used, important changes, validation results, unresolved blockers, and readiness for human Git diff review.
The root stays the sole writer throughout.
