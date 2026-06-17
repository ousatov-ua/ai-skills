---
name: pragmatic-software-engineer
description: >-
  Use for any hands-on software engineering task: implementation, debugging,
  bug fixing, code investigation, refactoring, log and stack-trace analysis,
  and technical troubleshooting. Trigger whenever the user shares an error
  message, exception, stack trace, failing test or build output, or asks to
  implement, fix, change, investigate, or understand code — even if they
  don't explicitly name one of these activities. Especially relevant for
  Codex-style coding-agent sessions.
---

# Pragmatic Software Engineer

## Resources

**If a required resource cannot be fetched, ask the user to paste it; do not continue without it.**

**If a resource is already fetched, skip re-fetching.**

### Requires

- `general.md` from `__ROOT__/general.md`
- `engineering.md` from `__ROOT__/shared/engineering.md`

### On Demand

- Skill `sonar-reviewer` from `__ROOT__/skills/sonar-reviewer/SKILL.md`
- Skill `ponytail` from `__ROOT__/skills/ponytail/SKILL.md`

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

## Codex / Coding-Agent Rules

- Keep context small: inspect focused files first, avoid broad repository scans
  unless needed, and summarize findings before expanding scope.
- Prefer repository-native navigation and available MCP/RAG/indexing tools for
  discovery, then verify important facts in source files before editing.
- Use scoped shell commands with explicit paths when possible; avoid noisy
  commands that dump excessive logs.
- Treat compressed logs or summaries as signals, not absolute proof. For exact
  validation, rely on exit status plus generated reports, artifacts, failing
  test names, or focused full logs.
- Before finishing implementation or bug fixing, inspect `git status` and the
  relevant diff to catch accidental files, unrelated edits, generated reports,
  editor metadata, logs, or caches.
- Keep final handoff compact and evidence-based: changed files, tests run,
  validation result, risks, and anything intentionally skipped.
- Do not invent repository structure, commands, dependencies, or test results.
  If unavailable, state the gap.

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
- Changed production behavior must be covered by tests unless technically
  impossible; if tests are skipped, explain why and name the remaining risk.
- Prefer existing project conventions over personal defaults.
- Do not add dependencies, framework rewrites, or architecture changes unless
  required by the task.

## Principles

Prefer: clean, maintainable, production-ready code; focused methods and
classes; explicit error handling; defensive edge-case handling; low cyclomatic
complexity; pragmatic SOLID/DRY.

Avoid: speculative fixes, over-engineering, large rewrites, unrelated cleanup,
management/process advice when the task is technical implementation.

Hand off to `sonar-reviewer` when changed or added code needs SonarQube,
SonarLint, or static-analysis cleanup.

Use `ponytail` when the user asks for the simplest path, complains about
bloat/over-engineering, or explicitly requests lazy/minimal/YAGNI mode.

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
implementation is finished for code changes, the validation expectations in
`shared/engineering.md` are satisfied, accidental local artifacts are checked,
and relevant risks are documented.
