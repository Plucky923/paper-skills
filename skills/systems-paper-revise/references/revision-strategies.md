# Structural Revision Strategies

Use this reference when a defect spans several sentences, sections, claims, or evidence objects. Diagnose the root cause before selecting a repair; apply the positive prose standard in [writing-core.md](writing-core.md) after the scientific structure is sound.

The paragraph-local contract in [revision-protocol.md](revision-protocol.md) controls existing prose. Use the strategies below to diagnose needed work; perform cross-paragraph movement, splitting, merging, content expansion, or reframing only under an explicit author restructuring request. A supplied whole paper or review finding is not that permission.

## Choose the repair

Ask:

1. What claim or reader obligation fails?
2. Is it false or unsupported, missing a premise, organized around the wrong dependency, expressed at the wrong level, or merely unclear?
3. Which support already exists inside scope or in a permitted verified source?
4. Can the root cause be repaired inside the affected original paragraph without changing its purpose or adding content?
5. Could that change create a new promise, contradiction, or author-intent choice elsewhere in scope?

A paragraph-local repair may clarify or reorder that paragraph's supported propositions and make their existing relation explicit. If the repair needs broader authority or new evidence, identify the exact sentence or paragraph dependency and stop that repair.

Authority must match the repair. Restructuring permission changes placement, not scientific claim strength. For existing prose, a missing premise or unsupported claim remains an author decision even during restructuring. Depending on the explicit request, a repair may:

- correct a proposition from authoritative evidence;
- expose an inference already warranted by established premises;
- reorganize supported material around its dependencies;
- narrow or delete a claim when the author explicitly authorizes that scientific correction;
- add supported content required to complete the local argument.

When none applies, state the evidence, source, context, or author decision required. Prose alone cannot repair that gap.

## Rebuild only with explicit author authority

These conditions can justify proposing a rebuild, not performing one without an explicit author request:

- no single controlling thesis explains the scoped material;
- the prose follows a contribution contract different from the evidence it offers;
- major mechanisms or analyses do not derive from visible requirements;
- headline evidence does not test the main claim;
- local repairs preserve contradictory promises across the scope.

For an authorized rebuild, first choose the positive contract in [paper-archetypes.md](paper-archetypes.md). Then build only the necessary internal maps:

```text
controlling thesis
  → supporting claim or finding
  → reason, mechanism, or method
  → decisive evidence
  → boundary and failure consequence
```

Use a design-derivation map or claim-evidence map only when that relation is actually broken. At paragraph scale, repair directly from the local obligation instead of constructing a paper-wide model.

## Contribution and positioning

- Recover actor, setting, failure or unknown, and consequence from existing evidence. Flag unsupported prevalence or impact; changing the importance claim requires an author decision.
- Check the exact change in assumption, boundary, capability, guarantee, cost, or evidence relative to prior work. An open-world superlative needs support or an author-authorized correction, not a silently substituted bounded claim.
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
- Check conclusions against evaluated workloads, hardware, scale, data, failure model, and implementation status. Flag an exceeded boundary; changing an existing scientific conclusion requires author authorization.
- Add a robustness or ablation result only when expansion is authorized, the evidence exists, and the corresponding claim requires it. Otherwise expose the evidence gap; narrow an existing claim only with explicit author authorization.
- Treat negative results, failure regions, and plausible alternative explanations as scientific information rather than prose to hide.

## Section and attention repair

When section restructuring is explicitly requested, use the section contracts in [writing-core.md](writing-core.md) and reallocate attention according to novelty and uncertainty:

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

Under an explicit deletion or restructuring request, remove or move material only when it does not change the thesis, a required premise, a decisive mechanism/finding, evidence credibility, or a material boundary. In paragraph-local revision, remove redundant wording rather than substantive content, and report any placement issue separately.

Retain negative evidence, limitations, attribution, assumptions, and reviewer-relevant costs near the claims they constrain. Report any deletion or reframing that materially changes what the author foregrounds.
