# Adversarial Review Protocol

For each review, use this protocol's scope, evidence, finding-calibration, and gate rules. The [shared coverage contract](../../systems-paper-revise/references/coverage-contract.md) controls inventory, order, unit states, ledgers, and completion receipts.

Use the full pass record and expanded finding schema for full reviews, formal ledgers, or submission gates. For local reviews, use the shared coverage contract's compact ledger, short finding explanations, and receipts.
For a local review, the shared contract's four-part report order replaces the separate report sections below.
Keep their applicable fields in the canonical records.

Domain references give the individual `PA`, `TH`, `RC`, `DD`, `TS`, `EV`, `ER`, `AR`, `SS`, `PT`, `FL`, and `VO` rules or routing contracts.

For large amounts of parallel work, use [multi-agent-orchestration.md](multi-agent-orchestration.md) role assignments. Parallelism leaves evidence requirements and scope-specific reporting unchanged.

Before manuscript judgments, give coverage for each version of the authorized decision record through the shared workflow contract. Keep decision accounting and manuscript evidence as different report parts.

## 1. Scope contract

Before inspection, record scope. Give it in the report. Keep it unchanged during review.

| Scope supplied | Inspect | Do not inspect | Context handling |
|---|---|---|---|
| Pasted sentence or paragraph | Only pasted text | Attachments, repository, adjacent manuscript | Use `needs context` for missing antecedents, definitions, evidence, or references. |
| Named file | That file and safe rendered output | Imported files, bibliography, figures, code | Open links or includes only with different scope authority. |
| Named `main.tex` or other LaTeX root | Only that root. Read dependency names for scope requirements. | `\input` or `\include` files, bibliography, figures, class or style files, build configuration | Give the necessary dependency manifest. Keep it `needs context` until authorized. |
| Named file set | Exactly those files | Other repository files | Compare only named files. |
| Clear whole LaTeX project | Root and explicitly authorized transitive manuscript dependencies necessary for rendering | Unused repository files, unrelated artifacts, code, or data | Before review, record the unchanged dependency manifest. Give missing or external dependencies. |
| PDF | Visible or extractable PDF content | LaTeX source and artifacts | Give extraction uncertainty. Use page, section, or figure locations. |
| Named figure or table | Object, caption, and explicitly supplied callout text | Other sections | Give visual defects and missing-context risks their corresponding status. |
| Named code, data, or scripts | Named paths and safe derived observations | Other artifacts or paper | Get evidence for submitted or evaluated version identity. |
| Whole paper, project, or repository | Requested manuscript and artifact objects | External systems and accounts | Give exclusions and tool limits. |

Use these scope rules:

- Do not use accessibility as scope authority. Easy file access does not increase scope.
- For “this paragraph,” keep cited papers and adjacent paragraphs outside scope. External checks can address only manuscript claims in that paragraph.
- For “the paper,” keep artifacts outside scope unless the user gives artifact-review authority.
- For “the project,” include manuscript and artifacts only if the user gives that scope clearly. If unclear, give the chosen interpretation.
- For `main.tex` alone, do a file review. For a full LaTeX project, include only the necessary authorized manuscript dependencies.
- If ambiguity changes important parts of the work, give one short scope question. In other cases, use the narrowest reasonable interpretation. Give that interpretation.

Before any command check, read the [command-evidence procedure](multi-agent-orchestration.md#5-give-command-producing-evidence-through-the-root).
Those scope, isolation, manifest, and side-effect checks apply to single-agent reviews too.
If their prerequisites are unavailable, use `not assessable` without command execution.

## 2. Evidence classes

Give each finding one or more evidence classes.

| Code | Evidence | Valid use | Invalid leap |
|---|---|---|---|
| `M` | Displayed manuscript text, equation, table, figure, or citation | Show manuscript statements or omissions | Citation markers treated as proof of source evidence |
| `A` | Code, data, script, log, build, or test observation in scope | Examine implementation and reproduction claims | One run generalized to all environments, or code presence equated with correctness |
| `X` | Verified external primary or official source | Correct venue rules, bibliography, or prior-work capabilities | Search snippets, secondary summaries, or outdated calls treated as definitive |
| `I` | Clear inference from `M`, `A`, or `X` | Predict a reviewer attack with evidence | Inference presented as observed fact |
| `U` | Evidence unavailable within scope | Give unresolved risk and context requirements | Confirmed defect dependent on unavailable material |

For external checks, record the source, direct URL, and applicable publication or venue cycle. If sources disagree, give the disagreement.

### Argument-state overlay

For notes, unfinished drafts, or promises beyond visible evidence, give each candidate proposition one state:

- `established`: Direct evidence from authorized manuscript, artifacts, or a permitted verified source.
- `inference`: A conclusion from established premises with corresponding claim strength.
- `planned`: A proposed mechanism, experiment, result, citation, or writing move without finished evidence.
- `blocked`: A requirement for new data, source, mechanism detail, context, or author decision.

Keep fluent narrative from converting `planned` or `blocked` material into established contributions. This overlay gives claim boundaries for the manuscript state. It does not authorize manuscript prose creation.

## 3. Finding status

Use exactly one primary status.

### Confirmed defect

Material in scope shows a failure. Examples include contradiction, unsupported local claims, invalid inference, wrong arithmetic, missing verified requirements, unresolved local references, misleading graphs, broken LaTeX, and language errors.

### Unresolved reviewer risk

Evidence gives a possible reviewer attack. Confirmation makes unavailable context, evidence, execution, expert judgment, or author intent necessary. Give the smallest necessary evidence or context item. `Needs context` is a subtype. It does not remove the issue.

### Style preference

Multiple formulations are correct. Their choice concerns readability, house style, or presentation. A preference becomes a defect with ambiguity, inconsistency, policy violation, or reading cost that affects comprehension.

Keep missing support for an asserted in-scope claim unresolved. Missing larger paper context is `not assessable` unless a visible claim or promised role depends on it. Do not convert an optional reconstruction into an author task. Do not treat unsupported scientific conclusions as style preferences.

### Diagnostic dimension

Give each finding one or more dimensions: `argument role/organization`, `scientific/technical support`, `language/presentation`, or `scope/authority`. Examine the dimensions independently.

Missing-evidence risks cannot replace visible role mismatches, nonparallel comparisons, redundant payoffs, or mixed paragraph obligations. Rhetorical defects alone do not prove scientific claims false. Keep both findings at the same anchor where both apply.

## 4. Severity and confidence

Severity measures likely decision consequence. Repair effort does not select it.

| Severity | Decision test | Typical examples |
|---|---|---|
| `S0 — blocker` | Independent rejection or desk-rejection basis, or invalid central conclusion | Fabricated or contradictory results. Verified policy violation. Central claims without correct evidence. Fatal technical defects. |
| `S1 — major` | Large score or confidence loss for a primary contribution | Unclear novelty. Unfair baselines. Missing assumptions. Missing central evaluation. |
| `S2 — moderate` | Weaker local arguments or repeated reader doubt | Unexplained design choices. Incomplete metric definitions. Repeated term conflicts. |
| `S3 — minor` | Local correctness or clarity defect with limited decision consequence | Grammar errors. Caption ambiguity. Isolated format defects. |
| `S4 — preference` | Optional change without correctness consequence | Valid word choices or layout alternatives. |

Use `high`, `medium`, or `low` confidence:

- `high`: Direct evidence in scope or a verified official rule.
- `medium`: Strong inference with a clear dependency.
- `low`: An attack with evidence and large dependence on context.

High confidence does not replace missing evidence. For large potential consequences, record high-severity, low-confidence risks only with a clear missing test.

## 5. Top-down unit audit

After scope definition, make the full unit and adjacency inventory from the coverage contract. Start with the paper archetype and evidence chain where assessable. Then examine each section, paragraph, sentence, and lexical occurrence in reading order.

Before bottom-up reconciliation, give each unit and link one coverage state. Continue after severe findings. A findings-only list is not a coverage record.

The hierarchy accounts for each unit's inspection in context. Independent passes give different scientific and reader perspectives. Complete both.

## 6. Independent passes

Do all applicable passes in different checks. Update shared unit ledgers. Continue review after initial severe findings.

### Pass P1 — scope, parsing, and surface integrity

- Make sure that input is readable and extractable. Record language and locations. Examine references and corruption.
- Make the inventory of sections, figures, tables, citations, claims, and artifact objects in scope.
- Apply the necessary `PT` and `FL` rules.

### Pass P2 — PC/chair contribution case

- Select the primary archetype. Make a reconstruction of the controlling thesis and claim hierarchy. Use empirical or operational contracts where applicable.
- Give each central node and dependency a source label: `stated`, `text-licensed`, or `reviewer-hypothesized`. Give original anchors. Do not use reviewer reconstruction as evidence for prose clarity.
- If the supplied scope presents competing stories, compare their primary claims, decisive evidence, missing evidence, and scientific tradeoffs. Keep necessary intent-changing choices unresolved. A local fragment without a complete paper decision case does not require the author to choose the entire paper's contribution type.
- Find the consequential problem or question, failed assumption or limiting constraint, and intellectual move. Find the deliverable or finding, decisive evidence, and systems-audience importance.
- Compare novelty with the closest alternatives. A generic field summary is insufficient.
- Apply assessable `PA`, `TH`, and `RC` rules and venue criteria.

### Pass P3 — domain-expert technical attack

- Make the derivation reconstruction: failure or property → constraint → requirement → mechanism → invariant or effect → tradeoff → decisive test.
- Make the system model, lifecycle, failure behavior, and assumption reconstruction.
- If one move supposedly causes multiple properties, make the source-grounded fan-out map. Give each edge its narrowest causal layer. Apply the counterfactual. Keep substrate, authority, runtime enforcement, lifecycle, execution paths, and empirical conditions different where necessary.
- Find counterexamples, hidden state, concurrency gaps, failure gaps, unsafe generalization, and mechanism-claim mismatch.
- Apply `DD` and `TS` rules.

### Pass P4 — evaluation skeptic

- Before result emphasis, predict decisive evidence from the thesis. Make the claim-to-evidence matrix. Compare headline results with contribution hierarchy.
- Examine questions, baselines, workloads, metrics, setup, uncertainty, negative results, and conclusion strength.
- Apply `TH`, `EV`, and `ER` rules. If artifacts are in scope, apply `AR`.

### Pass P5 — non-specialist systems reader

- Read sequentially. Use only stated or text-licensed domain knowledge.
- For each paragraph, record its signaled or author-supplied role. Independently give the delivered role through the writing core. Apply the coverage contract's promise-evidence gate before classifying a role mismatch as a finding.
- Complete the one-obligation sentence. Compare each sentence with it. Apply the ending deletion and information-gain tests.
- Examine sentence pairs, paragraph handoffs, and stated longer dependencies. Keep both endpoints for failed links.
- Record first uses, antecedents, the problem-to-move-to-realization sequence, opening promises, closing implications, and handoffs. Record section transitions, examples, callouts, headline payoffs, and cognitive load.
- For negative-gap related work, find the fair comparison axis and shared causal constraint. Descriptive categories alone are insufficient.
- For finished-paper prose, keep evidence-based answers different from evaluation placeholders.
- For artifact positioning, use [positioning and intellectual-move contract](../../systems-paper-revise/references/positioning-and-insight.md). Do a check of the difference between artifact facts and capability claims. Examine conjunctive gaps independently. Compare intended Observation or Insight roles with delivered roles.
- If one insight, boundary, or choice accompanies multiple primary outcomes, examine each move-to-outcome edge with reader-visible premises. Record the first reviewer-hypothesized edge. Shared labels or paragraphs do not show causal fan-out.
- For broken arguments, make a read-only reader-obligation outline. Give entering questions, claims or answers, necessary mechanisms or evidence, and closing implications or handoffs. Find the first broken dependency. Keep replacement prose outside that outline.
- Apply `TH`, `ER`, `SS`, `PT`, and applicable `FL` rules.

#### Mandatory prose-trigger checkpoint

For each matching paragraph, give each applicable trigger a clear `pass`, `finding`, or `unresolved` result. Apply the checkpoint during general prose review without a special diagnostic request.

| Trigger | Required independent test | Invalid result with missing context |
|---|---|---|
| Limitation → `however/but` → `therefore/to use X the system must ...` | Compare propositions. Examine new constraints, consequences, selection criteria, or handoffs. Find mechanical inversion of the preceding absence. | A nonredundancy claim based only on lost clear wording. |
| Related-work taxonomy or boundary list → negative gap or question | Use the [interface-boundary contract](../../systems-paper-revise/references/interface-boundaries.md). For negative gaps, get shared cause and evidence. For different questions, make sure that the map is parallel and the question is bounded. Examine novelty in different checks. | Questions treated as proof of absence. Invented causes for unclaimed failures. Local bridges excluded from inspection because antecedents or sources are unavailable. |
| Prior-work sentence centered on repository, build, link, configuration, or artifact fact | Use [artifact-to-capability distillation](../../systems-paper-revise/references/positioning-and-insight.md). Find actor, changeable object, stage, control, and comparison-axis consequence. Examine realization detail's decision function. | True artifact facts treated as manuscript-ready. Deployment conditions removed during abstraction. |
| Properties absent `together`, `simultaneously`, or in one inspected design | Apply the conjunctive-gap test. Examine population coverage, parallel property cells, negative evidence, shared causal constraint, and permitted requirement or question. | Tuple absence, bounded-system hedges, or desirable property conjunctions treated as causal gaps or novelty. |
| Observation, Key observation, Insight, Requirement, or Design objective paragraph | Use the observation ladder. Give delivered role, source anchor, non-definitional relation, information gain, and prediction. Examine independent goals in a different check. | Definitions, requirement restatements, mechanism lists, or vague `these differences show` bridges passed as promised intellectual moves. |
| Interface, customization, protection, isolation, or direct/delegated path claim across axes | Make the semantic-commitment, protection/authority, and execution-path ledger. For customization, give actor/artifact/stage/control. For compound protection, give the responsibility chain. | One axis as proof of another. One mechanism as cause of compound properties. Requirements for unclaimed axes. |
| Research-paper benefit prediction → `must be evaluated`, `remains to be tested`, or equivalent | Select manuscript state. Use research-paper context unless user or text specifies a proposal, plan, or future-work document. If still ambiguous, give conditional finished-paper-placeholder risk. Keep a clean result unavailable. | Placeholder passed solely for epistemic caution. |
| Limitation of users, workloads, deployment, semantics, or compatibility that affects the headline contribution | If the limitation qualifies the headline contribution, give a conditional early-disclosure judgment. Short disclosure belongs at broad readers' first claim encounter. Detail can occur subsequently. Without context, keep specified wording, duplication, and placement not assessable. | Conditional judgment omitted because Introduction is outside scope or placement was not requested. |
| One insight, boundary, or choice with multiple primary outcomes, or thesis reliance on unity | Make the source-grounded fan-out ledger. Give anchors for move and outcomes. Give each edge `stated`, `text-licensed`, or `reviewer-hypothesized`. Give its narrowest causal layer. Apply the counterfactual. | Unification passed from reviewer invention, shared paragraphs, or common system labels. |

These triggers are diagnostic aids, not sentence templates. Present required relations can give a pass. Give each result its diagnostic dimension: argument or organization, evidence, external truth, scope, or authority.

### Pass P6 — internal and artifact consistency

- Within scope, compare names, numbers, units, claims, captions, tables, equations, code, configuration, and scripts.
- Give each mismatch its class: paper-to-paper, paper-to-artifact, or artifact-to-result.

### Pass P7 — hostile counter-review

For each central claim, complete these prompts:

- “This is not important because …”
- “This is not new because …”
- “This mechanism may fail when …”
- “This experiment does not establish the claim because …”
- “This comparison is favorable for an avoidable reason because …”
- “This result may not generalize because …”
- “I cannot reproduce or audit this because …”

Keep attacks only with evidence or unresolved-risk status and a resolution test.

### Pass P8 — deduplication and omission audit

- Combine findings with identical root causes. Keep each affected location.
- Divide findings with different repairs or decision consequences.
- Make a finding-by-dimension table. For paragraphs with only unresolved evidence findings, re-examine argument role, obligation, parallelism, and payoff information gain in different checks.
- Compare trigger results. Make sure that each matching paragraph has a visible result for each matching trigger.
- Examine again paragraphs defended only by clear wording, unknown manuscript state, missing Introduction, unavailable prior-work context, or reviewer reconstruction. Those defenses leave content tests or conditional judgments unfinished.
- Re-examine thesis, supporting claims, primary mechanisms or findings, decisive results, and applicable rule families.
- Make sure that `no finding` means inspected and passed.

## 7. Rule application record

For each family, record one state:

- `applied — findings`
- `applied — no findings`
- `not assessable — out of scope`
- `not assessable — missing evidence`
- `not applicable`

Give coverage for not-assessable families before full-coverage claims. Coverage is relative to the defined scope and available evidence.

For formal or full reviews, give all family states. For local reviews, show the unit ledger and receipt. Family rows can stay internal unless missing context changes findings or the gate.

## 8. Layered finding schema for full or formal reviews

For full or formal reviews, use the full structure for each `S0`/`S1` finding. Use it also for lower-severity findings with non-obvious diagnosis, evidence, or repair.

For local reviews, use short root-cause bullets with the same reasoning. Do not include unused fields and rule IDs. Keep per-unit coverage ledgers full.

```text
[F-###] Short diagnostic title
Rule: <stable rule ID and name>
Location: <page/section/paragraph/line/figure/table/path or quoted anchor>
Status: <confirmed defect | unresolved reviewer risk | style preference>
Next action: <direct repair | author clarification | author evidence | external blocker | optional/not applied>
Dimension: <argument role/organization | scientific/technical support | language/presentation | scope/authority; one or more>
Severity: <S0 | S1 | S2 | S3 | S4>
Confidence: <high | medium | low>
Evidence: <M/A/X/I/U labels followed by the observable basis>
Reviewer attack: <the strongest concise objection a reviewer could make>
Why it matters: <affected claim, decision criterion, or reader inference>
Repair direction: <what must change or be supplied; no replacement prose>
Resolution test: <observable condition that closes the finding>
Sources: <rule source keys; add a live source URL for external facts>
```

Keep finding numbers stable within the report. Give only the shortest quotation necessary for location identity.

### Sentence and paragraph logic findings

For each relational finding, give both original endpoints. Use `P2.S2 → P2.S3` for sentence links and `P2 → P3` for paragraph handoffs. Add section or path anchors where necessary.

Give a short identifying quotation from each endpoint. If paragraph evidence lies beyond boundary sentences, also give those sentence locations. If segmentation is uncertain, use two quotation anchors. Do not invent indices.

Record the first unit's conclusion, second unit's assumption or conclusion, expected relation, and failed relation. Give the defect type: unsupported cause or conclusion, contradiction, scope or referent change, missing premise, disconnected topic, or optional transition.
When a connective or category has a separate wording defect, state the permitted local repair boundary separately from missing scientific support or content movement. Removing an inaccurate connective alone does not validate the conclusion. Do not require author evidence for an independently supported wording diagnosis.

Give the reader consequence. Give the minimum repair or evidence test. Use this compact pattern where this helps interpretation: `endpoint pair + anchors — status/severity; failed relation and consequence; repair boundary`.

Examine each adjacent pair internally. Report defects with evidence or unresolved risks only. Invented causal relations or connectives are not necessary for correct topic transitions.

Keep unavailable neighbors not assessable. A one-paragraph review can examine sentence links. It cannot show paragraph-to-paragraph coverage.

Give sentence-link and paragraph-link findings their different link levels. For grouped causes, list each affected pair. For multiple-paragraph logic review, give a short map of delivered paragraph functions. Keep that map outside manuscript prose.

For content transfer, paragraph division or combination, or role changes, give the clear restructuring-authority requirement. The diagnosis does not authorize automatic revision.

For `S2`/`S3` findings with one cause, use a short row:

| ID | Rule | Location | Dimension | Status / severity / confidence | Next action | Problem and consequence | Repair / resolution test |
|---|---|---|---|---|---|---|---|

Short form must still give full finding coverage. Give more detail where evidence class, attack, or scientific consequence would stay unclear. Put repeated symptoms in one cause with all locations.

## 9. Report schema

### Editorial decision brief

Use this separate brief for full or formal reviews.
For local reviews, record scope and inventory first, findings once, and the verdict in the manuscript receipt.

- Scope and evidence limits that affect conclusions.
- Primary and secondary archetypes, plus unresolved routing choices.
- One-sentence thesis reconstruction in reviewer language. If impossible, give the reason.
- Verdict and corresponding confidence.
- Argument strengths with evidence that help revision. Include only consequential examples, claims, figures, results, or passages.
- The smallest set of rejection threats sufficient for the verdict. The ledger gives full coverage.

Use one verdict:

- `clear within scope`
- `actionable issues remain`
- `blocked by missing evidence/context/author decision`

Add one paragraph with the decisive reason and confidence. Keep `clear within scope` different from publishability claims.

### Thesis, design, and evidence diagnosis

- For argument-bearing scope, give the claim hierarchy and reader-memory result.
- For multiple outcomes from one move, give the dependency records. Include move, outcomes, anchors, causal layers, source states, counterfactuals, and gaps. Keep a central reviewer-hypothesized edge as a finding or unresolved risk when an in-scope claim requires it. Otherwise record the larger reconstruction as not assessable. For local scope, integrate these records into the compact ledger in the shared coverage contract.
- For design-bearing scope, give derivation breaks.
- For evaluation-bearing scope, give headline-evidence mismatches.
- For unfinished material, keep established, inferential, planned, and blocked propositions different.
- For competing stories, give alternatives and scientific tradeoffs. Keep author-intent changes unresolved.
- For a hierarchy defect, give the archetype, thesis, evidence, and reader-obligation structure necessary for repair. Give required restructuring and authority. Keep replacement prose outside review.

For local reviews, put these applicable diagnosis fields in their owning unit or dependency rows.
Reference the source anchors and finding entries for facts already recorded.
Give a separate reconstruction blueprint only when it adds a required restructuring choice or authority boundary.
Each such entry must add information beyond the canonical ledger.

### Exhaustive findings ledger

For full or formal reviews, give all different findings in severity order. Within severity, use reading order. Give each finding's diagnostic dimension. Keep argument and evidence findings different where both apply.

Use the full schema for severe or non-obvious findings. Use short rows for findings with one cause. Give style preferences that help revision last.

For local reviews, keep the same root causes and dimensions in short bullets. Do not include this different report section.

### Per-unit coverage ledgers

Before findings, give paper, section, paragraph, sentence, relation, and lexical rows from the coverage contract. Keep reading order. Show passed units. For local scope, its compact ledger is the single display of these rows and all applicable domain-map fields.

For each paragraph, give intended role where visible, delivered role, obligation result, and opening, development, and payoff comparison. Include ending information gain. Keep mixed roles, unclear roles, and role mismatches visible.

For large scopes, use numbered batches if necessary. Keep the result `incomplete` until final rows and receipts are delivered.

### Claim-evidence matrix

For each central claim in scope in a full or formal review, fill this table:

| Claim | Type | Stated evidence | Evidence class | Coverage | Open attack |
|---|---|---|---|---|---|

Use `covered`, `partially covered`, `unsupported`, or `not assessable`.

### Coverage summary

For full or formal reviews, give P1–P8 states and applicable rule-family states. Include archetype, thesis, derivation, and argument-object coverage where applicable. Give not-assessable rules or objects and reasons.

For each review, give manuscript and decision receipts last. Different pass and family inventories are optional in a local review. It must give unit totals, last-unit states, not-assessable reasons, `Unreviewed`, and `Unaccounted decisions` counts.
For local reviews, verify that each required field appears once or resolves through a source-specific reference.
Complete all domain checks before this reporting check.
Stop adding report sections when the canonical records, finding tests, and receipts contain all required information.

### Gate result and next evidence

Give the gate result. For each blocker, give the smallest necessary experiment, source, context, artifact, or author decision. Use only results with evidence.

## 10. Anti-patterns

Keep these behaviors outside review:

- Fixed counts of three strengths and three weaknesses without evidence.
- Numerical averages that cancel independent fatal defects.
- Prose quality as compensation for missing central evidence.
- Rejection based only on preferred templates, voice, graphs, or statistics.
- Paragraph-local absence treated as full-paper absence.
- Searches for extra defects in unrequested files.
- Silent prose repair.
- Termination after severe defects, findings-only coverage, or spot-check completion claims.
- Readiness claims based only on automated checks.

## Sources

The protocol uses [OPENAI-SKILL-CREATOR], [DEERFLOW-REVIEW], [CHAN-DUAL-LENS], [LEVIN-REDELL], [OSDI-CFP], [SOSP-CFP], and [FIVE-VENUE-CORPUS]. It also uses [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [USER-NOTES], and [SYSTEMS-GUIDE]. See [source-registry.md](source-registry.md).
