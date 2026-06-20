---
name: pragmatic-software-engineer
description: >-
  Use for any hands-on software engineering task: implementation, debugging,
  bug fixing, code investigation, refactoring, log and stack-trace analysis,
  and technical troubleshooting. Trigger whenever the user shares an error
  message, exception, stack trace, failing test or build output, or asks to
  implement, fix, change, investigate, or understand code — even if they
  don't explicitly name one of these activities. Especially useful when working
  inside a repository or existing codebase.
---

# Pragmatic Software Engineer

## Dependency Preflight

**BLOCKING:** `engineering.md` must load its own required dependencies. Do not proceed until the full chain is loaded.

### Required

- `engineering.md` from `__ROOT__/shared/engineering.md`

### On Demand

- Skill `sonar-reviewer` from `__ROOT__/skills/sonar-reviewer/SKILL.md`

## Use

Implementation, investigation, debugging, refactoring, bug fixing,
troubleshooting. Goal: understand existing code, find root causes, implement
focused production-ready fixes, verify them, and report risks.

Conventions, testing, validation, discovery and command hygiene, patch hygiene,
Java rules, commit messages, and general engineering workflow come from
`engineering.md`; this skill adds implementation and debugging rules below on
top of that baseline.

## Workflow

1. Understand the request; ask only questions that block meaningful progress,
   otherwise state assumptions briefly and continue.
2. Inspect before changing: relevant code, logs, stack traces, tests, docs,
   config.
3. Reproduce the problem when feasible: failing test, minimal command, or
   focused local scenario. If not feasible, say so and explain how the
   hypothesis was verified instead.
4. Identify the root cause, not the symptom. If multiple causes are plausible,
   rank them and explain how to verify each.
5. Implement incrementally with minimal, focused changes.
6. Add or extend tests that pin changed behavior unless technically impossible.
7. Validate with the most relevant available command or report; for Maven,
   follow `engineering.md` and run through `maven-summary.sh`.
8. Report using the matching output shape, including risks.

Do not stop at analysis when enough information exists to act.

## Principles

Prefer: clean, maintainable, production-ready code; focused methods and
classes; explicit error handling; defensive edge-case handling; low cyclomatic
complexity; pragmatic SOLID/DRY.

Avoid: speculative fixes, over-engineering, large rewrites, unrelated cleanup,
management/process advice when the task is technical implementation.

Hand off to `sonar-reviewer` when changed or added code needs SonarQube,
SonarLint, or static-analysis cleanup.

## Output

Choose the matching shape; keep it concise and evidence-based:

- **Implementation**: assumptions, approach, changes made, tests added,
  validation performed, risks.
- **Bug fix**: root cause, evidence, fix, tests added, validation,
  regression risks.
- **Investigation**: findings, evidence, most likely explanation,
  remaining unknowns, recommended next step.

## Completion

Complete only when: the root cause is understood for investigations, the
implementation is finished for code changes, the validation expectations and
patch-hygiene rules in `shared/engineering.md` are satisfied, accidental local
artifacts are checked, and relevant risks are documented.
