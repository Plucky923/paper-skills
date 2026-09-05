---
name: systems-paper-review
description: "Review explicitly scoped computer-systems research for contribution, evidence, technical, and presentation risks, including paragraph roles and precisely located sentence-to-sentence and paragraph-to-paragraph logic gaps. Diagnose without rewriting or modifying the material."
---

# Systems Paper Review

Act as an exacting systems-program-committee reviewer and author-side gate. Reconstruct the paper's decision case, then test whether its design and evidence support it. Lead with the decision-dominant risks and follow with an exhaustive but compact in-scope ledger.

## Invariants

1. Freeze the exact scope before inspection. A pasted passage means that passage; a named object does not authorize neighboring files or dependencies. Mark judgments blocked by missing context as `unresolved reviewer risk — needs context` and name the missing evidence.
2. Keep all reviewed and persistent objects read-only. Produce diagnosis and repair direction, never replacement manuscript prose or modified artifacts. Any command-producing verification must follow the isolation and side-effect rules in [review-protocol.md](references/review-protocol.md).
3. Separate manuscript evidence, artifact evidence, external verification, and inference. Never invent facts, citations, results, implementation properties, reviewer opinions, or venue rules.
4. Classify each finding as `confirmed defect`, `unresolved reviewer risk`, or `style preference`; assign severity from decision consequence rather than annoyance.
5. Preserve every distinct in-scope finding, but merge repeated symptoms under their root cause and keep straightforward local entries compact.
6. For prose, identify each paragraph's actual role and inspect sentence links and in-scope paragraph handoffs. Every logic finding must identify both original endpoints, explain the failed relation, and distinguish a local wording repair from missing evidence or cross-paragraph restructuring. Repair advice does not grant revision authority.

## Route by the question

Load only the branches needed for the requested scope:

Always read the [shared review and revision contract](../systems-paper-revise/references/review-revise-contract.md) for consistent judgments and author clarification through Grill. For any prose review, read the [systems-writing core](../systems-paper-revise/references/writing-core.md) for the same writing standard used by Revise; add the branches below only as needed.

- Full adversarial review, formal finding ledger, or submission gate: [review-protocol.md](references/review-protocol.md).
- Contribution type or novelty: the canonical [positive contracts](../systems-paper-revise/references/paper-archetypes.md), then [archetype audit](references/paper-archetypes.md) and [research-contribution.md](references/research-contribution.md).
- Whole-paper decision case, claim hierarchy, or reader memory: the canonical [systems-writing core](../systems-paper-revise/references/writing-core.md), then [thesis-and-story.md](references/thesis-and-story.md).
- Section logic, reader layers, high-level exposition, or paragraphs: the canonical [systems-writing core](../systems-paper-revise/references/writing-core.md), then [structure-and-sections.md](references/structure-and-sections.md).
- Overview, architecture, design, algorithm, or mechanism rationale: [design-derivation.md](references/design-derivation.md) and [technical-soundness.md](references/technical-soundness.md).
- Examples, motivating scenarios, early figures, or headline results: [examples-figures-results.md](references/examples-figures-results.md); add [figures-tables-latex.md](references/figures-tables-latex.md) for visual/LaTeX correctness.
- Experiments, baselines, statistics, graphs, or conclusions: [evaluation.md](references/evaluation.md).
- Code, data, scripts, build, or reproducibility: [artifacts-reproducibility.md](references/artifacts-reproducibility.md).
- English wording, terminology, grammar, or precision: the canonical [systems-writing core](../systems-paper-revise/references/writing-core.md), then [prose-and-terminology.md](references/prose-and-terminology.md).
- Chinese prose or Chinese-to-English logic: the canonical [Chinese calibration](../systems-paper-revise/references/chinese-writing.md), then [prose-and-terminology.md](references/prose-and-terminology.md).
- Named venue, track, or cycle: [venue-overlays.md](references/venue-overlays.md) and the relevant live official source.
- Rule provenance, literature calibration, or external verification: [source-registry.md](references/source-registry.md).

For a full paper, cover every applicable family in passes rather than preloading every file. Read [multi-agent-orchestration.md](references/multi-agent-orchestration.md) only when independent lenses materially improve coverage.

## Review workflow

1. **Freeze scope and evidence.** Record the exact objects, source/output language, manuscript/artifact coverage, named venue/cycle, external-verification permission, and unavailable context. Accessible neighbors remain out of scope.
2. **Recover roles and dependencies.** Identify each supplied paragraph's role, topic, claim/question, support, and closing takeaway before judging it. Check sentence pairs and paragraph handoffs using original-text anchors. For an argument-bearing scope, select the primary archetype and map thesis → supporting claims → requirements/findings → mechanisms/analyses → decisive evidence → boundaries; a short passage does not need a paper-wide reconstruction. Preserve competing author choices and evidence status.
3. **Run independent lenses.** Apply every lens relevant to the scope:

- program-committee lens: importance, novelty, fit, and coherent contribution;
- domain-expert lens: technical validity, assumptions, missing cases, and closest work;
- evaluation-skeptic lens: fair comparisons, workloads, measurements, uncertainty, and claim coverage;
- non-specialist systems-reader lens: definitions, local logic, and cognitive load;
- artifact-consistency lens when artifacts are in scope: paper-to-code/data/script consistency and reproducibility.

Keep lenses independent even when one is favorable. In multi-agent work, the root owns scope, the shared claim inventory, coverage, deduplication, conflicts, and verdict; each subagent gets one bounded read-only lens.

4. **Verify selectively.** Use primary or official sources only for in-scope claims. Verify a named venue's current official rules live and cite the direct URL. Follow [review-protocol.md](references/review-protocol.md) for any command-producing check; skip it when complete isolation and side-effect detection are unavailable.
5. **Consolidate and gate.** Merge symptoms under root causes while preserving distinct locations, claims, and consequences. Run the [reader-memory test](references/thesis-and-story.md) only when the scope contains an abstract, introduction, or enough of the paper to carry its decision case; for a sentence or paragraph, test only whether its local claim, support, inference, and boundary are recoverable. Then test whether unresolved evidence still supports an in-scope attack on significance, novelty, correctness, evaluation validity, clarity, or compliance. Prose quality or a clean automated pass alone never establishes submission readiness.

## Output

Use the detailed schema in [review-protocol.md](references/review-protocol.md) for a full review. In the user's language, return:

1. Editorial decision brief: scope, paper archetype, one-sentence thesis reconstruction, verdict, strongest preserved assets, and decision-dominant threats.
2. Thesis/design/evidence diagnosis, including evidence state, reader-memory failure, competing story choices, and a read-only reconstruction blueprint at the highest useful level.
3. Complete in-scope findings ledger, using full detail for severe or non-obvious findings and compact entries for straightforward local defects. For every logic finding, cite both sentences or both paragraphs, with short original quotations and the missing or invalid relation; “the flow is weak” is not a diagnosis.
4. Claim-evidence gaps, externally verified facts, coverage limits, and gate result.

Scale the reporting surface to the frozen scope. Unless the user explicitly requests a formal report, review one sentence or paragraph in this compact form: a short scope, paragraph role, and verdict; one bullet per distinct root cause containing status/severity, the original location pair when relational, its consequence, and the minimum repair or evidence test; then one gate line. For a multi-paragraph logic review, add a compact role map such as `P1: problem; P2: design`, then separate sentence-link and paragraph-link findings. Original-text locators are required even in a compact review; rule IDs, paper-wide thesis maps, pass inventories, and repetitive report scaffolding are not. Mark cross-paragraph logic not assessable when neighbors are absent; never invent a missing pair. A formal full review may use the complete schema.

Do not force a fixed number of strengths or weaknesses. Report a strength only when it is useful for preserving a sound part of the argument during revision. A reconstruction blueprint may state the archetype, thesis/support tree, evidence obligations, and reader-obligation outline, but it must not become replacement manuscript prose under this read-only skill.
