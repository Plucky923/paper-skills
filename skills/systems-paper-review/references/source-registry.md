# Source Registry and Rule Precedence

This registry gives the evidence hierarchy for review rules. Reference files give citations for the stable source keys below. The rules combine source principles into procedures. They are not quotations.

## Source hierarchy

If sources conflict, use this order:

1. **Venue and track rules in effect** — binding for that submission only.
2. **Publisher/template requirements in effect** — binding formatting and policy constraints.
3. **Primary methodological standards** — strong evidence for study design and reporting.
4. **Standard systems-paper guidance** — standard reviewer expectations, not submission law.
5. **User-provided house style** — binding when the user requests it, in other cases a preference.
6. **Prior skill implementations** — workflow examples only. They give no authority for scientific claims or venue rules.

Give each rule one class:

- `hard requirement`: An official rule in effect or condition for logical or scientific validity.
- `general best practice`: A defensible default with exceptions that depend on context.
- `venue preference`: A clear venue, track, publisher, or template preference.
- `house style`: A user or lab convention.
- `diagnostic heuristic`: An inspection aid. Alone, it does not show a defect.

If an official source in effect contradicts a reference, obey the official source. Record the difference. Treat this registry as outdated until its update.

## User-provided sources

### [USER-NOTES]

**Source:** Chinese systems-paper writing notes supplied by the user.

**Role:** The user's requirements for sequential explanation, terminology, accurate claims, section functions, protocol detail, evaluation interpretation, figures, and LaTeX consistency.

**Normalization:** The notes combine requirements, diagnostic aids, and local LaTeX conventions. Some tactics become misleading as universal rules. These references keep the intent that helps revision. They give context-dependent rules the applicable class.

- These items are not universal defects:
  - `which` attachment, passive voice, and `we`.
  - Number spelling, abbreviation punctuation, paragraph length, and line-end appearance.
  - Float placement, caption punctuation, `\resizebox`, and heading macros.
  - Citation spacing and number-unit spacing.
- Figures must give accurate results. Visual choices must not exaggerate an advantage.
- Term definitions depend on the intended audience. A fixed “undergraduate knows it” test does not apply.
- Cross-references help retrieval where necessary. A cross-reference for each repeated term is not necessary.

### [SYSTEMS-GUIDE]

**Source:** [Systems Paper Writing Guide](https://nia-teams.baichuan-ai.com/f/thu-hpc/public/systems-paper-writing-guide.md), supplied by the user.

**Role:** Reviewer criteria, paper narrative, section purposes, evaluation planning, figure design, and final checklist.

**Status:** Lab or community guidance. Use its instructions as best practices unless a venue rule in effect gives corroboration.

### [ASD-STE100]

**Sources:** ASD Simplified Technical English Maintenance Group,
[About ASD-STE100](https://www.asd-ste100.org/about_STE.html),
[official FAQ](https://www.asd-ste100.org/STE_faq.html), and
[Issue 9: Writing rules and dictionary](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf).

**Supports:** Controlled words with specified meanings and parts of speech. Subject-field technical nouns and verbs. Active voice in Rule 3.6. Information in stages, logical connecting phrases, and one topic per paragraph.

**Instruction revision:** The user requested the standard for the full skill text. Skill procedures use imperative sentences with one action per sentence. Conditions that change actions occur first. Procedural sentences have at most 20 words. Descriptive sentences have at most 25 words.

Descriptive paragraphs have at most six sentences. Section 8 gives punctuation and word-count rules. Dictionary words must have their approved part of speech and meaning. Subject-field exceptions must have a correct technical noun or verb category.

**Research-prose adaptation:** The core applies clarity principles through PT-02, PT-11, PT-18, and paragraph-obligation checks. Bidirectional terminology checks and meaning checks after sentence division are project procedures. They are not quoted STE rules. Research-prose sentence and paragraph limits stay inspection triggers. They do not independently show manuscript defects or give restructuring authority.

**Limit:** This bundle does not certify manuscript STE compliance. Use research meaning and the editing contract for scientific modality, domain terms, necessary qualifications, and permitted research-prose passive voice. Those manuscript allowances do not remove the skill instructions' STE requirements.

**Verification:** On 2026-10-04, revision used the official Issue 9 writing rules and dictionary entries. The source PDF supplies the definitions and examples. Dictionary indexing and sentence counts are inspection aids. They do not show full compliance by themselves.

## Canonical systems-writing sources

### [LEVIN-REDELL]

**Source:** Roy Levin and David D. Redell, [“How (and How Not) to Write a Good Systems Paper”](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/good_paper.html), revised 1993.

**Supports:** Problem with evidence and importance, original ideas, lessons beyond an implementation, clear design choices, relationship to prior work, focus, and clear presentation.

**Limit:** Advice reflects enduring reviewer reasoning, not submission mechanics for the specified cycle.

### [ERNST]

**Source:** Michael D. Ernst, [“How to Write a Technical Paper”](https://homes.cs.washington.edu/~mernst/advice/write-technical-paper.html).

**Supports:** Reader-oriented organization, clear claims, terminology, examples, paragraph and sentence revision, and separating content problems from surface polish.

### [HEISER-STYLE]

**Source:** Gernot Heiser, [Style Guide for Technical Writing](https://gernot-heiser.org/style-guide.html).

**Supports:** Accurate technical prose, structure, terminology, figures, and common style failure modes.

## Evaluation and artifact sources

### [SIGPLAN-EMPIRICAL]

**Source:** ACM SIGPLAN, [Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation/).

**Supports:** Research questions, design validity, sampling, measurement, uncertainty, statistical analysis, transparent reporting, and reproducibility.

**Limit:** A checklist is an aid for expert judgment. It does not replace judgment. Select methods for the research question and system.

### [HEISER-BENCH]

**Source:** Gernot Heiser, [“Systems Benchmarking Crimes”](https://gernot-heiser.org/benchmarking-crimes.html).

**Supports:** Fair baselines, meaningful workloads, measurement rigor, variability, full reporting, and accurate interpretation.

### [NSDI-ARTIFACT]

**Source:** USENIX NSDI 2026, [Call for Artifacts](https://www.usenix.org/conference/nsdi26/call-for-artifacts).

**Supports:** Artifact availability, functionality, reproducibility, documentation, and evaluation against paper claims.

**Limit:** Badge names and required packaging depend on the cycle. Use this source as an artifact-quality model. Examine the target venue's artifact call in effect.

### [ACM-ARTIFACT]

**Source:** ACM, [Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current).

**Supports:** Distinguishing artifact availability, functionality, reusability, and reproduced/replicated results.

## Venue source entry points

These sources give calibration and starting points for venue checks for the specified cycle. Before reuse in another cycle, examine its rules in effect. Include page limits, deadlines, anonymity, AI, artifacts, and review stages.

### [OSDI-CFP]

**Sources:** USENIX, [OSDI 2027 Call for Papers](https://www.usenix.org/conference/osdi27/call-for-papers) and [OSDI 2026 Call for Papers](https://www.usenix.org/conference/osdi26/call-for-papers).

**Supports:** Novelty, significance, interest, clarity, relevance, correctness, practical system contribution, correct conclusions, and the Operational Systems contribution type.

**Status:** Examine whether the target CFP is preliminary or final. A possible review procedure for the first stage becomes mandatory only with an official rule in effect for that stage.

### [SOSP-CFP]

**Source:** ACM SIGOPS, [SOSP 2026 Call for Papers](https://sigops.org/s/conferences/sosp/2026/cfp.html).

**Supports:** Systems scope and submission/policy checks for the specified cycle for SOSP 2026 only.

### [EUROSYS-CFP]

**Source:** EuroSys, [EuroSys 2027 Call for Papers](https://2027.eurosys.org/cfp.html).

**Supports:** Novelty, significance, clarity, correctness, methodological rigor in evidence of benefits and limitations, comparison with prior work, and general quantitative lessons for experience papers.

### [ASPLOS-CFP]

**Source:** ASPLOS, [ASPLOS 2027 Call for Papers](https://www.asplos-conference.org/asplos2027/cfp/).

**Supports:** Important advance in architecture, operating systems, programming languages, or a new-domain pillar. Benefits, costs, and implementation status. Correct empirical methods. Review-stage self-containment where the target CFP in effect makes it mandatory.

### [ATC-WRITING]

**Sources:** USENIX, [ATC 2025 Call for Papers](https://www.usenix.org/conference/atc25/call-for-papers), [ATC 2025 submission instructions](https://www.usenix.org/conference/atc25/submission-instructions), and [ATC termination announcement](https://www.usenix.org/blog/usenix-atc-announcement).

**Supports:** Writing criteria for implementation, experimental results, practical systems, pros/cons, and accurate implementation status.

**Scope:** ATC has concluded. Its criteria stay a writing reference. It is not a submission target.

### [FIVE-VENUE-CORPUS]

**Source:** Repository research report, [OSDI、SOSP、EuroSys、USENIX ATC 与 ASPLOS 系统论文写作要求调研](../../../research/systems-paper-writing-requirements.md). Its appendix links each sampled paper to an official conference page or DOI.

**Corpus:** A stratified purposive sample of 50 accepted papers. It has 10 papers from each of OSDI, SOSP, EuroSys, USENIX ATC, and ASPLOS. Abstract coding covers problem, gap, artifact or approach, insight, evidence, and boundary moves in all 50 papers. Close reading covers full introductions and paragraphs in 13 papers. The sample includes award and non-award papers and multiple contribution types.

**Supports:** Contribution-type selection, function over template, and problem- or question-driven explanation. High-level causal compression, paragraph obligations, first- and last-sentence roles, and sentence information structure. Agreement between claims, evidence, and boundaries. Figures and captions as argument text.

**Limits:** The sample is purposive. It is not random. Award papers occur more frequently in close reads. Abstract coding includes judgment without a second coder who works independently. It cannot give estimates of acceptance probability, venue differences, best paragraph length, or causal effects of prose choices.

Use observed patterns as calibration. Do not use these patterns as submission policy or automatic defect tests.

### [NSDI-CFP]

**Source:** USENIX, [NSDI 2027 Call for Papers](https://www.usenix.org/conference/nsdi27/call-for-papers).

**Supports:** Networking-systems contribution, track-specific review expectations, and submission rules in effect for NSDI 2027 only.

### [ACM-TEMPLATE]

**Source:** ACM, [Proceedings Manuscript Preparation](https://www.acm.org/publications/proceedings-template).

**Supports:** ACM template and production conventions. A conference's author instructions can give different requirements or requirements for a specified case.

### [USENIX-TEMPLATE]

**Source:** USENIX, [USENIX Templates for Conference Papers](https://www.usenix.org/conferences/author-resources/paper-templates).

**Supports:** USENIX template starting points. Examine the target event's call in effect.

## Prior skill implementations studied

These sources give examples of branch selection, progressive disclosure, output structure, evidence handling, and iterative workflows. They do not give scientific truth.

### [OPENAI-SKILL-CREATOR]

**Source:** OpenAI, [Skill Creator](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md).

**Adopted patterns:** Clear trigger description, short entry point, progressive disclosure, clear reference routing, validation.

### [JENSEN-SYSTEMS-SKILL]

**Source:** Jensen Yao, [Systems Paper Writing Skill](https://github.com/Jensen-Yao/agents-skills/blob/main/skills/systems-paper-writing/SKILL.md).

**Adopted patterns:** Systems-specific section reasoning and agreement between claims and evaluation.

### [DEERFLOW-REVIEW]

**Source:** ByteDance DeerFlow, [Academic Paper Review Skill](https://github.com/bytedance/deer-flow/blob/main/skills/public/academic-paper-review/SKILL.md).

**Adopted patterns:** Multi-dimensional review and structured findings.

### [CHAN-DUAL-LENS]

**Source:** ChanMeng, [Academic Paper Review Dimensions](https://github.com/ChanMeng666/academic-paper-review-skill/blob/main/skills/academic-paper-review/references/review-dimensions.md).

**Adopted patterns:** Separating scientific/content review from presentation review.

### [YSLAB-REVISION]

**Source:** YSLAB AI, [Manuscript Writing Skill](https://github.com/YSLAB-ai/manuscript-writing/blob/main/SKILL.md) and [Revision Checklist](https://github.com/YSLAB-ai/manuscript-writing/blob/main/references/revision-checklist.md).

**Adopted patterns:** Revision staging and checklist-driven final verification.

### [BRANDON-EVIDENCE]

**Source:** Brandon, [Academic Writing Skill](https://github.com/Brandon030722/academic-writing-skill/blob/main/academic-writing/SKILL.md).

**Adopted patterns:** Evidence-first claim control and source discipline.

### [SIMCHOWITZ-WRITING]

**Source:** Max Simchowitz, [Paper Writing Skill](https://github.com/msimchowitz/writing-skills/blob/main/for-agents/paper-writing/SKILL.md).

**Adopted patterns:** Author-goal preservation, staged revision, and local-to-global writing checks.

## Agent-orchestration sources

### [OPENAI-CODEX-SUBAGENTS]

**Source:** OpenAI, [Codex Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents).

**Supports:** Codex can obey applicable skill instructions for delegation. Specialized agents can work in parallel and give summaries to the root agent. Read-heavy analysis is a strong starting point. Parallel writes to shared state make caution necessary. Subagents increase token use.

### [OPENAI-MULTI-AGENT]

**Source:** OpenAI, [Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent).

**Supports:** Root and subagent orchestration, bounded independent work, parallel execution, focused contexts, final synthesis, and scheduling within concurrency limits. If work is sequential or has shared-state contention, use one agent if possible.

**Limit:** API availability and schemas can change. Examine the official documentation for the runtime in use. This project uses runtime-available collaboration tools. A sequential fallback always stays available.

## Citation discipline for review reports

- Give citations for the manuscript location for each manuscript-grounded finding.
- Give citations for an artifact path and observable output for each artifact-grounded finding.
- Give a verified direct URL for each external rule or factual correction.
- Give a reasoned extrapolation the label `inference`.
- Give source meanings in new words. Keep copied passages short in reports and reference files.
