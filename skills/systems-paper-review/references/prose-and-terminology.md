# Prose, Terminology, and Language Precision

Before high-level or local prose checks, read the [systems-writing core](../../systems-paper-revise/references/writing-core.md). For Chinese or Chinese-to-English text, also read [Chinese calibration](../../systems-paper-revise/references/chinese-writing.md).

This file adds review checks and severity. Fluent prose cannot replace missing scientific evidence. Review gives no replacement prose.

The [coverage contract](../../systems-paper-revise/references/coverage-contract.md) makes full sentence and lexical coverage necessary within the defined scope. Before judgment, make the inventory of sentences, adjacent sentence pairs, and visible lexical occurrences.

For Chinese or mixed prose, use the smallest unit with stable meaning. It can be a word, term, punctuation, or code or math span. Give segmentation ambiguity. Do not invent token counts.

Examine each occurrence in its proposition. The same term can pass at one location and fail at another. Its referent, scope, or evidence commitment can differ.

## Terminology and claim language

## PT-01 — Nonstandard terms have definitions for the intended reader

- **Nature:** General best practice.
- **Reviewer attack:** “A non-specialist systems reviewer cannot recover the paper's meaning without importing subfield-specific knowledge.”
- **Check:** At the first use that affects meaning, examine acronyms, new names, overloaded words, metrics, roles, and domain terms. Make sure that definitions give the distinguishing meaning without further unexplained terms.
- **Severity:** `S2`. `S1` if a central claim becomes ambiguous. `S3` locally.
- **Exceptions / false positives:** Standard audience terms do not make textbook definitions necessary. Intuitive use can precede formal definitions with a clear signal.
- **Repair direction:** Give a minimal local definition, example, or contrast. Do not use chains of unexplained definitions.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE].

## PT-02 — Concept names and term meanings stay unchanged

- **Nature:** Condition for internal consistency when names alter meaning. For other cases, best practice.
- **Reviewer attack:** “I cannot tell whether two labels denote the same mechanism, or whether the same label has changed its meaning.”
- **Check:** Record concept-to-name and term-to-meaning relations for systems, components, actors, stages, metrics, properties, datasets, and baselines. Give both source anchors for suspected name or meaning changes. Do a check of differences between clear aliases, hierarchies, defined contextual meanings, and accidental identity changes.
- **Severity:** `S1` if technical identity is unclear. `S2` recurring. `S3` isolated.
- **Exceptions / false positives:** General prose can use synonyms. Technical terms must keep unchanged identities. Different concepts, clear aliases, and contextual meanings stay different. Similarity alone gives no identity evidence.
- **Repair direction:** Select the term for the source-established identity. Give clear hierarchies or aliases. If identity or distinction is unknown, give the author a clarification question. Recommend different terms for different concepts.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE], [ASD-STE100] as adapted for research prose.

## PT-03 — Paired and categorical terms use symmetric dimensions

- **Nature:** Condition for precision.
- **Reviewer attack:** “The categories compare different dimensions—such as offline versus runtime—so the partition is neither exhaustive nor interpretable.”
- **Check:** Examine each pair or set for a common axis, claimed mutual exclusion, coverage, and the same granularity. Include online/offline, static/dynamic, local/remote, and trusted/untrusted as applicable.
- **Severity:** `S2`. `S1` when taxonomy supports novelty or evaluation.
- **Exceptions / false positives:** System categories can overlap. The text must give example status or different dimensions.
- **Repair direction:** Give repair options: names from one dimension, a two-dimensional taxonomy, or removal of a false opposition.
- **Sources:** [USER-NOTES], [ERNST].

## PT-04 — Acronyms and abbreviations obey the conventions in use

- **Nature:** General best practice. Venue/style specifics vary.
- **Reviewer attack:** “The paper invents or punctuates abbreviations inconsistently, increasing ambiguity.”
- **Check:** Give nonstandard acronyms one definition. Use official abbreviations. Keep capitalization. Keep abbreviations such as `Fig.` different from initialisms such as `CPU`. Make periods necessary only where applicable.
- **Severity:** `S2` for ambiguity/inconsistency. `S3` surface. Venue violation per overlay.
- **Exceptions / false positives:** Known audience acronyms can have no expansion with venue-style permission for that form. Acronyms with only one or two uses can stay as full terms.
- **Repair direction:** Use the official or full term. Give one definition. Use it with the same meaning subsequently.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE].

## PT-05 — Quantifiers are bounded and auditable

- **Nature:** Condition for accuracy.
- **Reviewer attack:** “Words such as `some`, `several`, `various`, `many`, `most`, or Chinese equivalents hide an unsupported population or quantity.”
- **Check:** Examine the quantity's consequence for the inference. Find population, numerator, denominator, range, or representative examples. Make numerical replacements necessary only for meaning.
- **Severity:** `S1` for a claim-driving ambiguity. `S2` in other cases. `S3` if harmless.
- **Exceptions / false positives:** Indefinite quantifiers can be correct with unknown or irrelevant counts and no stronger inference.
- **Repair direction:** Give repair options: measured quantities or ranges, named examples, population boundaries, or removal of an unnecessary quantifier.
- **Sources:** [USER-NOTES], [ERNST], [BRANDON-EVIDENCE].

## PT-06 — Epistemic strength matches evidence

- **Nature:** Condition for accuracy.
- **Reviewer attack:** “The authors claim to ensure/determine/prove when they only observe, or hedge a conclusion that their evidence directly establishes.”
- **Check:** Use the [writing core](../../systems-paper-revise/references/writing-core.md) evidence-verb distinctions. Compare `show`, `demonstrate`, `establish`, `prove`, `ensure`, `guarantee`, `suggest`, `indicate`, `observe`, and Chinese equivalents with evidence. Include inference, assumptions, and scope in that comparison.
- **Severity:** `S0`/`S1` for unsupported guarantee or proof. `S2` for recurring miscalibration.
- **Exceptions / false positives:** `We assume` correctly gives a model assumption. Uncertainty that agrees with evidence gives scientific precision.
- **Repair direction:** Give repair options: changed verbs or quantifiers, clear evidence and conditions, or missing validation.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [SIGPLAN-EMPIRICAL].

## PT-06A — Technical verbs give the accurate mechanism relation

- **Nature:** Condition for precision when the verb carries a technical claim.
- **Reviewer attack:** “The prose says the system `supports`, `enables`, `handles`, or `eliminates` something without identifying the changed operation, enforcement path, or remaining condition.”
- **Check:** Find the actor, action, object, condition, and consequence. Do a check of the difference between implementation and enforcement. Do a check of the difference between permission and causation. Do a check of the difference between removal and transfer outside a common or critical path. Do a check of the difference between measured reduction and guarantees. Do a check of the difference between observed association and mechanism claims.

  Use the precision-verb table for meaning distinctions, not automatic word replacements.
- **Severity:** `S0`/`S1` when a central guarantee or causal claim is false. `S2` for recurring ambiguity. `S3` locally.
- **Exceptions / false positives:** A short mechanism verb can be sufficient if a definition near it gives its relation and boundary.
- **Repair direction:** Give the narrowest relation with evidence. Put its condition beside it.
- **Sources:** [FIVE-VENUE-CORPUS], [SIGPLAN-EMPIRICAL].

## PT-07 — Adjectives and emotional adverbs must have evidence

- **Nature:** General best practice.
- **Reviewer attack:** “Marketing or emotional language substitutes for measured importance or surprise.”
- **Check:** Examine `novel`, `simple`, `easy`, `efficient`, `significant`, `dramatic`, `surprising`, `unfortunately`, `overwhelmingly`, and equivalents. Find the metric or comparison that gives each word content.
- **Severity:** `S2` if it overstates a scientific claim. `S3` style.
- **Exceptions / false positives:** `Surprisingly` can show a result contrary to a clear hypothesis. `significant` can have a statistical definition. Each use must give its basis.
- **Repair direction:** Replace the word with the measured property or remove it.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## PT-08 — Numbers include scale, comparator, and precision sufficient for interpretation

- **Nature:** Condition for interpretability for decision-related values.
- **Reviewer attack:** “A number is presented without saying whether it is large, small, costly, or meaningful, or with precision unsupported by measurement.”
- **Check:** For each nontrivial value, find units, baseline or denominator, variability or tolerance, and practical thresholds. Examine the rule for significant digits. Make commentary necessary only for interpretation. Commentary can be unnecessary for identifiers, obvious counts, or usual constants.
- **Severity:** `S1` for a misleading headline number. `S2` for missing context. `S3` for rounding inconsistency.
- **Exceptions / false positives:** Exact integer facts and parameter settings do not always make magnitude interpretation necessary.
- **Repair direction:** Give comparators, absolute values, or ranges. Remove false precision. Keep raw evidence.
- **Sources:** [USER-NOTES] as normalized, [SIGPLAN-EMPIRICAL], [HEISER-BENCH].

## PT-09 — Units and notation agree in meaning and typography

- **Nature:** Condition for correctness plus template preference.
- **Reviewer attack:** “Values cannot be compared because units, prefixes, capitalization, or spacing change.”
- **Check:** Examine SI or binary prefixes, bits or bytes, time or rate, percentages or percentage points, conversion, plural forms, and notation. In LaTeX, `~` makes a nonbreaking space. It is not a visible tilde. Its correctness depends on the macro and template.
- **Severity:** `S1` for numerical meaning error. `S2` recurring ambiguity. `S3` typography.
- **Exceptions / false positives:** Number-unit spacing depends on field and venue conventions. `~` is not universally incorrect.
- **Repair direction:** Select standard units or macros. Convert values correctly. Use the same spacing.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE].

## PT-10 — `e.g.` and `i.e.` keep different meanings

- **Nature:** Condition for meaning.
- **Reviewer attack:** “An example is presented as an exhaustive restatement, or a definition as one optional example.”
- **Check:** `e.g.` gives non-exhaustive examples. `i.e.` gives an equivalent restatement. Examine punctuation and surrounding logic for the applicable venue and language style.
- **Severity:** `S2` if scope changes. `S3` in other cases.
- **Exceptions / false positives:** Plain `for example` or `that is` can be clearer in mixed Chinese and English prose.
- **Repair direction:** Select the correct relation or give it clearly.
- **Sources:** [USER-NOTES], [ERNST].

## PT-10A — High-level wording gives specified relations and boundaries

- **Nature:** General systems-writing principle with claim-precision consequences.
- **Reviewer attack:** “The prose sounds abstract, but it could describe almost any system and does not explain why this design follows.”
- **Check:** Apply the four high-level tests: substitution, prediction, boundary or counterexample, and evidence. Record the missing relation at the specified endpoints. A vague criticism alone is insufficient.
- **Severity:** `S1` when the central idea or design derivation is unrecoverable. `S2` when a paragraph loses specificity. `S3` for one vague sentence.
- **Exceptions / false positives:** A short roadmap can be broad if adjacent text immediately gives the distinguishing relation. A technical term can encode a relation with a previous definition.
- **Repair direction:** Give the shortest causal relation with evidence at the applicable abstraction level. Keep low-level details only for consequential decisions, properties, or boundaries.
- **Sources:** [USER-NOTES], [FIVE-VENUE-CORPUS].

## PT-10B — Evidence provenance is distilled at the manuscript's comparison level

- **Nature:** General systems-writing principle with evidence-scope consequences.
- **Reviewer attack:** “The sentence narrates what the authors found in a repository or build instead of stating the prior system capability that matters to this comparison.”
- **Check:** For artifact facts in prior-work positioning, use [artifact-to-capability distillation](../../systems-paper-revise/references/positioning-and-insight.md). Find actor, object, stage, required control, and comparison-axis consequence. Do a check of the difference between raw observations and inference. Examine the implementation detail's materiality to the argument.
- **Severity:** `S1` when an unsupported inference carries the gap. `S2` when forensic detail obscures a comparison. `S3` for a local abstraction mismatch.
- **Exceptions / false positives:** Build or artifact detail can be the studied mechanism, implementation evidence, or a necessary claim boundary. Citations or evidence notes can give provenance without a central sentence role.
- **Repair direction:** Give the narrowest capability or limitation with evidence. Keep its deployment qualification. Missing inference or alternative deployment paths make evidence necessary.
- **Sources:** [SYSTEMS-GUIDE], [FIVE-VENUE-CORPUS].

## Sentence logic and grammar

## PT-11 — Each sentence has one dominant assertion

- **Nature:** Condition for readability and grammar.
- **Reviewer attack:** “I cannot determine actor, action, object, condition, contrast, or main assertion.”
- **Check:** Find the primary assertion and its conditions, reasons, contrasts, and qualifications. Find fragments, run-ons, unrelated primary claims, excessive embedding, unclear coordination, missing actors, missing actions, and guessed relations. List new entities, relations, and abstraction changes. Examine definition and dependency sequence. Length alone does not show failure.
  Check `and` and `or` against the source's independent requirements. Grammatical coordination can still suggest that one duty replaces another. Identify each required duty and distinguish it from the evidence needed to establish it.
- **Severity:** `S1` if a central technical statement has multiple readings. `S2` recurring. `S3` local grammar.
- **Exceptions / false positives:** Length alone does not make a sentence defective. Sentence structure can clearly represent an accurate relation.
- **Repair direction:** Divide independent assertions. Give source-established actors and relations. If this helps interpretation, put the primary claim before its qualifications. After division, compare each original proposition's conditions, quantifiers, modality, negation, sequence, and causal or evidential relations.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE], [ASD-STE100] as adapted for research prose.

## PT-12 — Modifiers have unambiguous attachment and scope

- **Nature:** Condition for meaning.
- **Reviewer attack:** “`which`, an adverb, prepositional phrase, participle, or relative clause can modify more than one candidate.”
- **Check:** Examine each modifier's position and meaning. Find misplaced `only`, `also`, `respectively`, negation, and dangling participles. Nearest-noun attachment is a clarity aid. It is not a universal grammar rule.
- **Severity:** `S1` if technical meaning changes. `S2`/`S3` in other cases.
- **Exceptions / false positives:** Grammar and meaning can select a distant antecedent without ambiguity. Distance alone does not give a defect.
- **Repair direction:** Give repair options: changed modifier position, a named antecedent, a repeated noun, or different sentences.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE].

## PT-13 — Pronouns and demonstratives have unique antecedents

- **Nature:** Condition for clarity.
- **Reviewer attack:** “`it`, `this`, `that`, `they`, `these results`, or a Chinese zero pronoun could refer to multiple mechanisms or findings.”
- **Check:** Find each pronoun's or demonstrative's local antecedent. Find unclear `This shows...` uses without a definite observation or inference.
- **Severity:** `S1` if claim meaning changes. `S2`/`S3` in other cases.
- **Exceptions / false positives:** Immediate singular antecedents do not make noun repetition necessary.
- **Repair direction:** Give an accurate noun phrase or the referenced proposition.
- **Sources:** [ERNST], [HEISER-STYLE], [USER-NOTES].

## PT-14 — Articles, countability, number, and agreement are correct in English

- **Nature:** Condition for grammar.
- **Reviewer attack:** “Frequent article/count/agreement errors reduce confidence and sometimes change whether a class or instance is meant.”
- **Check:** Examine singular count nouns, generic or definite references, mass nouns, subject-verb agreement, pronoun agreement, and `data` or collective-noun use. Use the selected style.
- **Severity:** `S2` if recurring/ambiguous. `S3` local.
- **Exceptions / false positives:** Bare nouns can be correct as mass nouns, generic plurals, proper nouns, or noun modifiers.
- **Repair direction:** Give repair options: article addition or removal, plural forms, or the correct mass/count construction. Keep the referent unchanged.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE].

## PT-15 — Coordination and parallelism keep category and scope

- **Nature:** Condition for meaning and grammar.
- **Reviewer attack:** “A list combines unlike grammatical or conceptual units, so operators and comparisons have uncertain scope.”
- **Check:** Examine `and/or`, series punctuation, paired constructions, comparison targets, bullets, and shared-modifier scope. Make sure that conceptual and grammatical symmetry are present. Interface level, hosted object, and implementation organization are different axes. Verb phrases alone do not make that list parallel. The Oxford comma is a clarity aid, not a universal requirement.
- **Severity:** `S1` for altered technical logic. `S2`/`S3` in other cases.
- **Exceptions / false positives:** Venue style can select punctuation. Meaning controls the judgment.
- **Repair direction:** Make elements conceptually and grammatically parallel. Repeat operators where their scope has ambiguity.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE].

## PT-16 — Comparison has a clear and like-for-like target

- **Nature:** Condition for meaning.
- **Reviewer attack:** “`faster`, `lower`, `better`, `similar`, or `X than Y` compares different objects, metrics, conditions, or omitted baseline.”
- **Check:** Find compared entities, metric, direction, conditions, and reference point. Examine `only X% lower`, percentages, percentage points, and ratio ambiguity.
- **Severity:** `S1` for headline result. `S2` in other cases.
- **Exceptions / false positives:** An immediately clear sentence or figure can give the comparison target.
- **Repair direction:** Give both targets and the metric in equivalent conditions. Correct arithmetic language.
- **Sources:** [USER-NOTES], [SIGPLAN-EMPIRICAL], [ERNST].

## PT-16A — Necessary and sufficient conditions are not interchanged

- **Nature:** Condition for logic.
- **Reviewer attack:** “The manuscript moves from `X requires Y` to `Y guarantees X`, or from co-occurrence to sufficiency, without ruling out other mechanisms.”
- **Check:** For `requires`, find evidence for necessity. For `ensures` or `guarantees`, find assumptions and enforcement or proof for sufficiency. Keep `helps`, `permits`, and `is associated with` as weaker relations. Make sure that conclusions do not strengthen them without explanation.
- **Severity:** `S0`/`S1` when the error supports a central design or correctness claim. `S2` locally.
- **Repair direction:** Give the evidence-supported relation as a repair option. Give missing premises or evidence. Put necessary limits on the conclusion.
- **Sources:** [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE].

## PT-16B — System properties and proof obligations stay at the same explanatory level

- **Nature:** Condition for logic and meaning when the mismatch changes the claim. For other cases, clarity.
- **Reviewer attack:** “The sentence says a runtime property cannot replace a proof, so I cannot tell whether the remaining obligation is another system property, an enforcement mechanism, or merely an author task.”
- **Check:** Do a check of the difference between system properties and evidence, proof, or argument obligations. Include execution, interface, authorization, equivalence, and isolation properties. For necessary-but-insufficient claims, find both properties. Examine necessity in different checks. Clear proof-obligation lists can correctly use epistemic wording.
- **Severity:** `S1` when the category shift obscures a central correctness claim. `S2` locally.
- **Repair direction:** Give the remaining object-level property or clear proof-obligation framing for both items. Keep unsupported necessity visible during wording repair.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE].

## PT-17 — Tense agrees with knowledge status

- **Nature:** General best practice / house style.
- **Reviewer attack:** “Tense makes completed experiments sound ongoing, established facts temporary, or proposed behavior already observed.”
- **Check:** Use present tense for paper content, definitions, described algorithms, and enduring interpretations. Use past tense for finished experimental actions or observations. Use future tense for future work. Use the same tense for one event.
- **Severity:** `S2` if status is misleading. `S3` in other cases.
- **Exceptions / false positives:** Disciplines and venues differ. Evaluation does not always use past tense. Design does not always use present tense.
- **Repair direction:** Use tense that agrees with temporal and epistemic status.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE].

## PT-18 — Active/passive voice identifies the important agent

- **Nature:** Diagnostic heuristic, not a ban.
- **Reviewer attack:** “Passive wording hides who performs, configures, trusts, observes, or decides a technically important action.”
- **Check:** Record a passive-voice defect only if the missing actor matters, ambiguity results, or repeated passives hide workflow. Keep research-prose passive voice for a correct object or result focus, or an obvious or irrelevant actor.
- **Severity:** `S2` if responsibility is technically ambiguous. `S3`/`S4` style.
- **Exceptions / false positives:** Methods and design sections can correctly use passive voice. Active-voice quotas do not apply to manuscript prose.
- **Repair direction:** Give the source-established actor. Use active voice where it makes responsibility clear. An unknown actor that affects meaning makes author clarification necessary. Keep invented actors outside language repair.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE], [ASD-STE100] as adapted for research prose.

## PT-19 — First-person `we` has a clear function

- **Nature:** Style choice with clarity implications.
- **Reviewer attack:** “Repetitive `we` narration foregrounds authors rather than system behavior,” or conversely, “agentless prose hides an author choice.”
- **Check:** Keep `we` for author actions, design decisions, observations, and paper organization. Find redundant `we can see` or `we believe` without an epistemic function. Find sentences whose actor is the system or mechanism.
- **Severity:** `S2` if agency/claim basis is unclear. `S3`/`S4` style.
- **Exceptions / false positives:** `We propose`, `we implement`, and `we evaluate` are standard academic constructions. They are permitted.
- **Repair direction:** Use the actor that does the action or give the claim directly. Keep `we` where it makes author responsibility clear.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [HEISER-STYLE].

## PT-20 — Sentence economy keeps necessary logic

- **Nature:** General best practice.
- **Reviewer attack:** “Padded noun phrases, weak verb phrases, metadiscourse, and repeated qualifiers obscure the technical point,” or “overcompression removes conditions.”
- **Check:** Use the concision priority in order: claim and boundary, necessary premise, decisive causal link, credibility-changing evidence, required definition. Examine nominalizations, weak verb phrases, repeated framing, metadiscourse, and unnecessary jargon. For an ending, record the lost conclusion, boundary, obligation, or handoff if removed. Without information loss, record a redundant payoff even with correct transition words.

  Repetition is permitted across different functions. Examples include abstract conclusions, introduction derivations, design realization, and evaluation evidence. Record repetition only without a new function.
- **Severity:** `S2` recurring. `S3` local.
- **Exceptions / false positives:** Term repetition often helps precision. Some phrasal verbs have no accurate alternative with one word.
- **Repair direction:** Put the primary actor and action first. Use the accurate mechanism relation. Remove words without a reasoning function. Keep all meaning constraints.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## PT-21 — Transitions give relations with evidence

- **Nature:** General best practice.
- **Reviewer attack:** “`however`, `therefore`, or a synonym signals a relation the neighboring claims do not support.”
- **Check:** Examine contrast, cause, consequence, concession, example, and sequence. Keep transition meanings unchanged. Synonym changes alone do not repair repeated structure. Examine `however X does not Y; therefore Z is still required` as a relation. Its requirement must give a design-specific consequence beyond repeated `not Y`.
- **Severity:** `S2` for false logic. `S3` for repetition.
- **Exceptions / false positives:** A repeated transition with the correct meaning is better than a synonym with the wrong meaning.
- **Repair direction:** Repair the organization or give the accurate relation. If adjacency is sufficient, remove the transition.
- **Sources:** [USER-NOTES] as normalized, [ERNST].

## PT-22 — Punctuation reflects logical structure

- **Nature:** Condition for grammar and meaning, with style conventions.
- **Reviewer attack:** “Comma, semicolon, colon, dash, parentheses, or quote usage obscures clause boundaries or scope.”
- **Check:** In common English, a semicolon joins related independent clauses. A colon gives elaboration or a list after a full lead-in. Parentheses contain secondary material. Citation and quotation punctuation depends on the template.
- **Severity:** `S2` if meaning changes. `S3` in other cases.
- **Exceptions / false positives:** Publisher and language conventions differ. Before typography judgments, examine venue and template rules.
- **Repair direction:** Use punctuation for the clause relation in the source or divide the sentence.
- **Sources:** [USER-NOTES], [ERNST], [ACM-TEMPLATE], [USENIX-TEMPLATE].

## PT-23 — Compound modifiers and collocations are idiomatic and accurate

- **Nature:** General best practice. Grammar where ambiguity arises.
- **Reviewer attack:** “Nonidiomatic word combinations or missing hyphenation make the property or attachment unclear.”
- **Check:** Keep attributive `high-performance system` different from predicative or noun `high performance`. Examine verb-noun polarity, prepositions, and standard domain collocations. Compare `incur overhead` with the usually incorrect `incur benefit`.
- **Severity:** `S2` if meaning is wrong. `S3` style/grammar.
- **Exceptions / false positives:** Compound hyphens depend on dictionaries and templates. Compounds after `-ly` adverbs can have no hyphen.
- **Repair direction:** Use standard field terms or direct constructions. Keep technical distinctions.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## PT-24 — Number spelling obeys its style rule

- **Nature:** House style / venue preference.
- **Reviewer attack:** “Number styling is inconsistent or hard to scan.”
- **Check:** Obey the venue, publisher, or document convention for prose numbers. If numerals help interpretation, keep them for measurements, parameters, equations, identifiers, units, tables, and comparisons.
- **Severity:** `S3` for inconsistency. `S4` preference. Venue violation per overlay.
- **Exceptions / false positives:** “Spell integers below ten” is common but not universal. It can conflict with parallel technical notation.
- **Repair direction:** Use one documented style throughout. Keep numerical values unchanged.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE].

## Chinese-specific checks

Use [Chinese systems-writing calibration](../../systems-paper-revise/references/chinese-writing.md) as the source of truth. Examine visible defects and their consequences within the authorized scope.

## PT-25 — Chinese technical prose makes agents and logical relations clear

- **Nature:** Condition for clarity.
- **Reviewer attack:** “省略主语、指代或连接关系后，无法判断是谁执行、什么导致什么，或结论适用于哪一层。”
- **Check:** Examine omitted subjects, repeated `其/该/这`, long modifiers before `的`, topic changes, and English terms without grammatical integration. For each `通过—从而—进而—最终` chain, examine each arrow in different checks. Do a check of the difference between mechanism predictions and measured results. Find `针对……问题，提出……方法` sentences without specified failure conditions or technical changes.
- **Severity:** `S1` if technical meaning changes. `S2` recurring. `S3` local.
- **Exceptions / false positives:** Chinese can correctly have no subject with a clear referent. Topic-comment structure is permitted. Give findings only for ambiguity or reading cost with evidence.
- **Repair direction:** Give the actor and object. Use shorter modifier chains. Divide propositions. Give clear causal or conditional relations.
- **Sources:** [USER-NOTES], generalized reader-oriented principles from [ERNST].

## PT-25A — Chinese-to-English review keeps logic rather than word order

- **Nature:** Condition for meaning preservation when translation is in scope.
- **Reviewer attack:** “The English is grammatical but preserves an omitted Chinese actor, ambiguous `从而`, or inflated evidence claim.”
- **Check:** Compare source and translation for actor, primary assertion, conditions, causal arrows, evidence strength, quantifiers, and boundaries. Proposition equivalence controls the judgment. Literal order does not.
- **Severity:** `S0`/`S1` when technical meaning changes. `S2` for a recurring ambiguity. `S3` locally.
- **Exceptions / false positives:** Use only the supplied translation unless the user authorizes a new translation. This read-only skill gives the logical repair requirement. It gives no replacement translation.
- **Repair direction:** Record the lost or stronger proposition. Give the necessary restored relation.
- **Sources:** [FIVE-VENUE-CORPUS], [USER-NOTES].

## PT-26 — Chinese and English terms have clear equivalence

- **Nature:** General best practice / house style.
- **Reviewer attack:** “The paper alternates Chinese translation, English term, acronym, and code identifier without clear equivalence.”
- **Check:** Give the Chinese term, English term, and acronym their first-use equivalence. Keep code and system identifiers unchanged. Select one subsequent form. Keep technical terms different from casual `flow`, `point`, or `work` where accurate Chinese terms are available.
- **Severity:** `S2` for conceptual ambiguity. `S3` style.
- **Exceptions / false positives:** Bilingual drafts can keep both languages. Consistency still applies.
- **Repair direction:** Give one equivalence declaration. Use the standard form for the audience.
- **Sources:** [USER-NOTES], [ERNST].

## PT-27 — Chinese punctuation and enumeration keep hierarchy

- **Nature:** General best practice.
- **Reviewer attack:** “顿号、逗号、分号、冒号、括号或多级编号无法反映项目层级和句间关系。”
- **Check:** Examine list levels, full-width or half-width punctuation, and semicolons between complex parallel items. Examine colon lead-ins, excessive parentheses, and English, math, or code punctuation.
- **Severity:** `S2` if logical grouping changes. `S3` typography.
- **Exceptions / false positives:** Obey publisher or template conventions for mixed punctuation.
- **Repair direction:** Show the hierarchy. Use the same punctuation rules. Keep technical tokens unchanged.
- **Sources:** [USER-NOTES], house style if the venue gives no different rule.

## Local prose audit sequence

First, complete checks at the higher assessable paper, section, and paragraph levels. Lower-level fluency cannot remove higher-level role or evidence failures.

For each sentence in scope, use these steps:

1. Record its proposition and evidence status.
2. For high-level sentences, apply substitution, prediction, boundary or counterexample, and evidence tests.
3. Find terms, referents, actors, units, quantifiers, mechanism verbs, and epistemic strength.
4. Examine modifiers, negation, comparisons, coordination, conditions, necessity, sufficiency, and inter-sentence logic.
5. Examine source-language grammar and punctuation.
6. After full meaning accounting, apply the deletion test.

For each lexical occurrence in scope, use these steps:

1. Record its sentence-local function and technical identity.
2. Examine applicable definitions, first uses, referents, quantifiers, modifiers, negation, comparisons, mechanism commitments, and epistemic strength.
3. Examine applicable collocations, tense, articles, countability, agreement, punctuation, units, notation, and source-language forms.
4. Give the shared coverage state.
5. Give any finding ID.
6. Give each risk-bearing occurrence a different row.
7. Compress passed ranges only with the shared coverage contract's permission.

For each paragraph in scope, use these steps:

1. Record its signaled or author-supplied role.
2. Independently record its delivered role and local claim.
3. Complete `the reader should believe ___ because ___`.
4. Record a second independent answer as a competing obligation.
5. Give each sentence its role: claim, reason, mechanism, evidence, qualification, example, or transition.
6. Read the first and last sentences together.
7. Record the opening promise and closing answer, implication, boundary, or handoff.
8. Record the information lost without the ending.
9. Find role mismatches, missing or unrelated functions, circular reasoning, and unsupported inferences. Find mechanism detail before its motivating relation and stranded or repeated closing claims.
10. Examine argument organization and scientific evidence in different checks.
11. Record both dimensions if both fail.
12. Treat rendered line count and one-word final lines as layout diagnostics.

After the last sentence and lexical occurrence, compare terms, referents, numbers, conditions, claim strength, and evidence status throughout scope. Record the last units and totals in the shared receipt. An absence of further findings does not show completion.
