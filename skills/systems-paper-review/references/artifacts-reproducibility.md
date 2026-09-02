# Artifacts and Reproducibility

Apply these rules only when code, data, scripts, environments, logs, or artifact documentation are explicitly in scope. Artifact review is evidence-based and read-only. Never modify the artifact to make the paper pass, and never infer that local files are the submitted version without evidence.

## AR-01 — Artifact identity and version are unambiguous

- **Nature:** Hard traceability condition.
- **Reviewer attack:** “I cannot tell whether this artifact corresponds to the manuscript's evaluated system and results.”
- **Check:** Identify version/tag/commit or immutable archive, paper/version association, component inventory, generated versus source files, and stated artifact boundary.
- **Severity:** `S1`; `S0` if a different version materially contradicts results.
- **Exceptions / false positives:** A development checkout can be reviewed, but conclusions must say it is not an immutable submission snapshot.
- **Repair direction:** Provide immutable version metadata and mapping to manuscript; do not create a tag or commit during review.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT]. Checked 2026-09-01.

## AR-02 — Every artifact-backed claim maps to an observable object

- **Nature:** Hard evidence condition.
- **Reviewer attack:** “The repository exists, but no code, data, or procedure supports the headline claim.”
- **Check:** Map claim → implementation/configuration → workload/input → command/script → raw output → analysis → paper figure/table/value.
- **Severity:** `S0` for a central nonexistent/contradictory object; `S1` for incomplete mapping.
- **Exceptions / false positives:** Theory/analysis claims may not map to executable code; state the alternate evidence.
- **Repair direction:** Add documentation and traceable pipeline, supply missing artifact, or narrow claim.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT], [SIGPLAN-EMPIRICAL]. Checked 2026-09-01.

## AR-03 — Build and setup are specified from a clean environment

- **Nature:** General best practice; venue-specific artifact requirement where stated.
- **Reviewer attack:** “The artifact works only in the authors' preconfigured environment or depends on unrecorded local state.”
- **Check:** Inspect platform, architecture, hardware, OS/kernel, compilers/runtimes, package versions, patches, services, permissions, environment variables, containers/VMs, credentials, and expected setup time.
- **Severity:** `S1` if setup opacity blocks central validation; `S2` for recoverable detail.
- **Exceptions / false positives:** Specialized hardware or private infrastructure is acceptable when intrinsic and documented, with emulation/trace alternatives where feasible.
- **Repair direction:** Pin dependencies, document prerequisites and clean setup, or state access limits.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT]. Checked 2026-09-01.

## AR-04 — Instructions are executable, ordered, and diagnostic

- **Nature:** General best practice.
- **Reviewer attack:** “The README lists fragments but not a reproducible workflow or expected outcome.”
- **Check:** Verify commands, working directories, ordering, required inputs, runtime/resource expectations, expected output, success criteria, common failure modes, cleanup, and whether instructions are copy-safe.
- **Severity:** `S1` if no path reaches central results; `S2` otherwise.
- **Exceptions / false positives:** Expert-targeted artifacts may assume standard domain tools, but nonstandard state must be explicit.
- **Repair direction:** Add a minimal smoke path and full reproduction path with observable checkpoints.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT]. Checked 2026-09-01.

## AR-05 — A smoke test distinguishes setup failure from research failure

- **Nature:** General best practice.
- **Reviewer attack:** “The full experiment fails after hours, with no way to know whether the artifact is installed correctly.”
- **Check:** Look for a short, representative test that exercises core components, validates environment, and reports an interpretable expected result without claiming to reproduce the paper.
- **Severity:** `S2`; `S1` when full validation is otherwise impractical and opaque.
- **Exceptions / false positives:** Extremely simple or non-executable artifacts may not need a separate smoke test.
- **Repair direction:** Provide a fast sanity path and clearly separate it from full results.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT]. Checked 2026-09-01.

## AR-06 — Workloads, datasets, and traces have provenance and legal access

- **Nature:** Hard integrity/access condition.
- **Reviewer attack:** “Inputs are missing, transformed opaquely, licensed incompatibly, privacy-sensitive, or selected differently from the paper.”
- **Check:** Inspect origin, version/date, license/terms, checksums, sampling/filtering, preprocessing, labels, train/test split, privacy/consent, download stability, and synthetic generator parameters.
- **Severity:** `S0` for fabricated/unauthorized/materially different data; `S1` for missing central provenance; `S2` for detail.
- **Exceptions / false positives:** Restricted data can be scientifically valid with transparent provenance, controlled access, synthetic/aggregate alternatives, and bounded reproducibility claims.
- **Repair direction:** Document and archive lawful inputs/transforms/checksums; provide access or qualify claims.
- **Sources:** [SIGPLAN-EMPIRICAL], [NSDI-ARTIFACT], [ACM-ARTIFACT]. Checked 2026-09-01.

## AR-07 — Randomness and nondeterminism are controlled and exposed

- **Nature:** Hard when stochasticity affects conclusions.
- **Reviewer attack:** “Reported numbers may be a lucky seed, run order, race, or environmental draw.”
- **Check:** Locate seeds, seed generation, number of independent runs, concurrency nondeterminism, time-dependent inputs, randomization, and aggregation. Verify scripts do not silently discard failed/unfavorable runs.
- **Severity:** `S1` for central unstable evidence; `S2` otherwise.
- **Exceptions / false positives:** Fixed seeds aid replay but do not by themselves establish robustness; deterministic systems may mark this not applicable.
- **Repair direction:** Record seeds and environment, repeat independent runs, report variability and failures.
- **Sources:** [SIGPLAN-EMPIRICAL], [HEISER-BENCH], [NSDI-ARTIFACT]. Checked 2026-09-01.

## AR-08 — Raw results are preserved separately from derived results

- **Nature:** Hard auditability condition for artifact-backed values.
- **Reviewer attack:** “Only final plots or hand-edited tables exist; the transformation cannot be audited.”
- **Check:** Identify raw immutable output, schema, metadata, exclusions, normalization, analysis scripts, intermediate cache, and final figure/table generation. Check that scripts do not embed headline values manually.
- **Severity:** `S0` for evidence fabrication/manipulation; `S1` for unauditable central results; `S2` otherwise.
- **Exceptions / false positives:** Massive raw data may be represented by documented aggregates plus hashes/access path.
- **Repair direction:** Separate and document raw/processed/generated layers; automate transformations; record exclusions.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT], [SIGPLAN-EMPIRICAL]. Checked 2026-09-01.

## AR-09 — Figure and table regeneration matches the manuscript

- **Nature:** Hard consistency condition.
- **Reviewer attack:** “The artifact regenerates different values, labels, workloads, or error bars than the submitted paper.”
- **Check:** Compare generated data and rendered output with in-scope manuscript values, units, legend, ordering, rounding, and exclusions. Distinguish harmless rendering/version drift from scientific mismatch.
- **Severity:** `S0` for material contradiction; `S1` for unresolved mismatch; `S3` for cosmetic drift.
- **Exceptions / false positives:** Platform noise may cause bounded variation; artifact should state tolerance and paper aggregation.
- **Repair direction:** Reconcile source of truth, record expected tolerance/version, regenerate consistently, or correct claims.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT], [HEISER-BENCH]. Checked 2026-09-01.

## AR-10 — Error handling does not convert failures into success

- **Nature:** Hard integrity condition.
- **Reviewer attack:** “Scripts ignore exit codes, missing data, timeouts, NaNs, failed trials, or partial output and still emit a result.”
- **Check:** Inspect error propagation, shell strictness where relevant, validation, missing-file behavior, retry policy, timeout handling, partial writes, log visibility, and denominator adjustment after failures.
- **Severity:** `S0` if it can produce false central results; `S1` otherwise.
- **Exceptions / false positives:** Intentional best-effort processing is valid when failures are counted and conclusions reflect them.
- **Repair direction:** Fail clearly or record/include failures; validate input/output completeness; document retry/exclusion.
- **Sources:** [SIGPLAN-EMPIRICAL], [NSDI-ARTIFACT], [HEISER-BENCH]. Checked 2026-09-01.

## AR-11 — Paper, configuration, and implementation constants agree

- **Nature:** Hard internal-consistency condition.
- **Reviewer attack:** “The paper reports one threshold/topology/feature set while code and scripts use another.”
- **Check:** Cross-check named parameters, defaults, enabled features, workload scale, hardware resources, timeouts, iteration counts, versions, and metric definitions only across in-scope objects.
- **Severity:** `S0` if material to headline result; `S1`/`S2` otherwise.
- **Exceptions / false positives:** Artifact may include additional configurations; identify the one used for the paper.
- **Repair direction:** Establish one source of truth, document overrides, and align paper/scripts.
- **Sources:** [NSDI-ARTIFACT], [SIGPLAN-EMPIRICAL], [USER-NOTES]. Checked 2026-09-01.

## AR-12 — Artifact availability is not conflated with functionality or reproducibility

- **Nature:** Hard claim-calibration condition.
- **Reviewer attack:** “A public repository is presented as proof that results are reproducible or the artifact is reusable.”
- **Check:** Separate: available; installable/functional; results reproducible; independently replicated; reusable beyond paper workflow. Verify each label using the current venue/badge definition.
- **Severity:** `S1` for inflated artifact claims; `S0` for a verified policy/badge misrepresentation.
- **Exceptions / false positives:** An artifact can be valuable at one level without satisfying the others.
- **Repair direction:** Use exact level and evidence; follow current badge terminology.
- **Sources:** [ACM-ARTIFACT], [NSDI-ARTIFACT]. Checked 2026-09-01.

## AR-13 — Security, privacy, credentials, and anonymity are protected

- **Nature:** Hard ethical/policy condition.
- **Reviewer attack:** “The artifact leaks secrets, personal data, author identity under double-blind rules, vulnerable services, or unsafe commands.”
- **Check:** Inspect only in-scope visible material for keys/tokens, private endpoints, usernames/paths, personal data, dangerous privileges, exposed services, destructive commands, telemetry, and deanonymizing metadata. Verify current venue rules.
- **Severity:** `S0` for credential/privacy/verified anonymity breach; `S1` for unsafe execution risk.
- **Exceptions / false positives:** Public author identity is normal outside anonymous review. Example credentials must be unmistakably fake.
- **Repair direction:** Revoke/remove sensitive material, anonymize as required, sandbox/document unsafe operations, and minimize privileges. Do not echo secrets in report.
- **Sources:** Current venue rules, [NSDI-ARTIFACT], [ACM-ARTIFACT]. Live verification required.

## AR-14 — Licensing and third-party dependencies permit claimed use

- **Nature:** Hard legal/access condition where distribution is claimed.
- **Reviewer attack:** “The artifact cannot be distributed, built, or reused as claimed because licenses or proprietary dependencies are absent/incompatible.”
- **Check:** Locate artifact license, third-party licenses/notices, dataset/model terms, redistribution constraints, patent/export/access requirements, and whether instructions depend on unavailable binaries/services.
- **Severity:** `S0` for unlawful or impossible claimed distribution; `S1` for central unresolved access; `S2` for incomplete notices.
- **Exceptions / false positives:** Closed or noncommercial components can be valid if clearly disclosed and consistent with claims/venue rules.
- **Repair direction:** Clarify permissions and dependencies, replace/repackage lawfully, or narrow availability/reuse claims.
- **Sources:** [ACM-ARTIFACT], [NSDI-ARTIFACT]. Checked 2026-09-01.

## AR-15 — Documentation states resource and time expectations

- **Nature:** General best practice; may be artifact-review requirement.
- **Reviewer attack:** “Reviewers cannot plan execution or distinguish a hung run from a week-long intended experiment.”
- **Check:** Inspect runtime, storage, memory, compute/network/hardware needs, cost, parallelism, checkpointing, expected output size, and reduced/full workflows.
- **Severity:** `S1` if central reproduction is infeasible without disclosure; otherwise `S2`.
- **Exceptions / false positives:** Exact time varies; give tested reference environment and range.
- **Repair direction:** Document expected resources/time and meaningful reduced path; never imply reduced path reproduces full numbers.
- **Sources:** [NSDI-ARTIFACT], [ACM-ARTIFACT]. Checked 2026-09-01.

## Artifact execution discipline

When execution is authorized and in scope:

1. Read instructions before running anything.
2. Prefer read-only inspection and a documented smoke test.
3. Use disposable temporary outputs when possible.
4. Do not install dependencies, contact external services, use credentials, change system configuration, or run destructive/privileged commands without explicit authorization.
5. Capture exact command, environment, exit status, and relevant output.
6. Report an observed pass only for the executed environment and path.
7. Do not repair the artifact during review.

## Artifact coverage table

| Paper claim | Artifact object | Procedure inspected/run | Observable result | Match status | Limitation |
|---|---|---|---|---|---|

Use `match`, `partial`, `mismatch`, `not runnable`, `not inspected`, or `not in scope`. A repository's mere existence never yields `match`.

