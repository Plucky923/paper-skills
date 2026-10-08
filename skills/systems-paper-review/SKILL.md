---
name: systems-paper-review
description: "Examine computer-systems research in the user's specified scope. Find contribution, evidence, technical, presentation, paragraph-role, and logic defects. Give findings without changes to the manuscript."
---

# Systems Paper Review

Use the standards of a systems program committee. Make a source-grounded reconstruction of the paper's decision case. Compare its design and evidence with that case.

Start with the scope and unit inventory. Then give the most consequential risks. Give coverage for each section, paragraph, sentence, link, and lexical occurrence in scope. Use the shared coverage contract.

## Invariants

1. Before inspection, record the specified scope. Examine only the pasted passage or named object. Keep adjacent files and dependencies outside scope. Missing support for an in-scope claim can be an `unresolved reviewer risk — needs context`. Missing larger paper context is `not assessable`; it does not create a new author obligation. Record the distinction.
2. Keep reviewed objects and saved objects read-only. Give findings and repair directions. Do not write replacement manuscript prose or change artifacts. For checks that execute commands, obey [review-protocol.md](references/review-protocol.md).
3. Keep manuscript evidence, artifact evidence, external checks, and inference as different classes. Use only facts, citations, results, implementation properties, reviewer opinions, and venue rules with evidence.
4. Give each finding one status: `confirmed defect`, `unresolved reviewer risk`, or `style preference`. Select severity from its consequence for the decision. Give it exactly one next-action class from the shared contract: `direct repair`, `author clarification`, `author evidence`, `external blocker`, or `optional/not applied`.
5. Keep each different finding in scope. Put repeated symptoms under their root cause. Use short entries for local findings with one cause.
6. For prose, record the paragraph role that the text or author gives. Also record the role that the paragraph delivers. Keep any role mismatch as a finding. Examine its one local obligation, ending information gain, sentence links, and paragraph handoffs in scope.

   For each logic finding, record both original endpoints. Show the failed relation. Keep local wording repairs, missing evidence, and changes across paragraphs as different repair types. Repair advice does not give authority to change the manuscript.
7. Use the [shared coverage contract](../systems-paper-revise/references/coverage-contract.md). Before judgment, make the unit inventory. Examine units from the highest assessable level down to lexical occurrences. Then compare the results from bottom to top. Show passed units. Give a completion claim only when the receipt has `Unreviewed: 0`.
8. Before a clean result for any prose paragraph, complete the trigger checkpoint in [review-protocol.md](references/review-protocol.md). A general prose review includes each applicable trigger. These include ending inversion, comparison bridges, interface boundaries, manuscript state, limitations that affect conclusions, and intellectual moves with multiple outcomes. Apply these checks even without a request for that check.
9. Keep each reconstruction source-grounded. Give each central node and causal edge one label: `stated`, `text-licensed`, or `reviewer-hypothesized`. A hypothesized bridge is a missing dependency only when an in-scope claim or promised role requires it. Identify the visible endpoints and that dependent claim. A possible reconstruction alone creates neither evidence nor an author obligation.

## Route by the question

Read only the branches necessary for the requested scope.

Always read the [shared coverage contract](../systems-paper-revise/references/coverage-contract.md). Also read the [shared review and revision contract](../systems-paper-revise/references/review-revise-contract.md).

For prose, read the applicable references that the coverage contract specifies. These include the [systems-writing core](../systems-paper-revise/references/writing-core.md) and the detailed sentence and lexical rules. For prose with multiple sentences, also read the detailed section and paragraph rules.

- For a full adversarial review, findings ledger, or submission gate, read [review-protocol.md](references/review-protocol.md).
- For contribution type or novelty, read the [positive contracts](../systems-paper-revise/references/paper-archetypes.md). Then read [archetype audit](references/paper-archetypes.md) and [research-contribution.md](references/research-contribution.md).
- For the paper's decision case, claim hierarchy, or reader memory, read the [systems-writing core](../systems-paper-revise/references/writing-core.md). Then read [thesis-and-story.md](references/thesis-and-story.md).
- For sections, reader layers, high-level descriptions, or paragraphs, read the [systems-writing core](../systems-paper-revise/references/writing-core.md). Then read [structure-and-sections.md](references/structure-and-sections.md).
- For an overview, architecture, design, algorithm, or mechanism rationale, read [design-derivation.md](references/design-derivation.md). Also read [technical-soundness.md](references/technical-soundness.md).
- For interface boundaries or virtualization boundaries, read the shared [interface-boundary contract](../systems-paper-revise/references/interface-boundaries.md). Use it also for semantic freedom, customization, protection, authority, compound isolation, and direct or delegated execution paths. Then read [design-derivation.md](references/design-derivation.md) and [technical-soundness.md](references/technical-soundness.md).
- For prior-work positioning with artifact evidence, read the [positioning and intellectual-move contract](../systems-paper-revise/references/positioning-and-insight.md). Use it also for conjunctive gaps and paragraphs labeled Observation, Insight, Requirement, or Design objective. Then read [structure-and-sections.md](references/structure-and-sections.md) and [prose-and-terminology.md](references/prose-and-terminology.md).
- For examples, motivating scenarios, the first figures, or headline results, read [examples-figures-results.md](references/examples-figures-results.md). For visual or LaTeX correctness, also read [figures-tables-latex.md](references/figures-tables-latex.md).
- For experiments, baselines, statistics, graphs, or conclusions, read [evaluation.md](references/evaluation.md).
- For code, data, scripts, builds, or reproducibility, read [artifacts-reproducibility.md](references/artifacts-reproducibility.md).
- For English words, terminology, grammar, or precision, read the [systems-writing core](../systems-paper-revise/references/writing-core.md). Then read [prose-and-terminology.md](references/prose-and-terminology.md).
- For Chinese prose or Chinese-to-English logic, read [Chinese calibration](../systems-paper-revise/references/chinese-writing.md). Then read [prose-and-terminology.md](references/prose-and-terminology.md).
- For a specified venue, track, or cycle, read [venue-overlays.md](references/venue-overlays.md). Examine the official source in effect online.
- For rule sources, literature calibration, or external checks, read [source-registry.md](references/source-registry.md).

For a full paper, examine each applicable rule family in different passes. The shared prose references are mandatory. Read [multi-agent-orchestration.md](references/multi-agent-orchestration.md) when reviewers who work independently can remove important coverage gaps.

## Review workflow

1. **Record scope and decision history.** Record the specified objects, source language, and output language. Record manuscript and artifact coverage, venue, cycle, external-check authority, and unavailable context. Use the shared workflow contract to find the authorized decision record. Read all its versions.

   Before prose judgment, find the effective, applicable, and executable decision sets. Make the inventory of stable unit IDs. Record full unit totals, link totals, and the last unit at each applicable level. Keep accessible adjacent objects outside scope.
2. **Examine units from top to bottom.** Start with the highest assessable level. Use this order:

   1. Venue and cycle
   2. Contribution archetype
   3. Paper thesis and evidence
   4. Sections and handoffs
   5. Paragraphs and handoffs
   6. Sentences and links
   7. Lexical occurrences.

   If one insight supposedly causes multiple primary outcomes, make the writing core's source-grounded fan-out map. Examine each edge. Do not use reviewer-hypothesized dependencies as manuscript evidence.

   Use the existing conventions for each paragraph role. Compare the intended and delivered roles. Complete the one-obligation test. Record what information disappears if the ending is removed.

   If higher context is missing, record `not assessable`. Continue through each lower level in scope.
   Complete coverage of a named file does not establish complete paper context. Derive the assessable level from the supplied claims and promises. Do not require a local fragment to select the whole paper's contribution type or complete its decision case.
3. **Use different review lenses.** Apply each lens necessary for the scope. Keep the full unit examination from step 2.

   - Program committee: importance, novelty, venue fit, and contribution coherence.
   - Domain expert: technical validity, assumptions, missing cases, and closest work.
   - Evaluation skeptic: fair comparisons, workloads, measurements, uncertainty, and claim coverage.
   - Systems reader outside the specialty: source-grounded fan-out, paragraph roles, local obligations, ending information gain, definitions, logic, and cognitive load.
   - Artifact consistency, when artifacts are in scope: agreement between paper, code, data, and scripts, plus reproducibility.

   Keep the lenses different. A pass from one lens does not cancel another lens's findings. In multi-agent work, the root owns scope, claim inventory, coverage, repeated findings, conflicts, and verdict. Give each subagent one bounded read-only lens.

   Before the next step, apply each matching protocol trigger to each paragraph with its surface pattern. Do not give `pass` from a correct connective alone. An unknown manuscript lifecycle or unavailable Introduction also does not show `pass`. A missing prior-work antecedent changes status or repair authority. It does not remove the local question.

4. **Do selected external checks.** For claims in scope, use primary or official sources. Examine the specified venue's official rules in effect online. Give the source URL. For command execution, obey [review-protocol.md](references/review-protocol.md). If full isolation or side-effect detection is unavailable, do not execute the command check.
5. **Compare from bottom to top.** Compare lexical judgments with sentence propositions. Compare sentence functions with paragraph roles. Compare paragraph functions with section obligations. Compare sections with the selected paper contract.

   Again, examine terms, assumptions, numbers, claim strength, and evidence state throughout scope. Keep argument organization, scientific or technical evidence, language or presentation, and scope or authority as different dimensions. A missing evidence item cannot cancel a confirmed prose or reasoning defect.
6. **Combine findings and apply the gate.** Put repeated symptoms under their root causes. Keep different locations, claims, and consequences. If scope supplies the paper's decision case, do the [reader-memory test](references/thesis-and-story.md). An abstract or introduction can supply that case.

   For a sentence or paragraph, examine only its local claim, evidence, inference, and boundary. Complete the shared coverage gate and receipt. Examine the attack from missing evidence on significance, novelty, correctness, evaluation validity, clarity, or compliance. Good prose or a clean automated check alone does not show submission readiness.

## Output

For a local sentence or paragraph review, use only the shared coverage contract's compact schema and its two receipts.
That schema replaces the full-review sections below.

For a full review, use the detailed schema in [review-protocol.md](references/review-protocol.md).
Give these items in the user's language:

1. Editorial decision brief: scope and inventory totals, paper archetype, thesis reconstruction, verdict, strengths that help revision, and the most consequential threats. Use one sentence for the thesis reconstruction.
2. Thesis, design, and evidence findings: evidence state, reader-memory failures, competing story choices, and a read-only reconstruction blueprint. Use the highest level that helps revision. If one move supposedly causes multiple primary outcomes, include the source-grounded fan-out ledger. Give each edge its source class: `stated`, `text-licensed`, or `reviewer-hypothesized`.
3. Full coverage ledgers from top to bottom. Include each supplied paragraph. Give its signaled or intended role, delivered role, role convention, one-obligation result, and opening, development, and payoff comparison. Also give ending information gain, sentence roles, neighbor relation, dimension states, controlling state, and finding IDs. Include the section, sentence, link, and lexical rows specified by the shared coverage contract. Show passed units.
4. Full findings ledger for the scope. Give full detail for severe or non-obvious findings. Use short entries for local defects with one cause. Show each finding's diagnostic dimension. Keep argument and organization findings visible beside evidence and technical risks.

   For each logic finding, give citations for both original endpoints. Give short original quotations and the missing or invalid relation. A statement such as “the flow is weak” does not show the defect.
5. Claim-evidence gaps, externally checked facts, coverage limits, and gate result. Include the manuscript coverage receipt with `Unreviewed: 0` or a clear `incomplete` result. Also include the decision coverage receipt. Give `Unaccounted decisions: 0` only when accounting covers all versions.

Select finding detail for the scope. Keep coverage full.

For a local review of one sentence or paragraph, use the shared coverage contract's compact-ledger rule.
Give manuscript and decision receipts after the ledger.

For multiple paragraphs, show one row for each paragraph. Always give original-text locators. Do not include unused paper-wide maps and repeated finding boilerplate. If adjacent paragraphs are unavailable, record cross-paragraph logic as not assessable. Use only endpoint pairs from the source.

For a large paper, continue in numbered batches. Keep the result `incomplete` until all unit ledgers and the final reconciliation are delivered.

Select strengths and weaknesses from the findings. Do not impose a fixed count. Give a strength only when it helps the author keep a correct argument during revision.

A reconstruction blueprint can give the archetype, thesis-support tree, evidence obligations, and reader-obligation outline. Keep it read-only. Do not turn it into replacement manuscript prose.
