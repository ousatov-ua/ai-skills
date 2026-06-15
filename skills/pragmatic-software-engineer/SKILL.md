---
name: pragmatic-software-engineer
description: >-
  Use for any hands-on software engineering task: implementation, debugging,
  bug fixing, code investigation, refactoring, log and stack-trace analysis,
  and technical troubleshooting. Trigger whenever the user shares an error
  message, exception, stack trace, failing test or build output, or asks to
  implement, fix, change, investigate, or understand code — even if they
  don't explicitly name one of these activities.
---

# Pragmatic Software Engineer

## Resources

** If a required resource cannot be fetched, ask the user to paste it; do not continue without it. **

** If resource is already fetched, skip re-fetching **

### Requires

- `general.md` from `__ROOT__/general.md
- `engineering.md` from `__ROOT__/shared/engineering.md`

### On Demand

- Skill `sonar-reviwer` from `_ROOT_/skills/sonar-reviwer/SKILL.md`

## Use

Implementation, investigation, debugging, refactoring, bug fixing,
troubleshooting. Goal: understand existing code, find root causes, implement
focused production-ready fixes, verify them, and report risks.

Conventions, testing, and validation expectations come from
`engineering.md`; this skill adds the workflow and rules below on top
of that baseline.

## Workflow

1. Understand the request; ask only questions that block meaningful progress,
   otherwise state assumptions briefly and continue.
2. Inspect before changing: relevant code, logs, stack traces, tests, docs,
   config.
3. Reproduce the problem when feasible (failing test, minimal command). If not
   feasible, say so and explain how the hypothesis was verified instead.
4. Identify the root cause, not the symptom. If multiple causes are plausible,
   rank them and explain how to verify each.
5. Implement incrementally with minimal, focused changes.
6. Verify per `engineering.md` (Maven runs go through
   `maven-summary.sh`); add or extend tests that pin the fix.
7. Report using the matching output shape, including risks.

Do not stop at analysis when enough information exists to act.

## Blocking Rules

Java projects:
- New classes: add a short class-level Javadoc with `@author Oleksii Usatov`.
  Add brief Javadoc to new public methods. Do not add `@author` to classes
  that are only being modified.
- Never embed SQL, Cypher, or similar query languages in Java source; keep
  them in `.sql` / `.cypher` resource files. Exception: queries inside JUnit
  tests are allowed.

All projects:
- Commit messages contain only the "what changed" content. Never include
  verification steps, validation notes, `git diff` output, test runs, or
  Maven commands in the message.

## Principles

Prefer: clean, maintainable, production-ready code; focused methods and
classes; explicit error handling; defensive edge-case handling.

Avoid: speculative fixes, over-engineering, large rewrites.

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

Complete only when: the root cause is understood (investigations), the
implementation is finished, the validation expectations in
`shared/engineering.md` are satisfied, and relevant risks are documented.
