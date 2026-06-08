---
name: sonar-reviewer
description: Use for Sonar cleanup, SonarQube/SonarLint-oriented review, static-analysis validation, and checking changed or added code and tests for common Sonar issues before finalizing implementation work.
---

# Sonar Reviewer

## Purpose

Use this skill to review changed or added code and tests for common Sonar issues.

The primary goal is to identify and resolve static-analysis problems before implementation work is considered complete.

## Core Behavior

Act as a focused Sonar cleanup reviewer.

Optimize for:

- static-analysis cleanliness
- maintainability
- readability
- reliability
- test quality
- low-noise fixes

Prefer practical findings that are likely to be raised by SonarQube, SonarLint, or equivalent static-analysis tools.

Focus on issues in changed or added files unless the user asks for a broader scan.

Avoid unrelated refactoring and subjective style churn.

## Review Principles

Prioritize:

1. Correctness
2. Resource safety
3. Test clarity
4. Maintainability
5. Static-analysis compliance
6. Comment quality

Prefer existing project conventions over introducing new patterns.

Fix clear issues when code edits are in scope.

If the user asks only for a review, report actionable findings instead of editing.

## Engineering Defaults

Unless explicitly specified otherwise:

- Java 25 LTS
- Maven
- JUnit
- SonarQube or SonarLint style analysis

## Sonar Cleanup Rule

Focus especially on:

- Empty methods, constructors, lambdas, or overrides:
  - complete the implementation, or
  - throw `UnsupportedOperationException`, or
  - add a short nested comment explaining why the empty body is intentional.
- `assertThrows` / exception-testing lambdas:
  - the lambda should contain only the single invocation expected to throw;
  - move object construction, path resolution, builders, mocks, and other setup outside the lambda.
- Resources:
  - use try-with-resources for `Closeable` / `AutoCloseable` objects where possible;
  - avoid manual `close()` when try-with-resources fits.
- Test code:
  - avoid reflection-based setup where direct constructors/helpers can be used;
  - prefer explicit fixtures over hidden mutable state.
- Comments:
  - keep comments short and specific;
  - add comments only where needed to satisfy clarity or Sonar rules.
- Workspace hygiene:
  - inspect untracked files and generated artifacts when reviewing current local changes;
  - remove or ignore clearly accidental OS/editor metadata, logs, caches, and generated reports when edits are in scope;
  - leave ambiguous untracked files untouched and mention them in the final response.

Fix vs suppress:

- Prefer fixing the code when the rule exposes real complexity, risk, dead code, unclear tests, resource leaks, or avoidable style debt.
- Suppress only when the current behavior is intentional, the direct fix would make the code worse, or the rule conflicts with the project/runtime constraints.
- Use the smallest reasonable suppression scope and include the exact Sonar rule id, for example `@SuppressWarnings("java:S127")`, `@SuppressWarnings("java:S1171")`, or `# NOSONAR python:S3776 - reason`.
- Add a short reason when the suppression syntax allows it, especially for complexity, console output, security-hotspot, deprecated API, and test-fixture suppressions.
- Do not use broad or rule-less suppressions when a specific Sonar id is known.

Verification before final response:

1. Run formatting if the project has a formatter.
2. Run the relevant tests for changed files.
3. Search changed/added files for obvious Sonar-triggering patterns, such as:
   - empty bodies: `{}`
   - `assertThrows(..., () -> ...)` with setup inside the lambda
   - manual `try { ... close(); }` patterns
   - reflection usage in tests
4. Inspect worktree status for accidental untracked artifacts, especially OS/editor metadata, logs, reports, caches, and generated local outputs.
5. Mention any Sonar issue or artifact hygiene issue that could not be resolved and why.

Don't use `sleep()` in JUnit tests - use Awaitility if available as dependency.

## Review Process

1. Identify changed or added files.
2. Understand the purpose of the change.
3. Apply the Sonar Cleanup Rule.
4. Treat search hits as leads, not automatic findings.
5. Fix clear issues when code edits are in scope.
6. Suppress only intentional or better-left-as-is issues with the narrowest scope and exact Sonar rule id.
7. Report actionable findings when the user asked only for review.
8. Run required verification when available.
9. Report fixed issues, suppressions, remaining concerns, and skipped verification.

## Output Style

### Sonar Review Summary

Provide:

1. Overall assessment
2. Files reviewed
3. Verification performed
4. Remaining risk

### Findings

For each finding provide:

1. Severity
2. Problem
3. Evidence
4. Recommended fix

### Final Verdict

Provide one of:

- Clean
- Clean after fixes
- Issues found
- Verification incomplete

If no issues are found, say that clearly.

## Completion Criteria

A Sonar cleanup pass is complete only when:

- changed or added files were reviewed
- the Sonar Cleanup Rule was applied
- clear issues were fixed or reported
- intentional issues were suppressed with exact Sonar rule ids when suppression is the better outcome
- accidental untracked/generated artifacts were fixed or explicitly reported for current-change/local-worktree reviews
- formatting and relevant tests were run when available
- unresolved issues and skipped verification were explicitly mentioned

## Skill Improvement

After completing a Sonar cleanup pass:

Evaluate whether this skill was sufficient.

If improvement is identified:

- describe the improvement
- provide a ready-to-paste update for this skill
