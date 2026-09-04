# Multi-Agent Review–Revise Loop

Use this protocol only for a large authorized scope whose independent scientific, evaluation, or presentation checks materially improve the convergence loop in [convergence-loop.md](convergence-loop.md). A sentence, paragraph, narrow local repair, or strongly sequential argument stays single-agent.

## Ownership model

```text
read-only reviewers inspect independent questions in parallel
  → root consolidates one evidence-backed diagnosis
  → root alone writes one coherent revision
  → read-only reviewers inspect the complete revised scope
  → root decides whether another supported edit remains
```

The root owns scope, evidence, author-intent choices, synthesis, edits, validation commands, stopping decisions, and the final response. Reviewer subagents inspect and report; they do not draft replacement prose or modify any shared object.

Every agent follows the same boundaries:

- inspect only the exact frozen scope and permitted primary sources;
- preserve the distinction between manuscript evidence, artifact evidence, external verification, and inference;
- use no Git or source-control API and create no branch, commit, stash, tag, patch, diff report, or backup;
- leave compile, render, lint, tests, benchmarks, scripts, installations, and other state-changing commands to the root and only when separately authorized.

If collaboration tools are unavailable, run only the independent checks that remain useful in the root context; do not simulate agreement among fictional reviewers.

## Select reviewers by question

Use only roles that can make independent progress on the scoped material:

- contribution and broad-reader coherence;
- domain assumptions, design derivation, correctness, or closest work;
- claim-to-evidence alignment, baselines, measurement, and uncertainty;
- paragraph, terminology, figure, and local logic;
- paper–artifact consistency when artifacts are explicitly in scope;
- bounded primary-source or venue-rule verification.

Do not merge materially different questions merely because concurrency is limited; schedule them in waves. Additional agents are justified by a new independent question or failed coverage, not by a finding being difficult.

## Baseline wave

The root first freezes:

```text
authorized objects and explicit exclusions
current complete content
reader obligations and contribution contract
available evidence and unavailable dependencies
protected technical content
questions assigned to each reviewer
```

Send each reviewer the same scope boundary and current content, plus only the references needed for its question. Require a read-only result containing evidence, location, consequence, repair direction or blocker, and coverage limits.

Wait for every applicable reviewer. The root verifies each finding, merges true duplicates without losing affected locations, and resolves disagreement from evidence rather than majority vote. A request for a stronger claim loses to evidence that cannot support it; a stylistic deletion loses when it removes a material limitation.

If scoped content changes while reviewers are reading, their judgments apply to a stale version. Stop the wave, establish the intended current content with the user when necessary, and rerun affected checks before writing.

## Root-only synthesis and writing

Order the consolidated problems by scientific dependency. Apply [revision-protocol.md](revision-protocol.md), [paper-archetypes.md](paper-archetypes.md), and [revision-strategies.md](revision-strategies.md) only where relevant. Before writing, run the preservation snapshot in [change-safety.md](change-safety.md).

The root then produces one coherent draft through [writing-core.md](writing-core.md). Reviewer suggestions are diagnoses, not text to paste. Alternatives that encode different technical meaning, contribution priority, assumption, or trade-off become an author decision; ordinary wording resolves to one conservative version.

No reviewer writes concurrently with the root. Any authorized command that can produce output runs through the root, with writable output isolated outside the source tree. The root verifies that scoped content and the source tree did not change as an unintended side effect.

## Regression wave

After preservation checks, ask every still-applicable role to inspect the complete revised scope, not only changed lines. Supply the current content and the findings the revision intended to close. Require each role to state:

- which assigned issue is closed, still open, regressed, or blocked, with evidence;
- any new materially distinct issue;
- which question it checked and which part remained unassessable.

Wait for all applicable roles, verify that they assessed the current content, and consolidate again. One clean role cannot close another role's evidence-backed concern. A minority fatal finding remains open until the evidence resolves it.

## Iterate and stop

Return to root-only writing only when a specific evidence-safe repair remains. Apply the progress and stopping conditions in [convergence-loop.md](convergence-loop.md). A locally complete multi-agent gate additionally requires:

- every applicable role finished after the last edit;
- no actionable issue or required evidence/context/source/author choice remains;
- disagreements are resolved or exposed as blockers;
- the root independently passed [change-safety.md](change-safety.md);
- no reviewer modified shared state and no agent used Git.

If a required role fails and cannot be safely rerun, report incomplete reviewer coverage rather than exhaustive convergence.

## Final handoff

Lead with the revised manuscript or exact edited files. Report only the roles used, consequential changes, actual validation, unresolved blockers, and readiness for human Git diff review. The root remains the sole writer throughout.
