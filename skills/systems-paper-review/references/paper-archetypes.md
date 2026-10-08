# Contribution-Type Audit

First, read the [positive contracts by contribution type](../../systems-paper-revise/references/paper-archetypes.md). Those contracts give the argument structures. This file gives the review checks. Each archetype has different obligations and evidence forms. The scientific standard stays the same.

## PA-01 — Select by the primary acceptance claim

Find the strongest supported claim on which acceptance depends. Use that claim to select the paper archetype. Do not select it from the venue, section names, or system name.

| Archetype | Decisive reviewer question | Evidence mismatch to attack |
|---|---|---|
| New abstraction, interface, or system mechanism | Does the contract, boundary, or control-point change cause the claimed property in stated conditions? | API or component novelty without a causal property, realization, or boundary |
| Performance system or cross-layer co-design | Which bottleneck limits performance? Why do local fixes fail? Which interactions cause the end-to-end effect? | Optimizations with evidence only from isolated microbenchmarks |
| Verification, correctness, security, or formal analysis | Which property does the method prove, check, detect, or enforce? Under which model? Can users use the method? | Evaluation scale in place of soundness, or proof in place of implementation evidence |
| Measurement, characterization, or negative result | Does the finding have evidence and representativeness? What consequences and boundaries does it have? Which alternative explanations stay? | A forced solution story, unsupported causality, or generalization beyond the population |
| Benchmark or testing infrastructure | Does the construction give the claimed fidelity, coverage, cost, and reproducibility? Which new scientific conclusions can it give? | Tools without evidence for representativeness or downstream scientific use |
| Operational or experience report | What occurred at a meaningful scale? Which intervention or lesson results? Under which conditions does the lesson transfer? | Deployment scale without novelty, diagnosis, validation, or transferable knowledge |
| Case study or guideline | What is the case-selection principle? Do counterexamples or sensitivity tests change the governing factors? Where does the lesson transfer? | Generalization from one case without selection rationale, alternatives, or transfer boundary |
| Hybrid study plus tool | Does the study give the tool's requirements? Does the tool include the discovered classes? | Two adjacent contributions without a causal relation |

If multiple types apply, record one primary chain. Put the other chains below it. If this choice changes author intent, record `unresolved reviewer risk — author decision`.

For benchmark or testing infrastructure, keep structural coverage, behavioral fidelity, and use cost as different claims.
When behavioral validity matters to the declared use, give a concrete question about behavior beyond structural presence.
Select a relevant behavior, such as output, ordering, timing, or response to a fault, from the stated test purpose.
If that purpose is unclear, ask which behavior the benchmark must preserve.
Keep the question conditional on that purpose; it does not make complete production fidelity necessary.
Unavailable artifact evidence stays unresolved.

- **Severity:** `S1` if the type mismatch changes the central claim or evidence. For other cases, `S2`.
- **Calibration:** A negative result usually belongs to measurement or characterization. Artifact-first order is correct when the reader can immediately find its motivating relation. A different surface order alone does not make another template necessary.

## PA-02 — Examine the selected positive contract

Use the applicable contract to make a reconstruction of these items:

1. Problem, question, or operating condition.
2. Limiting constraint, disputed assumption, or evidence gap.
3. Intellectual move, finding, construction principle, or intervention.
4. Deliverable or analysis that gives that move a realization.
5. Decisive evidence and permitted inference.
6. Cost that affects conclusions, assumption, or transfer boundary.

For each missing link, record its evidence state. Use absent from scope, contradicted, inferential, or not assessable because context is outside scope.

A `P/G/A/I/E/B` scan can find omissions in an abstract. It is a diagnostic aid. Moves can combine or change order. A missing letter alone is not a defect.

- **Reviewer attack:** “The manuscript supplies the surface form of this contribution type but not its decision case.”
- **Severity:** `S1` for a broken primary chain. Use `S2` for a recoverable chain with an unnecessarily difficult order.

## PA-03 — Examine function

- Before detailed mechanisms, make sure that the reader can find their motivating problem, tension, or question. An artifact name first is permitted.
- Make sure that the reader can find the intellectual move without the labels `insight`, `challenge`, or `contribution`.
- Contribution bullets, research-question lists, an Overview section, and a figure before the design detail are optional. If present, examine their argument functions.
- Use the evidence forms for measurement, formal, operational, negative-result, benchmark, and characterization papers. Do not make a system-building sequence necessary.
- Keep paragraph count, sentence count, and move order outside acceptance criteria.

For a case study or guideline, examine the case-selection rationale in different checks. Examine alternative explanations, counterexamples, rule sensitivity, and transfer conditions in different checks. One clear case can show an observation about that case. General guidance must have a stable mechanism or decision boundary beyond that case.

Record these fields internally:

```text
Primary archetype and acceptance claim:
Secondary chain(s):
Canonical positive contract selected:
Missing or contradicted link(s):
Evidence form required:
Template assumptions deliberately not imposed:
```

## Provenance

The five-venue corpus in [source-registry.md](source-registry.md) gives evidence for these distinctions. Corpus frequency gives a description of observed papers. It is neither a venue rule nor an explanation of acceptance.
