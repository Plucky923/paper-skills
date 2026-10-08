# Evaluation Validity and Evidence

Evaluation connects observations to claims. Examine whether the design answers the question, measurements have evidence for accuracy, and conclusions stay within evidence boundaries.

Make ablation, significance tests, or benchmark suites necessary only for questions about manuscript claims.
## EV-01 — Each central claim has an evidence plan

- **Nature:** Condition for scientific validity.
- **Reviewer attack:** “The paper's strongest contribution is never directly evaluated.”
- **Check:** Make a claim-to-evidence matrix. Include each claimed correctness, performance, overhead, scalability, robustness, usability, security, generality, and practicality property. Record evidence type: experiment, proof, analysis, case study, artifact, or external fact. Use the [thesis-support hierarchy](thesis-and-story.md). Make sure that decisive evidence and headline results include primary claims before secondary measurements.
- **Severity:** `S0` for a central conclusion without evidence. Use `S1` for partial coverage. Use `S2` for secondary claims.
- **Exceptions / false positives:** Cited primary evidence can show premises. The cited source must give the same conditions.
- **Repair direction:** Give repair options: an applicable test with evidence from observations, a claim with evidence, or claim removal. Use only results with evidence.
- **Sources:** [OSDI-CFP], [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE].

## EV-02 — Evidence is selected by recoverable scientific questions

- **Nature:** General best practice.
- **Reviewer attack:** “The evaluation is a collection of favorable plots rather than tests of explicit hypotheses or system questions.”
- **Check:** For each experiment, proof, case study, or operational observation, find its question, outcomes, conditions, controls, permitted inference, and challenged claim. The question can be clear or result from a closely related finding and intervention. Find evidence objects without a decision function.
- **Severity:** `S1` when the experiment design cannot show claims. For other cases, `S2`.
- **Exceptions / false positives:** A research-question list or one evaluation section is optional. Exploratory, measurement, and operational studies can interleave descriptive questions, method, observation, and intervention. Each inference must stay auditable.
- **Repair direction:** Organize experiments by questions. Remove non-evidentiary plots or give them lower prominence.
- **Sources:** [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE], [HEISER-BENCH].

## EV-03 — The study design matches the inference

- **Nature:** Condition for scientific validity.
- **Reviewer attack:** “The evaluation is observational but the paper draws a causal conclusion,” or “a microbenchmark is used to claim end-to-end benefit.”
- **Check:** Give each inference its type: descriptive, comparative, causal, predictive, correctness, or feasibility. Compare interventions, controls, randomization or pairing, trace provenance, and measurement level with that inference.
- **Severity:** `S0` for a central invalid inference. For other cases, `S1`.
- **Exceptions / false positives:** Controlled systems experiments can show causal effects without random population samples. Generalization stays within tested conditions.
- **Repair direction:** Give repair options: changed design, added controls, multiple evidence forms, or a narrower conclusion type.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH].

## EV-04 — Baselines answer the comparison necessary for the decision

- **Nature:** Condition for fairness.
- **Reviewer attack:** “The paper avoids the strongest, simplest, most current, or operationally relevant alternative.”
- **Check:** Examine applicable baseline classes. Include practice in use, closest prior research, and strong specialized methods. Include strawman baselines with few mechanisms, system ablations, and meaningful oracles or upper bounds. Make only classes related to the claim and deployment choice necessary.
- **Severity:** `S1`. Use `S0` when baseline omission makes the headline advantage knowingly misleading.
- **Exceptions / false positives:** Unavailable or proprietary baselines can be excluded with evidence, limitations, and a defensible substitute. Each cited work is not mandatory.
- **Repair direction:** Give repair options: a configured missing comparator, exclusion rationale, or narrower comparative claims.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [OSDI-CFP].

## EV-05 — Baseline configurations are fair and reproducible

- **Nature:** Condition for fairness.
- **Reviewer attack:** “The proposed system is tuned while baselines use defaults, obsolete versions, weaker hardware, fewer resources, or incompatible goals.”
- **Check:** Compare versions, patches, hardware allocation, parallelism, compilation, warmup, tuning budgets, parameter search, stopping criteria, features, and correctness targets. Make sure that tuning does not use test data.
- **Severity:** `S0` for manipulation that changes conclusions. For other cases, `S1`.
- **Exceptions / false positives:** Default settings can represent practice in use with rationale. Defaults that affect conclusions make sensitivity checks necessary.
- **Repair direction:** Make resources, effort, and objectives equal. Give settings. Add sensitivity evidence or limits on the comparison.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL].

## EV-06 — Workloads represent the claim domain

- **Nature:** Condition for external validity in broad claims.
- **Reviewer attack:** “The result depends on toy, outdated, cherry-picked, or nonrepresentative workloads.”
- **Check:** Examine workload sources, versions, scale, diversity, realism, skew, arrival patterns, and read/write mix. Examine failures, hardware/software interactions, and known bias. Compare the tested domain with claim quantifiers.
- **Severity:** `S1`. Use `S0` when the selected workload contradicts the advertised use case.
- **Exceptions / false positives:** A microbenchmark can isolate a mechanism with a clear label. End-to-end claims must still have sufficient end-to-end evidence.
- **Repair direction:** Give repair options: representative or diverse cases, scope rationale, or narrower generalization.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE].

## EV-07 — Calibration, training, tuning, and evaluation data are separated

- **Nature:** Condition for validity with adaptation or search.
- **Reviewer attack:** “The method overfits the workloads or traces used to select its rules, parameters, prompts, thresholds, or model.”
- **Check:** Record provenance and partitions for training, profiling, tuning, validation, test, and case-study data. Find repeated test-set feedback and leakage through handcrafted choices.
- **Severity:** `S0` for central results with data leakage. For other cases, `S1`.
- **Exceptions / false positives:** Online or adaptive systems can learn from deployment traffic. Evaluation must include that lifecycle and applicable future or held-out outcomes.
- **Repair direction:** Give repair options: disjoint evaluation, nested selection, temporal partitions, or a clear in-sample behavior account.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH].

## EV-08 — Metrics correspond to user/system objectives

- **Nature:** Condition for construct validity.
- **Reviewer attack:** “The chosen proxy improves while the outcome users or operators care about may not.”
- **Check:** Give each metric's definition, direction, unit, aggregation, and relation to the objective. Examine proxies, denominator omissions, averages that hide tails, and throughput without latency. Examine accuracy without cost or error asymmetry.
- **Severity:** `S1`. Use `S0` for a headline conclusion with an invalid metric.
- **Exceptions / false positives:** Proxies are permitted with validation or clear proxy status.
- **Repair direction:** Give direct outcomes or proxy validation. Add complementary metrics and boundaries.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [ERNST].

## EV-09 — Numerators, denominators, aggregation, and units are clear

- **Nature:** Condition for interpretability.
- **Reviewer attack:** “The reported percentage or average has no auditable population, weighting, or unit.”
- **Check:** Find sample units, denominators, inclusion and exclusion, weighting, macro/micro averaging, percentile definitions, time windows, and unit conversions. If data are in scope, calculate values with short formulas again.
- **Severity:** `S1` for headline ambiguity or error. Use `S2`/`S3` for local findings.
- **Exceptions / false positives:** Short captions can refer to setup details. A full review must have those details somewhere in scope.
- **Repair direction:** Give population, formula, and unit. If this helps interpretation, show absolute values beside ratios. Correct arithmetic.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [USER-NOTES].

## EV-10 — The measured boundary includes all costs that affect conclusions

- **Nature:** Condition for fairness.
- **Reviewer attack:** “Speedup/efficiency excludes setup, preprocessing, retraining, migration, recovery, network transfer, client work, hardware cost, or operator labor.”
- **Check:** Draw measurement start and end boundaries. Draw resource boundaries. Examine amortization, caching, cold and warm state, background work, subsequent cleanup, and transferred costs.
- **Severity:** `S0` for intentional misrepresentation or misrepresentation that changes conclusions. For other cases, `S1`.
- **Exceptions / false positives:** Component measurements can isolate mechanisms with clear labels. They do not show total-system claims.
- **Repair direction:** Give end-to-end and component costs. Give amortization and deployment-frequency rationale. Put necessary limits on claims.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL].

## EV-11 — Measurement procedure controls transient and environmental effects

- **Nature:** Condition for measurement validity when effects affect conclusions.
- **Reviewer attack:** “Results may be artifacts of warmup, caching, frequency scaling, background load, placement, network variance, garbage collection, JIT, or run order.”
- **Check:** Examine warmup, steady-state detection, cache policy, randomization or interleaving, pinning or placement, and isolation. Examine clocks, timers, run length, cooldown, environment monitoring, and outlier policy.
- **Severity:** `S1` when uncontrolled effects are comparable to the gain. For other cases, `S2`.
- **Exceptions / false positives:** Controls depend on the system. CPU pinning is unnecessary without an effect on the claim or measurement.
- **Repair direction:** Give repair options for each factor: control, randomization, pairing, monitoring, or a clear model. Repeat in representative conditions.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL].

## EV-12 — Replication and variability are reported

- **Nature:** General best practice. It is a condition when stochastic or noisy results give evidence for a claim.
- **Reviewer attack:** “A single run or unreported variability cannot establish that the observed difference is stable.”
- **Check:** Find independent repetitions, experimental units, seeds, within-run and between-run variance, error bars or intervals, and agreement between aggregation and design. Do a check of the difference between repeated measurements and independent samples.
- **Severity:** `S1` when uncertainty could reverse the central conclusion. For other cases, `S2`.
- **Exceptions / false positives:** Deterministic exhaustive proof or checks can justify other evidence forms. An unusually expensive full deployment can also justify alternatives. Uncertainty and limitations stay necessary.
- **Repair direction:** Repeat independent units. Give distributions or intervals. Give seeds. Put necessary limits on stability claims.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH].

## EV-13 — Statistical analysis fits the design and question

- **Nature:** Condition when the paper uses inferential statistics. For other cases, a conditional best practice.
- **Reviewer attack:** “The test assumes independence/normality it does not have, performs uncorrected multiple comparisons, or uses p-values as effect magnitude.”
- **Check:** Examine experimental units, pairing, distribution assumptions, repeated measures, censoring, multiple tests, effect sizes, uncertainty intervals, and practical relevance. Find ambiguity in `significant`.
- **Severity:** `S1` for an invalid central inference. Use `S2` for incomplete reporting.
- **Exceptions / false positives:** Statistical significance tests are not mandatory for each deterministic or controlled benchmark. Uncertainty treatment depends on measurement noise and claims.
- **Repair direction:** Give an applicable model, test, or interval. Give effect size or descriptive conclusions as applicable.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH].

## EV-14 — End-to-end evidence and microanalysis play different roles

- **Nature:** General best practice.
- **Reviewer attack:** “End-to-end plots show an effect but not why; microbenchmarks show a fast primitive but not system benefit.”
- **Check:** Give end-to-end experiments their practical outcome role. Give component experiments their mechanism or causal explanation role. Make both necessary only for claims at both levels.
- **Severity:** `S1` when the missing level leaves the central claim without evidence. For other cases, `S2`.
- **Exceptions / false positives:** Component papers and measurement studies can concentrate on one level.
- **Repair direction:** Give repair options: the missing evidence level, its causal relation, or a narrower contribution.
- **Sources:** [SYSTEMS-GUIDE], [HEISER-BENCH], [LEVIN-REDELL].

## EV-15 — Ablation is used when component necessity is claimed

- **Nature:** Conditional best practice. It is not universal.
- **Reviewer attack:** “The paper attributes gains to component X without isolating X from co-varying components.”
- **Check:** Find claims about necessity, contribution, interaction, or co-design. If present, examine removal, substitution, or factorial evidence. Make sure that removal leaves a meaningful functioning system.
- **Severity:** `S1` for central attribution without evidence. For other cases, `S2`.
- **Exceptions / false positives:** Ablation can be impossible or meaningless for inseparable invariants, safety mechanisms, or one-piece algorithms. Analysis or focused evidence can be substitutes.
- **Repair direction:** Give repair options: a correct isolation study, evidence for inseparability, or removal of single-component attribution.
- **Sources:** [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE], [JENSEN-SYSTEMS-SKILL].

## EV-16 — Sensitivity, scalability, and operating envelope are tested

- **Nature:** Condition for robustness or scalability claims. For other cases, a conditional check.
- **Reviewer attack:** “The result holds at one favorable parameter point and may collapse under scale, skew, load, failure, or hardware variation.”
- **Check:** Select factors from system assumptions and claim domain. Examine ranges, interactions, saturation, phase changes, and failure points. Additional parameter plots alone are insufficient.
- **Severity:** `S1` for broad claims without evidence. Use `S2` for incomplete characterization.
- **Exceptions / false positives:** Parameter sweeps are not necessary without a mechanism or deployment relation.
- **Repair direction:** Do tests of ranges and boundaries related to the decision. Give the safe or efficient operating envelope. Put limits on claims.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [OSDI-CFP].

## EV-17 — Negative, null, and failure results are not hidden

- **Nature:** Condition for reporting integrity.
- **Reviewer attack:** “Only favorable workloads/configurations/metrics are shown, so the conclusion may be selected after seeing results.”
- **Check:** Find missing benchmarks without explanations, truncated ranges, inconsistent subsets, dropped runs, post-hoc metrics, and missing failure rates. Compare the plan, text, tables, and artifacts in scope.
- **Severity:** `S0` for deceptive selective reporting. Use `S1` for primary unresolved selection risk.
- **Exceptions / false positives:** Full summaries or supplements can satisfy space limits. They do not justify silent omissions based on outcomes.
- **Repair direction:** Give all prespecified or related outcomes. Give exclusions. Give failure analysis. Put necessary limits on the claim.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH].

## EV-18 — Graphical presentation preserves quantitative truth

- **Nature:** Condition for integrity.
- **Reviewer attack:** “Axis truncation, aspect ratio, normalization, log scale, binning, or chart selection exaggerates advantage or hides regressions.”
- **Check:** Examine axis origin, range, scale, aspect ratio, units, normalization denominators, uncertainty, missing data, sorting, and aggregation. Examine dual axes, colors, sequence, and table or plot effects on perception. If data are in scope, calculate the visual implications again.
- **Severity:** `S0` for misleading presentation that changes conclusions. Use `S1` for an ambiguous headline plot. Use `S2` for correct but difficult displays.
- **Exceptions / false positives:** Nonzero axes, logarithmic scales, normalized values, and compressed aspect ratios are permitted with clear labels and question-specific rationale.
- **Repair direction:** Select an accurate representation that answers the research question. Give transformations. Add absolute values or another view where necessary.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [USER-NOTES] as normalized.

## EV-19 — Result interpretation separates observation, cause, and speculation

- **Nature:** Condition for inference validity.
- **Reviewer attack:** “The paper observes a correlation or performance change and invents a causal explanation without measurement.”
- **Check:** Do a check of differences between measurements, mechanism evidence, logical consequences, and hypotheses. Refer to design only when it predicts the effect.
- **Severity:** `S1` for a central explanation without evidence. Use `S2` for local findings.
- **Exceptions / false positives:** An explanation with evidence can help interpretation if its label clearly shows hypothesis status. It cannot serve as proof.
- **Repair direction:** Give repair options: diagnostic or ablation evidence, clear uncertainty, or removal of causal language.
- **Sources:** [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE], [ERNST].

## EV-20 — Practical significance accompanies relative gains

- **Nature:** General best practice. It is a condition when rhetoric depends on magnitude.
- **Reviewer attack:** “The relative improvement is large only because the baseline value is tiny, or the absolute change does not affect operation.”
- **Check:** Give absolute and relative values, resource or user consequences, thresholds or SLOs, effect sizes, and cost tradeoffs. Find excessive significant digits and qualitative labels without evidence.
- **Severity:** `S1` for exaggerated headline impact that changes conclusions. For other cases, `S2`.
- **Exceptions / false positives:** Small absolute changes can matter near hard thresholds. The threshold must have an explanation.
- **Repair direction:** Give absolute scale, context, and tradeoff. Make sure that adjectives and precision agree with evidence.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [USER-NOTES].

## EV-21 — Reproducibility information is sufficient to audit results

- **Nature:** General best practice. It can be a venue or artifact requirement.
- **Reviewer attack:** “Versions, environment, commands, data provenance, or randomness are insufficient to recreate the reported experiment.”
- **Check:** Examine hardware and software versions, topology, builds, configuration, workload generation, seeds, commands, sequence, repetitions, analysis, figure generation, and nondefault settings.
- **Severity:** `S1` when missing information prevents confidence in central measurements. Use `S2` for missing secondary detail. Use `S0` for a verified submission-rule violation.
- **Exceptions / false positives:** Security, privacy, licensing, or infrastructure limits can restrict release. Methodology and alternative access or validation must still give the maximum available detail.
- **Repair direction:** Give accurate environments and procedures. Archive inputs and outputs. Obey artifact rules in effect.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT], [SIGPLAN-EMPIRICAL].

## EV-22 — Evaluation limitations bound the conclusion

- **Nature:** Condition for accuracy.
- **Reviewer attack:** “The conclusion generalizes beyond tested systems, traces, hardware, scale, geography, users, or time.”
- **Check:** Compare conclusion quantifiers with the sample frame and experimental range. Find threats to construct, internal, external, or conclusion validity that could change the result.
- **Severity:** `S1`. Use `S0` when the conclusion directly contradicts scope.
- **Exceptions / false positives:** Implausible threat lists are not necessary in limitations. They must show threats related to the decision.
- **Repair direction:** Give repair options: boundaries, representativeness rationale, multiple evidence forms, or a narrower conclusion.
- **Sources:** [SIGPLAN-EMPIRICAL], [OSDI-CFP].

## Claim-to-evidence matrix

For each central claim, fill this table:

| Claim | Required inference | Evidence object | Comparator/control | Population/conditions | Uncertainty | Result | Valid conclusion | Gap |
|---|---|---|---|---|---|---|---|---|

Then apply these three attacks:

1. **Alternative explanation:** What uncontrolled factor could cause the same observation?
2. **Boundary failure:** What condition with evidence for its possibility lies just outside the tested range?
3. **Decision reversal:** What missing cost, baseline, uncertainty, or negative case could reverse the practical choice?

## Methods depend on claims

A missing method alone does not show a defect. These items are not universal requirements:

- A fixed repetition count.
- Specifically 95% confidence intervals.
- A p-value.
- An ablation table.
- An end-to-end benchmark for a component-only claim.
- Each public benchmark suite.
- Each cited prior system as an executable baseline.

Record the inference without evidence. Give the correct evidence with the lowest burden that would show it.
