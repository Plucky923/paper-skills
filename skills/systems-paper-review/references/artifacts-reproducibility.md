# Artifacts and Reproducibility

Use these rules only for code, data, scripts, environments, logs, or artifact documentation that the user clearly puts in scope. Keep artifact review evidence-based and read-only.

Keep artifacts unchanged during review. Use evidence before any claim that local files are the submitted version.
## AR-01 — Artifact identity and version are unambiguous

- **Nature:** Condition for traceability.
- **Reviewer attack:** “I cannot tell whether this artifact corresponds to the manuscript's evaluated system and results.”
- **Check:** Find the version, tag, commit, or immutable archive. Record its paper-version relation, components, source or generated files, and artifact boundary.
- **Severity:** `S1`. `S0` if a different version contradicts results in ways that change conclusions.
- **Exceptions / false positives:** Development checkouts can be reviewed. Conclusions must give their status as mutable development versions.
- **Repair direction:** Give immutable version metadata and its manuscript relation. Keep tag or commit creation outside review.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT].

## AR-02 — Each artifact-backed claim maps to an observable object

- **Nature:** Condition for evidence.
- **Reviewer attack:** “The repository exists, but no code, data, or procedure supports the headline claim.”
- **Check:** Make this map: claim → implementation/configuration → workload/input → command/script → raw output → analysis → paper figure/table/value.
- **Severity:** `S0` for a central nonexistent/contradictory object. `S1` for incomplete mapping.
- **Exceptions / false positives:** Theory or analysis claims can have no executable code. Give the different evidence form.
- **Repair direction:** Give repair options: documentation and a traceable pipeline, missing artifacts, or narrower claims.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT], [SIGPLAN-EMPIRICAL].

## AR-03 — Build and setup are specified from a clean environment

- **Nature:** General best practice. Venue-specific artifact requirement where stated.
- **Reviewer attack:** “The artifact works only in the authors' preconfigured environment or depends on unrecorded local state.”
- **Check:** Examine platform, architecture, hardware, OS or kernel, compilers, runtimes, package versions, and patches. Examine services, permissions, environment variables, containers, VMs, credentials, and setup time.
- **Severity:** `S1` if setup opacity blocks central validation. `S2` for recoverable detail.
- **Exceptions / false positives:** Specialized hardware or private infrastructure is permitted with intrinsic necessity and documentation. Give emulation or trace alternatives where feasible.
- **Repair direction:** Set the specified dependency versions. Give prerequisites and clean setup. Give access limits where necessary.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT].

## AR-04 — Instructions are executable, ordered, and diagnostic

- **Nature:** General best practice.
- **Reviewer attack:** “The README lists fragments but not a reproducible workflow or expected outcome.”
- **Check:** Examine commands, working directories, sequence, required inputs, runtime and resource expectations, outputs, success criteria, failure modes, and cleanup. Examine copy-and-paste safety.
- **Severity:** `S1` if no path reaches central results. `S2` in other cases.
- **Exceptions / false positives:** Expert artifacts can assume standard domain tools. Nonstandard state must be clear.
- **Repair direction:** Give a minimal smoke-test path. Give a full reproduction path with observable checkpoints.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT].

## AR-05 — A smoke test identifies setup failure and research failure

- **Nature:** General best practice.
- **Reviewer attack:** “The full experiment fails after hours, with no way to know whether the artifact is installed correctly.”
- **Check:** Find a short representative test of core components and environment. Make sure that it gives an interpretable expected result. Do not use smoke-test success as evidence for full paper reproduction.
- **Severity:** `S2`. `S1` when no other full validation procedure is practical and clear.
- **Exceptions / false positives:** Artifacts with few operations or no executable code do not always make smoke tests necessary.
- **Repair direction:** Give a fast sanity-check path. Give smoke-test results and full reproduction results different status labels.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT].

## AR-06 — Workloads, datasets, and traces have provenance and legal access

- **Nature:** Condition for integrity and access.
- **Reviewer attack:** “Inputs are missing, transformed opaquely, licensed incompatibly, privacy-sensitive, or selected differently from the paper.”
- **Check:** Examine origin, version, date, licenses, terms, checksums, sampling, filtering, preprocessing, and labels. Examine train/test partitions, privacy, consent, download stability, and synthetic-generator parameters.
- **Severity:** `S0` for fabricated, unauthorized, or different data that change conclusions. `S1` for missing central provenance. `S2` for detail.
- **Exceptions / false positives:** Restricted data can be permitted with clear provenance, controlled access, synthetic or aggregate alternatives, and bounded reproduction claims.
- **Repair direction:** Give documentation and archives for lawful inputs, transformations, and checksums. Give access or necessary claim limits.
- **Sources:** [SIGPLAN-EMPIRICAL], [NSDI-ARTIFACT], [ACM-ARTIFACT].

## AR-07 — Randomness and nondeterminism are controlled and exposed

- **Nature:** Condition when stochasticity affects conclusions.
- **Reviewer attack:** “Reported numbers may be a lucky seed, run order, race, or environmental draw.”
- **Check:** Find seeds, seed generation, independent run counts, concurrency nondeterminism, time-dependent inputs, randomization, and aggregation. Find silent removal of failed or unfavorable runs.
- **Severity:** `S1` for central unstable evidence. `S2` in other cases.
- **Exceptions / false positives:** Fixed seeds help replay. They do not alone give robustness evidence. Deterministic systems can use not-applicable status.
- **Repair direction:** Record seeds and environment. Repeat independent runs. Give variability and failures.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [NSDI-ARTIFACT].

## AR-08 — Raw and derived results stay in different records

- **Nature:** Condition for auditability for artifact-backed values.
- **Reviewer attack:** “Only final plots or hand-edited tables exist; the transformation cannot be audited.”
- **Check:** Find immutable raw output, schema, metadata, exclusions, normalization, analysis scripts, intermediate caches, and final figure or table generation. Find manually embedded headline values.
- **Severity:** `S0` for evidence fabrication/manipulation. `S1` for unauditable central results. `S2` in other cases.
- **Exceptions / false positives:** Large raw datasets can use documented aggregates with hashes and access paths.
- **Repair direction:** Keep raw, processed, and generated data in different layers. Give their documentation. Use automatic transformations. Record exclusions.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT], [SIGPLAN-EMPIRICAL].

## AR-09 — Figure and table regeneration matches the manuscript

- **Nature:** Condition for consistency.
- **Reviewer attack:** “The artifact regenerates different values, labels, workloads, or error bars than the submitted paper.”
- **Check:** Compare generated data and rendered output with manuscript values, units, legends, sequence, rounding, and exclusions in scope. Do a check of the difference between harmless rendering or version changes and scientific mismatch.
- **Severity:** `S0` for contradiction that changes conclusions. `S1` for unresolved mismatch. `S3` for cosmetic drift.
- **Exceptions / false positives:** Platform noise can cause bounded changes. Artifacts must give tolerance and paper aggregation.
- **Repair direction:** Select the source of truth. Record expected tolerance and version. Make sure that generation agrees with the source of truth or correct the claims.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT], [HEISER-BENCH].

## AR-10 — Error handling does not convert failures into success

- **Nature:** Condition for integrity.
- **Reviewer attack:** “Scripts ignore exit codes, missing data, timeouts, NaNs, failed trials, or partial output and still emit a result.”
- **Check:** Examine error propagation, applicable shell strictness, validation, missing-file behavior, retries, timeouts, partial writes, log visibility, and denominator changes after failures.
- **Severity:** `S0` if it can produce false central results. `S1` in other cases.
- **Exceptions / false positives:** Best-effort processing is permitted with failure counts and corresponding conclusion limits.
- **Repair direction:** Give clear failure results or clear failure counts. Examine input and output completeness. Give retry and exclusion documentation.
- **Sources:** [SIGPLAN-EMPIRICAL], [NSDI-ARTIFACT], [HEISER-BENCH].

## AR-11 — Paper, configuration, and implementation constants agree

- **Nature:** Condition for internal consistency.
- **Reviewer attack:** “The paper reports one threshold/topology/feature set while code and scripts use another.”
- **Check:** Within scope, compare parameters, defaults, enabled features, workload scale, hardware resources, timeouts, iteration counts, versions, and metric definitions.
- **Severity:** `S0` if it affects the headline result. `S1`/`S2` in other cases.
- **Exceptions / false positives:** Artifacts can include more configurations. Find the configuration used in the paper.
- **Repair direction:** Select one source of truth. Give override documentation. Make sure that the paper and scripts agree.
- **Sources:** [NSDI-ARTIFACT], [SIGPLAN-EMPIRICAL], [USER-NOTES].

## AR-12 — Artifact availability is not conflated with functionality or reproducibility

- **Nature:** Condition for claim calibration.
- **Reviewer attack:** “A public repository is presented as proof that results are reproducible or the artifact is reusable.”
- **Check:** Do a check of differences between availability, installation or function, result reproduction, independent replication, and reuse. Compare each label with venue or badge definitions in effect.
- **Severity:** `S1` for inflated artifact claims. `S0` for a verified policy/badge misrepresentation.
- **Exceptions / false positives:** An artifact can have value at one level without other properties.
- **Repair direction:** Use the correct evidence level. Obey badge terminology in effect.
- **Sources:** [ACM-ARTIFACT], [NSDI-ARTIFACT].

## AR-13 — Security, privacy, credentials, and anonymity are protected

- **Nature:** Condition for ethics and policy.
- **Reviewer attack:** “The artifact leaks secrets, personal data, author identity under double-blind rules, vulnerable services, or unsafe commands.”
- **Check:** Examine only visible material in scope. Find keys, tokens, private endpoints, usernames, paths, personal data, dangerous privileges, exposed services, destructive commands, telemetry, and identity metadata. Examine venue rules in effect.
- **Severity:** `S0` for credential/privacy/verified anonymity breach. `S1` for unsafe execution risk.
- **Exceptions / false positives:** Public author identity is normal outside anonymous review. Example credentials must be clearly fake.
- **Repair direction:** Give directions for removal or revocation of secrets, required anonymity, isolated unsafe operations, and minimum privileges. Keep secrets outside the report.
- **Sources:** Current venue rules, [NSDI-ARTIFACT], [ACM-ARTIFACT]. Live verification required.

## AR-14 — Claimed use obeys licensing and third-party dependency terms

- **Nature:** Condition for law and access where distribution is claimed.
- **Reviewer attack:** “The artifact cannot be distributed, built, or reused as claimed because licenses or proprietary dependencies are absent/incompatible.”
- **Check:** Find the artifact license, third-party licenses and notices, dataset or model terms, redistribution limits, and patent, export, or access requirements. Find dependencies on unavailable binaries or services.
- **Severity:** `S0` for unlawful or impossible claimed distribution. `S1` for central unresolved access. `S2` for incomplete notices.
- **Exceptions / false positives:** Closed or noncommercial components can be permitted with disclosure and agreement with claims and venue rules.
- **Repair direction:** Give permissions and dependencies. Give lawful replacement or packaging options. Put necessary limits on availability or reuse claims.
- **Sources:** [ACM-ARTIFACT], [NSDI-ARTIFACT].

## AR-15 — Documentation gives resource and time expectations

- **Nature:** General best practice. Can be artifact-review requirement.
- **Reviewer attack:** “Reviewers cannot plan execution or distinguish a hung run from a week-long intended experiment.”
- **Check:** Examine runtime, storage, memory, computation, networks, hardware, cost, parallelism, checkpoints, output size, and reduced or full workflows.
- **Severity:** `S1` if central reproduction is infeasible without disclosure. For other cases, `S2`.
- **Exceptions / false positives:** Measured time can change. Give the tested reference environment and time range.
- **Repair direction:** Give resource and time expectations. Give a meaningful reduced path. Do not treat reduced-path success as reproduction of full numbers.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT].

## Artifact execution discipline

If execution is authorized and in scope, read the [command-evidence procedure](multi-agent-orchestration.md#5-give-command-producing-evidence-through-the-root).
Apply its scope, isolation, manifest, and side-effect checks before these steps:

1. Before execution, read the instructions.
2. Use read-only inspection when it supplies the required evidence.
3. For required execution, select a documented smoke test when it can answer the review question.
4. Use disposable temporary outputs outside the source tree.
5. Before dependency installation, external services, credentials, system configuration, or destructive or privileged commands, get clear authority.
6. Record the command used, environment, exit status, and related output.
7. Give an observed pass only for the executed environment and path.
8. Keep artifact repairs outside review.

## Artifact coverage table

| Paper claim | Artifact object | Procedure inspected/run | Observable result | Match status | Limitation |
|---|---|---|---|---|---|

Use `match`, `partial`, `mismatch`, `not runnable`, `not inspected`, or `not in scope`. Repository existence alone does not show `match`.
