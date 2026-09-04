# Venue and Submission Overlays

Use this reference only when the user names a venue, track, year/cycle, submission stage, or asks for submission readiness. Venue rules change. Never rely on a remembered page limit, deadline, anonymity rule, artifact rule, ethics statement, generative-AI policy, or supplementary-material policy.

## VO-01 — Resolve exact venue, cycle, track, and stage

- **Nature:** Hard prerequisite to venue compliance review.
- **Reviewer attack / consequence:** “The authors followed a different year's, round's, track's, or revision stage's rules.”
- **Check:** Record official venue name, year/cycle, track, round, submission/revision/camera-ready/artifact stage, and timezone if deadlines matter.
- **Severity:** `S0` when mismatch causes invalid submission; `S1` when requirements remain uncertain.
- **Exceptions / false positives:** If the user asks only for generic venue fit and gives no cycle, do not fabricate one; report that volatile compliance is not assessable.
- **Repair direction:** Obtain exact target or label review generic; use current official source.
- **Sources:** Current official venue page. Verify live.

## VO-02 — Official sources outrank aggregators and remembered rules

- **Nature:** Hard evidence rule.
- **Reviewer attack / consequence:** “The compliance advice came from a stale blog, call aggregator, prior cycle, or search snippet.”
- **Check:** Prefer official conference domain and publisher/society author resources. Follow linked policies/templates. Record direct URLs and checked date. Use archived pages only for the named past cycle.
- **Severity:** `S0` if wrong advice would invalidate submission; otherwise `S1`.
- **Exceptions / false positives:** Organizers may publish official updates on a linked submission site or society page; verify provenance.
- **Repair direction:** Replace with official current source and record discrepancies.
- **Sources:** [OSDI-CFP], [SOSP-CFP], [EUROSYS-CFP], [ASPLOS-CFP], [ATC-HISTORICAL], [NSDI-CFP], [ACM-TEMPLATE], [USENIX-TEMPLATE].

## VO-03 — Hard requirements are separated from reviewer preferences

- **Nature:** Hard classification rule.
- **Reviewer attack / consequence:** “The review treats optional advice as desk-reject policy, or misses a binding rule because it looks stylistic.”
- **Check:** Label each retrieved item `required`, `prohibited`, `recommended`, `review criterion`, or `unclear`. Preserve exact condition/track/stage; do not infer `must` from examples.
- **Severity:** By underlying rule; classification uncertainty is `S1` until resolved if submission-critical.
- **Exceptions / false positives:** Program-chair FAQs and submission-system validation may clarify official rules; cite them.
- **Repair direction:** Quote/paraphrase minimally with direct official citation and ask organizer only when official sources conflict.
- **Sources:** Current official venue and publisher sources.

## VO-04 — Scope and contribution fit use current review criteria

- **Nature:** Venue requirement / reviewer criterion.
- **Reviewer attack:** “The paper is out of scope or its primary advance is not the kind this venue evaluates.”
- **Check:** Map central problem, contribution type, evaluated object, and audience to official topics and criteria. Treat topic lists as inclusive/exemplary where wording says so.
- **Severity:** `S0` for clear out-of-scope; `S1` for weak fit.
- **Exceptions / false positives:** Interdisciplinary work may fit through its systems/architecture/networking/security contribution; topic keywords alone are not sufficient.
- **Repair direction:** Clarify the target-community advance or choose a fitting venue/track.
- **Sources:** Live target CFP; examples [OSDI-CFP], [SOSP-CFP], [EUROSYS-CFP], [ASPLOS-CFP], [ATC-HISTORICAL], [NSDI-CFP].

## VO-04A — Apply venue emphasis without flattening the contribution

- **Nature:** Review calibration; live official criteria control.
- **Check:** Use the dated snapshot below to select reviewer questions, then verify the target cycle and track before reporting compliance.

| Snapshot checked 2026-09-03 | Decision emphasis | Writing risk to inspect |
|---|---|---|
| OSDI 2027 preliminary, with finalized OSDI 2026 as fallback | Significant systems problem, compelling advance, potential research/practice impact; operational knowledge is a valid contribution | An application result that never becomes a systems advance; an operational story with scale but no reusable knowledge |
| SOSP 2026 | New territory or an important research dialogue; design, implementation, analysis, evaluation, deployment, and measurement can carry the contribution | Principles reduced to slogans, or a narrow artifact with no transferable insight |
| EuroSys 2027 | Benefits, limitations, and advantage over prior work; experience lessons should be general, rigorous, quantitative, and useful | Benefits presented without cost/boundary, or deployment scale substituted for a transferable lesson |
| ASPLOS 2027 | Substantive advance to architecture, OS, PL, or a new domain connected to at least one of those pillars; pros/cons and implementation status matter | Merely using a pillar technique, unexplained cross-layer necessity, or an overclaimed incomplete implementation |
| USENIX ATC 2025, historical only | Practical implementation and experimental evidence, with pros/cons and implementation status | Treating pragmatism as a lower evidence standard or treating ATC as a current submission target |

- **Severity:** Use the live venue's consequence. A mismatch with this snapshot alone is not noncompliance.
- **Repair direction:** Name the actual target-community advance and apply its current official rubric without distorting the contribution type.
- **Sources:** [OSDI-CFP], [SOSP-CFP], [EUROSYS-CFP], [ASPLOS-CFP], [ATC-HISTORICAL].

## VO-04B — Rapid-review page boundaries are applied only when official

- **Nature:** Hard venue rule where currently enacted; otherwise diagnostic heuristic.
- **Check:** Verify the exact review stage and what reviewers are instructed to read. ASPLOS 2027 formally uses a first-two-page rapid review and requires those pages to be self-contained. The OSDI 2027 preliminary CFP only describes a possible early-review procedure; it is not a final rule. For other venues, a two-page test may diagnose discoverability but cannot establish noncompliance.
- **Severity:** `S0`/`S1` by the live ASPLOS rule or another confirmed rule; otherwise report only the underlying reader risk.
- **Exceptions / false positives:** Page boundaries and stages can change before submission. Never transfer one venue's rapid-review rule to another.
- **Repair direction:** Put the decision case and credibility preview inside the actual reviewed unit; do not cram in mechanism inventory merely to satisfy a diagnostic.
- **Sources:** [ASPLOS-CFP], [OSDI-CFP]. Live verification required.

## VO-05 — Format, length, and required content are checked on rendered submission

- **Nature:** Hard submission requirement.
- **Reviewer attack / consequence:** Desk rejection or upload rejection for page count, font/margin, columns, paper size, references/appendix accounting, title/author block, abstract length, or file format.
- **Check:** Retrieve official template/version and rule wording; render final PDF; inspect body/reference/appendix page accounting, paper size, fonts, margins, columns, anonymity fields, file size, and mandatory sections/statements.
- **Severity:** `S0` for verified violation; `S1` if final rendered form unavailable.
- **Exceptions / false positives:** Draft source line count is irrelevant. Do not enforce publisher camera-ready rules on anonymous submission unless the CFP does.
- **Repair direction:** Use official template and remove noncompliant hacks; do not infer compliance from source alone.
- **Sources:** Live target author instructions, [ACM-TEMPLATE] or [USENIX-TEMPLATE] as applicable.

## VO-06 — Anonymity and conflicts are checked across all submitted material

- **Nature:** Hard policy condition where anonymous review applies.
- **Reviewer attack / consequence:** Desk rejection, compromised review, or policy breach.
- **Check:** Verify single/double/open review, self-citation requirements, acknowledgments, artifact/repository anonymity, URLs, PDF metadata, file names, code/user paths, grant text, prior-paper wording, conflicts, and submission-system declarations. Inspect only material in scope; disclose incomplete coverage.
- **Severity:** `S0` for confirmed breach; `S1` for high-risk unassessable artifact/link.
- **Exceptions / false positives:** Some venues permit nonanonymous preprints or artifacts; follow exact policy. Public identity is not inherently a breach.
- **Repair direction:** Apply official anonymization/conflict procedure, not generic deletion that harms scholarship.
- **Sources:** Live target CFP, FAQ, submission and artifact instructions.

## VO-07 — Prior publication, preprint, overlap, and concurrent submission rules are current

- **Nature:** Hard publication-ethics condition.
- **Reviewer attack / consequence:** Rejection or ethics investigation for duplicate/concurrent publication or undisclosed overlap.
- **Check:** Retrieve definitions of prior publication, workshop/preprint allowances, overlap thresholds/procedures, concurrent review, extended versions, disclosure/citation, and author responsibility. Do not make legal/ethical accusations from textual similarity alone.
- **Severity:** `S0` for confirmed violation; `S1` unresolved high-stakes risk.
- **Exceptions / false positives:** Policies vary sharply; preprints are often allowed under conditions.
- **Repair direction:** Disclose/cite/describe overlap as required and seek chair guidance for ambiguity.
- **Sources:** Live target ethics/submission policy and publisher policy.

## VO-08 — Human-subjects, data, security, and ethics requirements are addressed

- **Nature:** Hard policy/ethical condition where applicable.
- **Reviewer attack / consequence:** Missing IRB/ethics review, consent, data authorization, risk disclosure, responsible vulnerability handling, or required ethics statement.
- **Check:** Search official ethics guidance and required statements; inspect study population, personal data, network scanning, vulnerable systems, dual use, environmental/resource cost, and disclosure timeline within scope.
- **Severity:** `S0` for confirmed material violation; `S1` for missing required statement or unresolved approval.
- **Exceptions / false positives:** Not all telemetry or user data constitutes human-subjects research; jurisdiction/institutional determination matters. Do not invent approval requirements.
- **Repair direction:** Add accurate approval/exemption/consent/risk disclosure, change practice if authorized, or consult chairs/institution.
- **Sources:** Live target ethics policy and applicable institutional/legal authority.

## VO-09 — Generative-AI and tool-use policy is verified, not assumed

- **Nature:** Hard venue/publisher policy where stated.
- **Reviewer attack / consequence:** Missing disclosure, prohibited authorship/citation/review use, confidentiality breach, or unsupported generated content.
- **Check:** Retrieve current policy for authoring, disclosure, authorship, figures, code, citations, reviewer confidentiality, and responsibility. Distinguish language assistance from content generation only as official wording does.
- **Severity:** `S0` for confirmed prohibited use/noncompliance; `S1` when disclosure requirement is unresolved.
- **Exceptions / false positives:** Policies differ by venue and year. Never transfer one venue's AI policy to another.
- **Repair direction:** Follow exact disclosure/prohibition and verify all facts/citations/results independently.
- **Sources:** Live venue and publisher AI policy.

## VO-10 — Supplementary material is treated according to reviewer obligations

- **Nature:** Hard venue rule plus general argument principle.
- **Reviewer attack / consequence:** Central evidence is placed in optional, nonarchival, over-limit, or impermissible supplement.
- **Check:** Verify allowed formats/length, reviewer obligation, anonymity, archival status, links, appendices, videos, and whether supplement counts toward limits. Test whether required paper stands alone.
- **Severity:** `S0` for prohibited/over-limit material; `S1` when central case depends on optional material.
- **Exceptions / false positives:** Proofs, extended results, videos, and artifacts may appropriately supplement when official rules allow.
- **Repair direction:** Move central evidence into required paper or narrow claim; package supplement exactly as instructed.
- **Sources:** Live target CFP/author instructions.

## VO-11 — Artifact requirements and badges use the target cycle's definitions

- **Nature:** Hard when artifact submission/evaluation is required or a badge is claimed.
- **Reviewer attack / consequence:** Ineligible artifact, missed deadline, nonanonymous link, or inflated badge/reproduction claim.
- **Check:** Verify eligibility, timing, required/optional status, packaging, availability, reviewer platform, documentation, licenses, anonymity, badges, and paper-artifact linkage. Use `AR` rules for quality.
- **Severity:** `S0` for binding noncompliance; `S1` for missing central artifact support.
- **Exceptions / false positives:** Artifact evaluation may be post-acceptance or optional; do not impose it on initial paper unless current rules do.
- **Repair direction:** Follow target artifact call and calibrate claims/badge language.
- **Sources:** Live target artifact call; [NSDI-ARTIFACT], [ACM-ARTIFACT] for concepts.

## VO-12 — Track-specific evaluation criteria are not flattened

- **Nature:** Hard review-routing condition.
- **Reviewer attack:** “A short/experience/operational/measurement/artifact/deployed/vision track is judged by the wrong contribution or evidence model.”
- **Check:** Retrieve track purpose, eligible contribution types, review criteria, length, required evidence, and relationship to main track. Preserve track-specific values such as operational lessons, negative results, or early vision.
- **Severity:** `S1`; `S0` for ineligible track submission.
- **Exceptions / false positives:** Track names recur across venues but definitions differ.
- **Repair direction:** Apply exact track rubric or reassess track choice.
- **Sources:** Live target track page.

## VO-13 — Deadlines and submission mechanics include timezone and version

- **Nature:** Hard operational requirement when the user asks readiness/schedule.
- **Reviewer attack / consequence:** Missed registration/submission/artifact/revision deadline or wrong submission portal/version.
- **Check:** Verify date, time, timezone/AoE meaning, abstract registration, author freeze, revision windows, portal, file/version policy, and whether updates are allowed. Cross-check official page and linked system.
- **Severity:** `S0` if missed/noncompliant; `S1` if ambiguous.
- **Exceptions / false positives:** Do not add schedule checks to a pure prose review unless requested.
- **Repair direction:** Record exact official timestamp and prerequisite; resolve conflicts with chairs.
- **Sources:** Live official venue page/submission system.

## Live overlay procedure

1. Search the exact venue + cycle + track + stage.
2. Open the official CFP/author instructions; follow official policy/template/artifact links.
3. Record:

   ```text
   Venue:
   Cycle/year:
   Track/round:
   Stage:
   Official URL:
   Last updated on page (if shown):
   Checked at <date/time/timezone>:
   ```

4. Extract only rules relevant to the in-scope material.
5. For each rule, record exact condition, classification, report location, and compliance evidence.
6. If two official pages conflict, prefer the more specific/recent source only when clearly identified; otherwise mark blocked and recommend chair clarification.
7. Do not hardcode retrieved volatile facts back into generic review rules.

## Official entry points studied

- [OSDI 2027 preliminary CFP](https://www.usenix.org/conference/osdi27/call-for-papers)
- [OSDI 2026 finalized CFP](https://www.usenix.org/conference/osdi26/call-for-papers)
- [SOSP 2026 CFP](https://sigops.org/s/conferences/sosp/2026/cfp.html)
- [NSDI 2027 CFP](https://www.usenix.org/conference/nsdi27/call-for-papers)
- [EuroSys 2027 CFP](https://2027.eurosys.org/cfp.html)
- [ASPLOS 2027 CFP](https://www.asplos-conference.org/asplos2027/cfp/)
- [USENIX ATC 2025 submission instructions](https://www.usenix.org/conference/atc25/submission-instructions)
- [USENIX ATC termination announcement](https://www.usenix.org/blog/usenix-atc-announcement)
- [USENIX paper templates](https://www.usenix.org/conferences/author-resources/paper-templates)
- [ACM proceedings templates](https://www.acm.org/publications/proceedings-template)

These links were checked 2026-09-03 as research inputs. They are not automatically the current target for a future request; ATC is historical.

## Venue compliance table

| Rule | Classification | Official source/date | In-scope evidence | Status | Consequence | Required action |
|---|---|---|---|---|---|---|

Use `compliant`, `noncompliant`, `not assessable`, `not applicable`, or `source conflict`. A paper can be scientifically strong and still fail a hard submission rule; report these dimensions separately.
