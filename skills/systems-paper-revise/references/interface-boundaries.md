# Interface, Boundary, Authority, and Path Claims

Use this shared contract when a paper's argument depends on an interface,
virtualization or protection boundary, customization or independent
implementation, isolation, or a direct/delegated execution path. It specializes
the [writing core](writing-core.md); it is a conditional reasoning aid, not a
required paragraph template or a venue rule.

## Keep a three-axis ledger

Recover three independent axes before accepting a compound boundary claim:

| Axis | Recover from the scoped material | What it can support |
|---|---|---|
| **Semantic commitments** | The objects, operations, state transitions, errors, authority rules, and lifecycle behavior fixed by the interface. | Which abstractions a client may implement, replace, or omit above that declared contract. |
| **Protection and authority** | The principals, protected objects, trust assumptions, admission rules, grants, checks, allocation, binding, revocation, reclamation, and enforcement points. | Memory soundness, resource authorization, fault containment, and lifecycle properties under named assumptions. |
| **Execution path** | The transitions, copies, emulation, mediation, delegation, and resource work performed by a particular operation. | A path-level cost model or prediction, and only with evidence an observed end-to-end effect. |

No axis determines any of the others. A lower-level interface is not
semantics-free; a shared address space does not establish isolation, policy
freedom, or lower end-to-end cost; and a hardware protection domain does not
state which abstractions a client can replace. When a claim crosses axes, anchor
each edge and apply the writing core's source-status, causal-layer, and
counterfactual tests. Mark an axis `not claimed` rather than inventing an
obligation the passage does not rely on.

## Bound semantic freedom and customization

An interface commits to more than a privilege level. Identify the client-visible
objects and behavior that remain fixed, then state what can vary only above that
contract. A client that needs an absent lower-level operation, state transition,
or failure behavior needs an adapter or a changed mediator; calling the interface
`resource-level`, `low-level`, `policy-neutral`, or `general` does not prove its
coverage.

For `customizable`, `independent`, `pluggable`, `extensible`, or equivalent claims,
recover the **actor, artifact, stage, and control**:

- who changes the system: source author, operator, runtime deployer, tenant, or
  untrusted client;
- what changes: configuration, policy, extension, linked component, loadable
  artifact, mediator, or complete implementation;
- when it changes: source/build time, deployment, instance creation, or runtime;
- whose rebuild, installation, approval, or privilege is required.

Source-fork customization, host-compiled extension, per-instance configuration,
and tenant-supplied runtime replacement are distinct capabilities. State the one
the evidence supports and preserve deployment-model qualifications.

## Attribute protection through a responsibility chain

For an isolation or authority claim, reconstruct the narrowest sufficient chain:

```text
protected object or invariant
  -> admission, non-forgeability, or no-bypass condition
  -> runtime identity, ownership, quota, revocation, and lifecycle decisions
  -> resource-specific enforcement and fault behavior
```

Assign every step to the mechanism that actually supplies it. A language,
type system, capability representation, or hardware substrate may remove one
bypass class without establishing complete authorization, lifecycle, fault
containment, or availability. A trusted mediator must identify the state-changing
events it decides; a backend must explain how those decisions remain effective
for CPU, memory, storage, devices, or other claimed resources.

A direct or delegated data path is neither inherently protected nor inherently
unprotected. Recover how authority is established before delegation, what
persistent capability or backend rule constrains each operation, and how
revocation, termination, failure, and cleanup restore the invariant. Conversely,
`the host mediates every operation` is too broad when some paths are delegated;
name the control events and continuing enforcement instead.

## Compare boundaries at the licensed commitment

For each alternative in a boundary comparison, use one parallel tuple:

```text
exposed or mediated interface
  -> state and responsibility retained on each side
  -> one consequence material to the current question
```

Then classify the bridge:

- A **`negative gap`** says prior approaches cannot, do not, or fundamentally
  fail to provide a target property. It requires a fair common axis, a shared
  assumption, mechanism, or constraint that causes the bounded failure, and
  evidence for the claims about the named alternatives.
- A **`distinct question`** maps supported placements and asks whether another
  contract or division of responsibility is possible. It needs a parallel map
  and a question that follows from it, but no invented common failure. This local
  bridge establishes neither prior-work absence nor novelty; assess those claims
  separately wherever the manuscript makes them.

A descriptive taxonomy may stop without either bridge. Do not promote it into a
gap, and do not demand a root cause for a failure the passage does not claim.

Treat `tradeoff`, `tension`, `fundamental`, `impossible`, and equivalent wording as
causal claims. Operationalize each objective, identify the constraint connecting
them, state the assumption domain, test nearby counterexamples or alternative
mechanisms, and name the decisive evidence. When the sources establish only a
conditional interaction, preserve it as a bounded tension rather than a universal
law.

## Keep path facts separate from measured outcomes

Trace the exact operation before writing a cost consequence. Removing an address-
space switch, transition, copy, or emulation step can support a path-level fact or
prediction while scheduling, authorization, queueing, resource work, and workload
mix still determine the end-to-end result. A measured improvement requires a
matched semantic guarantee, baseline, resources, workload, metric, aggregation,
and material uncertainty. Evidence for one path does not transfer to unrelated
operations or the whole system.

## Match explanation depth to the section

An abstract or introduction supplies the causal core needed to understand the
claim: the visible object or contract, the consequential division of
responsibility, and the relevant property and boundary. Name the mechanism
categories there when that division is the intellectual contribution. Defer
resource-specific data structures, drivers, state machines, and backend inventories
to Overview or Design unless they establish the central causal step. This is a
reader-obligation test, not a fixed sentence count or section order.

## Review and revision actions

Review builds only the axis rows triggered by the manuscript's claims, keeps
organization, technical support, and external truth separate, and locates every
invalid cross-axis edge at its original endpoints. A missing edge becomes a
finding or unresolved risk with the action class from the [shared workflow
contract](review-revise-contract.md), not a reviewer-supplied explanation.

Revise preserves supported axis-specific propositions and may separate a
conflated sentence inside its authorized paragraph when the supplied evidence
fixes the attribution unambiguously. It does not turn interface placement into
customization, a protection mechanism into complete isolation, or a path fact
into an end-to-end result. If a repair would change whether the author intends a
negative gap, universal claim, tradeoff, customization model, or other scientific
claim strength, obtain the author's decision through the shared clarification
loop. That decision can authorize narrowing or withdrawal; it does not substitute
for evidence needed to support a strengthened or newly factual claim.
