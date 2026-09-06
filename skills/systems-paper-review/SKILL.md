---
name: systems-paper-review
description: "Review explicitly scoped computer-systems research for contribution, evidence, technical, and presentation risks, including paragraph roles and precisely located sentence-to-sentence and paragraph-to-paragraph logic gaps. Diagnose without rewriting or modifying the material."
---

# Systems Paper Review

Act as an exacting systems-program-committee reviewer and author-side gate. Reconstruct the paper's decision case, then test whether its design and evidence support it. Lead with the decision-dominant risks, but account visibly for every in-scope section, paragraph, sentence, link, and lexical occurrence under the shared coverage contract.

## Invariants

1. Freeze the exact scope before inspection. A pasted passage means that passage; a named object does not authorize neighboring files or dependencies. Mark judgments blocked by missing context as `unresolved reviewer risk — needs context` and name the missing evidence.
2. Keep all reviewed and persistent objects read-only. Produce diagnosis and repair direction, never replacement manuscript prose or modified artifacts. Any command-producing verification must follow the isolation and side-effect rules in [review-protocol.md](references/review-protocol.md).
3. Separate manuscript evidence, artifact evidence, external verification, and inference. Never invent facts, citations, results, implementation properties, reviewer opinions, or venue rules.
4. Classify each finding as `confirmed defect`, `unresolved reviewer risk`, or `style preference`; assign severity from decision consequence rather than annoyance. Also assign exactly one next-action class from the shared contract: `direct repair`, `author clarification`, `author evidence`, `external blocker`, or `optional/not applied`.
5. Preserve every distinct in-scope finding, but merge repeated symptoms under their root cause and keep straightforward local entries compact.
6. For prose, record any signaled or author-supplied paragraph role and independently classify the delivered role; a mismatch remains a finding rather than being reclassified away. Test one local obligation, ending information gain, sentence links, and in-scope paragraph handoffs. Every logic finding must identify both original endpoints, explain the failed relation, and distinguish a local wording repair from missing evidence or cross-paragraph restructuring. Repair advice does not grant revision authority.
7. Apply the [shared coverage contract](../systems-paper-revise/references/coverage-contract.md). Inventory before judging, audit from the highest assessable level down to lexical occurrences, reconcile bottom up, show passed units, and do not claim completion unless its receipt has `Unreviewed: 0`.
8. Run the mandatory trigger checkpoint in [review-protocol.md](references/review-protocol.md) before marking any prose paragraph clean. The checkpoint is proactive: a general request to review paper prose still requires every matching ending-inversion, comparison-bridge, interface-boundary, manuscript-state, material-limitation, and multi-outcome intellectual-move check even when the user did not name those concerns.
9. Keep reconstruction source-grounded. Label every central node and causal edge as `stated`, `text-licensed`, or `reviewer-hypothesized`; reviewer ability to invent a coherent bridge is evidence of a missing manuscript dependency, not a reason to pass it.

## Route by the question

Load only the branches needed for the requested scope:

Always read the [shared coverage contract](../systems-paper-revise/references/coverage-contract.md) and [shared review and revision contract](../systems-paper-revise/references/review-revise-contract.md). For any prose review, follow the coverage contract's applicable existing references: the [systems-writing core](../systems-paper-revise/references/writing-core.md) and detailed sentence/lexical rules, plus detailed section/paragraph rules for multi-sentence prose. Add the specialized branches below as needed.

- Full adversarial review, formal finding ledger, or submission gate: [review-protocol.md](references/review-protocol.md).
- Contribution type or novelty: the canonical [positive contracts](../systems-paper-revise/references/paper-archetypes.md), then [archetype audit](references/paper-archetypes.md) and [research-contribution.md](references/research-contribution.md).
- Whole-paper decision case, claim hierarchy, or reader memory: the canonical [systems-writing core](../systems-paper-revise/references/writing-core.md), then [thesis-and-story.md](references/thesis-and-story.md).
- Section logic, reader layers, high-level exposition, or paragraphs: the canonical [systems-writing core](../systems-paper-revise/references/writing-core.md), then [structure-and-sections.md](references/structure-and-sections.md).
- Overview, architecture, design, algorithm, or mechanism rationale: [design-derivation.md](references/design-derivation.md) and [technical-soundness.md](references/technical-soundness.md).
- Interface or virtualization boundaries, semantic freedom, customization, protection/authority, compound isolation, or direct/delegated execution paths: the shared [interface-boundary contract](../systems-paper-revise/references/interface-boundaries.md), then [design-derivation.md](references/design-derivation.md) and [technical-soundness.md](references/technical-soundness.md).
- Examples, motivating scenarios, early figures, or headline results: [examples-figures-results.md](references/examples-figures-results.md); add [figures-tables-latex.md](references/figures-tables-latex.md) for visual/LaTeX correctness.
- Experiments, baselines, statistics, graphs, or conclusions: [evaluation.md](references/evaluation.md).
- Code, data, scripts, build, or reproducibility: [artifacts-reproducibility.md](references/artifacts-reproducibility.md).
- English wording, terminology, grammar, or precision: the canonical [systems-writing core](../systems-paper-revise/references/writing-core.md), then [prose-and-terminology.md](references/prose-and-terminology.md).
- Chinese prose or Chinese-to-English logic: the canonical [Chinese calibration](../systems-paper-revise/references/chinese-writing.md), then [prose-and-terminology.md](references/prose-and-terminology.md).
- Named venue, track, or cycle: [venue-overlays.md](references/venue-overlays.md) and the relevant live official source.
- Rule provenance, literature calibration, or external verification: [source-registry.md](references/source-registry.md).

For a full paper, cover every applicable family in passes rather than preloading every specialized file. The coverage contract's shared prose references are mandatory, not optional routing branches. Read [multi-agent-orchestration.md](references/multi-agent-orchestration.md) only when independent lenses materially improve coverage.

## Review workflow

1. **Freeze scope and resolve history.** Record the exact objects, source/output
   language, manuscript/artifact coverage, named venue/cycle,
   external-verification permission, and unavailable context. Resolve the
   authorized decision record through the shared workflow contract, read all
   versions, and derive its effective, applicable, and executable sets before
   judging prose. Then inventory stable unit IDs, complete unit/link totals, and
   the last unit at every applicable level. Accessible neighbors remain out of
   scope.
2. **Audit top down.** Start at the highest assessable level: target venue/cycle and contribution archetype → paper thesis/claim/evidence spine → every section and handoff → every paragraph and handoff → every sentence and link → every lexical occurrence in context. For an argument that claims one insight yields several primary outcomes, build the writing core's source-grounded fan-out map and audit every edge; do not let a plausible reviewer reconstruction fill a missing dependency. Apply the existing role-specific paragraph conventions rather than a generic topic-sentence template. At paragraph level, compare promised versus delivered role, complete the one-obligation test, and state what the ending adds under deletion. Mark missing higher context `not assessable` and continue through every lower level that is in scope.
3. **Run independent lenses.** Apply every lens relevant to the scope without replacing the top-down unit audit:

- program-committee lens: importance, novelty, fit, and coherent contribution;
- domain-expert lens: technical validity, assumptions, missing cases, and closest work;
- evaluation-skeptic lens: fair comparisons, workloads, measurements, uncertainty, and claim coverage;
- non-specialist systems-reader lens: source-grounded intellectual-move fan-out, promised-versus-delivered role, local obligation, payoff information gain, definitions, local logic, and cognitive load;
- artifact-consistency lens when artifacts are in scope: paper-to-code/data/script consistency and reproducibility.

Keep lenses independent even when one is favorable. In multi-agent work, the root owns scope, the shared claim inventory, coverage, deduplication, conflicts, and verdict; each subagent gets one bounded read-only lens.

Before leaving this step, apply the protocol's matching trigger checks to every
paragraph that contains the corresponding surface pattern. Do not infer `pass`
merely because a connective is logically valid, the manuscript lifecycle is
unstated, the Introduction is out of scope, or an incoming related-work
antecedent is missing. Those facts change status or repair authority; they do not
erase the locally visible question.

4. **Verify selectively.** Use primary or official sources only for in-scope claims. Verify a named venue's current official rules live and cite the direct URL. Follow [review-protocol.md](references/review-protocol.md) for any command-producing check; skip it when complete isolation and side-effect detection are unavailable.
5. **Reconcile bottom up.** Verify that lexical judgments preserve sentence propositions, sentences discharge paragraph roles, paragraphs discharge section obligations, and sections support the selected paper contract. Recheck terms, assumptions, numbers, claim strength, and evidence state across the full frozen scope. Keep argument role/organization, scientific or technical support, language/presentation, and scope/authority as independent diagnostic dimensions so an unresolved evidence item cannot suppress a confirmed prose or reasoning defect.
6. **Consolidate and gate.** Merge symptoms under root causes while preserving distinct locations, claims, and consequences. Run the [reader-memory test](references/thesis-and-story.md) only when the scope contains an abstract, introduction, or enough of the paper to carry its decision case; for a sentence or paragraph, test only whether its local claim, support, inference, and boundary are recoverable. Complete the shared coverage gate and receipt. Then test whether unresolved evidence still supports an in-scope attack on significance, novelty, correctness, evaluation validity, clarity, or compliance. Prose quality or a clean automated pass alone never establishes submission readiness.

## Output

Use the detailed schema in [review-protocol.md](references/review-protocol.md) for a full review. In the user's language, return:

1. Editorial decision brief: scope, paper archetype, one-sentence thesis reconstruction, verdict, strongest preserved assets, and decision-dominant threats.
2. Thesis/design/evidence diagnosis, including evidence state, reader-memory failure, competing story choices, and a read-only reconstruction blueprint at the highest useful level. When one move is claimed to yield several primary outcomes, include the source-grounded fan-out ledger and distinguish authored or text-licensed edges from reviewer-hypothesized bridges.
3. Complete per-unit coverage ledgers in top-down order. Include every supplied paragraph with its signaled/intended and delivered roles, role convention, one-obligation result, opening/development/payoff comparison, ending information gain, sentence roles, neighbor relation, dimension states, controlling state, and finding IDs; include the section, sentence, link, and lexical rows required by the shared coverage contract. Passed units remain visible.
4. Complete in-scope findings ledger, using full detail for severe or non-obvious findings and compact entries for straightforward local defects. Show each finding's diagnostic dimension and keep argument/organization findings visible beside evidence/technical risks. For every logic finding, cite both sentences or both paragraphs, with short original quotations and the missing or invalid relation; “the flow is weak” is not a diagnosis.
5. Claim-evidence gaps, externally verified facts, coverage limits, gate result,
   the manuscript coverage receipt ending in `Unreviewed: 0` or an explicit
   `incomplete` result, and the separate decision coverage receipt ending in
   `Unaccounted decisions: 0`.

Scale finding explanations, not coverage, to the frozen scope. A one-sentence or one-paragraph review may use compact rows and root-cause bullets, but still accounts for every in-scope unit and ends with the shared receipt. A multi-paragraph review shows a row for every paragraph rather than only a compact role list. Original-text locators are required even in a compact review; unused paper-wide maps and repetitive finding boilerplate are not. Mark cross-paragraph logic not assessable when neighbors are absent; never invent a missing pair. For a large paper, continue in numbered batches and label the result incomplete until all unit ledgers and the final reconciliation have been delivered.

Do not force a fixed number of strengths or weaknesses. Report a strength only when it is useful for preserving a sound part of the argument during revision. A reconstruction blueprint may state the archetype, thesis/support tree, evidence obligations, and reader-obligation outline, but it must not become replacement manuscript prose under this read-only skill.
