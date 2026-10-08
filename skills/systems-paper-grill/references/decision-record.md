# Paper Decision Record

Use one author-authorized *paper-decisions.md* for each paper.
Keep the full version history in this decision ledger.
Find the effective decision from that history.
Keep the record with the paper.
Do not put the record in the installed skills or this skill-source repository.

## Find the record before completion

For a paper project with an author-supplied name, use *paper-decisions.md* at the project root.
If there is no record, give zero history in the report.
If there is no record, do not write one during Review and Revise.
If there is no record, write it before the first Grill decision with changed decision content.

For pasted text or unknown project ownership, get the record path or author's no-history confirmation for the supplied scope.
For a manuscript-only path without a record path, get that path or the author's no-history confirmation.
Filesystem access does not give paper-project permission.

Before classification or entry changes, read the full authorized record.
Keep unrelated entries and author text.
While the record path is unknown, let standalone or embedded Grill continue.
Before completion of a changed decision, save the decision at an authorized path.
Read that saved decision again.
Before you let Revise continue, make sure these persistence and read-back checks show correct saved content.

No-history confirmation gives Review or Revise zero previous versions.
After that confirmation, save each Grill state with changed decision content before completion.
No-history confirmation does not remove the persistence requirement.

## Versioned full snapshots

For each state with changed decision content, write a versioned full snapshot.
Give each issue a stable lineage, such as `D7`.
For each decision-content change, give a higher version ID than all previous versions in the same lineage.
For example, use `D7.v1`, then `D7.v2`.
Include all these fields in each snapshot:

- Source finding and unit IDs
- Source anchor
- Problem
- Decision
- Reason
- Allowed edit
- Evidence state and basis
- Confirmation basis
- Resolution test.

Make sure that each snapshot makes sense without previous changes or chat turns.

For each version, use one lifecycle status only:

- `pending`: The proposal or answer is not full or has no author confirmation.
- `confirmed`: The author gave confirmation of the snapshot's meaning and permitted action.
- `rejected`: The author rejected that candidate.
- `superseded`: A version that follows replaced this snapshot but kept it in the history.

For same-lineage relations, use the literal version IDs:

- `Proposes replacement for`: The pending candidate's target. This relation gives no authority.
- `Supersedes`: The previous snapshot that this confirmed version replaced.
- `Superseded by`: The reciprocal pointer on the replaced snapshot.

An unversioned entry in the record, such as `D0`, is a permitted legacy snapshot.
Keep its literal ID.
Include that ID in the decision report.
If legacy decision content changes, add `D0.v2`.
Connect that version to the legacy entry as the first snapshot.
Keep the legacy entry's name and core text.

After a write, keep the snapshot payload immutable.
For confirmation or rejection of the same pending payload, update only its status, confirmation basis, and lifecycle links.
If decision content changes, write a new full version.
Decision content includes meaning, reason, evidence, allowed edit, scope, anchor, and resolution test.
Do not reuse an ID.

Keep rejected and superseded versions terminal.
For reconsideration, write a new version.
Do not put dates, other version headings, changelogs, or chronological transcripts in the ledger.
Use the entry ID as the only version heading.

## State transitions and authority

Keep the confirmed head effective while a pending candidate is present.

```text
D7.v1 confirmed
  -> append D7.v2 pending; proposes replacement for D7.v1
     D7.v1 remains the effective confirmed head
  -> author confirms the exact D7.v2 payload
     one atomic record update:
       D7.v1 = superseded; Superseded by D7.v2
       D7.v2 = confirmed; Supersedes D7.v1
  -> or author rejects D7.v2
       D7.v2 = rejected; D7.v1 remains confirmed and effective
```

If an author answer changes a pending candidate's decision content, add a full new snapshot.
Keep previous pending alternatives in the record.
Only after the author's rejection, give an alternative the `rejected` status.
Only after a newer snapshot replaces it, give an alternative the `superseded` status.
Multiple pending alternatives do not change the confirmed head.

Before successor confirmation, make sure that its target is the one effective confirmed head.
If competing or stale candidates make the replacement not clear, get the author's decision before confirmation.

When a confirmed head changes, update the reciprocal links in one atomic filesystem write.
Read each changed entry again.
On a crash or failed write, keep the previous file as authority.
Do not give an in-memory draft as evidence of a saved promotion.

Keep the previous confirmed snapshot's core text and initial confirmation basis the same.
Update only its lifecycle status and `Superseded by` pointer.

## Record decisions

Record each decision, reason, and open question one time in each snapshot.
Keep the source finding's repair boundary and resolution test with a result that readers can see.
Do not use diagnosis, intended meaning or role, scientific evidence, or edit authority as evidence for a different type.
For structural permission, record the operation given by the author:

- Split
- Merge
- Move
- Purpose change.

Record the source unit, destination, and the role after the change.
Keep a placement question pending.

For an intellectual-move fan-out issue, record the same changed constraint or boundary.
Record one edge with a short description for each claimed outcome.
Include its causal layer, source or author basis, counterfactual, and permitted location.
Confirmation of the same move gives no confirmation of the outcome edges.

For evidence, use `supported`, `missing`, or `conflicting` with a basis in source evidence.
If evidence is missing, do not add a fact from confirmed intention.
Give the author as the source of author-supplied implementation facts.
Agreement with an assistant hypothesis does not supply an experiment, proof, or result.
When necessary to prevent reintroduction, keep alternatives with author rejection.

For grammar fixes, give a decision entry only if the fix makes a confirmed edit clear.
Record paper decisions applicable after the session.
Do not put temporary session restrictions in the record.
Keep Grill's read-only manuscript boundary in its instructions.
Record the permitted future edit in the decision record.
Completed Grill gives no permission for edits not in the active Revise request.

## Find the decision sets

Before manuscript judgment or edits, give a classification to each version in the full record.
Find these sets from literal entries:

1. **All versions:** Each literal ID: pending, confirmed, rejected, superseded, and legacy entries.
2. **Effective heads:** Confirmed versions without correct supersession by a confirmed same-lineage successor.
3. **Applicable heads:** Effective heads with manuscript scope and meaning-based anchors that agree with the authorized source text.
4. **Executable heads:** Applicable heads with evidence compatibility, conflict-free links, and permission for the requested operation.

Do not use a cached head list to find these sets.
Use only executable heads as authority for manuscript changes.
During read-only Review, use applicable confirmed intention only for text interpretation.
Do not use that intention as evidence for a scientific defect's resolution.
Do not use it as missing evidence or edit permission.

Keep these versions as history, not revision authority:

- Pending
- Rejected
- Superseded
- Stale
- Out of scope
- Evidence-conflicting
- Structurally conflicting.

Use the ledger as editorial input.
Do not put the ledger in manuscript prose.
When this request corrects the ledger, obey the author's correction.
An edit instruction gives permission for its given change.
Do not record that instruction as history before this request.

After the author gives confirmation of that correction through Grill, save it as a new version before Grill completion.
Before an embedded Revise resumes, complete the persistence and read-back checks for each authorized record update.
If the request excludes persistence, retain the answer in conversation as current-request authority and resume the same scoped revision.
Keep chat-only answers separate from saved decision history.

Find locations through anchors and meaning.
Paragraph numbers can change.
If the text agrees with an executable decision, keep it the same.
Keep each confirmed edit in its authorized local boundary.

Give these cases the conflict classification:

- Duplicate IDs
- Unknown statuses
- Missing link targets
- Cross-lineage links
- Cycles
- Nonreciprocal confirmed supersession
- A superseded head without a confirmed successor
- Multiple effective confirmed heads in one lineage.

Do not select revision authority by file order, highest version, or timestamp.
Give each version a classification.
Keep the affected lineage non-executable.
Get the smallest necessary repair to the record or author decision.
For Review, keep the record read-only.
For Revise, keep affected manuscript prose the same.

## Decision coverage receipt

For each Review and Revise response, give decision accounting in a different receipt from manuscript-unit coverage.
For prose-only output, put one short receipt line after the manuscript.
Honor an explicit manuscript-body-only request or receipt exclusion; keep decision accounting internal.
Use this receipt schema:

```text
Decision coverage: record=<authorized path | absent at named project | author-confirmed none | unresolved>; all=<literal IDs>; status=<pending:n, confirmed:n, rejected:n, superseded:n, unknown:n>; effective=<IDs>; applicable=<IDs>; executable=<IDs>; not applicable=<ID:reason | none>; conflicts=<ID/relation:reason | none>; Unaccounted decisions: 0
```

`Unaccounted decisions: 0` shows that each version read has a classification.
It does not show that each decision is correct or used.
When the record path or content is not available, get it from the author.
Give `Unaccounted decisions: unknown` in the receipt.
Do not claim completion.

During a Revise clarification pause, give decision accounting for the versions read.
Do not use that accounting as terminal finding closure or manuscript coverage receipts.

After the full post-edit audit, let Revise give each finding its closure state.
For Review, keep the record the same.
For Revise, do not change decision history to agree with manuscript output.
When you find a new conflict, give it to Grill or the author.
Do not repair decision history without the author's decision.
