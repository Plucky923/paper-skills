# Revision Strategies by Root Cause

Use this map when a writing problem is structural or spans multiple findings. Choose a strategy from the root cause and available evidence, not from surface symptoms. Structural and claim repairs precede prose polishing.

## Strategy selection

For any finding, ask in order:

1. Is the claim true and supported under the stated conditions?
2. Is the support already inside the editable scope or an allowed verified source?
3. Is the problem missing evidence, missing reasoning, poor organization, ambiguous language, or incorrect formatting?
4. What is the smallest coherent scope that closes the root cause without changing author intent: phrase, sentence, paragraph, section, or the full authorized argument?
5. Could the change create a contradiction or new promise elsewhere in scope?

Use one of five evidence-safe moves:

- **Add supported content** already available in scope/verified source.
- **Expose reasoning** that is implicit but logically warranted.
- **Reorganize** existing content around dependencies.
- **Calibrate/delete a claim** that exceeds support.
- **Block** when new evidence or author intent is required.

Use a global in-scope rebuild when the sibling review cannot recover one controlling thesis, the paper follows the wrong archetype contract, mechanisms do not derive from requirements, decisive evidence does not support the primary claims, or local edits retain contradictory section promises. Build the archetype route, thesis-support tree, design-derivation map, and headline-evidence map before rewriting. Otherwise keep the repair local.

## Contribution and positioning (`RC`)

### Missing problem/significance (`RC-01`, `RC-02`)

- Extract actor, setting, failure/cost, and consequence from existing evidence.
- Replace adjectives with measurable or categorical consequences.
- If prevalence/impact is absent, narrow to the observed setting or mark `B1/B2`.
- Do not invent a motivating anecdote, user population, or scale.

### Unclear central idea/co-design (`RC-03`, `RC-08`, `RC-10`)

- Write an internal causal skeleton at the principle level: binding constraint → observation/leverage → changed abstraction or action → resulting property/tradeoff.
- State that principle before the realization, then reorder components by how they instantiate it.
- Connect each component to one challenge/design choice; demote incidental optimizations.
- If several contribution hierarchies are equally valid, mark `B4` rather than choosing the most marketable one.

### Weak or risky novelty (`RC-05`, `RC-06`, `RC-07`, `RC-14`)

- Compare on exact problem, assumption, mechanism, capability, and evidence—not adjectives.
- Replace open-world superlatives with a bounded, verifiable delta.
- Group related work by decision-relevant dimension.
- If the closest work has not been verified, retain `B2`; never manufacture a distinction.

### Maturity/generality mismatch (`RC-09`, `RC-11`, `RC-16`)

- State prototype/simulation/deployment boundary and supported environments.
- Move material assumptions/limitations adjacent to the affected claim.
- Replace universal transfer with tested instances plus transfer conditions.

## Technical soundness (`TS`)

### Missing model/assumptions (`TS-01`–`TS-03`)

- Introduce actors, resources, trust/fault/workload boundaries before mechanism.
- Make each assumption testable: who establishes it, how detected, failure behavior.
- If model choice changes the actual research goal, mark `B4`.

### Vague mechanism/lifecycle (`TS-04`–`TS-06`)

- Rewrite each stage as input/state → operation → output → property.
- Add start/stop/update/recovery conditions from existing design evidence.
- Replace `ensure/guarantee` with the exact invariant and enforcement point—or calibrate to observed behavior.
- A polished overview cannot replace missing algorithm/implementation evidence; use `B1/B3`.

### Missing concurrency/failure/edge behavior (`TS-07`–`TS-09`)

- Add known ordering, synchronization, fault handling, and boundary cases.
- Separate excluded cases from handled cases and state fail-open/fail-closed behavior.
- If behavior is unknown or untested, do not improvise; narrow claim or block.

### Unjustified choice/cost/scale (`TS-10`–`TS-12`)

- State objective and constraints, then compare credible alternative and tradeoff.
- Put shifted/offline/setup/operator costs in the same accounting story as benefits.
- Bound scale to tested/analyzed range and name limiting resource.

### Implementation/security/consistency (`TS-13`–`TS-17`)

- Expose privilege and new attack surface only from supported evidence.
- Separate design from implemented/emulated/simulated/future parts.
- Reconcile prose, figure, equation, pseudocode, and example against one source of truth.
- When sources disagree, do not choose silently; mark blocker.

## Evaluation (`EV`)

### Broken claim-to-evidence map (`EV-01`–`EV-03`)

- Organize evaluation around recoverable scientific questions and falsifiable claims. Questions may be expressed through prose or an interleaved finding/intervention structure rather than an enumerated RQ list.
- State what each experiment can and cannot establish.
- If design is observational, remove unsupported causal language.
- If a central claim has no evidence, add `B1`; prose cannot close it.

### Baseline/workload fairness (`EV-04`–`EV-07`)

- Add available configuration/version/resource/tuning detail.
- Justify baseline exclusion with verified facts; otherwise narrow comparison.
- Bound results to tested workloads/data split.
- Never describe an unrun baseline or held-out experiment as completed.

### Metric/boundary/procedure (`EV-08`–`EV-11`)

- Define metric, unit, numerator/denominator, aggregation, and objective relation.
- Make timing/resource boundaries explicit, including preprocessing and amortization.
- Add known warmup/cache/run-order/environment controls.
- Missing measurement metadata is `B1/B3` when not in evidence.

### Uncertainty and analysis (`EV-12`, `EV-13`, `EV-20`)

- Add repetitions, distribution, intervals/effect size only from actual data.
- Distinguish independent samples from repeated reads.
- Replace false precision and `significant` rhetoric with supported absolute/relative context.
- Do not invent error bars or run a new statistical analysis unless data and authorization are in scope.

### Mechanism, robustness, negative results (`EV-14`–`EV-19`)

- Link end-to-end result to practical claim and micro/ablation evidence to causal attribution.
- Require ablation only when component attribution is claimed.
- State operating range, failures, missing cases, and plausible alternative explanations.
- Replace causal story with hypothesis when diagnostic evidence is absent.

### Reproducibility and conclusion (`EV-21`, `EV-22`)

- Add available environment/procedure/provenance.
- Align conclusion with tested population/conditions.
- Keep restricted-data/hardware limitations explicit.

## Structure (`SS`)

### Global flow (`SS-01`–`SS-06`)

- Select the primary contract from the sibling `paper-archetypes.md` before building an argument spine. A mechanism paper may use reader/setting → consequential problem → binding constraint → intellectual move → requirements → mechanisms → evidence → bounded implication; empirical and operational papers require their own positive contracts.
- Build an abstraction ladder for every central idea: constraint → leverage → action/change → resulting property or tradeoff. A high-level sentence must explain this causal relation; component names and operation sequences belong below it. Reject a sentence that is interchangeable across unrelated systems, cannot predict the need for the major mechanisms, or hides the condition/boundary of the resulting property.
- Move definitions before substantive use; delete unused terminology.
- Separate overview (model/workflow) from design (mechanism/rationale) and implementation (realization/status).
- Add cross-references only where retrieval is genuinely costly.

### Paragraphs/lists (`SS-07`–`SS-11`, including `SS-09A`)

- Write each paragraph's local reasoning obligation; label support, mechanism, evidence, qualification, and transition.
- Draft or inspect the first/last-sentence pair before polishing the middle: the opening makes the local promise, while the ending gives the supported answer, implication, boundary, or next necessary question. Do not append a redundant summary when the logical close is already clear.
- Split independent claims; merge fragments; order prerequisite before consequence and evidence before the inference it licenses.
- Delete any middle sentence whose removal loses no inference, definition, evidence, boundary, or necessary handoff.
- Make bullets parallel along one dimension.
- Do not optimize rendered line count at the expense of logic.

### Abstract/introduction (`SS-12`–`SS-14`)

- Preserve the shortest complete decision case required by the selected archetype. Judge functions, not fixed sentence order, explicit contribution bullets, or use of the word `insight`.
- Remove low-level detail before removing a required causal link.
- Cross-check every abstract number/superlative with evidence.
- Do not force a fixed sentence or paragraph count.

### Background through conclusion (`SS-15`–`SS-24`)

- Background: keep only prerequisites used later.
- Motivation/related work: group fairly by mechanism/assumption and expose precise gap.
- Overview: state model/workflow/insight, not implementation minutiae.
- Design: state input/state/action/output/rationale/lifecycle.
- Implementation: state what is actually built and reused.
- Evaluation: answer questions with evidence and bounded interpretation.
- Discussion: keep material limitations and adoption costs visible.
- Conclusion: synthesize supported lessons; delete new claims.

### Examples, figures, and headline results (`ER`, `TH-05`–`TH-08`)

- Preserve or introduce a running example only when it executes a difficult inference, exposes an exact failure boundary, or makes mechanism interaction cheaper to understand.
- Give each early figure one argumentative job: reveal a mismatch/boundary, define the model, show a causal path/workflow, or visualize the intellectual move. Do not add a diagram merely because successful papers often have one.
- Align abstract/introduction headline results with the thesis-support hierarchy. Keep the condition, comparison, uncertainty/scope, and implication attached to each decisive result.
- Move enough motivation evidence before the requirement it licenses; leave full methodology and secondary results later.
- Allocate attention to novelty and uncertainty. Compress commodity background, implementation inventory, repeated motivation, and results that do not alter the decision case.

## Prose and terminology (`PT`)

- Create a canonical glossary before changing repeated technical words.
- Define only terms the intended reader needs; keep definitions local and nonrecursive.
- Reduce each difficult sentence to actor → action → object/property, plus only the condition or qualification needed to interpret it. Put that main relation before secondary clauses.
- Replace generic verbs and nominalizations with the exact operation or relation: what maps, isolates, defers, constrains, measures, compares, or causes what. Do not use `enables`, `supports`, `addresses`, or `improves` without naming the capability, mechanism, or metric.
- Keep one principal assertion per sentence. Resolve modifier, pronoun, negation, comparison, coordination, and condition scope before shortening.
- Link sentences through given information → new proposition. Add `therefore`, `however`, or causal language only when the stated premises entail that relation.
- Replace vague quantifiers and loaded adjectives only when the exact supported quantity/property is available; otherwise delete or qualify. Calibrate epistemic verbs to evidence.
- Delete metadiscourse, repeated setup, and sentences that add no necessary reasoning role. Preserve exact technical repetition when a synonym would change or blur meaning.
- Use active/passive and `we` according to agency, not a blanket ban.
- Follow source language and venue style for tense, number spelling, punctuation, and abbreviations.

## Figures, tables, and LaTeX (`FL`)

- Repair data truth and encoding before aesthetics.
- Preserve values, uncertainty, missing cases, scale, normalization, and comparable conditions.
- Make captions/callouts state the object and supported takeaway.
- Standardize semantic encodings across in-scope figures.
- Redesign density/size for final rendering; do not use `\resizebox` or aspect compression as an automatic fix.
- Preserve citation keys, labels, macros, math, environments, and project/template conventions.
- Compile and visually inspect only when the complete relevant source is in scope.

## Artifact findings (`AR`)

- Do not edit artifacts unless explicitly authorized and in scope.
- Documentation fixes may expose version, setup, commands, resources, provenance, and expected output already known.
- Missing code/data/results, broken scientific behavior, or paper-artifact mismatch is not a prose-only fix.
- If code/script correction changes outputs, mark manuscript numbers and conclusions unverified until experiments are rerun and audited.
- Never alter data, exclusion rules, or scripts to force agreement with the paper.

## Venue findings (`VO`)

- Fetch current official rule before editing format/policy content.
- Separate hard compliance from recommendation.
- Use official template and rendered PDF for format checks.
- Preserve accurate anonymity, ethics, overlap, AI-use, artifact, and supplement disclosures.
- A venue mismatch may require a target decision (`B4`), not rhetorical reframing alone.

## When deletion is the best revision

Delete or demote content when it is:

- unsupported and nonessential;
- a redundant claim/definition/detail;
- an optimization unrelated to central co-design;
- a plot/table with no research question;
- a superlative that cannot be bounded;
- speculation presented as explanation;
- future work presented as current contribution;
- a style flourish that raises cognitive cost.

Deletion is unsafe if it hides negative evidence, limitations, attribution, assumptions, or reviewer-relevant costs.

## Blocker wording

Use precise internal blocker records:

```text
Blocked claim/location:
Finding/rule:
Why text alone cannot solve it:
Required item: experiment | raw data | implementation fact | source | context | author choice
Minimum resolution test:
Safe interim claim, if any:
```

Do not insert this diagnostic text into the manuscript unless the user asks for TODO annotations.

## Sources

Strategies map directly to the sibling `systems-paper-review` rule IDs and the evidence-safe workflow in this skill. They also synthesize staged revision approaches from [YSLAB-REVISION], [SIMCHOWITZ-WRITING], and [BRANDON-EVIDENCE]. Source keys are defined in the sibling registry. Last reconciled 2026-09-03.
