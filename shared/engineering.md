## Resources

**If a required resource cannot be fetched, ask the user to paste it; do not continue without it.**

**If a resource is already fetched, skip re-fetching.**

**BLOCKING:** Fetch and follow `__ROOT__/shared/compress.md`. For engineering tasks, final handoffs and progress updates are not “prose explanation” unless the user explicitly asks for an explanation. If it cannot be loaded, ask the user to paste it.

### Requires

- `general.md` from `__ROOT__/general.md`

### On Demand

- Skill `sonar-reviewer` from `__ROOT__/skills/sonar-reviewer/SKILL.md`
- Skill `ponytail` from `__ROOT__/skills/ponytail/SKILL.md`
- **Only for Maven projects:** `maven-summary.sh` from `__ROOT__/scripts/maven-summary.sh` — to run Maven verification.

## Engineering Baseline

Shared baseline for engineering skills: implementation, debugging, code review,
static analysis, and any task whose selected skill requires this file. If loaded
directly, fetch `general.md` first and follow the normal skill-loading process.
Skills extend this baseline; on conflict, follow Instruction Precedence below.

## Instruction Precedence

When instructions conflict, prefer:

1. Explicit user request in the current task.
2. Repository-local instructions and documented project conventions.
3. Task-specific selected skill.
4. Shared engineering baseline.
5. General assistant defaults.

Do not invent missing repository conventions, commands, dependencies, structure,
test results, or validation status. If unavailable, state the gap.

## Engineering Workflow

For implementation, debugging, refactoring, review, and static-analysis tasks:

1. Understand the goal, constraints, and existing behavior.
2. Inspect relevant files, tests, configs, logs, and docs before changing code.
3. Ask only questions that block meaningful progress.
4. When intent is clear, make conservative assumptions, state them briefly, and continue.
5. Prefer the smallest coherent change that solves the problem.
6. Add or update tests for changed behavior unless technically impossible.
7. Run the narrowest meaningful validation first, then broader validation when needed.
8. Inspect changed files, relevant diff, tracked changes, and untracked files before handoff.
9. Report changes, validation, skipped checks, and remaining risks.

Do not stop at analysis when enough information exists to act.

## Discovery and Command Hygiene

- Keep context focused: inspect targeted files first, avoid broad repository scans unless needed, and summarize findings before expanding scope.
- Prefer repository-native navigation, search, indexing, or RAG tools when available; verify important facts in source files before editing or reporting.
- Use scoped shell commands with explicit paths when possible; avoid noisy commands that dump excessive logs.
- Treat generated summaries, compressed logs, and search snippets as leads, not proof. Confirm important claims with source files, exit status, reports, artifacts, named tests, or focused full logs.

## Change Scope

- Follow existing project conventions, architecture, naming, testing, and error handling before personal preferences.
- Keep changes focused; avoid unrelated refactoring, formatting, cleanup, or rewrites.
- Do not add dependencies, frameworks, generated code, broad rewrites, or architecture changes unless required by the task.
- For refactorings: preserve behavior, keep tests protecting it, and reduce complexity or risk with evidence.
- Prefer small reversible changes over large speculative designs.

## Testing and Validation

- Add or update relevant tests for code changes unless technically impossible.
- Changed production behavior must be covered by tests unless technically impossible; if tests are skipped, explain why and name the remaining risk.
- Run available validation before completion; report skipped or blocked verification.
- For local implementation or review, validate only what is relevant and feasible for the task scope.

## Validation Evidence

Prefer evidence in this order:

1. Command/process exit status.
2. Generated reports and artifacts.
3. Named passing/failing tests.
4. Focused full logs.
5. Compressed logs or summaries.
6. Reasoned inspection when execution is unavailable.

Never claim tests, builds, checks, or static analysis passed unless command
execution or authoritative reports confirm it. If validation is skipped or
blocked, say why and name the remaining risk.

## Patch Hygiene

Before completion:

- Inspect tracked and untracked files.
- Revert unrelated formatting, cleanup, generated files, logs, reports, caches, and editor metadata.
- Do not modify lockfiles, generated sources, snapshots, formatter configs, or dependency metadata unless required.
- Fix clearly accidental artifacts when edits are in scope.
- Leave ambiguous untracked files untouched and mention them.
- Keep the final patch limited to task-relevant changes.

## Java Projects

- Default to Java 25 LTS and Maven unless the repository or user request says otherwise.
- New classes: add a short class-level Javadoc with `@author Oleksii Usatov`.
- New public methods: add brief Javadoc when project style supports public API documentation.
- Do not add `@author` to classes that are only being modified.
- Never embed SQL, Cypher, or similar query languages in Java production source; keep them in `.sql`, `.cypher`, or equivalent resource files.
- Exception: queries inside tests are allowed.

## Tool Output

Large logs may be compressed with `logpare`; treat them as summaries. When exact
verification matters, rely on exit status plus generated reports, artifacts,
named tests, or focused full logs.

## Maven Verification

**BLOCKING:** Run Maven verification (tests, integration tests, full builds,
noisy commands) through `maven-summary.sh`, never bare `mvn` — even when direct
`mvn -q ...` would be shorter:

1. If a local `scripts/maven-summary.sh` exists, read it and run Maven through it.
2. Otherwise fetch it, save and run it via a temporary executable or `bash -s -- ...`.
3. Pass `-q` when the task or skill asks for error-focused output.
4. Treat the script exit status as the Maven exit status; judge results by summary lines, reports, and artifacts — never raw log volume.
5. If the script cannot be loaded locally or remotely, say so before falling back to direct Maven plus Surefire/Failsafe reports.

## Commit Messages

Commit messages contain only what changed. Do not include verification steps,
validation notes, `git diff` output, test runs, Maven commands, or local logs.

## Skill Improvement

After finishing, note whether the selected skill was sufficient and suggest a
concrete skill improvement when useful.
