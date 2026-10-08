# Examples, Argument Figures, and Headline Results

Use this reference when examples, scenarios, motivating measurements, the first diagrams, or headline results carry the argument. Also use the correctness and rendering checks in [figures-tables-latex.md](figures-tables-latex.md). Keep the validity checks in [evaluation.md](evaluation.md).

## ER-01 — A running example shows a difficult inference

- **Check:** Find the abstract relation that the example shows with specified conditions. Examine assumption failure, boundary crossings, lifecycle, mechanism interactions, and claimed outcomes as applicable. When the example recurs, use the same entities and terminology.
- **Reviewer attack:** “The example is decorative; it never helps me understand why the design is necessary or how it works.”
- **Severity:** `S2`. Use `S1` when prose alone leaves a central relation unclear.
- **Exception:** An example is unnecessary when the model, theorem, or architecture already gives a clear, short explanation.

## ER-02 — Counterexamples show the accurate failure boundary

- **Check:** Make sure that the counterexample satisfies the old approach's assumptions. Make sure that it causes the claimed failure. Do a check of the difference between the related constraint and unrelated weaknesses. Record the example's conclusion and its generalization boundary.
- **Reviewer attack:** “The motivating case is a strawman or does not demonstrate the claimed limitation.”
- **Severity:** `S1`. Use `S0` when the counterexample is the paper's only premise and that premise is false.

## ER-03 — The first figures have an argument function

- **Check:** Record each motivation, overview, or architecture figure's function. Examine mismatch, boundaries, causal path, actors, trust, workflow, or the intellectual move's system effect as applicable. Boxes and arrows that only repeat nouns consume attention without a new relation.
- **Reviewer attack:** “Figure 1 shows the system, but not the idea.”
- **Severity:** `S2`. Use `S1` when the central abstraction stays impossible to find.
- **Exception:** The first figures are optional. Make one necessary only if it shows the relation more clearly than short prose.

## ER-04 — Prose, example, figure, and mechanism use one model

- **Check:** Compare actors, state, sequence, trust boundaries, fault boundaries, terminology, optional paths, and claimed results across the objects. Let simplification occur only if the omitted detail does not reverse the inference.
- **Reviewer attack:** “The example succeeds only because it silently omits a state or failure path present in the real design.”
- **Severity:** `S0`–`S2`, as determined by the affected claim.

## ER-05 — Headline results answer open reader questions

- **Check:** List the questions that the thesis and design requirements leave open. Connect abstract numbers, introduction numbers, and prominent figures to answers. Select a small set of results related to the decision. Do not use an inventory of measurements selected for positive results.
- **Reviewer attack:** “The headline results are large but orthogonal to the main claim.”
- **Severity:** `S1`. Use `S2` for emphasis imbalance.

## ER-06 — Result sentences give conditions, comparison, and implications

- **Check:** For each headline result, record the measurement, setting, reference, uncertainty or scope, and supported claim. The closing sentence can give the implication or boundary. Repetition of the number is not necessary.
- **Reviewer attack:** “The number is memorable, but its denominator, comparison, or scientific meaning is not.”
- **Severity:** `S1` for a central result with ambiguity. For other cases, `S2`.

## ER-07 — Motivation evidence stays different from general proof

- **Check:** Do a check of differences between illustrative incidents, representative measurements, exhaustive characterization, and controlled causal evidence. An example with specified conditions can show possibility. Alone, it cannot show prevalence, typicality, or cause.
- **Reviewer attack:** “One vivid case is used to justify a general workload or deployment claim.”
- **Severity:** `S1`. Use `S0` when invalid generalization controls all the significance case.

## Argument-object map

| Object | Intended reader question | Observable message | Claim advanced | Boundary | Redundant or missing work |
|---|---|---|---|---|---|

Apply this map to examples, Figure 1/2, contribution bullets, and headline results. Keep objects that make difficult inferences easier, even without novelty of their own.

## Sources

These rules use [SYSTEMS-GUIDE], [HEISER-STYLE], [SIGPLAN-EMPIRICAL], and observations in [FIVE-VENUE-CORPUS]. Corpus frequency gives calibration. It is not a requirement.
