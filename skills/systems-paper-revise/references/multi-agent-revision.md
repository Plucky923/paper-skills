# Multi-Agent Review–Revise Loop

Use this protocol when a writing or revision scope is large enough to benefit from specialized parallel review. It extends `convergence-loop.md`; every Git-free, scope, evidence, blocker, and convergence rule still applies.

The invariant is:

```text
specialized subagents read and review in parallel
               ↓
root consolidates one evidence-backed ledger
               ↓
root is the only writer and writes serially
               ↓
specialized subagents re-review the complete revised scope
               ↓
root decides the next edit or stopping condition
```

No subagent may edit pasted text, manuscript files, figures, code, data, scripts, or any other shared state.

## 1. Select the execution mode

Use this multi-agent loop when:

- `systems-paper-review` selects multi-agent mode for the same frozen scope;
- several independent reviewer lenses are applicable;
- the scoped writing contains structural, technical, evaluation, and presentation concerns that can be reviewed independently;
- the expected coverage or latency benefit justifies extra token and coordination cost.

Keep the loop single-agent for a sentence, short paragraph, narrow local fix, or strongly sequential argument where parallel roles would repeat the same work.

If collaboration tools are unavailable, run the same reviewer roles sequentially and preserve the unique-writer invariant.

## 2. Authority separation

### Root coordinator / sole writer

The root alone may:

- freeze scope and preservation invariants;
- recover the scoped writing obligation and own the evidence and thesis structures required at that scale;
- create and verify the content manifest for each review wave;
- construct and own the finding ledger;
- resolve duplicate/conflicting findings;
- select repair classes `E1`–`E5` or blockers `B1`–`B4`;
- choose edits that preserve author intent;
- modify in-scope text/files;
- run authorized compile/render/lint/test commands in isolated temporary output locations;
- decide convergence and produce the handoff.

### Reviewer subagents

Reviewer subagents may only:

- inspect the exact frozen scope;
- use authorized read-only tools and external sources;
- return evidence-backed findings and coverage;
- recheck resolved findings and search for regressions/new issues;
- request specific missing evidence, context, source, or author decisions.

Reviewer subagents may not:

- edit any file or proposed text;
- create patches, backup copies, rewritten passages, replacement figures, or modified artifacts;
- invoke Git or source-control APIs;
- compile, render, lint, run tests/benchmarks/scripts, or invoke any command that may write local or external state;
- install dependencies or perform unauthorized external writes;
- decide a paper-wide or loop-wide fixed point independently.

## 3. Phase A — Parallel baseline review

1. Root freezes scope, evidence, writing obligation, and invariants using `revision-protocol.md` and `change-safety.md`.
2. Root reads the sibling `systems-paper-review/references/multi-agent-orchestration.md`.
3. Root creates one immutable review packet, shared claim inventory, and non-Git content manifest under the sibling orchestration protocol.
4. Root spawns each applicable reviewer role as one strictly read-only subagent.
5. Roles run concurrently up to the available limit and in waves beyond it.
6. Root waits for every applicable role.
7. Root recomputes the content manifest. If scoped content changed, root rejects stale judgments, halts, and requires user recovery or explicit authorization of the current content before creating a new baseline and rerunning every affected role. Only an unchanged manifest permits scope verification and consolidation into the working ledger.

Do not begin writing while a required baseline role remains outstanding. Starting from an incomplete evidence model or ledger can optimize prose around a later-discovered fatal flaw.

## 4. Phase B — Root synthesis and repair selection

For every missing writing obligation or returned finding, root must:

1. verify location, evidence, rule, and scope;
2. merge true duplicates while preserving every affected claim/location;
3. resolve cross-role disagreement from evidence, not majority vote;
4. map a repair finding to `E1`–`E5`, and map any missing evidence or decision to `B1`–`B4`;
5. order repairs by scientific dependency;
6. apply the global-rebuild triggers in `revision-protocol.md` and select the smallest coherent repair scope that closes the root cause;
7. select one coherent, auditable edit batch.

Typical cross-role interactions:

- R1 wants a stronger contribution claim while R3 finds insufficient evidence: evidence wins; calibrate or block.
- R2 exposes an assumption that R4 finds difficult to explain: preserve the assumption and improve its local explanation.
- R3 finds a misleading plot while R4 suggests layout compression: correct quantitative integrity before layout.
- R4 recommends deletion that removes a limitation R1/R2 considers material: retain the limitation and improve placement.

If alternatives encode different contribution priorities, system models, or author intent, record `B4 — author decision` instead of choosing rhetorically.

## 5. Phase C — Single-writer revision

The root performs the selected edit batch directly.

Before editing:

- capture the preservation snapshot from `change-safety.md`;
- capture the preserve/amplify map for strong examples, figures, result framings, terminology, boundaries, and author voice;
- state the writing obligations or findings the batch intends to close;
- state exact resolution tests;
- confirm no blocker is being disguised as prose work.

When a global rebuild is triggered, establish the archetype route, thesis-support tree, design-derivation map, headline-evidence map, and dependency outline before the root edits sentences. Reviewer subagents may assess those structures but may not author the replacement text.

During editing:

- modify only the frozen scope;
- keep all subagents idle or read-only;
- make no Git or source-control call;
- create no backup copy;
- do not ask a subagent to draft replacement prose that the root applies blindly;
- preserve supported claims, numbers, citations, equations, identifiers, macros, limitations, and source language.

After writing, run local non-Git preservation checks before asking reviewers to inspect the new state. Then freeze a **post-edit, pre-command** content manifest for every scoped object and a non-content source-tree inventory of paths/types/sizes needed to detect newly created caches or generated files without reading out-of-scope contents.

Any compile, render, lint, test, benchmark, or script execution is root-only. Before running it, assess filesystem, network, device, database, credential, and external-service effects. Prefer a read-only sandbox/mount for the source; use a fresh isolated temporary directory outside the source tree for every writable output/cache; and serialize execution while reviewer subagents are inactive. After execution, recompute both the post-edit content manifest and source-tree inventory. If either changes, halt and treat it as an unauthorized side effect. If read-only isolation or complete side-effect detection is unavailable, keep the validation as a blocker rather than running it.

After preservation and authorized validation, promote the verified post-edit manifest to the regression-gate manifest. This verified manifest, not a live path or timestamp, identifies the version reviewed in the next gate.

## 6. Phase D — Parallel regression gate

Re-run every applicable baseline role using the same role boundaries and rule set.

Each role must inspect the **complete revised scope**, not only a diff or the sentences connected to its previous findings. Supply:

- the unchanged scope boundaries plus the new content manifest ID and per-object digests;
- the current complete text/files;
- the consolidated findings assigned to that role;
- which findings the edit claims to resolve;
- the same finding and coverage schema.

Ask each role to return:

```text
Previously assigned findings:
- closed, with resolution evidence
- improved but open
- regressed
- blocked
New findings:
Rules re-applied — no findings:
Rules not assessable:
Role-level gate:
Scope manifest ID reviewed:
```

Reuse an existing role subagent with a focused follow-up when its context remains accurate and this reduces setup cost. Restate scope and require a full-scope read each round. Replace/rerun a role when its context is stale, it exceeded scope, or independence is important after a major structural rewrite.

The root waits for every applicable role, verifies that each echoed the current manifest ID, recomputes the manifest to detect concurrent changes, and then updates the one canonical ledger. If scoped content changed during the wave, affected results are stale: halt and do not refreeze until the user recovers the intended content or explicitly authorizes the current content as a new baseline, then rerun every affected role. One clean role does not close another role's unresolved finding.

## 7. Iterate safely

After the regression gate, the root chooses:

- another root-only edit batch, if at least one evidence-safe actionable repair remains;
- a blocked fixed point, with precedence over clean, if no admissible edit remains and any `B1`–`B4` item remains;
- a no-progress/oscillation stop under `convergence-loop.md`;
- a locally clean fixed point, only after all applicable roles and root checks pass and zero `B1`–`B4` items remain.

An `improved but open` item authorizes another round only when the ledger records an observable reduction in severity, affected claims, or unresolved conditions, or a passed predeclared intermediate test, and names the next admissible repair. After one unsuccessful attempt, a distinct predeclared admissible alternative may run when it changes the repair mechanism and the repeated-failure stop has not been met. Otherwise apply the no-progress rule in `convergence-loop.md`.

Do not spawn more agents merely because a finding remains hard. A new subagent is justified only by a new independent reviewer role, a bounded external verification task, or recovery from a failed/incomplete role.

## 8. Multi-agent convergence gate

In addition to the base convergence criteria, multi-agent fixed point requires:

- every applicable role completed after the last edit;
- every role echoed the same final content manifest ID, and the root verified that manifest unchanged after the wave;
- no role reported an unresolved actionable `S0`–`S3` finding;
- no `B1`–`B4` blocker remains;
- all conflicts were adjudicated or converted to explicit blockers;
- the coverage ledger identifies omitted/not-assessable roles and rules;
- root independently checked preservation invariants;
- no agent used Git or modified shared state during the loop.

Unanimity is neither necessary nor sufficient. A minority evidence-backed fatal finding remains open; unanimous unsupported reassurance does not close a finding.

If a required role fails and cannot be safely rerun, report `blocked — incomplete reviewer-role coverage`. Do not claim exhaustive convergence.

## 9. Scheduling for speed without conflict

- Keep one subagent per reviewer role; schedule excess roles in waves.
- Do not merge roles solely because concurrency is limited.
- Do not run a writer subagent in parallel with reviewers.
- While reviewers run, root may prepare non-mutating ledger/synthesis scaffolding but may not edit the manuscript before the baseline or regression gate finishes.
- Run command-producing validation only through the root, serialized between reviewer waves and isolated outside the source tree.
- Use role-specific references and structured outputs to reduce context pollution.
- Use focused follow-ups for missing coverage rather than rerunning unrelated roles.
- Track total rounds and role completion, but never use their count as the convergence criterion.

## 10. Git-free enforcement across the agent tree

Every role prompt and follow-up must repeat this operational boundary once:

```text
Do not invoke Git directly, through a script/alias, or through an IDE/source-
control API. Do not create a branch, commit, stash, tag, patch, diff report, or
backup. Inspect only the authorized current content and return a read-only
review to the root.
```

If any subagent invokes Git, its scientific findings may still be inspected, but the loop no longer satisfies the promised Git-free execution. Stop and disclose the breach. Do not accept a changed working state as a new baseline; require the user to recover the intended content or explicitly authorize the current content before restarting the affected gate without Git.

## 11. Final human handoff

The root reports:

- scope and final version reviewed by all roles;
- reviewer roles used and any roles not assessable;
- number of completed root edit rounds;
- findings closed, blocked, or unresolved;
- validations actually performed;
- confirmation that the root was the sole writer;
- confirmation that no agent used Git during the loop;
- readiness for the human to inspect the final Git diff and comment.

Human feedback starts a new frozen-scope, Git-free loop under the same role architecture.

## Sources

This protocol combines the sibling multi-agent review protocol with the evidence and convergence constraints in this skill. It follows [OPENAI-CODEX-SUBAGENTS] and [OPENAI-MULTI-AGENT]: delegate independent read-heavy work, retain root synthesis, respect runtime concurrency, account for additional token use, and avoid parallel writes to shared mutable state. Source keys are defined in the sibling `systems-paper-review/references/source-registry.md`. Last checked 2026-09-03.
