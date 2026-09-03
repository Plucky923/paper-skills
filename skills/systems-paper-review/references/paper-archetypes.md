# Paper Archetypes and Narrative Routing

Choose an argument shape from the paper's primary scientific contribution, not from its venue, section names, or system name. OSDI/SOSP papers share standards of significance, clarity, correctness, and evidence, but they do not share one mandatory introduction or evaluation template. Use this reference for an abstract, introduction, whole paper, or any review whose result depends on what kind of paper is being claimed.

## PA-01 — The primary archetype matches the acceptance claim

Classify the primary decision case before applying section-level rules:

| Archetype | Primary contribution | Reader's decisive question | Typical evidence |
|---|---|---|---|
| New abstraction or interface | A different contract or boundary makes a previously difficult capability possible | Why is the old interface the binding constraint, and what property follows from changing it? | Semantics, compatibility, implementation, end-to-end results, boundary cases |
| Performance system or co-design | Coordinated mechanisms remove a consequential bottleneck | Why do simpler optimizations fail, and which mechanisms cause the gain? | Bottleneck evidence, end-to-end comparison, attribution, sensitivity, costs |
| Verification, correctness, or security | A method establishes a stated property under explicit assumptions | What failure class is excluded, and why is the method sound and usable? | Model, theorem/proof or validation, counterexamples, coverage, overhead |
| Measurement or empirical study | New observations revise understanding of a system or practice | Is the finding real, representative, and consequential? | Data provenance, methodology, descriptive results, robustness, limitations |
| Operational or experience report | Production evidence yields actionable interventions or reusable lessons | What happened at meaningful scale, what changed, and what transfers? | Field evidence, intervention comparison, deployment outcomes, negative cases |
| Hybrid study plus tool | Empirical findings derive requirements for a mechanism or tool | Does the study actually license the tool, and does the tool address the discovered classes? | Taxonomy/root-cause study, requirement coverage, tool evaluation |

If several apply, choose the archetype that carries the strongest supported acceptance claim and treat the others as supporting chains. Do not make a paper appear more novel by relabeling an empirical or operational contribution as a new mechanism. An unresolved choice that would change author intent is an author-decision risk, not permission to choose the most marketable story.

- **Reviewer attack:** “The paper asks to be judged as one kind of contribution but supplies the novelty or evidence of another.”
- **Severity:** `S1` when the mismatch distorts the central claim or evaluation; otherwise `S2`.

## PA-02 — The argument satisfies the selected positive contract

These are dependency relations, not required sentence or section orders.

### New abstraction or interface

`existing contract → newly important mismatch → binding constraint → changed contract → resulting property → realization → compatibility/cost evidence`

The paper must explain which relationship changes and why that change produces the claimed property. Naming an API, layer, or virtualization boundary is not the idea.

### Performance system or co-design

`consequential workload/bottleneck → why local fixes saturate → exploitable structure → design requirements → interacting mechanisms → end-to-end effect → attribution and shifted costs`

A bag of optimizations fails this contract even when every optimization improves a microbenchmark. Co-design is established by necessity and interaction, not by component count.

### Verification, correctness, or security

`failure/assurance gap → precise model and target property → tractability or enforcement insight → method → soundness/coverage boundary → feasibility and overhead`

State whether the contribution proves, checks, detects, prevents, or empirically observes a property. Do not substitute evaluation scale for a missing correctness argument, or a proof for implementation practicality.

### Measurement or empirical study

`important question or disputed assumption → observable population and method → validated finding → alternative explanations → consequence for design/operation → bounded lesson`

Do not require a new system, algorithm, root cause, or causal claim. The intellectual move may be a taxonomy, falsified assumption, boundary, or newly measured relationship.

### Operational or experience report

`production setting/stakes → observed failure or cost → diagnosis → intervention → production outcome → transfer conditions and unresolved limits`

Quantified field evidence may establish the problem before any new abstraction appears. Novelty can lie in scale, evidence, intervention, or lesson rather than algorithmic technique.

### Hybrid study plus tool

`observed incidents/phenomena → taxonomy or root causes → requirements derived from the study → tool/mechanism → coverage of discovered classes → deployment or controlled validation`

The tool must trace back to study-derived needs. A study followed by an unrelated system is two weak contributions, not automatically one strong hybrid contribution.

- **Reviewer attack:** “The sections are individually plausible, but they do not discharge the decision case appropriate to this paper.”
- **Severity:** `S1` for a broken primary chain; `S2` for a recoverable but costly ordering problem.

## PA-03 — Required functions are not confused with surface form

- The reader receives the motivating problem, tension, or question before being asked to accept detailed mechanisms. A paper may name the system first if the same sentence or immediate continuation supplies that context.
- The central intellectual move is recoverable even when the paper never uses the words `insight`, `challenge`, or `contribution`.
- Contribution bullets are optional. When present, they must express a hierarchy of claims and deliverables rather than replay the table of contents.
- Evaluation questions may be explicit headings, prose obligations, or interleaved with operational findings. Require recoverable question–answer pairs, not a ritual section layout.
- A running example or early figure is optional. Its absence is a defect only when the remaining prose cannot make a central relation, boundary, or counterexample economical to understand.

- **Reviewer attack:** “The review or manuscript mistakes a conventional label, order, or section shape for scientific completeness.”
- **Severity:** Record the underlying missing function; surface-form variation alone is not a defect.

## Routing output

Record internally:

```text
Primary archetype:
Secondary archetype(s):
Primary acceptance claim:
Archetype-specific narrative chain:
Evidence form required by that claim:
Template assumptions deliberately not imposed:
```

When the archetype is ambiguous because author intent or missing scope would change the primary claim, mark the choice as unresolved instead of silently selecting the most marketable story.

## Sources

This routing model synthesizes the contribution categories permitted by [OSDI-CFP] and [SOSP-CFP], the category-sensitive review guidance in [LEVIN-REDELL], and cross-year observations in [OSDI-SOSP-CORPUS]. It describes recurring argument functions, not official venue templates or acceptance causes. Source keys are defined in [source-registry.md](source-registry.md). Last reconciled 2026-09-03.
