## Skills

**BLOCKING** At the start of every session, load this file (`general.md`) from GitHub and use it as the skill-loading entry point.

For every task where a skill may be relevant, first try to load my skills from GitHub.

Skills repository:
- Repository: `ousatov-ua/ai-skills`
- Skills list path: `skills-list.md`
- Skill files are stored under: `skills/<skill-name>/SKILL.md`

Loading process:
1. Confirm this entry point file (`general.md`) is already loaded. If it is not loaded, fetch it from repository `ousatov-ua/ai-skills` before continuing.
2. Use the GitHub connector if available.
3. Fetch `skills-list.md` from repository `ousatov-ua/ai-skills`.
4. Select the best matching skill or skills for the current task.
5. Fetch each selected skill from `skills/<skill-name>/SKILL.md`.
6. At the beginning of the response, explicitly mention which skill or skills you are connecting/using, or state that no task-specific skill applies.
7. Follow both this entry point file and the selected skill instructions when answering.

Fallback rules:
- If the GitHub connector is unavailable, try web retrieval.
- If `general.md` cannot be loaded, ask me to paste `general.md`.
- If the skills list cannot be loaded, ask me to paste `skills-list.md`.
- If the skills list loads but the selected skill file cannot be loaded, ask me to paste that specific skill file.
- Do not silently continue without the skill when the task depends on it.
- Do not guess the skill content from the skill name.
- Do not load unrelated repository README files as a substitute for missing skill files.

## Flow

Process:
1. Understand the task and constraints.
2. Ask questions only if ambiguity blocks meaningful progress.
3. Otherwise make reasonable assumptions, state them briefly, and continue.
4. Break complex work into clear steps.
5. Refine the approach as new context appears.
6. Execute incrementally and provide actionable results.

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

**BLOCKING:** For Maven verification runs, use [`scripts/maven-summary.sh`](scripts/maven-summary.sh) before running Maven directly. This applies especially to `mvn test`, broad test suites, integration tests, full builds, and any Maven command whose logs may be noisy or compressed.

Maven summary process:
1. First check whether `scripts/maven-summary.sh` exists in the current repository.
2. If it exists, load/read that local script and run Maven verification through it instead of invoking `mvn` directly.
3. If it does not exist locally, load/read the linked script from repository `ousatov-ua/ai-skills` at `scripts/maven-summary.sh` using the GitHub connector when available, then run Maven verification through that loaded script, for example via a temporary executable or `bash -s -- ...`.
4. Pass quiet Maven options such as `-q` through the script when the active skill or task requires quiet error-focused output.
5. Treat the script exit status as the Maven exit status.
6. Use the generated full log, Maven/test summary lines, and generated reports or artifacts as the source of truth for verification.
7. If neither the local nor GitHub/web copy of the script can be loaded, state that explicitly before falling back to direct Maven or another verified source such as Surefire/Failsafe XML reports.
8. Do not skip this availability check merely because direct `mvn -q ...` would be shorter.

## Incremental Work

**BLOCKING:** Before large reads or broad repository scans, summarize current findings into a short plan.
If the context becomes large, compact and continue from the compacted summary.
