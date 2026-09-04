# Thesis, Claim Hierarchy, and Reader Memory

Read the canonical [systems-writing core](../../systems-paper-revise/references/writing-core.md) and [positive contracts](../../systems-paper-revise/references/paper-archetypes.md) first. This file audits whether the scoped material delivers one memorable decision case whose design and evidence follow from its thesis; it adds review attacks and diagnostic maps rather than a second writing model.

## TH-01 — The paper has one controlling thesis

- **Check:** Recover the consequential problem or question, failed assumption/binding tension, intellectual move, resulting capability or finding, decisive evidence, and boundary. The thesis may span several sentences; it fails when reconstruction requires choosing among incompatible stories or listing components.
- **Reviewer attack:** “I understand what was built, but not the proposition this paper asks me to believe.”
- **Severity:** `S1`; `S2` when present but difficult to recover.
- **Exception:** A measurement or experience paper may center a finding or lesson rather than a new mechanism.

## TH-02 — Supporting claims form a hierarchy

- **Check:** Build a tree with one controlling thesis, a small decision-relevant set of supporting claims, the mechanisms or analyses that discharge them, and evidence for each. Separate primary contributions from enabling engineering, implementation facts, and incidental optimizations.
- **Reviewer attack:** “The contribution list is flat, so I cannot tell which failure would invalidate the paper.”
- **Severity:** `S1` when the central case depends on the ambiguity; otherwise `S2`.
- **Exception:** Do not force an arbitrary claim count; require only the distinctions needed to expose which failure would invalidate the thesis.

## TH-03 — The thesis predicts the design

- **Check:** Hide component names and ask what requirements follow from the paper's stated problem and intellectual move. Then verify the actual major mechanisms discharge those requirements. A central idea that cannot explain the design is usually a slogan or retrospective summary.
- **Reviewer attack:** “The claimed insight could introduce many unrelated systems and does not explain this design.”
- **Severity:** `S1`.

## TH-04 — The thesis predicts the decisive evidence

- **Check:** Before reading the evaluation, derive what observations would make the central thesis credible or false. Compare this set with the actual headline results. Evidence quantity cannot compensate for omission of the decisive test.
- **Reviewer attack:** “The paper evaluates what is easy to measure, not what its thesis requires.”
- **Severity:** `S0` for a central unsupported conclusion; otherwise `S1`.

## TH-05 — Motivation evidence arrives before the inference that needs it

- **Check:** Locate evidence for problem prevalence, bottleneck, failed assumption, operational cost, or counterexample. Verify it appears early enough to license the design requirement or claim it motivates. A later evaluation cannot retroactively make an unsupported introduction premise easy to follow.
- **Reviewer attack:** “The system is derived from a premise that is asserted first and only investigated much later.”
- **Severity:** `S1` when the premise controls the design; `S2` for avoidable evidence debt.
- **Exception:** Full methodology or result detail may remain later; the early text needs only enough evidence and a precise pointer to support the inference.

## TH-06 — Headline results mirror the contribution hierarchy

- **Check:** Match each primary supporting claim to one decisive result, proof, study finding, or production observation. Abstract and introduction results should foreground these items rather than whichever numbers are largest. Record costs and boundary conditions beside the result they constrain.
- **Reviewer attack:** “The strongest advertised number is impressive but does not validate the paper's main contribution.”
- **Severity:** `S1`; `S2` for imbalanced emphasis.

## TH-07 — The paper passes a reader-memory test

After the abstract and introduction, a technically literate systems reader should be able to state, without copying prose:

1. the problem or question and why it matters;
2. the failed assumption, binding constraint, or surprising observation;
3. the intellectual move;
4. the primary deliverable or finding;
5. the strongest supporting evidence;
6. the most important boundary;
7. the precise delta from the closest alternative.

Failure is not merely stylistic: it predicts that later mechanisms and experiments will be interpreted as unrelated details. Do not require specialized mechanism detail in this retelling.

## TH-08 — Attention follows novelty and uncertainty

- **Check:** Compare space and repetition with decision importance. Give more explanation to the new abstraction, counterintuitive constraint, critical mechanism, closest-work delta, decisive experiment, and material limitation. Compress standard background, commodity implementation, repeated motivation, and results that do not change the conclusion.
- **Reviewer attack:** “The paper spends pages on implementation inventory while the novel or vulnerable inference is compressed into a sentence.”
- **Severity:** `S2`; `S1` when the central idea or evidence is effectively hidden.
- **Exception:** Reproducibility-critical detail may belong in the paper or appendix even when not narratively central; placement should separate audit depth from the main reading path.

## Internal maps

### Thesis-support tree

| Level | Claim | Why needed | Supported by | Failure consequence |
|---|---|---|---|---|
| Thesis | | | | |
| Supporting claim | | | | |
| Mechanism/finding | | | | |
| Evidence | | | | |

### Headline-evidence map

| Decision-relevant claim | Predicted decisive test | Actual evidence | Headline emphasis | Boundary/cost | Gap |
|---|---|---|---|---|---|

The maps are diagnostic. Do not paste them into the manuscript unless the user asks for them.

## Sources

These rules synthesize [LEVIN-REDELL], [OSDI-CFP], [SOSP-CFP], [SYSTEMS-GUIDE], and observed thesis/evidence alignment in [FIVE-VENUE-CORPUS]. The memory test and map are author-side diagnostics, not official review forms. Last reconciled 2026-09-03.
