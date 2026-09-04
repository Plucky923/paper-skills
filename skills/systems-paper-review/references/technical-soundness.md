# Technical Soundness and System Design

Reconstruct the proposed system as if implementing, operating, or attacking it. A fluent overview is not evidence of a complete mechanism. Apply only to technical material in scope; missing details in a short excerpt are usually unresolved risks rather than confirmed omissions from the full paper.

## TS-01 — System model names actors, resources, and boundaries

- **Nature:** Hard condition for reasoning about correctness; presentation detail depends on paper type.
- **Reviewer attack:** “I cannot determine what the system controls, observes, trusts, or protects.”
- **Check:** Identify actors, components, resources, inputs/outputs, state, administrative domains, trust boundaries, and external dependencies. Draw an internal model if prose is ambiguous.
- **Severity:** `S1`; `S0` if the central guarantee is meaningless without the missing boundary.
- **Exceptions / false positives:** A conventional model may be concise, but unusual deviations and security-relevant boundaries must be explicit.
- **Repair direction:** State entities, authority, state, interfaces, and excluded responsibilities; align overview, figure, and mechanism.
- **Sources:** [SYSTEMS-GUIDE], [LEVIN-REDELL], [OSDI-CFP].

## TS-02 — Assumptions are explicit, necessary, and plausible

- **Nature:** Hard accuracy condition.
- **Reviewer attack:** “The method works only because it assumes an oracle, cooperative workload, ideal hardware, trusted component, synchronized clock, or failure-free environment.”
- **Check:** Enumerate stated and implied assumptions. For each, ask who establishes it, how it is checked, what happens when it fails, and whether alternatives need the same privilege.
- **Severity:** `S0` if a hidden/false assumption invalidates the central claim; otherwise `S1`.
- **Exceptions / false positives:** Strong assumptions are acceptable when bounded, motivated, and reflected in claims.
- **Repair direction:** Expose and justify the assumption, add validation/fallback, or narrow the claim.
- **Sources:** [LEVIN-REDELL], [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE].

## TS-03 — Threat, fault, and workload models match claims

- **Nature:** Hard correctness condition.
- **Reviewer attack:** “The claimed security/reliability/performance property is evaluated under a weaker adversary, fault set, or workload than the wording implies.”
- **Check:** List adversary capabilities, fault types, timing, workload distribution, excluded cases, and recovery goals. Compare each property verbatim with that model.
- **Severity:** `S0` for a central mismatch; otherwise `S1`.
- **Exceptions / false positives:** Non-security papers need not invent a threat model, but still require relevant fault/workload boundaries.
- **Repair direction:** Align the model and quantifiers; justify exclusions; add evidence or weaken the property.
- **Sources:** [OSDI-CFP], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL].

## TS-04 — Every major mechanism has a causal role

- **Nature:** General best practice and technical completeness condition.
- **Reviewer attack:** “The paper names modules but never shows how they produce the claimed property.”
- **Check:** For each component, trace input → state/operation → output → downstream effect → claim. Flag unexplained transformations and result-by-assertion.
- **Severity:** `S1` for central mechanism gaps; `S2` for secondary components.
- **Exceptions / false positives:** Standard implementation components may be summarized if their behavior is conventional and not part of the claim.
- **Repair direction:** Add operational detail and causal link; remove decorative components from the contribution story.
- **Sources:** [SYSTEMS-GUIDE], [LEVIN-REDELL].

## TS-05 — Inputs, outputs, state, and lifecycle are complete

- **Nature:** General best practice; hard when lifecycle affects correctness.
- **Reviewer attack:** “The algorithm is understandable only in steady state; initialization, termination, updates, cleanup, or reconfiguration are unspecified.”
- **Check:** Ask when each phase starts/stops, required preconditions, persistent/transient state, update triggers, idempotence, cleanup, and behavior across restart.
- **Severity:** `S1` if omitted lifecycle can break the property; otherwise `S2`.
- **Exceptions / false positives:** A paper may abstract routine setup, but must not abstract state transitions that change outcomes.
- **Repair direction:** Describe phase transitions, conditions, and state ownership; add pseudocode/state machine if it reduces ambiguity.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [ERNST].

## TS-06 — Invariants and guarantees have an enforcement story

- **Nature:** Hard correctness condition.
- **Reviewer attack:** “The paper asserts that property P always holds but provides no invariant, proof, validation point, or enforcement mechanism.”
- **Check:** Translate `ensure`, `guarantee`, `prevent`, `always`, `safe`, `correct`, and equivalents into a precise property. Identify the enforcement point and all state-changing paths.
- **Severity:** `S0` for an unsupported central guarantee; `S1` otherwise.
- **Exceptions / false positives:** Empirical reliability claims may be probabilistic; their language and evidence must reflect that.
- **Repair direction:** Define and justify the invariant, test all paths, replace a guarantee with observed behavior, or narrow its domain.
- **Sources:** [OSDI-CFP], [LEVIN-REDELL], [BRANDON-EVIDENCE].

## TS-07 — Concurrency, ordering, and time are specified where relevant

- **Nature:** Hard condition for concurrent/distributed mechanisms.
- **Reviewer attack:** “The design assumes an execution order that concurrent nodes, threads, interrupts, or failures do not preserve.”
- **Check:** Examine races, atomicity, synchronization, memory visibility, event ordering, clock assumptions, duplicates, reordering, and simultaneous updates.
- **Severity:** `S0` for a counterexample to correctness; `S1` for a major unresolved gap.
- **Exceptions / false positives:** Sequential/offline components can mark this not applicable.
- **Repair direction:** State ordering model and synchronization; handle or exclude races explicitly; add proof/test evidence.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP].

## TS-08 — Failure detection, containment, and recovery are coherent

- **Nature:** Hard for reliability/availability claims; otherwise context-dependent.
- **Reviewer attack:** “A partial failure leaves corrupt, leaked, duplicated, or unrecoverable state, or the recovery path assumes knowledge it cannot have.”
- **Check:** Cover crash, timeout, partition, resource exhaustion, bad input, partial write, component restart, and cascading failure as relevant. Track detection, rollback/retry, persistence, and restored invariant.
- **Severity:** `S0` for central correctness/data loss; `S1` for major availability risk; `S2` for unclaimed operational gap.
- **Exceptions / false positives:** Failure behavior outside the explicit model may be a limitation rather than defect if the exclusion is realistic and visible.
- **Repair direction:** Add failure path and state reconciliation, justify exclusion, or narrow reliability claims.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [OSDI-CFP].

## TS-09 — Edge cases and degenerate inputs do not defeat the method

- **Nature:** Hard when a counterexample violates a claim; diagnostic otherwise.
- **Reviewer attack:** “The mechanism only works on typical cases and silently fails at empty, maximal, skewed, adversarial, or rapidly changing inputs.”
- **Check:** Test boundary sizes, zero/one item, all-equal/all-different data, skew, churn, overload, malformed input, cold start, and conflicting objectives as relevant.
- **Severity:** `S0` for a valid central counterexample; `S1`/`S2` for unresolved coverage.
- **Exceptions / false positives:** Do not enumerate irrelevant combinatorial cases; select cases from the mechanism and claim domain.
- **Repair direction:** Handle, detect, or exclude the case and test the boundary.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [LEVIN-REDELL].

## TS-10 — Design choices are compared with credible alternatives

- **Nature:** General best practice.
- **Reviewer attack:** “The chosen mechanism is arbitrary; a simpler or established alternative may offer the same result.”
- **Check:** For each major choice, identify objective/constraints, plausible alternatives, tradeoffs, rejected strawman, and evidence. Detect strawmen weakened by bad configuration or false characterization.
- **Severity:** `S1` when novelty/necessity depends on the choice; otherwise `S2`.
- **Exceptions / false positives:** Routine implementation choices need not all be defended. Focus on choices that affect claims, cost, correctness, or generality.
- **Repair direction:** State decision criteria and compare fairly through reasoning, evidence, or targeted evaluation.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [JENSEN-SYSTEMS-SKILL].

## TS-11 — Costs are accounted at the same boundary as benefits

- **Nature:** Hard fairness condition for cost/performance claims.
- **Reviewer attack:** “The system looks efficient only because preprocessing, training, indexing, migration, failures, operator time, hardware, or storage are outside the accounting boundary.”
- **Check:** Enumerate one-time and recurring costs, resource shifts, client/server split, offline/online split, and amortization assumptions. Verify baselines use the same boundary.
- **Severity:** `S0` for materially deceptive accounting; otherwise `S1`.
- **Exceptions / false positives:** Excluding a one-time cost is acceptable when explicitly amortized over a justified lifetime and separately reported.
- **Repair direction:** Report complete costs and breakouts; justify amortization; qualify claims.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL].

## TS-12 — Scalability reasoning identifies the limiting resource

- **Nature:** General best practice; hard for broad scalability claims.
- **Reviewer attack:** “The evaluation stops before the design bottleneck, and no complexity or resource argument supports extrapolation.”
- **Check:** Identify computational, memory, storage, bandwidth, contention, coordination, metadata, and human-control scaling terms. Compare claimed scale with tested range and asymptotic/empirical evidence.
- **Severity:** `S1` for unsupported headline scalability; `S2` for missing secondary analysis.
- **Exceptions / false positives:** A fixed-scale appliance or embedded system may not claim general scale.
- **Repair direction:** Expose limiting resource, test sensitivity/range, or bound the scale claim.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [OSDI-CFP].

## TS-13 — Security and privacy reasoning covers new attack surfaces

- **Nature:** Hard when security/privacy is claimed; general risk check for privileged systems.
- **Reviewer attack:** “The new control plane, metadata, instrumentation, model, cache, or cross-domain interface creates an unexamined attack or leakage path.”
- **Check:** Track privilege, input trust, confidentiality/integrity/availability, side channels, metadata leakage, secret handling, policy bypass, compromised components, and denial of service.
- **Severity:** `S0` for a direct counterexample to a central property; `S1` for major unresolved exposure.
- **Exceptions / false positives:** Do not demand a full security analysis from unrelated benign components, but report material safety consequences of privileged operation.
- **Repair direction:** Define threat boundary, enforce least privilege/validation, evaluate attacks, or narrow claims.
- **Sources:** [OSDI-CFP], [LEVIN-REDELL].

## TS-14 — Implementation feasibility and status support the design

- **Nature:** Hard accuracy condition; level of implementation is paper-dependent.
- **Reviewer attack:** “Critical paths are conceptual, simulated, stubbed, or delegated to unavailable components, yet the paper claims a working system.”
- **Check:** Map design components to implementation evidence, code path, hardware/software dependency, and experiment. Distinguish implemented, emulated, simulated, mocked, analytically modeled, and future.
- **Severity:** `S0` for misrepresentation; `S1` for central missing feasibility evidence.
- **Exceptions / false positives:** Design/theory papers may intentionally stop before production implementation if framed and evaluated accordingly.
- **Repair direction:** Disclose status and boundary; add feasibility evidence; narrow deliverable claims.
- **Sources:** [LEVIN-REDELL], [OSDI-CFP], [NSDI-ARTIFACT].

## TS-15 — Technical notation, algorithms, and examples agree

- **Nature:** Hard internal-consistency condition.
- **Reviewer attack:** “The prose, pseudocode, equation, example, and figure define different operations or quantities.”
- **Check:** Cross-check symbols, domains, units, indices, base cases, algorithm steps, figures, and worked examples. Recompute simple derivations and trace at least one example when in scope.
- **Severity:** `S0` if it invalidates a central result; otherwise `S1`/`S2`/`S3` by consequence.
- **Exceptions / false positives:** Equivalent notations are acceptable if correspondence is explicit.
- **Repair direction:** Select one authoritative definition, reconcile every representation, and add domain/base conditions.
- **Sources:** [ERNST], [LEVIN-REDELL], [USER-NOTES].

## TS-16 — Generality claims identify what transfers

- **Nature:** Hard accuracy condition for general claims.
- **Reviewer attack:** “The mechanism is inseparable from one workload, kernel version, ISA, topology, dataset, or proprietary service.”
- **Check:** Separate transferable principle, parameterized mechanism, porting work, environment-specific implementation, and tested instances. Look for dependence on hidden constants or handcrafted rules.
- **Severity:** `S1` for a central unsupported generality claim; `S2` for unclear transfer cost.
- **Exceptions / false positives:** A narrowly scoped system can be valuable without generality if significance is established in that scope.
- **Repair direction:** State transfer conditions and porting effort, evaluate more instances where necessary, or narrow the claim.
- **Sources:** [LEVIN-REDELL], [SIGPLAN-EMPIRICAL], [OSDI-CFP].

## TS-17 — Limitations do not contradict the operating story

- **Nature:** Hard internal-consistency condition.
- **Reviewer attack:** “A late caveat removes the property, deployment scenario, or workload that motivated the system.”
- **Check:** Compare limitations with abstract, introduction, system model, and conclusions. Determine whether excluded cases are rare, detectable, and fail-safe, or fundamental to the advertised scenario.
- **Severity:** `S0` if the caveat collapses the central contribution; otherwise `S1`.
- **Exceptions / false positives:** Honest limitations are a strength when they bound rather than negate the contribution.
- **Repair direction:** Reframe problem and claims consistently; justify prevalence; add mitigation or evaluation.
- **Sources:** [OSDI-CFP], [LEVIN-REDELL], [SIGPLAN-EMPIRICAL].

## Soundness reconstruction template

Before closing the pass, fill this table from in-scope evidence:

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

Any blank central row is either a finding or explicitly not assessable under scope.
