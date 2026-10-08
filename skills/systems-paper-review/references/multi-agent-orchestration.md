# Multi-Agent Orchestration for Systems-Paper Review

Use this protocol for parallel reviews that occur independently. Keep scope, evidence discipline, and coverage unchanged. This is an optional `systems-paper-review` execution mode. The root coordinator owns the final report.

## 1. Select single-agent or multi-agent mode

If collaboration tools are available, use multiple agents for substantial independent work within the defined scope. Examples include:

- A full paper or multiple substantial sections.
- A manuscript with explicitly scoped figures, code, data, or experiment scripts.
- Independent contribution, mechanism, evaluation, and presentation arguments.
- Independent factual, venue, citation, or closest-work checks in scope.
- A last full-scope gate where different perspectives remove important coverage gaps.

If possible, use one agent for these conditions:

- One sentence, short paragraph, caption, or other narrow object.
- One controlling sequence of reasoning.
- The same small context and local judgment for all roles.
- Unavailable collaboration tools.
- One controlling external operation with no parallel benefit.
- Token or coordination cost greater than the likely coverage or latency benefit.

Select mode from task structure. Use no fixed word, page, or token threshold. Keep the user's scope unchanged during delegation.

## 2. Root coordinator responsibilities

Keep these responsibilities with the root:

1. Record scope. Give its interpretation.
2. Make the immutable scope manifest.
3. Do its verification.
4. Make the shared claim inventory.
5. Execute authorized commands with temporary output.
6. Select applicable reviewer roles.
7. Set concurrency waves.
8. Get decisions about contradictory findings.
9. Combine repeated findings with all affected locations.
10. Select status, severity, and final gate result.
11. Write the report for the user.

Keep final synthesis with the root. A role agent can give a role-specific risk summary. It cannot give the paper-wide verdict.

## 3. Make one immutable review packet

Before subagent creation, make the same scope packet for all roles.

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

For files, give their full paths. For a named range, give anchors or line boundaries. For pasted text, give only that text. Give a repository path only if the repository is authorized scope.

Give each role these items:

- [review-protocol.md](review-protocol.md).
- This scope packet with unchanged content.
- Only the references for that role.
- The same finding schema and evidence, status, and severity definitions.

Give [source-registry.md](source-registry.md) or verified official sources only to roles with source requirements. Applicable requirements include provenance, literature calibration, novelty checks, and venue rules. Keep purely internal technical or prose checks free of that unnecessary load.

Keep each role's raw reasoning unavailable to other roles. The root gets decisions about differences after results arrive.

## 4. Keep one unchanged content version

Before each reviewer wave, make a non-Git scope manifest at the root.

```text
Manifest ID: <round/wave label plus digest of ordered entries>
Entries:
- <exact path, pasted-object label, or path:range> | <content SHA-256>
Dependencies explicitly included:
Dependencies explicitly excluded or missing:
Created before wave at:
Verified unchanged after wave at:
```

Calculate a digest of all bytes of each file. For pasted text, use the supplied text unchanged. For a range, record its path and anchors. Calculate a digest of the extracted range unchanged.

For an authorized full LaTeX project, first record the necessary transitive dependency list. Include source files, bibliography, figures, class or style files, and build configuration. Keep that list unchanged. Then calculate each entry's digest.

Keep unauthorized files unopened during dependency discovery. With `main.tex` alone, read only dependency names. Missing authority for the dependencies gives a context blocker.

Put the same manifest ID in each role prompt. Make sure that each result gives the unchanged ID. After all results return, calculate the manifest again before synthesis.

If an external edit, tool side effect, or agent violation changes an entry, discard stale judgments. Stop the gate. Keep the modified content outside a new baseline without user authority. Do not use backup copies or Git for recovery.

Give affected objects and their before and after digests. Before a new baseline, get user recovery or clear authority for the content after the change. After that, make a new manifest. Run all affected roles again.

Use content evidence for version identity. Timestamps and Git alone are insufficient.

## 5. Give command-producing evidence through the root

Give subagents only operations with provably read-only local and external behavior. Keep compilation, rendering, lint, tests, benchmarks, and experiment scripts with the root.

Also keep potentially mutating commands with the root. Possible effects include caches, logs, generated files, network mutations, device state, database changes, and saved outputs.

If command execution is necessary for an authorized check, use these root steps:

1. Examine filesystem, network, device, database, credential, and external-service side effects.
2. Reject effects outside scope or get the required authority.
3. Before execution, make the content manifest.
4. For the scoped project root, make a non-content inventory of paths, types, and sizes.
5. Keep file contents outside scope unread during that inventory.
6. If available, use a read-only sandbox or mount for the source.
7. Use a fresh isolated temporary directory outside the source tree.
8. Put all writable caches and outputs there.
9. Execute the command outside active reviewer work on shared state.
10. Record command, environment, input manifest ID, exit status, and related output.
11. Make sure that scoped digests and the source-tree inventory stay unchanged.
12. Give the resulting evidence summary to applicable roles.

If read-only isolation or full side-effect detection is unavailable, do not execute the command. Record `not assessable`. Give the missing isolation or side-effect-detection prerequisite. Get author authority only for effects that the review contract permits.

## 6. Reviewer roles

Give each applicable role to a different subagent. Use coherent review lenses across related rules. Do not create one subagent per rule or reference.

### Role R1 — PC / Contribution Reviewer

**Primary question:** Is this an important, novel, coherent systems contribution related to the venue?

**Load:**

- [paper-archetypes.md](paper-archetypes.md)
- [thesis-and-story.md](thesis-and-story.md)
- [research-contribution.md](research-contribution.md)
- [venue-overlays.md](venue-overlays.md), for a specified venue or cycle
- Section contracts `SS-12`–`SS-16` and `SS-21`–`SS-24`, for sections in scope

**Examine:** Primary archetype, thesis, claim hierarchy, problem evidence, significance, intellectual move, contribution type, closest-work difference, nontriviality, and co-design. Also examine lessons, limitations, audience or venue fit, introduction promises, reader memory, and conclusion agreement.

**Boundary:** Detailed correctness proofs, benchmark audits, and prose revisions are outside this role. Examine local issues only where they directly change the contribution case.

### Role R2 — Domain / Technical Reviewer

**Primary question:** Do the model and mechanism show their properties with realistic assumptions and failures?

**Load:**

- [design-derivation.md](design-derivation.md)
- [technical-soundness.md](technical-soundness.md)
- [research-contribution.md](research-contribution.md), where assumptions or implementation maturity change the contribution
- Related verified primary technical sources, where authorized

**Examine:** Constraint-to-requirement-to-mechanism derivation, actors, boundaries, assumptions, threat or fault or workload models, mechanisms, invariants, lifecycle, and concurrency. Also examine failure, recovery, edge cases, design choices, alternatives, cost boundaries, scale, security, privacy, implementation status, and internal consistency.

**Boundary:** Keep missing implementation behavior unresolved. Keep unauthorized artifact operations outside the role. A counterexample with evidence for its applicability must still have evidence for confirmed status.

### Role R3 — Evaluation / Artifact Reviewer

**Primary question:** Does evidence show each empirical claim? Can artifacts in scope give evidence for or reproduce it?

**Load:**

- Headline-evidence rules in [thesis-and-story.md](thesis-and-story.md)
- [examples-figures-results.md](examples-figures-results.md), for headline results or motivating measurements in scope
- [evaluation.md](evaluation.md)
- [artifacts-reproducibility.md](artifacts-reproducibility.md), only for explicitly scoped artifacts
- Quantitative-integrity rules `FL-03`–`FL-05` and `FL-09`–`FL-10`

**Examine:** Thesis-evidence agreement, headline hierarchy, claim-evidence relations, questions, baselines, configurations, workloads, data separation, metrics, measured boundaries, and procedure. Also examine repetitions, uncertainty, statistics, end-to-end evidence, mechanism evidence, sensitivity, negative results, graphics, interpretation, reproducibility, and artifact consistency.

**Boundary:** Keep code, data, scripts, and dependencies unchanged. Keep mutating commands outside the role. Use only experiments with evidence. Repository existence alone does not show reproducibility. If necessary, get execution evidence from the root.

### Role R4 — Reader / Presentation Reviewer

**Primary question:** Can a systems reviewer outside the specialty find the intended argument accurately and efficiently from rendered material?

**Load:**

- Reader-memory and attention rules in [thesis-and-story.md](thesis-and-story.md)
- [examples-figures-results.md](examples-figures-results.md), for examples, the first figures, or headline results in scope
- [structure-and-sections.md](structure-and-sections.md)
- [prose-and-terminology.md](prose-and-terminology.md)
- [figures-tables-latex.md](figures-tables-latex.md), except quantitative-validity judgments owned by R3

**Examine:** Reader memory, global and local logic, dependency sequence, and section or paragraph promises. Examine examples, counterexamples, arguments in the first figures, terminology, definitions, referents, and claim language. Also examine source-language grammar, visual readability, captions, callouts, citations, references, notation, LaTeX correctness, and rendered layout in scope.

**Boundary:** Do not treat scientific evidence defects as style defects. Use house preferences only where applicable. Keep text unchanged. Keep compilation and rendering with the root. Examine the root's rendered evidence where available.

## 7. Role applicability

For a full systems-paper review, use all four roles. For narrower scopes, use this table.

| Scope | Minimum applicable roles |
|---|---|
| Introduction/abstract/conclusion | R1 + R4. Add R2/R3 for technical or result claims. |
| Design/protocol/mechanism | R2 + R4. Add R1 for contribution or design-choice claims. |
| Evaluation section or result figures | R3 + R4. Add R2 for mechanism explanation claims. |
| Related work/novelty passage | R1 + R4 |
| Paper plus artifact | R1 + R2 + R3 + R4 |
| Short prose-only passage | If possible, use one agent with applicable lenses. |

Include each applicable role. If slots are unavailable, use another wave for necessary roles.

## 8. Concurrency and scheduling

Keep active subagents within runtime limits. Keep one subagent per role across different waves.

If three subagent slots are available, use this sequence:

1. Start R1, R2, and R3 concurrently.
2. Wait for the first role to complete its work.
3. Start R4 in the available slot.
4. Before synthesis, wait for all applicable roles.

For other limits, use the fewest feasible waves. Keep R2 and R3 different because their questions differ. Let descendants work only on clear root assignments. Give them bounded subtasks beyond the role's capacity.

During reviews, the root can organize claims and prepare the synthesis structure. Keep last synthesis pending until all applicable results arrive.

## 9. Subagent contract

Give these items in each role prompt:

- Specified role and primary question.
- Specified scope with unchanged content and clear exclusions.
- Strict read-only behavior, including unchanged files.
- Permitted references, read-only tools, and external-check boundaries.
- Scope manifest ID for unchanged return.
- Compilation, rendering, tests, scripts, and potentially mutating commands outside the role.
- All applicable assigned rules as required inspection.
- Give each finding its corresponding status: confirmed defect, unresolved risk, or preference.
- Finding schema from [review-protocol.md](review-protocol.md).
- Role coverage summary and not-assessable rules.
- Paper-wide verdict reserved for the root.
- Descendant delegation only with authority.
- Short evidence and findings instead of raw notes.

Use this task structure:

```text
Act as <role>. Review only <scope>. Do not open or modify anything outside it.
Use <common references> and <role references>. Apply every assessable assigned
rule. Return findings in the required schema, followed by claim coverage,
rules applied with no findings, rules not assessable and why, and any conflict
the root must adjudicate. Remain strictly read-only. Do not issue the final
paper-wide verdict.
```

## 10. Required role result

Make sure that each role returns these fields:

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

`Role-level gate` does not select the final gate. One role can be clear while another finds a blocker.

## 11. Root synthesis

After all applicable roles return, use these steps:

1. Make sure that each role returned the scope manifest ID for this review.
2. Calculate the manifest again.
3. If content changed, stop the gate.
4. Before a new baseline, get user recovery or clear authority.
5. After baseline authority, run each affected role again.
6. Make sure that each role stayed within scope and read-only.
7. Reject findings without evidence or outside the assigned scope.
8. Combine findings only with the same root cause and repair direction.
9. Keep all their locations and affected claims.
10. Divide findings with different resolution tests.
11. Select severity and status from evidence.
12. Keep voting and automatic selection of the harshest role outside that decision.
13. For a conflict that affects conclusions, give the role a focused follow-up if possible.
14. If follow-up is unavailable, give the uncertainty and resolution test.
15. Make one claim-evidence matrix.
16. Make one coverage ledger.
17. Apply the final rejection gate in the root context.
18. Give one report in the user's language.

Keep raw subagent transcripts outside the report. Summaries must keep evidence, locations, rule IDs, consequential dissent, and all not-assessable coverage.

## 12. Failure handling

- If a role exceeds scope or mutates state, discard its result. Stop further side effects. Give the violation to the user. Before another review, get recovery or clear authority for a new baseline. Potentially mutating commands also cause this response.
- If the manifest changes during a wave, discard affected stale results. Stop the gate. Before another full review and gate result, get the user's intended baseline.
- If a role fails or gives incomplete coverage, give a bounded follow-up or run that role again.
- If a required role stays unavailable, record `not assessable — role unavailable`. Keep exhaustive-coverage and clean-gate claims unavailable.
- If collaboration tools disappear, do unfinished roles sequentially in the root context.
- If the user changes scope, stop or discard stale assignments. Record the new scope. Delegate only the new work.

## 13. Performance discipline

Subagents increase token use. For speed and focused context, use these practices:

- Delegate only independent roles justified by scope.
- Load only role-specific references.
- Give all roles one shared claim inventory.
- Give structured findings.
- Schedule within concurrency limits in effect.
- Do not repeat the same external searches across roles.
- Use focused follow-ups for missing fields.

Lower latency or fewer root-context tokens are improvements only with unchanged coverage, evidence quality, and scope compliance.

## Sources

This protocol uses the skill's review principles and [OPENAI-CODEX-SUBAGENTS] and [OPENAI-MULTI-AGENT] orchestration guidance. OpenAI documentation includes skill-directed delegation, parallel read-heavy work, root synthesis, increased token costs, and risks from shared mutable state. See [source-registry.md](source-registry.md).
