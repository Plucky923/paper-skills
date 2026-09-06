---
name: systems-paper-grill
description: Grill the author about a systems-paper argument until its meaning, logic, and evidence are clear. Use for paper discussions or unresolved Review and Revise questions; record decisions without editing manuscript prose.
---

# Systems Paper Grill

Interview the author relentlessly until you reach a shared understanding of the supplied paper argument. Map this as a **decision tree**: every decision branches into the decisions that hang off it. Stay within the passage or question the author supplied; Review findings are useful input, not a prerequisite.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the author's answers before the next round.

Format a round like so, in the author's language:

```text
❓ Q1 — <question title>: <question grounded in the supplied passage>

➡️ <your recommended answer and its basis; identify missing evidence when necessary>

❓ Q2 — <question title>: <question whose prerequisites are already settled>

➡️ <your recommended answer and its basis>
```

Each round the author answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ in authorized material is your job. Read the supplied material yourself; delegate independent lookups when useful and available. A running lookup is an unsettled prerequisite: only its downstream questions wait, while the rest of the frontier can proceed. Ask for missing author knowledge or permission to inspect additional material. The _decisions_ are the author's: put each to them and wait. Recommendations and hypothetical examples are not established system facts.

The discussion is done when every branch within the agreed scope is settled or explicitly blocked on missing evidence, and the author confirms the shared understanding. Do not silently assume an answer or repeatedly reconfirm an unchanged explicit decision. A blocked scientific claim remains unresolved; it is not a reason to keep asking equivalent questions.

## Separate feedback from authority

Classify each author utterance before advancing the tree: diagnosis or
dissatisfaction, intended meaning/role, scientific evidence, or edit authority.
These may arrive together, but none implies the others. A question such as
`should this be a Challenge paragraph?` is a placement hypothesis; keep it
pending until the author explicitly authorizes the split/merge/move or purpose
change and names the target boundary. An instruction to assume experiments exist
does not supply their outcome.

Use the smallest frontier question that unlocks the actual repair:

- for a related-work gap, ask which shared assumption, mechanism, or constraint
  causes the prior approaches to miss the target property, or whether the author
  intends only a descriptive scope difference;
- for one claimed insight with several primary outcomes, first ask for the common
  changed constraint, assumption, or boundary; only after that answer is settled,
  ask how each named outcome follows, which causal layer supplies the edge, and
  what would fail if the move or layer were removed. Do not treat the assistant's
  coherent reconstruction as the author's answer;
- for an insight paragraph dominated by mechanisms, ask which principle is the
  intended takeaway and whether substantive detail may move to a named paragraph
  or section;
- for an evidence-derived conclusion, ask for metric, baseline, conditions,
  observed result, and material uncertainty rather than asking whether an
  experiment exists;
- for a proposed structural repair, ask for the exact operation, source unit,
  destination, and the role each resulting paragraph should perform;
- for an Introduction limitation, ask which broad-reader claim it constrains and
  whether the author wants a concise early disclosure, leaving detailed treatment
  in its current location.

Skip a question when the author has already supplied its exact answer. Ordinary
meaning-preserving wording or category repairs remain Revise work and should not
be routed through Grill.

## Apply the paper standard

Before discussing the text, read the [coverage contract](../systems-paper-revise/references/coverage-contract.md), [writing core](../systems-paper-revise/references/writing-core.md), and [shared workflow contract](../systems-paper-revise/references/review-revise-contract.md). Read the [Chinese calibration](../systems-paper-revise/references/chinese-writing.md) for Chinese prose or translation, and [paper archetypes](../systems-paper-revise/references/paper-archetypes.md) when contribution framing matters.

When Review findings are supplied, accept only the precise items marked `author decision required` or otherwise genuinely dependent on author intent. Preserve their finding and section/paragraph/sentence/lexical unit IDs, original anchors, evidence state, repair boundary, and resolution test. Do not rerun the full paper audit or ask the author to reconfirm passed units. When discussion starts without Review, assign stable local issue and unit anchors for the supplied scope.

Ground questions in the relevant quotations and sentence or paragraph pair. Resolve what the author means, how the inference follows, what evidence supports it, and—when structure is at issue—which exact operation and destination are authorized. Distinguish a defect from an uncertain intention or optional wording. Ordinary grammar corrections do not require an interview. Author confirmation settles only the named intended meaning and allowed edits, not the truth of an unsupported experiment or guarantee. A pending issue never becomes revision authority.

For a multi-outcome insight, preserve Review's source-grounded fan-out map. Keep
`reviewer-hypothesized` edges pending until the author supplies or selects the
missing relation, then record the common move, every named outcome, its causal
layer, evidence state, counterfactual, and permitted manuscript location. An
answer that only repeats the outcome or system name does not settle the edge.

Challenge a term that conflicts with an already agreed definition; ask whether the meaning changed rather than silently choosing a synonym. When a distinction is unclear, test it with a concrete hypothetical boundary case. Save the resolved definition and any misleading terms to avoid alongside the relevant decision. A hypothetical case tests the argument; it is not a new implementation fact or measured result.

## Record as you go

Read and follow the [decision-record rules](references/decision-record.md). Save intermediate answers and open questions as pending; update them in place when confirmed or rejected. Preserve existing unrelated decisions. Manage the record yourself rather than asking the author to fill in a form.

Write only the authorized paper decision record; keep the manuscript and other files unchanged. If no record location is authorized, continue in chat and ask where to save it. Briefly finish with what was agreed, what remains open, the source finding/unit IDs, and the saved record location. Revise can then use the original manuscript and confirmed record when the author requests revision; Grill itself does not rewrite the paper or claim a finding closed.
