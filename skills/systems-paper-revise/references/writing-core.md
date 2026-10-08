# Canonical Systems-Writing Core

Review, Grill, and Revise use this single quality standard for the same scoped prose, including requested drafts.
Other references add specialized checks or control actions.
They do not change the meaning of clear, accurate writing with valid logic and evidence.
Use the [coverage contract](coverage-contract.md) for the required top-down audit and visible accounting.
Use the [shared workflow contract](review-revise-contract.md) for judgments that agree and uncertain-logic discussion.

## Top-systems calibration and editing authority

The stable standard for OSDI, SOSP, EuroSys, ATC, and ASPLOS writing has these elements:

- An important bounded problem or question
- A clear advance over the related baseline
- A technical realization or method with evidence for its claimed behavior
- Evidence matched to each claim
- Accurate costs and limitations
- Correctness and conclusions supported by evidence.

OSDI's [review criteria](https://www.usenix.org/conference/osdi27/call-for-papers) and the [systems-paper writing guide](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/good_paper.html) give the calibration.
Apply it through contribution type and each unit's delivered role.
A background paragraph can keep its background role without an introduction or evaluation role.

Accepted-paper patterns give functional expectations.
They do not impose one fixed template.
For a named venue, track, cycle, or submission-policy question, add the applicable official overlay through [venue rules](../../systems-paper-review/references/venue-overlays.md).
Keep page limits, anonymity rules, review stages, and preliminary calls out of this stable standard.

Paragraph-local revision is the author's editing limit for this project.
It is not an OSDI submission rule.
Quality criteria do not give permission for new research content or paragraph restructuring.
Use the [revision protocol](revision-protocol.md) for edit permission.
For submission-policy judgments, do a check of applicable venue rules.

Examine quality independently from edit permission.
An unsupported inference stays a scientific gap even when its initial words must stay.
A different expression alone is not a defect.
Use the shared contract for action on that judgment.

## The decision case

A systems paper gives a bounded scientific advance for the reader's acceptance:

```text
important problem or question under stated conditions
  → decisive constraint, gap, or unknown
  → intellectual move: principle, method, or finding
  → mechanism, study, proof, or artifact that realizes it
  → evidence that discriminates the claim
  → cost, assumption, limitation, and transferable consequence
```

This is a dependency spine, not a required sentence or section order.
Include only the roles necessary for each text unit's local obligation.
For unconventional or unclear contribution types, use [paper-archetypes.md](paper-archetypes.md).

Use two reading depths along the same claim hierarchy:

- A broad systems reader can find the problem, delta, intellectual move, evidence with correct methodology, and primary boundary.
  Give these elements in the title, abstract, introduction, overview, headline results, and conclusion.
- A domain expert can validate that account through the model, assumptions, invariants, lifecycle, implementation status, experimental controls, and failure cases.

The first two pages give a test for each venue.
They are not a universal submission rule.
Can a reader accurately retell the decision case without inventing a missing link?
Apply a requirement for specified pages only after verification of the named venue and cycle.

## High-level causal compression

`High-level` prose keeps causal structure and omits detail irrelevant to the reader's decision at this point.
At the highest level that answers the reader's question, make these elements clear:

1. **Object and condition:** The system, workload, model, population, or stage to which the statement applies
2. **Constraint or unknown:** The relation that defeats the old approach or prevents a conclusion
3. **Intellectual move:** The principle, boundary change, method, or finding that changes the problem
4. **Realization:** Sufficient mechanism, analysis, or study design to show evidence for the move
5. **Consequence and evidence:** The resulting property or conclusion and its evidence
6. **Boundary:** The cost, assumption, comparison scope, or failure condition that limits the conclusion.

Give a paragraph only elements related to its promised and delivered role.
A clear implicit link can stay implicit.
Do not add sentences only to expose each step or fill all six elements.
For a missing scientific premise, get author evidence.
Do not supply reviewer reconstruction as that evidence.

If evidence gives a binding constraint or failure relation, keep that relation clear.
Do not replace it with a weaker benefit expression.
Keep the affected operation, condition or frequency, and bottleneck or failure when they give the reason for the move's necessity.
An operation's placement at one component does not imply that it is serialized or invoked for each request.
Keep supplied serialization, synchronization, frequency, or cross-layer dependencies explicit in the causal compression.

Do four tests of each principle-level statement:

- **Distinction:** Replace its nouns with unrelated systems or methods as an internal test.
  If the proposition stays unchanged, it is too generic.
- **Prediction:** Find at least one important design, study, or proof choice that the statement predicts.
  Without such a choice, the principle is detached from the work.
- **Falsification:** Find a condition or observation in which the statement fails or narrows.
- **Evidence:** Find scoped proof, analysis, experiment, or observation that can support the stated consequence.

## Source-grounded intellectual-move fan-out

Reconstruction is a diagnostic tool, not an editorial repair.
Give each central node and causal edge one source status:

- **stated:** The prose clearly gives the node or relation.
  Use the shortest initial span as its anchor.
- **text-licensed:** The relation comes from premises and a dependency in the scoped text.
  The source can supply it without word-for-word repetition.
  Give the two endpoint anchors and the inference.
- **reviewer-hypothesized:** The relation could give the account a clear dependency chain.
  But the scoped text lacks a necessary premise or causal edge.

A `reviewer-hypothesized` bridge does not make the manuscript clear.
Review gives the specified missing edge.
Grill requests the author's confirmation or replacement and evidence.
Revise keeps it out of prose until scoped evidence or an evidence-compatible author decision supplies it.

If one insight, boundary change, or design choice yields several primary outcomes, make this **fan-out map**:

```text
problem or binding constraint -> intellectual move
intellectual move -> outcome A, through <causal layer and mechanism>
intellectual move -> outcome B, through <causal layer and mechanism>
intellectual move -> outcome C, through <causal layer and mechanism>
```

Use the number of outcomes claimed by the manuscript.
Give each edge its source status and initial-text anchors.
Source status records provenance, not validity.
`X provides Y` is `stated`, but it can lack the necessary causal layer, mechanism, or premise.

The shared-move account passes only when the move comes from source evidence.
Each advertised outcome must have an anchored dependency with a clear causal layer and counterfactual.
A shared system name, paragraph, component, or list in the same region shows co-occurrence.
It does not show causality.

Do two checks of each fan-out edge:

1. **Causal-layer attribution:** Give the step to the narrowest layer that supplies it.
   Possible layers include enabling substrate, abstraction/authority boundary, runtime enforcement/lifecycle, execution-path organization, and empirical condition.
   Do not credit one layer with a compound property that depends on another layer.
   An enforcement-friendly language can remove a bypass class.
   Alone, it does not show authorization, isolation, availability, or end-to-end performance.
   When the source requires several properties, explain each remaining obligation after an enabling property is supplied.
   Keep object-level requirements separate from proof work and from uncertain term equivalences.
   Do not infer that one fulfilled property satisfies or removes another independent duty.
2. **Counterfactual:** Keep the other stated assumptions fixed.
   Remove the proposed move or named layer as an internal reasoning test.
   Find the outcome or mechanism that no longer holds.
   If the source gives no answer, the edge is `reviewer-hypothesized`.
   If the outcome holds independently, it is not evidence for the move's unification of that outcome.

A paper can have several independent contributions.
Do not force them below one insight when the manuscript presents them independently.
The fan-out test applies when a paper claims, implies, or relies on one move for several headline properties.
It checks if prose completes that promised role or only groups independent mechanisms below one label.
This test governs causal outcome claims.
For an identified paragraph-local hierarchy defect below a supplied principle, apply the organization rule in [positioning-and-insight.md](positioning-and-insight.md).
That rule organizes stated design membership while keeping unproved outcome relations unresolved.

Keep these three levels as different categories:

- A **principle** changes a design or reasoning constraint, boundary, dependency, or assumption.
  It gives the reason that the change matters.
- A **mechanism or method** carries out the principle through an operation, state transition, algorithm, proof rule, sampling choice, or intervention.
- An **implementation detail** gives the specified realization: data structure, API, thread, parameter, tool, or code path.

If information order causes a specified comprehension defect, expose the existing controlling relation where it is necessary for comprehension.
Keep a clear progression and author emphasis.
A principle-first alternative to sufficient prose is optional.
Get clear restructuring permission for cross-paragraph or cross-section detail movement.

When repetition is an identified defect, separate the distinct premises from repeated statements of the same limitation or requirement.
If the source supplies a limitation and its design consequence, combine them into one progression.
Keep every distinct premise, condition, and consequence; remove only their repeated expression.
Check that the revised passage advances the argument rather than restating the same requirement with a new connective.
This repair applies to the identified repetition, while adequate surrounding prose stays unchanged.

Calibration:

> **Original:** “Each worker keeps a quota locally. Each worker keeps that quota locally so it can make admission decisions locally.”
>
> **Redundancy repair:** “Each worker keeps a local quota so it can make admission decisions locally.”

> **Original:** “Requests enter a local queue. A background thread submits them in batches.”
>
> **Decision:** Keep this adequate description. It does not establish reduced coordination overhead, latency, or a correctness guarantee. Adding one of those claims would change the scientific content.

These synthetic examples show editing decisions.
A component inventory without a supplied causal relation cannot become a supported principle through word changes alone.

## Paragraphs as inference units

A paragraph completes one local reasoning obligation.
It gives the reader one usable update about a problem, premise, mechanism, finding, evidence, or boundary.

- The **opening region** makes the obligation clear.
  It can give the claim immediately or first use a short bridge from the preceding paragraph.
- The **development** supplies only necessary definitions, reasons, mechanisms, evidence, comparisons, and qualifications.
- The **ending region** answers the obligation or transfers it to the next necessary question.
  It can give a result, implication, requirement, limitation, or clear handoff.
  It can end without repetition of the opening.

First and last sentences carry high information weight.
They are not fixed slots.
Mathematical continuations, bridge paragraphs, lists, and close derivations can end without a stated closing takeaway.
Examine if the obligation is clear and met.
A topic-sentence template is not required.

Let reasoning determine manuscript paragraph length.
Use these diagnostic signals:

- **Overfull:** Two independent conclusions, or context/mechanism/evidence/new-limitation mixtures without hierarchy
- **Fragmented:** Short neighboring paragraphs contain only setup, one number, or an empty transition
- **Level jumping:** Principle, source-code detail, and system consequence alternate without a stated relation
- **Citation inventory:** Names and citations collect without a comparison axis or author inference
- **Overcompressed:** A shorter version loses a condition, causal bridge, evidence scope, or boundary.

Overfull and fragmented states do not give permission for automatic paragraph splitting or combination.
During paragraph-local revision, keep boundaries and improve internal hierarchy where possible.
If that is insufficient, give the necessary structural change independently.
Split or combine paragraphs only for a clear restructuring request.
Then use reasoning roles, not sentence counts, to select boundaries.
A direct request to reorganize named overfull or fragmented paragraphs is such a request.
Verify the resulting boundaries; sentence compression alone cannot complete a required boundary repair.

Do this internal test: `This paragraph makes the reader believe ___ because ___.`
Two unrelated answers show competing obligations.
No answer shows an unclear argument role.
Neither result gives permission for a new purpose or invented content.

## Role, payoff, and evidence-state gates

Apply these checks independently.
A scientific-support risk does not clear an argument-role defect.
A sound rhetorical structure does not show scientific truth.

### Promise versus delivery

A heading, roadmap, opening claim, clear phrase, or author intent can signal a paragraph's promised role.
A clear phrase can be `our key insight`.
Record that role independently from the delivered role.
If an insight paragraph mainly lists operations, checks, or data structures, give the mismatch.
Calling it overview or mechanism gives the symptom.
It does not complete the insight role.

If no role signal exists in scope, set intended role to `not assessable`.
Still find the delivered role.

### One obligation and one payoff

Do the `believe ___ because ___` test.
Examine if each sentence helps show that update.
`also`, `however`, or `therefore` does not make an independent question subordinate.
An evaluation plan and a new architecture challenge usually give separate obligations.
They share one obligation only when the challenge clearly belongs to the plan's evidence logic.
Give that split diagnosis even when edit permission prevents movement.

For the ending, give its specified new information.
Do a deletion test.
If deletion loses no supported conclusion, boundary, design obligation, or necessary handoff, the ending is redundant or formulaic.
A `limitation -> requirement` ending has a shown limitation and a consequence of that design.
A repeated absence is not sufficient for that requirement.

Also do a mechanical-inversion test.
`does not provide X` changed to `must provide X` can repeat the same information.
An ending that only negates or makes a statement positive can have the same problem.
A passing payoff adds a supported consequence, constraint, choice, boundary, or handoff beyond that mechanical requirement.
A fixed contrast or conclusion phrase is not necessary.

### Compare the same kinds of claim

Keep a system property and the evidence work that shows it as different categories.
For a necessary-but-insufficient property claim, give the remaining property or invariant.
`cannot replace an argument/proof` compares behavior with manuscript evidence.
That comparison fits only when the sentence clearly discusses proof obligations.
Review the necessity claim and category defect independently.

Revise can fix a meaning-equivalent category defect while the necessity claim stays blocked.
If the sentence or immediate preceding context names the remaining properties, use those object-level properties in the comparison.
Keep the necessity claim at its initial strength.
Keep its evidence gap clear.
Do not leave the independent category defect merely because necessity evidence is unavailable.

### Related work must earn the research gap

For repository, build, or artifact comparisons, apply [positioning-and-insight.md](positioning-and-insight.md).
Give the specified actor, deployment-control, interface, or capability fact related to the comparison.
An audit trail is not automatically the proper manuscript abstraction.
For `A, B, and C have not appeared together`, give population coverage, parallel cells, and a causal bridge.
Hedges or fewer named examples do not supply that bridge.

Use one decision-related comparison dimension at a time.
Grammatical parallelism is insufficient when predicates compare different dimensions or levels.
If prior designs fail a new requirement, find this chain:

```text
fair comparison axis -> shared assumption/mechanism/constraint
  -> why it prevents the target property -> bounded unmet requirement
```

A boundary comparison can instead use a **distinct-question bridge**.
Parallel placements can motivate another contract or responsibility division without a failure claim about the alternatives.
Apply [interface-boundaries.md](interface-boundaries.md).
For this bridge, give a clear comparison axis and bounded resulting question.
It shows neither prior-work absence nor novelty.

Different boundaries or objects show descriptive contrast, not a shared root cause.
If that list leads to a negative gap without a supplied common cause, Review gives the missing causal bridge.
Revise requests author input.
Neither invents the cause.
If prose only gives a distinct question, do not demand a cause for an unclaimed failure.
A survey paragraph can stop at a clear comparison axis.

Do a check of negative prior-work claims independently.
Missing literature evidence must not hide an organization defect visible in the prose.
Do the `classification -> claimed gap or distinct question` test even without the excerpt's incoming antecedent or citations.
Keep scope and evidence blockers as different categories.

### Observations are intellectual updates, not requirement labels

For Observation, Insight, Requirement, or Design objective promises, apply [positioning-and-insight.md](positioning-and-insight.md).
For an observation or insight, give a source-grounded relation in addition to a definition.
That relation changes reasoning and predicts a design or evidence consequence.
A generic `determines` statement, desired-property list, or heading restatement does not complete that role.

Keep evidence observation, interpretation, insight, requirement, objective, and mechanism as different categories.
Give role mismatches or make them clear.
Do not fill them with reviewer-invented principles.

### Completed-paper prose answers with evidence

In a completed paper, `performance must be evaluated` gives a plan or placeholder.
It does not give an evidence-derived payoff.
For manuscript-review requests, use completed research-paper context by default.
Use proposal, roadmap, plan, or future-work context when the user or text identifies it.

If lifecycle stays unclear, give the completed-paper reading as a conditional risk.
Request the intended lifecycle state.
Do not pass the placeholder as a result.

If permitted results exist, give the bounded observed answer.
Include metric, baseline, conditions, and important uncertainty.
If results are unavailable, keep the evidence state accurate.
Request the result that the experiment supplied.
An instruction to assume experiments exist supplies no outcome.
Proposals, roadmaps, and future work can give planned evaluation.

Do not delete the comparison question, workload dependence, residual-cost boundary, or other proposition that the missing result must answer.
Dissatisfaction with a placeholder gives no withdrawal permission for those propositions.
Neither does an instruction to derive from assumed experiments.
If permitted evidence cannot replace the result-dependent payoff, keep the affected passage unchanged.
Give the necessary result tuple.
Remove a pure editorial TODO only when it has no scientific content and clear withdrawal permission exists.

### Place important boundaries near the claims they govern

A limitation can change important parts of the contribution's users, workloads, deployment model, semantics, or applicability.
Make the boundary clear in the abstract or introduction to prevent an overbroad first impression.
Detailed consequences can stay in Discussion or Limitations.
This placement judgment is conditional.
It does not give permission for text movement automatically.

For an isolated limitation paragraph, identify the affected broad-reader claim.
Set specified placement or wording to `not assessable` until that claim and its surrounding introduction are in scope.
Give this conditional judgment when the visible boundary seems important.
Give that judgment without waiting for a clear placement question.
Do not omit it only because the Introduction is not in scope.

## Identify roles and inspect links

Use initial-text anchors.
Give prose paragraphs IDs `P1`, `P2`, and sentences IDs `P1.S1`, `P1.S2`.
Use author labels or section/path anchors when available.
Source-file wraps are not paragraph breaks.
Read LaTeX paragraphs, lists, headings, display equations, and citation abbreviations according to their document syntax.
If extraction makes boundaries unclear, use short quotations instead of invented numbers.

For each paragraph, find its observable promised role and delivered content.
Record topic, role, claim/question, support, and closing takeaway.
Roles include background, problem, gap, principle, mechanism, implementation, evidence, comparison, limitation, and transition.
These are reading aids, not required headings or slots.
Record uncertainty, mixed roles, and promise-versus-delivery mismatch.
Do not replace author intent without an author decision.

Examine each adjacent sentence pair and clear longer dependency.
Find the first sentence's conclusion and the second sentence's necessary premises.
Find their relation: explanation, evidence, consequence, contrast, condition, example, qualification, or continuation.

Do a check of referents, objects, assumptions, comparison scope, and claim strength.
A connective cannot repair an unsupported inference.
A correct relation can be noncausal or have no transition word.

For each adjacent paragraph pair, compare roles and the first paragraph's closing claim with the second's opening premise/question.
Examine named nonadjacent dependencies too.
Do a check of missing premises, unsupported topic/abstraction changes, repeated reasoning, inconsistent assumptions, and overbroad conclusions.
A stated topic change or clear handoff is not a defect.
For one scoped paragraph, cross-paragraph logic is not assessable.

Give each faulty link's initial endpoints and missing or invalid relation.
If the defect is in a paragraph, use the supporting sentences in the scoped text as anchors.
Keep these anchors in findings or blocker notes.
Do not put them in revised manuscript prose.

## STE-derived clarity for research prose

Use [ASD-STE100](https://www.asd-ste100.org/about_STE.html) clarity rules for term, sentence, and paragraph checks.
Prefer familiar words and direct verbs when technical relations and evidence strength stay unchanged.
Replace nominalizations or unclear noun groups when they hide actors, actions, or relations.
Keep domain terms, official names, and identifiers that carry the specified technical meaning.

Two text types have different obligations in this skill.
The English skill instructions themselves use STE procedural and descriptive rules.
Use a maximum of 20 words per procedural sentence.
Give one instruction per sentence, except for simultaneous actions.
Use imperative verbs and put prerequisite conditions first.

For skill descriptions, use a maximum of 25 words per sentence and six sentences per paragraph.
Use active voice.
Rule 3.6 lets you use descriptive passive voice only when the agent is unknown.
Do not use semicolons in authored prose.
Count words according to Section 8.
Use its rules for parentheses, quotations, identifiers, titles, and hyphens.

For research manuscripts, the application is an adaptation, not a claim of full STE compliance.
STE combines writing rules with a controlled dictionary.
Its [FAQ](https://www.asd-ste100.org/STE_faq.html) lets writers use clarity principles in other contexts.
The manuscript's 25-word and six-sentence limits are inspection prompts, not quotas.
Find ambiguity in the scoped text, overload, or competing obligations.
Keep necessary qualifications, modality, dependencies, and paragraph-local edit limits.

Sufficient manuscript prose can stay unchanged.
A manuscript passive can keep an object/result focus that fits its role, without an invented actor.
This manuscript choice does not make a Rule 3.6 exception for skill instructions.
Do not call a word STE-approved without an official dictionary check of its part of speech and meaning.

When an explanation is requested, distinguish supplied dictionary evidence from project terminology.
Keep each approval claim within the entry's part of speech and meaning.
Report original and revised word or sentence counts when explaining a limit-related repair.
The [source registry](../../systems-paper-review/references/source-registry.md) records provenance and adaptation limits in [ASD-STE100].

## Sentence information structure

Give each manuscript sentence one **dominant assertion**.
Keep conditions, reasons, contrasts, and qualifications in that sentence when they directly organize its assertion.
If readers must accept two claims independently, divide the sentence.
Length alone is not the manuscript defect.

- Start with information available to the reader.
  Put important new information where it gets emphasis.
  Give referents and dependencies before dependent information.
  Several new terms are defective only when readers must guess their relations.
- Make the technically important actor and action clear before ambiguity can occur.
  Use `we` for author choices and the system/mechanism for system actions.
  In manuscripts, use passive voice when object/result focus is justified.
  Get the actor from scoped evidence.
  If an important actor is unknown, request clarification instead of inventing one.
- Keep modifiers, quantifiers, negation, comparisons, and conditions close to the propositions they limit.
- Put items at the same grammatical and conceptual level.
  Do not list an idea, implementation, and evaluation result as equivalent contributions.
- Repeat the same technical term when a synonym changes identity.
  Replace a pronoun or bare `this` when several antecedents are plausible.

Prefer simple clauses when they keep the relation.
Complexity helps when it makes one specified dependency clearer.
After splitting or simplification, compare actor, action, object, condition, ordering, negation, modality, comparison, and causal/evidential relation with the initial.
Each qualification must apply to the same proposition.
Short sentences are not clearer when they lose those bindings.

## Logical and lexical precision

Do term checks in the two directions.
Keep one stable name for each concept.
Keep each term's intended meaning in its specified context.
Keep clear aliases, subtypes, and contextual distinctions.
Combine names only when scoped text or author-confirmed meaning shows identity.
Words that look the same do not show the same mechanisms, properties, or metrics.

If a distinction is missing, put it in `author clarification`.
Do not remove distinctions during revision for verbal simplicity.
Divide propositions with different evidence requirements:

- An **observation** gives what data or an artifact shows.
- An **explanation** gives a cause for that observation.
- A **design prediction** gives an expected consequence of a mechanism or principle.
- A **conclusion** gives what the full evidence supports.

Temporal correlation alone does not show explanation.
A mechanism prediction alone does not show conclusion.
Keep different meanings for `necessary` and `sufficient`.
`X requires Y` makes Y necessary.
`Y guarantees X` makes Y sufficient when the stated assumptions hold.

Use transitions only for supported cause, consequence, contrast, condition, example, qualification, or handoff relations.
Premises before `therefore` must support its conclusion.
Clauses around `however` must have a supported contrast.

Keep comparison problems equivalent.
Give the entities, objective, metric, semantic guarantee, resources, conditions, and baseline necessary for a comparison that answers the claim.
If weaker semantics or transferred cost causes a benefit, put that difference beside the result.

Keep conclusions in the measurement object:

- A microbenchmark measures an operation.
- A simulation shows claims in its model.
- A mean does not give a tail.
- One deployment shows bounded feasibility.
- An executable artifact alone does not reproduce each paper claim.

Select manuscript verbs by technical relation and evidence strength.
The quoted forms below are scientific terms for analysis, not a list of STE-approved verbs:

| Verb class | Commitment |
|---|---|
| `observes`, `measures`, `finds` | Gives evidence without a claim of causality. |
| `suggests`, `indicates` | Gives a bounded inference with alternatives open. |
| `shows`, `demonstrates`, `establishes` | Claims direct evidence for the stated conclusion. |
| `implements`, `builds` | Claims that the realization exists. Its implemented extent must be clear. |
| `enforces`, `guarantees`, `ensures` | Claims an invariant, proof, or exhaustive enforcement with clear assumptions. |
| `allows`, `enables` | Claims permission for an action or removal of a necessary obstacle. Give the action and obstacle. |
| `reduces`, `improves` | Claims a measured direction. Give metric, baseline, conditions, and important magnitude. |
| `avoids`, `eliminates` | Claims operation/failure absence in clear scope. |

Treat these manuscript words as claims, not decoration:

- `novel`, `first`, `efficient`, `lightweight`
- `scalable`, `practical`, `secure`, `robust`
- `significant`, `optimal`, `fundamental`, `all`, `never`.

Do a check of their delta, metric, model, population, or exhaustive boundary.
For revision, give missing support as a different issue and get the author's claim decision.
Do not invent evidence.
Do not use a weaker property without an author decision.
For new drafts, select only properties supported by supplied evidence.

## Section contracts and reader layers

Section names contain reasoning obligations.
They are not required templates.

| Unit | Reader obligation |
|---|---|
| Title | Identify the object and distinctive advance in the strongest supported conclusion. |
| Abstract | Give the smallest self-contained decision case for the contribution type. Include decisive bounded evidence rather than a component/section inventory. |
| Introduction | Give stakes, gap/question, intellectual move, deliverable, implementation status, and evidence preview before detailed mechanism knowledge is necessary. |
| Background | Give only prerequisites used by subsequent claims, constraints, or design choices. |
| Motivation | Use an observation or limitation with evidence to give a fair causal research requirement. |
| Overview | Give the model, principle, primary dependencies, and important boundary before the implementation inventory. |
| Design / method | Give each important choice's reason, operation, rejected alternative, and resulting property or limitation. |
| Implementation | Distinguish existing, reused, and incomplete parts. Give realization choices that affect claims. |
| Evaluation | Organize evidence around related end-to-end, attribution, cost, robustness, fairness, correctness/reality, and limit questions. |
| Figure / table / caption | Give one visual argument role. Give object, setting, supported takeaway, and important boundary in the caption. |
| Related work | Locate the delta in related assumptions, mechanisms, guarantees, deployment conditions, costs, or evidence. |
| Limitations | Give conditions most likely to change a central conclusion, near the affected claims. |
| Conclusion | Give the shown thesis, usable insight, demonstrated outcome, and boundary without new technical claims. |

## Concision

Concision keeps scientific judgment and reduces reading cost.
Keep these items in this importance order:

1. The controlling claim and boundary
2. Premises necessary for that claim
3. Decisive causal or deductive links
4. Evidence that changes credibility
5. Definitions necessary for those items.

In an existing paragraph, remove verbal redundancy and empty metadiscourse.
Keep substantive information and role.
Make an implicit relation clear only when that paragraph supports it.
For missing scientific premises, get evidence or author input.
Get clear composition or restructuring permission for content deletion, movement, or expansion beyond that limit.

Remove duplicate status words when one expression carries the full meaning.
`we plan to evaluate` identifies future evaluation.
`in future work` is redundant unless its timing or placement matters.
After deletion, keep the proposition clearly planned, conditional, inferred, or shown as before.

A claim can recur at different depths when its function changes.
The abstract states it, introduction derives it, design carries it out, evaluation does its test, and conclusion gives its lesson.
Use shorter words for redundancy repairs with evidence in the text.
A shorter alternative to sufficient prose stays optional.
