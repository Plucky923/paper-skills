# Figures, Tables, Captions, Math, and LaTeX

If both source and rendered output are explicitly in scope, examine both. Correct source does not show readable output. Visual quality does not show truthful encoding.

Obey template and venue instructions before local preferences.
## Figures and plots

## FL-01 — Each figure has one decision-related message

- **Nature:** General best practice.
- **Reviewer attack:** “The figure is decorative, combines unrelated stories, or requires reconstructing its purpose from the paper.”
- **Check:** Record the figure's reader question and conclusion. For the first figures, use [examples-figures-results.md](examples-figures-results.md). Find its mismatch, boundary, causal path, system model, workflow, or intellectual move. Make sure that panels and elements contribute to that message. Examine the text's use of the figure in the argument.
- **Severity:** `S2`. `S1` if a central claim depends on an unreadable/ambiguous figure.
- **Exceptions / false positives:** Overview figures can give architecture or workflows instead of numerical claims. A coherent purpose is still necessary.
- **Repair direction:** Give repair options: unrelated-content removal, different panels, or a clear question and conclusion. Use only supported annotations.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [HEISER-STYLE].

## FL-02 — Visual encodings have clear, stable semantics

- **Nature:** Condition for interpretability.
- **Reviewer attack:** “Color, shape, line, arrow, box, position, or size appears meaningful but is undefined or changes meaning across figures.”
- **Check:** Make an encoding inventory. Give each encoding its legend, caption, or text definition. Compare the same concepts and baselines across figures in scope.
- **Severity:** `S1` if it can reverse interpretation. `S2` recurring. `S3` cosmetic.
- **Exceptions / false positives:** Unambiguous spatial structure does not make extended explanation necessary. Decorative style must stay different from data encoding.
- **Repair direction:** Give repair options: encoding definitions, removal, or use with the same meaning. Give redundant shapes, patterns, or text for important distinctions.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE].

## FL-03 — Graphs do not visually exaggerate or suppress results

- **Nature:** Condition for research integrity.
- **Reviewer attack:** “Axis, scale, aspect ratio, normalization, sorting, cropping, or chart type was chosen to manufacture an advantage.”
- **Check:** Examine origin, range, linear or logarithmic scales, aspect ratio, dual axes, and broken axes. Examine normalization denominators, missing values, sequence, bins, aggregation, and representation. Compare visual magnitude with numerical effect.
- **Severity:** `S0` for misleading presentation that changes conclusions. `S1` for ambiguous headline result.
- **Exceptions / false positives:** Truncated axes, logarithmic scales, and short vertical dimensions can be applicable with labels and question-specific rationale.
- **Repair direction:** Use an accurate scale and representation. Give transformations. Add absolute or reference values where necessary. Keep visual advantage subordinate to quantitative truth.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [USER-NOTES] as normalized.

## FL-04 — Uncertainty and missing data are visible

- **Nature:** Condition when noisy or stochastic evidence gives claim evidence.
- **Reviewer attack:** “The plot implies exact stable values while variability, failed runs, censoring, or missing cases are hidden.”
- **Check:** Examine error bars, bands, distributions, uncertainty definitions, sample sizes, missing markers, clipped values, and timeout or failure treatment. Make sure that readers can see the uncertainty bars.
- **Severity:** `S1` if uncertainty can change conclusion. `S2` in other cases.
- **Exceptions / false positives:** Exact deterministic data do not make error bars necessary. Give the rationale if unclear.
- **Repair direction:** Show applicable uncertainty. Give its definition. Show missing or failed cases. Put necessary limits on conclusions.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH].

## FL-05 — Baseline and “ours” styling does not replace labels or fairness

- **Nature:** General best practice / house style.
- **Reviewer attack:** “The plot privileges the proposed method through ordering/emphasis while identities or comparison conditions remain unclear.”
- **Check:** Make sure that readers can identify each series and see differences between series. The same colors and sequence can help. Rightmost placement or bold text for `ours` is optional. Keep emphasis from hiding data or implying a result.
- **Severity:** `S2` if misleading/ambiguous. `S3`/`S4` style.
- **Exceptions / false positives:** Emphasis is permitted with equal data legibility.
- **Repair direction:** Give clear labels. Use the same labels across figures. Keep emphasis subordinate to accurate values.
- **Sources:** [USER-NOTES] as normalized, [HEISER-BENCH].

## FL-06 — Figures stay readable at final size and common viewing modes

- **Nature:** General best practice. Accessibility can be official policy.
- **Reviewer attack:** “Text, lines, markers, or panel labels are unreadable in two-column size, grayscale, print, or for color-vision deficiency.”
- **Check:** Render at final size. Examine fonts, strokes, markers, contrast, grayscale differences, color palette, and dependence on zoom. Compare figure and body text without a universal same-size requirement.
- **Severity:** `S1` if central evidence cannot be read. `S2` recurring. `S3` detail. Official accessibility violation per overlay.
- **Exceptions / false positives:** Dense diagrams can use smaller secondary labels if readable and outside decisive evidence.
- **Repair direction:** Simplify the figure. Increase necessary sizes. Use redundant encodings. Select accessible colors.
- **Sources:** [USER-NOTES], publisher/venue accessibility instructions in effect.

## FL-07 — Layout expresses structure without collision or waste

- **Nature:** General best practice.
- **Reviewer attack:** “Misalignment, overlap, inconsistent sizing, excessive whitespace, or arbitrary diagonals obscure grouping and flow.”
- **Check:** Examine alignment, spacing, overlap, arrow crossings, arrow direction, grouping, hierarchy, whitespace, and sizes of elements in the same class.
- **Severity:** `S2` if comprehension suffers. `S3` presentation.
- **Exceptions / false positives:** Irregular layouts can give topology, geometry, or sequence more clearly than grids.
- **Repair direction:** Use semantic groups and alignment. Give arrows clear paths. Make density balanced.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE].

## FL-08 — Architecture/workflow figures match the technical text

- **Nature:** Condition for internal consistency.
- **Reviewer attack:** “The diagram shows components, trust paths, ordering, inputs, or outputs that the prose omits or contradicts.”
- **Check:** Compare actors, boundaries, labels, and arrow direction with overview or design text in scope. Compare stage sequence, optional paths, inputs, outputs, and legends with that text. In a different check, examine whether the figure shows the governing design relation. Technical consistency alone does not show that a component inventory communicates the design.
- **Severity:** `S0` if mismatch invalidates central reasoning. `S1`/`S2` in other cases.
- **Exceptions / false positives:** Diagrams can have fewer details. Captions or text must give abstraction boundaries that affect conclusions.
- **Repair direction:** Use the same system model throughout. Give clear omitted or optional paths.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [LEVIN-REDELL].

## Tables

## FL-09 — Table schema and comparison conditions are clear

- **Nature:** Condition for interpretability and fairness.
- **Reviewer attack:** “Rows and columns compare incomparable settings, or symbols/units/aggregation are undefined.”
- **Check:** Examine headers, units, improvement direction, grouping, footnotes, missing-value symbols, normalization, hardware, workload, and decimal precision.
- **Severity:** `S1` for misleading central comparison. `S2` in other cases.
- **Exceptions / false positives:** Captions or headers can give units without repetition in each cell.
- **Repair direction:** Give specified schema and conditions. Use the same precision and notation.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [USER-NOTES].

## FL-10 — Highlighting corresponds to a declared rule

- **Nature:** Condition for integrity when emphasis encodes superiority. For other cases, style.
- **Reviewer attack:** “Bold/underline/color selectively highlights favorable cells or ignores ties, uncertainty, and incomparable metrics.”
- **Check:** Find the rule for best or second-best values, improvement direction, statistical or practical ties, and missing results. If values are in scope, calculate highlighted rankings again.
- **Severity:** `S0` for deceptive selection. `S1` for incorrect headline emphasis. `S3` style.
- **Exceptions / false positives:** Highlighted configurations can show selections instead of winners with a clear label.
- **Repair direction:** Give one clear rule. Apply it to ties and uncertainty as well as other values.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL].

## FL-11 — Table resizing does not destroy readability

- **Nature:** Diagnostic heuristic / template preference.
- **Reviewer attack:** “The table technically fits but becomes unreadably small or distorted.”
- **Check:** Examine the final rendering. Use `\resizebox{\linewidth}{!}{...}` only as a possible last option. It scales all text and can hide excessive structure.
- **Severity:** `S2` if unreadable. `S3` presentation.
- **Exceptions / false positives:** Small proportional scaling is permitted within template legibility.
- **Repair direction:** Give repair options: fewer columns or digits, permitted division or rotation, changed headers, or permitted scaling.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE].

## Captions and callouts

## FL-12 — Caption is self-contained enough for correct reading

- **Nature:** General best practice.
- **Reviewer attack:** “I cannot interpret the figure/table without searching for dataset, metric, condition, abbreviations, or panel meaning.”
- **Check:** Examine purpose, comparison, necessary setup, normalization, encodings, panels, uncertainty, conclusion, and boundaries against overgeneralization. Keep a full paragraph of repeated text outside the caption.
- **Severity:** `S1` if central evidence is ambiguous. `S2` in other cases.
- **Exceptions / false positives:** Setup can contain details with an accurate caption reference and an interpretable caption.
- **Repair direction:** Give only necessary interpretation information and a bounded conclusion. Put extended analysis in prose.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [HEISER-STYLE].

## FL-13 — Prose callout states what the object shows

- **Nature:** General best practice.
- **Reviewer attack:** “The paper says `Figure 5 shows the results` but never states the observation, comparison, or implication.”
- **Check:** Find the first callout near the object. Find subsequent claim uses. Make sure that each element related to the decision has an explanation. A full prose account of decorative parts is not necessary.
- **Severity:** `S1` if evidence-to-claim link is absent. `S2` in other cases.
- **Exceptions / false positives:** Multiple paragraphs near the diagram can give a short overview diagram's explanation.
- **Repair direction:** Give the observed result, number, condition, and bounded implication.
- **Sources:** [USER-NOTES], [SYSTEMS-GUIDE], [ERNST].

## FL-14 — Caption punctuation obeys sentence and template rules

- **Nature:** House style / venue preference.
- **Reviewer attack:** Usually none unless inconsistency signals poor finishing or violates template.
- **Check:** Find whether the caption or subcaption is a sentence or fragment. Obey publisher or venue style in effect. No universal caption/subcaption period rule applies.
- **Severity:** `S3` for inconsistency/verified style issue. `S4` preference.
- **Exceptions / false positives:** Template examples and production rules can differ.
- **Repair direction:** Obey the verified venue or template convention throughout.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE]. Live overlay can override.

## LaTeX, references, and typography

## FL-15 — The project compiles without unresolved structural errors

- **Nature:** Condition for submission quality.
- **Reviewer attack:** “The PDF contains missing references/citations, broken figures, overfull content, malformed math, or compilation-dependent omissions.”
- **Check:** If the full editable project is in scope, compile with the required isolation. Examine errors and warnings. Include undefined commands, missing files, unresolved references or citations, and duplicate labels. Include fatal font or image faults and box warnings that affect readability. Render pages for visual checks.
- **Severity:** `S0` if required PDF cannot compile/render. `S1` for missing content. `S2`/`S3` for layout warning by consequence.
- **Exceptions / false positives:** Not all warnings are defects. Give individual judgments for hidden or debug boxes and small protrusions.
- **Repair direction:** Correct the root source or template fault. Compile again. Before toolchain installation, get authority.
- **Sources:** [ACM-TEMPLATE], [USENIX-TEMPLATE], venue instructions in effect.

## FL-16 — Labels, references, and citations resolve to the intended object

- **Nature:** Condition for correctness.
- **Reviewer attack:** “The paper points to the wrong figure/section/equation/reference or leaves a dangling placeholder.”
- **Check:** Examine `\label`, `\ref`/`\autoref`/`\cref`, hyperlinks, equation numbers, panel references, citation keys, and prose nouns. Make sure that label placement gives the intended number.
- **Severity:** `S1` if evidence/argument is misdirected. `S2`/`S3` locally.
- **Exceptions / false positives:** Macro packages differ. Examine rendered output instead of one universal command form.
- **Repair direction:** Correct the target, key, or noun. Use the same project convention throughout.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE].

## FL-17 — Citation placement and spacing keep meaning

- **Nature:** Condition for attribution plus template style.
- **Reviewer attack:** “It is unclear which claim a citation supports, or a citation appears to endorse an entire paragraph.”
- **Check:** Examine citation adjacency to supported claims. Do a check of the difference between source attribution and examples. Compare `~\cite{}` or plain spacing with project and template conventions. `~` makes a nonbreaking space and is often intentional.
- **Severity:** `S1` for misattribution/missing support. `S2` ambiguity. `S3` spacing.
- **Exceptions / false positives:** Boundary citations can give evidence for a clear preceding clause. Citation repetition after each mention is not necessary.
- **Repair direction:** Give accurate adjacent citations. Obey template spacing. Examine source evidence in different checks.
- **Sources:** [USER-NOTES] as normalized, [ERNST], [ACM-TEMPLATE], [USENIX-TEMPLATE].

## FL-18 — Custom macros keep semantics and portability

- **Nature:** General best practice. Condition when macro expansion changes meaning or builds.
- **Reviewer attack:** “System names, units, headings, or annotation macros produce inconsistent text, spacing bugs, hidden author notes, or template violations.”
- **Check:** Examine custom name, term, and unit macros, `\xspace`, arguments, capitalization, math or text mode, author-comment macros, and definition collisions. Examine rendered occurrences.
- **Severity:** `S0` for leaked confidential/review notes or compile failure. `S1` for semantic inconsistency. `S2`/`S3` in other cases.
- **Exceptions / false positives:** Macros for repeated system names or terms can help. Macros for all repeated terms are not necessary.
- **Repair direction:** Use central definitions for repeated tokens where this helps interpretation. Remove annotations. Use stable spacing. Keep template commands.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE].

## FL-19 — Quotes, code, identifiers, and emphasis use semantic markup

- **Nature:** General best practice / template preference.
- **Reviewer attack:** “Typography fails to distinguish literal code, variables, emphasized terms, and quotations, or manual characters render incorrectly.”
- **Check:** Examine LaTeX quotes, literal code or identifier `\texttt`, math-mode variables, `\emph` or project emphasis conventions, escapes, and function-call parentheses. Do not use automatic italics for each special noun.
- **Severity:** `S2` if semantic distinction is lost. `S3` typography.
- **Exceptions / false positives:** System-name macros can use different typefaces. Obey venue and project conventions.
- **Repair direction:** Use semantic commands or macros. Use the same identifier spelling.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE].

## FL-20 — Mathematical notation is typed and defined correctly

- **Nature:** Condition for correctness.
- **Reviewer attack:** “Symbols change meaning, domains/operators are undefined, units appear as variables, or text arithmetic is ambiguous.”
- **Check:** Examine first-use symbol definitions, domains, indices, vectors, sets, operators, conditions, and units. Compare equations and prose. Examine punctuation, `\pm`, minus signs, hyphens, subscripts, and dimensions.
- **Severity:** `S0` for invalid central derivation. `S1` for ambiguous core notation. `S2`/`S3` local.
- **Exceptions / false positives:** Standard notation with clear audience meaning does not make full definitions necessary.
- **Repair direction:** Give notation definitions that agree with each other. Use math mode or semantic macros. Correct dimensional errors.
- **Sources:** [USER-NOTES], [ERNST], [HEISER-STYLE].

## FL-21 — Heading and spacing hacks obey the template in effect

- **Nature:** Venue/template requirement or house style. It is not universal.
- **Reviewer attack:** “Manual negative space, scaled bullets, faux headings, or font changes evade page limits or break accessibility/production.”
- **Check:** Compare manual `\vspace`, font scaling, `\noindent\textbf`, custom third-level or fourth-level headings, compressed lists, margins, and line spacing with official instructions. Render for excessive crowding.
- **Severity:** `S0` for verified page-limit/template evasion. `S1` for important readability defects. `S3` for benign inconsistency.
- **Exceptions / false positives:** Template-supported run-in headings and list options are permitted. User ACM macros are local examples.
- **Repair direction:** Use official section and list commands. Use permitted spacing. Remove unsupported adjustments.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE], live venue rules.

## FL-22 — Float placement helps reading and obeys constraints

- **Nature:** General best practice plus template preference.
- **Reviewer attack:** “A figure/table appears far from first use, interrupts reading, or violates float/page rules.”
- **Check:** Examine callout distance, page and column balance, sequence, and top, bottom, or middle placement. Examine float queues and two-column space use. Top or bottom placement is a good default. Mid-page placement is permitted where applicable.
- **Severity:** `S2` when interpretation suffers. `S3`/`S4` layout. Venue violation per overlay.
- **Exceptions / false positives:** LaTeX can move floats for correct layout reasons. Immediate adjacency is not always possible.
- **Repair direction:** Give repair options: permitted callout, sequence, or float changes, changed size or aspect ratio, or an accurate reference.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE].

## FL-23 — Asset format keeps quality and submission compatibility

- **Nature:** General best practice plus venue requirement.
- **Reviewer attack:** “Rasterized diagrams/text are blurry, fonts are missing, PDF assets are incompatible, or the final submission is oversized.”
- **Check:** If supported, use vector formats for line art and plots. Use sufficient-resolution raster formats for photographs or heatmaps. Examine font embedding, transparency, crop boxes, color space, file size, and accepted formats.
- **Severity:** `S1` if evidence unreadable or submission invalid. `S2`/`S3` quality.
- **Exceptions / false positives:** PDF is not universally necessary. Raster formats are applicable for raster data.
- **Repair direction:** Export an applicable vector or raster format at final size. Examine the rendered PDF.
- **Sources:** [USER-NOTES] as normalized, [ACM-TEMPLATE], [USENIX-TEMPLATE], live venue rules.

## Render audit checklist

If rendering is in scope, examine each page at normal reading scale. Also examine enlarged details.

- Missing glyphs, tofu, broken ligatures, and encoding.
- Clipped or overlapping text, equations, floats, footnotes, and headers.
- Figures, tables, or captions too small to read.
- Orphan headings, difficult column or page breaks, and excessive whitespace.
- Unresolved placeholders, author notes, and anonymity leaks.
- Link, citation, and reference appearance.
- Figure or table sequence and callout distance.
- Page count and required metadata with venue rules in effect.

Give different compilation and visual-inspection results. Compilation alone does not show a full LaTeX pass.
