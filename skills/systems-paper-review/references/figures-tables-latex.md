# Figures, Tables, Captions, Math, and LaTeX

Inspect source and rendered output when both are explicitly in scope. Source correctness does not guarantee readable rendering, and visual polish does not guarantee truthful encoding. Template and venue instructions override local preferences.

## Figures and plots

## FL-01 — Every figure has one decision-relevant message

- **Nature:** General best practice.
- **Reviewer attack:** “The figure is decorative, combines unrelated stories, or requires reconstructing its purpose from the paper.”
- **Check:** State the figure's intended reader question and takeaway. For early motivation/overview figures, also apply [examples-figures-results.md](examples-figures-results.md): determine whether the object reveals a mismatch, boundary, causal path, system model, workflow, or intellectual move rather than merely repeating nouns. Verify panels/elements support the message and the text uses it in the argument rather than merely mentioning it.
- **Severity:** `S2`; `S1` if a central claim depends on an unreadable/ambiguous figure.
- **Exceptions / false positives:** Overview figures may communicate architecture/workflow rather than one numerical claim; they still need a coherent purpose.
- **Repair direction:** Remove unrelated content, split panels, or clarify the question/takeaway without adding unsupported annotation.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [HEISER-STYLE]. Checked 2026-09-01.

## FL-02 — Visual encodings have explicit, stable semantics

- **Nature:** Hard interpretability condition.
- **Reviewer attack:** “Color, shape, line, arrow, box, position, or size appears meaningful but is undefined or changes meaning across figures.”
- **Check:** Inventory every encoding and map it to legend/caption/text. Cross-check same concept/baseline across all in-scope figures.
- **Severity:** `S1` if it can reverse interpretation; `S2` recurring; `S3` cosmetic.
- **Exceptions / false positives:** Ordinary spatial structure need not be overexplained when unambiguous; decorative styling should not mimic data encoding.
- **Repair direction:** Define, remove, or standardize the encoding; use redundant shape/pattern/text for critical distinctions.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE]. Checked 2026-09-01.

## FL-03 — Graphs do not visually exaggerate or suppress results

- **Nature:** Hard research-integrity condition.
- **Reviewer attack:** “Axis, scale, aspect ratio, normalization, sorting, cropping, or chart type was chosen to manufacture an advantage.”
- **Check:** Inspect origin/range, linear/log scale, aspect ratio, dual axes, broken axes, normalization denominator, missing values, order, binning, aggregation, and plot/table choice. Compare visual magnitude with numerical effect.
- **Severity:** `S0` for materially misleading presentation; `S1` for ambiguous headline result.
- **Exceptions / false positives:** Truncated axes, logs, and compact vertical dimensions can be appropriate when labeled and matched to the question.
- **Repair direction:** Use an honest scale/representation, disclose transforms, and include absolute/reference values where needed. Never optimize the chart solely to display superiority.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [USER-NOTES] as normalized. Checked 2026-09-01.

## FL-04 — Uncertainty and missing data are visible

- **Nature:** Hard when noisy/stochastic evidence supports a claim.
- **Reviewer attack:** “The plot implies exact stable values while variability, failed runs, censoring, or missing cases are hidden.”
- **Check:** Inspect error bars/bands/distributions, definition of uncertainty, sample size, missing markers, clipped values, timeout/failure treatment, and whether bars are discernible.
- **Severity:** `S1` if uncertainty can change conclusion; `S2` otherwise.
- **Exceptions / false positives:** Deterministic/exact data need no error bars; state why when not obvious.
- **Repair direction:** Display/define appropriate uncertainty and missing/failure cases; qualify conclusions.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH]. Checked 2026-09-01.

## FL-05 — Baseline and “ours” styling does not replace labels or fairness

- **Nature:** General best practice / house style.
- **Reviewer attack:** “The plot privileges the proposed method through ordering/emphasis while identities or comparison conditions remain unclear.”
- **Check:** Ensure every series is directly identifiable and accessible. Consistent colors/order can aid reading; placing `ours` at the right or bolding it is optional and must not conceal data or imply a result.
- **Severity:** `S2` if misleading/ambiguous; `S3`/`S4` style.
- **Exceptions / false positives:** Emphasis is acceptable when all data remain equally legible.
- **Repair direction:** Label clearly, standardize across figures, and keep emphasis subordinate to truthful values.
- **Sources:** [USER-NOTES] as normalized, [HEISER-BENCH]. Checked 2026-09-01.

## FL-06 — Figures remain readable at final size and common viewing modes

- **Nature:** General best practice; accessibility may be official policy.
- **Reviewer attack:** “Text, lines, markers, or panel labels are unreadable in two-column size, grayscale, print, or for color-vision deficiency.”
- **Check:** Render at final size; inspect font, stroke, marker, contrast, grayscale distinguishability, color palette, and zoom dependence. Compare figure text with body text without requiring identical size.
- **Severity:** `S1` if central evidence cannot be read; `S2` recurring; `S3` detail; official accessibility violation per overlay.
- **Exceptions / false positives:** Dense diagrams may justify smaller secondary labels if still readable and not decision-critical.
- **Repair direction:** Simplify, enlarge, use redundant encodings, and select accessible colors.
- **Sources:** [USER-NOTES], current publisher/venue accessibility instructions. Checked 2026-09-01.

## FL-07 — Layout expresses structure without collision or waste

- **Nature:** General best practice.
- **Reviewer attack:** “Misalignment, overlap, inconsistent sizing, excessive whitespace, or arbitrary diagonals obscure grouping and flow.”
- **Check:** Inspect alignment, spacing, overlap, arrow crossings/direction, grouping, visual hierarchy, whitespace balance, and same-class element size.
- **Severity:** `S2` if comprehension suffers; `S3` presentation.
- **Exceptions / false positives:** Diagonal/irregular layout is valid when it encodes topology, geometry, or sequence better than a grid.
- **Repair direction:** Align/group by semantics, route arrows cleanly, and rebalance density.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE]. Checked 2026-09-01.

## FL-08 — Architecture/workflow figures match the technical text

- **Nature:** Hard internal-consistency condition.
- **Reviewer attack:** “The diagram shows components, trust paths, ordering, inputs, or outputs that the prose omits or contradicts.”
- **Check:** Cross-check actors, boundaries, labels, arrow direction, stage order, optional paths, inputs/outputs, and legend with in-scope overview/design. Separately ask whether the figure makes the design's governing relation visible; technical consistency cannot rescue an architecture diagram that communicates only a component inventory.
- **Severity:** `S0` if mismatch invalidates central reasoning; `S1`/`S2` otherwise.
- **Exceptions / false positives:** Diagrams intentionally abstract details; caption/text must state the abstraction where it matters.
- **Repair direction:** Reconcile one system model and mark omitted/optional paths explicitly.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL]. Checked 2026-09-01.

## Tables

## FL-09 — Table schema and comparison conditions are explicit

- **Nature:** Hard interpretability/fairness condition.
- **Reviewer attack:** “Rows and columns compare incomparable settings, or symbols/units/aggregation are undefined.”
- **Check:** Inspect row/column headers, units, direction of better, grouping, footnotes, missing-value symbols, normalization, hardware/workload condition, and alignment of decimal precision.
- **Severity:** `S1` for misleading central comparison; `S2` otherwise.
- **Exceptions / false positives:** Repeated units may be in caption/header rather than every cell.
- **Repair direction:** Add exact schema/conditions and use consistent precision/notation.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [USER-NOTES]. Checked 2026-09-01.

## FL-10 — Highlighting corresponds to a declared rule

- **Nature:** Hard integrity condition when emphasis encodes superiority; otherwise style.
- **Reviewer attack:** “Bold/underline/color selectively highlights favorable cells or ignores ties, uncertainty, and incomparable metrics.”
- **Check:** Determine the rule for best/second best, direction, statistical/practical tie, and missing results. Recompute when values are in scope.
- **Severity:** `S0` for deceptive selection; `S1` for incorrect headline emphasis; `S3` style.
- **Exceptions / false positives:** Highlighting a chosen configuration rather than a winner is valid if labeled.
- **Repair direction:** State/apply one rule and account for ties/uncertainty.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL]. Checked 2026-09-01.

## FL-11 — Table resizing does not destroy readability

- **Nature:** Diagnostic heuristic / template preference.
- **Reviewer attack:** “The table technically fits but becomes unreadably small or distorted.”
- **Check:** Inspect final rendering. `\resizebox{\linewidth}{!}{...}` is a possible last resort, not a default rule; it scales text indiscriminately and can hide structural excess.
- **Severity:** `S2` if unreadable; `S3` presentation.
- **Exceptions / false positives:** Modest proportional scaling can be acceptable within template legibility.
- **Repair direction:** Reduce columns/precision, split/rotate where allowed, redesign headers, or use approved scaling.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## Captions and callouts

## FL-12 — Caption is self-contained enough for correct reading

- **Nature:** General best practice.
- **Reviewer attack:** “I cannot interpret the figure/table without searching for dataset, metric, condition, abbreviations, or panel meaning.”
- **Check:** Verify object purpose, what is compared, essential setup/normalization, encodings, panel labels, uncertainty, takeaway, and any boundary needed to prevent an overbroad reading. Avoid duplicating a full paragraph.
- **Severity:** `S1` if central evidence is ambiguous; `S2` otherwise.
- **Exceptions / false positives:** Details can live in setup when caption supplies a precise pointer and remains interpretable.
- **Repair direction:** Add only information required for correct interpretation and a bounded takeaway; move extended analysis to prose.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [HEISER-STYLE]. Checked 2026-09-01.

## FL-13 — Prose callout states what the object establishes

- **Nature:** General best practice.
- **Reviewer attack:** “The paper says `Figure 5 shows the results` but never states the observation, comparison, or implication.”
- **Check:** Locate first callout near the object and subsequent claim uses. Verify every decision-relevant panel/element is explained, but do not require prose to narrate every decorative part.
- **Severity:** `S1` if evidence-to-claim link is absent; `S2` otherwise.
- **Exceptions / false positives:** A compact overview diagram may be explained across several nearby paragraphs.
- **Repair direction:** State the observed result with number/condition and bounded implication.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [ERNST]. Checked 2026-09-01.

## FL-14 — Caption punctuation follows complete-sentence and template logic

- **Nature:** House style / venue preference.
- **Reviewer attack:** Usually none unless inconsistency signals poor finishing or violates template.
- **Check:** Determine whether caption/subcaption is a complete sentence or fragment and follow current publisher/venue style. A universal “caption needs period, subcaption does not” rule is unsupported.
- **Severity:** `S3` for inconsistency/verified style issue; `S4` preference.
- **Exceptions / false positives:** Template examples and production rules differ.
- **Repair direction:** Apply verified venue/template convention consistently.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Live overlay may override.

## LaTeX, references, and typography

## FL-15 — The project compiles without unresolved structural errors

- **Nature:** Hard submission-quality condition.
- **Reviewer attack:** “The PDF contains missing references/citations, broken figures, overfull content, malformed math, or compilation-dependent omissions.”
- **Check:** When the full editable project is in scope, compile safely and inspect errors/warnings: undefined control sequence, missing file, unresolved ref/cite, multiply defined label, fatal font/image issue, and materially overfull/underfull boxes. Render pages for visual checks.
- **Severity:** `S0` if required PDF cannot compile/render; `S1` for missing content; `S2`/`S3` for layout warning by consequence.
- **Exceptions / false positives:** Not every warning is a defect; overfull boxes inside hidden/debug content or tiny tolerable protrusions need judgment.
- **Repair direction:** Fix root source/template issue and recompile; do not install toolchains without permission.
- **Sources:** [ACM-TEMPLATE], [USENIX-TEMPLATE], current venue instructions.

## FL-16 — Labels, references, and citations resolve to the intended object

- **Nature:** Hard correctness condition.
- **Reviewer attack:** “The paper points to the wrong figure/section/equation/reference or leaves a dangling placeholder.”
- **Check:** Inspect `\label`, `\ref`/`\autoref`/`\cref`/hyperlinks, equation numbering, panel references, citation keys, and prose nouns. Confirm label placement yields intended number.
- **Severity:** `S1` if evidence/argument is misdirected; `S2`/`S3` locally.
- **Exceptions / false positives:** Macro packages differ; validate rendered result rather than enforcing one command.
- **Repair direction:** Correct target/key/noun and use project convention consistently.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## FL-17 — Citation placement and spacing preserve meaning

- **Nature:** Hard attribution condition plus template style.
- **Reviewer attack:** “It is unclear which claim a citation supports, or a citation appears to endorse an entire paragraph.”
- **Check:** Place citations adjacent to supported claims, distinguish source attribution from examples, and verify `~\cite{}` or plain spacing under project/template conventions. `~` creates a nonbreaking space and is often intentional.
- **Severity:** `S1` for misattribution/missing support; `S2` ambiguity; `S3` spacing.
- **Exceptions / false positives:** A citation at a sentence boundary can support a well-defined preceding clause; repeated citations need not follow every mention.
- **Repair direction:** Move/add precise citations and follow template spacing; verify source support separately.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## FL-18 — Custom macros preserve semantics and portability

- **Nature:** General best practice; hard when expansion changes meaning/build.
- **Reviewer attack:** “System names, units, headings, or annotation macros produce inconsistent text, spacing bugs, hidden author notes, or template violations.”
- **Check:** Inspect custom name/term/unit macros, `\xspace` behavior, argument safety, capitalization, math/text mode, author-comment macros, and definition collisions. Verify rendered occurrences.
- **Severity:** `S0` for leaked confidential/review notes or compile failure; `S1` for semantic inconsistency; `S2`/`S3` otherwise.
- **Exceptions / false positives:** Macros for recurring system names/terms are useful; not every repeated term needs a macro.
- **Repair direction:** Centralize genuinely repeated tokens, remove annotations, avoid fragile spacing, and preserve template commands.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## FL-19 — Quotes, code, identifiers, and emphasis use semantic markup

- **Nature:** General best practice / template preference.
- **Reviewer attack:** “Typography fails to distinguish literal code, variables, emphasized terms, and quotations, or manual characters render incorrectly.”
- **Check:** Inspect LaTeX quotes, `\texttt` for literal code/identifiers where appropriate, math variables in math mode, `\emph`/project convention for emphasis, escaping, and function-call parentheses. Do not italicize every “special noun” mechanically.
- **Severity:** `S2` if semantic distinction is lost; `S3` typography.
- **Exceptions / false positives:** System names often use project macros and may not be monospaced; follow venue/project convention.
- **Repair direction:** Use semantic commands/macros and consistent identifier spelling.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## FL-20 — Mathematical notation is typed and defined correctly

- **Nature:** Hard correctness condition.
- **Reviewer attack:** “Symbols change meaning, domains/operators are undefined, units appear as variables, or text arithmetic is ambiguous.”
- **Check:** Define symbols near first use, domains, indices, vectors/sets, operators, conditions, and units; check equation/prose consistency, punctuation, `\pm`, minus/hyphen, subscripts, and dimensional consistency.
- **Severity:** `S0` for invalid central derivation; `S1` for ambiguous core notation; `S2`/`S3` local.
- **Exceptions / false positives:** Standard notation need not be exhaustively defined if unambiguous to audience.
- **Repair direction:** Define/reconcile notation, use math mode/semantic macros, and correct dimensional errors.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE]. Checked 2026-09-01.

## FL-21 — Heading and spacing hacks obey the current template

- **Nature:** Venue/template requirement or house style, never universal.
- **Reviewer attack:** “Manual negative space, scaled bullets, faux headings, or font changes evade page limits or break accessibility/production.”
- **Check:** Inspect manual `\vspace`, font scaling, `\noindent\textbf`, custom third/fourth-level headings, list compression, margin changes, and line spacing against official instructions. Render for conspicuous crowding.
- **Severity:** `S0` for verified page-limit/template evasion; `S1` for material readability; `S3` for benign inconsistency.
- **Exceptions / false positives:** Template-supported run-in headings and list options are valid. The user's ACM macros are local examples, not universal commands.
- **Repair direction:** Use official sectioning/list commands and permitted spacing; remove hacks.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE], live venue rules.

## FL-22 — Float placement supports reading and follows constraints

- **Nature:** General best practice plus template preference.
- **Reviewer attack:** “A figure/table appears far from first use, interrupts reading, or violates float/page rules.”
- **Check:** Inspect rendered proximity, page/column balance, ordering, top/bottom/mid-page behavior, float queues, and whether a two-column figure uses space effectively. Top/bottom is a useful default, not a universal prohibition on mid-page placement.
- **Severity:** `S2` when interpretation suffers; `S3`/`S4` layout; venue violation per overlay.
- **Exceptions / false positives:** LaTeX may move floats for valid layout reasons; exact adjacency is not always possible.
- **Repair direction:** Adjust callout/order/float options within template, redesign size/aspect, or add a precise reference.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Checked 2026-09-01.

## FL-23 — Asset format preserves quality and submission compatibility

- **Nature:** General best practice plus venue requirement.
- **Reviewer attack:** “Rasterized diagrams/text are blurry, fonts are missing, PDF assets are incompatible, or the final submission is oversized.”
- **Check:** Prefer vector for line art/plots when supported; use sufficient-resolution raster for photographs/heatmaps; inspect font embedding, transparency, crop boxes, color space, file size, and venue-accepted formats.
- **Severity:** `S1` if evidence unreadable or submission invalid; `S2`/`S3` quality.
- **Exceptions / false positives:** PDF is not universally required, and raster is appropriate for inherently raster data.
- **Repair direction:** Export in suitable vector/raster format at final size and verify rendered PDF.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE], live venue rules.

## Render audit checklist

When rendering is in scope, inspect every page at normal reading scale and zoomed detail:

- missing glyphs, tofu, broken ligatures, encoding;
- clipped/overlapping text, equations, floats, footnotes, headers;
- unreadably small figures/tables/captions;
- orphan headings, awkward column/page breaks, conspicuous whitespace;
- unresolved placeholders, author notes, anonymity leaks;
- link/citation/reference appearance;
- figure/table order and callout proximity;
- page count and required metadata under live venue rules.

Do not report “LaTeX passes” from compilation alone; compilation and visual inspection answer different questions.
