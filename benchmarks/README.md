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

It checks the three-skill bundle, attribution, frontmatter, UI metadata, relative links and reachable references.
It also checks cross-skill dependencies, rule/status/source-key definitions and fixture schemas.
A structural failure blocks behavioral comparison.

The behavioral layer is a blind current-versus-candidate comparison. It tests
whether each skill preserves scope, evidence, and technical meaning while
performing its distinct role.

## Model execution

Use [internal_benchmarks.py](../scripts/internal_benchmarks.py) to generate actual
model outputs from a frozen bundle. The bundle must contain `skills/`,
`research/`, and `benchmarks/`. Keep generation evidence outside that bundle.
Select the model and reasoning effort explicitly:

```bash
python3 -B scripts/internal_benchmarks.py run \
  --tree /absolute/path/to/frozen-bundle --suite manuscript \
  --output /absolute/path/to/new-manuscript-run \
  --model MODEL --effort high --jobs 3 --timeout 240

python3 -B scripts/internal_benchmarks.py run \
  --tree /absolute/path/to/frozen-bundle --suite authoring \
  --output /absolute/path/to/new-authoring-run \
  --model MODEL --effort high --jobs 3 --timeout 240
```

The manuscript suite contains 49 cases and 62 model invocations. The separate
authoring suite contains six cases. Use `--cases 1,7,43-49` for a focused diagnostic.
Existing output directories are refused. Failed invocations stay in the record;
the runner does not retry them.

The runner supplies frozen guidance inline and disables ambient skills, project
instructions, memories, and plugins. Text cases have no tools. Workflow cases use
real project files; Grill confirmation resumes the captured conversation UUID.
Fixture 12 uses live web search and a verbatim handoff between fresh contexts.
Fixtures and expected answers remain separate from candidate-visible input.

Each invocation saves the input, prompt, runtime controls, raw events, stderr,
answer, hashes, and runtime result. File workflows also save project contents
before and after each stage. Known CLI startup warnings are recorded separately
from candidate tool actions. Unknown errors still fail the runtime check.

Generation status `completed_unscored` means only that the invocation completed
within its runtime and write constraints. An independent evaluator must still
check every hard gate and all twelve rubric items. These runs test execution of
inline guidance; they do not test native skill discovery. Tool events and project
snapshots do not provide a complete filesystem access log. A development run or
focused retest alone does not satisfy the blind acceptance procedure below.

Use the `acceptance` mode for progressive instruction loading with a controlled,
audited access surface:

```bash
python3 -B scripts/internal_benchmarks.py acceptance \
  --tree /absolute/path/to/anonymous-frozen-tree --suite manuscript \
  --output /absolute/path/to/new-anonymous-run \
  --model MODEL --effort high --jobs 3 --timeout 900
```

Prepare the anonymous tree copies and hidden baseline/candidate map separately.
The runner does not receive that map. It installs the complete declared bundle
under each run's separate environment and freezes a runnable harness copy.
The model receives named instruction entrypoint paths and the permitted fixture
projection. It reads the entrypoints and required references through an
allowlisted MCP server. Guidance is not supplied inline. The separate authoring
suite exposes only its exact STE guidance section, although the complete bundle
is installed.

The model has no shell, arbitrary-code, ambient plugin, memory, or other file
access tool. The MCP server records each allowed or denied candidate action,
exact file bytes, returned content, and a hash chain. Project writes are enabled
only for the current stage's declared files. For fixture 12, the server retrieves
live official ASPLOS text/HTML pages and retains URLs, timestamps, response
headers, full response bytes, extracted text, and official links. Runtime
authentication and CLI session storage are harness infrastructure; they are not
exposed by the candidate tools. This mode tests explicitly routed skills with
progressive loading, not automatic native skill selection.
Known unavailability of an allowed official source is retained as an unavailable
verification result. It establishes no current venue rule; the fixture still
permits an explicitly unresolved venue assessment.

For fixture 23, final Review also receives the preceding Revise editorial output
byte-for-byte as `revision_audit_output`. This identical protocol supplement in
both anonymous conditions carries the chat-only coverage and location map from
authorized manuscript edits. It adds no scientific evidence or write authority.
The original `review.md` remains byte-exact. Keeping this artifact is necessary
to audit intermediate ID continuity rather than reconstructing it only from the
initial and final manuscript. Record the supplement in the closure record.

Unknown emitted events, unexpected tools, denied/failed access, missing required
entrypoint reads, an altered installed bundle, or invalid access evidence fail
the runtime check. `--cases` supports development diagnostics; only the complete
blind comparison with frozen independent scores can satisfy acceptance.
The runner also freezes its runtime model catalog. Pass the same
`--model-catalog /absolute/path/to/frozen-catalog.json` to both conditions so an
isolated CLI home does not refresh model metadata independently. Unknown CLI
error or warning lines fail the runtime check. `input-access.json` records the
prompt/projection and exact handoff delivery, separately from model-initiated
MCP access.
Every invocation uses both a UTC wall-clock deadline and a monotonic deadline.
It stops when either budget expires, including immediately after a suspended
host resumes. Records include actual wall-clock elapsed time and the monotonic
measurement separately. A wall-clock budget overrun fails the runtime check.

## Latest development evaluation

See the [2026-10-04 model evaluation](reports/2026-10-04-model-evaluation.md) for actual generation, independent scores, revisions, and unresolved failures.
The report distinguishes development tests from formal acceptance and retains the negative results.

## Blind procedure

1. Freeze two immutable skill trees: the current baseline and one candidate.
   Install each complete bundle in a separate temporary environment. Do not run
   either against the working tree.
2. Randomly label the trees `A` and `B`. Keep the mapping from both the runner
   and evaluator until scoring is complete.
3. Start a fresh agent context for every candidate invocation. Single-stage fixtures
   require one invocation per tree. Fixture 12 uses two fresh invocations.
   Fixtures 20, 23, and 39 use the five-stage procedure below.
   Supply `prompt`, `scope`, and the permitted `evidence` projection, plus the selected
   tree's named skill and artifacts explicitly authorized by `scope.authorized`.
   Use the stage-specific evidence limits below for multi-stage fixtures.

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

Check each task's author instructions against its evaluator requirements before running it.
Explicit author output restrictions take precedence over skill defaults.
A conflicting task oracle cannot test skill compliance fairly.
The [output-authority record](task-input-authority.json) preserves the five repaired task prompts and all original hashes.
These repairs explicitly authorize existing required metadata; gates, rubrics, scientific material, and scope stay unchanged.
Apply the same repaired task inputs to both instruction trees in a new full comparison.
Keep earlier runs and scores intact.

The fixture's `hard_gates` are binary. Across all fixtures, these universal
conditions also apply:

- no out-of-scope read or write;
- no review-side replacement prose or persistent mutation;
- no revise-side invented fact, citation, experiment, mechanism, or result;
- no loss or semantic change of a protected token or proposition;
- no stale venue rule presented as current without live official verification.

The harness-required reads of the selected candidate skill instructions and the
permitted fixture projection are test inputs, not manuscript or artifact scope.
Record those inputs in the access log. Do not count them as out-of-scope research access.
Each additional manuscript, repository, attachment or external-source read remains subject to the fixture's authority boundary.

A run passes quality at **10/12 or higher** after passing every hard gate. A
candidate is accepted only when:

- all 49 candidate fixture runs pass their hard gates;
- every candidate run scores at least 10/12;
- no candidate fixture scores below its baseline counterpart; and
- the candidate's total score exceeds the baseline, or a previously observed
  failure is closed without opening another fixture failure.

Do not claim acceptance before saving a durable closure record.
Freeze both tree digests, hidden-label reveal, model/runtime controls, per-fixture scores and every hard-gate outcome in that record.
Also freeze access/action logs, observed failure closure, regression checks and the final decision.
An unrecorded ad-hoc run cannot accept a bundle.

For each claimed closure, name the baseline fixture and failed gate or rubric item.
Keep the baseline evidence and link to the candidate evidence that closes the failure.
Show that the candidate introduces no gate or rubric regression.
Compare each rubric item as well as the case total.
A gain on one item cannot offset a loss on another item.

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
- `evidence`: scientific material or author/editorial guidance supplied for the task;
- `protected_tokens`: literal or semantic items that must survive revision;
- `forbidden_actions`: fixture-specific authority boundaries;
- `hard_gates`: binary failure conditions;
- `expected_behavior`: behavioral outcomes, not a golden answer;
- `rubric`: twelve independent one-point checks.

Only `scope` and `evidence` from this list enter the runner projection. All
identity, routing, protection, gate, expectation, and rubric fields remain
harness-only.

Supplied editorial guidance makes a case an assisted test. It can test how a skill
uses that guidance, but cannot prove that the skill found the defect independently.
The workflow projection below also excludes future confirmations and evaluator-only
diagnoses that are stored under `evidence`.

Fixtures 21, 24–26, 28–29, 34, 38, 40 and 41 supply paragraph-role, defect or
decision-state guidance. Treat their corresponding checks as assisted.
Fixture 32 tests cold detection: omit `visible_structure` from its `evidence`
projection and keep that diagnostic field harness-only.

Fixture 12 replaces `prompt` with two non-empty `stage_prompts`, `review` and
`revise`, and still counts as one fixture run. Invoke Review in a fresh context
with the runner projection `{prompt: stage_prompts.review, scope, evidence}`.
Record its complete output. Then invoke Revise in a different fresh context
with `{prompt: stage_prompts.revise, scope, evidence}` and attach the complete
Stage 1 output verbatim as the authorized `stage_1_output` artifact. Do not
summarize, edit, annotate, or selectively quote that handoff. Evaluate the two
invocations and their combined access/action log once against fixture 12's hard
gates and twelve-point rubric.

This is the supported composition path. It does not add a third compose skill.
Keep evaluator-only fields out of both stages.

## Full discussion workflows (fixtures 20, 23, and 39)

Fixtures 20, 23, and 39 replace `prompt` with five `stage_prompts` and add
`initial_files` for harness setup. Each still counts as one fixture run. Fixture
20 tests decision persistence and evidence-safe revision.
Fixture 23 also tests stable coverage/finding IDs, pending authority, full-scope post-edit audit and closure states.
Fixture 39 tests versioned decision promotion, reciprocal supersession links, read-back and fresh-context consumption.

Run this separately for each frozen skill tree in a fresh temporary paper project.
The harness writes the two `initial_files` verbatim before invoking any skill.
Replace `{project}` in the current stage's prompt with that project's absolute
path. Treat `initial_files` as harness setup, not extra candidate-visible metadata.

Pass only the current stage prompt, `scope`, the permitted evidence fields below,
and the explicitly named files. Keep future prompts, especially the author reply,
hidden until their turn. Never pass the whole evidence object without this filter.

| Fixture | Evidence for `review` and `grill_open` | Evidence from `grill_confirm` through `rereview` |
| --- | --- | --- |
| 20 | `initial_facts`, `unavailable` | Same fields; new author input comes from the current stage prompt |
| 23 | `not_supported` | `not_supported`, `confirmed_after_grill` |
| 39 | `initial` | `initial`, `confirmed_after_grill`; keep the initial facts labeled as historical |

Keep fixture 23's `required_findings` harness-only at every stage. It gives expected
finding classifications, not scientific input. Reveal `confirmed_after_grill` only
with the author's reply. Do not insert its observations, results or permissions into
the initial files or earlier prompts.

1. **review:** Fresh Review invocation, manuscript and initial decision record read-only. Save its complete
   user-facing report verbatim as `review.md` through the harness, not Review.
2. **grill_open:** Fresh Grill invocation, with only the decision record writable.
   Capture its pending record and questions before continuing. It must not invent
   an answer. Absence of a question or premature confirmation is a failure.
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
procedure defines the model test that the runner executes. Validating fixture JSON
alone does not execute the workflow.

## Install closure

`bundle.json` is the installation contract. Its mappings contain exactly the
three paper skill directories and the unchanged provenance report. Validate a
staged or installed bundle with:

```bash
python3 scripts/validate_skills.py --install-root /absolute/path/to/codex-root
```

The install root is the directory that contains `skills/` and `research/`.
This mode byte-compares each declared source-to-install mapping.
It checks all installed relative Markdown links.
It also checks that canonical references and the provenance report are reachable from their declared skill entrypoints.

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
| `35-revise-interactive-finding-queue` | Revise applies direct repairs, asks the complete author-answerable frontier, and resumes instead of terminally blocking the queue |
| `36-boundary-distinct-question` | A parallel boundary map may pose a distinct question without inventing a negative prior-work gap or treating the question as novelty evidence |
| `37-interface-axis-revision` | Revise keeps interface semantics, protection/authority, customization control, and execution-path cost on their supported axes |
| `38-decision-history-pending-head` | Review accounts for every status while a pending successor leaves the prior confirmed head effective |
| `39-decision-lineage-promotion-workflow` | Grill promotes a complete successor with reciprocal links and fresh Revise consumes only the effective head |
| `40-decision-conflict-prose-receipt` | Revise preserves conflicted prose, applies independent repairs, and emits decision accounting even for prose-only output |
| `41-positioning-observation-review` | Review separates artifact evidence from manuscript abstraction, rejects conjunctive tuple gaps, and audits an Observation as an intellectual move |
| `42-positioning-observation-revision` | Revise distills artifact evidence, replaces an authorized tuple gap with a distinct question, and rebuilds an Observation around supplied causal content |
| `43-ste-clarity-preservation` | Revise resolves alias drift and hidden actors, splits an overloaded causal sentence without losing qualifiers, and preserves distinct concepts and adequate passive prose |
| `44-ste-terms-and-context` | Stable aliases, distinct concepts, context-sensitive meanings, and adequate domain terms |
| `45-ste-noun-clusters` | Noun-group relations, hidden actions, formal names, sizes, and alignment |
| `46-ste-condition-scope` | Conditions, quantifiers, negation, exceptions, and modifier attachment |
| `47-ste-action-order` | Ordered and simultaneous actions survive sentence separation |
| `48-ste-unknown-actor` | Unknown causes remain unknown; known actors become explicit without speculative causality |
| `49-ste-information-order` | Concepts precede dependent information; adequate long prose and original paragraph boundaries survive |

## STE-derived tests

Fixtures 43–49 adapt selected [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf) examples to original systems-paper passages.
The [source registry](ste-manuscript.json) pins the edition, source checksum, rules, and test purposes.
It records rule-derived risks, not observed model failures or official STE benchmark scores.
No official example passage or dictionary is redistributed.

These manuscript tests check clarity and preservation of scientific meaning.
They use no universal word quota, dictionary gate, or requirement to convert every passive sentence.
Each new case includes repair targets and adequate material that should survive.
Explicit unchanged-source controls check preservation of adequate text; they do not prescribe a golden replacement.
Author facts make the preservation checks assisted; they do not prove independent defect discovery without those facts.

The [separate authoring suite](ste-authoring/README.md) tests English skill instructions against supplied STE rules and dictionary entries.
Its six cases have a separate denominator and acceptance decision.
Do not route them through a paper skill or count them as six additional manuscript runs.
Passing them does not certify the whole skill bundle against the complete standard or dictionary.

Validate packaging and export candidate inputs with these commands:

```bash
python3 -B scripts/ste_benchmarks.py validate
python3 -B scripts/ste_benchmarks.py list --suite manuscript
python3 -B scripts/ste_benchmarks.py export --suite manuscript --case 48 --output /tmp/ste-candidate-input.json
```

The exporter includes only `prompt`, `scope`, and `evidence`.
It hides identity, source mapping, protection controls, hard gates, expected behavior, and rubrics.
It refuses to replace an existing output file.
Use the exported input with each frozen tree in the blind procedure above.
Supply the selected skill separately and keep its fixture identity from the candidate.
These commands do not call a model or score an output.

## Maintaining the benchmark

Add a fixture for a distinct observed failure or a documented rule-derived risk.
Identify which basis applies; a prospective case does not establish a model failure.
Keep synthetic inputs
small enough that scope and proposition preservation can be audited manually.
Update `bundle.json` whenever a canonical reference moves. When a behavioral
rule changes, revise the relevant criterion rather than adding a regex for the
new preferred wording.
