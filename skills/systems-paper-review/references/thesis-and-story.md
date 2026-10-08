# Thesis, Claim Hierarchy, and Reader Memory

First, read the [systems-writing core](../../systems-paper-revise/references/writing-core.md) and [positive contracts](../../systems-paper-revise/references/paper-archetypes.md). This file gives decision-case checks within scope. It adds reviewer attacks and diagnostic maps. It does not give another writing model.

## TH-01 — The paper has one controlling thesis

- **Check:** Find the consequential problem or question, failed assumption or limiting tension, intellectual move, capability or finding, decisive evidence, and boundary. The thesis can use multiple sentences. It fails if reconstruction makes a choice between incompatible stories or a component list necessary.
- **Reviewer attack:** “I understand what was built, but not the proposition this paper asks me to believe.”
- **Severity:** `S1`. Use `S2` when the thesis exists but is difficult to find.
- **Exception:** A measurement or experience paper can have a finding or lesson as its central contribution.

## TH-02 — Supporting claims form a hierarchy

- **Check:** Make a tree with one controlling thesis and a small set of supporting claims related to the decision. Add their mechanisms or analyses. Add evidence for each claim. Keep primary contributions, enabling engineering, implementation facts, and incidental optimizations as different levels in the tree.
- **Reviewer attack:** “The contribution list is flat, so I cannot tell which failure would invalidate the paper.”
- **Severity:** `S1` when the ambiguity controls the central case. For other cases, `S2`.
- **Exception:** No fixed claim count applies. Only distinctions that show the thesis-invalidating failure are necessary in the hierarchy.

## TH-03 — The thesis predicts the design

- **Check:** Hide component names. Find the requirements that result from the paper's problem and intellectual move. Make sure that the primary mechanisms in the paper satisfy them. For each central node and dependency, give the writing core's source status. Keep a reviewer-supplied requirement as a missing edge. A central idea without a relation to the design is usually a slogan or retrospective summary.
- **Reviewer attack:** “The claimed insight could introduce many unrelated systems and does not explain this design.”
- **Severity:** `S1`.

## TH-03A — Reviewer reconstruction does not show authored clarity

- **Check:** Write the shortest coherent thesis in reviewer language. Compare each node and edge with original anchors. If one move supposedly causes multiple primary outcomes, use the [source-grounded fan-out test](../../systems-paper-revise/references/writing-core.md#source-grounded-intellectual-move-fan-out). Record each reviewer-hypothesized bridge. Do not use a full reviewer reconstruction as evidence for manuscript clarity.
- **Reviewer attack:** “The reviewer can invent a strong story for this system, but the paper does not actually make that story available to the reader.”
- **Severity:** `S1` when the missing edge controls the contribution. For other cases, `S2`.

## TH-04 — The thesis predicts the decisive evidence

- **Check:** Before the evaluation, find the observations that would show or contradict the central thesis. Compare them with headline results. Large evidence quantity does not replace a missing decisive test.
- **Reviewer attack:** “The paper evaluates what is easy to measure, not what its thesis requires.”
- **Severity:** `S0` for a central conclusion without evidence. For other cases, `S1`.

## TH-05 — Motivation evidence occurs before the dependent inference

- **Check:** Find evidence for prevalence, bottlenecks, failed assumptions, operational cost, or counterexamples. Make sure that it occurs before the design requirement or claim that must have it. Later evaluation does not remove the reader's earlier uncertainty about an unsupported introduction premise.
- **Reviewer attack:** “The system is derived from a premise that is asserted first and only investigated much later.”
- **Severity:** `S1` when the premise controls the design. Use `S2` for unnecessary evidence debt.
- **Exception:** Full method or result details can occur subsequently. Text before the full detail must have sufficient evidence and an accurate reference for the inference.

## TH-06 — Headline results reflect the contribution hierarchy

- **Check:** Connect each primary supporting claim to a decisive result, proof, study finding, or production observation. Give these items prominence in abstract and introduction results. Do not select prominence from numerical size alone. Record each cost and condition beside its constrained result.
- **Reviewer attack:** “The strongest advertised number is impressive but does not validate the paper's main contribution.”
- **Severity:** `S1`. Use `S2` for emphasis imbalance.

## TH-07 — The paper passes a reader-memory test

After the abstract and introduction, a technically literate systems reader can give these items without copied prose:

1. Problem or question and its importance.
2. Failed assumption, limiting constraint, or surprising observation.
3. Intellectual move.
4. Primary deliverable or finding.
5. Strongest supporting evidence.
6. Most important boundary.
7. Accurate difference from the closest alternative.

Failure predicts that the reader will treat later mechanisms and experiments as unrelated details. It is more than a style defect. Keep specialized mechanism details outside this retelling.

## TH-08 — Explanation reflects novelty and uncertainty

- **Check:** Compare space and repetition with decision importance. Give more explanation to new abstractions, unexpected constraints, and mechanisms important to the claim. Give more explanation to closest-work differences, decisive experiments, and limitations that affect conclusions. Reduce standard background, commodity implementation, repeated motivation, and results without consequences for the conclusion.
- **Reviewer attack:** “The paper spends pages on implementation inventory while the novel or vulnerable inference is compressed into a sentence.”
- **Severity:** `S2`. Use `S1` when the central idea or evidence is effectively hidden.
- **Exception:** Reproducibility details can belong in the paper or appendix without a central narrative role. Audit detail can have a different location outside the primary reading sequence.

## Internal maps

### Thesis-support tree

| Level | Claim | Why needed | Supported by | Failure consequence |
|---|---|---|---|---|
| Thesis | | | | |
| Supporting claim | | | | |
| Mechanism/finding | | | | |
| Evidence | | | | |

### Headline-evidence map

| Decision-related claim | Predicted decisive test | Evidence in the paper | Headline emphasis | Boundary/cost | Gap |
|---|---|---|---|---|---|

These maps are diagnostic aids. Keep them outside the manuscript during Review. For requested manuscript insertion, use Revise with the applicable edit authority.

## Sources

These rules use [LEVIN-REDELL], [OSDI-CFP], [SOSP-CFP], and [SYSTEMS-GUIDE]. They also use observed thesis-evidence agreement in [FIVE-VENUE-CORPUS]. The memory test and maps are author-side diagnostics. They are not official review forms.
