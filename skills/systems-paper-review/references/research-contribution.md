# Research Contribution and Positioning

First, read the [systems-writing core](../../systems-paper-revise/references/writing-core.md) and [positive contracts](../../systems-paper-revise/references/paper-archetypes.md). Examine the contribution case: problem, importance, central insight, novelty, lessons, limitations, and venue relevance. For a narrow excerpt, examine only visible claims. Use `needs context` for dependencies on unavailable sections.

## RC-01 — The problem has specified conditions and evidence

- **Nature:** General best practice. A central contribution without an identifiable problem is a scientific defect.
- **Reviewer attack:** “The paper optimizes or builds something without establishing a real systems problem.”
- **Check:** Find the affected actors, setting, unwanted behavior, magnitude, and frequency. Find why existing practice cannot avoid the problem. Do a check of the difference between observed evidence and hypothetical motivation.
- **Severity:** `S1`. Use `S0` if the paper's evidence contradicts the central problem.
- **Exceptions / false positives:** A theoretical or exploratory paper can address a capability or boundary without a deployment problem. It must still give the question's importance.
- **Repair direction:** Give different repair options: evidence in scope, a clear causal chain, or a narrower problem statement. Use only prevalence and impact with evidence.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [SYSTEMS-GUIDE].

## RC-02 — Consequences give the significance evidence

- **Nature:** General best practice.
- **Reviewer attack:** “Even if true, the problem is too narrow or the gain too inconsequential for this venue.”
- **Check:** Find the problem's measurable cost, capability, correctness, security, operational burden, scientific insight, or affected population. If local evidence is missing, record `important`, `critical`, `substantial`, `widespread`, and other terms with almost the same meaning as risks.
- **Severity:** `S1` for a missing significance case. Use `S2` for local overstatement.
- **Exceptions / false positives:** Importance can be qualitative for a categorical consequence, such as isolation failure. The premise must still have evidence.
- **Repair direction:** Give different repair options: available scale or consequence evidence, the boundary's importance, or a narrower claim.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [ERNST].

## RC-03 — The central intellectual contribution is clear

- **Nature:** General best practice and diagnostic heuristic.
- **Reviewer attack:** “I can list components but cannot tell what intellectual idea makes the system work.”
- **Check:** First, use [paper-archetypes.md](paper-archetypes.md) to find the contribution type. Examine mechanism, finding, taxonomy, operational lesson, or another form. Write a causal or inferential reconstruction in one or two sentences. Use this chain: limiting constraint or question → observation or leverage → abstraction or action change, or revised understanding → property, finding, or tradeoff. Do a check of differences between that move, system name, component inventory, work sequence, goal, and result.

  For independent contributions, identify each contribution and its own supported rationale.
- **Severity:** `S1` when a primary intellectual contribution or a claimed shared move has no clear account. Use `S2` for an existing idea that is difficult to find.
- **Exceptions / false positives:** A paper can contribute measurements, experience, negative results, or a dataset. It must still have a clear central intellectual contribution. If the manuscript claims a shared intellectual move, make sure that it gives a unifying principle.
- **Repair direction:** Give the required account of each contribution as a repair direction. Give each primary component its source-grounded relation to that contribution. Recommend removal or lower prominence for optimizations without a role in any claimed contribution.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [JENSEN-SYSTEMS-SKILL], [FIVE-VENUE-CORPUS].

## RC-04 — Contribution type and deliverable are clear

- **Nature:** General best practice.
- **Reviewer attack:** “The paper alternates between claiming a new principle, system, algorithm, study, and engineering implementation.”
- **Check:** Give each contribution its type: problem characterization, insight/theory, algorithm/protocol, system/design, implementation, measurement/experience, artifact/dataset, or evaluation result. Use [thesis-and-story.md](thesis-and-story.md) for the claim hierarchy. Do a check of differences between thesis, supporting claims, enabling mechanisms, implementation facts, and evidence. Compare verbs and evidence with contribution type.
- **Severity:** `S1` when ambiguity exaggerates novelty or changes the required evaluation. For other cases, `S2`.
- **Exceptions / false positives:** Multiple contribution types are permitted. Their hierarchy and evidence must be clear.
- **Repair direction:** Recommend contribution statements with deliverables and validated claims. Recommend different primary and enabling contributions.
- **Sources:** [OSDI-CFP], [LEVIN-REDELL], [SYSTEMS-GUIDE].

## RC-05 — Novelty is relative to the closest alternatives

- **Nature:** General best practice. Factual novelty claims must have evidence.
- **Reviewer attack:** “The claimed novelty disappears when compared with the closest prior system or technique.”
- **Check:** Find the closest works by problem, mechanism, and assumptions. Citation frequency alone is insufficient. For each novelty claim, record the specified difference. If external research is authorized, examine the cited sources.
- **Severity:** `S0` for a demonstrably false central “first” claim. Use `S1` for missing or weak differentiation. Use `S2` for incomplete local positioning.
- **Exceptions / false positives:** For an introduction without related work in scope, missing comparisons can be `needs context`. Absolute novelty claims stay assessable.
- **Repair direction:** Give different repair options: an accurate capability, assumption, or mechanism difference, the closest citation, or a narrower claim.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [SYSTEMS-GUIDE].

## RC-06 — “First,” “only,” and superlatives survive an open-world test

- **Nature:** Condition for evidence.
- **Reviewer attack:** “The authors cannot justify an exhaustive claim over all prior work or deployments.”
- **Check:** Find `first`, `only`, `never`, `all`, `best`, `state of the art`, and Chinese equivalents. Give questions about population, cutoff date, search completeness, and metric or setup comparability.
- **Severity:** `S1`. Use `S0` for a central claim that external evidence disproves.
- **Exceptions / false positives:** A bounded claim such as “among the evaluated open-source systems under workload W” can be supported.
- **Repair direction:** Recommend clear population, date, metric, and conditions. Use “to our knowledge” only with a search with documented coverage. This phrase alone supplies no evidence.
- **Sources:** [ERNST], [LEVIN-REDELL], [BRANDON-EVIDENCE].

## RC-07 — The advance is nontrivial with its assumptions

- **Nature:** General best practice.
- **Reviewer attack:** “The result follows from an obvious engineering substitution, relaxed requirement, stronger oracle, or shifted cost.”
- **Check:** Write a reconstruction of the naive or strawman solution. Find its failure and the new constraint or insight. Examine costs outside the measured boundary. Include overhead, training, annotation, preprocessing, hardware, and operator work.
- **Severity:** `S1`. Use `S0` when an undisclosed relaxation of the problem controls all the advance.
- **Exceptions / false positives:** Careful engineering can give a surprising capability, reusable lesson, or implementation with strong evidence. Algorithmic novelty is not a universal requirement.
- **Repair direction:** Recommend clear constraints and design reasoning. Recommend measurements for transferred costs. Compare the contribution type with the advance in the paper.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [SYSTEMS-GUIDE].

## RC-08 — Components form a coherent co-design

- **Nature:** General best practice.
- **Reviewer attack:** “The system is a bag of optimizations with no necessity, interaction, or transferable idea.”
- **Check:** Use [design-derivation.md](design-derivation.md). For each primary component, find its problem-derived requirement, alternative failures, mechanism interactions, and resultant property or tradeoff. Record the contribution that stays without that component.
- **Severity:** `S1` when coherence is central to novelty. For other cases, `S2`.
- **Exceptions / false positives:** Independent techniques are permitted when the paper gives them different contribution claims and evaluations.
- **Repair direction:** Give different repair options: clear dependencies and co-design logic, lower prominence for incidental optimizations, or different claims.
- **Sources:** [USER-NOTES], [LEVIN-REDELL], [JENSEN-SYSTEMS-SKILL].

## RC-09 — Claims give different statuses for idea, prototype, implementation, and deployment

- **Nature:** Condition for accuracy.
- **Reviewer attack:** “The paper presents a prototype or simulation as a complete, practical, or deployed system.”
- **Check:** Find verbs such as `design`, `implement`, `integrate`, `deploy`, `support`, `validate`, and `demonstrate`. Compare maturity claims with implementation and evaluation evidence.
- **Severity:** `S0` for misrepresentation that changes conclusions. Use `S1` for a maturity mismatch that stays unresolved.
- **Exceptions / false positives:** Evaluation can use a model, simulator, trace-driven prototype, or partial implementation. Its type and conclusion boundaries must be clear.
- **Repair direction:** Recommend clear implementation boundaries, unavailable components, environment, and prototype conclusion limits.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [NSDI-ARTIFACT].

## RC-10 — The contribution gives lessons beyond one implementation

- **Nature:** General best practice. Its strength depends on paper type.
- **Reviewer attack:** “The implementation works, but the paper teaches no reusable principle, tradeoff, boundary, or surprising empirical fact.”
- **Check:** Find mechanisms, design principles, negative results, boundaries, or measured relations that help another system. Make sure that evidence gives the lesson. Do not use speculation as evidence for the lesson.
- **Severity:** `S1` for venues or papers with general insight as the central contribution. Use `S2` for experience or artifact papers that are strong in other respects.
- **Exceptions / false positives:** A unique infrastructure, dataset, or operational experience can have significance without a new algorithm.
- **Repair direction:** Recommend evidence-based design lessons and conditions. Keep generalization within the evidence from the available instances.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP].

## RC-11 — Scope conditions and limitations are visible

- **Nature:** Condition for accuracy at claim boundaries. General best practice for presentation.
- **Reviewer attack:** “The contribution is stated universally, while the mechanism only applies under hidden workload, hardware, trust, topology, or failure assumptions.”
- **Check:** Compare quantifiers and headline claims with the system model and evaluation domain. Find omitted unsupported cases and contradictory caveats.
- **Severity:** `S0` when a hidden condition invalidates the central conclusion. For other cases, `S1` or `S2`.
- **Exceptions / false positives:** Discussion of some theoretical corner cases is not necessary. Conditions that affect correctness, adoption, or headline results must have discussion.
- **Repair direction:** Recommend the boundary beside the claim and evidence for its realism. Recommend necessary sensitivity tests. Keep limitations visible.
- **Sources:** [OSDI-CFP], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL].

## RC-12 — Venue and audience fit are argued, not assumed

- **Nature:** Venue-specific requirement and general best practice.
- **Reviewer attack:** “The work may be competent, but its central question and contribution do not advance this venue's systems community.”
- **Check:** Compare the contribution with the venue and track's official scope and criteria in effect. Examine the systems consequence for readers outside the subfield.
- **Severity:** `S0` for a submission clearly outside the verified scope. Use `S1` for a weak audience case.
- **Exceptions / false positives:** Interdisciplinary papers can fit through a systems contribution. The application domain can be external.
- **Repair direction:** Give different repair options: the systems advance in the paper or a more applicable venue. Keep claims accurate.
- **Sources:** [OSDI-CFP], [SOSP-CFP], [NSDI-CFP], [EUROSYS-CFP], [ASPLOS-CFP]. Current online checks are required.

## RC-13 — Contribution statements are promises the paper fulfills

- **Nature:** Condition for internal consistency.
- **Reviewer attack:** “The introduction promises properties or evaluations that later sections do not deliver.”
- **Check:** Make a contribution-to-section-to-evidence map. Find unfulfilled promises, unadvertised central contributions, and conclusions stronger than the introduction or evidence.
- **Severity:** `S1` for a central unfulfilled promise. Use `S2` for map or wording mismatch.
- **Exceptions / false positives:** An introduction review can examine promise testability. Without subsequent sections, fulfillment stays `needs context`.
- **Repair direction:** Give different repair options: evidence, a claim equal to the deliverable, or removal or lower prominence for the promise.
- **Sources:** [SYSTEMS-GUIDE], [JENSEN-SYSTEMS-SKILL], [ERNST].

## RC-14 — Related-work groups give reasoning evidence

- **Nature:** General best practice.
- **Reviewer attack:** “The paper enumerates citations but never explains the technical gap or why prior approaches cannot solve the stated problem.”
- **Check:** Examine prior-work groups by mechanism, assumption, or limitation. Make sure that each group has a relation to the design choice. Examine comparison accuracy and fairness.
- **Severity:** `S1` when novelty depends on a missing or incorrect comparison. Use `S2` for a list without reasoning.
- **Exceptions / false positives:** A short passage can name only the categories. Detailed evidence can occur elsewhere.
- **Repair direction:** Recommend organization by dimensions related to the decision. Recommend accurate differences. Keep fairness in comparisons.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [ERNST].

## Completion questions

Before completion of this family, give answers to these questions:

1. Can a reviewer pass the reader-memory test in [thesis-and-story.md](thesis-and-story.md) without guessing or listing components?
2. Is the closest-work difference accurate and in agreement with external evidence where checked?
3. Do assumptions or shifted costs erase the advance?
4. Does each contribution promise have evidence or a clear limitation?
5. Which `RC` rules are not assessable within scope?
