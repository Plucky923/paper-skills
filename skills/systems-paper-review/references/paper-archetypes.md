# Contribution-Type Audit

Read the canonical [positive contracts by contribution type](../../systems-paper-revise/references/paper-archetypes.md) first. That reference defines the argument shapes; this file defines how a reviewer tests them. An archetype changes the obligations and admissible evidence, never the scientific standard.

## PA-01 — Route by the primary acceptance claim

Classify the paper by the strongest supported claim on which acceptance depends, not by venue, section names, or system branding.

| Archetype | Decisive reviewer question | Evidence mismatch to attack |
|---|---|---|
| New abstraction, interface, or system mechanism | Does changing the contract, boundary, or control point produce the claimed property under explicit conditions? | API or component novelty without a causal property, realization, or boundary |
| Performance system or cross-layer co-design | Which bottleneck is binding, why do local fixes fail, and which interactions cause the end-to-end effect? | A bag of optimizations supported only by isolated microbenchmarks |
| Verification, correctness, security, or formal analysis | What property is proved, checked, detected, or enforced under which model, and is the method usable? | Evaluation scale substituted for soundness, or a proof substituted for implementation reality |
| Measurement, characterization, or negative result | Is the finding real, representative, consequential, and bounded against alternative explanations? | A forced solution narrative, unsupported causality, or a result generalized beyond the population |
| Benchmark or testing infrastructure | Does a principled construction achieve the claimed fidelity, coverage, cost, and reproducibility, and what conclusions does it newly enable? | A tool inventory with no representativeness argument or downstream scientific use |
| Operational or experience report | What happened at meaningful scale, what intervention or lesson follows, and under what conditions does it transfer? | Deployment scale treated as novelty without diagnosis, validation, or transferable knowledge |
| Case study or guideline | Were cases selected on a principle, do governing factors survive counterexamples and sensitivity tests, and where does the lesson transfer? | One bounded instance generalized without a selection argument, alternatives, or transfer boundary |
| Hybrid study plus tool | Does the study derive the tool's requirements, and does the tool cover the discovered classes? | Two adjacent but causally unrelated contributions |

If several types apply, record one primary chain and subordinate the others. If choosing would change author intent, report an `unresolved reviewer risk — author decision` rather than selecting the most marketable story.

- **Severity:** `S1` when a type mismatch distorts the central claim or evidence; otherwise `S2`.
- **Calibration:** A negative result normally belongs to measurement/characterization; artifact-first ordering is valid when the motivating relation becomes immediately recoverable. Do not create a separate template merely because surface order differs.

## PA-02 — Audit the selected positive contract

Using the matching canonical contract, reconstruct:

1. the problem, question, or operating condition;
2. the binding constraint, disputed assumption, or evidence gap;
3. the intellectual move, finding, construction principle, or intervention;
4. the deliverable or analysis that realizes it;
5. the decisive evidence and permitted inference;
6. the material cost, assumption, or transfer boundary.

For every missing link, state whether it is absent from the in-scope text, contradicted, inferential, or not assessable because context is out of scope. A `P/G/A/I/E/B` scan may help locate omissions in an abstract, but it is a diagnostic: moves may combine or reorder, and no absent letter is automatically a defect.

- **Reviewer attack:** “The manuscript supplies the surface form of this contribution type but not its decision case.”
- **Severity:** `S1` for a broken primary chain; `S2` for recoverable but costly ordering.

## PA-03 — Audit function, not ceremony

- A detailed mechanism should not arrive before its motivating problem, tension, or question is recoverable; naming the artifact first is not itself a defect.
- The intellectual move must be recoverable even without the labels `insight`, `challenge`, or `contribution`.
- Contribution bullets, enumerated research questions, a standalone overview, and an early figure are optional. When present, test the argumentative work they perform.
- Measurement, formal, operational, negative-result, benchmark, and characterization papers need their own evidence forms; never force them into a system-building sequence.
- Paragraph count, sentence count, and move order are not acceptance criteria.

For a case study or guideline, separately audit the case-selection rationale, rival explanations or counterexamples, sensitivity of the proposed rule, and the conditions under which another system may reuse it. A vivid instance can establish an observation about that instance; general guidance requires a stable mechanism or decision boundary beyond it.

Record internally:

```text
Primary archetype and acceptance claim:
Secondary chain(s):
Canonical positive contract selected:
Missing or contradicted link(s):
Evidence form required:
Template assumptions deliberately not imposed:
```

## Provenance

These audit distinctions are calibrated by the five-venue corpus documented in [source-registry.md](source-registry.md). Corpus frequency is descriptive evidence, not a venue rule or an explanation of acceptance.
