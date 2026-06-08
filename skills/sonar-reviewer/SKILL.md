---
name: sonar-reviewer
description: Use for Sonar cleanup, SonarQube/SonarLint-oriented review, and pre-final checks of changed or added code and tests for common static-analysis issues such as empty bodies, assertThrows lambdas, resource handling, reflection-heavy tests, comments, and sleep-based JUnit tests.
---

# Sonar Reviewer

## Purpose

Use this skill to review changed or added code and tests for common Sonar issues before considering implementation work complete.

The goal is to catch practical static-analysis problems early, especially issues that are easy to miss during normal implementation or code review.

## Core Behavior

Act as a focused Sonar cleanup reviewer.

Review only relevant changed or added files unless the user asks for a broader scan.

Prefer fixing clear issues when code edits are in scope. If the user asked only for a review, report actionable findings instead of editing.

Prioritize issues likely to be raised by SonarQube, SonarLint, or equivalent static analysis.

Avoid speculative style churn and unrelated refactoring.

## Primary Checks

Focus especially on:

- empty methods, constructors, lambdas, overrides, or blocks
- exception-testing lambdas with more than the single invocation expected to throw
- manual resource closing where try-with-resources fits
- reflection-based test setup where direct constructors or helpers are available
- comments that are stale, verbose, generic, or only restate the code
- JUnit tests that use `sleep()` instead of Awaitility when Awaitility is available

## Empty Bodies

For empty methods, constructors, lambdas, overrides, or blocks:

1. Complete the implementation when behavior is required.
2. Throw `UnsupportedOperationException` when the operation is intentionally unsupported.
3. Add a short nested comment only when the empty body is intentional and valid.

Do not leave an unexplained empty body.

## Exception Tests

For `assertThrows` and similar exception-testing helpers:

- keep the lambda to the single invocation expected to throw
- move object construction outside the lambda
- move path resolution outside the lambda
- move builders, mocks, fixtures, and setup outside the lambda
- avoid multiple calls inside the throwing lambda

Prefer making the tested failure point obvious.

## Resources

For `Closeable` or `AutoCloseable` resources:

- use try-with-resources where possible
- avoid manual `close()` when try-with-resources fits
- keep cleanup behavior clear for exceptional paths

## Tests

For test code:

- avoid reflection-based setup when direct constructors, factories, or helpers can be used
- prefer explicit fixtures over hidden mutable state
- avoid `sleep()` in JUnit tests
- use Awaitility for asynchronous waits when it is available as a dependency

## Comments

Keep comments short and specific.

Add comments only when they clarify non-obvious intent, explain an intentionally empty body, or satisfy a legitimate static-analysis concern.

Remove comments that only repeat the code.

## Verification Workflow

Before final response after code or test changes:

1. Run formatting if the project has a formatter.
2. Run relevant tests for the changed files.
3. Search changed or added files for obvious Sonar-triggering patterns.
4. Resolve clear issues.
5. Mention any Sonar issue that could not be resolved and why.

Useful search targets include:

- empty bodies: `{}`
- `assertThrows(..., () -> ...)` lambdas with setup inside
- manual `try { ... close(); }` patterns
- reflection usage in tests
- `sleep()` in JUnit tests

## Output Style

When reporting a Sonar review, provide:

1. Issues found, ordered by severity.
2. File and line references where available.
3. Recommended fixes.
4. Verification performed.
5. Any unresolved Sonar concerns.

If no issues are found, say that clearly and include the verification performed.

## Completion Criteria

A Sonar cleanup pass is complete only when:

- changed or added files were checked for the primary Sonar patterns
- clear issues were fixed or reported
- relevant formatting/tests were run when available
- unresolved issues and skipped verification are explicitly mentioned
