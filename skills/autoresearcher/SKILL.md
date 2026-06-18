---
name: autoresearcher
description: >-
  Use this skill only when the user explicitly asks for autoresearch/autoresearcher or an autonomous improvement loop. Supports any task, investigation, optimization, benchmark, evaluation, skill/document/code improvement, or research workflow where Codex should define a fixed evaluation, iterate independently, keep improvements, discard regressions, and produce durable run artifacts.
---

# autoresearcher

Run a universal autonomous research loop:

1. Define the goal, input data, metric contract, scope, constraints, outputs, and stop conditions.
2. Establish a same-environment baseline before editing.
3. Iterate with one hypothesis per iteration.
4. Run the fixed evaluation.
5. Keep only valid improvements according to the predeclared comparison rule.
6. Discard or abandon regressions and invalid runs.
7. Record every result and hand off the best artifact with evidence.

Do not start any experiment loop until every required field is set and the quality metric check has been validated.

## Hard Gate

Before baseline or looping, require a complete run specification. If anything below is missing, ambiguous, unavailable, or internally inconsistent, ask for the missing information or create the missing artifact when it is in scope. Do not begin the loop.

Required run specification:

```text
run_tag: <short unique tag for branch/artifact names>
goal: <what to improve or investigate>
task_type: <code | docs | prompt | benchmark | investigation | design | data | other>
input_data: <files, datasets, prompts, logs, requirements, user facts, services, URLs, or examples used as inputs>
output_artifacts: <files/reports/patches/models/tables/docs/results expected from the run>
can_modify: <paths/artifacts Codex may edit or create>
cannot_modify: <paths/artifacts Codex must not edit>
protected_evaluation: <benchmark, rubric, tests, fixtures, prompts, data, parser, judge, or manual check that must stay fixed>
target_metric: <primary metric or quality score>
metric_direction: <lower_is_better | higher_is_better | pass_fail | rubric | multi_metric>
comparison_rule: <exact keep/discard rule, including constraints and tie-breakers>
evaluation_command_or_process: <command, script, rubric procedure, review process, or manual measurement>
result_extraction: <how to parse or record metric/status from the evaluation>
metric_validity_check: <how to prove the metric measures the goal and cannot be trivially gamed>
baseline_required: <yes unless the user explicitly defines a valid reason it is impossible>
max_iterations: <positive integer hard cap, or explicit user-approved unbounded run policy>
per_iteration_timeout: <duration or bounded review budget>
stop_conditions: <target threshold, max iterations, blocker, budget, user interruption, or definition of done>
constraints: <runtime, memory, cost, style, compatibility, policy, dependency, or quality limits>
artifact_location: <where to write run spec, results.tsv, logs, reports, and generated artifacts>
```

Use a task-local `program.md` when the run is complex or long-lived. `program.md` is the standalone run contract for this skill, not an external template. For small runs, the conversation can hold the spec, but durable artifacts are still required once the loop begins.

## Input Data

Treat input data as immutable unless the run explicitly says the goal is to improve the input set itself.

Input data can be:

- repository files, docs, specs, tests, scripts, prompts, examples, benchmark cases, logs, datasets, URLs, screenshots, design references, business constraints, or human-provided facts;
- current environment details that affect evaluation, such as branch, commit, hardware, model, dependency lockfile, service endpoint, or date;
- evaluation inputs such as test fixtures, gold answers, scoring rubrics, judge prompts, validation datasets, or acceptance criteria.

Before looping:

1. Read enough in-scope input data to understand the task.
2. Verify every required file, dataset, fixture, service, dependency, credential, and tool exists.
3. Identify which inputs are protected and which are editable.
4. Record the input versions when reproducibility matters.
5. Stop if the evaluation depends on missing, stale, private, or changing data and no valid fallback is defined.

## Quality Metric Check

Validate the metric before trusting it. A metric is valid only if all checks pass:

```text
aligned: it measures the stated goal or a justified proxy for it
parseable: result_extraction reliably returns the target metric and status
directional: lower/higher/pass/rubric semantics are unambiguous
fixed: the benchmark, rubric, fixtures, prompts, and judge stay unchanged across iterations
bounded: timeout, cost, resource limits, and failure sentinels are defined
anti_gaming: improvements cannot come from weakening tests, deleting hard cases, hardcoding answers, skipping checks, or changing protected inputs
noise_handled: noisy metrics define repeats, confidence threshold, minimum delta, or tie policy
constraints_checked: required tests, style, compatibility, safety, and policy constraints are evaluated
baseline_parseable: the baseline can be run and parsed in this environment
```

If the user provides a quality metric check, audit it against this list. If it fails, fix the evaluation contract when that is in scope; otherwise ask the user. Do not start the loop with an invalid metric.

For rubric or qualitative work, define the score scale, subcriteria, evidence required, pass/fail constraints, and tie-breakers before scoring. Do not use "looks better" as the sole metric.

For investigations where the output is knowledge rather than an optimized artifact, use evidence quality metrics such as source authority, recency, contradiction resolution, coverage of hypotheses, reproducibility of commands, or confidence calibration.

## Output Data

Create all artifacts needed to make the run auditable and reusable. At minimum:

- `program.md`: standalone run specification, metric contract, scope, execution plan, and stop conditions for non-trivial runs.
- `results.tsv`: append-only experiment table with baseline and every iteration.
- `run.log` or per-iteration logs: raw evaluation output, kept concise in context.
- changed artifacts: code, docs, prompts, configs, data transforms, reports, or other in-scope outputs.
- final handoff: summary of baseline, best result, artifacts, validation, and risks.

Use TSV for experiment results. Include enough columns for the task:

```text
iteration	artifact_id	target_metric	secondary_metrics	status	description	comparison	evidence
```

Column definitions:

1. `iteration`: `0` for baseline, then increasing integers.
2. `artifact_id`: git commit hash, file version, report path, model/checkpoint id, or other stable identifier.
3. `target_metric`: primary score, pass/fail value, or explicit failure sentinel.
4. `secondary_metrics`: constraints such as time, memory, cost, tests, rubric subscores, or coverage.
5. `status`: `keep`, `discard`, `crash`, `invalid`, or `blocked`.
6. `description`: one short sentence describing the hypothesis.
7. `comparison`: `baseline`, `improved`, `worse`, `tie-kept`, `tie-discarded`, `invalid`, `timeout`, or `blocked`.
8. `evidence`: log path, report path, command, score sheet, source list, or reviewer note.

Do not leave required artifacts implied. If an artifact is required by the run specification, create or update it before final handoff.

## `program.md`

When the run is non-trivial, long-lived, or expected to continue autonomously, create `program.md` before baseline and execute it after setup approval.

`program.md` must contain:

- the complete required run specification;
- input data and protected evaluation definitions;
- output artifact definitions and artifact locations;
- quality metric check and validation result;
- baseline command or scoring process;
- exact iteration procedure;
- keep/discard comparison rule;
- timeout, crash, noisy metric, and blocker policy;
- definition of done and final handoff requirements.

After writing `program.md`:

1. Re-read it and verify every hard-gate field is present.
2. Fix missing or inconsistent fields before baseline.
3. Run the baseline exactly as specified.
4. Execute the iteration loop from `program.md`.
5. Update `results.tsv`, logs, and required artifacts as execution proceeds.

Do not treat `program.md` as documentation only. It is the executable operating plan for the run.

## Setup

Set up a fresh autoresearch run:

1. Choose a unique `run_tag`, usually based on date and goal.
2. Create or switch to a dedicated branch such as `autoresearch/<run_tag>` when the work is in git. If a slash branch conflicts, use `autoresearch-<run_tag>`.
3. Read the in-scope files and protected evaluation assets.
4. Verify required resources and inputs exist.
5. Create or update `program.md` when the run is non-trivial, long-lived, or expected to continue autonomously.
6. Re-read `program.md` and verify it contains all hard-gate fields.
7. Validate the quality metric check.
8. Run the baseline without edits, parse the output, and record iteration `0` in `results.tsv`.
9. Confirm the complete setup with the user before starting the autonomous loop unless the user already explicitly authorized running after setup.
10. Execute `program.md` by following its baseline, iteration, comparison, logging, and done instructions until a stop condition is reached.

Monorepo rule: stage only explicitly in-scope paths. Never use blind `git add -A`.

## Iteration Definition

One iteration is exactly one hypothesis tested against the fixed evaluation.

An iteration includes:

1. Start from the current best kept state.
2. Select one clear hypothesis or intervention.
3. Modify only in-scope artifacts.
4. Save a stable artifact id, usually a git commit.
5. Run the fixed evaluation within the timeout.
6. Extract target metric, status, secondary metrics, and evidence.
7. Validate that the result did not violate the metric contract.
8. Append the result to `results.tsv`.
9. Keep, discard, or mark blocked according to the comparison rule.

Do not count typo fixes or reruns for the same broken hypothesis as separate iterations unless the run specification says to. Keep them inside the same iteration budget.

## Experiment Loop

After the hard gate passes and the user has authorized the run, loop until `max_iterations`, target threshold, blocker, timeout policy, definition of done, or user interruption:

1. Inspect the current branch, best artifact, previous results, and working tree.
2. Generate the next hypothesis from observed evidence, near misses, baseline weaknesses, or domain knowledge.
3. Edit only allowed files or artifacts.
4. Commit or otherwise identify the candidate artifact.
5. Run `evaluation_command_or_process`, redirecting noisy output to logs.
6. Extract the result with `result_extraction`.
7. If the result is missing, invalid, crashed, or timed out, inspect concise failure output and fix only obvious implementation mistakes inside the same hypothesis. Otherwise log `crash` or `invalid`.
8. Compare against the best kept result using only the predeclared comparison rule.
9. Keep valid improvements; discard regressions; handle ties only if a tie-breaker was predeclared.
10. Continue without asking whether to keep going.

Keep advancing the branch or best artifact only through kept experiments. For discarded experiments, return to the previous best state using non-destructive methods when possible. Use destructive reverts only when the run explicitly allows it and they will not destroy unrelated user changes.

## Keep/Discard Logic

The comparison rule is the ground truth.

Common patterns:

```text
lower_is_better: keep if new_metric < best_metric and constraints pass
higher_is_better: keep if new_metric > best_metric and constraints pass
pass_fail: keep if pass status improves or tie-breakers improve
rubric: keep if score improves and evidence supports the score
multi_metric: keep if primary metric improves and all hard constraints pass
tie: keep equal primary metric only for predeclared improvements such as simpler, faster, safer, cheaper, or clearer
```

Invalid improvements do not count. Mark `discard` or `invalid` if the apparent improvement comes from:

- changing protected evaluation logic or input data;
- weakening tests, rubrics, fixtures, prompts, acceptance criteria, or constraints;
- reducing benchmark difficulty without authorization;
- hardcoding benchmark answers or overfitting known examples;
- skipping required checks;
- violating editable scope;
- exceeding hard resource, cost, compatibility, or policy limits;
- relying on local-only or non-reproducible state not declared in the spec.

For noisy metrics, require the predeclared repeat policy, minimum delta, confidence rule, or tie-breaker before keeping near-ties.

## Universal Examples

Code performance:

```text
goal: reduce parser p95 latency
target_metric: p95_ms
metric_direction: lower_is_better
comparison_rule: keep if p95_ms improves by >=2% and tests pass
evaluation_command_or_process: run unit tests, then benchmark parser
result_extraction: parse p95_ms from benchmark report
```

Skill improvement:

```text
goal: improve skill reliability across benchmark prompts
target_metric: rubric_total
metric_direction: higher_is_better
comparison_rule: keep if total score improves and SKILL.md stays concise
evaluation_command_or_process: validate frontmatter, run fixed prompt suite, score with rubric
result_extraction: total rubric score plus per-prompt notes
```

Investigation:

```text
goal: identify the root cause of flaky CI failures
target_metric: evidence_score
metric_direction: rubric
comparison_rule: keep if hypothesis explains more failures with cited logs and no contradictions
evaluation_command_or_process: inspect fixed CI logs, reproduce when possible, score evidence coverage
result_extraction: rubric score and cited evidence list
```

Documentation:

```text
goal: improve onboarding doc task success
target_metric: task_completion_score
metric_direction: higher_is_better
comparison_rule: keep if fixed checklist passes with fewer ambiguities and no factual regressions
evaluation_command_or_process: run doc lint plus rubric over required user tasks
result_extraction: checklist pass count and ambiguity count
```

## Definition of Done

The run is done only when one stop condition is reached and all required artifacts are current:

- `max_iterations` reached;
- target threshold or success criterion reached;
- evaluation is blocked by a missing external resource, repeated infrastructure failure, or invalid metric that cannot be fixed in scope;
- budget, timeout, or user interruption stops the run;
- no valid in-scope hypothesis remains after re-reading inputs, results, and near misses.

Final handoff must include:

- goal and run tag;
- branch and best artifact id;
- baseline result and best result;
- iterations run, kept/discarded/crashed/invalid counts;
- final changed artifacts and output artifacts;
- evaluation command or rubric used;
- metric validity notes and any noise policy used;
- definition-of-done reason;
- unresolved risks, blockers, and what the metric does not prove.

Do not claim success beyond what the evaluation proves.
