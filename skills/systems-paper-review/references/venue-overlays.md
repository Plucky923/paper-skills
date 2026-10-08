# Venue and Submission Overlays

Use this reference for a specified venue, track, cycle, submission stage, or submission-readiness request. Venue rules change. Examine rules in effect for page limits, deadlines, anonymity, artifacts, ethics, generative AI, and supplementary material.

## VO-01 — Find the specified venue, cycle, track, and stage

- **Nature:** Prerequisite for venue compliance review.
- **Reviewer attack / consequence:** “The authors followed a different year's, round's, track's, or revision stage's rules.”
- **Check:** Record official venue, cycle, track, round, and stage. If deadlines matter, record the timezone. Include submission, revision, camera-ready, or artifact stage as applicable.
- **Severity:** `S0` when mismatch causes invalid submission. `S1` when requirements stay uncertain.
- **Exceptions / false positives:** For a generic venue-fit request without a cycle, keep volatile compliance not assessable. Do not invent a cycle.
- **Repair direction:** Get the specified target or give the review a generic label. Use the official source in effect.
- **Sources:** Official venue page in effect. Examine it online.

## VO-02 — Official sources outrank aggregators and remembered rules

- **Nature:** Condition for evidence.
- **Reviewer attack / consequence:** “The compliance advice came from a stale blog, call aggregator, prior cycle, or search snippet.”
- **Check:** If possible, use official conference domains and publisher or society author resources. Open their policy and template links. Record direct URLs. Apply each page only to its specified cycle and stage.
- **Severity:** `S0` if wrong advice would invalidate submission. For other cases, `S1`.
- **Exceptions / false positives:** Official updates can occur on linked submission systems or society pages. Examine their source authority.
- **Repair direction:** Use official sources in effect. Record differences from earlier advice.
- **Sources:** [OSDI-CFP], [SOSP-CFP], [EUROSYS-CFP], [ASPLOS-CFP], [ATC-WRITING], [NSDI-CFP], [ACM-TEMPLATE], [USENIX-TEMPLATE].

## VO-03 — Requirements and reviewer preferences have different classes

- **Nature:** Condition for rule classification.
- **Reviewer attack / consequence:** “The review treats optional advice as desk-reject policy, or misses a binding rule because it looks stylistic.”
- **Check:** Give each retrieved item one label: `required`, `prohibited`, `recommended`, `review criterion`, or `unclear`. Keep its specified condition, track, and stage. Examples alone do not show `must`.
- **Severity:** By underlying rule. For submission-critical rules, use `S1` until the classification question has an answer.
- **Exceptions / false positives:** Program-chair FAQs and submission-system validation can resolve rule questions. Give citations for them.
- **Repair direction:** Give a short quotation or summary with a direct official citation. If official sources conflict, give the author a question for the organizer.
- **Sources:** Official venue and publisher sources in effect.

## VO-04 — Scope and contribution fit use review criteria in effect

- **Nature:** Venue requirement or reviewer criterion.
- **Reviewer attack:** “The paper is out of scope or its primary advance is not the kind this venue evaluates.”
- **Check:** Compare the central problem, contribution type, evaluated object, and audience with official topics and criteria. Treat example topic lists as non-exhaustive where specified.
- **Severity:** `S0` for clear out-of-scope. `S1` for weak fit.
- **Exceptions / false positives:** Interdisciplinary work can fit through systems, architecture, networking, or security contributions. Topic keywords alone are insufficient.
- **Repair direction:** Give the advance for the target community or select an applicable venue or track.
- **Sources:** Target CFP in effect. Examples [OSDI-CFP], [SOSP-CFP], [EUROSYS-CFP], [ASPLOS-CFP], [ATC-WRITING], [NSDI-CFP].

## VO-04A — Apply venue emphasis without flattening the contribution

- **Nature:** Review calibration. Use official criteria in effect.
- **Check:** Use the cycle-specific examples below to select reviewer questions. Before a compliance result, examine the target cycle and track.

| Venue/cycle example | Decision emphasis | Writing risk to inspect |
|---|---|---|
| OSDI 2027 / OSDI 2026 | Important systems problem, strong advance, potential research/practice impact. Operational knowledge can be a contribution | An application result without a systems advance. An operational story with scale but no reusable knowledge |
| SOSP 2026 | New territory or an important research dialogue. Design, implementation, analysis, evaluation, deployment, and measurement can carry the contribution | Principles reduced to slogans, or a narrow artifact with no transferable insight |
| EuroSys 2027 | Benefits, limitations, and advantage over prior work. Experience lessons must have generality, methodological rigor, and quantitative evidence that helps other systems | Benefits presented without cost/boundary, or deployment scale substituted for a transferable lesson |
| ASPLOS 2027 | Important advance in architecture, OS, PL, or a new domain connected to at least one of those pillars. Pros/cons and implementation status matter | Use of a pillar technique without a contribution in that pillar, unexplained cross-layer necessity, or an overclaimed incomplete implementation |
| USENIX ATC, writing reference | Practical implementation and experimental evidence, with pros/cons and implementation status | Treating pragmatism as a lower evidence standard or treating ATC as a submission target in use |

- **Severity:** Use the consequence from the venue rule in effect. A mismatch with these examples alone is not noncompliance.
- **Repair direction:** Give the advance in the paper for the target community. Use its official rubric in effect. Keep the contribution type accurate.
- **Sources:** [OSDI-CFP], [SOSP-CFP], [EUROSYS-CFP], [ASPLOS-CFP], [ATC-WRITING].

## VO-04B — Rapid-review page boundaries are applied only when official

- **Nature:** Venue rule only if mandatory in the specified cycle. In other cases, a diagnostic aid.
- **Check:** Examine the specified review stage and required reading. If the CFP in effect makes first-two-page rapid review mandatory, apply its self-containment requirements. Keep mandatory procedures and preliminary possibilities in different classes. Without that rule, use two-page tests only for discoverability findings.
- **Severity:** `S0`/`S1` by the confirmed venue rule in effect. For other cases, report only the underlying reader risk.
- **Exceptions / false positives:** Page boundaries and stages can change before submission. Apply rapid-review rules only to their source venue.
- **Repair direction:** Put the decision case and credibility preview inside the specified unit for review. Do not use unnecessary mechanism inventories.
- **Sources:** [ASPLOS-CFP], [OSDI-CFP]. Online verification is necessary.

## VO-05 — Format, length, and required content are checked on rendered submission

- **Nature:** Submission requirement.
- **Reviewer attack / consequence:** Desk rejection or upload rejection for page count, font/margin, columns, paper size, references/appendix accounting, title/author block, abstract length, or file format.
- **Check:** Get the official template, version, and rule text. Render the final PDF. Examine body, reference, and appendix page accounting, page size, fonts, margins, columns, anonymity, and file size. Examine mandatory sections and statements.
- **Severity:** `S0` for verified violation. `S1` if final rendered form unavailable.
- **Exceptions / false positives:** Draft line count is irrelevant. Camera-ready rules apply to anonymous submission only if the CFP makes them mandatory.
- **Repair direction:** Use the official template. Remove noncompliant adjustments. Examine rendered compliance in different checks from source compliance.
- **Sources:** Target author instructions in effect, [ACM-TEMPLATE] or [USENIX-TEMPLATE] as applicable.

## VO-06 — Anonymity and conflicts are checked across all submitted material

- **Nature:** Policy condition where anonymous review applies.
- **Reviewer attack / consequence:** Desk rejection, compromised review, or policy breach.
- **Check:** Examine review type, self-citations, acknowledgments, artifact anonymity, URLs, PDF metadata, filenames, code paths, usernames, grants, prior-paper wording, conflicts, and declarations. Examine only material in scope. Give incomplete-coverage limits.
- **Severity:** `S0` for confirmed breach. `S1` for high-risk unassessable artifact/link.
- **Exceptions / false positives:** Some venues give permission for public preprints or artifacts. Obey the policy in effect. Public identity alone does not show a violation.
- **Repair direction:** Obey the official anonymity and conflict procedures. Keep necessary scholarship information.
- **Sources:** Target CFP in effect, FAQ, submission and artifact instructions.

## VO-07 — Prior publication, preprint, overlap, and consubmission rules are in effect

- **Nature:** Condition for publication ethics.
- **Reviewer attack / consequence:** Rejection or ethics investigation for duplicate/concurrent publication or undisclosed overlap.
- **Check:** Get prior-publication definitions, workshop or preprint allowances, overlap thresholds and procedures, concurrent-review rules, extended-version rules, disclosures, citations, and author responsibilities. Text similarity alone does not show legal or ethical violations.
- **Severity:** `S0` for confirmed violation. `S1` unresolved high-stakes risk.
- **Exceptions / false positives:** Policies can have large differences. Preprints often have conditional permission.
- **Repair direction:** Give required overlap disclosure, citations, and explanation. For ambiguity, get chair guidance.
- **Sources:** Target ethics/submission policy in effect and publisher policy.

## VO-08 — Human-subjects, data, security, and ethics requirements are addressed

- **Nature:** Policy or ethical condition where applicable.
- **Reviewer attack / consequence:** Missing IRB/ethics review, consent, data authorization, risk disclosure, responsible vulnerability handling, or required ethics statement.
- **Check:** Find official ethics guidance and required statements. Examine the population, personal data, network scans, vulnerable systems, dual use, environmental or resource costs, and disclosure timeline.
- **Severity:** `S0` for confirmed violation that affects submission. `S1` for missing required statement or unresolved approval.
- **Exceptions / false positives:** Telemetry or user data does not always have human-subjects research status. Jurisdiction and institutional decisions matter. Use only approval requirements from applicable official sources.
- **Repair direction:** Give accurate approval, exemption, consent, and risk disclosures. If authorized, change practice. For other cases, give questions for chairs or institutions.
- **Sources:** Target ethics policy in effect and applicable institutional/legal authority.

## VO-09 — Generative-AI and tool-use policy is verified, not assumed

- **Nature:** Venue or publisher policy where specified.
- **Reviewer attack / consequence:** Missing disclosure, prohibited authorship/citation/review use, confidentiality breach, or unsupported generated content.
- **Check:** Get policies in effect for writing, disclosure, authorship, figures, code, citations, reviewer confidentiality, and responsibility. Use language-assistance and content-generation distinctions only as officially specified.
- **Severity:** `S0` for confirmed prohibited use/noncompliance. `S1` when disclosure requirement is unresolved.
- **Exceptions / false positives:** Policies differ by venue and year. Apply AI policies only to their source venue.
- **Repair direction:** Obey disclosure and prohibition rules in effect. Do checks of facts, citations, and results independently.
- **Sources:** Venue and publisher AI policy in effect.

## VO-10 — Supplementary material is treated according to reviewer obligations

- **Nature:** Venue rule and general argument principle.
- **Reviewer attack / consequence:** Central evidence is placed in optional, nonarchival, over-limit, or impermissible supplement.
- **Check:** Examine permitted formats, length, reviewer obligations, anonymity, archival status, links, appendices, videos, and page-limit accounting. Examine the required paper's self-containment.
- **Severity:** `S0` for prohibited/over-limit material. `S1` when central case depends on optional material.
- **Exceptions / false positives:** Proofs, extended results, videos, and artifacts can supplement the paper with official permission.
- **Repair direction:** Put central evidence in the required paper or narrow the claim. Package supplements with the required procedure unchanged.
- **Sources:** Target CFP in effect/author instructions.

## VO-11 — Artifact requirements and badges use the target cycle's definitions

- **Nature:** Condition when artifacts are mandatory or a badge is claimed.
- **Reviewer attack / consequence:** Ineligible artifact, missed deadline, nonanonymous link, or inflated badge/reproduction claim.
- **Check:** Examine eligibility, timing, required or optional status, packaging, availability, reviewer platform, documentation, licenses, anonymity, badges, and paper-artifact relation. For quality, use `AR` rules.
- **Severity:** `S0` for binding noncompliance. `S1` for missing central artifact support.
- **Exceptions / false positives:** Artifact evaluation can be optional or occur after acceptance. Initial-paper obligations depend on rules in effect.
- **Repair direction:** Obey the target artifact call. Make sure that claims and badge terms agree with evidence.
- **Sources:** Target artifact call in effect. [NSDI-ARTIFACT], [ACM-ARTIFACT] for concepts.

## VO-12 — Track-specific evaluation criteria are not flattened

- **Nature:** Condition for review routing.
- **Reviewer attack:** “A short/experience/operational/measurement/artifact/deployed/vision track is judged by the wrong contribution or evidence model.”
- **Check:** Get track purpose, eligible contributions, review criteria, length, evidence requirements, and primary-track relation. Keep track-specific operational lessons, negative results, or vision for a future system.
- **Severity:** `S1`. `S0` for ineligible track submission.
- **Exceptions / false positives:** Repeated track names can have different definitions across venues.
- **Repair direction:** Use the track rubric in effect or examine the track choice again.
- **Sources:** Target track page in effect.

## VO-13 — Deadlines and submission mechanics include timezone and version

- **Nature:** Operational requirement for readiness or schedule requests.
- **Reviewer attack / consequence:** Missed registration/submission/artifact/revision deadline or wrong submission portal/version.
- **Check:** Examine date, time, timezone or AoE meaning, abstract registration, author-list deadline, and revision windows. Examine portal, file policy, version policy, and update permission. Compare official pages with linked systems.
- **Severity:** `S0` if missed/noncompliant. `S1` if ambiguous.
- **Exceptions / false positives:** For a pure prose review, add schedule checks only if requested.
- **Repair direction:** Record the specified official timestamp and prerequisites. Give the author any source conflicts and a question for chair resolution.
- **Sources:** Official venue page/submission system in effect.

## Procedure for rules in effect

1. Search for the specified venue, cycle, track, and stage.
2. Open the official CFP or author instructions.
3. Open official policy, template, and artifact links.
4. Record these fields:

   ```text
   Venue:
   Cycle/year:
   Track/round:
   Stage:
   Official URL:
   ```

5. Collect only rules related to material in scope.
6. For each rule, record its specified condition, class, report location, and compliance evidence.
7. If official pages conflict, examine their specificity and dates.
8. If clear evidence gives source precedence, use the source for the specified case or a more recent source.
9. If the conflict stays, record the blocker.
10. Give the author a question for chair resolution.
11. Keep volatile retrieved facts outside generic review rules.

## Official entry points studied

- [OSDI 2027 CFP](https://www.usenix.org/conference/osdi27/call-for-papers)
- [OSDI 2026 CFP](https://www.usenix.org/conference/osdi26/call-for-papers)
- [SOSP 2026 CFP](https://sigops.org/s/conferences/sosp/2026/cfp.html)
- [NSDI 2027 CFP](https://www.usenix.org/conference/nsdi27/call-for-papers)
- [EuroSys 2027 CFP](https://2027.eurosys.org/cfp.html)
- [ASPLOS 2027 CFP](https://www.asplos-conference.org/asplos2027/cfp/)
- [USENIX ATC 2025 submission instructions](https://www.usenix.org/conference/atc25/submission-instructions)
- [USENIX ATC termination announcement](https://www.usenix.org/blog/usenix-atc-announcement)
- [USENIX paper templates](https://www.usenix.org/conferences/author-resources/paper-templates)
- [ACM proceedings templates](https://www.acm.org/publications/proceedings-template)

These links are research starting points. They do not automatically apply to the specified target. Examine the target cycle and each page's status in effect online. ATC stays a writing reference. It is not a submission target.

## Venue compliance table

| Rule | Classification | Official source | In-scope evidence | Status | Consequence | Required action |
|---|---|---|---|---|---|---|

Use `compliant`, `noncompliant`, `not assessable`, `not applicable`, or `source conflict`. Give different scientific-quality and submission-rule results. A scientifically strong paper can violate submission rules.
