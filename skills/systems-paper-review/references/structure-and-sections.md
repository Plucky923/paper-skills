# Structure, Narrative, and Section Contracts

Read the canonical [systems-writing core](../../systems-paper-revise/references/writing-core.md) and [positive contracts](../../systems-paper-revise/references/paper-archetypes.md) for the writing model. This file adds review-specific attacks, severity, exceptions, and diagnostic maps; it does not replace those definitions.

## Global narrative rules

## SS-01 — The paper has one recoverable, problem-driven argument chain

- **Nature:** General best practice.
- **Reviewer attack:** “The sections are individually plausible but never form a coherent case for the contribution.”
- **Check:** First select the primary contract in [paper-archetypes.md](paper-archetypes.md) and reconstruct its dependencies. Use the first sentences of introduction paragraphs as a quick skeleton diagnostic, then inspect each paragraph's opening region and ending or handoff before declaring the spine broken; a short continuation may place its local obligation after the first sentence. Mark narration that makes the reader carry an unexplained solution before learning its problem/tension, mechanism lists with no governing principle, and missing or circular links. Naming the system first is not itself a defect when the same sentence or immediate continuation supplies the motivating relation.
- **Severity:** `S1` for a broken central chain; `S2` for costly ordering.
- **Exceptions / false positives:** Measurement, experience, negative-result, theory, and dataset papers use different chains. Operational work may establish its problem with quantified field evidence; empirical work may center a finding rather than a new mechanism. Require the routed contract's functions, not one universal order.
- **Repair direction:** Reorder around causal dependencies, add missing premise/inference, or narrow promises.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL], [OSDI-CFP], [SOSP-CFP], [FIVE-VENUE-CORPUS].

## SS-01A — Broad and expert readers receive the same decision case

- **Nature:** General best practice.
- **Reviewer attack:** “The abstract, introduction, overview, and captions advertise one simple story, but the technical sections establish a different or narrower claim.”
- **Check:** Run two readings over the same claim hierarchy. At broad-reader depth, recover the problem, delta, intellectual move, system or study reality, decisive evidence, and boundary without specialized mechanism detail. At expert depth, trace the model, assumptions, invariant, mechanism, setup, and uncertainty that discharge that same case. Flag contradictions, silent quantifier changes, and a first-layer promise that the second layer never validates.
- **Severity:** `S1` when the two layers imply different central claims; `S2` when discoverability or verification is unnecessarily costly.
- **Exceptions / false positives:** A broad account may omit detail, but it may not change technical meaning or hide a condition that controls the conclusion.
- **Repair direction:** Align both layers to one bounded claim; expose the minimum premise needed early and place verification depth where experts can audit it.
- **Sources:** [FIVE-VENUE-CORPUS] and current venue criteria.

## SS-01B — The first two pages pass the correct stress test

- **Nature:** Hard only when the live venue rules make it a review stage; otherwise diagnostic heuristic.
- **Reviewer attack:** “A rapid reader cannot recover why the work matters, what advances, why it may work, what exists, or what evidence will decide the claim.”
- **Check:** When the first two pages are in scope, test whether title, abstract, and opening introduction jointly expose the problem, closest-work delta, intellectual move, deliverable or study, credibility preview, and material boundary. Treat this as a binding rapid-review interface only when the live official CFP confirms it for the target venue, cycle, and stage. A possible procedure in a preliminary CFP is not a final rule. Otherwise, report failure as a reader-risk diagnostic, not noncompliance.
- **Severity:** By live venue rule; otherwise `S1` only when the decision case is genuinely unrecoverable, not merely because an item appears after an arbitrary page boundary.
- **Exceptions / false positives:** Do not expand a narrow excerpt review to unseen pages. Different archetypes may preview method credibility or findings rather than a new mechanism.
- **Repair direction:** Move the missing decision premise or credibility signal before secondary background/detail while preserving the paper's archetype.
- **Sources:** [ASPLOS-CFP], [OSDI-CFP]. Live verification required.

## SS-02 — Concepts appear before they are required

- **Nature:** General best practice.
- **Reviewer attack:** “A key term, assumption, metric, component, or result is used before I know what it means.”
- **Check:** Track first semantic use, not only first textual occurrence. Identify forward references, delayed definitions, unexplained acronyms, and definitions separated far from use without retrieval support.
- **Severity:** `S2`; `S1` when misunderstanding changes a central claim; `S3` locally.
- **Exceptions / false positives:** A brief intuitive preview may precede a formal definition if clearly signposted.
- **Repair direction:** Move or add a minimal local definition, defer the use, or add a precise pointer.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## SS-03 — Introduced concepts earn their cognitive cost

- **Nature:** General best practice.
- **Reviewer attack:** “The paper introduces terminology, notation, modules, or distinctions that are never used or could be expressed directly.”
- **Check:** For each named concept, find later analytical/design use. Flag synonyms masquerading as new terms and definitions that recursively introduce more undefined terms.
- **Severity:** `S2`; `S3` for isolated excess.
- **Exceptions / false positives:** A term can support precise discussion even if used only a few times; judge necessity.
- **Repair direction:** Remove/inline it, combine terms, or use it consistently in later reasoning.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## SS-04 — Section promises match delivered content

- **Nature:** Hard internal-consistency condition.
- **Reviewer attack:** “The heading/opening promises a model, design, proof, or answer that the section does not provide.”
- **Check:** Compare heading and opening roadmap with subsections, figures, and closing synthesis. Check that each evaluation question receives an answer.
- **Severity:** `S1` for a central broken promise; `S2` otherwise.
- **Exceptions / false positives:** A short transition need not recap every detail.
- **Repair direction:** Supply promised content, change the promise/heading, or move unrelated content.
- **Sources:** [SYSTEMS-GUIDE], [ERNST], [JENSEN-SYSTEMS-SKILL].

## SS-05 — Cross-section references reduce retrieval cost

- **Nature:** General best practice; mechanical frequency is a house-style choice.
- **Reviewer attack:** “The text relies on an earlier definition/design detail, but the reader cannot efficiently locate it.”
- **Check:** Identify dependencies separated by significant distance or ambiguous names. Verify pointers target the exact definition, mechanism, or figure. Do not demand a reference every time a term repeats.
- **Severity:** `S2` when reasoning depends on retrieval; `S3` otherwise.
- **Exceptions / false positives:** Recently introduced, memorable, or standard concepts need no repetitive pointer.
- **Repair direction:** Add a short reminder plus precise section/figure reference; avoid sending readers backward for basic comprehension repeatedly.
- **Sources:** [USER-NOTES] as normalized, [ERNST].

## SS-06 — High-level exposition states the causal principle before realization detail

- **Nature:** General best practice.
- **Reviewer attack:** “The overview enumerates components and operations but never explains the idea that makes them work,” or “the prose is called high-level only because it is vague.”
- **Check:** Apply the canonical high-level tests in the [systems-writing core](../../systems-paper-revise/references/writing-core.md). In the review record, identify which test fails: substitution, prediction, boundary/counterexample, or evidence. Classify the text as principle, mechanism, or implementation realization and flag abstraction-level jumps or inventories that obscure their relation.
- **Severity:** `S2`; `S1` if mechanism remains absent.
- **Exceptions / false positives:** A low-level fact may appear early when it supplies the evidence that reveals the constraint, defines the target property, or makes a counterexample concrete. A design section must eventually supply operational detail. High-level is causal compression relative to the reader's current knowledge, not the removal of technical content.
- **Repair direction:** Restore the shortest discriminating causal relation and its evidence pointer, then retain only detail that derives a decision, establishes a boundary, or proves feasibility.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL], [FIVE-VENUE-CORPUS].

## Paragraph and list rules

For every paragraph, first record any signaled or author-supplied role, then
independently choose its delivered conventional role from the existing
[paragraph-role research](../../../research/systems-paper-writing-requirements.md#每一种段落应怎样写):
problem, prior limitation, insight, overview, mechanism, evidence, limitation,
transition, or a clearly named mixed/specialized role. Use that source's
role-specific opening, development, and payoff expectations. Do not replace them
with one generic topic-sentence template, and do not force the author's paragraph
into the role the surrounding section ought to have contained. When the signaled
and delivered roles differ, report that mismatch rather than reclassifying it
away. Record the
expected-versus-actual comparison in the shared
[coverage ledger](../../systems-paper-revise/references/coverage-contract.md#keep-visible-per-unit-ledgers).

## SS-07 — Each paragraph discharges one local reasoning obligation

- **Nature:** General best practice.
- **Reviewer attack:** “The paragraph mixes background, design, results, caveats, and unrelated claims, so its point is unstable.”
- **Check:** Identify each original paragraph's signaled role when observable, delivered role, topic, claim/question, support, and closing takeaway through the [systems-writing core](../../systems-paper-revise/references/writing-core.md). Record `the reader should believe ___ because ___`; test whether its sentences serve that obligation. A connective does not make a second independent conclusion subordinate. Cite the opening and closing sentence anchors when the payoff is unsupported, evidence is stranded, a second independent center appears, or the delivered role contradicts the paragraph's promise. Do not assign a replacement role to make the paragraph pass.
- **Severity:** `S2`; `S1` if mixed logic hides a contradiction; `S3` locally.
- **Exceptions / false positives:** A short bridge paragraph may connect two ideas; mathematical derivations, enumerations, and tightly connected continuations need not follow a rigid topic-sentence/summary-sentence form. Judge the reasoning obligation, not a template.
- **Repair direction:** Clarify the existing obligation or reorder support inside the paragraph. If it requires splitting, moving content, or changing purpose, identify the exact units and mark explicit restructuring authority as required.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE], [FIVE-VENUE-CORPUS].

## SS-08 — Sentence order follows information and causal dependencies

- **Nature:** General best practice.
- **Reviewer attack:** “I must infer why a sentence follows the previous one or reinterpret earlier sentences after learning a missing premise.”
- **Check:** Inspect each adjacent sentence pair and explicit longer dependency. Name the relation: elaboration, evidence, cause, consequence, contrast, condition, example, limitation, or handoff. For every failure, cite both original sentence IDs and short quoted anchors; state what the first establishes, what the second needs, and the invalid inference, changed referent/scope, or missing premise. A shared keyword or added connective is not sufficient evidence of a link.
- **Severity:** `S2`; `S3` for one rough transition.
- **Exceptions / false positives:** Repetition of an exact word is not required; conceptual continuity is.
- **Repair direction:** Clarify a relation supported inside the paragraph or reorder its sentences. A missing scientific premise requires evidence or an author decision; it cannot be supplied by a transition word or invented bridge.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## SS-09 — Topic sentences are informative, not overloaded

- **Nature:** General best practice.
- **Reviewer attack:** “The paragraph begins with a long inventory or vague metacommentary instead of its decision-relevant point.”
- **Check:** Determine whether the first sentence states the local claim, contrast, question, or dependency at the right level and leaves support/details to follow. In problem-driven passages, verify that it names the reader's current problem or inference rather than merely announcing a component. Flag `This section discusses...` when a substantive claim is available.
- **Severity:** `S2` for recurring issue; `S3` locally.
- **Exceptions / false positives:** Not every paragraph must use a rigid topic-sentence-first form, especially mathematical derivations or tightly connected continuations.
- **Repair direction:** Lead with the claim or relation, then supply mechanism/evidence/qualification.
- **Sources:** [USER-NOTES], [ERNST], [FIVE-VENUE-CORPUS].

## SS-09A — Paragraph endings resolve or deliberately transfer the local obligation

- **Nature:** General best practice.
- **Reviewer attack:** “The paragraph stops after an example or mechanism detail, so I do not know what was established or why the next paragraph follows.”
- **Check:** Determine what the final sentence contributes: strongest evidence, answer, consequence, limitation, design requirement, or question that licenses the next paragraph. State what supported information would be lost if it were deleted. Then run the mechanical-inversion test: a sentence can disappear while its wording is lost yet its entire update remains mechanically recoverable from `does not provide X` as `must provide X`. Flag an ending whose only function is that inversion or repeats the opening/preceding limitation in a stock `however/therefore/still requires` rhythm. Verify any limitation-to-requirement transition is established, design-specific, and adds a consequence, constraint, choice, or handoff beyond the missing property itself. For every adjacent pair in scope, compare both paragraph roles and inspect the first paragraph's close against the next paragraph's opening. A failure must name both paragraph IDs and relevant sentence anchors, explaining what was established, what is assumed next, and the missing or conflicting relation. Follow nonadjacent dependencies when explicitly signaled; absent neighbors are not assessable.
- **Severity:** `S2` when a missing close breaks an important inference; `S3` locally.
- **Exceptions / false positives:** The last sentence need not restate the topic sentence, and the logical close may be a result, caveat, or transition rather than a summary. Short bridge paragraphs, formal derivations, and lists may close implicitly when the implication is unambiguous.
- **Repair direction:** Make the existing takeaway or handoff explicit within its own paragraph where supported. If the link requires a new premise, content transfer, or structural change, report that dependency and required author authority; do not prescribe a fabricated bridge or formulaic summary.
- **Sources:** [USER-NOTES], [ERNST], [FIVE-VENUE-CORPUS].

## SS-10 — Paragraph length follows reasoning, not rendered line count

- **Nature:** Diagnostic heuristic / house style.
- **Reviewer attack:** “The paragraph is too dense to parse or so fragmented that the argument loses momentum.”
- **Check:** Diagnose inferential density, not sentence count. Flag a paragraph that mixes independent obligations, changes abstraction level without a bridge, accumulates citations without a comparison axis, or compresses away a condition, causal link, evidence scope, or payoff. Flag fragmentation when adjacent short paragraphs cannot independently complete an inference. Rendered height and sentence count may select passages for inspection but cannot establish a defect.
- **Severity:** `S2` when logic is obscured; `S3` or `S4` for layout only.
- **Exceptions / false positives:** Necessary proof/algorithm exposition can be longer; short transition paragraphs can be valid.
- **Repair direction:** First identify the exact sentence or paragraph pair causing overload or fragmentation. Distinguish a paragraph-local wording repair from a split, merge, or content transfer requiring explicit author restructuring authority.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE].

## SS-11 — Lists are parallel and introduced by a governing claim

- **Nature:** General best practice.
- **Reviewer attack:** “The bullets mix contributions, mechanisms, benefits, and results, or their relationship to the lead-in is unclear.”
- **Check:** Verify grammatical and conceptual parallelism, non-overlap, meaningful order, complete lead-in, and consistent granularity. Each long bullet should surface its point early.
- **Severity:** `S2`; `S3` for surface parallelism.
- **Exceptions / false positives:** Short label/value lists need no full topic sentence in every item.
- **Repair direction:** Choose one organizing dimension, rewrite lead-in, merge/split items, and align syntax.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## Section contracts

## SS-12 — Title is specific, accurate, and searchable

- **Nature:** General best practice plus venue formatting rules.
- **Reviewer attack:** “The title overclaims, hides the systems contribution, or could describe many unrelated papers.”
- **Check:** Compare title with actual problem, contribution type, domain, and claim boundary. Check unexplained acronym, marketing language, and superlative.
- **Severity:** `S2`; `S1` for material misrepresentation; venue violations follow `VO` severity.
- **Exceptions / false positives:** Memorable system names are acceptable when paired with an informative subtitle/title phrase.
- **Repair direction:** Name the distinctive systems idea/problem and bound scope.
- **Sources:** [ERNST], [LEVIN-REDELL], current venue rules.

## SS-13 — Abstract is a faithful, principle-level miniature argument

- **Nature:** General best practice; word/format limits are venue-specific.
- **Reviewer attack:** “After the abstract I still do not know the problem, gap, idea, implementation/evidence, or magnitude and boundary of results.”
- **Check:** Select the paper archetype, then verify that the abstract completes its decision functions: consequential problem/question; the relevant gap, failed assumption, or tension; intellectual move or central finding; concrete deliverable; decisive bounded evidence; implication or boundary. These functions may be combined, reordered, or expressed without labels. A list of components is not a substitute for the intellectual move. Cross-check every number and superlative with paper evidence when in scope.
- **Severity:** `S1` for missing/misleading central case; `S2` for imbalance.
- **Exceptions / false positives:** Do not enforce a fixed sentence count, problem-first grammar, contribution list, or `insight` wording. A system may be named first if the problem/tension becomes immediately recoverable. Adapt to contribution type and venue.
- **Repair direction:** Replace background/detail with the missing contribution element and calibrate results.
- **Sources:** [SYSTEMS-GUIDE], [ERNST], [OSDI-CFP], [SOSP-CFP], [FIVE-VENUE-CORPUS].

## SS-14 — Introduction establishes the complete decision case

- **Nature:** General best practice.
- **Reviewer attack:** “The introduction states a solution before establishing the problem/root cause/challenge, or promises novelty and results without a coherent path.”
- **Check:** Apply the selected archetype's positive contract and [thesis-and-story.md](thesis-and-story.md). Verify that the introduction establishes one controlling thesis, derives rather than announces major requirements/findings, previews decisive evidence, and makes scope recoverable. For a design paper, each mechanism must answer an already visible requirement and the high-level account must explain why it can work. For empirical or operational work, method credibility and findings may replace a root-cause/solution sequence.
- **Severity:** `S1`; `S2` for local flow.
- **Exceptions / false positives:** Order and paragraph count are flexible. Contribution bullets and an explicit challenge list are optional. Some paper types need no root cause, new mechanism, or standalone evaluation preview.
- **Repair direction:** Restore the shortest causal chain and eliminate details that interrupt it.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL], [OSDI-CFP], [SOSP-CFP], [FIVE-VENUE-CORPUS].

## SS-15 — Background teaches only prerequisites

- **Nature:** General best practice.
- **Reviewer attack:** “Background is a textbook survey, duplicates related work, or hides the paper's own contribution.”
- **Check:** For each background item, find a later dependency. Separate neutral prerequisite from motivation/critique and from novel design.
- **Severity:** `S2`; `S1` if contribution ownership becomes ambiguous.
- **Exceptions / false positives:** An interdisciplinary audience may need more background; explain it at the level used later.
- **Repair direction:** Remove unused exposition, move comparisons to motivation/related work, and mark original content.
- **Sources:** [SYSTEMS-GUIDE], [ERNST], [LEVIN-REDELL].

## SS-16 — Motivation makes prior limitations causal and fair

- **Nature:** Hard accuracy condition plus general best practice.
- **Reviewer attack:** “The motivation attacks weak caricatures or lists symptoms without showing why existing designs fundamentally miss the new requirement.”
- **Check:** First classify the bridge under the shared [interface-boundary contract](../../systems-paper-revise/references/interface-boundaries.md). A negative gap connects fair difference → shared root cause/constraint → why the target property remains unmet → new insight and needs evidence about the named work. A distinct-question bridge needs a parallel design-space map and a bounded question, but does not need an invented common failure and does not establish novelty. Keep comparison organization, causal strength, and external verification separate so one risk does not hide another. Missing incoming antecedents or source access changes evidence status but does not waive inspection of the locally visible bridge. Verify externally when permitted.
- **Severity:** `S1`; `S0` for materially false positioning.
- **Exceptions / false positives:** Empirical motivation can be a measurement study; causal language still needs evidence.
- **Repair direction:** Use accurate categories, precise limitations, and bounded claims; remove strawmen.
- **Sources:** [SYSTEMS-GUIDE], [LEVIN-REDELL], [OSDI-CFP].

## SS-17 — Overview defines model and workflow without replacing design

- **Nature:** General best practice.
- **Reviewer attack:** “I cannot tell assumptions, inputs/outputs, major stages, or where the contribution lies,” or “the design section later repeats the same boxes.”
- **Check:** Look for system model, deployment context, high-level workflow, interfaces, major insights/challenges, and scope. Ensure mechanism details and rationale remain for design.
- **Severity:** `S1` when model/workflow is unrecoverable; `S2` for abstraction imbalance.
- **Exceptions / false positives:** A separate overview is optional if introduction/design already provide these functions clearly.
- **Repair direction:** Add a compact model/workflow and map later sections; remove premature detail.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE].

## SS-18 — Design explains why and how, not just what

- **Nature:** Hard technical-completeness condition for a design contribution.
- **Reviewer attack:** “The design section restates goals and boxes but omits algorithm, state, lifecycle, edge cases, and design choices.”
- **Check:** Apply `TS` rules to each major stage: objective/constraint, input/state, operation, output, start/stop, alternatives/tradeoff, invariant, failure/edge behavior, and link to overview challenge.
- **Severity:** `S1`; `S0` for a fatal hidden gap.
- **Exceptions / false positives:** Standard mechanisms may be cited rather than rederived; adaptations must be explained.
- **Repair direction:** Add causal/operational detail and rationale, use pseudocode/figure when clearer, remove repetitive overview prose.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL].

## SS-19 — Implementation separates realization from intellectual design

- **Nature:** General best practice; hard accuracy for status claims.
- **Reviewer attack:** “I cannot tell what was actually built, what was borrowed, and which engineering detail is necessary for the reported result.”
- **Check:** Identify codebase/version, languages/LOC only with context, reused components, major engineering choices, incomplete/stubbed parts, and deviations from design. Avoid implementation inventory without consequence.
- **Severity:** `S1` for maturity mismatch; `S2` for unclear detail.
- **Exceptions / false positives:** Some venues/papers integrate implementation into design.
- **Repair direction:** State implementation boundary and decision-relevant realization details; remove vanity counts.
- **Sources:** [LEVIN-REDELL], [USER-NOTES], [NSDI-ARTIFACT].

## SS-20 — Evaluation evidence answers recoverable questions

- **Nature:** Hard evidence-organization condition.
- **Reviewer attack:** “The paper lists setup and plots but never says which contribution each experiment validates or what answer follows.”
- **Check:** Recover the question answered by each experiment, proof, case study, or production observation; it may be stated in a heading, prose, or an interleaved finding/intervention sequence. Look for reproducible setup, baseline/workload rationale, evidence-to-claim mapping, result plus interpretation, design reference for mechanism explanations, and limitations. In a completed-paper context, flag `must be evaluated`, `remains to be tested`, and equivalent prose when it replaces an available answer or exposes a result placeholder; in a proposal or roadmap, keep the planned status. Treat an ordinary request to review paper/manuscript prose as research-paper context unless proposal/plan status is explicit. If lifecycle is genuinely ambiguous, report the completed-paper placeholder risk conditionally and request that state; do not pass the sentence solely because it is cautious. Apply the selected archetype rather than requiring one monolithic evaluation section.
- **Severity:** `S1` when claim coverage is missing; `S2` for organization.
- **Exceptions / false positives:** Questions need not be enumerated mechanically. Operational and measurement papers may interleave method, observation, intervention, and validation when each inference remains auditable.
- **Repair direction:** Organize by claim/question, state answer with uncertainty, and connect cause only when supported.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [SIGPLAN-EMPIRICAL], [FIVE-VENUE-CORPUS].

## SS-21 — Related work distinguishes rather than enumerates

- **Nature:** General best practice; citation completeness is factual.
- **Reviewer attack:** “The section is a bibliography dump or hides the closest comparison among broad categories.”
- **Check:** Group by decision-relevant dimensions, cite accurate representative and closest work, state fair similarities/differences, and connect to contribution without repeating motivation. When the paragraph derives a negative research gap, require the shared assumption, mechanism, or constraint that causes it; different boundaries alone do not supply that claim. When it poses only a distinct question from a parallel map, do not manufacture a negative gap, and assess novelty separately. Keep organization independent from the evidentiary question of whether the literature supports every factual or negative claim.
- **Severity:** `S1` for missing/false closest-work positioning; `S2` for organization.
- **Exceptions / false positives:** Studies of system evolution and surveys may need chronology; use it only when chronology advances the argument.
- **Repair direction:** Reorganize by mechanism/assumption/capability and add precise comparison.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [ERNST].

## SS-22 — Discussion and limitations interpret boundaries honestly

- **Nature:** Hard accuracy condition for conclusions; section itself optional.
- **Reviewer attack:** “The paper buries adoption costs, unsupported environments, ethical/security risks, or threats to validity.”
- **Check:** Compare unresolved tradeoffs, failure modes, generality, deployment constraints, and evaluation validity with headline claims. Check future work is not described as current support. If a boundary materially narrows a central broad-reader claim, require a concise early disclosure while allowing detailed treatment later. With only an isolated limitation paragraph, proactively give that conditional judgment even when placement was not asked about, and mark exact Introduction placement not assessable rather than declaring the paragraph misplaced or moving it.
- **Severity:** `S1`; `S0` if hidden limitation negates central claim.
- **Exceptions / false positives:** Limitations may appear throughout rather than in a dedicated section.
- **Repair direction:** State material boundaries and consequences; separate mitigation already implemented from future work.
- **Sources:** [OSDI-CFP], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL].

## SS-23 — Conclusion closes the established argument without adding claims

- **Nature:** Hard internal-consistency condition.
- **Reviewer attack:** “The conclusion introduces a stronger property, application, or generalization than the paper established.”
- **Check:** Map each conclusion statement to a stated contribution and evidence. Ensure takeaway names the supported insight/lesson, not only system name and best number.
- **Severity:** `S1` for new/overbroad central claim; `S2` for weak synthesis.
- **Exceptions / false positives:** A concise implication can be inferential if clearly labeled and grounded.
- **Repair direction:** Remove/narrow new claims and synthesize supported lessons and conditions.
- **Sources:** [ERNST], [LEVIN-REDELL], [OSDI-CFP].

## SS-24 — Appendix and supplement are not required to rescue the main argument

- **Nature:** Venue-specific plus general best practice.
- **Reviewer attack:** “The main paper is unintelligible or unsupported unless optional/nonreviewed material is read.”
- **Check:** Verify current venue treatment of appendices/supplements. Ensure central problem, mechanism, evidence, and limitations stand in the required paper; supplement adds depth/reproduction rather than foundational missing logic.
- **Severity:** `S0` for verified noncompliance; `S1` for a main-paper dependency.
- **Exceptions / false positives:** Formal proofs, extended results, and artifact instructions may appropriately be supplementary when official rules allow.
- **Repair direction:** Move essential content into the main paper or narrow claims; verify live rules.
- **Sources:** Current venue instructions; [SYSTEMS-GUIDE]. Live verification required.

## Structure audit outputs

For a full paper, introduction, abstract, or other argument-bearing scope, produce an argument-spine map and feed its state into the visible coverage ledger:

### Argument-spine map

| Unit | Problem/consequence | Root constraint | Insight/principle | Realization | Evidence/implication | Break |
|---|---|---|---|---|---|---|

For every multi-paragraph prose or structure scope, produce a paragraph-envelope map. `Status` records whether the middle discharges the opening and the ending pays off or deliberately transfers that obligation. The shared paragraph ledger additionally records actual role, role convention, sentence roles, neighbor relation, and finding IDs; this smaller map does not replace it.

### Paragraph-envelope map

| Paragraph | Opening promise | Closing payoff/handoff | Status |
|---|---|---|---|

For a full paper, also produce these two maps:

### Promise map

| Promise location | Promise | Delivery location | Evidence location | Status |
|---|---|---|---|---|

### Dependency map

| First use | Required concept/model/result | Defined where | Retrieval cost | Problem |
|---|---|---|---|---|

For a scoped excerpt, do not search outside scope to fill these maps; use `not assessable — needs context`.
