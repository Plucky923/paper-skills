# Positive Contracts by Contribution Type

Read this reference when contribution type changes the required argument.
Select the primary contract from the strongest acceptance claim that evidence supports.
Use secondary contributions only to support that claim.
These contracts give dependencies, not fixed sentence or section orders.

## Route the contribution

Find the scientifically valuable proposition that stays without the artifact name and largest performance number.
Use these contribution types:

- A new system boundary, interface, or abstraction
- A performance result caused by co-design
- A correctness, verification, or security guarantee
- A measurement, characterization, or negative finding
- A production intervention or operational lesson that other systems can use
- A study whose findings yield a tool
- A benchmark, dataset, simulator, or testing infrastructure
- A formal or analytical method
- A bounded case study or guideline.

If two answers imply different audiences, evidence, or thesis hierarchies, keep the two as author choices.
Do not select the answer that is easier to market.

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

The contribution is the changed relation and its consequences.
An API name or component count alone does not supply that contribution.
Give sufficient mechanism information to show that the abstraction can operate.
Show that the abstraction's definition alone is not sufficient for its claimed property.

For an interface or boundary contribution, apply the [interface-boundary contract](interface-boundaries.md).
Find the interface's semantic commitments and the choices that a client can make above them.
Find the protection/authority division and any different execution-path claim.
One axis does not replace another.

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

Show the dependency between the mechanisms.
A benefit from each optimization alone does not show co-design.
A microbenchmark gain does not show the end-to-end claim.

## Verification, correctness, or security

```text
failure or assurance gap
  → precise model and target property
  → tractability or enforcement insight
  → proof, checker, or enforcement method
  → soundness and coverage boundary
  → usability, implementation status, and overhead
```

Keep different meanings for `proves`, `checks`, `detects`, `prevents`, and `observes`.
A proof does not show deployment with its use conditions.
Evaluation scale does not replace a correctness argument.

## Measurement, characterization, or negative result

```text
important unknown or disputed assumption
  → observable population and trustworthy method
  → validated observations
  → robustness and alternative explanations
  → bounded finding or falsified assumption
  → consequence for design, operation, or future studies
```

The contribution can be a taxonomy, asymmetry, limit, or absence of an expected effect.
A new mechanism or causal root cause is not necessary.
Show representativeness and measurement validity.
Identify the population to which the conclusion applies.

## Operational or experience paper

```text
production setting and stakes
  → observed failure, cost, or opportunity
  → diagnosis grounded in field evidence
  → intervention or changed practice
  → production outcome over meaningful scale or time
  → transferable lesson and unresolved limit
```

Scale and longitudinal deployment data are evidence when they show the phenomenon, intervention, or SLO outcome.
Show the lesson that another system can use when the stated conditions hold.
Deployment alone is not that lesson.

## Hybrid study plus tool

```text
observed incidents or phenomena
  → taxonomy or root causes
  → requirements derived from the study
  → tool or mechanism
  → coverage of the discovered classes
  → controlled or deployed validation
```

Make the derivation clear.
Connect each important tool capability to a requirement from the study.
A study followed by an unrelated artifact gives two claims.
It does not give one hybrid contribution with a clear derivation.

## Benchmark, dataset, simulator, or testing infrastructure

```text
measurement or validation deficit
  → principled construction criteria
  → artifact and methodology
  → coverage, representativeness, or fidelity
  → reproducibility and use cost
  → conclusions or failures newly exposed
```

Show what the infrastructure makes measurable that was not measurable before.
Do a check of the representation's scientific adequacy and the cost to use it.
Popularity or size alone is not validation.

## Formal or analytical method

```text
property or analysis obstacle
  → model and assumptions
  → new abstraction, decomposition, or algorithm
  → soundness, completeness, or approximation argument
  → tractability or precision evidence
  → applicability and failure boundary
```

Keep theorem-level guarantees, implementation claims, and empirical claims as different categories.
If the method is intentionally incomplete or approximate, make the trade-off part of the contribution.
Do not hide it only in limitations.

## Case study or guideline

```text
decision faced in a bounded setting
  → principled selection of cases and observations
  → analysis of the governing factors
  → finding or guideline
  → counterexamples and sensitivity
  → conditions under which the lesson transfers
```

Show the stable mechanism or decision boundary that makes the case interesting to other systems.
One instance does not represent a universal population.
Keep case observations and the inference that other systems can use them as different categories.

## Mixed contributions

Use one controlling thesis.
Put each secondary contribution below the claim it supports:

```text
thesis
  ├─ finding that derives a requirement
  ├─ mechanism or method that discharges it
  └─ evidence that tests the resulting claim
```

A flat list of a system, dataset, implementation, and performance number is not a hierarchy.
If evidence supports several independent papers, give that diagnosis to the author.
Do not force a synthetic relation to make one decision case.
