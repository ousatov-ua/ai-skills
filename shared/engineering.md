## Engineering Baseline

Use for software implementation, debugging, code review, static analysis, and any engineering task whose selected skill requires this file. If loaded directly, fetch `general.md` first and follow the normal skill-loading process.

For engineering work:
- Default to Java 25 LTS and Maven unless the repository or user request says otherwise.
- Follow existing project conventions, architecture, naming, testing, and error-handling before personal preferences.
- Keep changes focused; avoid unrelated refactoring.
- Add or update relevant tests for code changes unless technically impossible.
- Run available validation before completion; report skipped or blocked verification.
- For local implementation or review, inspect tracked and untracked files for accidental OS/editor metadata, logs, reports, caches, and local-only outputs.
- Fix clearly accidental artifacts when edits are in scope; leave ambiguous untracked files untouched and mention them.
- After finishing, note whether the selected skill was sufficient and suggest a concrete skill improvement when useful.

## Tool Output

Large logs may be compressed with `logpare`; treat them as summaries. When exact verification matters, rely on exit status plus generated reports, artifacts, or full logs.

**BLOCKING:** For Maven verification runs, use [`scripts/maven-summary.sh`](../scripts/maven-summary.sh) before direct `mvn`, especially for tests, integration tests, full builds, and noisy Maven commands.

Maven summary process:
1. Check for local `scripts/maven-summary.sh`; if present, read it and run Maven through it.
2. Otherwise fetch `scripts/maven-summary.sh` from `ousatov-ua/ai-skills` with the GitHub connector when available, then run it via a temporary executable or `bash -s -- ...`.
3. Pass quiet options such as `-q` when the task or skill asks for error-focused output.
4. Treat the script exit status as the Maven exit status.
5. Use the full log, Maven/test summary lines, and reports or artifacts as verification truth.
6. If neither local nor GitHub/web script can be loaded, say so before falling back to direct Maven or reports such as Surefire/Failsafe XML.
7. Do not skip this availability check merely because direct `mvn -q ...` is shorter.
