# Prose, Terminology, and Language Precision

Apply these rules after argument and evidence. Surface polish cannot repair an unsupported claim. Review English, Chinese, or deliberately mixed text in its source language; do not translate unless requested.

## Terminology and claim language

## PT-01 — Nonstandard terms are defined for the intended reader

- **Nature:** General best practice.
- **Reviewer attack:** “A non-specialist systems reviewer cannot recover the paper's meaning without importing subfield-specific knowledge.”
- **Check:** At first substantive use, inspect acronyms, coined names, overloaded common words, metrics, roles, and domain terms. A definition should state the differentiating meaning without recursively introducing unexplained terms.
- **Severity:** `S2`; `S1` if a central claim becomes ambiguous; `S3` locally.
- **Exceptions / false positives:** Widely standard terms for the target audience need no textbook definition; an intuitive use may precede a precise formalization if signposted.
- **Repair direction:** Add a minimal local definition, example, or contrast; avoid definition chains.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-02 — One concept has one stable name

- **Nature:** Hard internal-consistency condition when names alter meaning; otherwise best practice.
- **Reviewer attack:** “I cannot tell whether two labels denote the same mechanism or different ones.”
- **Check:** Track system name, component, actor, stage, metric, property, dataset, and baseline aliases. Distinguish deliberate hierarchy from accidental synonym rotation.
- **Severity:** `S1` if technical identity is unclear; `S2` recurring; `S3` isolated.
- **Exceptions / false positives:** Synonyms can improve ordinary prose, but technical terms should remain stable. Do not vary a precise term merely to avoid repetition.
- **Repair direction:** Select a canonical term and explicitly define any hierarchy/alias.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-03 — Paired and categorical terms use symmetric dimensions

- **Nature:** Hard precision condition.
- **Reviewer attack:** “The categories compare different dimensions—such as offline versus runtime—so the partition is neither exhaustive nor interpretable.”
- **Check:** Test pairs/sets for a common axis, mutual exclusivity where claimed, coverage, and consistent granularity: online/offline, static/dynamic, local/remote, trusted/untrusted, etc.
- **Severity:** `S2`; `S1` when taxonomy supports novelty or evaluation.
- **Exceptions / false positives:** Natural systems categories may overlap; state that they are examples or independent dimensions.
- **Repair direction:** Rename by one dimension, use a two-dimensional taxonomy, or remove false opposition.
- **Sources:** [USER-NOTES], [ERNST]. Checked 2026-09-01.

## PT-04 — Acronyms and abbreviations follow actual conventions

- **Nature:** General best practice; venue/style specifics vary.
- **Reviewer attack:** “The paper invents or punctuates abbreviations inconsistently, increasing ambiguity.”
- **Check:** Define nonstandard acronyms once; use official abbreviations; preserve capitalization; distinguish abbreviations (`Fig.`) from initialisms (`CPU`). Do not require periods universally.
- **Severity:** `S2` for ambiguity/inconsistency; `S3` surface; venue violation per overlay.
- **Exceptions / false positives:** Well-known audience acronyms may be used without expansion if venue style permits. Avoid defining an acronym used only once or twice.
- **Repair direction:** Use the official/full term, define once, and standardize.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## PT-05 — Quantifiers are bounded and auditable

- **Nature:** Hard accuracy condition.
- **Reviewer attack:** “Words such as `some`, `several`, `various`, `many`, `most`, or Chinese equivalents hide an unsupported population or quantity.”
- **Check:** Ask whether the quantity matters to the inference. Identify population, numerator/denominator, range, or representative examples. Do not mechanically replace every indefinite quantifier with a number.
- **Severity:** `S1` for a claim-driving ambiguity; `S2` otherwise; `S3` if harmless.
- **Exceptions / false positives:** Indefinite quantifiers are valid when exact count is unknown/irrelevant and no stronger inference follows.
- **Repair direction:** Provide measured quantity/range, name examples, bound the population, or delete the unnecessary quantifier.
- **Sources:** [USER-NOTES], [ERNST], [BRANDON-EVIDENCE]. Checked 2026-09-01.

## PT-06 — Epistemic strength matches evidence

- **Nature:** Hard accuracy condition.
- **Reviewer attack:** “The authors claim to ensure/determine/prove when they only observe, or hedge a conclusion that their evidence directly establishes.”
- **Check:** Calibrate `show`, `demonstrate`, `establish`, `prove`, `ensure`, `guarantee`, `suggest`, `indicate`, `may`, `assume`, `believe`, `hope`, and Chinese equivalents against evidence type and scope.
- **Severity:** `S0`/`S1` for unsupported guarantee or proof; `S2` for recurring miscalibration.
- **Exceptions / false positives:** `We assume` is correct when declaring a model assumption; it is not weak wording to delete. Appropriate uncertainty is scientific precision.
- **Repair direction:** Change verb/quantifier, state evidence and conditions, or add the missing validation.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [SIGPLAN-EMPIRICAL]. Checked 2026-09-01.

## PT-07 — Loaded adjectives and emotional adverbs have evidence or are removed

- **Nature:** General best practice.
- **Reviewer attack:** “Marketing or emotional language substitutes for measured importance or surprise.”
- **Check:** Inspect `novel`, `simple`, `easy`, `efficient`, `significant`, `dramatic`, `surprising`, `unfortunately`, `overwhelmingly`, and equivalents. Ask what metric or comparison supplies content.
- **Severity:** `S2` if it overstates a scientific claim; `S3` style.
- **Exceptions / false positives:** `Surprisingly` can signal a result that contradicts an explicit hypothesis, and `significant` can be statistically defined; state why.
- **Repair direction:** Replace with the measured property or remove.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-08 — Numbers include scale, comparator, and appropriate precision

- **Nature:** Hard interpretability condition for decision-relevant values.
- **Reviewer attack:** “A number is presented without saying whether it is large, small, costly, or meaningful, or with precision unsupported by measurement.”
- **Check:** For each nontrivial value, identify unit, baseline/denominator, variability/tolerance, practical threshold, and consistent significant digits. Do not require commentary for identifiers, counts obvious from context, or routine constants.
- **Severity:** `S1` for a misleading headline number; `S2` for missing context; `S3` for rounding inconsistency.
- **Exceptions / false positives:** Exact integer facts and parameter settings may need no “large/small” interpretation.
- **Repair direction:** Add comparator/absolute value/range and reduce false precision; preserve raw evidence.
- **Sources:** [USER-NOTES] as normalized, [SIGPLAN-EMPIRICAL], [HEISER-BENCH]. Checked 2026-09-01.

## PT-09 — Units and notation are semantically and typographically consistent

- **Nature:** Hard correctness condition plus template preference.
- **Reviewer attack:** “Values cannot be compared because units, prefixes, capitalization, or spacing change.”
- **Check:** Verify SI/binary prefixes, bit/byte, time/rate, percent/percentage points, unit conversion, pluralization, and math/text notation. In LaTeX, `~` is a nonbreaking space—not a visible tilde—and may be correct depending on macro/template.
- **Severity:** `S1` for numerical meaning error; `S2` recurring ambiguity; `S3` typography.
- **Exceptions / false positives:** Follow field/venue convention for spaces between number and unit; do not ban `~` universally.
- **Repair direction:** Choose canonical units/macros, convert accurately, and apply consistent spacing.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## PT-10 — `e.g.` and `i.e.` retain distinct meanings

- **Nature:** Hard semantic condition.
- **Reviewer attack:** “An example is presented as an exhaustive restatement, or a definition as one optional example.”
- **Check:** `e.g.` introduces nonexhaustive examples; `i.e.` restates/equates. Inspect punctuation under venue/language style and whether the surrounding logic matches.
- **Severity:** `S2` if scope changes; `S3` otherwise.
- **Exceptions / false positives:** Plain `for example` or `that is` may be clearer, especially in Chinese/English mixed prose.
- **Repair direction:** Select the correct relation or write it explicitly.
- **Sources:** [USER-NOTES], [ERNST]. Checked 2026-09-01.

## PT-10A — High-level wording remains specific and discriminating

- **Nature:** General systems-writing principle with claim-precision consequences.
- **Reviewer attack:** “The prose sounds abstract, but it could describe almost any system and does not explain why this design follows.”
- **Check:** Reduce the sentence to its claimed relation. A useful high-level statement names the exact constraint or failed assumption, the leverage or change, and the resulting property or tradeoff. Apply three tests: substitute unrelated system/component names and see whether the sentence remains equally true; ask whether it predicts the need for the major mechanism or study choice; identify the condition and boundary of what follows. Flag bare claims that a system `supports`, `enables`, `addresses`, `improves`, `decouples`, or `virtualizes` without precise objects and consequences.
- **Severity:** `S1` when the central idea or design derivation is unrecoverable; `S2` when a paragraph loses specificity; `S3` for one vague sentence.
- **Exceptions / false positives:** A short roadmap may remain broad when adjacent text immediately supplies the discriminating relation. A technical term may compactly encode a previously defined relation.
- **Repair direction:** State the shortest exact constraint → change → consequence relation, then place mechanism names and operations below it. Do not replace concrete detail with generic abstraction.
- **Sources:** [USER-NOTES], [OSDI-SOSP-CORPUS], [OSDI-BEST-SAMPLE], [SOSP-BEST-SAMPLE]. Checked 2026-09-03.

## Sentence logic and grammar

## PT-11 — Every sentence has one recoverable proposition structure

- **Nature:** Hard readability/grammar condition.
- **Reviewer attack:** “I cannot determine actor, action, object, condition, contrast, or main assertion.”
- **Check:** Locate the main clause and logical operators. Flag fragments, run-ons, overloaded embeddings, ambiguous coordination, missing subjects/verbs, and clauses whose relationship must be guessed.
- **Severity:** `S1` if a central technical statement has multiple readings; `S2` recurring; `S3` local grammar.
- **Exceptions / false positives:** Long sentences are not defects by length alone; complex structure is justified when it mirrors a precise relationship clearly.
- **Repair direction:** Split by proposition, restore explicit actor/relation, or reorder main claim before qualifications.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-12 — Modifiers have unambiguous attachment and scope

- **Nature:** Hard semantic condition.
- **Reviewer attack:** “`which`, an adverb, prepositional phrase, participle, or relative clause can modify more than one candidate.”
- **Check:** Test proximity and meaning for each modifier; inspect misplaced `only`, `also`, `respectively`, negation, and dangling participles. The nearest-noun idea is a clarity heuristic, not a universal grammar law.
- **Severity:** `S1` if technical meaning changes; `S2`/`S3` otherwise.
- **Exceptions / false positives:** Grammar and semantics can unambiguously select a non-nearest antecedent; do not flag proximity alone.
- **Repair direction:** Move modifier, name antecedent, repeat noun, or split sentence.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-13 — Pronouns and demonstratives have unique antecedents

- **Nature:** Hard clarity condition.
- **Reviewer attack:** “`it`, `this`, `that`, `they`, `these results`, or a Chinese zero pronoun could refer to multiple mechanisms or findings.”
- **Check:** Resolve every pronoun/demonstrative locally. Flag vague `This shows...` when the referenced observation/inference is unclear.
- **Severity:** `S1` if claim meaning changes; `S2`/`S3` otherwise.
- **Exceptions / false positives:** Immediate singular antecedents need no noun repetition.
- **Repair direction:** Replace with a precise noun phrase or state the proposition being referenced.
- **Sources:** [ERNST], [HEISER-STYLE], [USER-NOTES]. Checked 2026-09-01.

## PT-14 — Articles, countability, number, and agreement are correct in English

- **Nature:** Hard grammar condition.
- **Reviewer attack:** “Frequent article/count/agreement errors reduce confidence and sometimes change whether a class or instance is meant.”
- **Check:** Inspect singular count nouns, generic/definite reference, mass nouns, subject–verb agreement, pronoun agreement, and `data`/collective usage under chosen style.
- **Severity:** `S2` if recurring/ambiguous; `S3` local.
- **Exceptions / false positives:** Not every bare noun is wrong; mass, plural generic, proper, and attributive nouns are valid.
- **Repair direction:** Add/remove article, pluralize, or choose the correct mass/count construction without changing referent.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-15 — Coordination and parallelism preserve category and scope

- **Nature:** Hard semantic/grammar condition.
- **Reviewer attack:** “A list combines unlike grammatical or conceptual units, so operators and comparisons have uncertain scope.”
- **Check:** Examine `and/or`, series punctuation, paired constructions, comparison targets, bullet syntax, and whether shared modifiers apply to all items. Oxford comma is a clarity device, not universally mandatory.
- **Severity:** `S1` for altered technical logic; `S2`/`S3` otherwise.
- **Exceptions / false positives:** Venue style may choose punctuation; meaning governs.
- **Repair direction:** Make elements grammatically/conceptually parallel and repeat ambiguous operators.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-16 — Comparison has an explicit and like-for-like target

- **Nature:** Hard semantic condition.
- **Reviewer attack:** “`faster`, `lower`, `better`, `similar`, or `X than Y` compares different objects, metrics, conditions, or omitted baseline.”
- **Check:** Identify compared entities, metric, direction, conditions, and reference point. Inspect `only X% lower`, percentage-vs-percentage-point, and ratio ambiguity.
- **Severity:** `S1` for headline result; `S2` otherwise.
- **Exceptions / false positives:** A target can be inherited from an immediately clear sentence/figure.
- **Repair direction:** State both targets and metric under matched conditions; correct arithmetic language.
- **Sources:** [USER-NOTES], [SIGPLAN-EMPIRICAL], [ERNST]. Checked 2026-09-01.

## PT-17 — Tense follows knowledge status, not a rigid section rule

- **Nature:** General best practice / house style.
- **Reviewer attack:** “Tense makes completed experiments sound ongoing, established facts temporary, or proposed behavior already observed.”
- **Check:** Use present for paper content, definitions, algorithms as described, and enduring interpretation; past for completed experimental actions/observations; future for genuinely future work. Maintain consistency around one event.
- **Severity:** `S2` if status is misleading; `S3` otherwise.
- **Exceptions / false positives:** Disciplines and venues vary. Evaluation need not be mechanically all past tense, and design need not be mechanically all present tense.
- **Repair direction:** Align tense with temporal/epistemic status.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-18 — Active/passive voice identifies the important agent

- **Nature:** Diagnostic heuristic, not a ban.
- **Reviewer attack:** “Passive wording hides who performs, configures, trusts, observes, or decides a technically important action.”
- **Check:** Flag passive only when the missing agent matters, the sentence becomes vague, or repeated passives obscure workflow. Preserve passive when object/result is the legitimate focus or actor is obvious/irrelevant.
- **Severity:** `S2` if responsibility is technically ambiguous; `S3`/`S4` style.
- **Exceptions / false positives:** Methods/design sections may use passive voice correctly. Do not rewrite merely to satisfy an active-voice quota.
- **Repair direction:** Name the actor or use active voice where it clarifies responsibility.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-19 — First-person `we` is used purposefully

- **Nature:** Style choice with clarity implications.
- **Reviewer attack:** “Repetitive `we` narration foregrounds authors rather than system behavior,” or conversely, “agentless prose hides an author choice.”
- **Check:** Preserve `we` for author actions, design decisions, observations, and paper organization when natural. Flag redundant `we can see`, `we believe` without epistemic role, or cases where the system/mechanism is the actual actor.
- **Severity:** `S2` if agency/claim basis is unclear; `S3`/`S4` style.
- **Exceptions / false positives:** `We propose`, `we implement`, and `we evaluate` are standard academic constructions; do not ban them.
- **Repair direction:** Use the true agent or direct claim; retain `we` where it clarifies author responsibility.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-20 — Sentence economy preserves necessary logic

- **Nature:** General best practice.
- **Reviewer attack:** “Padded noun phrases, weak verb phrases, metadiscourse, and repeated qualifiers obscure the technical point,” or “overcompression removes conditions.”
- **Check:** Inspect `there is/are`, nominalizations, weak verb phrases, redundant framing, repeated content, excessive adjectives/adverbs, metadiscourse, and avoidable jargon. Apply the deletion test: if removing the sentence or phrase loses no necessary inference, definition, evidence, boundary, or handoff, it has not earned its space. Also verify that compression does not lose actor, condition, contrast, or uncertainty.
- **Severity:** `S2` recurring; `S3` local.
- **Exceptions / false positives:** Terminological repetition often improves precision; not every phrasal verb has an exact simple replacement.
- **Repair direction:** Put the main actor/action relation early, use the exact technical verb, and remove text that performs no reasoning role while preserving all semantic constraints.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-21 — Transitions express real relations, not variety for its own sake

- **Nature:** General best practice.
- **Reviewer attack:** “`however`, `therefore`, or a synonym signals a relation the neighboring claims do not support.”
- **Check:** Validate contrast, cause, consequence, concession, example, and sequence. Do not replace repeated `however` with `nevertheless` merely for lexical variety if the structure itself repeats.
- **Severity:** `S2` for false logic; `S3` for repetition.
- **Exceptions / false positives:** Repetition of a precise transition is preferable to an inaccurate synonym.
- **Repair direction:** Repair underlying organization or choose the exact relation; omit transition if adjacency is sufficient.
- **Sources:** [USER-NOTES] as normalized, [ERNST]. Checked 2026-09-01.

## PT-22 — Punctuation reflects logical structure

- **Nature:** Hard grammar/meaning condition plus style conventions.
- **Reviewer attack:** “Comma, semicolon, colon, dash, parentheses, or quote usage obscures clause boundaries or scope.”
- **Check:** A semicolon normally joins related independent clauses; colon introduces an elaboration/list after a complete lead-in under common English style; parentheses should contain genuinely secondary material; punctuation with citations/quotes follows template.
- **Severity:** `S2` if meaning changes; `S3` otherwise.
- **Exceptions / false positives:** Publisher and language conventions vary; verify venue/template before enforcing typography.
- **Repair direction:** Match punctuation to clause relation or split sentence.
- **Sources:** [USER-NOTES], [ERNST], [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## PT-23 — Compound modifiers and collocations are idiomatic and exact

- **Nature:** General best practice; grammar where ambiguity arises.
- **Reviewer attack:** “Nonidiomatic word combinations or missing hyphenation make the property or attachment unclear.”
- **Check:** Distinguish attributive `high-performance system` from predicative/noun `high performance`; inspect verb–noun polarity (`incur overhead`, not usually `incur benefit`), prepositions, and domain-standard collocations.
- **Severity:** `S2` if meaning is wrong; `S3` style/grammar.
- **Exceptions / false positives:** Compound hyphenation varies by dictionary/template and may be omitted after adverbs ending in `-ly`.
- **Repair direction:** Use established field wording or direct construction; preserve technical nuance.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## PT-24 — Number spelling follows a declared style, not a universal ten rule

- **Nature:** House style / venue preference.
- **Reviewer attack:** “Number styling is inconsistent or hard to scan.”
- **Check:** Follow current venue/publisher or document convention for numbers in prose. Always preserve numerals for measurements, parameters, equations, identifiers, units, tables, and comparisons where clearer.
- **Severity:** `S3` for inconsistency; `S4` preference; venue violation per overlay.
- **Exceptions / false positives:** “Spell integers below ten” is common but not universal and can conflict with technical parallelism.
- **Repair direction:** Apply one documented style consistently without changing numerical value.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## Chinese-specific checks

## PT-25 — Chinese technical prose makes agents and logical relations explicit

- **Nature:** Hard clarity condition.
- **Reviewer attack:** “省略主语、指代或连接关系后，无法判断是谁执行、什么导致什么，或结论适用于哪一层。”
- **Check:** Inspect zero subjects, repeated `其/该/这`, long modifier chains before `的`, `通过…使得…` ambiguity, topic shifts, and English technical terms inserted without grammatical integration.
- **Severity:** `S1` if technical meaning changes; `S2` recurring; `S3` local.
- **Exceptions / false positives:** Chinese legitimately omits recoverable subjects and uses topic-comment structure; flag only real ambiguity/cost.
- **Repair direction:** Name the actor/object, shorten modifier chains, split propositions, and state causal/conditional relation.
- **Sources:** [USER-NOTES], generalized reader-oriented principles from [ERNST]. Checked 2026-09-01.

## PT-26 — Chinese–English terminology mixing is controlled

- **Nature:** General best practice / house style.
- **Reviewer attack:** “The paper alternates Chinese translation, English term, acronym, and code identifier without clear equivalence.”
- **Check:** Define translation/English/acronym at first use; preserve code/system identifiers exactly; choose one later form; distinguish a borrowed technical term from casual English filler such as `flow`, `point`, or `work` when a precise Chinese term exists.
- **Severity:** `S2` for conceptual ambiguity; `S3` style.
- **Exceptions / false positives:** Deliberately bilingual drafts may retain both languages; consistency still matters.
- **Repair direction:** Declare equivalence once and use the canonical form appropriate to audience.
- **Sources:** [USER-NOTES], [ERNST]. Checked 2026-09-01.

## PT-27 — Chinese punctuation and enumeration preserve hierarchy

- **Nature:** General best practice.
- **Reviewer attack:** “顿号、逗号、分号、冒号、括号或多级编号无法反映项目层级和句间关系。”
- **Check:** Inspect list levels, full-width/half-width punctuation consistency, semicolon use among complex parallel items, colon lead-ins, parenthetical overload, and punctuation around English/math/code.
- **Severity:** `S2` if logical grouping changes; `S3` typography.
- **Exceptions / false positives:** Follow publisher/template style for mixed punctuation.
- **Repair direction:** Make hierarchy explicit and normalize punctuation without altering technical tokens.
- **Sources:** [USER-NOTES], house style unless venue specifies otherwise. Checked 2026-09-01.

## Local prose audit sequence

For every sentence in scope:

1. State its proposition and evidence status.
2. If it is high-level, apply substitution, prediction, and boundary tests.
3. Resolve technical terms, referents, agents, units, quantifiers, and epistemic strength.
4. Validate modifier, negation, comparison, coordination, condition, and inter-sentence relation.
5. Check grammar/punctuation in the source language.
6. Apply the deletion test only after all meaning is accounted for.

For every paragraph in scope:

1. State the local claim.
2. Label each sentence as claim, reason, mechanism, evidence, qualification, example, or transition.
3. Read the first and last sentences together: record the opening promise and the closing answer, implication, boundary, or handoff.
4. Flag missing roles, unrelated roles, circular explanation, unsupported inference, premature mechanism detail, and a closing sentence that strands the local claim.
5. Treat rendered line count and one-word final lines as layout diagnostics, not universal writing defects.
