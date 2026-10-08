# Shared Coverage Contract

Review, Grill, and Revise use this contract for one auditable record of permitted material.
It controls inventory, execution order, coverage state, and handoff.
The [decision-record rules](../../systems-paper-grill/references/decision-record.md) control full decision-history accounting and its receipt.
Neither contract gives access to neighboring material or gives permission for a manuscript edit.
They do not replace the linked quality rules.

## Load the existing standard

Use the [systems-writing core](writing-core.md) and [positive archetype contracts](paper-archetypes.md) for the stable standard.
For any prose, read the detailed [sentence and lexical rules](../../systems-paper-review/references/prose-and-terminology.md).
For multi-sentence prose, also read the detailed [section and paragraph rules](../../systems-paper-review/references/structure-and-sections.md).
Use the existing [paragraph-role research](../../../research/systems-paper-writing-requirements.md#每一种段落应怎样写) for opening, development, and payoff expectations.
Do not invent another role matrix.
If the user names a venue, track, or cycle, add the [live venue overlay](../../systems-paper-review/references/venue-overlays.md).

These sources apply together at their related levels.
For a wording request, do each possible paragraph or section check in the frozen scope too.
Fluent words at a lower level cannot resolve a higher-level failure.

## Record the scope and inventory before judgment

Give the specified permitted objects before analysis.
Record unavailable context.
Keep the scope unchanged.
Before the first finding, inventory the full scope in reading order.
Use these rules:

- Use the author's stable section/path labels when available.
  If that condition does not hold, give sections IDs `SEC-01`, `SEC-02`, and so on.
- Give paragraphs IDs such as `SEC-01.P01`.
  Give sentences IDs such as `SEC-01.P01.S01`.
  Keep those IDs stable through one Review–Grill–Revise cycle.
- Keep incoming lexical occurrence IDs in the source-to-revision mapping.
  Before assigning new IDs, align surviving occurrences with the incoming inventory using the procedure below.
- Inventory headings, prose, lists, captions, equations, figures, tables, and each other reader-visible object in scope.
  Do not treat each object as a usual paragraph.
- Inventory each adjacent section, paragraph, and sentence link with the two endpoints in scope.
  Include clearly signaled longer dependencies.
- For English, identify word or token occurrences in sentence order.
- For Chinese or mixed prose, use the smallest semantically stable word, term, punctuation, or code/math span.
  Disclose segmentation uncertainty.
- Record the first and last unit ID at each applicable level.
  Do not infer full-scope coverage from a suspicious excerpt.

For a supplied sentence or paragraph, paper and section context can be `not assessable`.
That state gives no permission to read surrounding files.
Source line wraps are not paragraph or sentence boundaries.

### Align lexical occurrences after revision

Keep the incoming segmentation rule and source IDs.
Apply these steps before counting the revised text:

1. Match each current occurrence to at most one source occurrence.
   Use its token text, source unit, phrase, grammatical or technical function, and surviving neighboring occurrences.
   Count repeated tokens as separate occurrences.
2. Keep the source ID for each unambiguous surviving match.
   Record its current location, including movement within an authorized local edit.
   A changed sentence can contain unchanged occurrences.
   Align those occurrences individually before classifying the remaining text.
3. Give unmatched inserted or replacement occurrences unused new IDs.
   Mark unmatched source occurrences as deleted.
   Keep replacement and deletion links in the mapping.
4. Resolve ambiguous matches from the original anchors and current text.
   If identity remains uncertain, record that uncertainty and keep the mapping incomplete.
5. Check that every current occurrence has one unique ID and every source occurrence has one recorded disposition.
   A deleted ID cannot identify different text after revision.
   Derive current coverage and weighted state totals from this final mapping.

Carry this mapping into the next authorized handoff.
It is necessary when source IDs alone cannot recover current occurrence identity.

## Execute top down, then reconcile bottom up

Use this order at each assessable level:

```text
scope, target venue/cycle, and contribution archetype
  -> paper-level thesis, claim hierarchy, and evidence spine
    -> every section and section handoff
      -> every paragraph and paragraph handoff
        -> every sentence, adjacent sentence link, and explicit dependency
          -> every lexical occurrence in context
            -> bottom-up consistency and regression reconciliation
              -> coverage reconciliation
```

### Paper level

Find the applicable archetype, controlling thesis, supporting claims, decisive evidence, and important boundary.
Give each central node and edge a source status in the writing core.
Use `stated`, `text-licensed`, or `reviewer-hypothesized`.
If one move yields several primary outcomes, inventory each move-to-outcome dependency in the source-grounded fan-out map.
A reviewer-supplied bridge does not show coverage of a missing edge.

### Section level

Compare each section's conventional reader obligation with its promised and delivered content.
Record its claim–evidence contribution and the two handoffs.
Distinguish section genre, observable content promise, and delivered local function.
A broad section heading selects checks; it does not require each paragraph to supply every genre component.
A confirmed role mismatch needs a specific scoped promise or demonstrated reader dependency with failed delivery at that same level.
If genre alone supplies the expected function and necessary macro context is absent, mark broader adequacy `not assessable`.
Complete all local role, obligation, payoff, and link checks.
Request an author role or structural decision only when an evidence-supported repair requires that choice.

### Paragraph level

Record any promised role from a heading, roadmap, opening claim, clear label, or author-supplied intent.
A clear label can be `key insight`.
Independently find the role that the paragraph delivers.
Compare promised and delivered roles with the applicable convention.
Do a check of opening, development, payoff or handoff, sentence roles, and neighboring paragraph relations.

A mixed, unclear, or promise-versus-delivery mismatch is a result.
Do not replace the promised role with the delivered role without an author decision.
Do the writing core's one-obligation and payoff-information tests even when evidence risk also exists.

### Sentence and lexical levels

For each sentence, record these items:

- Dominant assertion and local function
- Actor, action, and object
- Evidence state, conditions, and boundary
- Relations to adjacent sentences.

For each lexical occurrence, do the applicable checks in its proposition:

- Term identity, definition, and referent
- Quantifier, modifier scope, and negation scope
- Technical verb commitment and epistemic strength
- Comparison, collocation, and tense
- Grammar, punctuation, units, and notation.

A dictionary-valid word can make a technical commitment without support.
Do not give it a pass for dictionary validity alone.

### Reconcile upward

Make sure that lexical repairs keep sentence propositions.
Make sure that sentences complete their paragraph's obligation.
Make sure that paragraphs complete their section's obligation.
Make sure that sections support the paper contract and evidence spine.
Do the full-scope checks of terms, assumptions, numbers, claim strength, and evidence status again.

Keep these diagnostic dimensions independent:

- Argument role/organization
- Scientific or technical support
- Language/presentation
- Scope/authority.

A pass or blocker in one dimension does not resolve another.
For example, missing evidence can coexist with a confirmed role mismatch, category comparison defect, or redundant payoff.

## Give each unit a coverage state

Give each inventoried unit and link one controlling state.
Leave no cell blank.
Use these states:

| State | Meaning |
|---|---|
| `pass` | Each applicable loaded criterion has a completed check. No defect, unresolved risk, or preference with a clear benefit stays. |
| `finding` | A confirmed defect or style preference with a clear benefit has an anchor at the unit. The finding's status distinguishes them. |
| `unresolved` | Missing context, evidence, source verification, or an author decision prevents judgment. No confirmed defect controls the unit. |
| `not assessable` | The permitted scope cannot show this level or relation. Give the specified missing material. |

If a unit has a confirmed defect and unresolved risk, use controlling state `finding`.
Keep the two finding IDs linked.
Coverage states do not replace Review's finding fields:

- Status, diagnostic dimension, severity, and confidence
- Evidence class and repair boundary
- Resolution test.

## Keep visible per-unit ledgers

Review shows sufficient detail to prove coverage, including passed units.
Give these rows at their applicable levels:

- Paper: archetype, thesis, claim/evidence spine, boundary, state, and finding IDs
- Intellectual-move dependency: shared move, advertised outcome, initial anchors, causal layer, source status, counterfactual, state, and finding IDs
- Section: expected/actual obligation, entering question, delivered answer, claim/evidence contribution, incoming/outgoing handoff, state, and finding IDs
- Paragraph: section, signaled/intended role when observable, delivered role, role convention, and one-obligation result
- Paragraph, continued: expected/actual opening, development, payoff/handoff, information gain, sentence roles, and neighboring paragraph relation
- Paragraph, continued: dimension states, controlling state, and finding IDs
- Sentence: dominant assertion, function, actor/action/object, evidence state, condition/boundary, incoming/outgoing relation, language state, and finding IDs
- Lexical occurrence: occurrence/span, sentence ID, technical or grammatical function, applicable checks, state, and finding IDs.

Use one paragraph row with all paragraph fields.
The split list above only makes the field description easier to read.
Give each risk-bearing lexical occurrence its own row.
Compress contiguous passed occurrences without risk into a range only with its specified sentence-local span and count.
That range states that each occurrence received a check.
It does not represent sampling.

Do not hide passed sections, paragraphs, sentences, or lexical spans in a findings-only list.
For a local Review, use one compact ledger for all inventoried units and links.
Keep every required field at its owning unit or dependency row.
Domain maps, trigger results, and dimension tables are views of these same records.
Integrate their required fields into those rows instead of adding another ledger.
State common field labels once in a header or key.
Reference another row or finding when it already records the applicable value.
Each reference must resolve to evidence or a field value for that particular unit.
Use the source anchor instead of paraphrasing an unchanged proposition again.
Explain each root cause once in its finding entry, with its anchors and resolution test.
Other rows give the applicable field value, coverage state, and finding IDs.
Add prose there only for a new fact specific to that unit.
When the same cause controls several fields, use its finding ID instead of repeating its explanation.
Use this local report order:

1. Scope, inventory totals, and unavailable context
2. One canonical unit ledger, including each applicable map and dependency
3. Short finding entries with distinct root causes and resolution tests
4. Manuscript and decision coverage receipts.

Keep the verdict in the manuscript receipt.
Keep the necessary next evidence in its finding's resolution test.
Before delivery, remove repeated conclusions, maps, causal explanations, and evidence requests from other report parts.
Keep their source IDs and resolvable references in the canonical records.
Keep exact passed lexical spans and counts, last-unit states, and both coverage receipts.
For a large paper, continue ledgers in numbered batches or a clearly permitted report artifact.
Keep result `incomplete` until the last batch and reconciliation are delivered.

Revise keeps the same full-scope ledgers before and after edits.
It usually gives the manuscript first, then a compact closure map and manuscript coverage receipt.
For a clear prose-only request, keep ledgers internal.
Obey the revision protocol's prose-only exception.
Give the compact decision coverage receipt after prose-only output when workflow metadata is permitted.
Honor explicit manuscript-body-only or receipt exclusions; keep the same accounting internal.

Grill shows only the source units and findings for discussion.
It does not repeat the full audit.

## Account for decision history independently

Before a manuscript judgment, use the decision-record rules to resolve the permitted record.
Put each literal version ID in its status and set classes.
Derive effective, applicable, and executable sets.
Decision accounting is independent of unit coverage.
`Unreviewed: 0` cannot hide an unaccounted decision.
`Unaccounted decisions: 0` cannot hide an unreviewed manuscript unit.

Keep broken lifecycle links, conflicting heads, unavailable history, and excluded decisions visible in the decision receipt.
They give no permission to guess or skip unaffected manuscript checks.
During an interactive Revise pause, give decision accounting at this point.
Do not call manuscript coverage or finding closure terminal.

## Keep IDs and close the loop

Review gives each finding a stable ID and these fields:

- Affected unit/link IDs and status
- Repair boundary and observable resolution test
- One next-action class from the shared workflow contract.

Use `direct repair`, `author clarification`, `author evidence`, `external blocker`, or `optional/not applied`.
Route author-intent questions to clarification.
Route scientific support requirements to author evidence or an external blocker.
Confirmed intended wording is not proof.

When Review IDs exist, Grill carries finding and unit IDs into the decision record.
Record author meaning, evidence state, permitted edit, and important rejected alternatives.
`pending` is not edit permission.

During interactive revision, `pending clarification` gives an author-answerable item awaiting a response.
It is non-terminal, not `blocked`, and not a closure state.
Revise gives each ready question and resumes after answers.
After no requested item stays pending, give each received finding one closure state:

| State | Required condition |
|---|---|
| `closed` | The permitted edit or existing text passes the initial test and post-edit full-scope audit. |
| `blocked` | An external prerequisite stays unavailable, or the author clearly declines, cannot supply, or confirms the requested input's unavailability. |
| `not applied` | The item is rejected, optional, not in scope, stale, or conflicts with a newer decision. Give the reason. |
| `reopened` | The initial problem stays, or the edit introduces an equal-or-higher-impact regression. |

Keep each finding in the handoff.
A text change alone does not close a finding.
A withdrawn claim does not gain evidence.
Recheck linked findings after an explicit author withdrawal or replacement, through [review-revise-contract.md](review-revise-contract.md).
Preserve their IDs and tests; use `not applied` for requirements that no longer apply, with the decision and reason.
Audit each retained claim independently without treating the old test as passed.

## Completion gate and receipt

Before a full-audit or full-revision claim, do these checks:

1. Derive receipt totals and any state subtotals from the final ledger.
   Count each compressed range by its declared occurrence count, not as one occurrence.
   Make sure that inventory totals equal ledger totals at each applicable level and adjacency/dependency class.
2. Make sure that the last unit at each level has a nonblank state.
3. Make sure that ledgers include passed and problematic units.
4. Make sure that each finding maps to all affected units.
5. At completed Revise, make sure that each received finding has a closure state.
   Verify the required source-occurrence mapping before claiming complete source-ID continuity or a completed revision audit.
   If that mapping remains incomplete, report the audit as incomplete even when every current occurrence received a check.
6. At an interactive pause, show the pending queue without a completion claim.
7. Make sure that no unresolved or not-assessable item appears as passed or closed.
8. Make sure that upward reconciliation finds no contradiction, scope drift, term drift, claim-strength change, or evidence promotion.
9. Make sure that each paragraph has independent role, competing-obligation, payoff-information, and evidence checks.
10. Make sure that a blocker in one dimension does not suppress a finding in another.
11. Make sure that each assessable central node and dependency has a source status.
12. For one move with several outcomes, make sure that each advertised outcome appears in the fan-out ledger.
13. Keep each `reviewer-hypothesized` edge as a finding or unresolved risk.
14. Make sure that each decision version has a status and set class.
15. Give decision conflicts and exclusions.
    Do not resolve them without an author decision.
16. Make sure that `unreviewed = 0` and `Unaccounted decisions: 0`.

If either last count is false or unknown, use result `incomplete`.
End Review and completed non-prose-only Revise with a coverage receipt.
Do not give a terminal receipt during any requested `pending clarification` item.

```text
Scope fingerprint: <objects and stable boundaries>
Highest assessable level: <paper | section | paragraph | sentence | lexical>
Sections: <ledgered>/<inventoried>; last=<ID/state>
Paragraphs: <ledgered>/<inventoried>; last=<ID/state>
Sentences: <ledgered>/<inventoried>; last=<ID/state>
Sentence links: <ledgered>/<inventoried>; last=<endpoint pair/state>
Paragraph links: <ledgered>/<inventoried>; last=<endpoint pair/state>
Intellectual-move dependencies: <ledgered>/<inventoried>; reviewer-hypothesized=<count>; last=<edge/state>
Lexical occurrences: <covered>/<inventoried>; rows=<after exact pass-range compression>; last=<ID or span/state>
Findings: <total; status counts>; closure: <counts when revising>
Not assessable: <units and reason>
Unreviewed: 0
Result: <clear within scope | actionable issues remain | blocked | incomplete>
```

Omit levels and the intellectual-move dependency line only when they do not exist.
Keep unavailable higher levels as `not assessable`.
Then give the decision coverage receipt from the decision-record rules.
A receipt proves only execution in scope.
It does not show acceptance, novelty over unread literature, or correctness not in the permitted evidence.
