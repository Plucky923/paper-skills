# Structural Revision Strategies

Use this reference when a defect spans several sentences, sections, claims, or evidence objects. Diagnose the root cause before selecting a repair; apply the positive prose standard in [writing-core.md](writing-core.md) after the scientific structure is sound.

## Choose the repair

Ask:

1. What claim or reader obligation fails?
2. Is it false or unsupported, missing a premise, organized around the wrong dependency, expressed at the wrong level, or merely unclear?
3. Which support already exists inside scope or in a permitted verified source?
4. What is the smallest coherent region whose revision closes the root cause?
5. Could that change create a new promise, contradiction, or author-intent choice elsewhere in scope?

An admissible repair may:

- correct a proposition from authoritative evidence;
- expose an inference already warranted by established premises;
- reorganize supported material around its dependencies;
- narrow or delete a claim that exceeds its evidence;
- add supported content required to complete the local argument.

When none applies, state the evidence, source, context, or author decision required. Prose alone cannot repair that gap.

## Rebuild only when the argument requires it

Rebuild the authorized structure when any of these conditions holds:

- no single controlling thesis explains the scoped material;
- the prose follows a contribution contract different from the evidence it offers;
- major mechanisms or analyses do not derive from visible requirements;
- headline evidence does not test the main claim;
- local repairs preserve contradictory promises across the scope.

First choose the positive contract in [paper-archetypes.md](paper-archetypes.md). Then build only the necessary internal maps:

```text
controlling thesis
  → supporting claim or finding
  → reason, mechanism, or method
  → decisive evidence
  → boundary and failure consequence
```

Use a design-derivation map or claim-evidence map only when that relation is actually broken. At paragraph scale, repair directly from the local obligation instead of constructing a paper-wide model.

## Contribution and positioning

- Recover actor, setting, failure or unknown, and consequence from existing evidence. Narrow importance to the observed setting when prevalence or impact is unknown.
- State the exact change in assumption, boundary, capability, guarantee, cost, or evidence relative to prior work. Replace open-world superlatives with a bounded delta.
- Group related work by a decision-relevant dimension rather than publication chronology.
- Separate prototype, simulation, deployment, and production status; state transfer conditions instead of universal generality.
- Preserve an author decision when several contribution hierarchies are scientifically defensible.

## Technical explanation

- Introduce actors, resources, trust, fault, and workload boundaries before a mechanism depends on them.
- Explain an operation as input/state → action → output/property, including lifecycle or failure behavior only where it affects the claim.
- State the objective and constraints before comparing a design alternative; account for setup, offline, operator, and shifted resource costs beside the claimed benefit.
- Distinguish designed, implemented, emulated, simulated, and future components.
- Reconcile prose, figure, equation, pseudocode, and example against one supported interpretation. Conflicting sources require resolution, not a silent choice.

## Evaluation and result interpretation

Organize the evaluation around falsifiable claims or recoverable questions rather than experiment chronology. For each decisive result, make the following relation visible:

```text
claim or question
  → method, workload, baseline, metric, and control conditions
  → result and uncertainty
  → interpretation
  → supported scope and remaining alternative explanations
```

- Match end-to-end results to practical claims and use microbenchmarks or ablations only for the causal attribution they can support.
- Compare like-for-like semantics, resources, tuning opportunities, and objectives. Record a deliberately relaxed guarantee as part of the result.
- Define timing and resource boundaries, aggregation, numerator/denominator, repetitions, and uncertainty when they affect interpretation.
- Bound conclusions to evaluated workloads, hardware, scale, data, failure model, and implementation status.
- Add a robustness or ablation result only when the available evidence exists and the corresponding claim requires it. Otherwise narrow the claim or expose the evidence gap.
- Treat negative results, failure regions, and plausible alternative explanations as scientific information rather than prose to hide.

## Section and attention repair

Use the section contracts in [writing-core.md](writing-core.md). Reallocate attention according to novelty and uncertainty:

- expand the counterintuitive constraint, intellectual move, critical mechanism, closest-work delta, decisive evidence, and material limitation;
- compress commodity background, implementation inventory, repeated motivation, and secondary results that do not alter the decision case;
- define concepts before substantive use and remove terminology with no later reasoning role;
- move enough motivation evidence before the requirement it licenses, while retaining full methodology where it belongs;
- keep overview, design rationale, implementation reality, and evaluation evidence at distinct depths even when a paper combines their sections.

For a title, abstract, introduction, or whole-paper story, route through [paper-archetypes.md](paper-archetypes.md). Do not convert an empirical, negative-result, formal, or operational contribution into a mechanism narrative merely to make it resemble a conventional system paper.

## Figures, tables, and captions

- Give each figure or table one argumentative job: expose a mismatch, define a model or boundary, show a causal workflow, or test a claim.
- Repair data truth, scale, normalization, uncertainty, missing cases, and comparable conditions before layout.
- Make the caption identify the object and setting, state the supported takeaway, and preserve the material boundary.
- Keep semantic encodings consistent across in-scope visuals; ensure the rendered result remains legible without using aspect compression to manufacture an effect.
- Modify underlying data or analysis only when explicitly authorized for a scientific correction. Any changed output makes dependent prose unverified until rerun and checked.

## Venue and submission material

Fetch the current official call and instructions for the named venue, cycle, and track before revising policy or formatting content. Separate hard compliance from general writing practice. Preserve accurate anonymity, ethics, overlap, AI-use, artifact, supplement, and implementation disclosures.

A venue mismatch that changes the contribution, audience, evidence, or paper length is an author decision rather than a wording repair.

## Delete or demote safely

Delete or move material down the reading path when it is true but does not change the thesis, a required premise, a decisive mechanism/finding, evidence credibility, or a material boundary. Common candidates are repeated definitions, implementation chronology, incidental optimizations, unqueried plots, duplicate results, and prose that only announces document structure.

Retain negative evidence, limitations, attribution, assumptions, and reviewer-relevant costs near the claims they constrain. Report any deletion or reframing that materially changes what the author foregrounds.
