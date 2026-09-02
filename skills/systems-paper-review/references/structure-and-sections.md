# Structure, Narrative, and Section Contracts

Systems papers are read linearly under limited attention. Each unit should make a promise, supply the information needed to understand it, and prepare the next inference. This does not require one universal section template; apply the contract that fits the paper type and venue.

## Global narrative rules

## SS-01 — The paper has one recoverable argument chain

- **Nature:** General best practice.
- **Reviewer attack:** “The sections are individually plausible but never form a coherent case for the contribution.”
- **Check:** Reconstruct: setting → problem → why existing approaches fail/root cause → insight → challenges → design → implementation status → evaluation questions/results → bounded conclusion. Mark missing or circular links.
- **Severity:** `S1` for a broken central chain; `S2` for costly ordering.
- **Exceptions / false positives:** Measurement, experience, negative-result, theory, and dataset papers use different chains; require coherence, not this exact template.
- **Repair direction:** Reorder around causal dependencies, add missing premise/inference, or narrow promises.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL]. Checked 2026-09-01.

## SS-02 — Concepts appear before they are required

- **Nature:** General best practice.
- **Reviewer attack:** “A key term, assumption, metric, component, or result is used before I know what it means.”
- **Check:** Track first semantic use, not only first textual occurrence. Identify forward references, delayed definitions, unexplained acronyms, and definitions separated far from use without retrieval support.
- **Severity:** `S2`; `S1` when misunderstanding changes a central claim; `S3` locally.
- **Exceptions / false positives:** A brief intuitive preview may precede a formal definition if clearly signposted.
- **Repair direction:** Move or add a minimal local definition, defer the use, or add a precise pointer.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## SS-03 — Introduced concepts earn their cognitive cost

- **Nature:** General best practice.
- **Reviewer attack:** “The paper introduces terminology, notation, modules, or distinctions that are never used or could be expressed directly.”
- **Check:** For each named concept, find later analytical/design use. Flag synonyms masquerading as new terms and definitions that recursively introduce more undefined terms.
- **Severity:** `S2`; `S3` for isolated excess.
- **Exceptions / false positives:** A term can support precise discussion even if used only a few times; judge necessity.
- **Repair direction:** Remove/inline it, combine terms, or use it consistently in later reasoning.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## SS-04 — Section promises match delivered content

- **Nature:** Hard internal-consistency condition.
- **Reviewer attack:** “The heading/opening promises a model, design, proof, or answer that the section does not provide.”
- **Check:** Compare heading and opening roadmap with subsections, figures, and closing synthesis. Check that each evaluation question receives an answer.
- **Severity:** `S1` for a central broken promise; `S2` otherwise.
- **Exceptions / false positives:** A short transition need not recap every detail.
- **Repair direction:** Supply promised content, change the promise/heading, or move unrelated content.
- **Sources:** [SYSTEMS-GUIDE], [ERNST], [JENSEN-SYSTEMS-SKILL]. Checked 2026-09-01.

## SS-05 — Cross-section references reduce retrieval cost

- **Nature:** General best practice; mechanical frequency is a house-style choice.
- **Reviewer attack:** “The text relies on an earlier definition/design detail, but the reader cannot efficiently locate it.”
- **Check:** Identify dependencies separated by significant distance or ambiguous names. Verify pointers target the exact definition, mechanism, or figure. Do not demand a reference every time a term repeats.
- **Severity:** `S2` when reasoning depends on retrieval; `S3` otherwise.
- **Exceptions / false positives:** Recently introduced, memorable, or standard concepts need no repetitive pointer.
- **Repair direction:** Add a short reminder plus precise section/figure reference; avoid sending readers backward for basic comprehension repeatedly.
- **Sources:** [USER-NOTES] as normalized, [ERNST]. Checked 2026-09-01.

## SS-06 — Detail appears at the right abstraction level

- **Nature:** General best practice.
- **Reviewer attack:** “The overview is buried in implementation minutiae, while the design section merely repeats the overview.”
- **Check:** Classify material as motivation, model, high-level workflow, design rationale/mechanism, implementation realization, or evaluation. Look for premature detail and repeated shallow descriptions.
- **Severity:** `S2`; `S1` if mechanism remains absent.
- **Exceptions / false positives:** A crucial low-level constraint may need early mention to make the problem intelligible.
- **Repair direction:** Move detail to the layer where it supports a decision; keep short forward pointers.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL]. Checked 2026-09-01.

## Paragraph and list rules

## SS-07 — Each paragraph advances one local claim

- **Nature:** General best practice.
- **Reviewer attack:** “The paragraph mixes background, design, results, caveats, and unrelated claims, so its point is unstable.”
- **Check:** Write the paragraph's claim in one sentence; test whether every sentence explains, supports, qualifies, or transitions from that claim. Flag multiple independent centers.
- **Severity:** `S2`; `S1` if mixed logic hides a contradiction; `S3` locally.
- **Exceptions / false positives:** A short bridge paragraph may connect two ideas; the relationship should be explicit.
- **Repair direction:** Split by claim, reorder evidence, or revise the topic sentence.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## SS-08 — Sentence order follows information and causal dependencies

- **Nature:** General best practice.
- **Reviewer attack:** “I must infer why a sentence follows the previous one or reinterpret earlier sentences after learning a missing premise.”
- **Check:** For each transition, name its relation: elaboration, evidence, cause, consequence, contrast, condition, example, limitation, or handoff. Verify old/given information anchors new information and prerequisites precede consequences.
- **Severity:** `S2`; `S3` for one rough transition.
- **Exceptions / false positives:** Repetition of an exact word is not required; conceptual continuity is.
- **Repair direction:** Reorder, add the missing relation, use an explicit transition only when the logic is not already obvious.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## SS-09 — Topic sentences are informative, not overloaded

- **Nature:** General best practice.
- **Reviewer attack:** “The paragraph begins with a long inventory or vague metacommentary instead of its decision-relevant point.”
- **Check:** Determine whether the first sentence states the local claim at the right level and leaves support/details to follow. Flag `This section discusses...` when a substantive claim is available.
- **Severity:** `S2` for recurring issue; `S3` locally.
- **Exceptions / false positives:** Not every paragraph must use a rigid topic-sentence-first form, especially mathematical derivations or tightly connected continuations.
- **Repair direction:** Lead with the claim or relation, then supply mechanism/evidence/qualification.
- **Sources:** [USER-NOTES], [ERNST]. Checked 2026-09-01.

## SS-10 — Paragraph length follows reasoning, not rendered line count

- **Nature:** Diagnostic heuristic / house style.
- **Reviewer attack:** “The paragraph is too dense to parse or so fragmented that the argument loses momentum.”
- **Check:** Look for multiple claims, excessive sentence count, hidden transitions, one-sentence fragments, and visual density in the rendered format. Do not use ten lines as a universal threshold.
- **Severity:** `S2` when logic is obscured; `S3` or `S4` for layout only.
- **Exceptions / false positives:** Necessary proof/algorithm exposition can be longer; short transition paragraphs can be valid.
- **Repair direction:** Split at a logical boundary, merge fragments, or improve internal signaling.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## SS-11 — Lists are parallel and introduced by a governing claim

- **Nature:** General best practice.
- **Reviewer attack:** “The bullets mix contributions, mechanisms, benefits, and results, or their relationship to the lead-in is unclear.”
- **Check:** Verify grammatical and conceptual parallelism, non-overlap, meaningful order, complete lead-in, and consistent granularity. Each long bullet should surface its point early.
- **Severity:** `S2`; `S3` for surface parallelism.
- **Exceptions / false positives:** Short label/value lists need no full topic sentence in every item.
- **Repair direction:** Choose one organizing dimension, rewrite lead-in, merge/split items, and align syntax.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## Section contracts

## SS-12 — Title is specific, accurate, and searchable

- **Nature:** General best practice plus venue formatting rules.
- **Reviewer attack:** “The title overclaims, hides the systems contribution, or could describe many unrelated papers.”
- **Check:** Compare title with actual problem, contribution type, domain, and claim boundary. Check unexplained acronym, marketing language, and superlative.
- **Severity:** `S2`; `S1` for material misrepresentation; venue violations follow `VO` severity.
- **Exceptions / false positives:** Memorable system names are acceptable when paired with an informative subtitle/title phrase.
- **Repair direction:** Name the distinctive systems idea/problem and bound scope.
- **Sources:** [ERNST], [LEVIN-REDELL], current venue rules. Checked 2026-09-01.

## SS-13 — Abstract is a faithful miniature argument

- **Nature:** General best practice; word/format limits are venue-specific.
- **Reviewer attack:** “After the abstract I still do not know the problem, gap, idea, implementation/evidence, or magnitude and boundary of results.”
- **Check:** Find: context/problem and consequence; failure of prior approach or root cause where needed; central idea/mechanism; concrete deliverable; evidence and key bounded result; implication. Cross-check every number and superlative with paper evidence when in scope.
- **Severity:** `S1` for missing/misleading central case; `S2` for imbalance.
- **Exceptions / false positives:** Do not enforce a fixed five-sentence formula; adapt to contribution type and venue.
- **Repair direction:** Replace background/detail with the missing contribution element and calibrate results.
- **Sources:** [SYSTEMS-GUIDE], [ERNST], [OSDI-CFP]. Checked 2026-09-01.

## SS-14 — Introduction establishes the complete decision case

- **Nature:** General best practice.
- **Reviewer attack:** “The introduction states a solution before establishing the problem/root cause/challenge, or promises novelty and results without a coherent path.”
- **Check:** Recover problem and significance, prior limitation, root cause or unmet constraint, insight, technical challenges, high-level solution, evaluated evidence, contributions, and scope. Verify challenge has substantive content and is not just implementation labor.
- **Severity:** `S1`; `S2` for local flow.
- **Exceptions / false positives:** Order and paragraph count are flexible. Closely related concepts can be combined; some paper types need no “root cause.”
- **Repair direction:** Restore the shortest causal chain and eliminate details that interrupt it.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL]. Checked 2026-09-01.

## SS-15 — Background teaches only prerequisites

- **Nature:** General best practice.
- **Reviewer attack:** “Background is a textbook survey, duplicates related work, or hides the paper's own contribution.”
- **Check:** For each background item, find a later dependency. Separate neutral prerequisite from motivation/critique and from novel design.
- **Severity:** `S2`; `S1` if contribution ownership becomes ambiguous.
- **Exceptions / false positives:** An interdisciplinary audience may need more background; explain it at the level used later.
- **Repair direction:** Remove unused exposition, move comparisons to motivation/related work, and mark original content.
- **Sources:** [SYSTEMS-GUIDE], [ERNST], [LEVIN-REDELL]. Checked 2026-09-01.

## SS-16 — Motivation makes prior limitations causal and fair

- **Nature:** Hard accuracy condition plus general best practice.
- **Reviewer attack:** “The motivation attacks weak caricatures or lists symptoms without showing why existing designs fundamentally miss the new requirement.”
- **Check:** Group prior approaches by relevant mechanism/assumption, cite representative/closest works, connect limitation → root cause/constraint → new insight. Verify externally when permitted.
- **Severity:** `S1`; `S0` for materially false positioning.
- **Exceptions / false positives:** Empirical motivation can be a measurement study; causal language still needs evidence.
- **Repair direction:** Use accurate categories, precise limitations, and bounded claims; remove strawmen.
- **Sources:** [SYSTEMS-GUIDE], [LEVIN-REDELL], [OSDI-CFP]. Checked 2026-09-01.

## SS-17 — Overview defines model and workflow without replacing design

- **Nature:** General best practice.
- **Reviewer attack:** “I cannot tell assumptions, inputs/outputs, major stages, or where the contribution lies,” or “the design section later repeats the same boxes.”
- **Check:** Look for system model, deployment context, high-level workflow, interfaces, major insights/challenges, and scope. Ensure mechanism details and rationale remain for design.
- **Severity:** `S1` when model/workflow is unrecoverable; `S2` for abstraction imbalance.
- **Exceptions / false positives:** A separate overview is optional if introduction/design already provide these functions clearly.
- **Repair direction:** Add a compact model/workflow and map later sections; remove premature detail.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE]. Checked 2026-09-01.

## SS-18 — Design explains why and how, not just what

- **Nature:** Hard technical-completeness condition for a design contribution.
- **Reviewer attack:** “The design section restates goals and boxes but omits algorithm, state, lifecycle, edge cases, and design choices.”
- **Check:** Apply `TS` rules to each major stage: objective/constraint, input/state, operation, output, start/stop, alternatives/tradeoff, invariant, failure/edge behavior, and link to overview challenge.
- **Severity:** `S1`; `S0` for a fatal hidden gap.
- **Exceptions / false positives:** Standard mechanisms may be cited rather than rederived; adaptations must be explained.
- **Repair direction:** Add causal/operational detail and rationale, use pseudocode/figure when clearer, remove repetitive overview prose.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL]. Checked 2026-09-01.

## SS-19 — Implementation separates realization from intellectual design

- **Nature:** General best practice; hard accuracy for status claims.
- **Reviewer attack:** “I cannot tell what was actually built, what was borrowed, and which engineering detail is necessary for the reported result.”
- **Check:** Identify codebase/version, languages/LOC only with context, reused components, major engineering choices, incomplete/stubbed parts, and deviations from design. Avoid implementation inventory without consequence.
- **Severity:** `S1` for maturity mismatch; `S2` for unclear detail.
- **Exceptions / false positives:** Some venues/papers integrate implementation into design.
- **Repair direction:** State implementation boundary and decision-relevant realization details; remove vanity counts.
- **Sources:** [LEVIN-REDELL], [USER-NOTES], [NSDI-ARTIFACT]. Checked 2026-09-01.

## SS-20 — Evaluation section answers explicit questions

- **Nature:** Hard evidence-organization condition.
- **Reviewer attack:** “The section lists setup and plots but never says which contribution each experiment validates or what answer follows.”
- **Check:** Look for reproducible setup, baseline/workload rationale, research questions, experiment-to-claim mapping, result plus interpretation, design reference for mechanism explanations, and limitations.
- **Severity:** `S1` when claim coverage is missing; `S2` for organization.
- **Exceptions / false positives:** Questions may be signaled in prose rather than enumerated mechanically.
- **Repair direction:** Organize by claim/question, state answer with uncertainty, and connect cause only when supported.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [SIGPLAN-EMPIRICAL]. Checked 2026-09-01.

## SS-21 — Related work distinguishes rather than enumerates

- **Nature:** General best practice; citation completeness is factual.
- **Reviewer attack:** “The section is a bibliography dump or hides the closest comparison among broad categories.”
- **Check:** Group by decision-relevant dimensions, cite accurate representative and closest work, state fair similarities/differences, and connect to contribution without repeating motivation.
- **Severity:** `S1` for missing/false closest-work positioning; `S2` for organization.
- **Exceptions / false positives:** Historical or survey contributions may need chronology; use it only when chronology advances the argument.
- **Repair direction:** Reorganize by mechanism/assumption/capability and add precise comparison.
- **Sources:** [LEVIN-REDELL], [SYSTEMS-GUIDE], [ERNST]. Checked 2026-09-01.

## SS-22 — Discussion and limitations interpret boundaries honestly

- **Nature:** Hard accuracy condition for conclusions; section itself optional.
- **Reviewer attack:** “The paper buries adoption costs, unsupported environments, ethical/security risks, or threats to validity.”
- **Check:** Compare unresolved tradeoffs, failure modes, generality, deployment constraints, and evaluation validity with headline claims. Check future work is not described as current support.
- **Severity:** `S1`; `S0` if hidden limitation negates central claim.
- **Exceptions / false positives:** Limitations may appear throughout rather than in a dedicated section.
- **Repair direction:** State material boundaries and consequences; separate mitigation already implemented from future work.
- **Sources:** [OSDI-CFP], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL]. Checked 2026-09-01.

## SS-23 — Conclusion closes the established argument without adding claims

- **Nature:** Hard internal-consistency condition.
- **Reviewer attack:** “The conclusion introduces a stronger property, application, or generalization than the paper established.”
- **Check:** Map each conclusion statement to a stated contribution and evidence. Ensure takeaway names the supported insight/lesson, not only system name and best number.
- **Severity:** `S1` for new/overbroad central claim; `S2` for weak synthesis.
- **Exceptions / false positives:** A concise implication can be inferential if clearly labeled and grounded.
- **Repair direction:** Remove/narrow new claims and synthesize supported lessons and conditions.
- **Sources:** [ERNST], [LEVIN-REDELL], [OSDI-CFP]. Checked 2026-09-01.

## SS-24 — Appendix and supplement are not required to rescue the main argument

- **Nature:** Venue-specific plus general best practice.
- **Reviewer attack:** “The main paper is unintelligible or unsupported unless optional/nonreviewed material is read.”
- **Check:** Verify current venue treatment of appendices/supplements. Ensure central problem, mechanism, evidence, and limitations stand in the required paper; supplement adds depth/reproduction rather than foundational missing logic.
- **Severity:** `S0` for verified noncompliance; `S1` for a main-paper dependency.
- **Exceptions / false positives:** Formal proofs, extended results, and artifact instructions may appropriately be supplementary when official rules allow.
- **Repair direction:** Move essential content into the main paper or narrow claims; verify live rules.
- **Sources:** Current venue instructions; [SYSTEMS-GUIDE]. Live verification required.

## Structure audit outputs

For a full paper, produce two internal maps:

### Promise map

| Promise location | Promise | Delivery location | Evidence location | Status |
|---|---|---|---|---|

### Dependency map

| First use | Required concept/model/result | Defined where | Retrieval cost | Problem |
|---|---|---|---|---|

For a scoped excerpt, do not search outside scope to fill these maps; use `not assessable — needs context`.

