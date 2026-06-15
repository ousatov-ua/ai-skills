---
name: autoresearcher
description: >-
  Use this skill only if specified directly
---

# autoresearcher

This is a task-generic version of `program.md`: an experiment to have the LLM do its own research for a user-specified goal. It runs an autonomous loop where Codex changes only approved files, runs a fixed evaluation, compares each result to the best kept result, records the result, keeps improvements, and discards regressions.

The user must specify:

- **Goal**: what to improve.
- **Evaluation logic**: how to measure the goal target.
- **Comparison rule**: how to decide if an iteration improved the target.
- **Maximum iterations**: hard cap for the loop.

If any of these are missing, ask the user for them before setup. Do not begin an autoresearch loop without all four.

**Monorepo note:** The target project may live inside a larger repo. Always stage only explicitly in-scope paths. Never use blind `git add -A`.

## Setup

To set up a new autoresearch run, work with the user to:

1. **Agree on a run tag**: propose a tag based on today's date or the goal name (for example `jun15`, `coverage-jun15`, or `skill-jun15`). The branch `autoresearch/<tag>` must not already exist - this is a fresh run.
2. **Create the branch**: `git checkout -b autoresearch/<tag>` from the current stable base branch or current checked-out commit, unless the user gives a different base. If `autoresearch/<tag>` cannot be created because of a Git ref namespace conflict, use a clear equivalent branch such as `autoresearch-<tag>`.
3. **Read the in-scope files**: Read all files needed for full context:
   - repository or task documentation;
   - evaluation harness, benchmark, rubric, prompt set, coverage config, or test command;
   - files the user allows Codex to modify;
   - files the user marks read-only or protected.
4. **Verify required resources exist**: Check that all data, fixtures, dependencies, benchmark inputs, eval prompts, scripts, services, credentials, and tools required by the evaluation are available. If something is missing, tell the human the exact command or action needed to prepare it.
5. **Initialize `results.tsv`**: Create `results.tsv` with a header row and baseline entry. Run the evaluation once before editing to establish YOUR baseline in this environment. Do NOT use baseline numbers from other machines, branches, datasets, prompt sets, or stale reports.
6. **Confirm and go**: Confirm setup looks good, including goal, editable scope, protected scope, evaluation command or rubric, comparison rule, timeout, and max iterations.

Once the user confirms, kick off the experimentation.

## Run Specification

Before the first baseline run, write down the run specification in the conversation or in a task-local `program.md` when the run is complex.

Required fields:

```text
goal: <user-specified goal>
target_metric: <primary metric or score>
comparison_rule: <lower is better | higher is better | pass/fail | rubric rule>
evaluation_command: <command to run, or rubric/scoring process>
result_extraction: <grep command, report parser, score sheet, or manual rubric>
max_iterations: <positive integer>
per_iteration_timeout: <duration>
can_modify: <paths/artifacts Codex may edit>
cannot_modify: <paths/artifacts Codex must not edit>
constraints: <tests, memory, runtime, quality, compatibility, or policy limits>
```

Examples:

```text
goal: reduce parser latency
target_metric: p95_ms
comparison_rule: lower is better, tests must pass
evaluation_command: uv run pytest && uv run python bench_parser.py
result_extraction: grep "^p95_ms:" run.log
max_iterations: 12
```

```text
goal: improve test coverage
target_metric: branch_coverage_percent
comparison_rule: higher is better, tests must pass, tests must assert meaningful behavior
evaluation_command: mvn test jacoco:report
result_extraction: read branch coverage from target/site/jacoco/index.html or generated CSV
max_iterations: 8
```

```text
goal: improve skill reliability
target_metric: eval_score
comparison_rule: higher is better; tie goes to shorter clearer skill
evaluation_command: validate skill frontmatter and score fixed benchmark prompts
result_extraction: total rubric score across prompts
max_iterations: 10
```

## Experimentation

Each experiment runs through the user-specified evaluation logic with a fixed per-iteration budget. Launch it exactly as specified by the run specification. Redirect noisy output to `run.log` or an equivalent log file so context is not flooded.

**What you CAN do:**

- Modify only files listed in `can_modify`.
- Change implementation, architecture, tests, prompts, skill text, configuration, hyperparameters, scripts, or documentation only when they are in scope.
- Add focused helper files only if the user or run specification allows new files.

**What you CANNOT do:**

- Modify files listed in `cannot_modify`.
- Modify the evaluation harness, scoring rubric, benchmark inputs, test fixtures, prompt set, or target metric unless the run goal is explicitly to improve the evaluation itself.
- Install new packages or add dependencies unless the run specification allows it.
- Skip required checks or weaken constraints to make the metric look better.
- Compare results from different environments, branches, datasets, prompts, or evaluation logic unless the run specification explicitly allows that.

**The goal is simple: improve the user-specified target.** If the comparison rule says lower is better, keep lower scores. If higher is better, keep higher scores. If pass/fail, keep only changes that pass and improve the defined tie-breakers. The only universal constraints are that the code or artifact must not crash, must finish within the per-iteration timeout, and must satisfy all run constraints.

**Resource constraints** are soft or hard according to the run specification. Some extra memory, runtime, complexity, or artifact size may be acceptable for meaningful target gains if the run allows it, but it should not blow up dramatically.

**Simplicity criterion**: All else being equal, simpler is better. A small improvement that adds ugly complexity is not worth it unless the run explicitly values raw score above maintainability. Conversely, removing something and getting equal or better results is a great outcome. When evaluating whether to keep a change, weigh complexity cost against improvement magnitude. A tiny metric improvement that adds hacky code is suspect. A tiny metric improvement from deleting code is worth keeping. An improvement of approximately zero with much simpler code may be kept if the comparison rule allows tie-breakers.

**The first run**: Your very first run should always establish the baseline, so run the evaluation as-is before making changes.

## Output Format

The evaluation must produce or be reduced to a parseable summary. Prefer a summary like this:

```text
---
target_metric:       123.456
comparison_rule:     lower_is_better
status:              pass
total_seconds:       42.1
memory_mb:           512.0
secondary_metric:    optional
notes:               optional
```

For command-based evaluation, provide an extraction command in the run specification, for example:

```bash
grep "^target_metric:\|^status:\|^total_seconds:" run.log
```

For rubric-based evaluation, record the rubric score and enough evidence to justify it.

Compare only against your own baseline and kept results from the same run, same evaluation logic, and same environment.

## Logging Results

When an experiment is done, log it to `results.tsv` (tab-separated, NOT comma-separated - commas break in descriptions).

The TSV has a header row and 7 columns:

```text
iteration	commit	target_metric	secondary_metrics	status	description	comparison
```

1. iteration number, with baseline as `0`;
2. git commit hash, short 7 chars, or artifact/version id when git is unavailable;
3. target metric achieved, using the run's required precision; use an explicit sentinel such as `0.000000`, `NA`, or `FAIL` for crashes as defined by the run specification;
4. secondary metrics or constraints, such as `time=42.1s;memory=512MB;tests=pass`;
5. status: `keep`, `discard`, or `crash`;
6. short text description of what this experiment tried;
7. comparison against the previous best, such as `improved`, `worse`, `tie-simpler`, `invalid`, or `timeout`.

Example:

```text
iteration	commit	target_metric	secondary_metrics	status	description	comparison
0	383abb4	2.667000	time=405.7s;memory=26.9GB	keep	baseline	baseline
1	909dd59	2.588904	time=390.2s;memory=26.9GB	keep	halve total batch size	improved
2	4161af3	2.610000	time=389.0s;memory=25.1GB	discard	reduce model width	worse
```

## The Experiment Loop

The experiment runs on a dedicated branch, for example `autoresearch/<tag>` or `autoresearch-<tag>`.

LOOP UNTIL `max_iterations`:

1. Look at the git state: the current branch/commit we're on.
2. Tune the in-scope files with one experimental idea by directly hacking the code, skill, tests, prompt, config, documentation, or other approved artifact.
3. Stage only in-scope files and commit with `git commit -m "experiment: <description>"` (never `git add -A` - this may be inside a larger repo).
4. Run the experiment using the evaluation command from the run specification. Redirect noisy output, for example `<evaluation_command> > run.log 2>&1`. Do NOT use `tee` or let output flood your context unless the command is intentionally short.
5. Read out the result using the extraction command, generated reports, or rubric scoring specified by the run.
6. If the result is missing or invalid, the run crashed. Read the relevant failure output, such as `tail -n 50 run.log`, and attempt a fix only if the mistake is obvious and belongs to the same hypothesis. If you cannot get things to work after more than a few attempts, give up on that hypothesis.
7. Record the result in `results.tsv`.
8. If the target improved according to the comparison rule, stage `results.tsv` and amend the experiment commit with `git commit --amend --no-edit` to include the log entry, advancing the branch.
9. If the target is equal or worse and the tie-breaker does not justify keeping it, record the discard result, then return to the previous kept state. Use `git reset --hard <previous kept commit>` only when it will not destroy user changes and the run explicitly allows clean reverts.
10. Stop when the iteration count reaches `max_iterations`, the target threshold is reached, verification becomes blocked, or the user interrupts.

The idea is that you are a completely autonomous researcher trying things out. If they work, keep. If they do not, discard. You advance the branch only through kept experiments. If you feel stuck, rewind sparingly if ever, re-read the in-scope files, inspect previous near-misses, combine ideas, or try a more radical but still in-scope change.

**Timeout**: Each experiment must finish within `per_iteration_timeout`. If a run exceeds that timeout, kill it if possible, treat it as a failure, log `crash` or `discard` according to the run specification, and revert or abandon the experiment.

**Crashes**: If a run crashes, use your judgment. If it is something dumb and easy to fix, such as a typo, missing import, invalid command flag, or malformed config, fix it and rerun within the same iteration. If the idea itself is fundamentally broken, skip it, log `crash` in the TSV, and move on.

**NEVER STOP EARLY**: Once the experiment loop has begun after setup confirmation, do NOT pause to ask the human if you should continue. Do NOT ask "should I keep going?" or "is this a good stopping point?". Continue autonomously until `max_iterations`, target threshold, blocker, timeout policy, or user interruption stops the run. If you run out of ideas, think harder: re-read the in-scope files, study the evaluation signal, inspect previous kept and discarded attempts, try combinations of near-misses, and test more radical in-scope changes.

As an example use case, a user might leave you running while they sleep. If `max_iterations` is 20 and each experiment takes 7 minutes, the loop should run up to 20 iterations unless stopped by the user, a target threshold, or a blocker.

## Comparison Logic

The comparison rule is the ground truth for keep/discard decisions.

Supported comparison patterns:

```text
lower is better: keep if new_metric < best_metric
higher is better: keep if new_metric > best_metric
pass/fail: keep if required checks pass and tie-breakers improve
rubric score: keep if new_score > best_score
multi-metric: keep if primary metric improves and all constraints pass
tie-breaker: keep equal primary metric only if the run explicitly allows simpler/faster/safer tie wins
```

Invalid improvements do not count. Mark an experiment `discard` or `crash` if it improves the target by:

- changing protected evaluation logic;
- reducing benchmark difficulty;
- deleting or weakening tests that are constraints;
- hardcoding benchmark answers;
- skipping required checks;
- violating scope;
- exceeding hard resource limits;
- relying on unavailable local-only state.

For noisy metrics, repeat near-tie experiments when practical or require a minimum improvement margin. Record the rule in the run specification before using it.

## Final Handoff

When the loop stops, report:

- goal;
- branch and best kept commit;
- baseline result;
- best result;
- max iterations and iterations actually run;
- kept, discarded, and crashed counts;
- files changed;
- verification command or rubric used;
- unresolved risks, blockers, or metric noise.

Do not claim success beyond what the evaluation proves.
