# Direct Composition and Revision Protocol

Use this protocol for the usual writer-first path.
Composition and revision use one evidence/output contract.
Their different source states select different starting actions.

## 1. Record scope and authority

Before edits, inventory the full scope through the [shared coverage contract](coverage-contract.md).
Keep incoming unit and finding IDs.
Record the last unit at each applicable level.
Keep the scope unchanged.

Scope permission and coverage are independent.
Paragraph-local limits can prevent a structural repair.
The full permitted section continues to have an inspection requirement.
Record these items internally:

```text
Editable text or file objects:
Explicit exclusions and unavailable context:
Compose or revise:
Requested unit and reader obligation:
Source and output language:
Author's intended claim or outcome:
Intellectual-move dependencies and their source status, when applicable:
Original paragraph boundaries and roles:
Explicit permission for restructuring, if any:
Authoritative evidence:
Protected technical content:
Missing evidence, context, source, or author choice:
Incoming finding action classes and prerequisite graph:
Decision record identity and all literal version IDs:
Effective, applicable, and executable decision heads:
Decision exclusions, broken links, or conflicts:
```

Use these scope limits:

| Input | Authorized action |
|---|---|
| Pasted prose | Revise only that prose. Give it in chat. |
| Notes/evidence and a requested passage | Compose only that passage from supplied material. |
| Named paragraph, section, file, or file set | Revise in each initial paragraph. Keep paragraph count, order, and content ownership. |
| Named `main.tex` | Included files, bibliography, figures, and build configuration stay unavailable unless independently named. |
| Clear full LaTeX project | Record the manuscript dependencies necessary for the paper. Unrelated repository files are not in scope. |
| PDF without editable source | Give proposed prose or blockers. Keep the PDF unchanged. |

If an antecedent, definition, citation, figure, experiment, or fact is not in scope, give the specified missing context.
Before judgment, resolve the paper decision record.
A named paper project without a record has zero versions.
For pasted or ambiguously owned text, get a shown record path or clear no-history confirmation.
Read and classify all ledger rows.
Do not use only the newest-looking entry.

Resolve wording only when the supplied text fixes meaning without ambiguity.
For a claim-changing qualification, get an author decision.
Access does not give permission.

Use this evidence priority:

1. A clear author correction or decision
2. In-scope manuscript or artifact evidence
3. A permitted verified primary source
4. A clearly identified inference from shown premises.

Reviewer feedback shows the existence of an objection.
It does not show the truth of the reviewer's factual suggestion.
Treat review and venue-audit output as editorial metadata unless independent permitted evidence shows the proposition.
Keep severity labels, evidence-state labels, venue taxonomy, pillar maps, reviewer hypotheses, and repair directions out of manuscript prose.
An upstream review alone does not supply those items as scientific content.

A missing, blocked, unsupported, or unresolved claim must not become a positive fit, novelty, causality, or compliance statement.
Keep shown, inferred, planned, and blocked propositions as different categories.
Fluent words do not turn plans, hypotheses, placeholders, or plausible mechanisms into completed work.

### Paragraph-local contract for existing prose

The initial paragraph is the editing unit, including for a supplied section or full paper.
Use [writing-core.md](writing-core.md) to interpret paragraph and sentence boundaries.
Source-file line wraps do not give those boundaries.
Obey these rules unless a clear author instruction changes the identified paragraph boundaries:

- Keep paragraph number, order, and boundaries.
- Keep each paragraph's topic, role, scientific propositions, evidence, and limitations in it.
- Keep headings and document environments.
- Use other supplied paragraphs only for meaning and handoff checks.
  Their facts, results, citations, or explanations are not permitted additions to the paragraph being edited.
- Use a clear author correction directed at that paragraph when supplied.
- Change only identified defects in the paragraph.
- Make unclear wording clear.
- Write an unambiguous referent only when the source text supplies it.
- Remove redundancy shown in the text.
- Reorder, split, or combine sentences only to fix a defect in that paragraph.
- Keep a sentence unchanged when the scoped audit finds no defect that requires its change.
  If repetition spans a sufficient and a defective formulation, repair or remove only the defective formulation.
  Keep each distinct condition and proposition.
- Use a connective only for a relation that this paragraph directly supports.
  A connective cannot supply a scientific premise, result, explanation, purpose, benefit, or claim.
- Keep initial heading levels, lists, emphasis, LaTeX commands, inline equations, citation placement, and usual-prose format.
- For a clear format-change request, use a role-appropriate form grounded in systems-paper practice.
  Its presence in an OSDI/SOSP paper alone gives no permission.
- Cite sources for venue-policy claims.
  Do not put editorial source justifications in revised manuscript prose.

A request for high-level, concise, logical, or OSDI-quality prose does not give permission for paragraph restructuring.
A reviewer's split, combination, or experiment suggestion also gives no such permission.
For broader changes, get a clear author request.
An explicit request to split, combine, or reorganize identified paragraphs supplies structural permission for that scope.
For requested repair of overload or fragmentation, choose boundaries by distinct reasoning obligations.
Do not stop at sentence compression when the requested repair needs paragraph boundaries.
Keep all supplied propositions, evidence status, and limitations within the authorized targets.
This permission does not authorize new scientific content, neighboring-scope movement, or a change of purpose.

A question or placement hypothesis such as `should this be a Challenge paragraph?` stays an unresolved decision.
It does not give restructuring permission.
Before text splitting, combination, movement, or repurposing, get a clear instruction or confirmation.
It must give the operation and target paragraph/section.
Discussion of a destination does not give permission for the move.

If premise, evidence, claim-strength, or purpose input for a repair is missing, keep the affected passage unchanged.
Give the specified gap apart from the manuscript.
Do not delete or narrow the claim without an author decision.
Complete other permitted meaning-preserving edits.
Fluent words alone do not repair an unsupported sentence.
Clear author corrections stay permitted repairs.
For an identified precision or abstraction defect, check the author's requested rewrite and supplied facts at that anchor.
If they fix the intended technical account, treat that scoped substitution as an author correction.
Use its supported relations, conditions, and limitations without another confirmation.
Keep independently specified results, guarantees, comparisons, and scientific questions subject to their evidence and withdrawal requirements.

Composition and restructuring requests apply only to their named scope.
Keep meaning unchanged for those requests too.
Do not invent research content.

## 2. Route the writing mode

### Compose from evidence or notes

If the requested prose does not exist or the user requests composition, use this mode.

1. Find the section or paragraph contract in [writing-core.md](writing-core.md).
2. If contribution type controls it, use [paper-archetypes.md](paper-archetypes.md).
3. Select the strongest supported answer, necessary premises, credibility-changing evidence, and important boundary.
4. Make the shortest dependency outline that completes the reader obligation.
5. For shared-move outcomes, use only source-supported or clearly author-supplied evidence-compatible edges from the writing core's fan-out map.
6. Select evidence by function.
7. Write one manuscript-ready version.

Only `stated` and `text-licensed` source edges qualify without new author input.
You can change the order of notes.
You can omit information that does not help the requested argument.

If notes contain artifact inspection or promise Observation/Insight, apply [positioning-and-insight.md](positioning-and-insight.md).
Give the capability that the evidence shows.
Reject a conjunctive gap without support.
Keep the intellectual-move unit pending if no evidence-bearing relation exists.
Add an inference bridge only when shown premises supply it.
If they do not, narrow a newly drafted claim to its evidence or give the missing item.

Composition is locally complete when its unit completes the section role and each important claim has support.
Omitted notes must not change the decision case.

### Revise existing prose

If manuscript prose exists and the user does not request composition, use this mode.

1. Do the full-scope audit in the shared top-down order.
2. Start with the highest assessable paper/archetype and section obligations.
3. Record each observable promised role.
4. Independently find each paragraph's delivered role and content.

For each paragraph, record these fields:

- Conventional role and topic
- Claim or question and one-obligation result
- Expected/actual opening, development, and payoff
- Ending information gain
- Support, boundary, and deliberate voice.

For shared-move outcomes, keep each fan-out edge's source status.
Put `reviewer-hypothesized` bridges in author clarification or author evidence.
Record mixed, unclear, or promise-versus-delivery mismatch without selecting a new purpose for the author.

5. Examine each sentence and lexical occurrence.
6. Examine all adjacent sentence, paragraph, and section links and clear longer dependencies.
7. Keep wording defects, optional improvements, scientific gaps, and higher-level structural failures as different categories.

A clear topic change is not a defect.

8. Divide compound findings into the shared action classes.
9. Make the permitted meaning-preserving repair queue.
10. Apply each permitted meaning-preserving paragraph-local repair before the author-input pause.
11. Record the change and any unmet part of the initial resolution test.
12. Keep sufficient sentences and paragraph-level content ownership.
13. Run the full hierarchy again over changed and unchanged units.
14. Reconcile lexical choices up through the paper argument.
15. Do each received finding's test at its initial endpoints.
16. Give each dependency that paragraph-local limits prevent you from repairing.

The permitted meaning-preserving queue includes wording, category, reference, redundancy, and information-order repairs.
Keep author clarification, author evidence, external prerequisites, and optional/not-applied items in their separate classes.
Accept an unchanged result only when no identified defect has a meaning-preserving local repair.
Keep optional improvements out of the primary revision.

#### Independent category repair

`property P is necessary, but it cannot replace an argument/proof for properties Q and R` can contain independent defects.
If Q and R are named system obligations, compare P with those object-level properties.
Keep `P is necessary` at its initial strength.
Keep the missing necessity evidence unresolved or blocked with the terminal-blocker rule.
Keep each independently required Q and R obligation. Check whether coordination suggests that satisfying one removes the other; category correction must not erase either duty or assert that it has been fulfilled.

This category repair asserts neither Q nor R.
It does not select a new thesis.
Do not put it in Grill merely because necessity proof is absent.
Do not return the full sentence unchanged when the independent category repair keeps meaning and has permission.

#### Artifact-backed comparison and observation repair

For an artifact-backed prior-work paragraph followed by promised Observation/Insight, apply [positioning-and-insight.md](positioning-and-insight.md) before either revision.
Use these checks:

- Convert repository, build, link, or configuration facts to actor/object/stage/control capability only when the inference is shown.
- Keep deployment qualifications.
- Keep raw provenance outside the argument's center unless the specified realization matters.
- Divide `A, B, and C have not appeared together` into population coverage, parallel cells, negative evidence, and shared causal bridge.
- Do not use a hedge as closure of those requirements.
- If bridge choice changes the claim, get the author's descriptive-map, distinct-question, or negative-gap decision.
- Find the next paragraph's delivered role.
- Do not convert a definition, requirement, objective, or mechanism list into an insight through word changes.
- Apply permitted meaning-preserving local repairs first.
- Request the specified pattern/model fact, supported relation beyond definition, predicted design consequence, and intended role.

After those inputs, rebuild around the controlling update in the permitted paragraph.
Paragraph renaming or repurposing stays a structural choice even when it improves fluency.

#### Keep result-dependent content without withdrawal permission

A completed-paper placeholder can share a sentence with scientific content that its missing experiment must answer.
That content can include a comparison question, workload condition, remaining-cost boundary, or claim.
Without a permitted result, deletion of the sentence or those propositions does not close the finding.
It removes the scientific obligation.

An instruction to assume experiments exist or derive their answer gives neither a result nor withdrawal permission.
Keep the affected passage.
Use `author evidence` for the finding.
Request metric, baseline, conditions, result, and uncertainty.
Use terminal `blocked` only with the rule below.

Remove a semantically empty TODO independently only with deletion permission.
It must contain no scientific proposition.

#### Clarification loop

If requested findings include author-input classes, do this loop after direct repairs:

1. Make their dependency tree.
2. Give each prerequisite-ready question in one Grill-style round.
3. Include each initial finding/unit anchor.
4. Include a recommended answer or course and its basis.
5. Give the specified decision or evidence tuple necessary.
6. Set these items to `pending clarification`.
7. Wait for answers.
8. Save each substantive answer with the decision-record rules.
9. Read the saved answer back.
10. Continue this same revision only after that gate.
11. Recalculate the ready queue after each round.

Keep dependent questions waiting until their prerequisites close.
Do not make the disputed edit or give a terminal closure table during a pending answer.
A clear one-shot, no-discussion, or prose-only instruction excludes this loop.
Keep affected propositions and use its output contract.
Do not call the unresolved finding resolved.

An item becomes terminal `blocked` only for an unavailable external prerequisite or clear author input that ends the request.
The author can decline the request.
They can give an answer that the input is unavailable or that they cannot supply it.

Revision is locally complete only with these conditions:

- Requested paragraph-local repairs are closed.
- Each received finding has a terminal closure state.
- No item stays `pending clarification`.
- The full scope has `Unreviewed: 0`.
- No semantic, structural, or rhetorical regression exists.

A separate cross-paragraph or evidence gap stays a blocker only with the terminal rule.
It is not a repaired argument.

## 3. Resolve structural uncertainty before prose

Use [revision-strategies.md](revision-strategies.md) for competing theses, mismatched contribution contracts, missing design/evidence dependencies, or interacting findings.
Apply its structural operations only for clear restructuring requests.
For other requests, give the required choice and stay paragraph-local.

If alternatives imply different meanings, hierarchies, assumptions, audiences, or trade-offs, keep the initial passage.
Use the [shared clarification contract](review-revise-contract.md) to get the author decision.
Keep unanswered questions and placement suggestions `pending clarification`.

For a structural edit, get clear permission for the named operation and destination.
For an active revision request, give that question at this time.
Continue the same revision after the answer.
Do not immediately give it terminal `blocked`.

Keep scientific choices and meaning-equivalent optional wording as different categories.
Apply neither without an author decision.

## 4. Write at the right level

Use [writing-core.md](writing-core.md) as the single standard for argument, explanation, paragraphs, sentences, wording, section contracts, and concision.
Use [chinese-writing.md](chinese-writing.md) for Chinese source/output or Chinese translation.

Before file or protected-content edits, record the snapshot in [change-safety.md](change-safety.md).
Do its preservation checks after edits.
Edit figures, tables, code, data, or scripts only when the user clearly includes them.
After an experimental-output correction, keep dependent claims unverified until regenerated evidence passes its checks.

## 5. Run the full-scope gate

Read the full scope again against Review's same standard.
Do the [coverage gate and receipt](coverage-contract.md#completion-gate-and-receipt).
For composition, do a check of unit role, supplied evidence, and output requirements through the composition branch.
Initial-paragraph preservation applies only to existing prose.

For revision, do these checks:

1. Make sure that initial paragraph boundaries, count, order, role, and content ownership stay, except for clear author changes.
   For requested restructuring, verify that the resulting boundaries separate or connect the identified reasoning obligations.
2. Make sure that each direct edit fixes an identified defect.
3. Make sure that preferred style alone did not trigger an edit or force scientific completion.
4. Make sure that abstractions keep initial propositions without new purpose, cause, benefit, condition, or evidence.
5. Make sure that each paragraph keeps its role and emphasis.
6. Make sure that no template-only background, explanation, summary, or transition sentence was added.
7. Make sure that sentence/paragraph links have correct relations, clear scope, clear referents, and stable terms.
8. Give the specified endpoints of unresolved links.
9. Make sure that sufficient sentences stay and redundancy removal keeps meaning.
10. Make sure that added length resolves a specified ambiguity rather than expands the argument.
11. Make sure that facts, numbers, units, citations, equations, identifiers, macros, and evidence status stay correct.
12. Make sure that review labels, venue-audit language, and new unresolved propositions stay apart from manuscript prose.
13. Keep initial unsupported claims unchanged and flagged unless a clear author correction or withdrawal exists.
14. If such permission exists, do a check of that specified change.
15. Make sure that each changed sentence addresses the requested repair.
16. Make sure that no paragraph adds an unsupported proposition or changes text type.
17. Make sure that each in-scope section, paragraph, sentence, link, and lexical occurrence has a coverage state.
18. Include unchanged passed units and the last unit at each level.
19. At completion, give each received finding a terminal closure state and make sure that `unreviewed = 0`.
20. Make sure that each permitted meaning-preserving local repair is applied or clearly `optional/not applied`.
21. Make sure that evidence or structure blockers did not suppress independent meaning-preserving corrections.
22. Make sure that new or stronger intellectual-move dependencies have source evidence or evidence-compatible author inputs.
23. Keep `reviewer-hypothesized` bridges out of manuscript prose.
24. Make sure that independent outcomes did not become a false shared insight.
25. Do the artifact-to-capability check for each artifact-backed positioning sentence.
26. Do conjunctive-gap evidence and causal checks, or keep the gap pending.
27. Make sure that each promised Observation/Insight gives an intellectual update beyond a definition or repeated requirement.
28. Make sure that no requested `author clarification` or `author evidence` item stays pending.
29. If an item is pending, keep the state as an interactive pause without a completion gate.
30. Make sure that each literal decision version has a classification.
31. Make sure that only executable heads constrained edits.
32. Give stale, rejected, superseded, out-of-scope, evidence-conflicting, and structure-conflicting versions in the decision receipt.

Compile, render, lint, or do tests only with clear dependency scope and action permission.
Give only the check that each tool did.
A clean tool result does not show publication readiness.

For clear iteration or interacting edits with a fixed-point requirement, use [convergence-loop.md](convergence-loop.md).
Do not repeat arbitrary paraphrases.
A loop can batch work.
It cannot reduce required coverage to changed paragraphs.

## 6. Return the deliverable first

For pasted material, start with conservative revised prose in its initial layout and markup.
An unchanged passage can be the correct result.
For file edits, apply only permitted corrections.
Give the edited objects.
Keep role labels, diagnostics, and optional alternatives apart from the manuscript and source files.

After the manuscript, give only applicable items.

### Pending clarification

After permitted meaning-preserving edits, show the full requested finding queue with action classes.
Give the full ready question queue in Grill format.
Wait for answers.
This output replaces the terminal finding-closure map and manuscript coverage receipt for that turn.
Show decision accounting at this point without a completion claim.
Keep scope and IDs for continuation of the same revision.

### Finding closure

Give each received Review/Grill ID a state: `closed`, `blocked`, `not applied`, or `reopened`.
Include initial unit IDs and a one-line initial-test result.
Separate the repaired local defect from retained scientific limits. Name any relevant uncertain outcome or unestablished scope; their presence in the revised prose does not itself explain the closure boundary.
Omit only if there are no incoming findings or the user clearly requests prose only.

### Manuscript coverage receipt

Give full-scope totals, last-unit states, not-assessable reasons, closure counts, and `Unreviewed`.
Omit only for clear prose-only requests.
The internal gate applies.

### Decision coverage receipt

Give permitted record identity, all literal IDs/status counts, effective/applicable/executable IDs, exclusions/reasons, conflicts, and `Unaccounted decisions`.
This receipt is mandatory during interactive pauses and after prose-only output too.

### Unresolved scientific issue

Give the initial sentence or paragraph pair and the shortest identifying quotation.
Give the missing premise or evidence.
For an isolated claim, use its own anchor.
Do not invent a pair.
Keep its initial assertion unchanged in the manuscript pending author decision.
This preservation requirement is an internal edit constraint, not an extra sentence for the scientific note.
The returned claim is not verification.

### 可选写法 / Optional wording

Give alternatives only for clear concision, precision, or information-order gains beyond required corrections.
Include initial anchor, one meaning-equivalent alternative, and one short reason.
Do not give usual synonym choices or a second full draft.
A paragraph split, heading, or list conversion without a direct author request is an optional format suggestion.
Apply it only with clear permission.

Give an important permitted change or related validation result when it helps the author judge the edit.

### Prose-only output

First check the author's explicit output exclusions.
For manuscript-body-only output or excluded receipts, keep decision accounting internal and omit the receipt.
For excluded scientific notes, keep the gap accounting internal without claiming the issue resolved.
For prose-only requests, omit closure maps, manuscript coverage records, alternatives, general advice, and process commentary.
When workflow metadata is permitted, append only the compact decision coverage receipt from the decision-record rules.
If a scientific issue remains unresolved and notes are permitted, put its minimal note before the receipt after the prose.
Give specified location and missing basis, without a replacement argument or separate report.
For an inference, locate both the initial supporting sentence and its conclusion.
One anchor suffices only for an isolated claim.
Explain the difference between the supplied support and the claim's metric, population, conditions, strength, or causal relation.
A list of unavailable inputs alone does not explain that difference.
Keep this note about the scientific basis, without skill quotations or workflow explanations.
Its content is limited to the source anchors, support mismatch, and missing basis.
End the note with the missing basis, then give the decision receipt without another pending-edit status sentence.
If there is no such issue, give only the prose and permitted receipt, including for unchanged prose.
Before returning, verify each permitted required output and each explicit exclusion.
This exception waives neither internal audit nor the restriction against unsupported completion claims.
