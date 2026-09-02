# Change Safety and Meaning Preservation

Use this checklist before and after every edit batch. A revision is unsafe if it improves prose while changing unsupported facts, technical behavior, evidence scope, author intent, or executable document structure.

## CS-01 — Preserve the frozen scope

- **Invariant:** Only named text/ranges/files/objects may be read or edited.
- **Before:** Record exact anchors/paths and exclusions.
- **After:** Confirm no neighboring content, includes, bibliography, figures, artifact, or generated files were opened/changed unless explicitly in scope.
- **Failure response:** Undo the out-of-scope edit directly and report the context dependency; never use Git during the loop.

## CS-02 — Preserve proposition inventory

- **Invariant:** Every supported factual/technical proposition remains present unless deliberately deleted, qualified, combined, or replaced for a stated finding.
- **Before:** List claims, assumptions, conditions, limitations, and causal links.
- **After:** Compare semantic propositions rather than word overlap. Check that compression did not drop a precondition, exception, agent, or failure case.
- **Failure response:** Restore the missing proposition or record an intentional, evidence-backed deletion.

## CS-03 — Do not strengthen claims accidentally

- **Invariant:** Revision cannot increase universality, certainty, causality, novelty, performance, practicality, security, or maturity beyond evidence.
- **Watch pairs:** `may → does`, `suggests → demonstrates`, `observed → guarantees`, `tested cases → all`, `prototype → system`, `can → supports`, `improves in W → improves`, `one of the first → first`.
- **After:** Reapply sibling `RC`, `TS`, `EV`, and `PT-06` rules.
- **Failure response:** Restore/calibrate the epistemic verb, quantifier, domain, and conditions.

## CS-04 — Preserve numbers and their semantics

- **Invariant:** Numeric value, sign, unit, precision, denominator, aggregation, baseline, percentile, time window, hardware/configuration, and uncertainty remain linked.
- **Before:** Inventory every number in the edit region and its meaning.
- **After:** Recompute simple arithmetic/conversions; compare all occurrences; check percentage vs percentage points, rate vs total, mean vs median, speedup vs reduction.
- **Failure response:** Restore authoritative value or mark an evidence blocker. Never “smooth” inconsistent values by choosing one without evidence.

## CS-05 — Preserve citations and attribution

- **Invariant:** Citation keys/links, author attribution, quoted material, and scope of support remain correct.
- **Before:** Identify the proposition each citation supports.
- **After:** Verify movement/sentence merging has not made a citation support a new claim; verify externally when permitted.
- **Failure response:** Reposition, split, qualify, or block for source verification. Never invent a citation/key.

## CS-06 — Preserve equations, algorithms, and notation

- **Invariant:** Symbols, domains, indices, operators, equations, pseudocode steps, invariants, complexity, and examples retain meaning unless explicitly corrected with evidence.
- **Before:** Mark math/code spans and defined terms as protected tokens.
- **After:** Check brace/mode integrity, symbol identity, definition order, prose-equation correspondence, and dimensional consistency.
- **Failure response:** Restore exact token/structure or make a separately justified technical correction.

## CS-07 — Preserve code and system identifiers exactly

- **Invariant:** System/component names, APIs, functions, files, flags, environment variables, commands, configuration keys, workload names, dataset identifiers, hardware models, versions, and case remain exact.
- **Before:** Extract identifiers from scoped text/artifact.
- **After:** Compare spelling/punctuation/capitalization and distinguish prose display from literal value.
- **Failure response:** Restore authoritative identifier; if inconsistent sources disagree, report blocker.

## CS-08 — Preserve LaTeX and Markdown structure

- **Invariant:** Commands, environments, braces, labels, references, citations, comments, math delimiters, escaping, links, code fences, headings, lists, and custom macros remain syntactically valid and semantically placed.
- **Before:** Identify prose-safe spans versus protected structure.
- **After:** Inspect exact source; compile/render only if relevant project scope/toolchain permits.
- **Failure response:** Correct structure directly, re-check rendering, and keep project convention.

## CS-09 — Preserve figure/table data and encoding

- **Invariant:** Values, categories, uncertainty, missing results, labels, units, baselines, and visual semantics remain truthful.
- **Before:** Record data/encoding map.
- **After:** Verify no axis, normalization, order, aspect, highlight, or omission magnifies advantage deceptively; cross-check caption/callout.
- **Failure response:** Restore truthful encoding or block for underlying data. Never modify data to fit prose.

## CS-10 — Preserve limitations near affected claims

- **Invariant:** Material assumptions, caveats, negative results, scope bounds, and future-work status remain visible where reviewers need them.
- **Before:** Link each limitation to affected claim.
- **After:** Check reordering did not bury/remove it or convert future work into present capability.
- **Failure response:** Restore proximity and claim calibration.

## CS-11 — Preserve source language and deliberate terminology choices

- **Invariant:** English remains English, Chinese remains Chinese, and deliberate mixed-language tokens remain unless translation is requested. Technical term choices do not drift for stylistic variety.
- **Before:** Record target language and canonical glossary.
- **After:** Check language, acronym expansion, translation equivalence, spelling, and system/code identifiers.
- **Failure response:** Restore language/term or ask author about a meaningful translation choice.

## CS-12 — Preserve author intent when several valid stories exist

- **Invariant:** The revision does not choose a different contribution hierarchy, audience, threat model, deployment scenario, baseline, or claim boundary merely because it sounds stronger.
- **Before:** Identify choices with scientific consequences.
- **After:** Ask whether a reasonable author could reject the chosen framing while accepting all facts.
- **Failure response:** Mark `B4 — author decision` and present alternatives with consequences.

## CS-13 — Preserve unrelated user work and working state

- **Invariant:** No backup, formatting churn, generated output, dependency change, external message, Git state change, or unrelated file edit.
- **Before:** Operate on explicit targets and use direct patching/editing.
- **After:** Inspect targeted content without Git; remove only disposable temporary outputs created by the process when safe and authorized.
- **Failure response:** Stop and disclose unintended effect. Do not use destructive recovery.

## CS-14 — Tool output is scoped evidence, not authority

- **Invariant:** Compiler/linter/grammar checker/test/plot/citation API output is interpreted in context.
- **Before:** State what the tool can and cannot validate.
- **After:** Confirm suggestions do not change technical semantics and passes do not overclaim readiness.
- **Failure response:** Reject false positive or record limitation; do not edit solely to silence a tool.

## Preservation snapshot

Before a nontrivial batch, maintain this internal snapshot:

```text
Central claim(s):
Assumptions/conditions:
Limitations:
Numbers + units + denominators:
Citations + supported propositions:
Equations/identifiers/macros/labels:
Canonical terminology:
Author-intent choices:
```

After the batch, check every line. If an item changes, link it to a finding, evidence, and resolution test.

## Safe claim calibration ladder

When evidence is weaker than wording, choose the strongest supported level, not automatically the weakest:

| Unsupported wording | Possible evidence-safe direction |
|---|---|
| Universal guarantee | Guarantee under explicit proven/enforced assumptions; otherwise observed property |
| Causal conclusion | Controlled effect if design supports it; otherwise association/observation |
| `first` / `only` | Bounded population/date or `to our knowledge` backed by search; otherwise precise delta |
| General scalability | Tested range and limiting resource |
| Production/deployment claim | Prototype/implementation/deployment status actually evidenced |
| “Significant improvement” | Absolute/relative effect, uncertainty, and practical context |
| Full support | Implemented/tested feature subset and exclusions |

Hedging is not a substitute for missing evidence. If the claim is essential and cannot be stated meaningfully at the supported level, keep an evidence blocker.

## Sources

Meaning-preservation principles derive from the sibling review rules and evidence hierarchy, plus revision patterns in [BRANDON-EVIDENCE], [YSLAB-REVISION], and [SIMCHOWITZ-WRITING]. Source keys are defined in the sibling `source-registry.md`. Last reconciled 2026-09-01.

