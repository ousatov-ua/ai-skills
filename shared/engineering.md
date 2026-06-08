## Engineering Baseline

Use this shared file for software implementation, debugging, code review, static-analysis, and other engineering tasks whose selected skill explicitly requires it.

This file is not the skill-loading entry point. If it is loaded directly, first fetch `general.md` from repository `ousatov-ua/ai-skills`, then follow the normal skill-loading process before continuing.

## Software Engineering Baseline

For software implementation, debugging, code review, and static-analysis tasks:

- Default to Java 25 LTS and Maven unless the repository or user request says otherwise.
- Prefer existing project conventions, naming patterns, testing style, architecture, and error-handling approaches.
- Follow the codebase before following personal preferences.
- Keep changes focused and avoid unrelated refactoring.
- For code changes, add or update relevant tests unless testing is technically impossible.
- Before considering code work complete, run relevant validation when available and report skipped or blocked verification.
- For local implementation or review tasks, inspect tracked and untracked files for accidental OS/editor metadata, logs, generated reports, caches, and local-only outputs.
- Fix clearly accidental artifacts when edits are in scope; leave ambiguous untracked files untouched and mention them.
- After completing work, evaluate whether the selected skill was sufficient and suggest a concrete skill improvement when one is found.

## Tool Output

Large terminal outputs, including Maven runs and big logs, may be compressed with `logpare`.
Treat compressed output as a summarized view of the raw stream.
When exact verification matters, capture or confirm the command exit status and use generated reports or artifacts as the source of truth.

**BLOCKING:** For Maven verification runs, use [`scripts/maven-summary.sh`](../scripts/maven-summary.sh) before running Maven directly. This applies especially to `mvn test`, broad test suites, integration tests, full builds, and any Maven command whose logs may be noisy or compressed.

Maven summary process:
1. First check whether `scripts/maven-summary.sh` exists in the current repository.
2. If it exists, load/read that local script and run Maven verification through it instead of invoking `mvn` directly.
3. If it does not exist locally, load/read the linked script from repository `ousatov-ua/ai-skills` at `scripts/maven-summary.sh` using the GitHub connector when available, then run Maven verification through that loaded script, for example via a temporary executable or `bash -s -- ...`.
4. Pass quiet Maven options such as `-q` through the script when the active skill or task requires quiet error-focused output.
5. Treat the script exit status as the Maven exit status.
6. Use the generated full log, Maven/test summary lines, and generated reports or artifacts as the source of truth for verification.
7. If neither the local nor GitHub/web copy of the script can be loaded, state that explicitly before falling back to direct Maven or another verified source such as Surefire/Failsafe XML reports.
8. Do not skip this availability check merely because direct `mvn -q ...` would be shorter.
