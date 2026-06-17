---
name: sonar-reviewer
description: >-
  Use for Sonar cleanup, SonarQube/SonarLint-oriented review, static-analysis
  validation, and checking changed or added code and tests for common Sonar
  issues before finalizing implementation work. Trigger whenever the user
  pastes Sonar findings or rule ids (e.g. java:S1186), mentions a failing
  quality gate, asks to clean up static-analysis issues, or when another
  skill (code-reviewer, pragmatic-software-engineer) delegates static-analysis
  validation of changed code.
---

# Sonar Reviewer

## Resources

**If a required resource cannot be fetched, ask the user to paste it; do not continue without it.**

**If a resource is already fetched, skip re-fetching.**

### Requires

- `general.md` from `__ROOT__/general.md`
- `engineering.md` from `__ROOT__/shared/engineering.md`

### On Demand

- None.

## Use

Review changed or added code/tests for likely SonarQube, SonarLint, or
equivalent static-analysis issues and resolve practical findings before
implementation work is complete.

Instruction precedence, validation evidence, patch hygiene, Maven verification,
and change-scope rules come from `engineering.md`; this skill adds
static-analysis cleanup rules and suppression policy below.

## Scope

- Focus on changed or added files unless the user asks for a broader scan.
- This skill owns static-analysis validation only. When invoked alongside or
  from `code-reviewer` or `pragmatic-software-engineer`, do not repeat their
  overall review or implementation work: assess readability, reliability,
  maintainability, and test quality only as surfaced through static-analysis
  rules.
- Fix clear issues when code edits are in scope; if the user asks only for
  review, report actionable findings instead.
- No subjective style churn.

## Cleanup Rules

Check especially:
- Empty methods, constructors, lambdas, and overrides: implement them, throw
  `UnsupportedOperationException`, or add a short nested comment explaining
  intentional emptiness.
- `assertThrows` and exception-testing lambdas: keep only the single
  invocation expected to throw inside the lambda; move setup outside.
- Resources: prefer try-with-resources for `Closeable`/`AutoCloseable`;
  avoid manual `close()` when try-with-resources fits.
- Tests: avoid reflection-based setup when direct constructors/helpers work;
  prefer explicit fixtures over hidden mutable state.
- Comments: short and specific; add only where needed for clarity or Sonar
  rules.
- JUnit waits: never `sleep()`; use Awaitility when available.

## Suppression Policy

Fix rather than suppress when the rule exposes real complexity, risk, dead
code, unclear tests, resource leaks, or avoidable debt.

Suppress only when the issue is intentional, the direct fix is worse, or the
rule conflicts with constraints. Use the smallest scope and the exact rule
id — e.g. `@SuppressWarnings("java:S127")` or
`# NOSONAR python:S3776 - reason` — and add a short reason when syntax
allows. Never use broad or rule-less suppressions when a specific id is
known.

## Process

1. Identify changed or added files and understand the change purpose.
2. Apply the Cleanup Rules; treat search hits as leads, not automatic
   findings.
3. Fix clear issues, or report them when review-only.
4. Apply the Suppression Policy to intentional or better-left-as-is issues.
5. Before final response: run relevant formatting/tests per `engineering.md`,
   then search changed/added files for obvious Sonar-prone patterns such as
   `{}`, setup inside `assertThrows`, manual close patterns, and reflection in
   tests.
6. Report fixed issues, suppressions, remaining concerns, skipped
   verification, and unresolved Sonar issues with reasons.

## Output

- Sonar review summary: overall assessment, files reviewed, verification
  performed, remaining risk.
- Findings: severity, problem, evidence, recommended fix.
- Final verdict: Clean, Clean after fixes, Issues found, or Verification
  incomplete.

If no issues are found, say so clearly.

## Completion

A Sonar pass is complete only when every applicable Process step has been
performed and unresolved issues or skipped verification are explicitly
mentioned.
