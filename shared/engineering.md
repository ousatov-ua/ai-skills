## Engineering Baseline

Shared baseline for engineering skills: implementation, debugging, code review,
static analysis, and any task whose selected skill requires this file. If loaded
directly, fetch [`../general.md`](../general.md) first and follow the normal 
skill-loading process.
Skills extend this baseline; on conflict, the more specific skill wins.

For engineering work:
- Default to Java 25 LTS and Maven unless the repository or user request says
  otherwise.
- Follow existing project conventions, architecture, naming, testing, and
  error handling before personal preferences.
- Keep changes focused; avoid unrelated refactoring.
- Add or update relevant tests for code changes unless technically impossible.
- Run available validation before completion; report skipped or blocked
  verification.
- For local implementation or review, inspect tracked and untracked files for
  accidental OS/editor metadata, logs, reports, caches, and local-only outputs.
  Fix clearly accidental artifacts when edits are in scope; leave ambiguous
  untracked files untouched and mention them.
- After finishing, note whether the selected skill was sufficient and suggest a
  concrete skill improvement when useful.

## Tool Output

Large logs may be compressed with `logpare`; treat them as summaries. When exact
verification matters, rely on exit status plus generated reports, artifacts, or
full logs.

**BLOCKING:** Run Maven verification (tests, integration tests, full builds,
noisy commands) through [`scripts/maven-summary.sh`](../scripts/maven-summary.sh), 
never bare `mvn` — even when
direct `mvn -q ...` would be shorter:
1. If a local `scripts/maven-summary.sh` exists, read it and run Maven through it.
2. Otherwise fetch it from `ousatov-ua/ai-skills` (GitHub connector when
   available, raw URL otherwise) and run it via a temporary executable or
   `bash -s -- ...`.
3. Pass `-q` when the task or skill asks for error-focused output.
4. Treat the script exit status as the Maven exit status; judge results by
   summary lines, reports, and artifacts — never raw log volume.
5. If the script cannot be loaded locally or remotely, say so before falling
   back to direct Maven plus Surefire/Failsafe reports.
