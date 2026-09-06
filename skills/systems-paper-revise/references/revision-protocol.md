# Direct Composition and Revision Protocol

Use this protocol for the ordinary writer-first path. It shares one evidence and output contract while routing composition and revision through different starting states.

## 1. Freeze scope and authority

Use the [shared coverage contract](coverage-contract.md) to inventory the complete
frozen scope, preserve incoming unit/finding IDs, and record the last unit at every
applicable level before editing. Scope authority and coverage are independent:
paragraph-local authority can prohibit a structural repair while the whole
authorized section still requires inspection.

Record internally:

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

Interpret scope narrowly:

| Input | Authorized action |
|---|---|
| Pasted prose | Revise only that prose and return it in chat. |
| Notes or evidence plus a requested passage | Compose only that passage from the supplied material. |
| Named paragraph, section, file, or file set | Revise within each original paragraph of those objects; preserve paragraph count, order, and content ownership. |
| Named `main.tex` | Treat included files, bibliography, figures, and build configuration as unavailable unless separately named. |
| Explicit whole LaTeX project | Freeze the manuscript dependency set needed for that paper; unrelated repository files remain outside scope. |
| PDF without editable source | Return proposed prose or blockers; the PDF itself remains unchanged. |

When an antecedent, definition, citation, figure, experiment, or fact lies outside
scope, name the exact missing context. Resolve the paper decision record before
judging prose: a named paper project with no record has zero versions; pasted or
ambiguously owned text requires an established record path or explicit
no-history confirmation. Read and classify the entire ledger rather than only
the newest-looking entry. Resolve wording only when the supplied text makes the
intended meaning unambiguous; a qualification that changes the claim needs an
author decision. Accessibility is not authorization.

Rank evidence as follows: an explicit author correction or decision; in-scope manuscript or artifact evidence; a permitted and verified primary source; a clearly marked inference from established premises. Reviewer feedback establishes that an objection exists, not that its factual suggestion is correct.

Treat review and venue-audit output as editorial metadata unless authorized evidence independently establishes the proposition. Do not import severity labels, evidence-state labels, venue taxonomy, pillar mappings, reviewer hypotheses, or repair directions into manuscript prose merely because they appear in an upstream review. A claim marked missing, blocked, unsupported, or unresolved must not reappear as a positive fit, novelty, causality, or compliance statement during revision.

Keep established, inferred, planned, and blocked propositions distinct. Fluency does not promote a plan, hypothesis, placeholder, or plausible mechanism into completed work.

### Paragraph-local contract for existing prose

The original paragraph is the editing unit, even when the user supplies an entire section or paper. Interpret paragraph and sentence boundaries using the shared [writing core](writing-core.md), not source-file line wrapping.

- Preserve the number, order, and boundaries of paragraphs, and keep each paragraph's topic, role, scientific propositions, evidence, and limitations in that paragraph. Preserve headings and document environments.
- Use other supplied paragraphs only to resolve meaning and check handoffs. Their facts, results, citations, or explanations are not authorized additions to the paragraph being edited. An explicit author correction directed at that paragraph is permitted.
- Inside the paragraph, change only identified defects. Clarify wording, remove actual redundancy, repair unambiguous referents, and reorder or split/merge sentences only when that fixes the defect. Preserve sound sentences even if a different phrasing is possible. A connective may express a relation directly supported by this paragraph; it cannot supply a scientific premise, result, explanation, purpose, benefit, or claim.
- Default to the original format, including heading levels, lists, emphasis, LaTeX commands, inline equations, and citation placement. Ordinary prose remains ordinary prose. An explicit format-adjustment request permits a role-appropriate form grounded in systems-paper practice; the existence of that form in an OSDI/SOSP paper alone grants no permission. Cite sources when making a venue-policy claim, not inside the revised manuscript as editorial justification.
- A request for high-level, concise, logical, or OSDI-quality prose does not authorize paragraph restructuring. Neither does a reviewer recommending a split, merge, or missing experiment. Broader changes require the author to ask explicitly for them.
- A question, diagnosis, classification, or placement hypothesis such as `should this be a Challenge paragraph?` is an unresolved decision, not restructuring authority. Before splitting, merging, moving, or repurposing text, require an explicit instruction or confirmation naming the operation and target paragraph/section. Permission to discuss or recommend a destination is not permission to perform the move.
- When a repair needs a missing scientific premise, new evidence, changed claim strength, or a different paragraph purpose, keep the affected passage unchanged and identify the exact gap outside the manuscript. Do not silently delete or narrow its claim. Complete other safe edits; making an unsupported sentence fluent is not a repair. Explicit author corrections remain actionable.

Explicit composition or restructuring requests follow their named scope; they do not relax meaning preservation or authorize new research content.

## 2. Route the writing mode

### Compose from evidence or notes

Use this branch when the requested prose does not yet exist.

1. Identify the section or paragraph contract in [writing-core.md](writing-core.md). When contribution type controls the contract, route through [paper-archetypes.md](paper-archetypes.md).
2. Extract the strongest supported answer, the premises required to understand it, the evidence that changes its credibility, and its material boundary.
3. Build the shortest dependency outline that completes the reader obligation. For one move with several claimed outcomes, include only `stated`, `text-licensed`, or explicitly author-supplied and evidence-compatible edges from the writing core's fan-out map. Select evidence by function; do not preserve note order or include every true detail.
4. Draft one manuscript-ready version. Add an inferential bridge only when it follows from established premises; otherwise narrow the claim or expose the missing item.

Composition is complete when the requested unit performs its section role, each material claim has support, and omitted notes do not change the decision case.

### Revise existing prose

Use this branch when prose already exists.

1. Audit the complete frozen scope in the shared top-down order. Start with the highest assessable paper/archetype and section obligations, then record every observable promised role and independently identify what each paragraph actually delivers: its conventional role, topic, claim or question, one-obligation result, expected and actual opening/development/payoff, ending information gain, support, boundary, and deliberate voice. When one move is meant to yield several outcomes, preserve the source status of every fan-out edge and route reviewer-hypothesized bridges to author clarification or author evidence. Mark a mixed, unclear, or promise-versus-delivery mismatch without choosing a new one for the author.
2. Inspect every sentence and lexical occurrence, all adjacent sentence/paragraph/section links, and explicit longer dependencies. Distinguish concrete wording defects, optional improvements, scientific gaps, and higher-level structural failures. A coherent topic change is not a defect.
3. Decompose compound findings into the shared action classes and build the safe repair frontier: locally repairable wording, category alignment, reference, redundancy, or information order versus author clarification, author evidence, external prerequisites, and optional/not-applied items. Apply every safe subrepair inside that paragraph before pausing for the author-answerable frontier; record what changed and what still fails the original resolution test. Keep adequate sentences and paragraph-level content ownership. An unchanged result is valid only when no identified defect has a meaning-preserving local repair. If only an optional improvement is available, leave it out of the main revision.
4. Re-run the full hierarchy over changed and unchanged units. Reconcile lexical choices upward through the paper-level argument, test every incoming finding at its original endpoints, and report any dependency that the paragraph-local contract prevents repairing.

A common non-atomic case is `property P is necessary, but it cannot replace an
argument/proof for properties Q and R`. When Q and R are already the sentence's
or paragraph's named system obligations, align the comparison at the object
level while preserving `P is necessary` at exactly its original strength. Keep
the missing support for P's necessity blocked. This category repair neither
asserts Q/R nor selects a new thesis, so do not route it to Grill or return the
whole sentence unchanged merely because the necessity proof is absent.

The inverse case is not a safe frontier: a completed-paper placeholder may share
a sentence with the comparison question, workload condition, residual-cost
boundary, or claim that the absent experiment must answer. Without an authorized
result, deleting that sentence or those propositions does not close the finding;
it erases the scientific obligation. An instruction to assume experiments exist
or derive the answer supplies neither a result nor withdrawal authority. Preserve
the affected passage, classify the finding as `author evidence`, and request its
metric, baseline, conditions, result, and uncertainty. It becomes terminally
blocked only under the rule below. Only a semantically empty TODO can be removed
independently, and only when its removal is authorized.

5. If any requested finding is `author clarification` or `author evidence`, build
its dependency tree and automatically ask every prerequisite-ready question in
one Grill-style round after applying the direct repairs. Each question includes
the original finding/unit anchor, a recommended answer or course and its basis,
and the exact decision or evidence tuple needed. Mark these items `pending
clarification`, wait, persist and read back each substantive answer under the
decision-record rules, and resume this same revision automatically only after
that gate. Recompute the frontier after each round; do not ask a downstream
question whose prerequisite remains open. Do not make the disputed edit or
publish a terminal closure table while waiting.

An explicit one-shot, no-discussion, or prose-only instruction opts out of this
loop. Preserve affected propositions and use that output contract without
pretending the finding was resolved. An item becomes terminally `blocked` only
when it needs an external unavailable prerequisite, or after the author declines,
cannot provide, or confirms unavailable the requested clarification/evidence.

Revision is locally complete when the requested paragraph-local repairs are closed, every incoming finding has a terminal closure state, no item remains `pending clarification`, the complete frozen scope has `Unreviewed: 0`, and no semantic, structural, or rhetorical regression is introduced. A separately reported cross-paragraph or evidence gap remains a blocker only under the terminal-blocker rule, not a successfully repaired argument.

## 3. Resolve structural uncertainty before prose

Use [revision-strategies.md](revision-strategies.md) to diagnose competing theses, mismatched contribution contracts, missing design/evidence dependencies, or interacting findings. Its structural operations are available only when the author explicitly requests restructuring; otherwise report the required choice and stay paragraph-local.

When alternatives imply different technical meanings, contribution hierarchies, assumptions, audiences, or trade-offs, preserve the original passage and resolve the author decision through the [shared clarification contract](review-revise-contract.md). Treat a question or placement suggestion as `pending clarification` until the author explicitly authorizes the exact structural operation and destination. When this is part of the requested revision, ask that question now and resume the same revision after the answer; do not merely list it as terminally blocked. Distinguish these scientific choices from meaning-equivalent optional wording; neither is silently applied.

## 4. Write at the right level

Apply [writing-core.md](writing-core.md) as the single source for argument, high-level exposition, paragraphs, sentences, wording, section contracts, and concision. Apply [chinese-writing.md](chinese-writing.md) when the source or output prose is Chinese or when translating from Chinese.

For file edits and fragile technical content, take the preservation snapshot and run the checks in [change-safety.md](change-safety.md). Edit figures, tables, code, data, or scripts only when the user explicitly includes those objects. A correction that changes experimental output leaves dependent manuscript claims unverified until the relevant evidence is regenerated and checked.

## 5. Run the full-scope gate

Re-read the complete frozen scope against the same standard used by Review and complete the [coverage gate and receipt](coverage-contract.md#completion-gate-and-receipt). For drafting, check the requested unit's role, supplied evidence, and output requirements under the composition branch above; original-paragraph preservation applies only to existing prose. For revision, confirm:

1. original paragraph boundaries, count, order, role, and content ownership remain intact unless the author explicitly authorized a change;
2. each direct edit fixes an identified problem rather than pursuing a preferred style or forcing a complete scientific argument;
3. any abstraction is equivalent to the original propositions and adds no purpose, cause, benefit, condition, or evidence;
4. the paragraph's existing role and emphasis remain recognizable; no background, explanation, summary, or transition sentence was added merely to fill a template;
5. sentence pairs and paragraph handoffs have valid logical relations, explicit scope, unique referents, and stable terminology, or their exact unresolved endpoints are reported;
6. adequate sentences remain intact, actual redundancy is removed without losing meaning, and any length increase is necessary to resolve a specific ambiguity rather than elaborate the argument;
7. facts, numbers, units, citations, equations, identifiers, macros, and evidence status remain correct.
8. review labels, venue-audit language, and new unresolved propositions have not entered the manuscript; an original unsupported claim is left unchanged and flagged unless the author explicitly authorized its correction or withdrawal, in which case verify that exact authorized change;
9. each changed sentence addresses the requested repair, and no paragraph adds an unsupported proposition or becomes a different kind of text.
10. every in-scope section, paragraph, sentence, relation, and lexical occurrence—including unchanged passed units and the last unit at each level—has a coverage state; when completing rather than pausing, every received finding has a terminal closure state and `unreviewed = 0`.
11. every identified local repair on the safe frontier was either applied or explicitly classified as optional/not applied; an evidence or structure blocker did not become a reason to skip an independent meaning-preserving correction.
12. every intellectual-move dependency added or strengthened by the revision is source-grounded or explicitly author-supplied and evidence-compatible; no reviewer-hypothesized bridge was promoted into manuscript prose, and independent outcomes were not falsely unified.
13. no requested `author clarification` or `author evidence` item remains pending;
    if one does, this is an interactive pause and the completion gate has not run.
14. every literal decision version has been classified; only executable heads
    constrained edits, and every stale, rejected, superseded, out-of-scope,
    evidence-conflicting, or structurally conflicting version is named in the
    decision receipt.

Compile, render, lint, or test only when the relevant dependencies are explicitly in scope and the action is authorized. State what a tool actually checked; a clean tool result does not establish publication readiness.

Use [convergence-loop.md](convergence-loop.md) instead of repeating ad hoc paraphrases when the user explicitly requests iteration or interacting edits require a fixed-point search. A loop may batch work, but it cannot narrow the frozen coverage obligation to changed paragraphs.

## 6. Return the deliverable first

For pasted material, lead with the conservatively revised prose in its original layout and markup; an unchanged passage is a valid result. For file edits, apply only the authorized corrections and name those objects. Keep role labels, diagnostics, and optional alternatives outside the manuscript and source files.

After the manuscript, include only applicable items:

- **Pending clarification:** after any safe edits, show the complete requested
  finding queue with action classes, then ask the whole prerequisite-ready
  frontier in the Grill format and wait. This replaces—not supplements—the
  terminal finding-closure map and manuscript coverage receipt for that turn.
  Show current decision accounting without claiming terminal completion. Preserve
  the scope and IDs so the next author answer resumes the same revision.

- **Finding closure:** map every received Review/Grill finding ID to `closed`, `blocked`, `not applied`, or `reopened`, with the original unit IDs and one-line resolution-test result. Omit this item only when there were no incoming findings or the user explicitly requested prose only.
- **Manuscript coverage receipt:** give the shared full-scope totals, last-unit
  states, not-assessable reasons, closure counts, and `Unreviewed` value. Omit it
  only under an explicit prose-only request; the internal gate still applies.
- **Decision coverage receipt:** give the authorized record identity, all literal
  IDs and status counts, effective/applicable/executable IDs, excluded versions
  with reasons, conflicts, and `Unaccounted decisions`. This receipt is mandatory,
  including during an interactive pause and after prose-only output.

- **Unresolved scientific issue:** name the original sentence pair or paragraph pair, quote the minimum identifying text, and state the missing premise or evidence. For an isolated claim, use its own anchor rather than inventing a pair. Keep the original claim unchanged pending the author's decision; do not imply that returning it verifies it.
- **可选写法 / Optional wording:** only when an alternative offers a clear gain in concision, precision, or information order beyond a necessary correction. Give its original anchor, one meaning-equivalent alternative, and one short reason. No routine synonym alternatives or duplicate full draft. A proposed split, heading, or list conversion is an optional format suggestion and needs explicit authorization before application.
- A consequential authorized change or relevant validation result when it helps the author assess the edit.

For a prose-only request, omit closure and manuscript-coverage records,
alternatives, general advice, and process commentary. Append exactly the compact
decision coverage receipt required by the decision-record rules. A minimal
post-prose note for an unresolved issue affecting scientific meaning may appear
before it; give the exact location and missing basis without a replacement
argument or separate report. Otherwise return the prose and that one receipt,
even when unchanged. This output exception does not waive either internal audit
or permit an unsupported completion claim.
