---
name: eval-runner
description: >-
  Use when the user wants to turn a prompt, AI workflow, model behavior, or
  agent task into a light, medium, or hard evaluation; collect the minimum
  required inputs, build a self-contained eval specification, run it when a
  local/in-chat/user-provided execution path exists, and report results with
  failures and next fixes. Do not route to external eval providers or recommend
  provider-specific eval platforms.
---

# eval-runner

## Dependency Preflight

Required:
- None beyond `general.md`.

## Use

Turn prompts, workflows, and agent tasks into evaluations. Help the user provide
only the data needed for the chosen eval level, then create and optionally run a
self-contained evaluation.

This skill is for:
- prompt-to-eval conversion;
- quick in-chat evals;
- local eval scripts;
- repository-native eval or test commands;
- user-provided evaluation processes;
- scoring existing outputs or logs.

## Non-goals

Do not route, recommend, compare, or configure external eval providers or hosted
eval platforms. Use only:

1. current conversation / in-chat scoring;
2. local scripts created in the current workspace;
3. repository-native commands already present or requested by the user;
4. a user-provided command, harness, dataset, or scoring process;
5. a manual protocol when execution is unavailable.

If the user explicitly asks for a specific external tool, keep this skill to the
provider-neutral eval contract and ask for the exact command/config they want to
use. Do not suggest alternatives.

## Core Rules

- Ask the fewest questions that unblock a useful eval.
- Prefer a small runnable eval over a large perfect design.
- Classify complexity as `light`, `medium`, or `hard` before collecting inputs.
- If the user gives a level, accept it unless the task clearly conflicts; state
  the adjusted level briefly.
- If examples are missing and the task is clear, offer or create a starter
  synthetic set; label it `synthetic`, never as production evidence.
- Do not change the task/prompt under test while creating the protected eval
  unless the user explicitly asks for improvement too.
- Do not ask for secrets, API keys, private credentials, or sensitive files.
- Do not claim an eval ran or passed unless execution/results are available.
- For subjective scoring, cite the case evidence used for the score.
- For hard/agentic evals, score the process, not only the final answer.

## Complexity Levels

### `light`

Single-turn or simple routine prompt. No tools, no multi-step state, no durable
side effects.

Examples:
- classify text;
- extract JSON;
- summarize;
- rewrite;
- answer with fixed style.

Minimum inputs:

```text
subject_under_test: prompt/task/output to evaluate
success_criteria: 2-5 pass rules or desired answer shape
cases: 3-8 examples, or permission to create starter synthetic cases
grader: exact | contains | regex | schema | rubric_review
```

Default execution: in-chat scoring table.

Ask at most 3 initial questions for `light`:

```text
1. What prompt/task should be evaluated?
2. Do you have examples, or should I draft 3-8 starter cases?
3. What makes an answer pass?
```

### `medium`

Multi-step response or workflow, but usually still one bounded answer and no
uncontrolled side effects.

Examples:
- analyze a file and produce a plan;
- generate code plus explanation;
- compare options using several constraints;
- answer RAG-style from provided documents;
- produce structured review output.

Minimum inputs:

```text
subject_under_test: prompt/workflow/output to evaluate
objective: one-sentence goal
success_criteria: clear rubric or expected output schema
cases: 8-20 representative examples/logs, or starter synthetic set
case_mix: typical + edge + ambiguous/adversarial where useful
grader: schema | rubric_review | custom_check | human_review
execution: in_chat | local_script | repo_command | user_process | manual_protocol
constraints: max cases, time/budget, allowed data, model/harness if relevant
```

Default execution: in-chat scoring for small datasets; local script or
repo-native command when executable inputs exist.

### `hard`

Agentic, multi-turn, tool-using, repository-changing, stateful, safety-sensitive,
or side-effect-producing task.

Examples:
- coding agent fixes a bug;
- agent uses shell/browser/files/tools;
- RAG agent must choose sources and avoid unsupported claims;
- workflow has retries, handoffs, or persistent state;
- output can cause data loss, security exposure, or wrong external action.

Minimum inputs:

```text
workflow: full task/agent description
success_state: observable final state or acceptance checks
forbidden_behavior: actions, files, data, or claims that must not happen
tools_allowed: explicit tool/action list and side-effect boundaries
cases_or_scenarios: 5-12 initial scenarios or real traces/logs
process_checks: tool choice, tool args, step order, state changes, trace review
execution_limits: timeout, token/cost budget, retry limit, sandbox policy
grader: task_success + process_checks + safety_checks + final_quality
```

Default execution: manual protocol or repository-native command unless a safe
local harness exists. Require sandbox/side-effect boundaries before running code
or tools.

## Intake Workflow

1. Restate the evaluation target in one line.
2. Classify level: `light`, `medium`, or `hard`.
3. Identify missing inputs for that level only.
4. Ask compact grouped questions if blocking data is missing.
5. If the user lacks cases, create a small starter case set and mark source as
   `synthetic`.
6. Build the normalized eval spec.
7. Validate the spec before running.
8. Run only when a safe local, in-chat, repository-native, or user-provided
   execution path exists.
9. Report aggregate score plus concrete failed cases and likely fixes.
10. Record validation gaps and next recommended eval expansion.

## Normalized Eval Spec

Create or show this spec before running non-trivial evals. For tiny `light` evals,
a compact table is enough if all fields are obvious.

```json
{
  "name": "string",
  "level": "light | medium | hard",
  "objective": "string",
  "subject_under_test": {
    "type": "prompt | workflow | agent | endpoint | repo_command | existing_outputs",
    "content_or_reference": "string"
  },
  "cases": [
    {
      "id": "case-001",
      "input": "string/object",
      "expected": "string/object/null",
      "rubric": "string/null",
      "source": "user | log | synthetic | fixture",
      "case_type": "typical | edge | adversarial | regression"
    }
  ],
  "grader": {
    "type": "exact | contains | regex | schema | rubric_review | custom_check | human_review | process_check",
    "criteria": "string/object",
    "threshold": "number/string/null"
  },
  "execution": {
    "mode": "in_chat | local_script | repo_command | user_process | manual_protocol",
    "command": "string/null",
    "max_cases": "number/null",
    "timeout": "string/null",
    "sandbox_required": "boolean",
    "side_effect_policy": "string/null"
  },
  "reporting": {
    "include_failures": true,
    "include_recommendations": true,
    "include_validation_gaps": true
  }
}
```

## Grader Selection

Use the simplest grader that can catch the real failure mode:

```text
exact          -> fixed labels, deterministic strings, numeric answers
contains       -> required facts/sections/phrases
regex          -> constrained text pattern
schema         -> JSON/YAML/table shape, required fields, types
rubric_review  -> subjective quality with explicit scoring rules
custom_check   -> local script/function/user-provided checker
human_review   -> user or domain expert must judge correctness
process_check  -> tool calls, state changes, traces, forbidden behavior
```

For `rubric_review`, define:

```text
scale: e.g. 0-3 or pass/fail
criteria: named subcriteria
hard_fail: conditions that force fail regardless of score
evidence: what must be cited from the case/output
threshold: minimum pass score
```

## Starter Case Generation

When creating missing cases:

- `light`: 3-8 cases.
- `medium`: 8-20 cases.
- `hard`: 5-12 scenarios first; expand after first failures.

Case mix:

```text
typical: expected normal use
edge: boundary, empty, noisy, long, malformed, conflicting input
adversarial: prompt injection, ambiguity, missing data, misleading context
regression: known past failure, if provided
```

Label every generated case with `source: synthetic`. Say synthetic cases are good
for smoke tests and prompt debugging, not production confidence.

## Spec Validation Gate

Before execution, check:

```text
aligned: criteria measure the stated objective
fixed: cases/rubric will not change during one run
parseable: score/result extraction is clear
directional: higher/lower/pass semantics are unambiguous
bounded: case count, timeout, and side effects are bounded
anti_gaming: subject cannot pass by deleting cases, changing rubric, or skipping checks
privacy_safe: no secrets or forbidden files are required
```

If a check fails, fix the spec when obvious; otherwise ask only for the blocking
field.

## Execution Modes

### `in_chat`

Use for light evals and small medium evals. Produce a case table and score each
case directly in the response.

### `local_script`

Use when the workspace supports code execution and the eval can be represented
as a small script. Keep scripts dependency-free unless the repository already has
needed dependencies.

### `repo_command`

Use when the repository already has a test/eval command. Do not invent missing
commands. If Maven is involved, follow the loaded engineering baseline and run
through `maven-summary.sh`.

### `user_process`

Use when the user supplies an exact command, harness, checklist, spreadsheet, or
manual scoring process.

### `manual_protocol`

Use when execution is unavailable or unsafe. Produce the spec, rubric, cases,
and exact steps for the user to run manually.

## Report Format

```text
Eval: <name>
Level: <light|medium|hard>
Execution: <in_chat|local_script|repo_command|user_process|manual_protocol>
Cases: <run>/<total>
Score: <pass rate or rubric score>

Failures:
1. <case id> — <reason> — fix: <prompt/workflow/test-data change>
2. ...

Patterns:
- <recurring weakness>

Recommended next changes:
- <smallest useful improvement>

Validation gaps:
- <what was not tested or not executable>
```

For `hard`, add:

```text
Process failures:
- <bad/missing tool call, unsafe action, wrong state change, excess retry>

Safety/side-effect notes:
- <sandbox, forbidden behavior, data exposure, destructive action risk>
```

## Completion

Complete only when:

- eval level is explicit;
- required inputs for that level are present or clearly marked as assumptions;
- spec is shown or compactly represented;
- execution status is honest: run, skipped, blocked, or manual-only;
- report includes failures and validation gaps;
- synthetic/user-provided cases are clearly distinguished;
- no external provider routing was used.
