# Technical Soundness and System Design

Make a system reconstruction sufficient for implementation, operation, or attack. A fluent overview does not show mechanism completeness.

Use only technical material in scope. Missing details in a short excerpt are usually unresolved risks. They do not show omissions from the full paper.
## TS-01 — System model names actors, resources, and boundaries

- **Nature:** Condition for correctness reasoning. Presentation detail depends on paper type.
- **Reviewer attack:** “I cannot determine what the system controls, observes, trusts, or protects.”
- **Check:** Find actors, components, resources, inputs, outputs, state, administrative domains, trust boundaries, and external dependencies. If prose has ambiguity, draw an internal model.
- **Severity:** `S1`. Use `S0` when the central guarantee has no meaning without the missing boundary.
- **Exceptions / false positives:** A conventional model can be short. Unusual differences and boundaries related to security must be clear.
- **Repair direction:** Give clear entities, authority, state, interfaces, and excluded responsibilities. Make sure that the overview, figure, and mechanism agree.
- **Sources:** [SYSTEMS-GUIDE], [LEVIN-REDELL], [OSDI-CFP].

## TS-02 — Assumptions are clear, necessary, and plausible

- **Nature:** Condition for accuracy.
- **Reviewer attack:** “The method works only because it assumes an oracle, cooperative workload, ideal hardware, trusted component, synchronized clock, or failure-free environment.”
- **Check:** List stated and implied assumptions. For each, give questions about its owner, checks, failure behavior, and the equivalent privilege for alternatives.
- **Severity:** `S0` when a hidden or false assumption invalidates the central claim. For other cases, `S1`.
- **Exceptions / false positives:** Strong assumptions are permitted with boundaries, motivation, and corresponding claim limits.
- **Repair direction:** Give repair options: clear assumptions and rationale, validation or fallback, or a narrower claim.
- **Sources:** [LEVIN-REDELL], [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE].

## TS-03 — Threat, fault, and workload models match claims

- **Nature:** Condition for correctness.
- **Reviewer attack:** “The claimed security/reliability/performance property is evaluated under a weaker adversary, fault set, or workload than the wording implies.”
- **Check:** List adversary capabilities, fault types, timing, workload distribution, excluded cases, and recovery goals. Compare each property's unchanged words with that model.
- **Severity:** `S0` for a central mismatch. For other cases, `S1`.
- **Exceptions / false positives:** Invented threat models are not necessary for papers without security claims. Related fault and workload boundaries still apply.
- **Repair direction:** Make sure that the model and quantifiers agree. Give rationale for exclusions. Add evidence or a weaker property.
- **Sources:** [OSDI-CFP], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL].

## TS-04 — Each primary mechanism has a causal role

- **Nature:** General best practice and condition for technical completeness.
- **Reviewer attack:** “The paper names modules but never shows how they produce the claimed property.”
- **Check:** For each component, examine input → state/operation → output → downstream effect → claim. Find unexplained transformations and results without reasoning.
- **Severity:** `S1` for central mechanism gaps. Use `S2` for secondary components.
- **Exceptions / false positives:** A summary can be sufficient for conventional implementation components outside the claim.
- **Repair direction:** Add operational detail. Give the causal link. Remove decorative components from the contribution story.
- **Sources:** [SYSTEMS-GUIDE], [LEVIN-REDELL].

## TS-05 — Inputs, outputs, state, and lifecycle have all necessary details

- **Nature:** General best practice. It is a correctness condition when lifecycle affects correctness.
- **Reviewer attack:** “The algorithm is understandable only in steady state; initialization, termination, updates, cleanup, or reconfiguration are unspecified.”
- **Check:** Give questions about phase starts and stops, preconditions, persistent state, transient state, update triggers, idempotence, cleanup, and restart behavior.
- **Severity:** `S1` when missing lifecycle details can break the property. For other cases, `S2`.
- **Exceptions / false positives:** Usual setup can stay abstract. State transitions that change outcomes must have a clear account.
- **Repair direction:** Give phase transitions, conditions, and state ownership. If this removes ambiguity, add pseudocode or a state machine.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [ERNST].

## TS-06 — Invariants and guarantees have an enforcement story

- **Nature:** Condition for correctness.
- **Reviewer attack:** “The paper asserts that property P always holds but provides no invariant, proof, validation point, or enforcement mechanism.”
- **Check:** Convert `ensure`, `guarantee`, `prevent`, `always`, `safe`, `correct`, and equivalent words into an accurate property. Find the enforcement point and all state-changing paths.
- **Severity:** `S0` for a central guarantee without evidence. For other cases, `S1`.
- **Exceptions / false positives:** Empirical reliability claims can be probabilistic. Their language and evidence must show that status.
- **Repair direction:** Give the invariant and its rationale. Do tests of all paths. Replace guarantees with observed behavior or narrower domains where necessary.
- **Sources:** [OSDI-CFP], [LEVIN-REDELL], [BRANDON-EVIDENCE].

## TS-07 — Concurrency, ordering, and time are specified where related

- **Nature:** Condition for concurrent or distributed mechanisms.
- **Reviewer attack:** “The design assumes an execution order that concurrent nodes, threads, interrupts, or failures do not preserve.”
- **Check:** Examine races, atomicity, synchronization, memory visibility, event sequence, clock assumptions, duplicates, reordering, and simultaneous updates.
- **Severity:** `S0` for a correctness counterexample. Use `S1` for a primary unresolved gap.
- **Exceptions / false positives:** For sequential or offline components, this rule can be not applicable.
- **Repair direction:** Give the ordering model and synchronization. Give clear race handling or exclusions. Add proof or test evidence.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP].

## TS-08 — Failure detection, containment, and recovery are coherent

- **Nature:** Condition for reliability or availability claims. Other applications depend on context.
- **Reviewer attack:** “A partial failure leaves corrupt, leaked, duplicated, or unrecoverable state, or the recovery path assumes knowledge it cannot have.”
- **Check:** Examine applicable crashes, timeouts, partitions, resource exhaustion, bad inputs, partial writes, restarts, and cascading failures. Record detection, rollback or retry, persistence, and the restored invariant.
- **Severity:** `S0` for central correctness failure or data loss. Use `S1` for primary availability risk. Use `S2` for an unclaimed operational gap.
- **Exceptions / false positives:** Failure behavior outside the model can be a limitation if the exclusion is realistic and visible.
- **Repair direction:** Give repair options: failure paths and state reconciliation, exclusion rationale, or narrower reliability claims.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [OSDI-CFP].

## TS-09 — Edge cases and degenerate inputs do not defeat the method

- **Nature:** Condition when a counterexample violates a claim. For other cases, a diagnostic aid.
- **Reviewer attack:** “The mechanism only works on typical cases and silently fails at empty, maximal, skewed, adversarial, or rapidly changing inputs.”
- **Check:** Do applicable tests for boundary sizes, zero or one item, equal or different data, skew, churn, and overload. Include malformed inputs, cold starts, and conflicting objectives.
- **Severity:** `S0` for a correct central counterexample. Use `S1`/`S2` for unresolved coverage.
- **Exceptions / false positives:** Select cases from the mechanism and claim domain. Do not include irrelevant combinations.
- **Repair direction:** Give handling, detection, or exclusion for the case. Do a boundary test.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [LEVIN-REDELL].

## TS-10 — Design choices are compared with alternatives with evidence for their applicability

- **Nature:** General best practice.
- **Reviewer attack:** “The chosen mechanism is arbitrary; a simpler or established alternative may offer the same result.”
- **Check:** For each primary choice, find objectives, constraints, alternatives with evidence for their applicability, tradeoffs, rejected strawmen, and evidence. Find alternatives with unfair configurations or false descriptions.
- **Severity:** `S1` when novelty or necessity depends on the choice. For other cases, `S2`.
- **Exceptions / false positives:** Full defense of usual implementation choices is not necessary. Examine choices that affect claims, cost, correctness, or generality.
- **Repair direction:** Give decision criteria. Give fair comparisons through reasoning, evidence, or focused evaluation.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [JENSEN-SYSTEMS-SKILL].

## TS-11 — Costs are accounted at the same boundary as benefits

- **Nature:** Condition for fair cost or performance claims.
- **Reviewer attack:** “The system looks efficient only because preprocessing, training, indexing, migration, failures, operator time, hardware, or storage are outside the accounting boundary.”
- **Check:** List one-time costs, repeated costs, resource transfers, client/server division, offline/online division, and amortization assumptions. Compare baseline boundaries with the system boundary.
- **Severity:** `S0` for deceptive accounting that changes conclusions. For other cases, `S1`.
- **Exceptions / false positives:** A one-time cost can be outside a recurring-cost total with clear amortization, lifetime rationale, and different cost reporting.
- **Repair direction:** Give full costs and breakdowns. Give amortization rationale. Put necessary limits on claims.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL].

## TS-12 — Scalability reasoning identifies the limiting resource

- **Nature:** General best practice. It is a condition for broad scalability claims.
- **Reviewer attack:** “The evaluation stops before the design bottleneck, and no complexity or resource argument supports extrapolation.”
- **Check:** Find scaling terms for computation, memory, storage, bandwidth, contention, coordination, metadata, and human control. Compare claimed scale with test range, asymptotic evidence, and empirical evidence.
- **Severity:** `S1` for headline scalability without evidence. Use `S2` for missing secondary analysis.
- **Exceptions / false positives:** A fixed-scale appliance or embedded system can have no general scalability claim.
- **Repair direction:** Give repair options: the limiting resource, sensitivity or range tests, or a bounded scalability claim.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [OSDI-CFP].

## TS-13 — Security and privacy reasoning covers new attack surfaces

- **Nature:** Condition for security or privacy claims. General risk check for privileged systems.
- **Reviewer attack:** “The new control plane, metadata, instrumentation, model, cache, or cross-domain interface creates an unexamined attack or leakage path.”
- **Check:** Examine privilege, input trust, confidentiality, integrity, availability, side channels, metadata leakage, secrets, policy bypass, compromised components, and denial of service.
- **Severity:** `S0` for a direct counterexample to a central property. Use `S1` for primary unresolved exposure.
- **Exceptions / false positives:** Full security analysis of unrelated benign components is not necessary. Safety consequences that affect claims or operation of privileged operations must still have findings.
- **Repair direction:** Give repair options: threat boundaries, least privilege or input validation, attack evaluations, or narrower claims.
- **Sources:** [OSDI-CFP], [LEVIN-REDELL].

## TS-14 — Implementation feasibility and status support the design

- **Nature:** Condition for accuracy. The necessary implementation level depends on paper type.
- **Reviewer attack:** “Critical paths are conceptual, simulated, stubbed, or delegated to unavailable components, yet the paper claims a working system.”
- **Check:** Make a map from design components to implementation evidence, code paths, hardware or software dependencies, and experiments. Give each implementation its status: implemented, emulated, simulated, mocked, analytically modeled, or future.
- **Severity:** `S0` for misrepresentation. Use `S1` for missing central feasibility evidence.
- **Exceptions / false positives:** Design or theory papers can stop before production implementation with corresponding claims and evaluation.
- **Repair direction:** Give implementation status and boundaries. Add feasibility evidence. Put necessary limits on deliverable claims.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [NSDI-ARTIFACT].

## TS-15 — Technical notation, algorithms, and examples agree

- **Nature:** Condition for internal consistency.
- **Reviewer attack:** “The prose, pseudocode, equation, example, and figure define different operations or quantities.”
- **Check:** Compare symbols, domains, units, indices, base cases, algorithm steps, figures, and worked examples. Calculate derivations with short formulas again. If in scope, do at least one example.
- **Severity:** `S0` when the mismatch invalidates a central result. For other cases, `S1`/`S2`/`S3`, as determined by consequence.
- **Exceptions / false positives:** Equivalent notations are permitted with clear correspondence.
- **Repair direction:** Select one authoritative definition. Make sure that all representations agree. Add domain and base conditions.
- **Sources:** [ERNST], [LEVIN-REDELL], [USER-NOTES].

## TS-16 — Generality claims identify what transfers

- **Nature:** Condition for accuracy in general claims.
- **Reviewer attack:** “The mechanism is inseparable from one workload, kernel version, ISA, topology, dataset, or proprietary service.”
- **Check:** Do a check of differences between transferable principles, parameterized mechanisms, porting work, environment-specific implementation, and tested instances. Find dependencies on hidden constants or handcrafted rules.
- **Severity:** `S1` for a central generality claim without evidence. Use `S2` for unclear transfer cost.
- **Exceptions / false positives:** A narrow system can have value without generality. Its significance must be clear within that scope.
- **Repair direction:** Give transfer conditions and porting effort. Where necessary, do evaluation on more instances. Put necessary limits on the claim.
- **Sources:** [LEVIN-REDELL], [SIGPLAN-EMPIRICAL], [OSDI-CFP].

## TS-17 — Limitations do not contradict the operating story

- **Nature:** Condition for internal consistency.
- **Reviewer attack:** “A late caveat removes the property, deployment scenario, or workload that motivated the system.”
- **Check:** Compare limitations with the abstract, introduction, system model, and conclusions. Examine excluded cases for rarity, detection, fail-safe behavior, and importance to the advertised scenario.
- **Severity:** `S0` when the caveat invalidates the central contribution. For other cases, `S1`.
- **Exceptions / false positives:** Accurate limitations are strengths when they bound the contribution without its negation.
- **Repair direction:** Make sure that the problem and claims agree. Give prevalence evidence. Add mitigation or evaluation.
- **Sources:** [OSDI-CFP], [LEVIN-REDELL], [SIGPLAN-EMPIRICAL].

## Soundness reconstruction template

Before completion of this pass, fill the table from evidence in scope.

| Element | Reconstructed content | Evidence location | Open risk |
|---|---|---|---|
| Actors/resources/boundary | | | |
| Inputs and outputs | | | |
| Assumptions/model | | | |
| Central invariant/property | | | |
| Mechanism and lifecycle | | | |
| Failure/concurrency behavior | | | |
| Costs and limiting resource | | | |
| Implementation status | | | |
| Exclusions/limitations | | | |

For each blank central row, give a finding or a clear not-assessable status.
