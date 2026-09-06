# Systems-paper skill benchmarks

This directory tests observable behavior of the Review, Grill, and Revise workflow.
It does not prescribe fixed manuscript wording. All
fixture passages are synthetic so the benchmark can be distributed without
copying paper text.

The [external benchmark integration](external/README.md) adds pinned public
paragraph-revision tasks (ParaRev) and fixed-output judge calibration
(ParaReval). No external review benchmark is currently admitted. These limited
diagnostics do not replace the acceptance procedure below.

## Layers

Run the deterministic structural layer first:

```bash
python3 scripts/validate_skills.py
```

It checks the three-skill bundle, adaptation attribution, frontmatter and UI metadata, relative Markdown
links, reachable references, cross-skill dependencies, rule/status/source-key
definitions, and the fixture schema. A structural failure blocks behavioral
comparison.

The behavioral layer is a blind current-versus-candidate comparison. It tests
whether each skill preserves scope, evidence, and technical meaning while
performing its distinct role.

## Blind procedure

1. Freeze two immutable skill trees: the current baseline and one candidate.
   Install each complete bundle in a separate temporary environment. Do not run
   either against the working tree.
2. Randomly label the trees `A` and `B`. Keep the mapping from both the runner
   and evaluator until scoring is complete.
3. Start a fresh agent context for every candidate invocation. Single-stage fixtures
   require one invocation per tree; fixture 12 uses two fresh invocations,
   and fixtures 20 and 23 use the five-stage procedure below. The runner projection is exactly `prompt`,
   `scope`, and `evidence`, plus the selected
   tree's named skill and artifacts explicitly authorized by `scope.authorized`.
   Never expose `id`, `title`, `material_origin`, `protected_tokens`,
   `forbidden_actions`, `hard_gates`, `expected_behavior`, or `rubric` to the
   candidate. Those fields belong only to harness control and evaluation. Do
   not tell the agent the expected answer, suspected regression, or the other
   tree's output.
4. Record the final answer, every file or URL read, every write/tool action, and
   any requested clarification. Preserve failures rather than retrying one tree
   selectively.
5. Apply hard gates before quality scoring. A gate failure makes that run fail
   regardless of prose quality.
6. Give the two anonymized outputs and access logs to an independent evaluator.
   Score each of the fixture's twelve one-point rubric items from observable
   evidence. Do not award points for matching a phrase or heading.
7. Reveal `A/B` only after all scores and rationales are frozen.

Use the same model, reasoning effort, tool availability, locale, and time budget
for both trees. If a fixture needs live venue verification, run both versions in
the same time window and retain the retrieved official URLs and relevant rules.

## Gates and acceptance

The fixture's `hard_gates` are binary. Across all fixtures, these universal
conditions also apply:

- no out-of-scope read or write;
- no review-side replacement prose or persistent mutation;
- no revise-side invented fact, citation, experiment, mechanism, or result;
- no loss or semantic change of a protected token or proposition;
- no stale venue rule presented as current without live official verification.

The harness-required reads of the selected candidate skill instructions and the
permitted fixture projection are test inputs, not manuscript or artifact scope.
Record them in the access log, but do not count them as out-of-scope research
access; any additional manuscript, repository, attachment, or external-source
read remains subject to the fixture's authority boundary.

A run passes quality at **10/12 or higher** after passing every hard gate. A
candidate is accepted only when:

- all 34 candidate fixture runs pass their hard gates;
- every candidate run scores at least 10/12;
- no candidate fixture scores below its baseline counterpart; and
- the candidate's total score exceeds the baseline, or a previously observed
  failure is closed without opening another fixture failure.

Do not claim acceptance until a durable closure record has frozen the baseline
and candidate tree digests, hidden-label reveal, model and runtime controls,
per-fixture scores, every hard-gate outcome, access/action logs, observed
failure closure, regression check, and final decision. The closure record is
part of acceptance evidence; an unrecorded ad-hoc run cannot accept a bundle.
For each claimed closure, name the baseline fixture and exact failed gate or
rubric item, preserve the baseline evidence, point to the candidate evidence
that closes it, and show that no new gate or rubric regression was introduced.

If baseline and candidate choose different but evidence-safe prose, score the
reasoning obligations and preserved meaning, not stylistic similarity.

## Fixture schema

Each JSON fixture is self-contained. For single-stage fixtures, `prompt` is a
non-empty string. The runner constructs this exact candidate-visible object:

```json
{"prompt": "...", "scope": {...}, "evidence": {...}}
```

The schema separates candidate inputs from harness-only controls:

- `id`, `title`, and `material_origin`: harness identity and provenance;
- `skills`: harness routing, not candidate-visible instructions;
- `scope`: candidate-visible authorized and excluded material/actions;
- `evidence`: candidate-visible scientific material the run may treat as
  established;
- `protected_tokens`: literal or semantic items that must survive revision;
- `forbidden_actions`: fixture-specific authority boundaries;
- `hard_gates`: binary failure conditions;
- `expected_behavior`: behavioral outcomes, not a golden answer;
- `rubric`: twelve independent one-point checks.

Only `scope` and `evidence` from this list enter the runner projection. All
identity, routing, protection, gate, expectation, and rubric fields remain
harness-only.

Fixture 12 replaces `prompt` with two non-empty `stage_prompts`, `review` and
`revise`, and still counts as one fixture run. Invoke Review in a fresh context
with the runner projection `{prompt: stage_prompts.review, scope, evidence}`.
Record its complete output. Then invoke Revise in a different fresh context
with `{prompt: stage_prompts.revise, scope, evidence}` and attach the complete
Stage 1 output verbatim as the authorized `stage_1_output` artifact. Do not
summarize, edit, annotate, or selectively quote that handoff. Evaluate the two
invocations and their combined access/action log once against fixture 12's hard
gates and twelve-point rubric. This is the supported composition path; it does
not imply a third compose skill or let evaluator-only fields leak into either
stage.

## Full discussion workflows (fixtures 20 and 23)

Fixtures 20 and 23 replace `prompt` with five `stage_prompts` and add
`initial_files` for harness setup. Each still counts as one fixture run. Fixture
20 tests decision persistence and evidence-safe revision; fixture 23 additionally
tests stable coverage/finding IDs, pending authority, full-scope post-edit audit,
and explicit closure states.

Run this separately for each frozen skill tree in a fresh temporary paper project.
The harness writes the two `initial_files` verbatim before invoking any skill.
Replace `{project}` in the current stage's prompt with that project's absolute
path. Treat `initial_files` as harness setup, not extra candidate-visible metadata.
Pass only the current stage prompt, `scope`, `evidence`, and the explicitly named
files. Keep future prompts, especially the author reply, hidden until their turn.

1. **review:** Fresh Review invocation, manuscript read-only. Save its complete
   user-facing report verbatim as `review.md` through the harness, not Review.
2. **grill_open:** Fresh Grill invocation, with only the decision record writable.
   Capture its pending record and questions before continuing. It must not invent
   an answer; absence of a question or premature confirmation is a failure.
3. **grill_confirm:** Send this author reply to the same Grill conversation only
   after step 2 finishes. Capture the confirmed record; do not manually correct it.
4. **revise:** Fresh Revise invocation with no Grill conversation context. Supply
   only the authorized files and current projection. The prompt identifies the
   paper project and its discussion record without spelling out the record's
   filename, exercising the shared default lookup. Only the manuscript is writable.
5. **rereview:** Fresh Review invocation of the resulting files, all read-only.

The harness keeps before/after file contents and action logs outside the paper
project and model context at every stage. Check unchanged-file gates after each
invocation, including preservation of existing D0. Evaluate each combined five-stage
run once against that fixture's gates and rubric. These setup and capture operations
are harness authority, not permission for the skills to write extra files. This
procedure defines a repeatable model test, not an automatic model runner or a claim
that merely validating the JSON executes the workflow.

## Install closure

`bundle.json` is the installation contract. Its mappings contain exactly the
three paper skill directories and the unchanged provenance report. Validate a
staged or installed bundle with:

```bash
python3 scripts/validate_skills.py --install-root /absolute/path/to/codex-root
```

The install root is the directory that contains `skills/` and `research/`.
This mode byte-compares every declared source-to-install mapping, checks all
installed relative Markdown links, and proves that canonical references and
the provenance report remain reachable from their declared skill entrypoints.

## Fixture coverage

| Fixture | Primary failure mode |
|---|---|
| `01-review-scope-trap` | Read-only scope and no replacement prose |
| `02-revise-preservation` | Numbers, conditions, citations, and epistemic status |
| `03-generic-high-level` | Generic abstraction repaired through supported causality |
| `04-concise-low-level` | Short component inventory is not automatically high-level |
| `05-measurement-negative-result` | Measurement and negative-result positive contract |
| `06-operational-experience` | Deployment evidence and transferable lessons |
| `07-benchmark-infrastructure` | Fidelity, coverage, and cost as distinct claims |
| `08-paragraph-density` | Dense/sparse paragraphs split or merged by obligation |
| `09-precision-verbs-logic` | Necessary/sufficient, elimination, and causality verbs |
| `10-chinese-translation` | Explicit actor, causal chain, and evidence-safe translation |
| `11-latex-token-safety` | Protected LaTeX, citation, math, and comment tokens |
| `12-venue-integrated-review-revise` | Live venue rules and review-to-revise composition |
| `13-paragraph-local-revision` | Original paragraph roles, boundaries, content ownership, and manuscript-only output |
| `14-sentence-paragraph-logic` | Exact endpoints of faulty sentence and paragraph links, with valid transitions as controls |
| `15-adequate-prose-optional-wording` | Adequate prose unchanged; clearly beneficial optional wording separated from preserved LaTeX |
| `16-prose-only-scientific-gap` | Safe local correction plus the minimal scientific-gap exception, without silent claim weakening |
| `17-chinese-faithful-local-repair` | Chinese redundancy repair without invented technical explanations or template filling |
| `18-confirmed-grill-handoff` | Apply confirmed author decisions and exclude rejected Grill suggestions |
| `19-grill-pending-record` | Paper-specific clarification, pending decisions, and record-location authority |
| `20-paper-discussion-workflow` | Persist pending and confirmed decisions, apply them in a fresh Revise context, and verify closure with read-only Review |
| `21-top-down-paragraph-roles` | Top-down paper/section audit plus explicit checks for all eight researched paragraph roles |
| `22-coverage-last-clean-units` | Passed-unit visibility and last-section/paragraph/sentence/lexical-occurrence completion |
| `23-coverage-closure-workflow` | Stable unit/finding IDs and complete Review–Grill–Revise closure accounting |
| `24-property-proof-category` | Object-level properties versus proof obligations, with necessity evidence kept separate |
| `25-related-work-root-cause` | Standalone antecedents, parallel comparison axes, and causal Root Cause before a research gap |
| `26-payoff-and-role-review` | Ending information gain and promised insight role versus mechanism-heavy delivery |
| `27-evidence-derived-conclusion` | Completed-paper result payoff from supplied bounded evidence rather than an evaluation placeholder |
| `28-mixed-evaluation-challenge` | Independent evaluation and architectural-Challenge obligations in one paragraph |
| `29-structural-question-authority` | Placement questions remain pending until an exact split/move and destination are authorized |
| `30-limitation-introduction-placement` | Conditional early disclosure for a material applicability boundary without unseen-context movement |
| `31-safe-local-repair-frontier` | Safe local category, payoff, and hierarchy repairs continue while evidence or structure remains blocked |
| `32-cold-review-trigger-checkpoint` | Ordinary blind Review proactively checks mechanical payoff inversion, research-paper result placeholders, and material-limit disclosure |
| `33-missing-result-placeholder-block` | Missing completed-paper results block revision without permitting deletion of the comparison or its scientific boundaries |
| `34-intellectual-move-fanout-grounding` | One claimed insight must expose source-grounded causal edges to every headline outcome rather than rely on reviewer reconstruction |

## Maintaining the benchmark

Add a fixture only for a distinct observed failure mode. Keep synthetic inputs
small enough that scope and proposition preservation can be audited manually.
Update `bundle.json` whenever a canonical reference moves. When a behavioral
rule changes, revise the relevant criterion rather than adding a regex for the
new preferred wording.
