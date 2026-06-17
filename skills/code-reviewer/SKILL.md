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

## Resources

**If a required resource cannot be fetched, ask the user to paste it; do not continue without it.**

**If a resource is already fetched, skip re-fetching.**

### Requires

- `general.md` from `__ROOT__/general.md`
- `engineering.md` from `__ROOT__/shared/engineering.md`

### On Demand

- Skill `sonar-reviewer` from `__ROOT__/skills/sonar-reviewer/SKILL.md`

## Use

Review code changes — PRs, commits, patches, implementations — as a senior
engineer doing an evidence-based production review.

Instruction precedence, project conventions, validation expectations, patch
hygiene, and change-scope rules come from `engineering.md`; this skill adds the
review process, severity model, performance-evidence rules, and review output
shape below.

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
3. Validate test coverage against `engineering.md` expectations: new behavior,
   regressions, edge and failure cases, existing-behavior protection. Flag
   missing critical coverage.
4. Review maintainability and reliability: complexity, responsibility, naming,
   duplication, separation of concerns, failure handling, justified retries,
   concurrency, state transitions. Flag abstractions without demonstrated
   value.
5. Review security when authentication, authorization, validation, sensitive
   data, external calls, persistence, or dependency boundaries change.
6. Review performance only for hot paths, large datasets, high throughput, or
   obvious inefficiencies; no speculative micro-optimizations. Back any
   performance claim per Performance Evidence.
7. Check conventions and change scope per `engineering.md`; flag unjustified
   new frameworks, patterns, broad rewrites, dependency changes, or convention
   drift.
8. For refactorings: behavior unchanged, tests protect it, complexity or risk
   reduced; reject risky refactoring without meaningful benefit.
9. For local/current-change reviews, apply `engineering.md` patch-hygiene
   checks.
10. Delegate to `sonar-reviewer` when static-analysis cleanup applies.
11. Produce prioritized findings.

## Performance Evidence

When a change claims, implies, or is asked about a performance effect, back
the assessment with evidence at the cheapest sufficient tier:

1. **Reason from code** (always required): identify what moved on or off the
   critical path, estimate per-call cost times call frequency, and bound the
   effect — best case, worst case, and the conditions where it is ~0.
2. **Measure with existing verification artifacts**: timings, counters, and
   reports produced by the test/build runs already executed for the review.
   Use only evidence sources the user has approved; do not mine local logs or
   private data files uninvited.
3. **Benchmark**: when a hard number matters and analysis cannot bound it,
   propose a dedicated reproducible A/B benchmark (baseline vs change,
   cold/warm state controlled) and let the user opt in; never run heavy
   benchmarks unprompted.

Rules:

- Never state a performance number without saying how it was obtained.
- Report magnitude with its bound and the conditions where the effect
  vanishes, not a single optimistic figure.
- Flag observability shifts: when work moves into or out of a measured
  phase or metric, note that historical metric comparisons will shift even
  if wall-clock behavior is unchanged.

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
