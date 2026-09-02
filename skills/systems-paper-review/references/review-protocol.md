# Adversarial Review Protocol

Use this protocol for every review. It defines scope control, evidence discipline, independent passes, finding calibration, completeness, and the final gate. Domain reference files define the individual `RC`, `TS`, `EV`, `AR`, `SS`, `PT`, `FL`, and `VO` rules.

For a large scope reviewed with collaboration tools, execute the applicable passes through the role assignments in [multi-agent-orchestration.md](multi-agent-orchestration.md). The pass definitions, evidence requirements, and output schema remain unchanged; only execution is parallelized.

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

For external verification, record source, direct URL, publication/version or venue cycle, and date checked. If sources disagree, report the disagreement.

## 3. Finding status

Use exactly one primary status.

### Confirmed defect

The in-scope material itself establishes a failure: contradiction, unsupported local claim, invalid inference, wrong arithmetic, missing required element under a verified rule, ambiguous reference with no valid local resolution, misleading graph, broken LaTeX, or clear language error.

### Unresolved reviewer risk

A skeptical attack is plausible, but confirmation requires unavailable context, evidence, execution, expert adjudication, or author intent. State the minimal item that resolves it. `Needs context` is a subtype, not an excuse to omit the issue.

### Style preference

More than one formulation is correct and the choice primarily concerns readability, house style, or presentation. A preference becomes a defect only when it causes ambiguity, inconsistency, policy violation, or material reading cost.

Do not label absent out-of-scope content a confirmed defect. Do not downgrade an unsupported scientific conclusion to style.

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

## 5. Independent passes

Run all applicable passes separately. Maintain an internal coverage ledger so an early severe finding does not terminate review.

### Pass P1 — scope, parsing, and surface integrity

- Confirm readable/extractable input, language, locations, cross-references, and obvious corruption.
- Inventory sections, figures, tables, citations, claims, and artifact objects that are actually in scope.
- Apply `PT` and `FL` rules appropriate to the input.

### Pass P2 — PC/chair contribution case

- Ask what problem matters, what insight is new, what was built or established, and why a systems audience should care.
- Stress novelty against the closest alternatives, not a generic field summary.
- Apply all assessable `RC` rules and venue criteria.

### Pass P3 — domain-expert technical attack

- Reconstruct the system model, mechanism, invariants, lifecycle, failure behavior, and assumptions.
- Search for counterexamples, hidden state, concurrency/failure gaps, unsafe generalization, and mechanism/claim mismatch.
- Apply `TS` rules.

### Pass P4 — evaluation skeptic

- Create a claim-to-evidence matrix.
- Test research questions, baselines, workloads, metrics, setup, uncertainty, negative results, and conclusion strength.
- Apply `EV` rules; apply `AR` when artifacts are in scope.

### Pass P5 — non-specialist systems reader

- Read linearly without importing unstated domain knowledge.
- Track first use of terms, antecedents, paragraph promises, section transitions, figure callouts, and cognitive load.
- Apply `SS`, `PT`, and `FL` rules.

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
- Revisit every central claim and every applicable rule family.
- Verify that “no finding” means inspected and passed, not forgotten.

## 6. Rule application record

For each rule family, record one coverage state:

- `applied — findings`;
- `applied — no findings`;
- `not assessable — out of scope`;
- `not assessable — missing evidence`;
- `not applicable`.

Never claim exhaustive review without disclosing not-assessable families. Exhaustiveness is relative to the frozen scope and observable evidence.

## 7. Finding schema

Use this exact structure for every distinct finding:

```text
[F-###] Short diagnostic title
Rule: <stable rule ID and name>
Location: <page/section/paragraph/line/figure/table/path or quoted anchor>
Status: <confirmed defect | unresolved reviewer risk | style preference>
Severity: <S0 | S1 | S2 | S3 | S4>
Confidence: <high | medium | low>
Evidence: <M/A/X/I/U labels followed by the observable basis>
Reviewer attack: <the strongest concise objection a reviewer could make>
Why it matters: <affected claim, decision criterion, or reader inference>
Repair direction: <what must change or be supplied; no replacement prose>
Resolution test: <observable condition that closes the finding>
Sources: <rule source keys; add live URL/date for external facts>
```

Use stable finding numbers within one report. Quote only the minimum text needed to anchor a location.

## 8. Report schema

### Scope and limits

- In scope
- Explicitly out of scope
- Input form and language
- Venue/cycle, if named
- External/tool checks performed
- Evidence unavailable because of scope

### Verdict

One of:

- `clear within scope`;
- `actionable issues remain`;
- `blocked by missing evidence/context/author decision`.

Add one paragraph explaining the decisive reason and confidence. Never translate `clear within scope` into `the paper is publishable`.

### Top rejection threats

List every `S0`, then the decision-dominant `S1` items. Do not impose a fixed count.

### Exhaustive findings ledger

Give all findings in severity order; within severity, follow reading order. Include style preferences last and only if useful.

### Claim-evidence matrix

For each central in-scope claim:

| Claim | Type | Stated evidence | Evidence class | Coverage | Open attack |
|---|---|---|---|---|---|

Use `covered`, `partially covered`, `unsupported`, or `not assessable`.

### Coverage summary

List P1–P8 status and each relevant rule family status. Name rules or objects not assessable and why.

### Gate result and next evidence

State the gate result. For every blocker, name the smallest experiment, source, context, artifact, or author decision required. Do not prescribe invented results.

## 9. Anti-patterns

Do not:

- generate exactly three strengths and three weaknesses regardless of evidence;
- average independent fatal flaws into an overall numerical score;
- reward surface polish when a central claim is unsupported;
- reject solely because the paper does not use a preferred section template, voice, graph type, or statistical test;
- conflate absence from a scoped paragraph with absence from the full paper;
- search for extra problems in unrequested files;
- silently repair prose while reviewing;
- call a paper ready because a linter, compiler, or automated review loop passes.

## Sources

Protocol design synthesizes [OPENAI-SKILL-CREATOR], [DEERFLOW-REVIEW], [CHAN-DUAL-LENS], [LEVIN-REDELL], [OSDI-CFP], [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [USER-NOTES], and [SYSTEMS-GUIDE]. See [source-registry.md](source-registry.md). Last reconciled 2026-09-01.
