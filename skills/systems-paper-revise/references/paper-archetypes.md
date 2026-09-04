# Positive Contracts by Contribution Type

Read this reference when the paper's contribution type changes what must be argued. Select the primary contract from the strongest supported acceptance claim, then use secondary contributions only to support it. These are dependency relations, not fixed sentence or section orders.

## Route the contribution

Ask which proposition would remain scientifically valuable if the artifact name and largest performance number disappeared:

- a new system boundary, interface, or abstraction;
- a performance result caused by a co-design;
- a correctness, verification, or security guarantee;
- a measurement, characterization, or negative finding;
- a production intervention or transferable operational lesson;
- a study whose findings derive a tool;
- a benchmark, dataset, simulator, or testing infrastructure;
- a formal or analytical method;
- a bounded case study or guideline.

When two answers imply different audiences, evidence, or thesis hierarchies, preserve both as author choices rather than selecting the more marketable one.

## New system, abstraction, or interface

```text
newly important setting or requirement
  → mismatch in the existing contract
  → binding constraint
  → changed boundary or abstraction
  → resulting property
  → mechanism and implementation reality
  → benefit, compatibility, cost, and limits
```

The contribution is the changed relationship and what follows from it, not the API name or number of components. Explain enough mechanism to show that the abstraction is realizable and that its property is not merely definitional.

## Performance system or co-design

```text
consequential workload or bottleneck
  → why local optimizations saturate
  → exploitable structure
  → derived requirements
  → interacting mechanisms
  → end-to-end effect
  → attribution, shifted costs, and operating range
```

Show why the mechanisms need one another. A collection of individually useful optimizations does not establish co-design, and a microbenchmark gain does not establish the end-to-end claim.

## Verification, correctness, or security

```text
failure or assurance gap
  → precise model and target property
  → tractability or enforcement insight
  → proof, checker, or enforcement method
  → soundness and coverage boundary
  → usability, implementation status, and overhead
```

Keep `proves`, `checks`, `detects`, `prevents`, and `observes` distinct. A proof does not establish practical deployment; evaluation scale does not replace a correctness argument.

## Measurement, characterization, or negative result

```text
important unknown or disputed assumption
  → observable population and trustworthy method
  → validated observations
  → robustness and alternative explanations
  → bounded finding or falsified assumption
  → consequence for design, operation, or future studies
```

The contribution may be a taxonomy, asymmetry, limit, or absence of an expected effect. It need not contain a new mechanism or causal root cause. Establish representativeness, measurement validity, and the population to which the conclusion transfers.

## Operational or experience paper

```text
production setting and stakes
  → observed failure, cost, or opportunity
  → diagnosis grounded in field evidence
  → intervention or changed practice
  → production outcome over meaningful scale or time
  → transferable lesson and unresolved limit
```

Scale and deployment history are evidence when they establish the phenomenon, intervention, or SLO outcome. Convert experience into knowledge another system can apply under stated conditions; deployment alone is not the lesson.

## Hybrid study plus tool

```text
observed incidents or phenomena
  → taxonomy or root causes
  → requirements derived from the study
  → tool or mechanism
  → coverage of the discovered classes
  → controlled or deployed validation
```

Make the derivation visible: each major tool capability should answer a study-derived requirement. A study followed by an unrelated artifact remains two claims rather than one coherent hybrid contribution.

## Benchmark, dataset, simulator, or testing infrastructure

```text
measurement or validation deficit
  → principled construction criteria
  → artifact and methodology
  → coverage, representativeness, or fidelity
  → reproducibility and use cost
  → conclusions or failures newly exposed
```

State what the infrastructure makes measurable that was not measurable before. Evaluate both the scientific adequacy of the representation and the practical cost of using it; popularity or size alone is not validation.

## Formal or analytical method

```text
property or analysis obstacle
  → model and assumptions
  → new abstraction, decomposition, or algorithm
  → soundness, completeness, or approximation argument
  → tractability or precision evidence
  → applicability and failure boundary
```

Keep theorem-level guarantees separate from implementation and empirical claims. If the method is intentionally incomplete or approximate, make the trade-off part of the contribution rather than hiding it in limitations.

## Case study or guideline

```text
decision faced in a bounded setting
  → principled selection of cases and observations
  → analysis of the governing factors
  → finding or guideline
  → counterexamples and sensitivity
  → conditions under which the lesson transfers
```

A case study earns general interest by identifying a stable mechanism or decision boundary, not by treating one instance as a universal population. Separate observations in the case from the inference that other systems may reuse.

## Mixed contributions

Use one controlling thesis. Place each secondary contribution beneath the claim it supports:

```text
thesis
  ├─ finding that derives a requirement
  ├─ mechanism or method that discharges it
  └─ evidence that tests the resulting claim
```

A flat list of a system, dataset, implementation, and performance number is not a hierarchy. If the evidence supports several genuinely independent papers rather than one decision case, preserve that diagnosis for the author instead of forcing a synthetic link.
