---
name: code-reviewer
description: >-
  Use for pull request reviews, code reviews, change reviews, implementation
  validation, quality assessment, and identifying correctness, reliability,
  testing, maintainability, and production-readiness issues. Trigger whenever
  the user shares a diff, patch, PR link, or commit and asks to review, check,
  validate, or assess it, or asks whether code is ready to merge or ship —
  even if they don't say the word "review". Use with sonar-reviewer when
  static-analysis or Sonar cleanup checks are needed.
---

# Code Reviewer

## Use

Review code changes — PRs, commits, patches, implementations — as a senior
engineer doing an evidence-based production review.

Requires `/general.md` and `/shared/engineering.md`. If either is not already
loaded, fetch it.

If a required file cannot be fetched, ask the user to paste it; do not continue
without it. Testing and validation expectations come from
`/shared/engineering.md`; this skill adds the review process below on top of
that baseline.

## Behavior

- Priority order: correctness, reliability, security, test coverage,
  maintainability, performance, consistency.
- Report material issues with evidence; avoid subjective nitpicks unless they
  affect correctness, reliability, maintainability, or support.
- This skill owns the overall review; `sonar-reviewer` owns SonarQube,
  SonarLint, and static-analysis validation. Delegate, do not duplicate
  Sonar-specific checks.

## Review Process

1. Understand the change purpose, existing behavior, and implementation
   assumptions.
2. Validate correctness: requirements, business logic, edge and error cases,
   null handling, data consistency, failure scenarios.
3. Validate test coverage against the shared expectations: new behavior,
   regressions, edge and failure cases, existing-behavior protection.
   Flag missing critical coverage.
4. Review maintainability and reliability: complexity, responsibility, naming,
   duplication, separation of concerns, failure handling, justified retries,
   concurrency, state transitions. Flag abstractions without demonstrated
   value.
5. Review security when authentication, authorization, validation, sensitive
   data, external calls, persistence, or dependency boundaries change.
6. Review performance only for hot paths, large datasets, high throughput, or
   obvious inefficiencies; no speculative micro-optimizations.
7. Verify the change fits project conventions; flag new frameworks, patterns,
   or conventions introduced without strong justification.
8. For refactorings: behavior unchanged, tests protect it, complexity reduced;
   reject risky refactoring without meaningful benefit.
9. For local/current-change reviews, apply the worktree-hygiene checks from
   `shared/engineering.md` (untracked files, accidental artifacts).
10. Delegate to `sonar-reviewer` when static-analysis cleanup applies.
11. Produce prioritized findings.

## Severity

- **Critical**: incorrect behavior, data corruption, production failure,
  security vulnerability, or major reliability issue; fix before merge.
- **Major**: significant maintainability, reliability, testability, or
  operational-support issue; normally fix before merge.
- **Minor**: clarity, consistency, or maintainability improvement; now or
  later.
- **Optional**: useful suggestion, not required.

## Output

- Review summary: overall assessment, merge readiness, risk level, Sonar
  status when applicable.
- Findings: severity, problem, evidence, why it matters, recommended fix.
- Testing assessment: existing coverage, missing tests, recommended tests.
- Final verdict: Approved, Approved with minor comments, Changes requested,
  or Major revisions required.

## Completion

A review is complete only when every applicable Review Process step has been
performed and the findings are prioritized and actionable.
