# Interface, Boundary, Authority, and Path Claims

For an interface, boundary, customization, implementation freedom, isolation, or direct/delegated path argument, use this shared contract.
It adds conditional reasoning checks to the [writing core](writing-core.md).
It is not a required paragraph template or venue rule.

## Keep a three-axis ledger

Before acceptance of a compound boundary claim, find its three independent axes:

| Axis | Information from scoped material | Possible claim |
|---|---|---|
| **Semantic commitments** | Objects, operations, state transitions, errors, authority rules, and lifecycle behavior fixed by the interface | Abstractions that a client can implement, replace, or omit above that contract |
| **Protection and authority** | Principals, protected objects, trust assumptions, admission rules, grants, checks, allocation, binding, revocation, reclamation, and enforcement points | Memory soundness, resource authorization, fault containment, and lifecycle properties in named assumptions |
| **Execution path** | Transitions, copies, emulation, mediation, delegation, and resource work for a specified operation | Path cost or prediction, and an observed end-to-end effect only with evidence |

No axis determines another.
A lower-level interface has semantics.
A shared address space alone does not show isolation, policy freedom, or lower end-to-end cost.
A hardware protection domain does not identify the abstractions that a client can replace.

If a claim crosses axes, give an anchor for each edge.
Apply the writing core's source-status, causal-layer, and counterfactual tests.
If the passage does not rely on an axis, set it to `not claimed`.
Do not invent an obligation for that axis.

## Bound semantic freedom and customization

An interface specifies more than a privilege level.
Find the client-visible objects and behavior that stay fixed.
Then show what can vary above that contract.
If a necessary operation, transition, or failure behavior is absent, the client must have an adapter or changed mediator.
`resource-level`, `low-level`, `policy-neutral`, and `general` do not prove interface coverage.

For `customizable`, `independent`, `pluggable`, `extensible`, or equivalent claims, record **actor, artifact, stage, and control**:

- Actor: source author, operator, runtime deployer, tenant, or untrusted client
- Artifact: configuration, policy, extension, linked component, loadable artifact, mediator, or full implementation
- Stage: source/build time, deployment, instance creation, or runtime
- Control: whose rebuild, installation, approval, or privilege is necessary for the change.

Keep these different capabilities:

- Source-fork customization
- Host-compiled extension
- Per-instance configuration
- Tenant-supplied runtime replacement.

Use the capability that the evidence supports.
Keep its deployment-model qualifications.

## Attribute protection through a responsibility chain

For an isolation or authority claim, reconstruct the shortest sufficient chain:

```text
protected object or invariant
  -> admission, non-forgeability, or no-bypass condition
  -> runtime identity, ownership, quota, revocation, and lifecycle decisions
  -> resource-specific enforcement and fault behavior
```

Give each step to the mechanism that supplies it.
A language, type system, capability representation, or hardware substrate can remove one bypass class.
That result does not show full authorization, lifecycle protection, fault containment, or availability.
Find the state-changing events that a trusted mediator decides.
For each claimed resource, give the explanation for the backend's continued enforcement of those decisions.

A direct or delegated data path does not show protection or its absence by itself.
Find how the system gives authority before delegation.
Find the capability that stays available or backend rule that constrains each operation.
Find how revocation, termination, failure, and cleanup restore the invariant.

`the host mediates every operation` is too broad when some paths use delegation.
Instead, give the control events and continued enforcement.

## Compare boundaries at the licensed commitment

For each alternative, use the same comparison tuple:

```text
exposed or mediated interface
  -> state and responsibility retained on each side
  -> one consequence material to the current question
```

Put the bridge in one of these classes:

- **`negative gap`:** Prior approaches cannot, do not, or fundamentally fail to supply a target property.
  For this claim, give a fair common axis and evidence about each named alternative.
  Give the shared assumption, mechanism, or constraint that causes the bounded failure.
- **`distinct question`:** Different placements suggest a possible alternative contract or responsibility division.
  For this claim, give a parallel map and a question that comes from it.
  Do not invent a common failure.
  It shows neither prior-work absence nor novelty.

Examine absence and novelty claims independently wherever the manuscript makes them.
A descriptive taxonomy can stop without either bridge.
Do not convert it into a gap.
Do not demand a root cause for a failure that the passage does not claim.

Treat `tradeoff`, `tension`, `fundamental`, `impossible`, and equivalent words as causal claims.
Give a definition of each objective with a measurement or another test.
Find the connecting constraint and its assumption domain.
Examine counterexamples and alternative mechanisms in the same problem domain.
Give the decisive evidence.

If sources show only a conditional interaction, keep it as a bounded tension.
Do not make it a universal law.

## Keep path facts and measured outcomes as different categories

Before a cost claim, find each step in the specified operation.
Removal of an address-space switch, transition, copy, or emulation step can show a path fact or prediction.
Scheduling, authorization, queueing, resource work, and workload mix determine the end-to-end result.

For a measured improvement, give these matched comparison attributes:

- Semantic guarantee and baseline
- Resources and workload
- Metric and aggregation
- Important uncertainty.

Evidence for one path does not apply automatically to other operations or the full system.

## Match explanation depth to the section

An abstract or introduction gives the causal core necessary to understand its claim:

- The visible object or contract
- The consequential responsibility division
- The related property and boundary.

If that division is the intellectual contribution, give the mechanism categories there.
Put resource-specified data structures, drivers, state machines, and backend inventories in Overview or Design.
Keep a detail before the principle only when it shows the central causal step.
This is a reader-obligation test, not a fixed sentence count or section order.

## Review and revision actions

Review makes only the axis rows necessary for manuscript claims.
It keeps organization, technical support, and external truth as different categories.
It locates each invalid cross-axis edge at its initial endpoints.
A missing edge becomes a finding or unresolved risk.
Use the action class from the [shared workflow contract](review-revise-contract.md).
Do not supply the explanation as reviewer evidence.

Revise keeps propositions in each axis when evidence supports them.
Divide a conflated sentence in its permitted paragraph only when supplied evidence fixes attribution without ambiguity.
Do not convert interface placement into customization.
Do not convert one protection mechanism into full isolation.
Do not convert a path fact into an end-to-end result.

If a repair changes scientific intent or claim strength, use the shared clarification loop.
Examples include a negative gap, universal claim, trade-off, or customization model.
An author decision can give permission for narrowing or withdrawal.
It does not replace evidence for a stronger or new factual claim.
