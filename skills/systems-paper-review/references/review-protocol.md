# Adversarial Review Protocol

Use the scope, evidence, finding-calibration, and gate rules in this protocol for every review. The [shared coverage contract](../../systems-paper-revise/references/coverage-contract.md) controls inventory, top-down order, per-unit states, visible ledgers, and the completion receipt. Use this protocol's full pass record and expanded finding schema only for a full review, formal finding ledger, or submission gate. A local review keeps finding explanations compact but does not hide passed units or omit the coverage receipt. Domain reference files define the individual `PA`, `TH`, `RC`, `DD`, `TS`, `EV`, `ER`, `AR`, `SS`, `PT`, `FL`, and `VO` rules or routing contracts.

For a large scope reviewed with collaboration tools, execute the applicable passes through the role assignments in [multi-agent-orchestration.md](multi-agent-orchestration.md). Parallelism does not change the evidence requirements or the reporting surface appropriate to the frozen scope. Before judging manuscript units, resolve and classify every version in the authorized paper decision record through the shared workflow contract; keep that read-only accounting separate from manuscript evidence.

## 1. Scope contract

Freeze scope before inspection. Record it in the report.

| Scope supplied | Inspect | Do not inspect | Context handling |
|---|---|---|---|
| Pasted sentence or paragraph | Only pasted text | Conversation attachments, repository, surrounding manuscript | Mark missing antecedents, definitions, evidence, or references as `needs context` |
| Named file | That file and its rendered form if rendering is safe | Included/imported files, bibliography, figures, code | Do not follow links or includes unless separately named |
| Named `main.tex` or other LaTeX root file | Only that root file; parse dependency names only to identify needed scope | `\input`/`\include` files, bibliography databases, figures, class/style files, build configuration | List the dependency manifest needed for a full-paper gate and mark it `needs context` until authorized |
| Named file set | Exactly those files | Other repository files | Cross-file checks only among named files |
| Explicit whole LaTeX project | The root plus the explicit transitive manuscript dependency closure required to render it | Unused repository files, unrelated artifact/code/data | Freeze the dependency manifest before review; report missing or external dependencies |
| PDF | Visible/extractable PDF content | LaTeX source and artifact | Report extraction uncertainty; use page/section/figure locations |
| Named figure/table | Graphic/table, caption, and explicitly supplied callout text | Other paper sections | Separate visual defect from missing-context risk |
| Named code/data/scripts | Those paths and safe derived observations | Rest of artifact or paper | Do not infer that inspected code is the submitted or evaluated version |
| Whole paper/project/repository | All requested manuscript/artifact objects | External systems/accounts | State exclusions and tool limitations |

Rules:

- Accessibility is not authorization. Do not expand scope because files are easy to open.
- A request to check “this paragraph” does not authorize checking cited papers or neighboring paragraphs. External verification is limited to factual claims inside that paragraph.
- A request to check “the paper” does not automatically include its artifact. A request to check “the project” may include both only if the user's wording makes that clear; otherwise declare the interpretation.
- A request naming only `main.tex` is a file review, not a full-paper review. A request explicitly naming the whole LaTeX project authorizes only the transitive manuscript dependencies needed for that paper, not every repository file.
- If scope is genuinely ambiguous and alternatives would materially change work, ask one concise question. Otherwise choose the narrowest reasonable interpretation and state it.

## 2. Evidence classes

Assign one or more evidence classes to every finding.

| Code | Evidence | Valid use | Invalid leap |
|---|---|---|---|
| `M` | Manuscript text, equation, table, figure, or citation as displayed | Show what the paper says or omits | Treat a citation marker as proof that the cited source supports the claim |
| `A` | In-scope code, data, script, log, build, or test observation | Check implementation and reproduction claims | Generalize one run to all environments or equate code presence with correctness |
| `X` | Externally verified primary/official source | Correct venue rules, bibliographic facts, prior-work capabilities | Use search snippets, secondary summaries, or stale calls as definitive |
| `I` | Explicit inference from `M`, `A`, or `X` | Predict a plausible reviewer attack | Present the inference as an observed fact |
| `U` | Evidence unavailable under current scope | Identify unresolved risk and required context | Declare a confirmed defect that depends on unseen material |

For external verification, record the source, direct URL, and applicable publication or venue cycle. If sources disagree, report the disagreement.

### Argument-state overlay

When reviewing notes, an incomplete draft, or a paper whose promises exceed visible evidence, also classify each candidate proposition:

- `established`: directly supported by authorized manuscript/artifact evidence or an allowed verified source;
- `inference`: follows from established premises but must retain calibrated force;
- `planned`: proposed mechanism, experiment, result, citation, or writing move that is not completed evidence;
- `blocked`: requires new data, source, mechanism detail, context, or author decision.

Never let a fluent narrative promote `planned` or `blocked` material into an established contribution. This overlay diagnoses what a defensible paper could currently claim; it does not authorize the reviewer to draft it.

## 3. Finding status

Use exactly one primary status.

### Confirmed defect

The in-scope material itself establishes a failure: contradiction, unsupported local claim, invalid inference, wrong arithmetic, missing required element under a verified rule, ambiguous reference with no valid local resolution, misleading graph, broken LaTeX, or clear language error.

### Unresolved reviewer risk

A skeptical attack is plausible, but confirmation requires unavailable context, evidence, execution, expert adjudication, or author intent. State the minimal item that resolves it. `Needs context` is a subtype, not an excuse to omit the issue.

### Style preference

More than one formulation is correct and the choice primarily concerns readability, house style, or presentation. A preference becomes a defect only when it causes ambiguity, inconsistency, policy violation, or material reading cost.

Do not label absent out-of-scope content a confirmed defect. Do not downgrade an unsupported scientific conclusion to style.

### Diagnostic dimension

Assign every finding one or more dimensions: `argument role/organization`,
`scientific/technical support`, `language/presentation`, or `scope/authority`.
Run the dimensions independently. A missing-evidence risk cannot replace a visible
role mismatch, nonparallel comparison, redundant payoff, or mixed paragraph
obligation; conversely, a rhetorical defect does not prove the scientific claim
false. Preserve both findings at the same anchor when both apply.

## 4. Severity and confidence

Severity measures likely decision impact, not repair effort.

| Severity | Decision test | Typical examples |
|---|---|---|
| `S0 — blocker` | Independently supports rejection, desk rejection, or invalidates a central conclusion | Fabricated/contradictory result; verified policy breach; central claim has no valid evidence; fatal technical flaw |
| `S1 — major` | Could substantially lower score or confidence in a main contribution | unclear novelty; unfair baseline; missing system assumption; evaluation misses a central claim |
| `S2 — moderate` | Weakens an important local argument or creates recurring reader doubt | unexplained design choice; underdefined metric; repeated terminology conflict |
| `S3 — minor` | Local correctness or clarity issue with limited decision impact | grammar error; caption ambiguity; isolated formatting defect |
| `S4 — preference` | Optional improvement with no correctness consequence | defensible word choice or layout alternative |

Confidence is `high`, `medium`, or `low`:

- `high`: direct in-scope evidence or verified official rule;
- `medium`: strong inference with a clearly stated dependency;
- `low`: plausible attack worth surfacing but highly context-sensitive.

Never use high confidence to compensate for missing evidence. A high-severity, low-confidence risk is valid when the potential consequence is large and the missing test is explicit.

## 5. Top-down unit audit

After freezing scope, build the complete unit and adjacency inventory from the
shared coverage contract. Audit paper/archetype and evidence spine first when
assessable, then every section, paragraph, sentence, and lexical occurrence in
reading order. Give each unit and link one coverage state before moving to the
bottom-up reconciliation. A severe early finding does not terminate the audit,
and a findings-only list is not a coverage record.

The hierarchy and independent passes answer different questions. The hierarchy
proves that every textual unit was visited in context; the passes test each unit
through independent scientific and reader lenses. Complete both.

## 6. Independent passes

Run all applicable passes separately. Update the shared per-unit ledgers so an early severe finding does not terminate review.

### Pass P1 — scope, parsing, and surface integrity

- Confirm readable/extractable input, language, locations, cross-references, and obvious corruption.
- Inventory sections, figures, tables, citations, claims, and artifact objects that are actually in scope.
- Apply `PT` and `FL` rules appropriate to the input.

### Pass P2 — PC/chair contribution case

- Select the primary paper archetype and reconstruct one controlling thesis plus its supporting-claim hierarchy. Do not force a design-paper template onto empirical or operational work.
- Mark every central reconstructed node and dependency `stated`, `text-licensed`, or `reviewer-hypothesized` with original-text anchors. A coherent reviewer-written thesis is the object being audited, not proof that the prose supplied its links.
- When several stories remain plausible, compare their primary claim, decisive evidence, missing support, and scientific tradeoff. Treat a choice that changes author intent as unresolved.
- Ask what problem/question matters, what failed assumption or binding constraint makes it unresolved, what intellectual move changes understanding or capability, what was built or established, what decisive evidence supports it, and why a systems audience should care.
- Stress novelty against the closest alternatives, not a generic field summary.
- Apply assessable `PA`, `TH`, and `RC` rules and venue criteria.

### Pass P3 — domain-expert technical attack

- Reconstruct the design derivation from observed failure/property through constraint, requirement, mechanism, invariant/effect, tradeoff, and decisive test. Then reconstruct system model, lifecycle, failure behavior, and assumptions.
- When one move is meant to yield several properties, build the source-grounded fan-out map, attribute each edge to its narrowest causal layer, and run the counterfactual. Keep an enabling substrate, authority boundary, runtime enforcement/lifecycle, execution path, and empirical condition distinct when the property depends on more than one.
- Search for counterexamples, hidden state, concurrency/failure gaps, unsafe generalization, and mechanism/claim mismatch.
- Apply `DD` and `TS` rules.

### Pass P4 — evaluation skeptic

- Predict the decisive evidence from the thesis before examining the paper's emphasis. Create a claim-to-evidence matrix and check whether headline results mirror the contribution hierarchy.
- Test research questions, baselines, workloads, metrics, setup, uncertainty, negative results, and conclusion strength.
- Apply `TH`, `EV`, and `ER` rules; apply `AR` when artifacts are in scope.

### Pass P5 — non-specialist systems reader

- Read linearly without importing unstated domain knowledge.
- For every supplied paragraph, record the signaled or author-supplied role and independently classify the delivered role through the shared writing core. A mismatch is a finding; reclassifying an alleged insight as overview or mechanism does not make it pass.
- Complete the one-obligation sentence, test every sentence against it, and run the ending deletion/information-gain test. Inspect adjacent sentence pairs, paragraph handoffs, and explicit longer dependencies; retain both endpoints of every faulty link.
- Track first use of terms, antecedents, the problem → intellectual move → realization ladder, paragraph-opening promises, paragraph-closing implications/handoffs, section transitions, examples, figure callouts, headline-result payoff, and cognitive load. For gap-producing related work, recover the fair comparison axis and shared root constraint rather than accepting descriptive categories as a cause. For completed-paper prose, distinguish an evidence-derived answer from an evaluation placeholder.
- For artifact-backed positioning, apply the shared [positioning and intellectual-move contract](../../systems-paper-revise/references/positioning-and-insight.md): separate the inspected artifact fact from the capability-level manuscript claim, test any conjunctive gap independently, and audit a promised Observation or Insight against the role it actually delivers.
- If the text advertises one key insight, boundary, or design choice beside multiple primary outcomes, test every move-to-outcome edge using only reader-visible premises. Report the first reviewer-hypothesized edge instead of completing the story silently; a common label or paragraph is not causal fan-out.
- For a broken or incomplete argument, build a read-only reader-obligation outline: each unit's entering question, claim/answer, required mechanism/evidence, and closing implication/handoff. Use it to locate the first broken dependency, not to write replacement prose.
- Apply `TH`, `ER`, `SS`, `PT`, and relevant `FL` rules.

#### Mandatory prose-trigger checkpoint

For every matching paragraph, record an explicit `pass`, `finding`, or
`unresolved` result for each trigger below. Run these checks during an ordinary
paper-prose review; do not wait for the user to ask the diagnostic question.

| Trigger | Required independent test | A missing context does not permit |
|---|---|---|
| A limitation is followed by `however/but` and then `therefore/to use X the system must ...` | Compare the propositions, not the connectives. Ask whether the ending supplies a new constraint, consequence, selection criterion, or handoff, or merely turns the immediately preceding absence into its positive or required form. | Calling the payoff nonredundant only because deleting its sentence removes the explicit wording. |
| A related-work taxonomy or boundary list leads to a negative gap or research question | Classify the bridge with the shared [interface-boundary contract](../../systems-paper-revise/references/interface-boundaries.md). For a negative gap, require the shared cause and evidence; for a distinct-question bridge, require a parallel map and bounded question without inventing prior-work failure. Assess novelty separately. | Treating a distinct question as proof of absence, demanding a root cause for an unclaimed failure, or treating the locally visible bridge as uninspectable merely because sources or incoming context are unavailable. |
| A prior-work sentence foregrounds a repository, build, link, configuration, or public artifact fact | Run the [artifact-to-capability distillation](../../systems-paper-revise/references/positioning-and-insight.md): recover actor, changeable object, stage, control, and the comparison-axis consequence; then ask whether the realization detail itself changes the paper's decision case. | Treating a true forensic observation as manuscript-ready, or dropping its deployment qualification while abstracting it. |
| A gap says that several properties have not appeared `together`, `simultaneously`, or in one inspected design | Run the shared contract's conjunctive-gap test: population coverage, parallel property cells, negative evidence, shared causal constraint, and licensed requirement or question. | Treating tuple absence, a bounded-system hedge, or a conjunction of desirable properties as a causal research gap or novelty result. |
| A paragraph is labeled Observation, Key observation, Insight, Requirement, or Design objective | Run the shared observation ladder: classify the delivered role, locate its source anchor and non-definitional relation, test information gain and prediction, and keep independent goals independent. | Passing a definition, requirement restatement, mechanism list, or vague `these differences show` bridge under the promised intellectual-move role. |
| An interface, customization, protection/isolation, or direct/delegated-path claim combines two or more boundary axes | Build the boundary-axis ledger for semantic commitments, protection/authority, and execution path; recover actor/artifact/stage/control for customization and the responsibility chain for compound protection claims. | Letting one axis prove another, crediting one mechanism with a compound property, or demanding an axis the passage does not claim. |
| Research-paper prose predicts a performance or correctness benefit and ends with `must be evaluated`, `remains to be tested`, or an equivalent future test | Determine manuscript state. A request to review manuscript/paper prose defaults to a research-paper claim context unless the user or text identifies a proposal, plan, or future-work document. If state truly remains ambiguous, report the completed-paper-placeholder risk conditionally; do not mark it clean. | Treating an evaluation placeholder as a sound payoff solely because it is epistemically cautious. |
| A visible limitation materially excludes a user class, workload, deployment model, semantics, or compatibility target | State the conditional early-disclosure judgment: if it qualifies the headline contribution, a concise version belongs where broad readers first encounter that claim; detailed treatment may remain later. Mark exact wording, duplication, and placement not assessable without that context. | Omitting the conditional judgment because the Introduction is out of scope or the user did not ask about placement. |
| A `key/core insight`, changed boundary, or single design choice is presented with two or more primary outcomes, or the thesis relies on such unity | Build the source-grounded fan-out ledger. Anchor the shared move and each advertised outcome; label every edge `stated`, `text-licensed`, or `reviewer-hypothesized`; identify its narrowest causal layer and run the counterfactual. | Passing the unification because the reviewer can invent a coherent bridge, because all outcomes occur in one paragraph, or because one system label names all mechanisms. |

These are diagnostic triggers, not fixed sentence templates. A paragraph may
pass any row when the required relation is genuinely present. Keep each trigger's
argument/organization result separate from evidence, external truth, and
scope/authority results.

### Pass P6 — internal and artifact consistency

- Cross-check names, numbers, units, claims, captions, tables, equations, code/configuration, and scripts only across in-scope objects.
- Distinguish paper-to-paper, paper-to-artifact, and artifact-to-result mismatches.

### Pass P7 — hostile counter-review

For each central claim, complete these prompts:

- “This is not important because …”
- “This is not new because …”
- “This mechanism may fail when …”
- “This experiment does not establish the claim because …”
- “This comparison is favorable for an avoidable reason because …”
- “This result may not generalize because …”
- “I cannot reproduce or audit this because …”

Keep an attack only if grounded in evidence or recorded as an unresolved risk with a resolution test.

### Pass P8 — deduplication and omission audit

- Merge identical root causes; retain every affected location.
- Split findings that need different fixes or have different decision impacts.
- Cross-tabulate findings by diagnostic dimension. Revisit every paragraph that has only an unresolved evidence finding and verify that argument role, one-obligation structure, comparison parallelism, and payoff information gain were independently checked rather than silently treated as passed.
- Reconcile the mandatory prose-trigger checkpoint: every matching paragraph has a visible state for every matching trigger. Re-open a paragraph whose only defense is `the sentence adds explicit words`, `the paper state is unknown`, `the Introduction is missing`, `the prior-work context is unavailable`, or `the reviewer can reconstruct a unified story`; each defense leaves the corresponding content test or conditional judgment undone.
- Revisit the controlling thesis, each supporting claim, every major mechanism/finding, each decisive result, and every applicable rule family.
- Verify that “no finding” means inspected and passed, not forgotten.

## 7. Rule application record

For each rule family, record one coverage state:

- `applied — findings`;
- `applied — no findings`;
- `not assessable — out of scope`;
- `not assessable — missing evidence`;
- `not applicable`.

Never claim exhaustive review without accounting for not-assessable families. Exhaustiveness is relative to the frozen scope and observable evidence. Disclose full rule-family accounting in a formal or full review. In a local review, the shared unit ledger and receipt remain visible; rule-family rows may stay internal unless missing context changes a finding or the gate.

## 8. Layered finding schema for full or formal reviews

In a full or formal review, use the full structure for every `S0`/`S1` finding and for any lower-severity finding whose diagnosis, evidence, or repair is non-obvious. In a local review, compress the same reasoning into one root-cause bullet without exposing rule IDs or unused fields. This compression applies only to finding explanations, never to the shared per-unit coverage ledgers:

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

Use stable finding numbers within one report. Quote only the minimum text needed to anchor a location.

### Sentence and paragraph logic findings

For a relational finding, replace a single vague location with both original endpoints. Use `P2.S2 → P2.S3` for a sentence link and `P2 → P3` for a paragraph handoff, adding section/path anchors as needed. Quote a short identifying phrase from each side; if the relevant paragraph evidence lies away from its boundary sentences, name those sentences too. If segmentation is uncertain, use two quoted anchors rather than fabricated indices.

Each finding states what the first unit establishes, what the second assumes or concludes, the claimed or expected relation, and why that relation fails. Distinguish an unsupported cause/conclusion, contradiction, scope or referent shift, missing premise, or disconnected topic from a merely optional transition. Explain the reader consequence and the minimum repair or evidence test. In compact form: `endpoint pair + anchors — status/severity; failed relation and consequence; repair boundary`.

Check every adjacent pair internally, but report only actual defects or unresolved risks. Do not require a connective, invent a causal relation, or report a valid topic transition as a defect. Mark unavailable neighbors as not assessable. A one-paragraph review can identify sentence links but cannot claim to have checked paragraph-to-paragraph logic.

Keep sentence-link and paragraph-link findings distinguishable; a grouped root cause still lists every affected pair. For multi-paragraph logic reviews, give a compact map of what each paragraph currently does. These diagnostics stay outside manuscript prose. If a repair would move content, split/merge paragraphs, or change a paragraph's role, label it as requiring explicit author restructuring authority rather than instructing revise to perform it automatically.

For a straightforward `S2`/`S3` item, use a compact ledger row instead of repeating boilerplate:

| ID | Rule | Location | Dimension | Status / severity / confidence | Next action | Problem and consequence | Repair / resolution test |
|---|---|---|---|---|---|---|---|

Compact form does not authorize omission. Expand an item whenever the evidence class, reviewer attack, or scientific consequence would otherwise be ambiguous. Group repeated symptoms under one root cause and list every affected location.

## 9. Report schema

### Editorial decision brief

- Scope and material evidence limits.
- Primary/secondary paper archetype and any unresolved routing choice.
- One-sentence thesis reconstruction in the reviewer’s words; if impossible, say why rather than inventing one.
- Verdict with calibrated confidence.
- Strongest argument assets to preserve or amplify: only evidence-backed examples, claims, figures, results, or passages that materially help the paper.
- Decision-dominant rejection threats. Prefer the smallest set that explains the verdict; the ledger carries completeness.

One of:

- `clear within scope`;
- `actionable issues remain`;
- `blocked by missing evidence/context/author decision`.

Add one paragraph explaining the decisive reason and confidence. Never translate `clear within scope` into `the paper is publishable`.

### Thesis, design, and evidence diagnosis

- Give the thesis-support hierarchy and reader-memory result for an argument-bearing scope.
- When one move is claimed to yield several primary outcomes, give an intellectual-move dependency ledger with the shared move, each outcome, original anchors, causal layer, source status, counterfactual, and gap. Any reviewer-hypothesized central edge remains a visible finding or unresolved risk.
- Give the design-derivation break for a design-bearing scope.
- Give the headline-evidence mismatch for an evaluation-bearing scope.
- Distinguish established, inferential, planned, and blocked propositions when the material is incomplete.
- If stories compete, show the alternatives and scientific tradeoff without choosing against author intent.
- State the highest-level reconstruction blueprint before local findings. If the hierarchy itself is wrong, give an archetype/thesis/evidence/reader-obligation outline and identify the global restructuring that needs author authorization; do not supply replacement prose or treat that diagnosis as editing permission.

### Exhaustive findings ledger

For a full or formal review, give all materially distinct findings in severity order; within severity, follow reading order. Show the diagnostic dimension on each item and ensure argument/organization and evidence/technical lanes remain separately visible when both apply. Use the full schema for severe/non-obvious findings and compact rows for straightforward findings. Include style preferences last and only if useful. For a local review, preserve the same distinct root causes and dimensions in compact bullets and omit this report section.

### Per-unit coverage ledgers

Before the findings ledger, show the paper, section, paragraph, sentence, relation,
and lexical rows required by the shared coverage contract. Preserve reading order
and show passed units. Every paragraph receives its signaled/intended role when
observable, delivered role, one-obligation result, and comparison against the
applicable opening, development, and payoff convention, including ending
information gain. A mixed, unclear, or promise-versus-delivery mismatch stays
visible; do not repair the author's argument by classification. For large scopes,
numbered batches are permitted, but the result
remains `incomplete` until the final ledger rows and receipt are delivered.

### Claim-evidence matrix

For each central in-scope claim in a full or formal review:

| Claim | Type | Stated evidence | Evidence class | Coverage | Open attack |
|---|---|---|---|---|---|

Use `covered`, `partially covered`, `unsupported`, or `not assessable`.

### Coverage summary

For a full or formal review, list P1–P8 status and each relevant rule family status, including archetype/thesis/design-derivation/argument-object coverage where applicable. Name rules or objects not assessable and why. For every review, end with the shared manuscript coverage receipt and the decision coverage receipt; a local review may omit the separate pass/rule-family inventory but not its unit totals, last-unit states, not-assessable reasons, `Unreviewed` count, or `Unaccounted decisions` count.

### Gate result and next evidence

State the gate result. For every blocker, name the smallest experiment, source, context, artifact, or author decision required. Do not prescribe invented results.

## 10. Anti-patterns

Do not:

- generate exactly three strengths and three weaknesses regardless of evidence;
- average independent fatal flaws into an overall numerical score;
- reward surface polish when a central claim is unsupported;
- reject solely because the paper does not use a preferred section template, voice, graph type, or statistical test;
- conflate absence from a scoped paragraph with absence from the full paper;
- search for extra problems in unrequested files;
- silently repair prose while reviewing;
- stop after the first severe defect, report only problematic units, or infer full coverage from a spot check;
- call a paper ready because a linter, compiler, or automated review loop passes.

## Sources

Protocol design synthesizes [OPENAI-SKILL-CREATOR], [DEERFLOW-REVIEW], [CHAN-DUAL-LENS], [LEVIN-REDELL], [OSDI-CFP], [SOSP-CFP], [FIVE-VENUE-CORPUS], [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [USER-NOTES], and [SYSTEMS-GUIDE]. See [source-registry.md](source-registry.md).
