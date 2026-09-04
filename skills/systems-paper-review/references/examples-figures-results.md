# Examples, Argument Figures, and Headline Results

Use this reference when examples, scenarios, motivating measurements, early diagrams, or headline results carry the paper's argument. It supplements—not replaces—the correctness and rendering checks in [figures-tables-latex.md](figures-tables-latex.md) and the validity checks in [evaluation.md](evaluation.md).

## ER-01 — A running example executes the paper's difficult inference

- **Check:** Determine which abstract relation the example makes concrete: failure of an old assumption, boundary crossing, lifecycle, mechanism interaction, or claimed outcome. Revisit the same entities and terminology when the example returns.
- **Reviewer attack:** “The example is decorative; it never helps me understand why the design is necessary or how it works.”
- **Severity:** `S2`; `S1` when prose alone leaves a central relation unintelligible.
- **Exception:** Do not demand an example when the model, theorem, or architecture is already economical to understand.

## ER-02 — Counterexamples expose the exact failure boundary

- **Check:** Verify the counterexample satisfies the old approach's assumptions, triggers the claimed failure, and isolates the relevant constraint rather than an unrelated weakness. State what the example establishes and what it does not generalize to.
- **Reviewer attack:** “The motivating case is a strawman or does not demonstrate the claimed limitation.”
- **Severity:** `S1`; `S0` if it is the sole false premise for the paper.

## ER-03 — Early figures perform an argumentative job

- **Check:** For a motivation, overview, or architecture figure, name its job: reveal a mismatch, compare boundaries, show a causal path, define actors/trust, trace a workflow, or preview how the intellectual move changes the system. Boxes and arrows that merely repeat nouns waste scarce attention.
- **Reviewer attack:** “Figure 1 shows the system, but not the idea.”
- **Severity:** `S2`; `S1` when the central abstraction remains unrecoverable.
- **Exception:** An early figure is optional. Add or require one only when the relation is materially clearer visually than in compact prose.

## ER-04 — Prose, example, figure, and mechanism share one model

- **Check:** Cross-check actors, state, order, trust/fault boundaries, terminology, optional paths, and claimed result. Simplification is valid only when the omitted detail does not reverse the inference.
- **Reviewer attack:** “The example succeeds only because it silently omits a state or failure path present in the real design.”
- **Severity:** `S0`–`S2` by affected claim.

## ER-05 — Headline results answer the reader's open questions

- **Check:** List the questions left open by the thesis and design requirements, then map abstract/introduction numbers and emphasized figures to their answers. Prefer a small set of decision-relevant results over a catalogue of favorable measurements.
- **Reviewer attack:** “The headline results are large but orthogonal to the main claim.”
- **Severity:** `S1`; `S2` for emphasis imbalance.

## ER-06 — Result sentences carry condition, comparison, and implication

- **Check:** For each headline result, recover what was measured, under which setting, against what reference, with what uncertainty or scope, and which claim it supports. The closing sentence may give the implication or boundary; it need not repeat the number.
- **Reviewer attack:** “The number is memorable, but its denominator, comparison, or scientific meaning is not.”
- **Severity:** `S1` for a central ambiguous result; otherwise `S2`.

## ER-07 — Motivation evidence is not disguised as general proof

- **Check:** Separate illustrative incident, representative measurement, exhaustive characterization, and controlled causal evidence. A concrete example can establish possibility; it cannot alone establish prevalence, typicality, or cause.
- **Reviewer attack:** “One vivid case is used to justify a general workload or deployment claim.”
- **Severity:** `S1`; `S0` if the paper's significance case depends entirely on the invalid generalization.

## Argument-object map

| Object | Intended reader question | Observable message | Claim advanced | Boundary | Redundant or missing work |
|---|---|---|---|---|---|

Apply this map to examples, Figure 1/2, contribution bullets, and headline results. Preserve an object that makes a difficult inference cheaper even when it is not itself novel.

## Sources

These rules combine [SYSTEMS-GUIDE], [HEISER-STYLE], [SIGPLAN-EMPIRICAL], and observations in [FIVE-VENUE-CORPUS]. Corpus frequency is calibration, not a requirement. Last reconciled 2026-09-03.
