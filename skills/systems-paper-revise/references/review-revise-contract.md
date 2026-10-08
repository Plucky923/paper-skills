# Shared Paper Workflow Contract

Review does checks, Grill discusses and records, and Revise edits.
All three use [writing-core.md](writing-core.md) for paragraph purpose, explanation level, logic, precision, and concision.
They use the [shared coverage contract](coverage-contract.md) for unit IDs, top-down checks, visible accounting, and finding closure.
The archetype and Chinese references add specialized requirements.
Review checklists add diagnostic detail, not a different quality standard.

## Same judgment, different action

Before a manuscript judgment, do decision-history resolution with the [decision-record rules](../../systems-paper-grill/references/decision-record.md).
Use a clearly shown record path.
If no record path is established for a clearly named paper project, use *paper-decisions.md* at its root.
An absent record in that project means zero history.
Review and Revise do not make that record.

For pasted text, ambiguous project ownership, or a manuscript-only path, give the author a record-location question.
Get the record path or clear confirmation that this scope has no history.
Do not search neighboring projects.
This lookup does not make project configuration or expand manuscript scope.

Read each decision version.
Derive all, effective, applicable, and executable sets before entry use.
Only an executable confirmed version can constrain a manuscript change.
It must be effective, applicable, evidence-compatible, conflict-free, and permitted for the requested operation.
Keep pending, rejected, superseded, stale, conflicting, and out-of-scope versions as visible history.

Give a decision coverage receipt in each Review and Revise result, independently of manuscript coverage.
Include `Unaccounted decisions: 0` when the accounting covers all versions.
For prose-only Revise, put its compact receipt after the manuscript.
Honor an explicit author restriction to manuscript body only or exclusion of receipts; keep that accounting internal.

For the same passage and evidence, keep these judgments as different categories:

- **Confirmed defect:** Find the initial anchor, failed standard, and evidence.
  Review gives the explanation for the defect.
  Revise makes the permitted repair and does the initial resolution test.
- **Unresolved reviewer risk:** Find the missing context, premise, evidence, or author decision.
  The skills do not accept uncertainty as a shown error or invent a resolution.
- **Style preference:** Give a defensible optional alternative.
  It is not a required correction.
  Review gives it the optional status.
  Revise obeys its optional-wording output contract.

An unchanged unsupported assertion stays unresolved even when an edit is not permitted.
Sufficient wording does not become defective because an alternative is available.
If new evidence or author clarification changes a finding's basis, examine that finding again.
Give the reason for the changed judgment.
After an explicit author withdrawal or replacement, recheck each linked finding against the propositions still asserted.
Keep its original ID, anchors, resolution test, and missing-evidence history.
Use `not applied` with the author decision when that requirement no longer applies; do not report the old test passed.
Audit the retained claim with evidence appropriate to its inference type.
Actual author-supplied observations are evidence inputs, separately from intent and edit permission.
A bounded qualitative observation does not assert a quantitative metric, comparative gain, causal explanation, or general guarantee.
Do not reopen a question only to satisfy an evidence requirement for the explicitly withdrawn proposition.
An inherited missing-input list does not itself establish a current scientific obligation.
Keep independently retained results, comparisons, guarantees, questions, conditions, and boundaries subject to their evidence requirements.
An absent outcome or a weaker verb alone does not remove those requirements.

A reviewer reconstruction is a manuscript hypothesis, not author evidence.
For each central node and edge, use the writing core's source status:

- `stated`
- `text-licensed`
- `reviewer-hypothesized`.

A `reviewer-hypothesized` edge stays a finding or unresolved risk when an in-scope claim or promised role requires it, even when reconstruction has clear dependencies.
Identify that claim and its visible endpoints before routing an author question.
Missing whole-paper context alone creates no local repair obligation.
If an inherited finding requires an unasserted claim or an out-of-scope paper decision, preserve its ID and original test as `not applied`, with the scope reason.
Do not claim that its original test passed, discard independently supported risks, or apply a pending decision.
Grill can get the author's relation and evidence.
Revise can write it only with support and author permission for the affected edit boundary.

Record four types of author input in different categories:

- Diagnosis or dissatisfaction
- Intended meaning or role
- Scientific evidence
- Edit permission.

`should this be a Challenge paragraph?`, a placement hypothesis, or agreement about awkward prose does not show a measured result.
It also does not give permission for text splitting, movement, combination, or repurposing.
For structural permission, get a clear instruction or confirmation with the operation and target boundary.

Review gives each finding a stable ID and these fields:

- Affected section, paragraph, sentence, lexical, or relation IDs
- Repair boundary
- Observable resolution test.

Keep those IDs during discussion and revision, even after prose changes.
If paragraph numbering becomes stale, use short quotations to keep identity clear.
Each handoff keeps all findings and important passed controls.
Keep unresolved items and rejected preferences visible.
Do not drop an item because it is difficult or not permitted by this skill.

Give each finding one next-action class.
Divide a mixed finding into independent repairs, each with its own action.
This class gives routing, not closure:

| Class | Required action or state |
|---|---|
| `direct repair` | An identified defect has a permitted edit that keeps meaning and uses available evidence. An author question is not necessary. |
| `author clarification` | The author must select intent, claim strength, term, paragraph role, or specified structural operation and destination. |
| `author evidence` | The author must supply a missing premise, implementation fact, metric, baseline, condition, result, uncertainty, citation, or other evidence. |
| `external blocker` | No author decision, supplied material, or permission answer can supply the prerequisite in this workflow. New research or inaccessible context, artifact, or source is necessary. |
| `optional/not applied` | The item is optional, rejected, stale, conflicting, satisfied, or not in edit scope. Give the applicable reason. |

If the missing material's availability is unclear, use `author evidence`.
Request that material.
Absence from Review scope alone does not make an item an `external blocker`.
If author permission is necessary for verification, put that question in `author clarification`.

## Discuss uncertain logic with the author

If an author choice or missing scientific input is necessary for a repair, use Grill.
Applicable inputs include intent, competing technical interpretations, premises, experiment outcomes, or a shared prior-work root cause.
They also include placement against unseen context and claim-strength or paragraph-structure decisions.
Review gives the action class and specified unit IDs.

An interview is not necessary for meaning-preserving grammar, category, redundancy, or clear local-logic repairs.
A statement about a property's inability to replace proof can have an independent category defect.
If the system obligations have names in the source, compare those object-level properties.
Keep the initial claim strength and its unresolved evidence status.
Complete each permitted meaning-preserving local repair before the author-input questions.

A request to revise against Review findings gives permission for an embedded clarification loop.
It includes each prerequisite-ready `author clarification` and `author evidence` item in that queue.
Do not wait for another Grill request or tell the author to start another task.
Do not give these items terminal blocker states immediately.
Limit the ready question queue to inputs that affect a requested repair or its authority.
Keep supplied plans as plans unless the user requests a change to established claims.
When no permitted repair depends on manuscript lifecycle, record it as unknown instead of asking a separate question.

Do the loop in this order:

1. Apply all independent `direct repair` items.
2. Give the full ready question queue in Grill round format.
3. Include a recommendation and the specified answer or evidence necessary for each question.
4. Set those items to `pending clarification`.
   Tell the author that their answers will resume this revision.
5. Wait for author answers.
6. Recalculate the ready question queue.
7. Continue the same revision automatically.

`pending clarification` is a non-terminal workflow state.
It is not a closure state or a completed revision.
A clear one-shot, no-discussion, or prose-only request can exclude the loop.
In that case, keep affected prose and give the unresolved issue with the applicable output contract.

Use standalone Grill when the user requests discussion itself.
Give paper-specified questions.
If the record location is permitted, record answers with the [decision-record rules](../../systems-paper-grill/references/decision-record.md).
A read-only Review request gives no permission for record writes nor revision.
Keep discussion in the supplied manuscript scope and shared standard.

Before the disputed edit, wait for the author's answer.
A recommendation is not confirmation.
Agreement with a writing goal gives neither experimental evidence nor an unstated mechanism.
Save each substantive intermediate or settled Grill outcome as a versioned full snapshot when the record is writable within scope.
Use only the permitted paper decision record.
When persistence is explicitly excluded, retain the answer and its anchors in the conversation as current-request authority.
Keep the same revision open and resume after the necessary answer.
Do not represent a chat-only answer as saved decision history.

A pending successor does not replace the confirmed head.
Confirmation of a successor atomically records the two sides of the supersession relation.
Keep rejected and superseded snapshots in the ledger.
When Review IDs exist, include these fields in each version:

- Source finding and unit IDs
- Initial resolution test
- Intended meaning and evidence state
- Allowed edit.

Confirmation applies only to the named meaning and edit.
It does not apply to each suggestion in the discussion.
Read back each permitted record update before completion or return to embedded Revise.

Use terminal `blocked` only for an `external blocker` or a clear author answer that ends the input request.
Such answers decline the request, cannot supply the input, or confirm its unavailability.
Silence during a wait is not a terminal decision.
If an answer is partial, settle only that part.
Keep the rest `pending clarification`.
Give the newly ready questions without a completion receipt.

For common blockers, request the smallest decisive input:

- The shared assumption or mechanism that causes a related-work gap
- Metric, baseline, conditions, result, and uncertainty for a quantitative or comparative experimental conclusion
- Observed object, setting, outcome, and scope for a qualitative observation
- The common changed constraint or boundary for a claimed shared insight
- Each move-to-outcome edge for its headline properties
- The causal layer supplied by an enabling substrate and complementary runtime mechanisms
- The intended paragraph role and permission for mechanism-detail movement
- The specified split, combination, or movement operation and destination
- The broad-reader claim that a limitation constrains.

If the author supplied the necessary input, use it without another confirmation.

## Carry the decision into revision

Review findings and Grill discussion are editorial input, not manuscript prose.
Use initial anchors, diagnosis, supplied evidence, and confirmed decisions to make only the requested change.
A completed review or discussion alone does not give permission for file edits or cross-paragraph movement.

Before edits, read the permitted decision record and newer clear author corrections.
Read them with the initial manuscript and supplied Review findings.
Apply the decision-record rules to anchors, confirmation, evidence, lifecycle links, and stale or conflicting lineages.
Use only executable heads at their named locations.
The full history is not a list of edits.

Save each important embedded clarification before revision resumes when a writable decision record is within scope.
Otherwise, use the chat-only branch above.
In a new task, request unavailable source text or decisions.
Do not guess them.

After revision, audit the full scope through the coverage contract.
Include unchanged passed units.
After no requested item stays `pending clarification`, give each received finding one terminal closure state.
Use `closed`, `blocked`, `not applied`, or `reopened`.

Close a finding only when its initial test passes without a new defect or another supported proposition's change.
For an explicitly withdrawn proposition, apply the applicability check above and retain its finding as `not applied` when appropriate.
Set a rejected item to `not applied`.
Use `blocked` for missing support only with the terminal-blocker rule, even with confirmed intended wording.
For a terminal evidence blocker, list each missing input needed by the initial resolution test.
For an experimental comparison, name the metric and aggregation, baseline configuration, operating conditions, outcome, and material uncertainty.
Honor a one-shot clarification opt-out by listing missing inputs without opening a question round.
Explain in the terminal report why the supplied information cannot satisfy the resolution test.
An experiment's existence supplies neither its outcome nor authority to withdraw the comparison.
Explain why neither result replacement nor withdrawal can close the finding without the applicable evidence or permission.
Deleting an unresolved scientific question, condition, boundary, or claim does not close its evidence-derived-payoff finding.
Only a clear author withdrawal of that proposition can remove that requirement.

Review stays read-only throughout.
A review request does not automatically start revision.
