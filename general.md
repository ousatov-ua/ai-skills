## Skills

**BLOCKING** For every task where a skill may be relevant, first try to load my skills from GitHub.

Skills repository:
- Repository: `ousatov-ua/ai-skills`
- Skills list path: `skills-list.md`
- Skill files are stored under: `skills/<skill-name>/SKILL.md`

Loading process:
1. Use the GitHub connector if available.
2. Fetch `skills-list.md` from repository `ousatov-ua/ai-skills`.
3. Select the best matching skill or skills for the current task.
4. Fetch each selected skill from `skills/<skill-name>/SKILL.md`.
5. Follow the loaded skill instructions when answering.
6. At the beginning of the response, mention which skill or skills were used.

Fallback rules:
- If the GitHub connector is unavailable, try web retrieval.
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
