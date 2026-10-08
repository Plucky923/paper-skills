---
name: systems-paper-revise
description: "Revise computer-systems paper prose in each initial paragraph. Keep its purpose, technical meaning, and manuscript format. Improve precision and logical flow. Draft from author-supplied material only when the user requests composition."
---

# Systems Paper Revise

Correct specified problems in supplied prose.
Keep the author's text when it is sufficient for the request.
Use the OSDI writing standard to examine each paragraph's existing role.
That standard does not give permission to complete or expand its argument automatically.

## Contract

- Work only on the passage, files, or source material that the user names.
- If context is unavailable, record that limit.
  Do not read neighboring material without permission.
- Keep facts, technical meaning, conditions, numbers, citations, equations, identifiers, macros, terms, evidence status, and author intent.
- Do not give plans, hypotheses, or plausible mechanisms the status of completed work.
- Use the manuscript language unless the user requests translation.
- Keep deliberate voice and repeat technical terms without name changes.
- For pasted material, give prose in chat.
- Edit clearly named editable files directly.
- Treat a PDF as read-only unless editable source is also in scope.
- Give the decision coverage receipt with each result.
  For a prose-only request, keep that receipt to one line after the prose.
  A named project without a record still needs the zero-history receipt.
  If the author explicitly requires manuscript body only or excludes receipts, keep decision accounting internal and honor that restriction.
- If an unresolved scientific issue remains, report its anchor and missing basis separately after the prose.
  This note keeps an unchanged claim from appearing verified, including in prose-only output.
  Omit optional commentary, but retain this note and the decision receipt.
  An explicit author exclusion of non-manuscript output takes precedence; retain the scientific-gap accounting internally.
- For existing prose, keep paragraph count, order, boundaries, and content ownership by default.
  A clear request to split, combine, or reorganize named paragraphs authorizes the necessary boundary changes in that scope.
  Use paragraph-local edits for a full paper too.
  Obey [revision-protocol.md](references/revision-protocol.md).
  A diagnosis or review suggestion does not replace that contract.
- Make each direct edit fix a specified grammar, reference, precision, redundancy, or supported local-logic defect.
  Keep sufficient sentences, emphasis, and rhythm.
  Another academic expression alone does not prove a defect.
- Give one conservative revision.
  Put optional wording with a clear benefit after the manuscript with heading `可选写法` or `Optional wording`.
  Give the initial anchor, one alternative, and one short reason.
  Obey the output rules in [revision-protocol.md](references/revision-protocol.md).
- If necessary evidence, premise, or strength input for a claim repair is missing, keep the affected passage unchanged.
  Give the gap independently.
  Complete other permitted meaning-preserving edits.
  An unchanged unsupported claim stays a flagged issue.
- Treat each `reviewer-hypothesized` node or edge as a blocked manuscript dependency.
  Write it only with scoped source evidence or an evidence-compatible author decision.
  Reviewer synthesis is not source material.
- Divide mixed findings into independent action classes.
  Complete each authorized direct repair of an identified defect before author-input questions.
  Keep evidence-, intent-, or structure-dependent items in their applicable queues.
  Keep sufficient wording unchanged.
  Route style or concision gains beyond required corrections to `optional/not applied`.
  An unchanged passage is successful when no authorized direct repair remains.
- Apply the [shared coverage contract](references/coverage-contract.md) before and after edits.
  Audit the full frozen scope from the highest assessable level through lexical occurrences.
  Keep Review unit and finding IDs.
  At completion, give each received finding a terminal closure state.
  During an interactive pause, keep `pending clarification` for items awaiting author answers.
  Paragraph-local limits control edits, not required audit coverage.

## Load the writing rules

Always read these references:

- The [shared coverage contract](references/coverage-contract.md)
- [writing-core.md](references/writing-core.md)
- The [shared review and revision contract](references/review-revise-contract.md)
- [revision-protocol.md](references/revision-protocol.md).

For existing prose, also read the detailed [sentence and lexical rules](../systems-paper-review/references/prose-and-terminology.md).
For multi-sentence prose, read the detailed [section and paragraph rules](../systems-paper-review/references/structure-and-sections.md).
The two reference loads are mandatory at their applicable levels in the coverage contract.
Apply the same quality standard as Review.
Before a disputed repair, use the shared contract to discuss uncertain logic through Grill.

Load the conditional references applicable to the request:

| Condition | Reference |
|---|---|
| Contribution type affects the argument | [paper-archetypes.md](references/paper-archetypes.md) |
| Chinese prose or Chinese-to-English translation | [chinese-writing.md](references/chinese-writing.md) |
| Structural, evaluation, visual, venue, or multi-finding repair | [revision-strategies.md](references/revision-strategies.md) |
| Interface, virtualization, semantic freedom, customization, protection/authority, compound isolation, or direct/delegated path claim | [interface-boundaries.md](references/interface-boundaries.md) |
| Artifact-backed prior-work comparison, conjunctive gap, or Observation/Insight/Requirement/Design objective prose | [positioning-and-insight.md](references/positioning-and-insight.md) |
| File edit or technical values, citations, equations, notation, identifiers, macros, figures, tables, or other protected content | [change-safety.md](references/change-safety.md) |
| Clear iteration/fixed-point request, or interacting edits with unresolved preservation risks after one pass | [convergence-loop.md](references/convergence-loop.md) |
| A large permitted scope benefits from independent read-only checks during that loop | [multi-agent-revision.md](references/multi-agent-revision.md) |

Contribution-type cases include titles, abstracts, introductions, contribution framing, section/full-paper structure, and measurement, experience, formal, or hybrid work.
Use [systems-paper-review](../systems-paper-review/SKILL.md) for a clear review-before-revision request or a full-scope scientific/submission judgment.
Its findings are internal input to this writing task.
This skill's scope, edit permission, and manuscript-first output rules control revision.

## Route automatically

### Compose from evidence or notes

If the unit has no manuscript prose or the user requests composition, select this mode.
Find the section or paragraph obligation.
Select only evidence necessary for that obligation.
Write a full dependency chain.
Give missing support as a blocker.
Notes are inputs, not sentences that must all stay.

### Revise existing prose

If manuscript prose is available and the user does not request composition, select this mode.
Record each signaled or author-supplied role.
Independently find each initial paragraph's delivered role, claim, support, payoff information, and boundary.
Repair only that paragraph unless the author requests restructuring of the identified paragraphs.
Sentence order changes, splitting, or combination can occur in it.

Get clear author permission for paragraph-boundary changes, content movement, and purpose changes.
That permission must give the operation and target.
A direct request to reorganize identified overfull or fragmented paragraphs supplies that structural permission.
Apply the requested boundary repair by reasoning role; sentence compression alone does not complete it.
A question, diagnosis, or placement suggestion does not give that permission.

Select the mode from the supplied material.
If the choice changes scientific contribution or technical meaning, give the author that decision.

## Existing-prose workflow

1. Give scope, language, author intent, evidence, and protected technical content.
2. Keep that record unchanged.
3. Resolve the permitted paper decision record through the shared contract.
4. Read each decision version.
5. Derive all, effective, applicable, and executable sets before edit selection.
6. Keep supplied Review section, paragraph, sentence, lexical, and finding IDs.

A named paper project without a record has zero history.
For pasted or ambiguously owned prose, get a record path or the author's confirmation of no history.

7. Inventory the full scope.
8. Do the shared top-down pre-edit audit from the highest assessable level through each lexical occurrence.
9. Record unavailable higher context without scope expansion.
10. Make the baseline finding-to-unit map before prose changes.

The audit includes paper/archetype, each section, each paragraph's promised and delivered roles, one obligation, and payoff information.
It also includes each sentence and link.

11. Use received Review findings as the primary repair queue.
12. Give each item its shared action class.
13. Add that field to older Review output when missing.

The action classes are `direct repair`, `author clarification`, `author evidence`, `external blocker`, and `optional/not applied`.
A pending question does not give permission to infer a repair.
It is not a terminal blocker.

14. Select permitted meaning-preserving local repairs through [writing-core.md](references/writing-core.md).
15. Apply each independent meaning-preserving repair before the author-input pause.
16. For a high-level role mismatch, keep the source-grounded intellectual-move map.
17. Make an existing principle clear in the paragraph when source evidence gives it.
18. Put mechanism detail below that principle only in the same paragraph.
19. Keep `reviewer-hypothesized` move-to-outcome edges out of manuscript prose.

If author permission or substantive-detail movement is necessary for a high-level repair, leave that dependency unapplied.
Put it in the clarification queue below.
Do not invent the relation or delete the detail.
Complete the independent local repairs.

Use an equivalent abstraction only when it comes directly from the paragraph and addresses the requested repair.
If that condition does not hold, keep the initial wording or give optional wording.
Add no purpose, cause, benefit, mechanism, experiment, or result only to make prose look finished.

20. Run the same full-scope audit after edits.
21. Include each unchanged and passed unit.
22. Reconcile from lexical occurrences up through the hierarchy.
23. Do the content-ownership and protected-content checks.
24. Do each initial finding's resolution test at its initial endpoints.

A loop does not expand edit permission.

25. After permitted meaning-preserving repairs, give one Grill-style round for each prerequisite-ready author-clarification and author-evidence item.
26. Give numbered questions with recommendations and specified required inputs.
27. Set those items to `pending clarification`.
28. Wait for answers.
29. Save each substantive answer as a versioned full snapshot when the decision record is writable within scope.
30. Read the saved answer back, or retain a chat-only answer as current-request authority when persistence is excluded.
31. Continue the same revision.

During a pending question, do not give a terminal closure map or manuscript coverage receipt.
Give the separate decision coverage receipt during that pause.
After the queue has no pending item, apply the coverage contract's terminal closure states to each received finding.
Those states are `closed`, `blocked`, `not applied`, and `reopened`.

Use terminal `blocked` only for an external prerequisite or a clear author decline or unavailable-input answer.
For a link needing evidence or cross-paragraph restructuring, give the two endpoints and its action class.
Do not complete the argument without an author decision and its required evidence.

## Output

Start with manuscript text in its initial paragraph layout and markup, except for explicitly requested restructuring or format changes.
Keep headings, lists, emphasis, citations, and other syntax.
For file edits, give the names of edited objects.
Keep diagnostics and alternatives apart from the manuscript and source files.
Check explicit author output exclusions before applying the default report format.
When the author requires manuscript body only, keep ledgers, gaps, and decision accounting internal.
Do not claim that undisclosed gaps are resolved or unsupported claims verified.

If clarification is pending, show the permitted meaning-preserving edits, finding action queue, decision accounting, and Grill question round.
Then wait without a terminal closure map or manuscript coverage receipt.
After resolution, give the compact closure map, full-scope manuscript coverage receipt, and decision coverage receipt.
Account for unchanged units and each decision version.
Give optional wording only for a clear benefit.
Do not give usual synonym alternatives.

For a clear prose-only request, omit closure maps, manuscript coverage receipts, optional wording, and usual commentary.
When the author permits workflow metadata, append the one-line decision coverage receipt.
For an unresolved scientific issue, put a minimal note before that line if non-manuscript notes are permitted.
Identify its original anchor or inference endpoints and missing basis.
For a failed inference, identify both the supporting sentence and its conclusion.
Use one anchor only for an isolated claim without a supplied support relation.
Explain what the supplied evidence establishes and which claim dimension exceeds that support.
Give the missing basis without a replacement argument.
Keep skill quotations, policy explanations, and routine permission commentary out of this scientific note.
The note contains only the source anchors, support mismatch, and missing basis.
End it with the missing basis; preserve the manuscript without an additional sentence announcing its pending edit status.
Use [revision-protocol.md](references/revision-protocol.md) for the full output contract.
