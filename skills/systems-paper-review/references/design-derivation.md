# Design Derivation and Mechanism Necessity

Use this reference for an overview, design, algorithm, architecture, implementation rationale, or introduction with technical challenges. It connects scientific reasoning with the soundness checks in [technical-soundness.md](technical-soundness.md).

## Required derivation chain

For each primary mechanism, make a reconstruction of this chain:

`observed failure or desired property → binding constraint → design requirement → mechanism → invariant/effect and tradeoff → decisive test`

This chain is an audit aid, not a prose template. It checks the mechanism's scientific motivation, technical sufficiency, and empirical testability.

## DD-01 — Evidence shows the limiting constraint

- **Check:** Do a check of the difference between symptoms and limiting constraints. Find evidence from measurements, counterexamples, model properties, theorems, prior-work limitations, or operations.
- **Reviewer attack:** “The design solves an asserted root cause that the paper never establishes.”
- **Severity:** `S1`. Use `S0` when evidence contradicts a constraint on which the design depends.

## DD-02 — The problem gives the requirements

- **Check:** For each goal, challenge, or desired property, find the earlier problem or constraint that makes it necessary. Do a check of differences between necessary requirements, preferences, and implementation conveniences.
- **Reviewer attack:** “The requirements are chosen to fit the proposed system rather than derived from the problem.”
- **Severity:** `S1` for central circular reasoning. For other cases, `S2`.
- **Exception:** For standard requirements common to the field, citations or brief rationale can be sufficient.

## DD-03 — Each mechanism satisfies a requirement

- **Check:** Connect each primary component or algorithm step to its requirement. Include interactions with other mechanisms. Find components without requirements, repeated mechanisms, and requirements without implementation paths.
- **Reviewer attack:** “This is a component inventory, not a design argument.”
- **Severity:** `S1` for a missing central link. For other cases, `S2`.

## DD-03A — A shared insight has source-grounded causal fan-out

- **Check:** If one intellectual move supposedly causes multiple primary properties, use the [canonical fan-out test](../../systems-paper-revise/references/writing-core.md#source-grounded-intellectual-move-fan-out). Give source anchors for the shared move and each move-to-property edge. Give each one a label: `stated`, `text-licensed`, or `reviewer-hypothesized`. Keep a reviewer-hypothesized bridge as a missing dependency, even if its reconstruction is clear.
- **Reviewer attack:** “These benefits share a system name, but the paper never shows that one conceptual change causes all of them.”
- **Severity:** `S1` when the unified claim controls the contribution. Use `S2` when different supporting claims would give an accurate account.
- **Exception:** An artificial common cause is not necessary for contributions with different manuscript descriptions and evaluations.

## DD-03B — Each property has its narrowest sufficient layer

- **Check:** Keep these layers different: enabling substrate, abstraction or authority boundary, runtime enforcement and lifecycle, execution path, and empirical conditions. For each property, record each layer's contribution. Record its dependencies on other layers. Use the canonical fan-out counterfactual to find attribution without a causal relation.
- **Reviewer attack:** “The paper credits the language, interface, or shared runtime with a compound guarantee that actually depends on unmentioned checks, completeness, lifecycle behavior, or workload conditions.”
- **Severity:** `S0` for a false central guarantee. Use `S1` for a missing central attribution path. For other cases, `S2`.

## DD-03C — Interface, authority, and path are different axes

- **Check:** For interface or boundary contributions, use the [interface-boundary contract](../../systems-paper-revise/references/interface-boundaries.md). Make the three-axis ledger for semantic commitments, protection or authority, and execution path. For customization or independent implementation claims, add the actor/artifact/stage/control tuple. For each property across axes, get a causal edge with a source anchor. Use `not claimed` for an axis without a claim. Do not invent an omission.
- **Reviewer attack:** “The paper treats a low-level API, protection boundary, or shorter path as if it automatically proved customization, isolation, or end-to-end performance.”
- **Severity:** `S0` for a false central guarantee. Use `S1` for a central edge without evidence. For other cases, `S2`.

## DD-04 — The mechanism causes the stated property

- **Check:** Record the input or state, action or abstraction change, enforcement point, and resultant property. Record the assumptions. Select the result type: guaranteed, detected, enabled, or only observed.
- **Reviewer attack:** “The prose says the mechanism ‘ensures’ the property without explaining the causal or enforcement path.”
- **Severity:** `S0` for a false central guarantee. Use `S1` for a missing central explanation.

## DD-05 — The derivation includes tradeoffs and transferred costs

- **Check:** Record each lost property and transferred cost. Include generality, latency, throughput, memory, hardware, offline work, operator effort, recovery, trust, compatibility, and implementation complexity. Make sure that the thesis stays meaningful with these costs.
- **Reviewer attack:** “The apparent benefit comes from relaxing the problem or moving cost outside the measured boundary.”
- **Severity:** `S0` for an undisclosed fatal cost. For other cases, `S1`/`S2`.

## DD-06 — Alternatives show necessity as well as advantage

- **Check:** For the same assumptions, compare the mechanism with the alternative that has the least complexity. Make sure that the alternative has evidence for its applicability. Find the requirement that this alternative cannot satisfy. Examine whether the proposed mechanism gives the smallest necessary conceptual change. An ablation can show a performance contribution. It does not necessarily show design necessity.
- **Reviewer attack:** “A simpler mechanism appears to provide the same property under the paper's assumptions.”
- **Severity:** `S1`. Use `S2` for incomplete local rationale.

## DD-07 — Evaluation completes the derivation chain

- **Check:** For each central requirement and property, find the decisive proof, experiment, negative case, sensitivity test, or field observation. End-to-end results show total effect. If the paper claims a particular cause, get attribution evidence or controlled analysis.
- **Reviewer attack:** “The mechanism is plausible, but the evidence never tests the reason it was introduced.”
- **Severity:** `S0`/`S1`, as determined by claim centrality.

## Knowledge-state rule

Technical details can occur before principles. A low-level fact before the principles can show a constraint or a counterexample with specified conditions. It can also give the target-property definition.

Record a detail defect only if the reader cannot know its relevance or if it replaces the governing relation.

## Derivation map

| Failure/property | Supporting evidence | Constraint | Requirement | Mechanism | Property/invariant | Tradeoff | Decisive test | Gap |
|---|---|---|---|---|---|---|---|---|

For systems with multiple mechanisms, examine both directions. Make sure that each requirement has a satisfying mechanism. Make sure that each primary mechanism has a requirement. For each shared move, get source anchors for its edge to each advertised outcome.

Do not use implementation effort, co-location, or reviewer reconstruction as evidence for conceptual necessity.

## Sources

This model uses [LEVIN-REDELL] and [SYSTEMS-GUIDE]. It also uses the system and evidence criteria in [OSDI-CFP] and [SOSP-CFP]. Recurring constraint-to-mechanism structures in [FIVE-VENUE-CORPUS] give further evidence.
