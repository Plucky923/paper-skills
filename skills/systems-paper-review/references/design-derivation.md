# Design Derivation and Mechanism Necessity

Use this reference when the scope includes an overview, design, algorithm, system architecture, implementation rationale, or an introduction that derives technical challenges. It connects top-down scientific reasoning to the bottom-up soundness checks in [technical-soundness.md](technical-soundness.md).

## Required derivation chain

For each major mechanism, reconstruct:

`observed failure or desired property → binding constraint → design requirement → mechanism → invariant/effect and tradeoff → decisive test`

The chain is not required as a prose template. It is an audit of whether the mechanism is scientifically motivated, technically sufficient, and empirically testable.

## DD-01 — The binding constraint is established

- **Check:** Distinguish a symptom from the constraint that makes obvious solutions fail. Locate measurement, counterexample, model property, theorem, prior-work limitation, or operational evidence that supports it.
- **Reviewer attack:** “The design solves an asserted root cause that the paper never establishes.”
- **Severity:** `S1`; `S0` when the constraint is contradicted and the design depends on it.

## DD-02 — Requirements are derived rather than announced

- **Check:** For each stated goal, challenge, or desideratum, identify the earlier problem/constraint that necessitates it. Separate essential requirements from preferences and implementation conveniences.
- **Reviewer attack:** “The requirements are chosen to fit the proposed system rather than derived from the problem.”
- **Severity:** `S1` for central circularity; otherwise `S2`.
- **Exception:** Standard requirements may be cited or briefly justified when genuinely shared by the field.

## DD-03 — Each mechanism discharges a requirement

- **Check:** Map every major component or algorithmic step to the requirement it satisfies, including interaction with other mechanisms. Flag orphan components, duplicate mechanisms, and requirements with no implementation path.
- **Reviewer attack:** “This is a component inventory, not a design argument.”
- **Severity:** `S1` for a missing central link; otherwise `S2`.

## DD-03A — A claimed shared insight has source-grounded causal fan-out

- **Check:** When one intellectual move is claimed or implied to produce several
  primary properties, apply the canonical fan-out test in the
  [systems-writing core](../../systems-paper-revise/references/writing-core.md#source-grounded-intellectual-move-fan-out).
  Anchor the shared move and every move-to-property edge, and label each one
  `stated`, `text-licensed`, or `reviewer-hypothesized`. A reviewer-supplied
  bridge is a missing dependency even when it yields an elegant reconstruction.
- **Reviewer attack:** “These benefits share a system name, but the paper never
  shows that one conceptual change causes all of them.”
- **Severity:** `S1` when the unified claim carries the contribution; `S2` when
  the paper could accurately present the items as separate supporting claims.
- **Exception:** Independent contributions need no artificial common cause when
  the manuscript presents and evaluates them independently.

## DD-03B — Each property is attributed to its narrowest sufficient layer

- **Check:** Separate enabling substrate, changed abstraction or authority
  boundary, runtime enforcement and lifecycle, execution path, and empirical
  condition. For every claimed property, state what each layer establishes and
  what still depends on another layer. Use the counterfactual in the canonical
  fan-out test to expose attribution that is merely adjacent in the prose.
- **Reviewer attack:** “The paper credits the language, interface, or shared
  runtime with a compound guarantee that actually depends on unmentioned checks,
  completeness, lifecycle behavior, or workload conditions.”
- **Severity:** `S0` for a false central guarantee; `S1` for a central missing
  attribution path; otherwise `S2`.

## DD-04 — The mechanism explains the resulting property

- **Check:** State the relevant input/state, action or changed abstraction, enforcement point, and property that follows. Identify assumptions and whether the result is guaranteed, detected, enabled, or only observed.
- **Reviewer attack:** “The prose says the mechanism ‘ensures’ the property without explaining the causal or enforcement path.”
- **Severity:** `S0` for a false central guarantee; `S1` for an absent central explanation.

## DD-05 — Tradeoffs and shifted costs are part of the derivation

- **Check:** Name what the mechanism gives up or moves: generality, latency, throughput, memory, hardware, offline work, operator effort, failure recovery, trust, compatibility, or implementation complexity. Verify the thesis remains meaningful after accounting for it.
- **Reviewer attack:** “The apparent benefit comes from relaxing the problem or moving cost outside the measured boundary.”
- **Severity:** `S0` when undisclosed and fatal; otherwise `S1`/`S2`.

## DD-06 — Alternatives test necessity, not only superiority

- **Check:** Compare with the simplest credible design that shares the same assumptions. Ask which requirement it fails and whether the proposed mechanism is the minimal conceptual change needed. An ablation can show contribution to performance but may not explain design necessity.
- **Reviewer attack:** “A simpler mechanism appears to provide the same property under the paper's assumptions.”
- **Severity:** `S1`; `S2` when rationale is locally incomplete.

## DD-07 — Evaluation closes the derivation chain

- **Check:** For every central requirement and claimed property, identify the proof, experiment, negative case, sensitivity test, or field observation that can validate it. End-to-end results establish total effect; attribution or controlled analysis is required only when the paper claims a particular cause.
- **Reviewer attack:** “The mechanism is plausible, but the evidence never tests the reason it was introduced.”
- **Severity:** `S0`/`S1` by claim centrality.

## Knowledge-state rule

Do not force every principle to precede every technical detail. An early low-level fact is appropriate when it is the evidence that reveals the constraint, makes a counterexample concrete, or defines the target property. Flag detail only when the reader cannot yet know why it matters or when it substitutes for the governing relation.

## Derivation map

| Failure/property | Supporting evidence | Constraint | Requirement | Mechanism | Property/invariant | Tradeoff | Decisive test | Gap |
|---|---|---|---|---|---|---|---|---|

For multi-mechanism systems, inspect both directions: every requirement needs a discharge, every major mechanism needs a requirement, and every claimed shared move needs an anchored edge to each advertised outcome. Do not treat implementation effort, co-location, or reviewer reconstruction as evidence of conceptual necessity.

## Sources

This derivation model operationalizes [LEVIN-REDELL], [SYSTEMS-GUIDE], the system and evidence criteria in [OSDI-CFP] and [SOSP-CFP], and recurring constraint-to-mechanism structures in [FIVE-VENUE-CORPUS].
