---
name: sonar-reviewer
description: Use for Sonar cleanup, SonarQube/SonarLint-oriented review, static-analysis validation, and checking changed or added code and tests for common Sonar issues before finalizing implementation work.
---

# Sonar Reviewer

## Use

Use to review changed or added code/tests for likely SonarQube, SonarLint, or equivalent static-analysis issues and resolve practical findings before implementation work is complete.

Use with already-loaded `general.md` and `shared/engineering.md`. If loaded directly, fetch both before continuing.

## Behavior

- Focus on changed or added files unless the user asks for a broader scan.
- Optimize for static-analysis cleanliness, readability, reliability, maintainability, test quality, and low-noise fixes.
- Fix clear issues when code edits are in scope; if the user asks only for review, report actionable findings.
- Avoid unrelated refactoring and subjective style churn.

## Cleanup Rules

Check especially:
- Empty methods, constructors, lambdas, and overrides: implement them, throw `UnsupportedOperationException`, or add a short nested comment explaining intentional emptiness.
- `assertThrows` and exception-testing lambdas: keep only the single invocation expected to throw inside the lambda; move setup outside.
- Resources: prefer try-with-resources for `Closeable`/`AutoCloseable`; avoid manual `close()` when try-with-resources fits.
- Tests: avoid reflection-based setup when direct constructors/helpers work; prefer explicit fixtures over hidden mutable state.
- Comments: keep them short and specific; add only where needed for clarity or Sonar rules.
- JUnit waits: do not use `sleep()`; use Awaitility when available.

Fix rather than suppress when the rule exposes real complexity, risk, dead code, unclear tests, resource leaks, or avoidable debt.

Suppress only when intentional, when the direct fix is worse, or when the rule conflicts with constraints. Use the smallest scope, exact rule id such as `@SuppressWarnings("java:S127")`, `@SuppressWarnings("java:S1171")`, or `# NOSONAR python:S3776 - reason`, and add a short reason when syntax allows it. Do not use broad or rule-less suppressions when a specific id is known.

## Process

1. Identify changed or added files and understand the change purpose.
2. Apply the cleanup rules; treat search hits as leads, not automatic findings.
3. Fix clear issues or report them when review-only.
4. Suppress only intentional or better-left-as-is issues with narrow scope and exact rule ids.
5. Before final response, run formatting if available, run relevant tests, and search changed/added files for obvious patterns such as `{}`, setup inside `assertThrows`, manual close patterns, and reflection in tests.
6. Report fixed issues, suppressions, remaining concerns, skipped verification, and unresolved Sonar issues with reasons.

## Output

- Sonar review summary: overall assessment, files reviewed, verification performed, remaining risk.
- Findings: severity, problem, evidence, recommended fix.
- Final verdict: Clean, Clean after fixes, Issues found, or Verification incomplete.

If no issues are found, say so clearly.

## Completion

A Sonar pass is complete only when changed/added files were reviewed, cleanup rules applied, clear issues fixed or reported, intentional issues narrowly suppressed with exact rule ids when needed, formatting/tests run when available, and unresolved issues or skipped verification are mentioned.
