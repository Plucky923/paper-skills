# Research Contribution and Positioning

Apply these rules to the contribution case: problem, importance, central insight, novelty, lessons, limitations, and venue relevance. For a narrow excerpt, assess only locally visible claims and mark dependencies on unseen sections as `needs context`.

## RC-01 — The problem is concrete and real

- **Nature:** General best practice; a central contribution with no identifiable problem is a scientific defect.
- **Reviewer attack:** “The paper optimizes or builds something without establishing a real systems problem.”
- **Check:** Identify affected actors, operating setting, undesirable behavior, magnitude/frequency, and why existing practice cannot simply avoid it. Separate observed problem evidence from hypothetical motivation.
- **Severity:** `S1`; `S0` if the central problem is contradicted by the paper's own evidence.
- **Exceptions / false positives:** A theoretical or exploratory systems paper may motivate a capability or boundary rather than a deployed pain point, but must still state why that question matters.
- **Repair direction:** Supply in-scope evidence, make the causal chain explicit, or narrow the problem statement. Do not invent prevalence or impact.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [SYSTEMS-GUIDE]. Checked 2026-09-01.

## RC-02 — Significance follows from consequences, not adjectives

- **Nature:** General best practice.
- **Reviewer attack:** “Even if true, the problem is too narrow or the gain too inconsequential for this venue.”
- **Check:** Trace the problem to measurable cost, capability, correctness, security, operational burden, scientific insight, or affected population. Flag `important`, `critical`, `substantial`, `widespread`, and similar terms when no local evidence gives them content.
- **Severity:** `S1` for a missing significance case; `S2` for local overstatement.
- **Exceptions / false positives:** Importance can be qualitative when the consequence is inherently categorical, such as violating isolation; the premise still needs support.
- **Repair direction:** Add already available scale/consequence evidence, explain why the boundary matters, or qualify the claim.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [ERNST]. Checked 2026-09-01.

## RC-03 — The paper states one intelligible, principle-level central idea

- **Nature:** General best practice and diagnostic heuristic.
- **Reviewer attack:** “I can list components but cannot tell what intellectual idea makes the system work.”
- **Check:** First use [paper-archetypes.md](paper-archetypes.md) to identify whether the intellectual contribution is a mechanism, finding, taxonomy, operational lesson, or other form. Then attempt a one- or two-sentence reconstruction of its causal or inferential move: binding constraint/question → observation/leverage → changed abstraction/action or revised understanding → resulting property/finding/tradeoff. Distinguish it from the system name, component inventory, step sequence, goal, and result.
- **Severity:** `S1` if the contribution appears to be an unprincipled bundle; `S2` if the idea exists but is hard to recover.
- **Exceptions / false positives:** Some papers contribute a measurement result, experience report, negative result, or dataset rather than a new algorithm; the central intellectual contribution must still be explicit.
- **Repair direction:** State the unifying principle before its realization, connect each major component to it, and remove or demote unrelated optimizations.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [JENSEN-SYSTEMS-SKILL], [OSDI-SOSP-CORPUS]. Checked 2026-09-03.

## RC-04 — Contribution type and deliverable are explicit

- **Nature:** General best practice.
- **Reviewer attack:** “The paper alternates between claiming a new principle, system, algorithm, study, and engineering implementation.”
- **Check:** Classify each claimed contribution: problem characterization, insight/theory, algorithm/protocol, system/design, implementation, measurement/experience, artifact/dataset, or evaluation result. Use [thesis-and-story.md](thesis-and-story.md) to distinguish the controlling thesis, decision-relevant supporting claims, enabling mechanisms, implementation facts, and evidence. Verify verbs and evidence match the type.
- **Severity:** `S1` when ambiguity inflates novelty or misdirects evaluation; otherwise `S2`.
- **Exceptions / false positives:** A paper may make several types of contribution, but their hierarchy and evidence must be clear.
- **Repair direction:** Rewrite contribution statements around deliverables and validated claims; separate primary from enabling contributions.
- **Sources:** [OSDI-CFP], [LEVIN-REDELL], [SYSTEMS-GUIDE]. Checked 2026-09-01.

## RC-05 — Novelty is relative to the closest alternatives

- **Nature:** General best practice; factual novelty claims require evidence.
- **Reviewer attack:** “The claimed novelty disappears when compared with the closest prior system or technique.”
- **Check:** Identify the closest works by problem, mechanism, and assumptions—not merely the most cited field categories. For each novelty claim, state the exact delta and verify cited sources when external research is allowed.
- **Severity:** `S0` if a central “first” claim is demonstrably false; `S1` for missing or weak differentiation; `S2` for incomplete local positioning.
- **Exceptions / false positives:** In a scoped introduction without related work, missing detailed comparison may be `needs context`; an absolute novelty claim inside it remains reviewable.
- **Repair direction:** Replace broad novelty language with a precise capability/assumption/mechanism delta, cite the closest source, or narrow the claim.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [SYSTEMS-GUIDE]. Checked 2026-09-01.

## RC-06 — “First,” “only,” and superlatives survive an open-world test

- **Nature:** Hard evidentiary condition.
- **Reviewer attack:** “The authors cannot justify an exhaustive claim over all prior work or deployments.”
- **Check:** Flag `first`, `only`, `never`, `all`, `best`, `state of the art`, and Chinese equivalents. Ask what population and cutoff date are quantified, how the search supports exhaustiveness, and whether the metric/setup makes a superlative comparable.
- **Severity:** `S1`; `S0` if externally disproved and central.
- **Exceptions / false positives:** A bounded claim such as “among the evaluated open-source systems under workload W” may be supported.
- **Repair direction:** Bound the population, date, metric, and conditions; change to “to our knowledge” only if a credible search was performed—this phrase does not itself supply evidence.
- **Sources:** [ERNST], [LEVIN-REDELL], [BRANDON-EVIDENCE]. Checked 2026-09-01.

## RC-07 — The advance is nontrivial under its assumptions

- **Nature:** General best practice.
- **Reviewer attack:** “The result follows from an obvious engineering substitution, relaxed requirement, stronger oracle, or shifted cost.”
- **Check:** Reconstruct the naive/strawman solution. Identify why it fails, the new constraint or insight, and whether the proposed mechanism merely moves overhead, training, annotation, preprocessing, hardware, or operator work outside the measured boundary.
- **Severity:** `S1`; `S0` when the claimed advance depends entirely on an undisclosed relaxed problem.
- **Exceptions / false positives:** Careful engineering can be a valuable systems contribution when it yields a surprising capability, reusable lesson, or compelling real implementation; do not demand algorithmic novelty universally.
- **Repair direction:** Make the hard constraint and design reasoning explicit; measure shifted costs; calibrate the contribution type.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [SYSTEMS-GUIDE]. Checked 2026-09-01.

## RC-08 — Components form a coherent co-design

- **Nature:** General best practice.
- **Reviewer attack:** “The system is a bag of optimizations with no necessity, interaction, or transferable idea.”
- **Check:** Apply [design-derivation.md](design-derivation.md): for every major component, identify the problem-derived requirement it discharges, why existing/simple alternatives fail, how it interacts with other mechanisms, which property/tradeoff follows, and what contribution remains if it is removed.
- **Severity:** `S1` if coherence is central to novelty; otherwise `S2`.
- **Exceptions / false positives:** Independent techniques are acceptable if the paper explicitly frames and evaluates them as separate contributions.
- **Repair direction:** Expose dependencies and co-design logic, demote incidental optimizations, or separate claims.
- **Sources:** [USER-NOTES], [LEVIN-REDELL], [JENSEN-SYSTEMS-SKILL]. Checked 2026-09-01.

## RC-09 — Claims distinguish idea, prototype, implementation, and deployment

- **Nature:** Hard accuracy condition.
- **Reviewer attack:** “The paper presents a prototype or simulation as a complete, practical, or deployed system.”
- **Check:** Track verbs such as `design`, `implement`, `integrate`, `deploy`, `support`, `validate`, and `demonstrate`. Compare the claimed maturity with visible implementation and evaluation evidence.
- **Severity:** `S0` for material misrepresentation; `S1` for unresolved maturity mismatch.
- **Exceptions / false positives:** A paper may legitimately evaluate a model, simulator, trace-driven prototype, or partial implementation if clearly labeled and conclusions are bounded.
- **Repair direction:** State implementation boundary, unsupported components, environment, and what conclusions the prototype can establish.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [NSDI-ARTIFACT]. Checked 2026-09-01.

## RC-10 — The contribution yields lessons beyond one implementation

- **Nature:** General best practice; strength depends on paper type.
- **Reviewer attack:** “The implementation works, but the paper teaches no reusable principle, tradeoff, boundary, or surprising empirical fact.”
- **Check:** Look for mechanisms, design principles, negative results, boundary conditions, or measured relationships that could inform another system. Verify the lesson is supported rather than added as speculation.
- **Severity:** `S1` for venues/papers centered on general insight; `S2` for otherwise strong experience or artifact papers.
- **Exceptions / false positives:** A uniquely valuable infrastructure, dataset, or operational experience can be significant without a new algorithm.
- **Repair direction:** Extract supported design lessons and conditions; do not claim universal generality from a single instance.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP]. Checked 2026-09-01.

## RC-11 — Scope conditions and limitations are visible

- **Nature:** Hard accuracy condition for claim bounds; general best practice for presentation.
- **Reviewer attack:** “The contribution is stated universally, while the mechanism only applies under hidden workload, hardware, trust, topology, or failure assumptions.”
- **Check:** Compare quantifiers and headline claims with system model and evaluation domain. Search for omitted unsupported cases and contradictory caveats.
- **Severity:** `S0` when a hidden condition invalidates the central conclusion; otherwise `S1` or `S2`.
- **Exceptions / false positives:** Not every theoretical corner case needs space. Conditions material to correctness, adoption, or headline results do.
- **Repair direction:** State the boundary near the claim, justify its realism, test sensitivity where needed, and include limitations without burying them.
- **Sources:** [OSDI-CFP], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL]. Checked 2026-09-01.

## RC-12 — Venue and audience fit are argued, not assumed

- **Nature:** Venue-specific requirement plus general best practice.
- **Reviewer attack:** “The work may be competent, but its central question and contribution do not advance this venue's systems community.”
- **Check:** Map the contribution to the current official scope and evaluation criteria of the named venue and track. Check whether the paper explains the systems consequence for readers outside the narrow subfield.
- **Severity:** `S0` for clear verified out-of-scope submission; `S1` for weak audience case.
- **Exceptions / false positives:** Interdisciplinary papers can fit through a systems contribution even when the application domain is external.
- **Repair direction:** Reframe around the actual systems advance or choose a more suitable venue; never distort the work to mimic a call.
- **Sources:** [OSDI-CFP], [SOSP-CFP], [NSDI-CFP], [EUROSYS-CFP], [ASPLOS-CFP]. Live verification required.

## RC-13 — Contribution statements are promises the paper fulfills

- **Nature:** Hard internal-consistency condition.
- **Reviewer attack:** “The introduction promises properties or evaluations that later sections do not deliver.”
- **Check:** Build a contribution-to-section-to-evidence map. Look for unmatched promises, unadvertised central contributions, and conclusion claims stronger than the introduction or evidence.
- **Severity:** `S1` for a central broken promise; `S2` for mapping/wording mismatch.
- **Exceptions / false positives:** A scoped introduction review can assess whether promises are testable but cannot confirm fulfillment without later sections; mark `needs context`.
- **Repair direction:** Supply evidence, align the claim with what is delivered, or remove/demote the promise.
- **Sources:** [SYSTEMS-GUIDE], [JENSEN-SYSTEMS-SKILL], [ERNST]. Checked 2026-09-01.

## RC-14 — Related-work grouping supports reasoning

- **Nature:** General best practice.
- **Reviewer attack:** “The paper enumerates citations but never explains the technical gap or why prior approaches cannot solve the stated problem.”
- **Check:** Verify works are grouped by relevant mechanism, assumption, or limitation; each group connects to the paper's design choice; comparisons are accurate and charitable.
- **Severity:** `S1` when novelty depends on a missing/incorrect comparison; `S2` for list-like exposition.
- **Exceptions / false positives:** A short scoped passage may only signpost categories; detailed support may appear elsewhere.
- **Repair direction:** Reorganize around decision-relevant dimensions and state precise deltas; avoid strawman descriptions.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [ERNST]. Checked 2026-09-01.

## Completion questions

Before closing this family, answer:

1. Can a reviewer pass the reader-memory test in [thesis-and-story.md](thesis-and-story.md) without guessing or listing components?
2. Is the closest-work delta precise and externally defensible where checked?
3. Do assumptions or shifted costs erase the advance?
4. Does every contribution promise map to evidence or an explicit limitation?
5. Which `RC` rules were not assessable under scope?
