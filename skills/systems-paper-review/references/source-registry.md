# Source Registry and Rule Precedence

This registry defines the evidence hierarchy behind the review rules. Reference files cite the stable source keys below. The rules are operational syntheses, not quotations.

## Source hierarchy

When sources conflict, apply this order:

1. **Current venue and track rules** — binding for that submission only.
2. **Current publisher/template requirements** — binding formatting and policy constraints.
3. **Primary methodological standards** — strong evidence for study design and reporting.
4. **Canonical systems-paper guidance** — durable reviewer expectations, not submission law.
5. **User-provided house style** — binding when the user requests it, otherwise a preference.
6. **Prior skill implementations** — workflow inspiration only; never authority for a scientific claim or venue rule.

Classify a rule as:

- `hard requirement`: a current official rule or a logical/scientific validity condition;
- `general best practice`: a broadly defensible default with contextual exceptions;
- `venue preference`: a stated preference of a venue, track, publisher, or template;
- `house style`: a user or lab convention;
- `diagnostic heuristic`: a prompt for inspection, never sufficient by itself to declare a defect.

If a current official source contradicts a reference file, follow the official source, record the discrepancy, and treat this registry as stale until updated.

## User-provided sources

### [USER-NOTES]

**Source:** Chinese systems-paper writing notes supplied by the user.

**Role:** Captures the user's desired attention to linear exposition, terminology, exact claims, section functions, protocol detail, evaluation interpretation, figures, and LaTeX consistency.

**Normalization:** The notes mix hard constraints, useful heuristics, local LaTeX conventions, and tactics that can become misleading when universalized. These references preserve the useful intent while reclassifying context-dependent rules. In particular:

- `which` attachment, passive voice, use of `we`, number spelling, abbreviation punctuation, paragraph length, line-end appearance, float placement, caption punctuation, `\resizebox`, heading macros, citation spacing, and number-unit spacing are not universal defects;
- figures must represent results honestly, not choose axes, aspect ratios, or formats merely to magnify an advantage;
- terms should be defined for the intended audience, not by a fixed “undergraduate knows it” test;
- cross-references should help retrieval when needed, not mechanically accompany every repeated term.

### [SYSTEMS-GUIDE]

**Source:** [Systems Paper Writing Guide](https://nia-teams.baichuan-ai.com/f/thu-hpc/public/systems-paper-writing-guide.md), supplied by the user.

**Role:** Reviewer criteria, paper narrative, section purposes, evaluation planning, figure design, and final checklist.

**Status:** Lab/community guidance. Treat prescriptions as best practices unless corroborated by a current venue rule.

## Canonical systems-writing sources

### [LEVIN-REDELL]

**Source:** Roy Levin and David D. Redell, [“How (and How Not) to Write a Good Systems Paper”](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/good_paper.html), revised 1993.

**Supports:** Real and significant problem, original ideas, lessons beyond an implementation, explicit design choices, relationship to prior work, focus, and clear presentation.

**Limit:** Advice reflects enduring reviewer reasoning, not current submission mechanics.

### [ERNST]

**Source:** Michael D. Ernst, [“How to Write a Technical Paper”](https://homes.cs.washington.edu/~mernst/advice/write-technical-paper.html).

**Supports:** Reader-oriented organization, clear claims, terminology, examples, paragraph and sentence revision, and separating content problems from surface polish.

### [HEISER-STYLE]

**Source:** Gernot Heiser, [Style Guide for Technical Writing](https://gernot-heiser.org/style-guide.html).

**Supports:** Precise technical prose, structure, terminology, figures, and common style failure modes.

## Evaluation and artifact sources

### [SIGPLAN-EMPIRICAL]

**Source:** ACM SIGPLAN, [Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation/).

**Supports:** Research questions, design validity, sampling, measurement, uncertainty, statistical analysis, transparent reporting, and reproducibility.

**Limit:** A checklist supports expert judgment; it does not replace it. Adapt methods to the research question and system.

### [HEISER-BENCH]

**Source:** Gernot Heiser, [“Systems Benchmarking Crimes”](https://gernot-heiser.org/benchmarking-crimes.html).

**Supports:** Fair baselines, meaningful workloads, measurement rigor, variability, complete reporting, and honest interpretation.

### [NSDI-ARTIFACT]

**Source:** USENIX NSDI 2026, [Call for Artifacts](https://www.usenix.org/conference/nsdi26/call-for-artifacts).

**Supports:** Artifact availability, functionality, reproducibility, documentation, and evaluation against paper claims.

**Limit:** Badge names and required packaging are cycle-specific. Use as a durable artifact-quality model; verify the target venue's current artifact call.

### [ACM-ARTIFACT]

**Source:** ACM, [Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current).

**Supports:** Distinguishing artifact availability, functionality, reusability, and reproduced/replicated results.

## Venue source entry points

These cycle-specific sources support calibration and are entry points for live overlays. Never copy page limits, deadlines, anonymity, AI, artifact, or review-stage rules into another cycle without verification.

### [OSDI-CFP]

**Sources:** USENIX, [OSDI 2027 Call for Papers](https://www.usenix.org/conference/osdi27/call-for-papers) and [OSDI 2026 Call for Papers](https://www.usenix.org/conference/osdi26/call-for-papers).

**Supports:** Novelty, significance, interest, clarity, relevance, correctness, practical system contribution, sound conclusions, and the Operational Systems contribution type.

**Status:** Verify whether the target cycle's CFP is preliminary or final. A possible early-review procedure is binding only when a live official page confirms it for the target stage.

### [SOSP-CFP]

**Source:** ACM SIGOPS, [SOSP 2026 Call for Papers](https://sigops.org/s/conferences/sosp/2026/cfp.html).

**Supports:** Systems scope and current submission/policy checks for SOSP 2026 only.

### [EUROSYS-CFP]

**Source:** EuroSys, [EuroSys 2027 Call for Papers](https://2027.eurosys.org/cfp.html).

**Supports:** Novelty, significance, clarity, correctness, rigorous evidence of benefits and limitations, comparison with prior work, and general quantitative lessons for experience papers.

### [ASPLOS-CFP]

**Source:** ASPLOS, [ASPLOS 2027 Call for Papers](https://www.asplos-conference.org/asplos2027/cfp/).

**Supports:** Substantive advancement of at least one architecture, operating-systems, programming-languages, or new-domain pillar; pros/cons and implementation-status disclosure; sound empirical methods; and review-stage self-containment where required by the live target CFP.

### [ATC-WRITING]

**Sources:** USENIX, [ATC 2025 Call for Papers](https://www.usenix.org/conference/atc25/call-for-papers), [ATC 2025 submission instructions](https://www.usenix.org/conference/atc25/submission-instructions), and [ATC termination announcement](https://www.usenix.org/blog/usenix-atc-announcement).

**Supports:** Writing criteria for implementation, experimental results, practical systems, pros/cons, and honest implementation status.

**Scope:** ATC has concluded. Use its criteria as a writing reference, not as a submission target.

### [FIVE-VENUE-CORPUS]

**Source:** Repository research report, [OSDI、SOSP、EuroSys、USENIX ATC 与 ASPLOS 系统论文写作要求调研](../../../research/systems-paper-writing-requirements.md). Its appendix links every sampled paper to an official conference page or DOI.

**Corpus:** A stratified purposive sample of 50 accepted papers, 10 each from OSDI, SOSP, EuroSys, USENIX ATC, and ASPLOS. All 50 abstracts were coded for explicit problem, gap, artifact/approach, insight, evidence, and boundary moves; 13 papers received full-introduction and paragraph-level close reading. The sample spans award and non-award papers and multiple contribution types.

**Supports:** Contribution-type routing; function over template; problem- or question-driven exposition; high-level causal compression; paragraph obligations and first/last-sentence roles; sentence information structure; claim/evidence/boundary alignment; and figures/captions as argumentative text.

**Limits:** The sample is purposive, not random; close reads overrepresent award papers; abstract coding contains judgment and has no second independent coder. It cannot estimate acceptance probability, venue differences, ideal paragraph length, or causal effects of prose choices. Treat all observed patterns as calibration, never submission policy or automatic defect tests.

### [NSDI-CFP]

**Source:** USENIX, [NSDI 2027 Call for Papers](https://www.usenix.org/conference/nsdi27/call-for-papers).

**Supports:** Networking-systems contribution, track-specific review expectations, and current submission rules for NSDI 2027 only.

### [ACM-TEMPLATE]

**Source:** ACM, [Proceedings Manuscript Preparation](https://www.acm.org/publications/proceedings-template).

**Supports:** ACM template and production conventions. A conference's author instructions may override or specialize them.

### [USENIX-TEMPLATE]

**Source:** USENIX, [USENIX Templates for Conference Papers](https://www.usenix.org/conferences/author-resources/paper-templates).

**Supports:** USENIX template entry points. Always verify the target event's call.

## Prior skill implementations studied

These sources inform routing, progressive disclosure, structured outputs, evidence handling, and iterative workflows. They do not define scientific truth.

### [OPENAI-SKILL-CREATOR]

**Source:** OpenAI, [Skill Creator](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md).

**Adopted patterns:** Clear trigger description, concise entry point, progressive disclosure, explicit reference routing, validation.

### [JENSEN-SYSTEMS-SKILL]

**Source:** Jensen Yao, [Systems Paper Writing Skill](https://github.com/Jensen-Yao/agents-skills/blob/main/skills/systems-paper-writing/SKILL.md).

**Adopted patterns:** Systems-specific section reasoning and claim/evaluation alignment.

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

**Supports:** Codex can follow applicable skill instructions that request delegation; specialized agents can work in parallel and return summaries to the main agent; read-heavy analysis is a strong starting point; parallel writes to shared state require caution; subagents increase token use.

### [OPENAI-MULTI-AGENT]

**Source:** OpenAI, [Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent).

**Supports:** Root/subagent orchestration, bounded independent workstreams, parallel execution, focused contexts, final synthesis, concurrency-aware scheduling, and the preference for one agent when work is sequential or agents would contend over shared mutable state.

**Limit:** API availability and schema may change; verify the official documentation for the runtime in use. This project relies on the collaboration tools available at runtime and always retains a sequential fallback.

## Citation discipline for review reports

- Cite the manuscript location for every manuscript-grounded finding.
- Cite an artifact path and observable output for every artifact-grounded finding.
- Give a verified direct URL for every external rule or factual correction.
- Label a reasoned extrapolation as inference.
- Paraphrase sources. Do not copy long passages into reports or reference files.
