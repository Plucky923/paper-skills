# Evaluation Validity and Evidence

Evaluation is an argument from observations to claims. Judge whether the design can answer the stated question, whether measurements are trustworthy, and whether conclusions remain inside the evidence boundary. Do not demand a ritual experiment—ablation, significance test, or benchmark suite—unless it resolves a real claim.

## EV-01 — Every central claim has an evidence plan

- **Nature:** Hard scientific-validity condition.
- **Reviewer attack:** “The paper's strongest contribution is never directly evaluated.”
- **Check:** Build a claim-to-evidence matrix covering correctness, performance, overhead, scalability, robustness, usability, security, generality, and practicality as claimed. Identify whether support is experiment, proof, analysis, case study, artifact, or external fact. Use the thesis-support hierarchy in [thesis-and-story.md](thesis-and-story.md) to verify that the decisive evidence and headline results cover the primary claims before secondary measurements.
- **Severity:** `S0` for a central unsupported conclusion; `S1` for partial coverage; `S2` for secondary claims.
- **Exceptions / false positives:** Some premises may be established by cited primary evidence; verify that the cited source actually supports the same conditions.
- **Repair direction:** Add an appropriate test using real evidence, replace with a supported claim, or remove it. Do not add invented results.
- **Sources:** [OSDI-CFP], [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE]. Checked 2026-09-01.

## EV-02 — Evidence is selected by recoverable scientific questions

- **Nature:** General best practice.
- **Reviewer attack:** “The evaluation is a collection of favorable plots rather than tests of explicit hypotheses or system questions.”
- **Check:** For each experiment, proof, case study, or operational observation, recover the question, outcomes, relevant conditions/controls, permitted inference, and which claim it can challenge. The question may be explicit or inferable from a tightly coupled finding/intervention narrative. Flag evidence objects with no decision role.
- **Severity:** `S1` when experiment design cannot establish claims; otherwise `S2`.
- **Exceptions / false positives:** Do not require an enumerated RQ list or one evaluation section. Exploratory, measurement, and operational studies may pose descriptive questions and interleave method, observation, and intervention, but must still make each inference auditable.
- **Repair direction:** Organize experiments around questions and remove or demote non-evidentiary plots.
- **Sources:** [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE], [HEISER-BENCH]. Checked 2026-09-01.

## EV-03 — The study design matches the inference

- **Nature:** Hard scientific-validity condition.
- **Reviewer attack:** “The evaluation is observational but the paper draws a causal conclusion,” or “a microbenchmark is used to claim end-to-end benefit.”
- **Check:** Classify the inference as descriptive, comparative, causal, predictive, correctness, or feasibility. Verify interventions, controls, randomization/pairing, trace provenance, and measurement level support it.
- **Severity:** `S0` for a central invalid inference; otherwise `S1`.
- **Exceptions / false positives:** Controlled systems experiments may establish causal effects without population random sampling, but generalization remains bounded to tested conditions.
- **Repair direction:** Change design, add controls, triangulate evidence, or narrow conclusion type.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH]. Checked 2026-09-01.

## EV-04 — Baselines answer the real comparison

- **Nature:** Hard fairness condition.
- **Reviewer attack:** “The paper avoids the strongest, simplest, most current, or operationally relevant alternative.”
- **Check:** Consider: current state of practice; closest prior research; strong specialized method; simple strawman; ablated current system; oracle/upper bound where meaningful. Require only categories relevant to the claim and deployment choice.
- **Severity:** `S1`; `S0` if omission makes the headline advantage knowingly misleading.
- **Exceptions / false positives:** An unavailable/proprietary baseline can be excluded with evidence, limitations, and a defensible substitute; do not demand every cited work.
- **Repair direction:** Add/configure the missing comparator, justify exclusion, or narrow comparative claims.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [OSDI-CFP]. Checked 2026-09-01.

## EV-05 — Baseline configurations are fair and reproducible

- **Nature:** Hard fairness condition.
- **Reviewer attack:** “The proposed system is tuned while baselines use defaults, obsolete versions, weaker hardware, fewer resources, or incompatible goals.”
- **Check:** Compare versions, patches, hardware allocation, parallelism, compilation, warmup, tuning budget, parameter search, stopping criteria, feature set, and correctness target. Verify authors did not tune on test data.
- **Severity:** `S0` for material manipulation; otherwise `S1`.
- **Exceptions / false positives:** Default settings may represent real practice if justified and sensitivity is checked where defaults matter.
- **Repair direction:** Equalize resources/effort/objective, disclose settings, add sensitivity, or qualify the comparison.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL]. Checked 2026-09-01.

## EV-06 — Workloads represent the claim domain

- **Nature:** Hard external-validity condition for broad claims.
- **Reviewer attack:** “The result depends on toy, outdated, cherry-picked, or nonrepresentative workloads.”
- **Check:** Inspect workload source, versions, scale, diversity, realism, skew, arrival pattern, read/write mix, failure conditions, hardware/software interaction, and known bias. Compare tested domain with quantifiers in the claim.
- **Severity:** `S1`; `S0` if the selected workload contradicts the advertised use case.
- **Exceptions / false positives:** A microbenchmark is valid for isolating a mechanism when clearly labeled and paired with evidence adequate for end-to-end claims.
- **Repair direction:** Add representative/diverse cases, justify scope, or narrow generalization.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE]. Checked 2026-09-01.

## EV-07 — Calibration, training, tuning, and evaluation data are separated

- **Nature:** Hard validity condition when adaptation or search is involved.
- **Reviewer attack:** “The method overfits the workloads or traces used to select its rules, parameters, prompts, thresholds, or model.”
- **Check:** Track provenance and partition of training, profiling, tuning, validation, test, and case-study data. Check repeated test-set feedback and leakage through handcrafted choices.
- **Severity:** `S0` for central leaked results; otherwise `S1`.
- **Exceptions / false positives:** Online/adaptive systems may learn from deployment traffic, but evaluation must model that lifecycle and use future/held-out outcomes appropriately.
- **Repair direction:** Create disjoint evaluation, nested selection, temporal split, or explicitly characterize in-sample behavior.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH]. Checked 2026-09-01.

## EV-08 — Metrics correspond to user/system objectives

- **Nature:** Hard construct-validity condition.
- **Reviewer attack:** “The chosen proxy improves while the outcome users or operators care about may not.”
- **Check:** Define each metric, direction, unit, aggregation, and relationship to objective. Watch proxy metrics, ratios without denominators, averages hiding tails, throughput without latency, and accuracy without cost/error asymmetry.
- **Severity:** `S1`; `S0` if the headline conclusion uses an invalid metric.
- **Exceptions / false positives:** Proxy metrics are acceptable when validated or clearly framed as proxies.
- **Repair direction:** Report direct outcomes or validate the proxy; add complementary metrics and bounds.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [ERNST]. Checked 2026-09-01.

## EV-09 — Numerators, denominators, aggregation, and units are explicit

- **Nature:** Hard interpretability condition.
- **Reviewer attack:** “The reported percentage or average has no auditable population, weighting, or unit.”
- **Check:** Recover sample unit, denominator, inclusion/exclusion, weighting, macro/micro averaging, percentile definition, time window, and unit conversion. Recompute simple values when data are in scope.
- **Severity:** `S1` for headline ambiguity/error; `S2`/`S3` locally.
- **Exceptions / false positives:** Space-constrained captions may defer details to setup, but the paper must provide them somewhere in scope for a full review.
- **Repair direction:** Define population/formula/unit, show absolute values alongside ratios when useful, and correct arithmetic.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [USER-NOTES]. Checked 2026-09-01.

## EV-10 — The measured boundary includes all material costs

- **Nature:** Hard fairness condition.
- **Reviewer attack:** “Speedup/efficiency excludes setup, preprocessing, retraining, migration, recovery, network transfer, client work, hardware cost, or operator labor.”
- **Check:** Draw the start/end boundary and resource boundary for each measurement. Check amortization, caching, cold/warm state, background work, deferred cleanup, and shifted cost.
- **Severity:** `S0` if intentionally/m materially misleading; otherwise `S1`.
- **Exceptions / false positives:** Component measurements can isolate a mechanism if labeled and not promoted to total-system claims.
- **Repair direction:** Report end-to-end and component costs; justify amortization and deployment frequency; narrow claims.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [LEVIN-REDELL]. Checked 2026-09-01.

## EV-11 — Measurement procedure controls transient and environmental effects

- **Nature:** Hard measurement-validity condition when effects are material.
- **Reviewer attack:** “Results may be artifacts of warmup, caching, frequency scaling, background load, placement, network variance, garbage collection, JIT, or run order.”
- **Check:** Inspect warmup, steady-state detection, cache policy, randomization/interleaving, pinning/placement, isolation, clock/timer, run length, cooldown, environment monitoring, and outlier policy.
- **Severity:** `S1` when uncontrolled effects are comparable to claimed gain; otherwise `S2`.
- **Exceptions / false positives:** Controls depend on system; do not demand CPU pinning for experiments where it is irrelevant.
- **Repair direction:** Control, randomize, pair, monitor, or explicitly model the factor; repeat under representative conditions.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL]. Checked 2026-09-01.

## EV-12 — Replication and variability are reported

- **Nature:** General best practice; hard when stochastic/noisy results support a claim.
- **Reviewer attack:** “A single run or unreported variability cannot establish that the observed difference is stable.”
- **Check:** Identify independent repetitions, experimental unit, seeds, within/between-run variance, error bars/intervals, and whether aggregation matches design. Distinguish repeated measurements from independent samples.
- **Severity:** `S1` when uncertainty could reverse a central conclusion; `S2` otherwise.
- **Exceptions / false positives:** A deterministic exhaustive proof/check or uniquely expensive full deployment may justify alternatives, but must explain uncertainty and limitations.
- **Repair direction:** Repeat independent units, report distribution/intervals, expose seeds, or weaken stability claims.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH]. Checked 2026-09-01.

## EV-13 — Statistical analysis fits the design and question

- **Nature:** Hard when inferential statistics are used; otherwise conditional best practice.
- **Reviewer attack:** “The test assumes independence/normality it does not have, performs uncorrected multiple comparisons, or uses p-values as effect magnitude.”
- **Check:** Verify experimental unit, paired/unpaired structure, distribution assumptions, repeated measures, censoring, multiple testing, effect size, uncertainty interval, and practical relevance. Check that `significant` is not used ambiguously.
- **Severity:** `S1` for an invalid central inference; `S2` for incomplete reporting.
- **Exceptions / false positives:** Statistical significance testing is not mandatory for every deterministic or controlled systems benchmark. Require the uncertainty treatment needed by the actual noise and claim.
- **Repair direction:** Use an appropriate model/test/interval, report effect size, or make descriptive conclusions.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH]. Checked 2026-09-01.

## EV-14 — End-to-end evidence and microanalysis play distinct roles

- **Nature:** General best practice.
- **Reviewer attack:** “End-to-end plots show an effect but not why; microbenchmarks show a fast primitive but not system benefit.”
- **Check:** Map end-to-end experiments to practical outcome and component experiments to mechanism/causal explanation. Require both only when both claims are made.
- **Severity:** `S1` if the missing level leaves the central claim unsupported; otherwise `S2`.
- **Exceptions / false positives:** A component paper or measurement study may legitimately focus on one level.
- **Repair direction:** Add the missing evidence level, connect it causally, or narrow contribution.
- **Sources:** [SYSTEMS-GUIDE], [HEISER-BENCH], [LEVIN-REDELL]. Checked 2026-09-01.

## EV-15 — Ablation is used when component necessity is claimed

- **Nature:** Conditional best practice, not a universal ritual.
- **Reviewer attack:** “The paper attributes gains to component X without isolating X from co-varying components.”
- **Check:** Determine whether the paper claims necessity, contribution, interaction, or co-design. If so, inspect removal/substitution/factorial evidence and whether removal preserves a meaningful functioning system.
- **Severity:** `S1` for unsupported central attribution; `S2` otherwise.
- **Exceptions / false positives:** Ablation may be infeasible or nonsensical for inseparable invariants, safety mechanisms, or one-piece algorithms; analytical or targeted evidence can substitute.
- **Repair direction:** Add a valid isolation study, explain inseparability with other evidence, or stop assigning the effect to one component.
- **Sources:** [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE], [JENSEN-SYSTEMS-SKILL]. Checked 2026-09-01.

## EV-16 — Sensitivity, scalability, and operating envelope are tested

- **Nature:** Hard for robustness/scalability claims; conditional otherwise.
- **Reviewer attack:** “The result holds at one favorable parameter point and may collapse under scale, skew, load, failure, or hardware variation.”
- **Check:** Select factors from system assumptions and claimed domain. Inspect range, interactions, saturation, phase changes, and failure points—not just more parameter plots.
- **Severity:** `S1` for unsupported broad claims; `S2` for incomplete characterization.
- **Exceptions / false positives:** Do not demand sweeping knobs unrelated to the mechanism or intended deployment.
- **Repair direction:** Test decision-relevant range and boundary; report safe/efficient operating envelope; narrow claims.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [OSDI-CFP]. Checked 2026-09-01.

## EV-17 — Negative, null, and failure results are not hidden

- **Nature:** Hard reporting-integrity condition.
- **Reviewer attack:** “Only favorable workloads/configurations/metrics are shown, so the conclusion may be selected after seeing results.”
- **Check:** Look for unexplained missing benchmarks, truncated ranges, inconsistent subsets, dropped runs, post-hoc metrics, and absent failure rates. Compare experimental plan, text, tables, and artifact if in scope.
- **Severity:** `S0` for deceptive selective reporting; `S1` for major unresolved selection risk.
- **Exceptions / false positives:** Space limits justify summarized complete results or supplements, not silent outcome-based omission.
- **Repair direction:** Report all prespecified/relevant outcomes and exclusions; analyze failures; qualify the claim.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH]. Checked 2026-09-01.

## EV-18 — Graphical presentation preserves quantitative truth

- **Nature:** Hard integrity condition.
- **Reviewer attack:** “Axis truncation, aspect ratio, normalization, log scale, binning, or chart selection exaggerates advantage or hides regressions.”
- **Check:** Inspect axis origin/range/scale, aspect ratio, units, normalization denominator, uncertainty, missing data, sorting, aggregation, dual axes, color/order, and whether table vs plot choice changes perception. Recompute visual implications when data are in scope.
- **Severity:** `S0` for materially misleading presentation; `S1` for ambiguous headline plot; `S2` for correct but difficult display.
- **Exceptions / false positives:** Nonzero axes, log scales, normalized values, and compressed aspect ratios are valid when clearly labeled and suited to the question.
- **Repair direction:** Choose the representation that answers the research question honestly; disclose transformations; include absolute values or alternate view where needed.
- **Sources:** [HEISER-BENCH], [SIGPLAN-EMPIRICAL], [USER-NOTES] as normalized. Checked 2026-09-01.

## EV-19 — Result interpretation separates observation, cause, and speculation

- **Nature:** Hard inference condition.
- **Reviewer attack:** “The paper observes a correlation or performance change and invents a causal explanation without measurement.”
- **Check:** Label what was measured, what mechanism evidence supports, what follows logically, and what is hypothesized. Cross-reference design only when it actually predicts the effect.
- **Severity:** `S1` for a central unsupported explanation; `S2` locally.
- **Exceptions / false positives:** A plausible explanation is useful when explicitly marked as hypothesis and not used as proof.
- **Repair direction:** Add diagnostic/ablation evidence, state uncertainty, or remove causal language.
- **Sources:** [SIGPLAN-EMPIRICAL], [SYSTEMS-GUIDE], [ERNST]. Checked 2026-09-01.

## EV-20 — Practical significance accompanies relative gains

- **Nature:** General best practice; hard when rhetoric depends on magnitude.
- **Reviewer attack:** “The relative improvement is large only because the baseline value is tiny, or the absolute change does not affect operation.”
- **Check:** Report absolute and relative values, resource/user consequence, threshold/SLO, effect size, and cost tradeoff. Inspect excessive significant digits and unsupported qualitative labels.
- **Severity:** `S1` if headline impact is materially overstated; `S2` otherwise.
- **Exceptions / false positives:** Small absolute changes can matter near hard thresholds; explain the threshold.
- **Repair direction:** Add absolute scale/context and tradeoff; calibrate adjectives and precision.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [USER-NOTES]. Checked 2026-09-01.

## EV-21 — Reproducibility information is sufficient to audit results

- **Nature:** General best practice; may become venue/artifact requirement.
- **Reviewer attack:** “Versions, environment, commands, data provenance, or randomness are insufficient to recreate the reported experiment.”
- **Check:** Inspect hardware/software versions, topology, build/configuration, workload generation, seeds, commands, run order, repetitions, analysis, figure generation, and deviations from defaults.
- **Severity:** `S1` when opacity prevents confidence in central measurements; `S2` for missing secondary detail; `S0` for verified submission-rule breach.
- **Exceptions / false positives:** Security, privacy, licensing, or infrastructure limits may restrict release, but methodology and alternative access/validation should be as complete as possible.
- **Repair direction:** Add precise environment/procedure and archive inputs/outputs; follow current artifact rules.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT], [SIGPLAN-EMPIRICAL]. Checked 2026-09-01.

## EV-22 — Evaluation limitations bound the conclusion

- **Nature:** Hard accuracy condition.
- **Reviewer attack:** “The conclusion generalizes beyond tested systems, traces, hardware, scale, geography, users, or time.”
- **Check:** Compare conclusion quantifiers with sample frame and experimental range. Identify threats to construct, internal, external, and conclusion validity that could change the result.
- **Severity:** `S1`; `S0` if conclusion directly contradicts scope.
- **Exceptions / false positives:** A limitations section need not enumerate implausible threats; it must surface decision-relevant ones.
- **Repair direction:** State boundary, justify representativeness, triangulate, or narrow conclusion.
- **Sources:** [SIGPLAN-EMPIRICAL], [OSDI-CFP]. Checked 2026-09-01.

## Claim-to-evidence matrix

For every central claim, fill:

| Claim | Required inference | Evidence object | Comparator/control | Population/conditions | Uncertainty | Result | Valid conclusion | Gap |
|---|---|---|---|---|---|---|---|---|

Then run three attacks:

1. **Alternative explanation:** What uncontrolled factor could produce the same observation?
2. **Boundary failure:** What plausible condition lies just outside the tested range?
3. **Decision reversal:** What missing cost, baseline, uncertainty, or negative case could reverse the practical choice?

## Methods are conditional, not ceremonial

Do not declare a defect merely because the evaluation lacks:

- a fixed number of repetitions;
- 95% confidence intervals specifically;
- a p-value;
- an ablation table;
- an end-to-end benchmark for a component-only claim;
- every public benchmark suite;
- every cited prior system as an executable baseline.

Instead, state the inference that is currently unsupported and the least burdensome valid evidence that would support it.
