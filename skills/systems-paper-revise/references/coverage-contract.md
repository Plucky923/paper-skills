# Shared Coverage Contract

Review, Grill, and Revise use this contract to keep one auditable view of the
authorized material. It governs inventory, execution order, coverage state, and
handoff. The separate [decision-record rules](../../systems-paper-grill/references/decision-record.md)
govern complete decision-history accounting and its receipt. Neither contract
grants access to neighboring material, authorizes a manuscript edit, or replaces
the quality rules in the linked references.

## Load the existing standard

Use the [systems-writing core](writing-core.md) and
[positive archetype contracts](paper-archetypes.md) for the stable systems-paper
standard. For any prose, load the existing detailed
[sentence and lexical rules](../../systems-paper-review/references/prose-and-terminology.md);
for multi-sentence prose, also load the detailed
[section and paragraph rules](../../systems-paper-review/references/structure-and-sections.md).
The role-specific opening, development, and payoff expectations come from the
existing [paragraph-role research](../../../research/systems-paper-writing-requirements.md#每一种段落应怎样写);
do not invent a second role matrix. When a target venue, track, or cycle is named,
add the [live venue overlay](../../systems-paper-review/references/venue-overlays.md).

These sources are cumulative at their applicable levels. A request about wording
does not bypass paragraph or section reasoning that is assessable inside the
frozen scope. A high-level failure cannot be cleared by fluent lower-level prose.

## Freeze and inventory before judging

Freeze the exact authorized objects and record unavailable context before analysis.
Inventory the complete scope in reading order before reporting the first finding:

- use the author's stable section/path labels when available; otherwise assign
  `SEC-01`, `SEC-02`, and so on;
- identify paragraphs within each section as `SEC-01.P01`, and sentences as
  `SEC-01.P01.S01`; keep these IDs stable through one Review–Grill–Revise cycle;
- inventory headings, prose, lists, captions, equations, figures, tables, and
  other reader-visible units that the user put in scope rather than pretending
  every object is an ordinary paragraph;
- inventory every adjacent section, paragraph, and sentence link whose two
  endpoints are in scope, plus explicitly signaled longer dependencies;
- for English, identify reader-visible word or token occurrences in sentence
  order; for Chinese or mixed prose, use the smallest semantically stable word,
  term, punctuation, or code/math span and disclose segmentation uncertainty;
- record the first and last unit ID at every applicable level. Do not start with
  a suspicious excerpt and infer that the remaining units were inspected.

If the user supplies only a sentence or paragraph, paper and section context may
be `not assessable`; this is not permission to inspect surrounding files. Source
line wraps are not paragraph or sentence boundaries.

## Execute top down, then reconcile bottom up

Use this order without skipping an assessable level:

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

At the paper level, determine the applicable archetype, controlling thesis,
supporting claims, decisive evidence, and material boundary. Mark every recovered
central node and edge `stated`, `text-licensed`, or `reviewer-hypothesized` under
the writing core. When one move is meant to yield several primary outcomes,
inventory every move-to-outcome dependency in the source-grounded fan-out map;
the reviewer's ability to supply a missing bridge does not make the edge covered.
At the section level,
compare each section's conventional reader obligation with what it promises and
delivers, its claim–evidence contribution, and both handoffs. At the paragraph
level, record any role promised by a heading, roadmap, opening claim, explicit
label such as `key insight`, or author-supplied intent. Independently classify
the role the paragraph actually delivers. Compare both with the applicable role
convention, opening, development, payoff or handoff, sentence roles, and neighboring
paragraph relations. A mixed, unclear, or promise-versus-delivery mismatch is a
result, not a reason to silently reclassify the paragraph into the role it happens
to perform. Complete the one-obligation and payoff-information tests in the
systems-writing core even when the paragraph also has an evidence risk.

At the sentence level, record the dominant assertion, local function, actor,
action, object, evidence state, conditions, boundary, and relations to adjacent
sentences. At the lexical level, check each occurrence in its proposition for term
identity and definition, referent, quantifier, modifier/negation scope, technical
verb commitment, epistemic strength, comparison, collocation, tense, grammar,
punctuation, units, and notation. Do not treat a dictionary-valid word as correct
when its local technical commitment is unsupported.

Finally reconcile upward: lexical repairs must preserve sentence propositions;
sentences must discharge their paragraph; paragraphs must discharge their section;
sections must support the selected paper contract and evidence spine. Recheck
terms, assumptions, numbers, claim strength, and evidence status across the
complete frozen scope.

Keep four diagnostic dimensions independent during this reconciliation:
argument role/organization, scientific or technical support, language/presentation,
and scope/authority. Passing or blocking in one dimension does not clear another.
For example, missing evidence may leave a scientific claim unresolved while the
same paragraph still has a confirmed role mismatch, nonparallel comparison, or
redundant payoff.

## Give every unit a coverage state

Every inventoried unit and link receives one controlling state; no cell is blank:

- `pass`: the unit was inspected under every applicable loaded criterion and no
  defect, unresolved risk, or useful preference remains;
- `finding`: at least one confirmed defect or useful style preference is anchored
  to the unit; use the finding's own status to distinguish them;
- `unresolved`: inspection exposed a risk that requires missing context, evidence,
  source verification, or an author decision, and no confirmed defect controls
  the unit;
- `not assessable`: the level or relation cannot be judged from the authorized
  scope; state exactly what is absent.

When a unit has both a confirmed defect and an unresolved risk, its controlling
coverage state is `finding` and both finding IDs remain linked. Coverage states do
not replace Review's finding status, diagnostic dimension, severity, confidence,
evidence class, repair boundary, or resolution test.

## Keep visible per-unit ledgers

Review exposes enough detail to prove coverage, including passed units:

- paper row: archetype, thesis, claim/evidence spine, boundary, state, finding IDs;
- intellectual-move dependency row when applicable: shared move, advertised
  outcome, original anchors, causal layer, source status, counterfactual, coverage
  state, and finding IDs;
- section row: expected and actual obligation, entering question, delivered answer,
  claim/evidence contribution, incoming/outgoing handoff, state, finding IDs;
- paragraph row: section, signaled/intended role when observable, delivered role,
  role convention, one-obligation result, expected/actual opening, development,
  payoff/handoff and its information gain, sentence roles, neighbor relation,
  dimension states, controlling state, and finding IDs;
- sentence row: dominant assertion, function, actor/action/object, evidence state,
  condition/boundary, incoming/outgoing relation, language state, finding IDs;
- lexical row: occurrence/span, sentence ID, technical or grammatical function,
  applicable checks, state, finding IDs.

Every risk-bearing lexical occurrence gets its own row. Contiguous ordinary passed
occurrences may be range-compressed only when the exact sentence-local span and
occurrence count are shown; the compression means every occurrence in the range
was checked, not sampled. Never hide clean sections, paragraphs, sentences, or
lexical spans behind a findings-only list.

A local review may keep finding explanations compact, but it still shows all
in-scope unit rows and its coverage receipt. For a large paper, continue the
ledgers in numbered batches or an explicitly authorized report artifact. Mark the
review `incomplete` until the final batch and reconciliation are delivered.

Revise maintains the same full-scope ledgers before and after editing. It normally
returns the manuscript first, followed by a compact closure map and manuscript
coverage receipt; if the author explicitly asks for prose only, keep these
ledgers internal and follow the prose-only exception in the revision protocol.
The compact decision coverage receipt remains mandatory after prose-only output.
Grill displays only the source units and findings being decided; it does not rerun
the full audit.

## Account for decision history independently

Before Review or Revise reports a manuscript judgment, follow the decision-record
rules to resolve the authorized record, classify every literal version ID, and
derive the effective, applicable, and executable sets. Decision accounting is
orthogonal to unit coverage: `Unreviewed: 0` cannot hide an unaccounted decision,
and `Unaccounted decisions: 0` cannot hide an unreviewed manuscript unit.

Broken lifecycle links, conflicting heads, unavailable history, and decisions
excluded from execution remain visible in the decision receipt. They do not
authorize guessing or suppress inspection of unaffected manuscript units. During
an interactive Revise pause, report current decision accounting without calling
the manuscript coverage or finding closure terminal.

## Preserve IDs and close the loop

Review assigns stable finding IDs and includes the affected unit/link IDs, status,
repair boundary, observable resolution test, and one next-action class from the
shared workflow contract: `direct repair`, `author clarification`, `author
evidence`, `external blocker`, or `optional/not applied`. A finding that needs
author intent is routed to clarification; one that needs scientific support is
routed to author evidence or an external blocker without treating confirmation
of intended wording as proof.

Grill carries the Review finding and unit IDs into the decision record when they
exist. It records the author's meaning, evidence state, permitted edit, and
materially rejected alternatives. `pending` is not revision authority.

During an interactive revision, `pending clarification` is a non-terminal
workflow state for an author-answerable item. It is neither `blocked` nor a
closure state. Revise asks the complete ready frontier and resumes the same
revision after the author answers. It maps every received finding to one closure
state only after no requested item remains pending:

- `closed`: the authorized edit or already-satisfied text passes the original
  resolution test and the post-edit full-scope audit;
- `blocked`: an external prerequisite remains unavailable, or the author has
  explicitly declined, cannot provide, or confirms unavailable the exact
  clarification or evidence requested;
- `not applied`: the item is rejected, optional, outside the current edit scope,
  stale, or conflicts with a newer decision; state which condition applies;
- `reopened`: the original problem persists or the edit creates an equal-or-higher
  impact regression.

No finding disappears from the handoff. Revise cannot close an item merely because
text changed, and Review cannot claim that a withdrawn claim gained evidence.

## Completion gate and receipt

Before saying an audit or revision is complete, verify all of the following:

1. inventory totals equal ledger totals at every applicable level and for every
   adjacency/dependency class;
2. the recorded last unit at each level has a nonblank state;
3. passed as well as problematic units are represented;
4. every finding maps to all affected units and every received finding has a
   closure state after Revise; an interactive pause instead exposes the pending
   queue and does not claim completion;
5. no unresolved or not-assessable item is described as passed or closed;
6. the bottom-up reconciliation found no new contradiction, scope drift,
   terminology drift, claim-strength change, or evidence promotion;
7. every paragraph was checked independently for promise-versus-delivery role,
   competing obligations, payoff information gain, and evidence status, so a
   blocker in one dimension did not suppress a finding in another;
8. every assessable central node and dependency has a source status; when the text
   claims one move yields several outcomes, every advertised outcome appears in
   the fan-out ledger and every reviewer-hypothesized edge remains a finding or
   unresolved risk;
9. every decision version read has a status and set classification, with conflicts
   and exclusions named rather than silently resolved;
10. `unreviewed = 0` and `Unaccounted decisions: 0`. If either is false or
    unknown, the result is explicitly `incomplete`.

End Review and completed non-prose-only Revise reports with a coverage receipt.
Do not emit a terminal receipt while any requested finding is `pending
clarification`:

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

Omit levels and the intellectual-move dependency line when they do not exist, but
retain higher levels that are unavailable as `not assessable`. Then emit the
decision coverage receipt defined by the decision-record rules. A receipt proves
bounded execution only; it does not establish paper acceptance, novelty over
uninspected literature, or correctness outside the authorized evidence.
