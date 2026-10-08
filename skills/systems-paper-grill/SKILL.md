---
name: systems-paper-grill
description: Get author answers about systems-paper arguments. Use for paper questions and Review or Revise questions about meaning or evidence. Save decisions without manuscript edits.
---

# Systems Paper Grill

Get the author's confirmation that your description agrees with the author's meaning, logic, and evidence.
Continue until each in-scope branch has a terminal state permitted by the conditions below.
Keep all questions in the supplied passage or question.
When available, use Review findings as input.
Review findings are not necessary.

Use a **decision tree** to show the prerequisite decisions.
Each branch contains a decision and its dependent decisions.
Give questions in **rounds**.
Use the **frontier** for each round.
The frontier contains all decisions with completed prerequisites.

Give each frontier question in the same round.
Give each question a number.
Give your recommendation and its reason for each question.
Use the author's language.
Wait for the author's answers before the next round.

Use this round format:

```text
❓ Q1 — <question title>: <question grounded in the supplied passage>

➡️ <your recommended answer and its basis; identify missing evidence when necessary>

❓ Q2 — <question title>: <question whose prerequisites are already settled>

➡️ <your recommended answer and its basis>
```

After each round, find the next frontier from the author's answers.
Before the prerequisite decision is completed, do not give its dependent question.

Find facts in authorized sources.
Read the supplied sources.
Quote each supplied factual premise in the decision tree and record with its source-unit ID.
Keep proposed interpretations separate and pending.
Before each round, compare the questions and record against those quotations.
Check the actor, action, conditions, temporal order, and evidence status.
When agents can help with lookups without dependencies on your work, use available agents.
While a search continues, do not give questions with that search as a prerequisite.
Continue with the other frontier questions.

Get missing information from the author.
Before you examine other sources, get the author's permission.
Get each decision from the author.
Wait for the author's decision.
Do not use recommendations and hypothetical examples as system facts.

Before completion, get the author's confirmation of the same meaning, logic, and evidence.
Make sure that each in-scope branch has one of these states:

- The decision has the author's answer and confirmation.
- An external prerequisite is not available.
- The author rejects the request for necessary input.
- The author cannot supply the necessary input.
- The author gives confirmation that the necessary input is not available.

After Grill completion, keep scientific claims without evidence as issues with missing evidence.
Do not give the same question again to get evidence that is not available.
Without a decision-content change, do not get confirmation again for a decision with author confirmation.

## Continue an active revision

When Revise starts Grill for an active repair queue, use an **embedded clarification loop**.
Keep the initial revision request as edit authority for its initial scope only.
Give all frontier questions.
Wait for the author's answers.
After record checks show correct saved content, let Revise continue the same revision without a second request.
A second revise command from the author is not necessary.

For items with missing answers, keep the `pending clarification` state.
Do not give items with missing answers the `blocked` state.
Do not give Revise's terminal closure receipt.
The completion conditions above are necessary for a question's terminal state.
Without an active revision request, keep the manuscript the same.

## Feedback and authority

For each author statement, select all applicable types:

- Diagnosis or dissatisfaction
- Intended meaning or role
- Scientific evidence
- Edit authority.

These types can occur together.
One type does not supply a different type.
A question such as `should this be a Challenge paragraph?` is a placement hypothesis.
Keep that question pending until the author confirms the decision.
For a structural change, get permission for the operation and its target boundary.
The assumption of experiments does not supply their results.

Use the smallest frontier question that supplies the necessary repair input.

- For a related-work gap, get the same assumption, mechanism, or constraint that prevents the target property.
  For a scope comparison, get the author's decision about a descriptive difference or a negative gap.
- For one insight with multiple primary outcomes, first get the same changed constraint, assumption, or boundary.
  After this answer is completed, get the relation from that change to each outcome.
  For each relation, get the causal layer that supplies it.
  Get the failure condition if the move or layer is removed.
  Do not use the assistant's reconstruction as the author's answer.
- For an insight paragraph with mechanisms as its primary content, get the author's principle.
  For scientific detail, get permission for a move to a paragraph or section with an author-supplied name.
- For an evidence-derived conclusion, get the metric, baseline, conditions, observed result, and uncertainty important to the conclusion.
  The existence of an experiment does not supply this evidence.
- For a structural repair, get the operation, source unit, and destination from the author.
  Get the role of each paragraph after the change.
- For an Introduction limitation, get the broad-reader claim and the limitation's effect on its scope.
  Get the author's decision about a short disclosure before the detailed limitation text.
  Without permission for a move, keep the full limitation text at the same location.

When the author supplies the same answer, do not give that question again.
Let Revise do meaning-preserving wording and category repairs.

## Apply the paper standard

Before Grill, read the [coverage contract](../systems-paper-revise/references/coverage-contract.md).
Read the [writing core](../systems-paper-revise/references/writing-core.md).
Read the [shared workflow contract](../systems-paper-revise/references/review-revise-contract.md).
For Chinese prose or translation, read the [Chinese calibration](../systems-paper-revise/references/chinese-writing.md).
For contribution framing, read [paper archetypes](../systems-paper-revise/references/paper-archetypes.md).

For supplied Review findings, use items with the action class `author clarification` or `author evidence`.
For previous findings, use those for which author intent or author-supplied evidence is necessary.
Keep their finding IDs and section, paragraph, sentence, and lexical unit IDs.
Keep their source anchors, evidence states, repair boundaries, and resolution tests.
Do not do the full paper audit again.
Do not get confirmation again for units with `pass` status.

Without Review findings, give stable local issue IDs and unit anchors to the supplied scope.
For each question, use quotations from its source units or sentence or paragraph pairs.
Get the author's meaning.
Get the premises and relation for the inference.
Get the evidence for that inference.
For structural changes, get permission for the operation and destination given by the author.

For intent without author confirmation, do not give the defect classification.
Do not give optional wording the defect classification.
Let Revise do grammar corrections.
Author confirmation supplies only the given meaning and permitted edits.
Author confirmation does not supply evidence for an experiment or guarantee.
A pending issue gives no revision authority.

For a multi-outcome insight, keep Review's source-grounded fan-out map.
Keep `reviewer-hypothesized` edges pending until the author supplies or selects the missing relation.
After that answer, record the same move and each outcome given by the author.
Record each outcome's causal layer, evidence state, counterfactual, and permitted manuscript location.
An answer with only the outcome or system name does not complete the edge.

Use the definition with author confirmation as the reference.
When a term does not agree with that definition, get the author's decision about the changed meaning.
Before that decision is completed, keep the term with author confirmation.
When a distinction is not clear, do a test with a hypothetical boundary case.
Save the definition with author confirmation in the same decision.
Save terms with incorrect meanings in that decision as terms with no permitted use.

A hypothetical case is an argument test, not an implementation fact or measured result.

## Record as you go

Read the [decision-record rules](references/decision-record.md).
Obey these rules.
Before classification, read the full authorized history.
Save each state with changed decision content as a versioned full snapshot.

Keep the effective confirmed head while candidates are pending.
When the successor gets author confirmation, update the two supersession links in one write.
Keep unrelated and legacy decisions.
Write the record.
Do not give the author a form to complete.

Write only the authorized paper decision record.
Keep the manuscript and other files the same.
A paper project with a given name and no record has zero history.
For pasted text or unknown project ownership, get the record path from the author.
Keep state in chat while the path is unknown.

Before you complete a changed decision, save it at the authorized path.
Read the changed entries again.
Read their reciprocal links again.
Read unrelated records again.
Make sure that the saved record keeps all necessary content.

At standalone Grill completion, give a short report of completed decisions and unresolved items.
Give each unresolved item its permitted terminal state.
Include the source finding and unit IDs.
Include the saved record location.

In an embedded loop, let Revise continue only after these record checks show correct saved content.
Revise uses executable decisions with evidence that agrees with the authorized sources.
Revise gives each finding its closure state.
Do not use Grill for manuscript edits or finding closure.
