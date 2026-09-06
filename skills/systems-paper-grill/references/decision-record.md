# Paper Decision Record

Use one author-authorized *paper-decisions.md* per paper. It is an append-preserving
decision ledger: the current decision is derived from the complete version
history, never substituted for that history. The record belongs to the paper,
not to the installed skills or this skill-source repository.

## Resolve the record before completion

An explicitly named paper project authorizes the default record at that project's
root. If the file is absent, report that its history contains zero versions and
continue; Review and Revise keep it absent, while Grill creates it when the first
substantive decision must be persisted. For pasted text, an ambiguous project, or
a manuscript-only path with no established record location, ask for the record
path or ask the author to explicitly confirm no prior decision history for this
scope. Filesystem accessibility alone does not select a paper project.

Read the complete authorized record before classifying or changing any entry.
Preserve unrelated entries and author text. A standalone or embedded Grill may
discuss while the record path is unresolved, but it cannot declare a substantive
decision complete or return control to Revise until that decision is persisted
and read back from an authorized path. An explicit no-history confirmation lets
Review or Revise account for zero prior versions; it does not waive persistence
for a new substantive Grill decision.

## Versioned full snapshots

Use a versioned full snapshot for each substantive state. Give each issue a
stable lineage such as `D7` and each substantive state a
monotonically increasing version such as `D7.v1`, `D7.v2`. Every version is a
complete snapshot: source finding and unit IDs, original anchor, problem,
decision, reason, allowed edit, evidence state and basis, confirmation basis, and
resolution test. It must make sense without replaying deltas or chat turns.

Use exactly one lifecycle status per version:

- `pending`: the proposal or answer is incomplete or not explicitly confirmed;
- `confirmed`: the author explicitly confirmed the snapshot's meaning and allowed
  action;
- `rejected`: the author declined that candidate;
- `superseded`: a later version replaced this snapshot while retaining it as
  history.

Use the applicable same-lineage relations with exact version IDs:

- `Proposes replacement for`: a pending candidate's target; it has no authority
  effect;
- `Supersedes`: the prior snapshot replaced by this confirmed version;
- `Superseded by`: the reciprocal pointer on the replaced snapshot.

An existing unversioned entry such as `D0` is a valid legacy snapshot. Preserve
and report its literal ID. If it later evolves, append `D0.v2` and link the legacy
entry as the first snapshot rather than renaming or rewriting it.

The snapshot payload is immutable after it is written. A lifecycle-only response
that confirms or rejects the exact pending payload may update that candidate's
status, confirmation basis, and lifecycle links. A substantive change to meaning,
reason, evidence, allowed edit, scope, anchor, or resolution test creates a new
complete version. Never reuse an ID. Rejected and superseded versions stay
terminal; renewed consideration creates another version. Do not add dates,
version headings outside the entry ID, a changelog, or a chronological transcript.

## State transitions and authority

A new pending candidate never displaces a confirmed head:

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

If an author answer materially changes a pending candidate, append a full new
snapshot. Earlier pending alternatives remain visible; mark one rejected only
when the author rejects it, or superseded only when the newer snapshot actually
replaces it. Multiple pending alternatives do not affect the confirmed head.
Before confirming a successor, ensure its target is still the one effective
confirmed head and ask the author to resolve any competing or stale candidate
that would make the intended replacement ambiguous.

When replacing a confirmed head, update both sides in the same filesystem write
and read back both entries. A crash or failed write must leave the prior file as
the authority; do not report the promotion complete from an in-memory draft.
Core text and original confirmation basis of the older confirmed snapshot remain
unchanged; update only its lifecycle status and `Superseded by` pointer.

## Record decisions rather than transcripts

Each snapshot states a decision, reason, and open question once. Preserve the
source finding's repair boundary and observable resolution test. Keep diagnosis,
intended meaning or role, scientific evidence, and edit authority distinct when
more than one matters. Structural permission names the exact split, merge, move,
or purpose change, source unit, destination, and resulting role. A placement
question stays pending.

For an intellectual-move fan-out issue, record the common changed constraint or
boundary and one compact edge per advertised outcome, including causal layer,
source or author basis, counterfactual, and allowed location. An answer confirming
the common move does not confirm every outcome edge.

Track evidence as `supported`, `missing`, or `conflicting`, with its concrete
basis. A confirmed intention with missing evidence is not an executable factual
addition. Author-supplied implementation facts can be attributed as such;
agreement with an assistant hypothesis does not establish an experiment, proof,
or result. Keep materially rejected alternatives when doing so prevents their
reintroduction. Routine grammar fixes need no entry unless they clarify an agreed
edit.

Record durable paper decisions, not transient session restrictions. Grill's
read-only manuscript boundary belongs in its instructions; the record states an
allowed future edit. A completed discussion still does not authorize an edit
outside the active Revise request.

## Derive the decision sets

Review and Revise account for the record before judging or editing. Derive these
sets from literal entries rather than a cached current-head list:

1. **All versions:** every literal ID, including pending, confirmed, rejected,
   superseded, and legacy entries.
2. **Effective heads:** confirmed versions not validly superseded by a confirmed
   same-lineage successor.
3. **Applicable heads:** effective heads whose manuscript scope and meaning-based
   anchor match the current authorized material.
4. **Executable heads:** applicable heads whose evidence is compatible, whose
   links are conflict-free, and whose allowed action covers the current operation.

Only executable heads may constrain a manuscript change. During read-only Review,
an applicable confirmed intention may inform interpretation, but cannot clear a
scientific defect, supply missing evidence, or authorize an edit. Pending,
rejected, superseded, stale, out-of-scope, evidence-conflicting, or structurally
conflicted versions remain history rather than authority.

The ledger is editorial input, never manuscript text and never higher authority
than a newer explicit author correction in the current request. A direct edit
instruction can authorize its named change without pretending it was prior
history. If that correction is settled through Grill, persist it as a new version
before Grill completes or an embedded Revise resumes.

Match locations using anchors and meaning; paragraph numbers can change. If the
current text already satisfies an executable decision, preserve it. Never broaden
a confirmed local edit into a paper-wide rewrite.

Treat duplicate IDs, unknown statuses, missing link targets, cross-lineage links,
cycles, nonreciprocal confirmed supersession, a supposedly superseded head whose
successor is not confirmed, or more than one effective confirmed head in a
lineage as conflicts. Do not choose by file order, highest version, or timestamp.
Account for every version, make the affected lineage non-executable, and ask only
for the smallest repair to the record or author decision. Review stays read-only;
Revise leaves affected prose unchanged.

## Decision coverage receipt

Every Review and every Revise response reports decision accounting separately
from manuscript-unit coverage. Include it even when the author requests prose
only; in that mode place one compact line after the manuscript. Report:

```text
Decision coverage: record=<authorized path | absent at named project | author-confirmed none | unresolved>; all=<literal IDs>; status=<pending:n, confirmed:n, rejected:n, superseded:n, unknown:n>; effective=<IDs>; applicable=<IDs>; executable=<IDs>; not applicable=<ID:reason | none>; conflicts=<ID/relation:reason | none>; Unaccounted decisions: 0
```

`Unaccounted decisions: 0` means every version read was classified; it does not
mean every decision is valid or applied. When the record location or contents are
still unavailable, ask for them and report `Unaccounted decisions: unknown`
instead of claiming completion. A non-terminal Revise clarification pause may
still give this accounting receipt; it is not a finding-closure or manuscript
coverage completion receipt.

Revise, not Grill, assigns finding closure after the post-edit full-scope audit.
Review does not mutate the record. Revise does not rewrite it to match its output.
A newly discovered conflict returns to Grill or the author; no stage silently
repairs decision history.
