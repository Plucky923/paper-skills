# Multi-Agent Orchestration for Systems-Paper Review

Use this protocol to parallelize independent reviewer perspectives without weakening scope, evidence discipline, or coverage. It is an optional execution mode of `systems-paper-review`, not a different review standard. The root coordinator remains responsible for the final report.

## 1. Select single-agent or multi-agent mode

Use multi-agent mode when collaboration tools are available and the frozen scope contains independent, substantial review work, such as:

- a full paper or several substantial sections;
- a manuscript plus explicitly scoped figures, code, data, or experiment scripts;
- contribution, mechanism, evaluation, and presentation arguments that can be inspected independently;
- several in-scope factual, venue, citation, or closest-work checks that can proceed independently;
- a final full-scope gate where independent perspectives materially improve coverage.

Prefer single-agent mode when:

- the scope is one sentence, a short paragraph, one caption, or another narrow object;
- one ordered reasoning chain dominates the task;
- all roles would need the same small context and reach the same local judgment;
- collaboration tools are unavailable;
- parallelism would be dominated by one external operation;
- token cost or coordination would exceed the likely coverage or latency benefit.

Do not use a fixed word, page, or token threshold. Decide from task shape. Never enlarge the user's scope merely to justify delegation.

## 2. Root coordinator responsibilities

Only the root coordinator may:

1. freeze and interpret scope;
2. create and verify the immutable scope manifest;
3. build the shared claim inventory;
4. execute any authorized command that can write temporary output;
5. select applicable reviewer roles;
6. assign concurrency waves;
7. adjudicate contradictory findings;
8. merge duplicates while preserving affected locations;
9. determine status, severity, and final gate result;
10. produce the user-facing report.

The root must not outsource final synthesis to another subagent. A role agent may give a role-level risk summary, but not the paper-wide verdict.

## 3. Create one immutable review packet

Before spawning any role, prepare the same scope packet for all roles:

```text
Review mode: multi-agent, strictly read-only
Exact in-scope objects:
Explicitly out-of-scope objects:
Scope manifest ID and per-object content digests:
Source language and report language:
Venue/cycle/track/stage, if named:
External verification permitted: yes | no | limited to ...
Subagent tool execution permitted: none | specified strictly read-only checks
Root-brokered command evidence available:
Location convention: page/section/paragraph/line/figure/table/path
Shared claim inventory:
Known missing context:
Required finding schema:
Role-specific assignment and references:
```

For file scopes, provide explicit paths. For a named range, provide anchors or line boundaries. For pasted text, include only the pasted text. Do not give a broad repository path when only one file or passage is authorized.

Every role receives:

- [review-protocol.md](review-protocol.md);
- this frozen packet;
- only its role-specific references;
- the same finding schema and evidence/status/severity definitions.

Also provide `source-registry.md` or the relevant verified official source only to roles that need provenance, literature calibration, novelty verification, or venue rules. Do not preload it into purely internal technical or prose checks.

Do not send one role another role's raw reasoning. Independence is useful; the root handles reconciliation after results return.

## 4. Freeze one exact content version

Before each reviewer wave, the root creates a non-Git scope manifest:

```text
Manifest ID: <round/wave label plus digest of ordered entries>
Entries:
- <exact path, pasted-object label, or path:range> | <content SHA-256>
Dependencies explicitly included:
Dependencies explicitly excluded or missing:
Created before wave at:
Verified unchanged after wave at:
```

Digest the exact bytes of each in-scope file. For pasted text, digest the exact supplied text. For a named range, record its file path/anchors and digest the exact extracted range. For an explicit whole LaTeX project, first freeze the authorized transitive dependency list—root/source files, bibliography, figures, class/style files, and build configuration actually needed—then digest each entry. Do not discover this closure by opening unauthorized files: a named `main.tex` alone permits only parsing its dependency names and yields a context blocker until the required files are added to scope.

Every role prompt includes the same manifest ID, and every role result echoes it. The root recomputes the manifest after all roles return and before synthesis. If any entry changes because of an external edit, tool side effect, or agent violation, discard stale judgments and halt the gate. Do not silently accept or refreeze the modified state, and do not create or use backup copies or Git for recovery. Disclose the affected objects and before/after digests; require the user to recover the intended content or explicitly authorize the current content as a new baseline. Only then create a new manifest and rerun all affected roles. Do not infer a version from timestamps or Git.

## 5. Broker command-producing evidence through the root

Reviewer subagents may use only operations that are provably read-only for local and external state. They must not compile, render, lint, run tests/benchmarks, execute experiment scripts, or invoke a command that may create caches, logs, generated files, network requests with side effects, device state, database changes, or other persistent output.

When an authorized check needs command execution:

1. The root assesses filesystem, network, device, database, credential, and external-service side effects.
2. The root refuses or requests authorization for any effect outside the user's scope.
3. The root freezes a pre-command content manifest and, for the explicitly scoped project root, a non-content tree inventory of paths/types/sizes needed to detect new caches or generated files without reading out-of-scope contents.
4. The root runs the source through a read-only sandbox/mount when available, uses a fresh isolated temporary directory outside the source tree, and redirects every writable cache/output there.
5. The root serializes the command outside active reviewer work on shared state.
6. The root records command, environment, input manifest ID, exit status, and relevant output.
7. The root verifies both scoped content digests and the source-tree inventory are unchanged.
8. The root distributes the resulting evidence summary to the applicable roles.

If read-only isolation or complete side-effect detection cannot be established, do not execute the command. Mark the check `not assessable` and name what safe environment or authorization is required.

## 6. Reviewer roles

Assign each applicable role to one distinct subagent. Do not create one subagent per rule or per reference: use coherent reviewer lenses that can reason across related rules.

### Role R1 — PC / Contribution Reviewer

**Primary question:** Is this an important, novel, coherent, and venue-relevant systems contribution?

**Load:**

- [paper-archetypes.md](paper-archetypes.md)
- [thesis-and-story.md](thesis-and-story.md)
- [research-contribution.md](research-contribution.md)
- [venue-overlays.md](venue-overlays.md) when a venue/cycle is named
- section contracts `SS-12`–`SS-16`, `SS-21`–`SS-24` when those sections are in scope

**Inspect:** primary archetype, controlling thesis, supporting-claim hierarchy, problem reality/significance, intellectual move, contribution type, closest-work delta, nontriviality, co-design, lessons, limitations, audience/venue fit, introduction promises, reader-memory result, and conclusion alignment.

**Do not:** attempt a detailed correctness proof, benchmark audit, or prose rewrite unless a local issue directly changes the contribution case.

### Role R2 — Domain / Technical Reviewer

**Primary question:** Does the system model and mechanism actually support its claimed properties under realistic assumptions and failures?

**Load:**

- [design-derivation.md](design-derivation.md)
- [technical-soundness.md](technical-soundness.md)
- relevant [research-contribution.md](research-contribution.md) rules only when assumptions or implementation maturity alter the contribution
- relevant externally verified primary technical sources when permitted

**Inspect:** constraint-to-requirement-to-mechanism derivation, actors, boundaries, assumptions, threat/fault/workload model, mechanisms, invariants, lifecycle, concurrency, failure/recovery, edge cases, design choices, alternatives, cost boundaries, scale, security/privacy, implementation status, and internal technical consistency.

**Do not:** infer missing implementation behavior, run unauthorized artifact operations, or treat a plausible counterexample as confirmed without evidence.

### Role R3 — Evaluation / Artifact Reviewer

**Primary question:** Does the evidence validly establish every empirical claim, and can the in-scope artifact support or reproduce it?

**Load:**

- relevant [thesis-and-story.md](thesis-and-story.md) headline-evidence rules
- [examples-figures-results.md](examples-figures-results.md) when headline results or motivating measurements are in scope
- [evaluation.md](evaluation.md)
- [artifacts-reproducibility.md](artifacts-reproducibility.md) only when artifacts are explicitly in scope
- quantitative-integrity rules `FL-03`–`FL-05`, `FL-09`–`FL-10`

**Inspect:** thesis-to-decisive-evidence alignment, headline-result hierarchy, claim-evidence mapping, recoverable questions, baselines/configurations, workloads/data separation, metrics, measured boundary, procedure, repetition/uncertainty/statistics, end-to-end and mechanism evidence, sensitivity, negative results, graphical truth, interpretation, reproducibility, and artifact consistency.

**Do not:** change code/data/scripts, install dependencies, run commands that can write or affect external state, fabricate a missing experiment, or equate a repository's existence with reproducibility. Request root-brokered execution evidence when needed.

### Role R4 — Reader / Presentation Reviewer

**Primary question:** Can a non-specialist systems reviewer recover the intended argument accurately and efficiently from the rendered material?

**Load:**

- relevant [thesis-and-story.md](thesis-and-story.md) reader-memory and attention rules
- [examples-figures-results.md](examples-figures-results.md) when examples, early figures, or headline results are in scope
- [structure-and-sections.md](structure-and-sections.md)
- [prose-and-terminology.md](prose-and-terminology.md)
- [figures-tables-latex.md](figures-tables-latex.md), excluding quantitative-validity judgments already owned by R3

**Inspect:** reader-memory result, global and local flow, dependency order, section/paragraph promises, examples and counterexamples, argumentative work of early figures, terminology, definitions, referents, claim language, grammar in the source language, figure/table readability, captions/callouts, citations/references, math notation, LaTeX correctness, and rendered layout when in scope.

**Do not:** downgrade unsupported science to a style issue, impose nonuniversal house preferences, rewrite text, or compile/render the project. Inspect root-brokered rendered evidence when available.

## 7. Role applicability

All four roles apply to a full systems-paper review. For narrower scopes:

| Scope | Minimum applicable roles |
|---|---|
| Introduction/abstract/conclusion | R1 + R4; add R2/R3 for technical or result claims |
| Design/protocol/mechanism | R2 + R4; add R1 for contribution/design-choice claims |
| Evaluation section or result figures | R3 + R4; add R2 when mechanism explanations are claimed |
| Related work/novelty passage | R1 + R4 |
| Paper plus artifact | R1 + R2 + R3 + R4 |
| Short prose-only passage | Prefer single-agent with the relevant lenses |

Omitting a role because it is not applicable is valid. Omitting it because no concurrency slot is currently free is not; schedule another wave.

## 8. Concurrency and scheduling

Use no more active subagents than the runtime permits. Keep one subagent per role even when roles run in separate waves.

Recommended scheduling when three subagent slots are available:

1. Spawn R1, R2, and R3 concurrently.
2. Wait for the first completed role.
3. Start R4 in the freed slot.
4. Wait for all applicable roles before synthesis.

For other limits, schedule the same roles in as few waves as possible. Do not merge R2 and R3 merely to fit a concurrency limit; their adversarial questions differ. Do not allow role subagents to spawn descendants unless the root explicitly delegates a concrete, bounded subtask that cannot be handled within the role.

The root may organize the claim inventory and synthesis scaffolding while roles run, but must not finalize before all applicable results arrive.

## 9. Subagent contract

Each role prompt must state:

- exact role and primary question;
- exact frozen scope and explicit exclusions;
- strict read-only behavior, including no file edits;
- allowed references, strictly read-only tools, and external verification boundary;
- the scope manifest ID to echo unchanged;
- prohibition on compiling, rendering, tests, scripts, or any command that may write or affect external state;
- requirement to inspect every applicable assigned rule;
- requirement to distinguish confirmed defects, unresolved risks, and preferences;
- the finding schema from [review-protocol.md](review-protocol.md);
- a role coverage summary and not-assessable rules;
- no final paper-wide verdict;
- no descendant delegation unless authorized;
- concise return of evidence and findings rather than raw notes.

Use this task shape:

```text
Act as <role>. Review only <scope>. Do not open or modify anything outside it.
Use <common references> and <role references>. Apply every assessable assigned
rule. Return findings in the required schema, followed by claim coverage,
rules applied with no findings, rules not assessable and why, and any conflict
the root must adjudicate. Remain strictly read-only. Do not issue the final
paper-wide verdict.
```

## 10. Required role result

Every role returns:

```text
Role:
Scope manifest ID:
Objects actually inspected:
External/tool checks actually performed:
Top role-specific rejection threats:
Findings: [review-protocol finding schema]
Claim-evidence observations:
Rules applied — no findings:
Rules not assessable and reason:
Possible duplicates or cross-role dependencies:
Role-level gate: clear | actionable | blocked
```

`Role-level gate` does not determine the final gate. A role may be clear while another finds a blocker.

## 11. Root synthesis

After all applicable roles return:

1. Verify every role echoed the current scope manifest ID.
2. Recompute the manifest. If scoped content changed, halt and do not refreeze; require user recovery or explicit authorization of the current content as a new baseline, then rerun every affected role.
3. Verify each role stayed inside scope and remained read-only.
4. Reject findings that lack evidence or exceed the assigned scope.
5. Merge findings only when they share the same root cause and repair direction; retain all locations and affected claims.
6. Keep separate findings whose resolution tests differ.
7. Reconcile severity/status from evidence, not by voting or automatically choosing the harshest role.
8. For a material conflict, ask the conflicting role for a focused follow-up when possible; otherwise report the uncertainty and resolution test.
9. Build one claim-evidence matrix and one coverage ledger.
10. Apply the final rejection gate in the root context.
11. Return one unified report in the user's language.

Do not expose raw subagent transcripts as the report. Summaries must preserve evidence, locations, rule IDs, dissent that affects confidence, and all not-assessable coverage.

## 12. Failure handling

- If a role exceeds scope, invokes a potentially writing command, or edits state, discard its result and stop further side effects. Do not refreeze or continue from the modified state. Disclose the breach and require user recovery or explicit authorization of a new baseline before rerunning.
- If the scope manifest changes during a wave, treat all affected role results as stale and halt. Do not claim a gate result until the user-established intended content is frozen and reviewed again.
- If a role fails or returns incomplete coverage, follow up with the missing bounded assignment or rerun that role.
- If a required role remains unavailable, mark its rules `not assessable — role unavailable`; do not claim exhaustive multi-role coverage or a clean gate.
- If collaboration tools disappear mid-run, complete unperformed roles sequentially in the root context.
- If the user changes scope while roles run, stop or disregard stale assignments, refreeze scope, and redelegate only the new work.

## 13. Performance discipline

Subagents increase token use. Obtain speed and focus benefits by:

- delegating only independent roles justified by scope;
- loading only role-specific references;
- sharing one claim inventory instead of making each role reconstruct unrelated context;
- returning structured findings rather than long narrative reviews;
- scheduling to the actual concurrency limit;
- avoiding repeated external searches across roles;
- using focused follow-ups rather than rerunning every role for one missing field.

Lower latency or fewer main-context tokens count as improvement only if final coverage, evidence quality, and scope compliance remain intact.

## Sources

This protocol applies the review principles in this skill and the orchestration guidance in [OPENAI-CODEX-SUBAGENTS] and [OPENAI-MULTI-AGENT]. OpenAI documents that Codex can follow skill instructions requesting delegation, that parallel read-heavy work is a strong use case, that the root synthesizes results, and that parallel work costs more tokens and is a poor fit for shared mutable state. See [source-registry.md](source-registry.md).
