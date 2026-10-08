# STE skill-authoring benchmarks

These six original cases test English instructions and reference text in agent skills.
They are separate from the paper-manuscript fixtures and do not invoke a paper skill.
The simulated interface in case 1 supplies an authoring context, not an executable maintenance task.

The supplied local rules and dictionary facts make these **assisted application** tests.
Their scores cannot establish independent dictionary retrieval, compliance with all 53 writing rules, or full dictionary certification.
All drafts and project terms are synthetic.
No case copies a published manuscript or a long passage from the standard.

## Source and rule map

The primary source is [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf), released on 2025-01-15.
The source URL, issue, date, and PDF SHA-256 are recorded in [suite.json](suite.json).
The PDF is not included in this repository.

| Case | Rule source | Tested behavior |
| --- | --- | --- |
| [1: Parts of speech](cases/01-part-of-speech.json) | Rule 1.2; dictionary entries `test`, `dim`, and `clean` | Use approved parts of speech and meanings. Keep valid adjective and verb uses. |
| [2: Meanings and technical terms](cases/02-meaning-and-technical-terms.json) | Rules 1.3 and 1.12; dictionary entries `follow`, `obey`, and `find` | Distinguish order from compliance. Use necessary domain verbs and approved ordinary verbs accurately. |
| [3: Noun clusters](cases/03-noun-clusters.json) | Rules 1.8, 2.1, and 2.2 | Introduce the approved long name and abbreviation. Make ordinary noun relations clear. |
| [4: Procedural actions](cases/04-procedural-actions.json) | Rules 5.2, 5.3, and 5.4 | Put conditions first. Use commands. Keep sequence and simultaneous actions. |
| [5: Word limits](cases/05-word-limits-and-protected-text.json) | Rules 5.1 and 6.3; Section 8 | Apply the 20-word and 25-word limits correctly. Keep protected code and identifiers. |
| [6: Paragraphs and passive](cases/06-paragraphs-and-passive.json) | Rules 3.6 and 6.4–6.6 | Group topics in paragraphs of at most six sentences. Permit descriptive passive when the agent is unknown. |

Project glossary entries supply authority for fictional technical names and processes.
They do not claim dictionary approval from ASD.
The local dictionary facts cover only the supplied words, parts of speech, and senses.

## Schema and candidate projection

The suite has schema version 1 and kind `ste-authoring`.
Its `cases` values are filenames relative to `cases/`.
Each case has twelve one-point rubric items, `R1` through `R12`.

Each case uses the existing single-stage fixture field types, with `kind` added and `skills` removed.
Only these fields enter candidate input:

```json
{"prompt": "...", "scope": {...}, "evidence": {...}}
```

`scope` contains `authorized`, `excluded`, and `output_language`.
The first two values are non-empty string lists.
`evidence` contains the draft and its supplied context, rules, or glossary.

The harness keeps these fields hidden:

- `id`, `title`, `kind`, and `material_origin`
- `protected_tokens` and `forbidden_actions`
- `hard_gates`, `expected_behavior`, and `rubric`.

Give the candidate the selected authoring guidance as a separate test input.
Keep case metadata and evaluator expectations outside that guidance.

## Structural commands

Run these commands from the repository root:

```bash
python3 scripts/ste_benchmarks.py validate
python3 scripts/ste_benchmarks.py list --suite authoring
python3 scripts/ste_benchmarks.py export --suite authoring --case 1
```

The CLI validates schemas and exports candidate input.
It does not invoke a model, apply behavioral gates, or score quality.
A successful validation is not a behavioral pass.

## Word-count assessment

Use the Section 8 rules to count candidate prose.
A whitespace split cannot certify a count.
Section 8 gives separate rules for vertical lists, parentheses, quoted text, identifiers, numbers, labels, and hyphens.
Count text in parentheses as one item in its surrounding sentence.
Also count the parenthetical text as a separate sentence.

In case 5, the original procedure has 21 words.
Its first description has 23 words, and its second description has 26 words.
These three inputs contain no word-count exceptions.
Their different limits test procedure and description classification.

Case 5 also has a procedure with an immutable quoted interface label.
It has 13 STE words, although a whitespace split gives 22 items.
Rule 8.6 counts that label as one word.
This negative control tests whether the evaluator uses the standard's count rules.

Keep the supplied Python block unchanged.
Treat its literal content as protected quoted text, not newly authored prose.
Assess newly authored prose as prose even if the response puts it in a quotation or code block.
Do not add quotation marks or hyphens to evade a limit.

## Blind comparison and acceptance

Compare two frozen sets of **skill-authoring guidance**: a baseline and a candidate.
Include the frozen writing-core authoring rules in each guidance set.
This comparison does not invoke manuscript Revise.
It has a separate acceptance decision from the 49 paper-manuscript fixture runs.

1. Save the official source hash, both guidance hashes, and each exported input hash.
2. Give the guidance sets random labels `A` and `B`.
3. Start a fresh context for each invocation.
4. Use the same model, reasoning effort, tools, inputs, locale, and time budget for both sets.
5. Save both outputs verbatim and their full access and action logs.
6. Give anonymized outputs and logs to an independent evaluator.
7. Apply each case's hard gates before scoring its rubric.
8. Require all hard gates and at least 10/12 for each candidate case.
9. Require no case score below its baseline score.
10. Save scores, gate outcomes, and evidence for each judgment before revealing the labels.

Score the revised skill text and explanation against observable behavior.
Do not require a fixed sentence or a matching heading.
An equivalent construction can receive credit when it keeps meaning and obeys the tested rule.
Keep failures in the record instead of retrying one guidance set selectively.
Compare each rubric item too; a gain on another item cannot offset a regression.

All six cases must pass for authoring-suite acceptance.
This result neither replaces nor increases the paper-manuscript acceptance total.
A saved closure record must contain source, input, and guidance hashes, anonymous outputs, tool logs, gates, scores, and the final label mapping.
