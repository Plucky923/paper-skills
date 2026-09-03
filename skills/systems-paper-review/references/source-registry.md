# Source Registry and Rule Precedence

This registry defines the evidence hierarchy behind the review rules. Reference files cite the stable source keys below. The rules are operational syntheses, not quotations. They were last reconciled on **2026-09-03**.

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

**Source:** Chinese systems-paper writing notes supplied by the user on 2026-09-01.

**Role:** Captures the user's desired attention to linear exposition, terminology, exact claims, section functions, protocol detail, evaluation interpretation, figures, and LaTeX consistency.

**Normalization:** The notes mix hard constraints, useful heuristics, local LaTeX conventions, and tactics that can become misleading when universalized. These references preserve the useful intent while reclassifying context-dependent rules. In particular:

- `which` attachment, passive voice, use of `we`, number spelling, abbreviation punctuation, paragraph length, line-end appearance, float placement, caption punctuation, `\resizebox`, heading macros, citation spacing, and number-unit spacing are not universal defects;
- figures must represent results honestly, not choose axes, aspect ratios, or formats merely to magnify an advantage;
- terms should be defined for the intended audience, not by a fixed “undergraduate knows it” test;
- cross-references should help retrieval when needed, not mechanically accompany every repeated term.

### [SYSTEMS-GUIDE]

**Source:** [Systems Paper Writing Guide](https://nia-teams.baichuan-ai.com/f/thu-hpc/public/systems-paper-writing-guide.md), supplied by the user and checked 2026-09-01.

**Role:** Reviewer criteria, paper narrative, section purposes, evaluation planning, figure design, and final checklist.

**Status:** Lab/community guidance. Treat prescriptions as best practices unless corroborated by a current venue rule.

## Canonical systems-writing sources

### [LEVIN-REDELL]

**Source:** Roy Levin and David D. Redell, [“How (and How Not) to Write a Good Systems Paper”](https://www.usenix.org/legacy/publications/library/proceedings/dsl97/good_paper.html), revised 1993; USENIX-hosted version checked 2026-09-01.

**Supports:** Real and significant problem, original ideas, lessons beyond an implementation, explicit design choices, relationship to prior work, focus, and clear presentation.

**Limit:** Advice reflects enduring reviewer reasoning, not current submission mechanics.

### [ERNST]

**Source:** Michael D. Ernst, [“How to Write a Technical Paper”](https://homes.cs.washington.edu/~mernst/advice/write-technical-paper.html), checked 2026-09-01.

**Supports:** Reader-oriented organization, clear claims, terminology, examples, paragraph and sentence revision, and separating content problems from surface polish.

### [HEISER-STYLE]

**Source:** Gernot Heiser, [Style Guide for Technical Writing](https://gernot-heiser.org/style-guide.html), checked 2026-09-01.

**Supports:** Precise technical prose, structure, terminology, figures, and common style failure modes.

## Evaluation and artifact sources

### [SIGPLAN-EMPIRICAL]

**Source:** ACM SIGPLAN, [Empirical Evaluation Guidelines](https://www.sigplan.org/Resources/EmpiricalEvaluation/), checked 2026-09-01.

**Supports:** Research questions, design validity, sampling, measurement, uncertainty, statistical analysis, transparent reporting, and reproducibility.

**Limit:** A checklist supports expert judgment; it does not replace it. Adapt methods to the research question and system.

### [HEISER-BENCH]

**Source:** Gernot Heiser, [“Systems Benchmarking Crimes”](https://gernot-heiser.org/benchmarking-crimes.html), checked 2026-09-01.

**Supports:** Fair baselines, meaningful workloads, measurement rigor, variability, complete reporting, and honest interpretation.

### [NSDI-ARTIFACT]

**Source:** USENIX NSDI 2026, [Call for Artifacts](https://www.usenix.org/conference/nsdi26/call-for-artifacts), checked 2026-09-01.

**Supports:** Artifact availability, functionality, reproducibility, documentation, and evaluation against paper claims.

**Limit:** Badge names and required packaging are cycle-specific. Use as a durable artifact-quality model; verify the target venue's current artifact call.

### [ACM-ARTIFACT]

**Source:** ACM, [Artifact Review and Badging](https://www.acm.org/publications/policies/artifact-review-and-badging-current), checked 2026-09-01.

**Supports:** Distinguishing artifact availability, functionality, reusability, and reproduced/replicated results.

## Current venue sources

These sources illustrate common systems-PC criteria and are also entry points for live overlays. Never copy their volatile dates, page limits, anonymity rules, AI policies, or artifact requirements into a different cycle without verification.

### [OSDI-CFP]

**Source:** USENIX, [OSDI 2026 Call for Papers](https://www.usenix.org/conference/osdi26/call-for-papers), checked 2026-09-03.

**Supports:** Novelty, significance, interest, clarity, relevance, correctness, practical system contribution, and sound conclusions.

### [SOSP-CFP]

**Source:** ACM SIGOPS, [SOSP 2026 Call for Papers](https://sigops.org/s/conferences/sosp/2026/cfp.html), checked 2026-09-03.

**Supports:** Systems scope and current submission/policy checks for SOSP 2026 only.

### [OSDI-SOSP-CORPUS]

**Index sources:** Official accepted-paper or technical-session pages for [OSDI 2020](https://www.usenix.org/conference/osdi20/accepted-papers), [OSDI 2022](https://www.usenix.org/conference/osdi22/technical-sessions), [OSDI 2023](https://www.usenix.org/conference/osdi23/technical-sessions), [OSDI 2024](https://www.usenix.org/conference/osdi24/technical-sessions), [OSDI 2025](https://www.usenix.org/conference/osdi25/technical-sessions), [OSDI 2026](https://www.usenix.org/conference/osdi26/technical-sessions), [SOSP 2021](https://sigops.org/s/conferences/sosp/2021/toc.html), [SOSP 2023](https://sigops.org/s/conferences/sosp/2023/toc.html), [SOSP 2024](https://sigops.org/s/conferences/sosp/2024/schedule.html), and [SOSP 2025](https://sigops.org/s/conferences/sosp/2025/accepted.html), checked 2026-09-03.

**Corpus:** 600 accepted-paper records, including 490 extractable abstracts. A stratified close-reading set contained 30 full papers from OSDI and SOSP, spanning award and non-award papers and abstraction/interface, performance, distributed systems, storage, verification, security, measurement/experience, operational, and ML-systems contributions. Twenty-nine introductions were reliably extractable for structural checks; selected papers were also inspected in rendered form.

**Representative close reads:** [Delos](https://www.usenix.org/conference/osdi20/presentation/balakrishnan), [Cancellation in Systems Software](https://www.usenix.org/conference/osdi22/presentation/sethi), [Ensō](https://www.usenix.org/conference/osdi23/presentation/sadok), [ServiceLab](https://www.usenix.org/conference/osdi24/presentation/chow), [Basilisk](https://www.usenix.org/conference/osdi25/presentation/zhang-tony), [Omniglot](https://www.usenix.org/conference/osdi25/presentation/schuermann), [large-scale LLM data pipelines](https://www.usenix.org/conference/osdi26/presentation/chen-luofan), [Semisolates and Try](https://www.usenix.org/conference/osdi26/presentation/lamprou), [Colloid](https://www.cs.cornell.edu/~ragarwal/pubs/colloid.pdf), and [Wasabi](https://bastoica.github.io/files/papers/2024_sosp_wasabi.pdf). These examples calibrate different archetypes; no individual paper is a universal writing model.

**Observed abstract calibration:** A surface-marker scan found problem/limitation language before proposal language in 384/490 abstracts (78.4%), proposal-first openings in 57/490 (11.6%), quantified results in 302/490 (61.6%), and result/evidence language in the final sentence of 373/490 (76.1%). These lexical counts corroborate close reading but do not identify causal structure by themselves.

**Observed full-text calibration:** Among 29 extractable introductions, 23 used a concrete example/scenario marker, 14 referred to Figure 1 or 2 early, 28 previewed evaluation/results/production evidence, 24 gave a concrete quantified result, and 17 used an explicit contribution list. Only four used the literal word `insight`, even though the intellectual move was usually recoverable without that label.

**Supports:** Paper-archetype routing; function-over-form checks; problem or tension made recoverable before detailed mechanism; thesis-to-design-to-evidence alignment; running examples and early figures as optional reasoning devices; headline-result hierarchy; and evidence-bearing abstract/introduction endings.

**Limits:** The abstract analysis uses lexical heuristics, not semantic or causal annotation. The close-reading set is purposive rather than a random sample. Accepted-paper patterns are not official rules, rejected-paper controls are unavailable, and no observed feature should be presented as causing acceptance. Use the corpus to challenge brittle templates, not to create new ones.

## Award-paper exposition samples

These samples calibrate how successful papers expose an argument; awards do not make every sentence a universal model. Use the samples to test whether a reader can recover problem, constraint, insight, principle, realization, and evidence—not to imitate phrasing, paragraph count, or section order.

### [OSDI-BEST-SAMPLE]

**Sources:** USENIX's official [Best Papers list](https://www.usenix.org/conferences/best-papers); the OSDI 2025 best-paper pages for [Basilisk](https://www.usenix.org/conference/osdi25/presentation/zhang-tony) and [Omniglot](https://www.usenix.org/conference/osdi25/presentation/schuermann); and the OSDI 2026 best-paper pages for [Semisolates and Try](https://www.usenix.org/conference/osdi26/presentation/lamprou), [Ambulance](https://www.usenix.org/conference/osdi26/presentation/giridharan), and [large-scale LLM data pipelines](https://www.usenix.org/conference/osdi26/presentation/chen-luofan). Abstracts and introduction openings checked 2026-09-03.

**Supports:** Empirical calibration of problem-first openings, causal abstraction, concise statement of the central idea, and evidence-bounded endings in recent OSDI award papers.

**Observed pattern:** The papers differ in style, but they make the motivating failure, constraint, or operational cost recoverable before—or in the same breath as—the solution. Their high-level descriptions name the leverage or changed constraint that makes the result possible before expanding into components. Operational papers may begin with quantified production evidence rather than a new abstraction.

**Limit:** This is a small purposive sample, not an official OSDI writing rule or proof that the pattern causes acceptance.

### [SOSP-BEST-SAMPLE]

**Sources:** The official [SOSP 2024 awards page](https://sigops.org/s/conferences/sosp/2024/); award papers [OZZ](https://doi.org/10.1145/3694715.3695944), [LazyLog](https://doi.org/10.1145/3694715.3695983), and [FBDetect](https://doi.org/10.1145/3694715.3695977). Abstracts and introduction openings checked 2026-09-03.

**Supports:** Empirical calibration of problem-driven narrowing, principle-before-realization exposition, paragraph-level claim/support/implication flow, and the distinct evidence-first form used by operational systems papers.

**Observed pattern:** LazyLog turns an eager-ordering cost into a timing insight and then an abstraction; OZZ turns an uncontrolled source of nondeterminism into an observable and controllable testing target; FBDetect begins with the measured production cost and derives the design challenges. These are different argument shapes with the same requirement that each mechanism answer an already visible problem.

**Limit:** This is a small purposive sample, not an official SOSP writing rule or a mandatory narrative template.

### [NSDI-CFP]

**Source:** USENIX, [NSDI 2027 Call for Papers](https://www.usenix.org/conference/nsdi27/call-for-papers), checked 2026-09-01.

**Supports:** Networking-systems contribution, track-specific review expectations, and current submission rules for NSDI 2027 only.

### [EUROSYS-CFP]

**Source:** EuroSys, [EuroSys 2026 Call for Papers](https://2026.eurosys.org/cfp.html), checked 2026-09-01.

**Supports:** Broad systems scope and current EuroSys 2026 rules.

### [ASPLOS-CFP]

**Source:** ASPLOS, [ASPLOS 2026 Call for Papers](https://www.asplos-conference.org/asplos2026/cfp/), checked 2026-09-01.

**Supports:** Cross-layer architecture, programming languages, and operating-systems scope and current ASPLOS 2026 rules.

### [ACM-TEMPLATE]

**Source:** ACM, [Proceedings Manuscript Preparation](https://www.acm.org/publications/proceedings-template), checked 2026-09-01.

**Supports:** ACM template and production conventions. A conference's author instructions may override or specialize them.

### [USENIX-TEMPLATE]

**Source:** USENIX, [USENIX Templates for Conference Papers](https://www.usenix.org/conferences/author-resources/paper-templates), checked 2026-09-01.

**Supports:** USENIX template entry points. Always verify the target event's call.

## Prior skill implementations studied

These sources inform routing, progressive disclosure, structured outputs, evidence handling, and iterative workflows. They do not define scientific truth.

### [OPENAI-SKILL-CREATOR]

**Source:** OpenAI, [Skill Creator](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md), checked 2026-09-01.

**Adopted patterns:** Clear trigger description, concise entry point, progressive disclosure, explicit reference routing, validation.

### [JENSEN-SYSTEMS-SKILL]

**Source:** Jensen Yao, [Systems Paper Writing Skill](https://github.com/Jensen-Yao/agents-skills/blob/main/skills/systems-paper-writing/SKILL.md), checked 2026-09-01.

**Adopted patterns:** Systems-specific section reasoning and claim/evaluation alignment.

### [DEERFLOW-REVIEW]

**Source:** ByteDance DeerFlow, [Academic Paper Review Skill](https://github.com/bytedance/deer-flow/blob/main/skills/public/academic-paper-review/SKILL.md), checked 2026-09-01.

**Adopted patterns:** Multi-dimensional review and structured findings.

### [CHAN-DUAL-LENS]

**Source:** ChanMeng, [Academic Paper Review Dimensions](https://github.com/ChanMeng666/academic-paper-review-skill/blob/main/skills/academic-paper-review/references/review-dimensions.md), checked 2026-09-01.

**Adopted patterns:** Separating scientific/content review from presentation review.

### [YSLAB-REVISION]

**Source:** YSLAB AI, [Manuscript Writing Skill](https://github.com/YSLAB-ai/manuscript-writing/blob/main/SKILL.md) and [Revision Checklist](https://github.com/YSLAB-ai/manuscript-writing/blob/main/references/revision-checklist.md), checked 2026-09-01.

**Adopted patterns:** Revision staging and checklist-driven final verification.

### [BRANDON-EVIDENCE]

**Source:** Brandon, [Academic Writing Skill](https://github.com/Brandon030722/academic-writing-skill/blob/main/academic-writing/SKILL.md), checked 2026-09-01.

**Adopted patterns:** Evidence-first claim control and source discipline.

### [SIMCHOWITZ-WRITING]

**Source:** Max Simchowitz, [Paper Writing Skill](https://github.com/msimchowitz/writing-skills/blob/main/for-agents/paper-writing/SKILL.md), checked 2026-09-01.

**Adopted patterns:** Author-goal preservation, staged revision, and local-to-global writing checks.

## Agent-orchestration sources

### [OPENAI-CODEX-SUBAGENTS]

**Source:** OpenAI, [Codex Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents), checked 2026-09-02.

**Supports:** Codex can follow applicable skill instructions that request delegation; specialized agents can work in parallel and return summaries to the main agent; read-heavy analysis is a strong starting point; parallel writes to shared state require caution; subagents increase token use.

### [OPENAI-MULTI-AGENT]

**Source:** OpenAI, [Multi-agent](https://developers.openai.com/api/docs/guides/responses-multi-agent), checked 2026-09-02.

**Supports:** Root/subagent orchestration, bounded independent workstreams, parallel execution, focused contexts, final synthesis, concurrency-aware scheduling, and the preference for one agent when work is sequential or agents would contend over shared mutable state.

**Limit:** The documented Responses API feature is beta and its API schema may change. This project relies on the collaboration tools available at runtime and always retains a sequential fallback.

## Citation discipline for review reports

- Cite the manuscript location for every manuscript-grounded finding.
- Cite an artifact path and observable output for every artifact-grounded finding.
- Give a direct URL and verification date for every external rule or factual correction.
- Label a reasoned extrapolation as inference.
- Never use a prior skill implementation as evidence that a scientific or venue-specific claim is true.
- Paraphrase sources. Do not copy long passages into reports or reference files.
