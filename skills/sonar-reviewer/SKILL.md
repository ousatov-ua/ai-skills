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

## Review Process

1. Identify changed or added files.
2. Understand the purpose of the change.
3. Review implementation code for common Sonar issues.
4. Review test code for common Sonar issues.
5. Check resource handling.
6. Check exception assertions.
7. Check empty bodies and comments.
8. Run formatting when the project has a formatter.
9. Run relevant tests for changed files.
10. Report fixed issues, remaining concerns, and skipped verification.

## Empty Body Review

Verify empty methods, constructors, lambdas, overrides, and blocks.

For each empty body:

1. Complete the implementation when behavior is required.
2. Throw `UnsupportedOperationException` when the operation is intentionally unsupported.
3. Add a short nested comment when the empty body is intentional and valid.

Do not leave unexplained empty bodies.

## Exception Test Review

For `assertThrows` and similar exception-testing helpers:

- keep the lambda to the single invocation expected to throw
- move object construction outside the lambda
- move path resolution outside the lambda
- move builders, mocks, fixtures, and setup outside the lambda
- avoid multiple calls inside the throwing lambda

Prefer making the exact failure point obvious.

## Resource Review

For `Closeable` and `AutoCloseable` objects:

- use try-with-resources where possible
- avoid manual `close()` when try-with-resources fits
- verify cleanup behavior on exceptional paths

Prefer structured resource management over manual cleanup.

## Test Review

For test code:

- avoid reflection-based setup when direct constructors, factories, or helpers can be used
- prefer explicit fixtures over hidden mutable state
- avoid `sleep()` in JUnit tests
- use Awaitility for asynchronous waits when it is available as a dependency

Tests should make setup, action, and assertion boundaries clear.

## Comment Review

Keep comments short and specific.

Add comments only when they clarify non-obvious intent, explain an intentionally empty body, or satisfy a legitimate static-analysis concern.

Remove comments that only restate the code.

## Pattern Search

Search changed or added files for obvious Sonar-triggering patterns when appropriate.

Useful search targets include:

- empty bodies: `{}`
- exception assertions with setup inside the throwing lambda
- manual close patterns
- reflection usage in tests
- `sleep()` in JUnit tests

Treat search hits as leads, not automatic findings.

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
- empty bodies were checked
- exception assertions were checked
- resource handling was checked
- test-specific Sonar issues were checked
- formatting and relevant tests were run when available
- unresolved issues and skipped verification were explicitly mentioned

## Skill Improvement

After completing a Sonar cleanup pass:

Evaluate whether this skill was sufficient.

If improvement is identified:

- describe the improvement
- provide a ready-to-paste update for this skill
