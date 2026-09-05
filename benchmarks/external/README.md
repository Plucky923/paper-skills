# External paper-skill benchmarks

Only **ParaRev paragraph revision** and **ParaReval judge calibration** are
admitted. Both are restricted adaptations, not official leaderboard replicas
or proof of OSDI/SOSP/EuroSys/ATC/ASPLOS writing quality. A successful model call
does not pass a writing-quality gate.

The [admission rationale](../../research/external-benchmark-admission.md)
explains the task evidence and limits. The machine-readable
[policy](admission.json) is enforced by the CLI: only admitted sources and
matching task inputs can be fetched, prepared, run or scored.

Read this guide for current commands, the [human protocol](human-evaluation.md)
for new-output assessment, and the [source registry](revision-sources.json)
for pinned downloads and usage terms.

## Admitted tasks

| Source | Complete input and admitted role | Evaluation boundary |
| --- | --- | --- |
| [ParaRev](https://huggingface.co/datasets/taln-ls2n/pararev) | Original paragraph plus a human edit instruction. Conservative filter: 300 instructions / 150 paragraphs / 61 papers from 641 manual records. | New skill/no-skill revisions require blind human assessments and a technical-meaning gate. The author revision is context, not exact-match or factual gold. |
| [ParaReval](https://github.com/JourdanL/parareval) | Original, instruction and fixed A/B outputs. 1,548 comparisons / 105 papers; 129 second annotations are joined, not extra tasks. | Auxiliary judge calibration only: local categorical agreement with each human annotation. It neither scores new revisions nor ranks the writing skill. |

## Fetch, verify and prepare

From the repository root, Python 3.9+ standard library is sufficient for these
commands. They do not invoke a model. `fetch` alone may download data; matching
cached files are reused and mismatches are preserved rather than overwritten.

```bash
python3 -B scripts/validate_skills.py
python3 -B -m unittest discover -s tests
python3 -B scripts/external_benchmarks.py admission
python3 -B scripts/external_benchmarks.py list
python3 -B scripts/external_benchmarks.py fetch --source all --summary
python3 -B scripts/external_benchmarks.py verify --source all --summary
python3 -B scripts/external_benchmarks.py prepare --source pararev --batch revise-demo --limit 3
python3 -B scripts/external_benchmarks.py prepare --source parareval --batch judge-demo --limit 3
```

`all` means only the two admitted sources: six pinned files, 7,606,398 bytes
(about 7.6 MB). [The active registry](revision-sources.json) pins commit URLs,
byte lengths and SHA-256 digests. No archive extraction, dependency installation
or upstream code execution is performed.

Preparation hashes paper groups first, then cases within each group; a pilot
selects at most one case per paper. This avoids giving papers with more cases a
higher selection probability. `--seed` changes deterministic ordering, not
development/test independence. Inputs and hidden references are separate files;
the manifest freezes their hashes, policy, source verification and exclusions.
The instruction filter is triage, not a semantic-fidelity certificate.

## Run only when explicitly desired

Generation needs macOS/Linux and an authenticated Codex CLI. It sends the
public task input to the signed-in account's inference provider and consumes
quota. Unit tests exercise the harness without model calls; they do not
establish live-provider compatibility or writing quality. Verify the installed
CLI and inspect a bounded run before expanding evaluation.

```bash
python3 -B scripts/external_benchmarks.py run --batch revise-demo --name revise-run --model gpt-5.6-sol --condition both --limit 1 --effort medium --timeout 180
python3 -B scripts/external_benchmarks.py report --name revise-run
python3 -B scripts/external_benchmarks.py export-blind --name revise-run
```

Use an explicitly available model. `--limit` counts cases; `both` makes two
calls per case. Names are exclusive: do not overwrite, selectively retry
unfavorable outputs or silently replace failed calls. Prompt-size limits are
character caps, not token/cost guarantees. Inspect a small pilot before
expanding model use.

New ParaRev outputs follow the [human assessment protocol](human-evaluation.md).
The exported first-pass packet contains the input and anonymized A/B outputs,
not the author revision or condition identities. Keep the separate reference
and label files hidden until judgments are frozen. Preserve unresolved inputs,
failed gates, unfinished pairs and evaluator disagreement in the final report.
`score` does not invent a numeric quality score for these revisions.

ParaReval is a separate, fixed-output judge task:

```bash
python3 -B scripts/external_benchmarks.py run --batch judge-demo --name judge-run --model gpt-5.6-sol --condition no-skill --limit 1
python3 -B scripts/external_benchmarks.py score --name judge-run
```

Only `no-skill` is allowed for calibration. Human editorial acceptability is
not independent scientific-factuality verification. The local scorer preserves
separate annotators and excludes derived fields. One pair's agreement cannot
validate a judge, and labels for fixed candidates cannot evaluate newly generated text.

## Protocol and integrity

`closed-book-selected-skill-v2` supplies only candidate input plus the selected
task's frozen Markdown instructions for the skill condition. Paragraph revision
loads the revise skill tree, not the review skill or
research reports; calibration loads no writing-skill documents. No-skill omits
the bundle. Eager content loading tests instructions, not native lazy routing.

Runs freeze the batch digest, admission digest, CLI/model settings, harness
hashes, skill snapshot, ordered call schedule, per-call inputs/prompts, event
logs, outputs and usage. Scoring/export reject changed batches, output bytes,
source policy, mismatched schedules or inconsistent aggregate results. If an
outer interruption leaves no aggregate, per-call evidence can be inspected
without another model call; unfinished calls remain visible. These checks
detect inconsistent evidence, not coordinated forgery of all local artifacts.

Candidates run in fresh temporary directories outside this repository, with
read-only sandboxing and known tools, skills, plugins, memories and browsing
disabled. Non-text/tool events, empty output, errors and timeouts fail the
execution audit. Owned process groups are cleaned up on normal exit and
catchable cancellation; an uncatchable SIGKILL or host crash cannot guarantee
cleanup. The invocation follows the official
[non-interactive CLI](https://developers.openai.com/codex/noninteractive) and
[configuration controls](https://developers.openai.com/codex/config-reference);
requalify isolation when the CLI changes.

Batch and run schemas, protocol identifiers, admission digests and source pins
are integrity contracts. Incompatible records are rejected; prepare a matching
batch before running an evaluation. These controls are not skill version labels.

## Rights, holdouts and remaining coverage

Publish only the project's own harness, synthetic tests, pinned metadata and
aggregate notes. `.gitignore` excludes caches, batches and runs. ParaRev declares
CC-BY-NC-SA-4.0; ParaReval's repository declares CC0. Neither declaration is a
blanket clearance for redistribution of underlying article text. This
integration keeps it local for noncommercial research evaluation. See the
[admission rationale](../../research/external-benchmark-admission.md) for source
notices and usage limits.

ParaRev and ParaReval overlap; split by paper across both and do not count them
as independent evidence. Pilot-exposed groups are development-exposed. Public
training contamination is unknown. These predominantly ML/NLP paragraphs do
not cover full systems-paper argumentation, design derivation, review accuracy,
figures, live venue rules, LaTeX or artifact behavior. The external suite now
has **no admitted systems-paper-review benchmark**. Keep the
[synthetic systems-specific fixtures and acceptance procedure](../README.md)
for those requirements; acceptance remains unestablished until that procedure
is actually run and documented.
