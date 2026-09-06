# Shared Paper Workflow Contract

Review checks; Grill discusses and records; Revise edits. All three use [writing-core.md](writing-core.md) as the same standard for paragraph purpose, high-level explanation, sentence and paragraph logic, precision, and concision. They use the [shared coverage contract](coverage-contract.md) for stable unit IDs, top-down execution, visible accounting, and finding closure. The shared archetype and Chinese references specialize that standard; review checklists add diagnostic detail, not a different quality bar.

## Same judgment, different action

Before Review or Revise judges prose, resolve and account for its decision history
under the [decision-record rules](../../systems-paper-grill/references/decision-record.md).
Use an explicitly established record path, or *paper-decisions.md* at the root of
an explicitly named paper project. An absent record in that project means zero
history and is not created by Review or Revise. For pasted text, ambiguous project
ownership, or a manuscript-only path, ask for the record or the author's explicit
confirmation that this scope has no prior history. Do not search neighboring
projects. This lookup rule does not create project configuration or expand
manuscript scope.

Read every decision version and derive all, effective, applicable, and executable
sets before using any entry. Only an effective, applicable, evidence-compatible,
conflict-free confirmed version with authority for the current operation may
constrain a manuscript change. Pending, rejected, superseded, stale, conflicting,
and out-of-scope versions remain visible history. Every Review and Revise reports
the separate decision coverage receipt, including `Unaccounted decisions: 0`;
even a prose-only Revise returns its compact receipt after the manuscript.

For the same passage and available evidence, all three skills distinguish:

- **Confirmed defect:** identify the original anchor, failed standard, and supporting evidence. Review explains it; Revise performs the authorized repair and checks that the same defect is resolved.
- **Unresolved reviewer risk:** identify the missing context, premise, evidence, or author decision. Neither skill treats uncertainty as an established error or invents its resolution.
- **Style preference:** a defensible alternative, not a mandatory correction. Review labels it as optional; Revise follows its optional-wording output contract.

An unchanged unsupported assertion remains unresolved, not acceptable simply because editing it is unauthorized. Adequate wording does not become defective because another formulation is possible. Reassess a finding when new evidence or author clarification changes its basis; explain that change rather than silently reversing the judgment.

A reviewer reconstruction is a hypothesis about the manuscript, not author
evidence. When Review recovers a central argument, it marks each node and edge
`stated`, `text-licensed`, or `reviewer-hypothesized` under the writing core. A
reviewer-hypothesized edge remains a finding or unresolved risk even when the
completed reconstruction is elegant. Grill may confirm the intended relation and
its evidence; Revise may express it only after that relation is supported and the
author has authorized the affected edit boundary.

Treat author input as four separable things: diagnosis or dissatisfaction,
intended meaning/role, scientific evidence, and edit authority. A question such as
`should this be a Challenge paragraph?`, a placement hypothesis, or agreement that
the current prose is awkward establishes neither a measured result nor permission
to split, move, merge, or repurpose text. Structural authority requires an explicit
instruction or confirmation naming the allowed operation and target boundary.

Review assigns each finding a stable ID, affected section/paragraph/sentence/lexical
unit or relation IDs, repair boundary, and observable resolution test. These IDs
survive discussion and revision even when prose changes; short quotations preserve
identity when paragraph numbering becomes stale. Every handoff retains all
findings, including passed controls that matter to preservation, unresolved items,
and rejected preferences. No stage silently drops an item because it is inconvenient
or outside its own action authority.

Each finding also carries one next-action class. A mixed finding is decomposed so
each independent subrepair has its own action. This is routing metadata, not a
closure judgment:

- `direct repair`: a meaning-preserving authorized edit can be made from current
  evidence without asking the author;
- `author clarification`: intent, claim strength, terminology, paragraph role, or
  an exact structural operation and destination must be chosen by the author;
- `author evidence`: the author must supply a premise, implementation fact,
  metric, baseline, condition, result, uncertainty, citation, or other evidence
  that may exist but is not currently available;
- `external blocker`: the prerequisite cannot be answered by an author decision,
  author-supplied material, or a permission question in the current workflow and
  requires new research or context, artifact, or source that is genuinely
  inaccessible after allowed checks;
- `optional/not applied`: the item is a style preference, rejected, stale,
  conflicting, already satisfied, or outside the current edit scope; state which.

When it is unclear whether missing material exists, prefer `author evidence` and
ask for it. Do not promote an author-answerable item to `external blocker` merely
because it was absent from the Review scope or because verification needs the
author's permission; ask that permission as `author clarification`.

## Discuss uncertain logic with the author

Use Grill when a needed repair depends on unresolved author intent, competing technical interpretations, an absent scientific premise, actual experiment outcomes, a shared prior-work root cause, placement against unseen context, or a decision to change the claim or paragraph structure. Review assigns the action class and gives the exact unit IDs. Ordinary grammar, category alignment, redundancy, and unambiguous local logic repairs need no interview when they preserve meaning. In particular, if prose says a property cannot replace proof of already named properties, Revise may align the comparison to those object-level properties while preserving the original claim strength and leaving its evidence unresolved. Review can report the rest of its findings; Revise completes every safe local subrepair before asking about the author-answerable frontier.

A request to Revise against Review findings already authorizes an embedded
clarification loop for every prerequisite-ready `author clarification` and
`author evidence` item on that repair queue. Revise must not wait for a separate
request to use Grill, tell the author to start another task, or convert those
items directly into terminal blockers. It first applies all independent `direct
repair` items, then asks the whole ready frontier in the Grill round format,
including a recommendation and the exact answer or evidence needed. It labels
these items `pending clarification`, waits for the author's answers, recomputes
the frontier, and resumes the same revision automatically. `pending
clarification` is a non-terminal workflow state, not a closure state and not a
completed revision. An explicit one-shot, no-discussion, or prose-only request
may opt out; preserve the affected prose and report the unresolved item under
that output contract.

Standalone Grill remains available when discussion itself is requested. It asks
paper-specific questions and records the answers using the [decision-record
rules](../../systems-paper-grill/references/decision-record.md) when a record
location is authorized. A read-only Review request does not authorize record
writes or start revision. Keep the discussion within the supplied manuscript
scope and shared standard.

Wait for the author's answer before applying the disputed repair. A recommendation
is not confirmation; agreement with a writing goal supplies neither experimental
evidence nor an unstated mechanism. Grill persists each substantive intermediate
or settled outcome as a versioned full snapshot in the authorized paper decision
record. A pending successor does not displace the confirmed head; confirming a
successor atomically records both sides of the supersession relation. Rejected
and superseded snapshots remain in the ledger. When Review IDs exist, each
version carries the source finding and unit IDs, original resolution test,
intended meaning, evidence state, and allowed edit. Confirmation applies only to
the named meaning and allowed edit, not every suggestion in the conversation.
Grill reads back each material update before it claims completion or returns an
embedded clarification to Revise.

Terminal `blocked` is reserved for an `external blocker`, or for an
author-answerable item after the author explicitly declines, cannot provide the
required input, or confirms that it is unavailable. Silence while Revise is
waiting is not a terminal decision. If the author supplies only part of an
answer, settle that part, retain the remainder as `pending clarification`, and
ask the newly ready frontier rather than issuing a completion receipt.

For common blockers, Grill asks for the smallest decisive input: the shared
assumption or mechanism that causes a related-work gap; the metric, baseline,
conditions, result, and uncertainty needed for an evidence-derived conclusion;
the common changed constraint or boundary and each move-to-outcome causal edge
when several headline properties are claimed to share one insight; the causal
layer supplied by an enabling substrate versus complementary runtime mechanisms;
the intended paragraph role and whether mechanism detail may move; the exact
split/merge/move operation and destination; or the broad-reader claim that a
limitation constrains. If the author supplied that input already, use it without
reconfirming.

## Carry the decision into revision

Review findings and Grill discussion are editorial input, not manuscript prose. Revise uses the original anchors, diagnosis, supplied evidence, and explicitly confirmed decision to make only the requested change. A completed review or discussion does not itself authorize editing files or moving content across paragraphs.

Before editing, read the authorized decision record and any newer explicit author
corrections alongside the original manuscript and supplied Review findings.
Follow the decision-record rules to match anchors, separate confirmation from
evidence, validate lifecycle links, and handle stale or conflicting lineages. Use
only executable heads at their named locations; do not treat the whole history as
a list of edits. A material embedded clarification must be persisted before
revision resumes. In a new task, request unavailable source text or decisions
rather than guessing them.

After revision, re-audit the complete frozen scope under the coverage contract, including unchanged passed units. Only when no requested item remains `pending clarification`, map every received finding to terminal `closed`, `blocked`, `not applied`, or `reopened`. Close a finding only when its original resolution test passes without changing another supported proposition or introducing a new defect. A rejected item is not applied; missing scientific support is blocked only under the terminal-blocker rule above, even when intended wording is confirmed. Deleting the question, condition, boundary, or claim that missing evidence was supposed to answer does not close an evidence-derived-payoff finding unless the author explicitly withdraws that scientific proposition. Review stays read-only throughout; a review request does not automatically start revision.
