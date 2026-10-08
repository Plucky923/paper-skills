# Structure, Narrative, and Section Contracts

Read the [systems-writing core](../../systems-paper-revise/references/writing-core.md) and [positive contracts](../../systems-paper-revise/references/paper-archetypes.md) for the writing model. This file adds reviewer attacks, severity, exceptions, and diagnostic maps. The shared definitions stay authoritative.

## Global narrative rules

## SS-01 — The paper has one recoverable, problem-driven argument chain

- **Nature:** General best practice.
- **Reviewer attack:** “The sections are individually plausible but never form a coherent case for the contribution.”
- **Check:** First, select the primary contract in [paper-archetypes.md](paper-archetypes.md). Make a reconstruction of its dependencies. Use introduction first sentences as a quick structure diagnostic. Before a broken-chain finding, examine each paragraph's opening, ending, and handoff.

  A short continuation can give its obligation after the first sentence. Find unexplained solutions before problems or tensions, mechanism lists without principles, and missing or circular links. A system name first is permitted with an immediate motivating relation.
- **Severity:** `S1` for a broken central chain. `S2` for costly ordering.
- **Exceptions / false positives:** Measurement, experience, negative-result, theory, and dataset papers use different chains. Operations can give field evidence for the problem. Empirical papers can have a finding as their central contribution. Use the selected contract's functions.
- **Repair direction:** Give repair options: causal dependency order, missing premises or inferences, or narrower promises.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL], [OSDI-CFP], [SOSP-CFP], [FIVE-VENUE-CORPUS].

## SS-01A — Broad and expert readers receive the same decision case

- **Nature:** General best practice.
- **Reviewer attack:** “The abstract, introduction, overview, and captions advertise one simple story, but the technical sections establish a different or narrower claim.”
- **Check:** Read the same claim hierarchy at two depths. For broad readers, find the problem, difference, move, system or study with evidence for its status, decisive evidence, and boundary. For experts, examine the model, assumptions, invariant, mechanism, setup, and uncertainty that show the same case. Find contradictions, silent quantifier changes, and first-layer promises without second-layer validation.
- **Severity:** `S1` when the two layers imply different central claims. `S2` when discoverability or verification is unnecessarily costly.
- **Exceptions / false positives:** A broad account can have fewer details. It must keep technical meaning and each condition that controls the conclusion.
- **Repair direction:** Make sure that both layers agree with one bounded claim. Give necessary premises before their dependent claims. Put verification detail where experts can examine it.
- **Sources:** [FIVE-VENUE-CORPUS] and venue criteria in effect.

## SS-01B — The first two pages pass the correct stress test

- **Nature:** Condition only when the venue rules in effect make it a review stage. For other cases, diagnostic heuristic.
- **Reviewer attack:** “A rapid reader cannot recover why the work matters, what advances, why it may work, what exists, or what evidence will decide the claim.”
- **Check:** If the first two pages are in scope, examine the title, abstract, and opening introduction together. Find the problem, closest-work difference, move, deliverable or study, credibility preview, and boundary that affects conclusions. Use this as a mandatory rapid-review interface only with an official rule in effect for that venue, cycle, and stage. Preliminary possibilities are not final rules. Without an official rule, give only reader-risk findings.
- **Severity:** Use the venue rule in effect. Without that rule, use `S1` only if the reader cannot find the decision case. A page boundary alone does not show that failure.
- **Exceptions / false positives:** Keep unseen pages outside narrow excerpt scope. Different archetypes can preview method credibility or findings without a new mechanism.
- **Repair direction:** Put missing decision premises or credibility evidence before secondary background and detail. Keep the paper archetype.
- **Sources:** [ASPLOS-CFP], [OSDI-CFP]. Online verification is necessary.

## SS-02 — Concepts appear before they are required

- **Nature:** General best practice.
- **Reviewer attack:** “A key term, assumption, metric, component, or result is used before I know what it means.”
- **Check:** Record first semantic use in different checks from first textual occurrence. Find forward references, late definitions, unexplained acronyms, and distant definitions without retrieval aids.
- **Severity:** `S2`. `S1` when misunderstanding changes a central claim. `S3` locally.
- **Exceptions / false positives:** An intuitive preview can precede a formal definition with a clear signal.
- **Repair direction:** Give repair options: a definition near its first use, subsequent use, or an accurate reference.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## SS-03 — Introduced concepts earn their cognitive cost

- **Nature:** General best practice.
- **Reviewer attack:** “The paper introduces terminology, notation, modules, or distinctions that are never used or could be expressed directly.”
- **Check:** For each concept name, find subsequent analysis or design use. Find synonyms presented as new terms and definitions with recursive unexplained terms.
- **Severity:** `S2`. `S3` for isolated excess.
- **Exceptions / false positives:** A term can help accurate discussion with few uses. Examine its necessity.
- **Repair direction:** Give repair options: removal, direct explanation, combined terms, or subsequent use with the same meaning.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## SS-04 — Section promises match delivered content

- **Nature:** Condition for internal consistency.
- **Reviewer attack:** “The heading/opening promises a model, design, proof, or answer that the section does not provide.”
- **Check:** Compare headings and opening roadmaps with subsections, figures, and closing synthesis. Make sure that each evaluation question has an answer.
- **Severity:** `S1` for a central broken promise. `S2` in other cases.
- **Exceptions / false positives:** A short transition does not make a full detail summary necessary.
- **Repair direction:** Give repair options: promised content, changed promises or headings, or relocated unrelated content.
- **Sources:** [SYSTEMS-GUIDE], [ERNST], [JENSEN-SYSTEMS-SKILL].

## SS-05 — Cross-section references reduce retrieval cost

- **Nature:** General best practice. Mechanical frequency is a house-style choice.
- **Reviewer attack:** “The text relies on an earlier definition/design detail, but the reader cannot efficiently locate it.”
- **Check:** Find distant dependencies and unclear names. Make sure that references point to the correct definition, mechanism, or figure. Make references necessary only for difficult retrieval.
- **Severity:** `S2` when reasoning depends on retrieval. `S3` in other cases.
- **Exceptions / false positives:** Recent, memorable, or standard concepts do not make repeated references necessary.
- **Repair direction:** Give a short reminder and accurate section or figure reference. Do not send readers backward repeatedly for basic comprehension.
- **Sources:** [USER-NOTES] as normalized, [ERNST].

## SS-06 — High-level exposition gives the causal principle before realization detail

- **Nature:** General best practice.
- **Reviewer attack:** “The overview enumerates components and operations but never explains the idea that makes them work,” or “the prose is called high-level only because it is vague.”
- **Check:** Apply the [writing core](../../systems-paper-revise/references/writing-core.md) high-level tests. Record failed substitution, prediction, boundary or counterexample, or evidence tests. Give the text its level: principle, mechanism, or implementation. Find abstraction changes or inventories without clear relations.
- **Severity:** `S2`. `S1` if mechanism stays absent.
- **Exceptions / false positives:** A low-level fact before the principles can give constraint evidence, target-property definitions, or counterexamples with specified conditions. Design must eventually give operational detail. High-level prose gives causal compression for the reader's knowledge at that point. It keeps technical content.
- **Repair direction:** Give the shortest distinguishing causal relation and evidence reference. Keep details for consequential decisions, boundaries, or feasibility.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL], [FIVE-VENUE-CORPUS].

## Paragraph and list rules

For each paragraph, record the signaled or author-supplied role first. Independently select the delivered role from the [paragraph-role research](../../../research/systems-paper-writing-requirements.md#每一种段落应怎样写).

Use problem, prior limitation, insight, overview, mechanism, evidence, limitation, transition, or a clear mixed or specialized role. Use that role's opening, development, and payoff expectations.

Do not treat these expectations as a generic topic-sentence template. Compare the delivered paragraph role with the expected section role. Record role mismatches. Give expected and delivered functions in the [coverage ledger](../../systems-paper-revise/references/coverage-contract.md#keep-visible-per-unit-ledgers).

## SS-07 — Each paragraph discharges one local reasoning obligation

- **Nature:** General best practice.
- **Reviewer attack:** “The paragraph mixes background, design, results, caveats, and unrelated claims, so its point is unstable.”
- **Check:** Use the [writing core](../../systems-paper-revise/references/writing-core.md) for paragraph checks. Record signaled role where visible, delivered role, topic, claim or question, evidence, and closing conclusion. Complete `the reader should believe ___ because ___`. Examine each sentence's contribution to that obligation. A connective alone does not subordinate a second independent conclusion.

  For payoff, evidence, competing-center, or role defects, give citations for opening and closing anchors. Keep the delivered role during judgment.
- **Severity:** `S2`. `S1` if mixed logic hides a contradiction. `S3` locally.
- **Exceptions / false positives:** A short bridge can connect two ideas. Derivations, lists, and close continuations have no fixed topic-sentence and summary-sentence requirement. Examine the reasoning obligation.
- **Repair direction:** Make the existing obligation clear or change the evidence order inside the paragraph.
  For division, relocation, or purpose changes, state the specified units and required restructuring authority.
  A diagnosis does not give that authority.
  If the diagnosed repair would split or move content, explicitly state that author authorization is required.
  State this boundary even when the current request prohibits restructuring.
  Keep the visible role diagnosis separate from unavailable destination context.
  Mark exact placement not assessable when the destination is outside scope.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE], [FIVE-VENUE-CORPUS].

## SS-08 — Sentence order agrees with information and causal dependencies

- **Nature:** General best practice.
- **Reviewer attack:** “I must infer why a sentence follows the previous one or reinterpret earlier sentences after learning a missing premise.”
- **Check:** Examine each adjacent sentence pair and each stated longer dependency. Give its relation: elaboration, evidence, cause, consequence, contrast, condition, example, limitation, or handoff. For each failed relation, give citations for both IDs and short original quotations. Record the first sentence's conclusion and the second's dependencies. Record invalid inference, changed referents or scope, and missing premises. A shared keyword or added connective alone does not show a link.
- **Severity:** `S2`. `S3` for one rough transition.
- **Exceptions / false positives:** Conceptual continuity is necessary. Exact word repetition is not.
- **Repair direction:** Give the relation with paragraph-local evidence or change sentence order. Missing scientific premises make evidence or author decisions necessary. Keep invented bridges outside repairs.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## SS-09 — Topic sentences are informative, not overloaded

- **Nature:** General best practice.
- **Reviewer attack:** “The paragraph begins with a long inventory or vague metacommentary instead of its decision-relevant point.”
- **Check:** Examine the first sentence's claim, contrast, question, or dependency at the applicable level. Make sure that subsequent text gives evidence and details. In problem-driven passages, find the problem or inference at that point. A component announcement alone can be insufficient. Find `This section discusses...` where a substantive claim is available.
- **Severity:** `S2` for recurring issue. `S3` locally.
- **Exceptions / false positives:** First-sentence topic form is not universal. Derivations and close continuations can use different forms.
- **Repair direction:** Give the claim or relation first. Then give mechanism, evidence, and qualifications.
- **Sources:** [USER-NOTES], [ERNST], [FIVE-VENUE-CORPUS].

## SS-09A — Paragraph endings complete the obligation or give it to the next paragraph

- **Nature:** General best practice.
- **Reviewer attack:** “The paragraph stops after an example or mechanism detail, so I do not know what was established or why the next paragraph follows.”
- **Check:** Record the final sentence's contribution: strongest evidence, answer, consequence, limitation, requirement, or next-paragraph question. Record information lost if removed. Apply the mechanical-inversion test. Compare `does not provide X` with `must provide X`. If all information stays mechanically recoverable, record the redundant ending.

  Find repeated openings or limitations in stock `however/therefore/still requires` endings. Make sure that limitation-to-requirement links have evidence and design-specific information gain. Make sure that a new consequence, constraint, choice, or handoff goes beyond the missing property.

  For each adjacent paragraph pair, compare roles and the close-to-opening relation. Give both paragraph IDs and sentence anchors for failures. Record the established information, next assumption, and missing or conflicting relation. Examine stated nonadjacent dependencies. Keep unavailable neighbors not assessable.
- **Severity:** `S2` when a missing close breaks an important inference. `S3` locally.
- **Exceptions / false positives:** The ending can give a result, caveat, or transition without a repeated topic sentence. Short bridges, derivations, and lists can close implicitly with an unambiguous implication.
- **Repair direction:** Make the existing conclusion or handoff clear in its paragraph with evidence. For new premises, content transfers, or structure changes, give dependencies and required authority. Keep invented bridges and formulaic summaries outside repair directions.
- **Sources:** [USER-NOTES], [ERNST], [FIVE-VENUE-CORPUS].

## SS-09B — Promised observations and insights deliver an intellectual update

- **Nature:** General best practice with important argument consequences when the role carries the contribution.
- **Reviewer attack:** “The paragraph is labeled as the paper's observation or insight, but it only restates definitions, requirements, or mechanisms.”
- **Check:** Use the [positioning and intellectual-move contract](../../systems-paper-revise/references/positioning-and-insight.md). Find the evidence anchor, non-definitional inference, information loss without that inference, predicted design or evidence choice, and boundary. Record the intended role in different checks from the delivered role. Include evidence-observation, interpretation, insight, requirement, objective, mechanism, or mixed roles. Examine `these differences show` openings and heading-restatement endings at their specified endpoints.
- **Severity:** `S1` when a central intellectual move is absent. `S2` for a local role mismatch.
- **Exceptions / false positives:** A model fact, counterexample, or prior-work contrast can give the relation. A new experiment or fixed sentence position is not necessary. A clear requirement paragraph does not make artificial surprise necessary.
- **Repair direction:** Give the source-grounded relation at the specified endpoints or the delivered role. For renaming, new purpose, or relocation, get author clarification and restructuring authority. Use only observations with evidence.
- **Sources:** [SYSTEMS-GUIDE], [FIVE-VENUE-CORPUS], [USER-NOTES].

## SS-10 — Paragraph length depends on reasoning

- **Nature:** Diagnostic heuristic / house style.
- **Reviewer attack:** “The paragraph is too dense to parse or so fragmented that the argument loses momentum.”
- **Check:** Examine inference density. Find independent obligations, abstraction changes without bridges, citations without comparison axes, and missing conditions, causal links, evidence scope, or payoff. Find fragmentation where adjacent short paragraphs cannot independently complete an inference. Rendered height and sentence count can select inspection targets. They do not show defects.
- **Severity:** `S2` when logic is obscured. `S3` or `S4` for layout only.
- **Exceptions / false positives:** Necessary proof or algorithm descriptions can be long. Short transitions can be correct.
- **Repair direction:** Give the specified sentence or paragraph pair with overload or fragmentation. Do a check of differences between local wording repairs and paragraph division, combination, or content transfer. Give required restructuring authority for those changes.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE].

## SS-11 — Lists are parallel and introduced by a governing claim

- **Nature:** General best practice.
- **Reviewer attack:** “The bullets mix contributions, mechanisms, benefits, and results, or their relationship to the lead-in is unclear.”
- **Check:** Examine grammatical and conceptual parallelism, overlap, meaningful sequence, full lead-ins, and the same granularity. Make sure that long bullets give their primary point first.
- **Severity:** `S2`. `S3` for surface parallelism.
- **Exceptions / false positives:** Short label/value lists do not make full topic sentences necessary in each item.
- **Repair direction:** Select one organizing dimension. Give a clear lead-in. Combine or divide items where necessary. Use the same syntax.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## Section contracts

## SS-12 — Title gives scope and permits accurate search

- **Nature:** General best practice plus venue formatting rules.
- **Reviewer attack:** “The title overclaims, hides the systems contribution, or could describe many unrelated papers.”
- **Check:** Compare the title with problem, contribution type, domain, and claim boundaries. Find unexplained acronyms, marketing language, and superlatives.
- **Severity:** `S2`. `S1` for misrepresentation that changes conclusions. Use `VO` severity for venue violations.
- **Exceptions / false positives:** System names are permitted with informative title or subtitle phrases.
- **Repair direction:** Give the distinctive systems idea or problem and its scope boundary.
- **Sources:** [ERNST], [LEVIN-REDELL], venue rules in effect.

## SS-13 — Abstract is a faithful, principle-level miniature argument

- **Nature:** General best practice. Word/format limits are venue-specific.
- **Reviewer attack:** “After the abstract I still do not know the problem, gap, idea, implementation/evidence, or magnitude and boundary of results.”
- **Check:** Select the paper archetype. Examine abstract functions: consequential problem or question, gap or failed assumption or tension, move or finding, deliverable, decisive evidence, and implication or boundary. Functions can combine or change order without labels. Component lists do not replace intellectual moves. Compare each number and superlative with evidence in scope.
- **Severity:** `S1` for missing/misleading central case. `S2` for imbalance.
- **Exceptions / false positives:** Fixed sentence counts, problem-first grammar, contribution lists, and `insight` labels are not necessary. A system name can occur first with an immediate motivating relation. Use the contribution type and venue.
- **Repair direction:** Replace unnecessary background or detail with missing contribution functions. Make sure that result claims agree with evidence.
- **Sources:** [SYSTEMS-GUIDE], [ERNST], [OSDI-CFP], [SOSP-CFP], [FIVE-VENUE-CORPUS].

## SS-14 — Introduction shows the full decision case

- **Nature:** General best practice.
- **Reviewer attack:** “The introduction states a solution before establishing the problem/root cause/challenge, or promises novelty and results without a coherent path.”
- **Check:** Use the selected positive contract and [thesis-and-story.md](thesis-and-story.md). Examine the controlling thesis, requirement or finding derivation, decisive-evidence preview, and recoverable scope. For design papers, compare each mechanism with an already visible requirement. Examine its high-level causal account. For empirical or operational work, method credibility and findings can replace a root-cause-to-solution sequence.
- **Severity:** `S1`. `S2` for local flow.
- **Exceptions / false positives:** Sentence order and paragraph count can differ. Contribution bullets and challenge lists are optional. Some paper types have no root-cause, new-mechanism, or evaluation-preview requirement.
- **Repair direction:** Give the shortest causal chain. Remove details that interrupt it.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL], [OSDI-CFP], [SOSP-CFP], [FIVE-VENUE-CORPUS].

## SS-15 — Background gives only prerequisites

- **Nature:** General best practice.
- **Reviewer attack:** “Background is a textbook survey, duplicates related work, or hides the paper's own contribution.”
- **Check:** For each background item, find a subsequent dependency. Do a check of differences between neutral prerequisites, motivation, criticism, and new design.
- **Severity:** `S2`. `S1` if contribution ownership becomes ambiguous.
- **Exceptions / false positives:** Interdisciplinary audiences can make more background necessary. Give it at the level of its subsequent use.
- **Repair direction:** Remove unused background. Put comparisons in motivation or related work. Give original content clear attribution.
- **Sources:** [SYSTEMS-GUIDE], [ERNST], [LEVIN-REDELL].

## SS-16 — Motivation makes prior limitations causal and fair

- **Nature:** Condition for accuracy plus general best practice.
- **Reviewer attack:** “The motivation attacks weak caricatures or lists symptoms without showing why existing designs fundamentally miss the new requirement.”
- **Check:** First, give the bridge its class from the [interface-boundary contract](../../systems-paper-revise/references/interface-boundaries.md). For a negative gap, examine fair difference → shared root cause or constraint → unmet property → new insight. Get evidence about the named work. For a different question, make sure that its design-space map is parallel and its question is bounded. Do not invent shared failure or novelty. Do the comparison-organization, causal-strength, and external checks independently.

  Missing antecedents or source access change evidence status. They do not cancel local bridge inspection. If authorized, do external checks.
- **Severity:** `S1`. `S0` for false positioning that changes conclusions.
- **Exceptions / false positives:** Empirical motivation can be a measurement study. Causal language still makes evidence necessary.
- **Repair direction:** Use accurate categories, accurate limitations, and bounded claims. Remove strawmen.
- **Sources:** [SYSTEMS-GUIDE], [LEVIN-REDELL], [OSDI-CFP].

## SS-17 — Overview gives model and workflow without replacing design

- **Nature:** General best practice.
- **Reviewer attack:** “I cannot tell assumptions, inputs/outputs, major stages, or where the contribution lies,” or “the design section later repeats the same boxes.”
- **Check:** Find the system model, deployment context, high-level workflow, interfaces, primary insights or challenges, and scope. Keep detailed mechanisms and rationale for design.
- **Severity:** `S1` when model/workflow is unrecoverable. `S2` for abstraction imbalance.
- **Exceptions / false positives:** An Overview section is optional when introduction or design gives its functions.
- **Repair direction:** Give a short model and workflow. Give their relations to subsequent sections. Remove unnecessary detail before those relations.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE].

## SS-18 — Design gives causes and operation

- **Nature:** Condition for technical completeness for a design contribution.
- **Reviewer attack:** “The design section restates goals and boxes but omits algorithm, state, lifecycle, edge cases, and design choices.”
- **Check:** For each stage, apply `TS` rules. Examine objective, constraint, input, state, operation, output, start, stop, alternatives, tradeoffs, invariant, failures, edge cases, and overview-challenge relation.
- **Severity:** `S1`. `S0` for a fatal hidden gap.
- **Exceptions / false positives:** Citations can give standard mechanisms without new derivations. Adaptations must have explanations.
- **Repair direction:** Give causal and operational detail. Give rationale. Use pseudocode or figures where clearer. Remove repeated overview prose.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL].

## SS-19 — Implementation and intellectual design have different roles

- **Nature:** General best practice. Condition for accuracy in status claims.
- **Reviewer attack:** “I cannot tell what was actually built, what was borrowed, and which engineering detail is necessary for the reported result.”
- **Check:** Find codebase and version, reused components, primary engineering choices, incomplete or stubbed parts, and design differences. Examine languages and LOC with context. Find implementation inventories without consequences.
- **Severity:** `S1` for maturity mismatch. `S2` for unclear detail.
- **Exceptions / false positives:** Some venues or papers put implementation inside design.
- **Repair direction:** Give implementation boundaries and consequential realization details. Remove counts without an argument function.
- **Sources:** [LEVIN-REDELL], [USER-NOTES], [NSDI-ARTIFACT].

## SS-20 — Evaluation evidence answers recoverable questions

- **Nature:** Condition for evidence organization.
- **Reviewer attack:** “The paper lists setup and plots but never says which contribution each experiment validates or what answer follows.”
- **Check:** Find each experiment, proof, case study, or production observation's question. Headings, prose, or interleaved finding/intervention sequences can give it. Examine reproducible setup, baseline and workload rationale, claim-evidence relations, results, interpretation, mechanism explanations, and limitations. For finished papers, find `must be evaluated`, `remains to be tested`, or equivalents in place of available answers. Record result placeholders. For clear proposals or roadmaps, keep planned status.

  Treat general manuscript-review requests as research-paper context unless proposal or plan status is clear. If lifecycle stays ambiguous, give the finished-paper placeholder risk conditionally. Give the author a manuscript-state question. Caution alone does not show a pass. Use the selected archetype without a universal single-section requirement.
- **Severity:** `S1` when claim coverage is missing. `S2` for organization.
- **Exceptions / false positives:** Numbered questions are optional. Operations and measurement papers can interleave method, observation, intervention, and validation with auditable inferences.
- **Repair direction:** Organize by claims or questions. Give answers with uncertainty. Give causes only with evidence.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [SIGPLAN-EMPIRICAL], [FIVE-VENUE-CORPUS].

## SS-21 — Related work gives similarities and differences

- **Nature:** General best practice. Citation completeness is factual.
- **Reviewer attack:** “The section is a bibliography dump or hides the closest comparison among broad categories.”
- **Check:** Put work in groups by dimensions related to the decision. Examine representative and closest citations. Give fair similarities and differences. Examine contribution relations without repeated motivation. For a negative gap, get its shared assumption, mechanism, or constraint. Different boundaries alone are insufficient.

  For a different question from a parallel map, keep negative-gap invention outside the review. Examine novelty in different checks. For each factual or negative claim, examine its literature evidence in a different check from organization.
- **Severity:** `S1` for missing/false closest-work positioning. `S2` for organization.
- **Exceptions / false positives:** Chronology can be necessary for system-evolution studies or surveys. Use it only for an argument function.
- **Repair direction:** Organize by mechanism, assumption, or capability. Give accurate comparisons.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [ERNST].

## SS-22 — Discussion and limitations give accurate boundaries

- **Nature:** Condition for accuracy for conclusions. Section itself optional.
- **Reviewer attack:** “The paper buries adoption costs, unsupported environments, ethical/security risks, or threats to validity.”
- **Check:** Compare tradeoffs, failures, generality, deployment constraints, and evaluation validity with headline claims. Do not use future work as implemented capabilities. If a boundary narrows a central broad-reader claim, make short disclosure before the full discussion necessary. Detailed discussion can occur subsequently.

  For an isolated limitation paragraph, report both the conditional early disclosure and the option for detailed discussion later.
  Give this judgment even without a placement request.
  Keep specified wording, duplication, and Introduction placement not assessable when that context is unavailable.
  Keep the paragraph unchanged without restructuring authority.
- **Severity:** `S1`. `S0` if hidden limitation negates central claim.
- **Exceptions / false positives:** Limitations can occur throughout the paper without a dedicated section.
- **Repair direction:** Give boundaries that affect conclusions and consequences. Keep implemented mitigations and future work in different classes.
- **Sources:** [OSDI-CFP], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL].

## SS-23 — Conclusion closes the established argument without adding claims

- **Nature:** Condition for internal consistency.
- **Reviewer attack:** “The conclusion introduces a stronger property, application, or generalization than the paper established.”
- **Check:** Give each conclusion statement its contribution and evidence relation. Make sure that the conclusion gives the supported insight or lesson. A system name and best number alone are insufficient.
- **Severity:** `S1` for new/overbroad central claim. `S2` for weak synthesis.
- **Exceptions / false positives:** A short implication can be inferential with a clear label and source basis.
- **Repair direction:** Remove or narrow new claims. Give supported lessons and conditions.
- **Sources:** [ERNST], [LEVIN-REDELL], [OSDI-CFP].

## SS-24 — Appendix and supplement are not required to rescue the primary argument

- **Nature:** Venue-specific plus general best practice.
- **Reviewer attack:** “The main paper is unintelligible or unsupported unless optional/nonreviewed material is read.”
- **Check:** Examine appendix and supplement rules in effect. Make sure that the required paper gives the central problem, mechanism, evidence, and limitations. Supplements add detail or reproduction without replacement of missing foundational logic.
- **Severity:** `S0` for verified noncompliance. `S1` for a primary-paper dependency.
- **Exceptions / false positives:** Supplementary proofs, extended results, and artifact instructions can have official permission.
- **Repair direction:** Put necessary content in the required paper or narrow claims. Examine rules in effect online.
- **Sources:** Current venue instructions. [SYSTEMS-GUIDE]. Online verification is necessary.

## Structure audit outputs

For argument-bearing scope, make the argument-spine map. Give its state in the visible coverage ledger. Scope can include a full paper, introduction, abstract, or another argument-bearing object. For local Review, integrate the map fields into their owning rows under the shared coverage contract's compact-ledger rule.

### Argument-spine map

| Unit | Problem/consequence | Root constraint | Insight/principle | Realization | Evidence/implication | Break |
|---|---|---|---|---|---|---|

For multiple prose paragraphs or structure scope, make the paragraph-envelope map. `Status` gives opening-to-development agreement and the ending's completion or transfer of that obligation.

The shared paragraph ledger also gives delivered role, convention, sentence roles, neighbor relation, and finding IDs. Keep those fields with the envelope fields. For local Review, show them once in the owning paragraph row.

### Paragraph-envelope map

| Paragraph | Opening promise | Closing payoff/handoff | Status |
|---|---|---|---|

For a full paper, also make these two maps:

### Promise map

| Promise location | Promise | Delivery location | Evidence location | Status |
|---|---|---|---|---|

### Dependency map

| First use | Required concept/model/result | Defined where | Retrieval cost | Problem |
|---|---|---|---|---|

For missing excerpt context, use `not assessable — needs context`. Keep map-filling searches within scope.
