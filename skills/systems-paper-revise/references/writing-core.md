# Canonical Systems-Writing Core

Review, Grill, and Revise use this single quality standard for the same scoped prose, including requested drafting. Other references specialize its criteria or govern actions; they do not redefine what counts as clear, precise, logically supported writing. Use the [coverage contract](coverage-contract.md) for the mandatory top-down audit and visible accounting, and the [shared workflow contract](review-revise-contract.md) for consistent judgments and discussion of uncertain logic.

## Top-systems calibration and editing authority

The stable common core for OSDI-, SOSP-, EuroSys-, ATC-, and ASPLOS-caliber systems writing is a significant and well-bounded problem or question, a clear advance over the relevant baseline, technically convincing realization or method, evidence matched to the claim, honest costs and limitations, correctness, and warranted conclusions. OSDI's [review criteria](https://www.usenix.org/conference/osdi27/call-for-papers) and the [systems-paper writing guide](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/good_paper.html) calibrate this core. Apply it through the contribution archetype and each unit's actual role; a background paragraph need not become a miniature introduction or evaluation.

Accepted-paper patterns calibrate functional expectations rather than impose one fixed template. When the user names a venue, track, cycle, or submission-policy question, add the current official overlay through Review's [venue rules](../../systems-paper-review/references/venue-overlays.md). Never freeze a page limit, anonymity rule, review stage, or preliminary call into this stable writing standard.

Paragraph-local revision is this project's author-specified editing boundary, not an OSDI submission rule. Writing criteria diagnose quality; they do not authorize adding research content or restructuring existing paragraphs. Apply the [revision protocol](revision-protocol.md) for editing authority and verify live venue rules only when making a submission-policy judgment.

Judge quality independently of permission to edit: an unsupported inference remains a scientific gap even when its original wording must be retained, and a merely different phrasing is not a defect. The shared contract governs how Review and Revise act on that judgment.

## The decision case

A systems paper asks a reader to accept a bounded scientific advance:

```text
important problem or question under stated conditions
  → decisive constraint, gap, or unknown
  → intellectual move: principle, method, or finding
  → mechanism, study, proof, or artifact that realizes it
  → evidence that discriminates the claim
  → cost, assumption, limitation, and transferable consequence
```

This is a dependency spine, not a required sentence or section order. A text unit includes only the roles needed for its local obligation. Route the spine through [paper-archetypes.md](paper-archetypes.md) when the contribution is not a conventional system mechanism or when the contribution type is uncertain.

Write for two depths of reading along the same claim hierarchy:

- A broad systems reader should recover the problem, delta, intellectual move, credible evidence, and main boundary from the title, abstract, introduction, overview, headline results, and conclusion.
- A domain expert should be able to validate that account through the model, assumptions, invariants, lifecycle, implementation status, experimental controls, and failure cases.

The first two pages are a useful stress test for every venue, not a universal submission rule: can a reader accurately retell the decision case without inventing a missing link? Apply a hard page-specific rule only after checking the named venue and cycle.

## High-level causal compression

`High-level` means preserving the causal structure while suppressing detail that does not affect the reader's current decision. At the highest useful level, make these elements recoverable:

1. **Object and condition:** the system, workload, model, population, or stage to which the statement applies.
2. **Constraint or unknown:** the relation that defeats the old approach or prevents a conclusion.
3. **Intellectual move:** the principle, changed boundary, method, or finding that changes the problem.
4. **Realization:** enough mechanism, analysis, or study design to explain why the move is credible.
5. **Consequence and evidence:** the property or conclusion that follows and the evidence that supports it.
6. **Boundary:** the cost, assumption, comparison scope, or failure condition that limits the conclusion.

A paragraph needs only the elements relevant to its promised and delivered role. A recoverable implicit link can remain implicit. Do not add sentences to expose every step or complete all six elements; an absent scientific premise needs author evidence, not editorial reconstruction.

When the evidence identifies a binding constraint or failure relation, keep that relation recoverable instead of replacing it with a weaker benefit paraphrase. Preserve the affected operation, the condition or frequency, and the bottleneck or failure when those facts explain why the intellectual move is necessary.

Apply four tests to a principle-level statement:

- **Distinction:** If unrelated systems or methods can replace the nouns without changing the proposition, the statement is too generic.
- **Prediction:** The statement should predict at least one major design, study, or proof choice; otherwise it is detached from the work.
- **Falsification:** A reader should be able to name a condition or observation under which the statement fails or narrows.
- **Evidence:** The scoped material should contain a proof, analysis, experiment, or observation capable of supporting the stated consequence.

## Source-grounded intellectual-move fan-out

Reconstruction is a diagnostic instrument, not an editorial repair. For every
central node and causal edge that Review recovers, record one source status:

- **stated:** the prose explicitly supplies the node or relation; anchor it to
  the shortest original span;
- **text-licensed:** the relation follows from premises and a dependency that the
  scoped text supplies, even if it is not restated word for word; anchor both
  endpoints and name the inference;
- **reviewer-hypothesized:** the relation is a plausible way to make the story
  coherent, but the scoped text does not supply a required premise or causal
  edge.

A reviewer-hypothesized bridge does not make the manuscript clear. Review reports
the exact missing edge, Grill asks the author to confirm or replace it, and Revise
keeps it out of prose until it is supported by the source or an evidence-compatible
author decision.

When a passage presents two or more primary outcomes as consequences of one
insight, changed boundary, or design choice, build this **fan-out map**:

```text
problem or binding constraint -> intellectual move
intellectual move -> outcome A, through <causal layer and mechanism>
intellectual move -> outcome B, through <causal layer and mechanism>
intellectual move -> outcome C, through <causal layer and mechanism>
```

The exact number of outcomes is whatever the manuscript claims. Give every edge
its source status and original-text anchors. Source status records provenance,
not validity: a sentence that merely asserts `X provides Y` is `stated` but can
still omit the causal layer, mechanism, or premise that makes the edge credible.
The unification passes only when the shared move is itself source-grounded and
each advertised outcome has an anchored dependency whose causal layer and
counterfactual are recoverable. A shared system name, paragraph, component, or
nearby list is co-occurrence, not a causal relation.

Apply two checks to each fan-out edge:

1. **Causal-layer attribution:** assign the narrowest layer that supplies the
   step—enabling substrate, changed abstraction or authority boundary, runtime
   enforcement and lifecycle, execution-path organization, or empirical
   condition. Do not credit one layer with a compound property that still needs
   another layer. For example, an enforcement-friendly language can remove a
   bypass class without by itself establishing authorization, isolation,
   availability, or end-to-end performance.
2. **Counterfactual:** hold the other stated assumptions fixed and remove the
   proposed intellectual move or the named layer. State which outcome or
   mechanism ceases to hold. If the text supplies no answer, the edge is
   reviewer-hypothesized; if an outcome survives independently, it is not evidence
   that the move unifies that outcome.

Several independent contributions are legitimate. Do not force them under a
single insight when the manuscript presents them separately. The fan-out test is
required when the paper claims, implies, or relies on one move explaining several
headline properties; it determines whether the prose delivers that promise or
only places independent mechanisms under one label.

Keep three levels distinct:

- A **principle** changes the design or reasoning space: what constraint, boundary, dependency, or assumption is changed and why that matters.
- A **mechanism or method** realizes the principle through an operation, state transition, algorithm, proof rule, sampling choice, or intervention.
- An **implementation detail** records the concrete realization: data structure, API, thread, parameter, tool, or code path.

When information order causes a specific comprehension problem, expose the existing governing relation at the point where the reader needs it. Preserve an already clear progression and the author's emphasis. A principle-first alternative to adequate prose is optional. Moving detail between paragraphs or sections requires explicit restructuring authority.

Calibration:

> **Original:** “Each worker keeps a quota locally. Each worker keeps that quota locally so it can make admission decisions locally.”
>
> **Redundancy repair:** “Each worker keeps a local quota so it can make admission decisions locally.”

> **Original:** “Requests enter a local queue. A background thread submits them in batches.”
>
> **Decision:** Keep this adequate description. It does not establish reduced coordination overhead, latency, or a correctness guarantee. Adding one of those claims would change the scientific content.

These synthetic examples illustrate editing decisions. A component inventory without a supplied causal relation cannot be turned into a supported principle merely by rephrasing it.

## Paragraphs as inference units

A paragraph performs one local reasoning obligation: it leaves the reader with one usable update about a problem, premise, mechanism, finding, evidence, or boundary.

- The **opening region** makes the obligation discoverable. It may state the claim immediately or use a short bridge from the preceding paragraph before doing so.
- The **development** supplies only the definitions, reasons, mechanisms, evidence, comparisons, and qualifications needed to discharge that obligation.
- The **ending region** resolves the obligation or transfers it to the next necessary question. It may close with a result, implication, requirement, limitation, or unambiguous handoff; it need not summarize the opening.

The first and last sentences carry high informational weight, but they are not fixed slots. Mathematical continuations, compact bridge paragraphs, lists, and tightly connected derivations may close implicitly. Judge whether the obligation is discoverable and resolved, not whether a topic-sentence template appears.

Let reasoning determine paragraph length. Diagnose structure with these signals:

- **Overfull:** the paragraph establishes two independent conclusions or mixes context, mechanism, evidence, and a new limitation without hierarchy.
- **Fragmented:** adjacent short paragraphs each contain only setup, one number, or an empty transition and cannot support a claim alone.
- **Level jumping:** principle, source-code detail, and system-level consequence alternate without a stated relation.
- **Citation inventory:** names and citations accumulate without a comparison axis or author inference.
- **Overcompressed:** a shorter version has lost a condition, causal bridge, evidence scope, or boundary.

Overfull and fragmented are diagnoses, not automatic permission to split or merge paragraphs. In paragraph-local revision, preserve the boundaries and improve internal hierarchy where possible. If that cannot resolve the problem, identify the required structural change separately. Split or merge paragraphs only when the author explicitly requests restructuring, and then let reasoning roles rather than sentence counts determine the boundary.

As an internal test, complete: `This paragraph makes the reader believe ___ because ___.` Two unrelated answers indicate competing obligations; no answer indicates that its argumentative job is unclear. Neither diagnosis licenses a new purpose or invented content.

## Role, payoff, and evidence-state gates

Apply these gates independently. A scientific-support risk does not clear an
argument-role defect, and a clean rhetorical structure does not establish the
science.

### Promise versus delivery

A paragraph can signal its intended job through a heading, roadmap, opening
claim, explicit phrase such as `our key insight`, or author-supplied intent.
Record that promised role separately from the role delivered by its sentences.
If an alleged insight paragraph mainly inventories operations, checks, or data
structures, report the mismatch; calling it an overview or mechanism paragraph
describes the symptom but does not repair the promise. When no role is observable
inside the authorized scope, mark intended role not assessable and still classify
the delivered role.

### One obligation and one payoff

Complete the `believe ___ because ___` test, then ask whether every sentence helps
establish that same update. A connective such as `also`, `however`, or `therefore`
does not subordinate an independent question. In particular, an evaluation plan
and a newly introduced architectural challenge normally create separate reader
obligations unless the latter is explicitly part of the former's evidence logic.
Diagnose the split even when paragraph-local editing authority prevents moving it.

For the ending region, state the exact information it adds and run a deletion
test: if removing it loses no supported conclusion, boundary, design obligation,
or necessary handoff, it is redundant or formulaic. A
`limitation -> requirement` ending is valid only when the limitation is established
and the requirement is a design-specific consequence, not a third restatement of
the same absence. Also run a mechanical-inversion test: deletion may remove the
explicit sentence while losing no reader update when the ending merely negates,
positivizes, or changes `does not provide X` into `must provide X`. To pass, the
payoff must add a supported consequence, constraint, choice, scope boundary, or
handoff beyond that mechanically recoverable requirement. The ending need not use
any fixed contrast or conclusion phrase.

### Keep claim kinds aligned

Distinguish a system property from the epistemic work used to establish it. A
claim that one property is necessary but insufficient should name the other
property or invariant that remains unsatisfied; phrasing it as a property that
"cannot replace an argument/proof" mixes object-level behavior with manuscript
evidence unless the sentence is explicitly discussing proof obligations. Review
the necessity claim and the category mismatch separately. Revise may repair a
meaning-equivalent category mismatch while leaving a disputed necessity claim
blocked. When the same sentence or immediately preceding context already names
the remaining object-level properties, aligning the sentence to those properties
does not require the author to choose a new scientific meaning: preserve the
necessity claim at its original strength, repair the category locally, and keep
the necessity evidence explicitly unresolved. Do not leave the category defect
unchanged merely because the independent necessity claim is blocked.

### Related work must earn the research gap

Use one decision-relevant comparison dimension at a time. Grammatical parallelism
is insufficient when the compared predicates describe different dimensions or
levels. When the paragraph claims that prior designs fail to meet a new
requirement, recover this chain:

```text
fair comparison axis -> shared assumption/mechanism/constraint
  -> why it prevents the target property -> bounded unmet requirement
```

A list of different boundaries or supported objects establishes descriptive
contrast, not a shared root cause. If the authorized material supplies no common
cause, Review reports the missing causal bridge and Revise requests author input;
neither invents it. A pure survey paragraph need not manufacture a root cause, but
it still needs a coherent comparison axis. Verify negative prior-work claims
separately; missing literature evidence must not hide the visible organizational
defect. Apply the visible `classification -> gap -> question` test even when the
excerpt's incoming antecedent or cited sources are unavailable: record those
scope/evidence blockers separately, then state whether the visible classification
contains the causal premise needed to earn the gap and research question.

### Completed-paper prose answers with evidence

In a completed-paper context, a sentence such as `performance must be evaluated`
is a plan or placeholder, not an evidence-derived payoff. For a request to review
manuscript or paper prose, use research-paper context as the default unless the
user or text identifies a proposal, roadmap, plan, or future-work document. If
the lifecycle truly remains ambiguous, report the completed-paper interpretation
as a conditional risk and ask which state applies; do not mark the placeholder as
a clean result. If authorized results
are available, state the bounded observed answer with its metric, baseline,
conditions, and material uncertainty. If they are unavailable, keep the evidence
state honest and request the actual result; an instruction to assume experiments
exist supplies no outcome. Proposal, roadmap, and future-work contexts may
legitimately state planned evaluation. Do not make completed-paper prose appear
answered by deleting the comparison question, workload dependence, residual-cost
boundary, or other scientific proposition that the missing result was meant to
resolve. Author dissatisfaction with a placeholder, or an instruction to derive
from assumed experiments, is not authority to withdraw those propositions. When
the result-dependent payoff cannot be replaced from authorized evidence, keep the
affected passage unchanged and report the result tuple required; remove a pure
editorial TODO only when it carries no scientific content and its withdrawal is
explicitly authorized.

### Place material boundaries near the claims they govern

A limitation that materially narrows the central contribution's supported users,
workloads, deployment model, semantics, or applicability should be recoverable in
the abstract or introduction at the depth needed to prevent an overbroad first
impression; detailed consequences may remain in Discussion or Limitations. This
is a conditional placement judgment, not automatic permission to move text. With
only an isolated limitation paragraph, identify the affected claim and mark the
exact placement or wording not assessable until the relevant broad-reader claim
and surrounding introduction are in scope. This conditional judgment is itself
required whenever the visible boundary appears material; do not wait for an
explicit placement question, and do not omit it merely because the Introduction
is outside the frozen scope.

## Identify roles and inspect links

Anchor analysis to the original text: number prose paragraphs `P1`, `P2`, and sentences within them `P1.S1`, `P1.S2`. Use the author's labels or section/path anchors when available. Source-file wraps are not paragraph breaks; LaTeX paragraphs, lists, headings, display equations, and citation abbreviations require document-aware interpretation. If extraction makes boundaries uncertain, use short quotations instead of invented numbering.

For every supplied paragraph, identify its promised role when observable and its delivered topic, role, claim or question, supporting content, and closing takeaway. Roles include background, problem, gap, principle, mechanism, implementation, evidence, comparison, limitation, or transition. These are reading aids, not mandatory headings or slots to fill. Record uncertainty, mixed roles, or promise-versus-delivery mismatch instead of silently replacing the author's intention.

Inspect every adjacent sentence pair and any explicit longer dependency. What does the first establish, what does the second need, and is their actual relation explanation, evidence, consequence, contrast, condition, example, qualification, or continuation? Check referents, objects, assumptions, comparison scope, and claim strength. A connective cannot repair an unsupported inference; logical continuity does not require every pair to be causal or contain a transition word.

For every adjacent pair of supplied paragraphs, compare their roles and inspect the closing claim of the first against the opening premise or question of the second. Follow additional nonadjacent dependencies when the text names them. Check missing premises, unsupported shifts of topic or abstraction, repeated reasoning, inconsistent assumptions, and conclusions that exceed the earlier evidence. A declared topic change or an already clear handoff is not a defect. If only one paragraph is in scope, cross-paragraph logic is not assessable.

Describe a faulty link by both original endpoints and the missing or invalid relation. Refer to the specific supporting sentences when a paragraph-level break is not located exactly at the last/first sentence. Keep these anchors in review findings or blocker notes, not inside revised manuscript prose.

## Sentence information structure

Give each sentence one **dominant assertion**. Conditions, reasons, contrasts, and qualifications may remain in the same sentence when they directly organize that assertion. Split a sentence when it asks the reader to accept two independent claims, not merely because it is long.

- Anchor the sentence in information already available to the reader, then place the consequential new information where it receives emphasis.
- Expose the technically important actor and action early enough to prevent ambiguity. Use `we` for author choices, the system or mechanism for system actions, and passive voice when the affected object or result is the legitimate focus.
- Keep a modifier, quantifier, negation, comparison, and condition adjacent to the proposition it limits.
- Coordinate items at the same grammatical and conceptual level. Separate an idea, an implementation, and an evaluation result rather than presenting them as parallel contributions.
- Repeat a precise technical term when a synonym would blur identity. Replace a pronoun or bare `this` when more than one antecedent is plausible.

Prefer a simple clause structure when it preserves the relation. Complexity is justified when it makes one exact dependency easier to see.

## Logical and lexical precision

Separate propositions that require different evidence:

- An **observation** reports what the data or artifact shows.
- An **explanation** attributes that observation to a cause.
- A **design prediction** states what should follow from a mechanism or principle.
- A **conclusion** states what the complete evidence licenses.

Temporal correlation alone does not establish the explanation; a mechanism prediction alone does not establish the conclusion. Keep `necessary` and `sufficient` distinct: `X requires Y` makes Y necessary, whereas `Y guarantees X` makes Y sufficient under stated assumptions.

Use transitions only for real relations: cause, consequence, contrast, condition, example, qualification, or handoff. The premises before `therefore` must license its conclusion; the clauses around `however` must actually contrast.

Comparisons preserve problem equivalence. Name the entities, objective, metric, semantic guarantee, resources, conditions, and baseline that make the comparison meaningful. If a benefit comes from weaker semantics or a shifted cost, attach that difference to the result.

Keep conclusions within the measurement object: a microbenchmark measures an operation, a simulation supports claims inside its model, a mean does not describe a tail, one deployment establishes a bounded feasibility result, and an executable artifact does not by itself reproduce every paper claim.

Choose verbs by technical relation and evidence strength:

| Verb class | Commitment |
|---|---|
| `observes`, `measures`, `finds` | Reports evidence without silently asserting its cause. |
| `suggests`, `indicates` | Draws a bounded inference while alternatives remain. |
| `shows`, `demonstrates`, `establishes` | Claims the cited evidence directly supports the stated conclusion. |
| `implements`, `builds` | Claims the named realization exists; its implemented extent must be clear. |
| `enforces`, `guarantees`, `ensures` | Claims a property holds through an invariant, proof, or exhaustive enforcement under explicit assumptions. |
| `allows`, `enables` | Claims a rule permits an action or a necessary obstacle has been removed; name the action and obstacle. |
| `reduces`, `improves` | Claims a measured direction; name the metric, baseline, conditions, and magnitude when material. |
| `avoids`, `eliminates` | Claims an operation or failure no longer occurs within an explicit scope. |

Words such as `novel`, `first`, `efficient`, `lightweight`, `scalable`, `practical`, `secure`, `robust`, `significant`, `optimal`, `fundamental`, `all`, and `never` are claims, not decoration. Check their delta, metric, model, population, or exhaustive boundary. During revision, missing support calls for a separate issue note and an author decision about the claim; do not invent support or silently substitute a weaker property. For new drafting, select only properties the supplied evidence supports.

## Section contracts and reader layers

Use section names as containers for reasoning jobs, not as mandatory templates:

| Unit | Reader obligation |
|---|---|
| Title | Identify the object and distinctive advance without exceeding the paper's strongest supported conclusion. |
| Abstract | Deliver the smallest self-contained decision case appropriate to the contribution type, including decisive bounded evidence rather than a component or section inventory. |
| Introduction | Establish stakes, the decisive gap or question, the intellectual move, the concrete deliverable, implementation reality, and an evidence preview before demanding detailed mechanism knowledge. |
| Background | Teach only prerequisites used by a later claim, constraint, or design choice. |
| Motivation | Convert a credible observation or prior limitation into a fair, causal research requirement. |
| Overview | Show the model, governing principle, main dependencies, and important boundary before implementation inventory. |
| Design / method | Explain why each major choice follows, how it operates, which alternative it rejects, and which property or limitation results. |
| Implementation | Distinguish what exists, what is reused, what is incomplete, and which realization choices affect a claim. |
| Evaluation | Organize evidence around recoverable questions: end-to-end effect, attribution, cost, robustness, fairness, correctness or reality, and limits as applicable. |
| Figure / table / caption | Give the visual one argumentative job. A caption identifies the object and setting, states the supported takeaway, and preserves the material boundary. |
| Related work | Locate the delta along decision-relevant dimensions such as assumption, mechanism, guarantee, deployment condition, cost, or evidence. |
| Limitations | Expose conditions most likely to change a central conclusion, near the claims they constrain. |
| Conclusion | Compress the established thesis, transferable insight, demonstrated outcome, and boundary without introducing a new technical claim. |

## Concision

Concision preserves scientific judgment while reducing reading cost. Retain, in order of importance:

1. the controlling claim and its boundary;
2. premises required for that claim;
3. decisive causal or deductive links;
4. evidence that changes credibility;
5. definitions required to understand those items.

Within an existing paragraph, remove verbal redundancy and empty metadiscourse while preserving its substantive information and role. Make an implicit relation explicit only when that paragraph supports it; missing scientific premises require evidence or author input. Content deletion, transfer, or expansion beyond this boundary belongs to explicitly authorized composition or restructuring, not routine concision.

Remove duplicate status markers when one precise construction already carries the full meaning: for example, `we plan to evaluate` already marks an evaluation as future, so `in future work` is redundant unless its timing or placement matters. After deletion, the proposition must remain unambiguously planned, conditional, inferred, or established as before.

A claim may recur at different depths when its function changes: the abstract states it, the introduction derives it, the design realizes it, the evaluation tests it, and the conclusion transfers its lesson. Prefer a shorter phrasing when repairing actual redundancy; a merely shorter alternative to adequate prose remains optional.
