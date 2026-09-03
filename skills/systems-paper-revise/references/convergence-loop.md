# Evidence-Safe Convergence Loop

The loop is a fixed-point search over the frozen scope:

```text
freeze scope and evidence
  -> recover the scoped writing obligation
  -> adversarial review or missing-text dependency check
  -> actionable ledger
  -> root-only evidence-safe writing batch
  -> preservation checks
  -> full in-scope re-review (same read-only roles)
  -> repeat or stop
  -> human examines final Git diff and comments
```

The loop contains **no Git operation by the root or any subagent**. Git is reserved for the human review that follows the completed or blocked loop. For scopes that use reviewer subagents, also follow [multi-agent-revision.md](multi-agent-revision.md).

## State model

Track findings by stable ID across rounds.

| State | Meaning | Next action |
|---|---|---|
| `new` | Newly found actionable issue | Diagnose root cause and evidence |
| `actionable` | An `E1`–`E5` repair is available | Batch and edit |
| `resolved` | Resolution test passes under full re-review | Keep closed unless regression appears |
| `regressed` | A prior fix or other edit recreated the issue | Reopen and identify interaction |
| `blocked-B1` | Missing experiment/data/proof/implementation evidence | Stop claiming automatic solvability |
| `blocked-B2` | Citation/factual source decision unresolved | Verify or ask author |
| `blocked-B3` | Required context outside frozen scope | Ask to expand scope or stop |
| `blocked-B4` | Author intent/tradeoff decision required | Present alternatives and stop |
| `preference` | Correct optional alternative | Exclude from convergence unless user requested it |

## Round 0 — Baseline

1. Freeze the scope, evidence classes, and invariants.
2. If prose exists, run the complete applicable sibling review protocol. If prose is missing, identify the minimum reader promise, supported answer, dependencies, and handoff required by the requested scope.
3. When multi-agent review applies, wait for every applicable read-only reviewer role and let the root consolidate one ledger.
4. Create the applicable claim inventory, claim-evidence matrix, and working ledger.
5. Record baseline counts by severity/status when findings exist, not a single score.
6. Separate writable obligations or repairable findings from blockers.

Do not skip Round 0 even when the user supplies reviewer comments; those comments can miss regressions and may contain invalid proposed fixes.

## Each edit round

### A. Select the correct scale and a dependency-safe batch

Before selecting sentences, apply the local-repair and structural-rebuild rules in `revision-protocol.md`. A requested missing passage starts from its minimal reader obligation and evidence dependencies. When a rebuild is triggered, first establish an evidence-bounded thesis/support tree and dependency outline, then repair section roles and only afterward draft paragraphs. `Smallest` means the smallest coherent scope that completes the obligation or closes the root cause, not the fewest changed words.

Choose the highest-impact writing obligation or root cause that does not depend on an unresolved blocker. Prefer one batch that can close multiple dependencies, for example:

- calibrate a central claim before reorganizing its evidence paragraph;
- define the system model before polishing component descriptions;
- correct evaluation boundary before editing result interpretation;
- settle canonical terminology before sentence-level consistency edits.

Avoid simultaneous changes whose semantic interactions cannot be audited.

### B. State preservation invariants

Before editing, list values/tokens/meanings that must remain unchanged. Use `change-safety.md`.

### C. Apply the correctly scoped writing repair

The root is the sole writer. Reviewer subagents must be idle or read-only while this batch is applied.

A draft or edit is admissible only if:

1. it remains inside scope;
2. every added factual proposition has evidence;
3. it completes a declared writing obligation or addresses the diagnosed root cause;
4. it preserves technical intent or openly calibrates it;
5. it does not hide a limitation or unresolved finding.

After adding missing prose or rebuilding structure, verify that the outline and prose make the problem, thesis hierarchy, design derivation, and decisive evidence mutually consistent. After a local repair, verify that it did not silently change any of those structures.

### D. Run local preservation checks

Compare claims, numbers, units, citations, equations, identifiers, labels, macros, and requested language before/after. If source is a file, inspect only non-Git file content and relevant tool output.

### E. Run the full gate

Reapply every relevant review pass to the entire frozen scope. Do not inspect only changed sentences. In multi-agent mode, use the same role boundaries, wait for all applicable roles, and let the root reconcile their results. Record:

- findings closed and resolution evidence;
- findings still actionable;
- blockers unchanged or newly exposed;
- regressions/new findings;
- coverage changes.

### F. Decide whether another round can make progress

Continue if at least one missing writing obligation or actionable finding has an admissible writing move and the previous round did at least one of the following:

- discharged a declared reader obligation with evidence-bounded prose;
- closed a finding's resolution test;
- reduced an evidence-backed severity, affected-claim set, or unresolved condition;
- passed a predeclared intermediate resolution test needed for the next repair;
- unlocked a dependency that makes a specific next repair admissible.

An incomplete obligation or `improved but open` finding counts as progress only when the ledger records one of these observable changes and names the next admissible move. A larger draft, smaller word count, or more fluent wording alone is not progress.

One unsuccessful repair does not create a dead state. Continue with a distinct, predeclared admissible alternative when it addresses the same root cause through a materially different change and the repeated-failure stop condition has not been met. Record why the alternative can satisfy the unresolved test. Stop only when the repeated-failure criterion is met or no specific admissible alternative remains.

## Convergence criteria

### Fixed point — locally clean

Declare `fixed point — no actionable issue remains within scope` only when:

- every declared writing obligation in scope has either been discharged or exposed as a blocker;
- every applicable review pass has been rerun after the last edit;
- no `S0`–`S3` confirmed defect remains;
- no unresolved reviewer risk has an evidence-safe in-scope edit available;
- no `B1`–`B4` blocker remains;
- style preferences are either requested and resolved or explicitly excluded;
- preservation checks pass;
- all unassessable rule families and external dependencies are disclosed.

This means the current material has no further supported automatic edit under the current scope. It does **not** mean:

- the whole paper has no problem;
- missing experiments are complete;
- novelty is proven over all literature;
- the artifact works in all environments;
- reviewers will accept the paper;
- the paper is publication-ready.

### Blocked fixed point

Declare `blocked — only evidence/context/source/author decisions remain` when no admissible edit remains but one or more `B1`–`B4` items persists. This outcome takes precedence over locally clean. Preserve the blocker in the final handoff; do not delete or euphemize it.

### No-progress / oscillation stop

Stop when either occurs:

- two successive admissible attempts recreate the same semantic defect in different wording;
- a change improves one equal-or-higher severity finding only by reopening another;
- repeated attempts fail the same declared resolution or intermediate test, the ledger shows no observable severity/scope/condition reduction, and no specific next admissible repair remains;
- alternative repairs encode different author intent.

Revert only the current unsafe edit using direct file editing, not Git, then report the decision needed.

## No arbitrary round or score threshold

Never stop merely because:

- three/four/six/ten rounds are complete;
- a reviewer score reaches a numerical threshold;
- a language linter is clean;
- no new findings appeared in one shallow pass;
- token/time budget is inconvenient.

Conversely, do not paraphrase indefinitely after reaching a true fixed point. Optional stylistic alternatives do not keep the loop alive.

## Internal progress ledger

Maintain:

| Finding | Rule | Severity | Round found | Repair class | State after round | Resolution evidence | Dependency/blocker |
|---|---|---|---|---|---|---|---|

At each round, summarize:

```text
Round N
- Closed:
- Still actionable:
- Blocked:
- New/regressed:
- Preservation checks:
- Next batch or stop reason:
```

This ledger need not be written to disk unless the user asks for a report file.

## Git-free guarantee

During Round 0 through the final automatic gate, every root and subagent instruction must enforce:

- do not invoke `git` directly or through scripts/aliases;
- do not use IDE/source-control APIs as a substitute;
- do not create commits, branches, stashes, patches, tags, or backup files;
- do not use `git diff` even read-only;
- inspect edited file content and tool outputs directly.

After the loop, tell the user it is ready for **their** Git diff review and feedback. Only a new explicit request authorizes Git use.

## Human feedback starts a new loop

When the user provides comments after inspecting the diff:

1. Treat comments as new requirements/objections, not automatically correct facts.
2. Re-freeze scope; retain the same scope unless the user changes it.
3. Verify technical/factual suggestions.
4. Add valid issues to the ledger and run another Git-free loop.
5. Hand back for human diff review again.

## Sources

This loop operationalizes the user's requested human-after-loop Git workflow and the sibling review gate. It also adapts staged revision patterns from [YSLAB-REVISION] and [SIMCHOWITZ-WRITING] without fixed round counts. Source keys are in the sibling `source-registry.md`. Last reconciled 2026-09-03.
