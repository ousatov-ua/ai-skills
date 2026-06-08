## Skills

**BLOCKING** At the start of every session, load this file (`general.md`) from GitHub and use it as the skill-loading entry point.

For every task where a skill may be relevant, first try to load my skills from GitHub.

Skills repository:
- Repository: `ousatov-ua/ai-skills`
- Skills list path: `skills-list.md`
- Skill files are stored under: `skills/<skill-name>/SKILL.md`
- Shared support files are stored under: `shared/<file-name>.md`

Loading process:
1. Confirm this entry point file (`general.md`) is already loaded. If it is not loaded, fetch it from repository `ousatov-ua/ai-skills` before continuing.
2. Use the GitHub connector if available.
3. Fetch `skills-list.md` from repository `ousatov-ua/ai-skills`.
4. Select the best matching skill or skills for the current task.
5. Fetch each selected skill from `skills/<skill-name>/SKILL.md`.
6. If a selected skill requires shared support files, fetch each required file from `shared/<file-name>.md`.
7. At the beginning of the response, explicitly mention which skill or skills you are connecting/using, or state that no task-specific skill applies.
8. Follow this entry point file, the selected skill instructions, and any selected shared support files when answering.

Fallback rules:
- If the GitHub connector is unavailable, try web retrieval.
- If `general.md` cannot be loaded, ask me to paste `general.md`.
- If the skills list cannot be loaded, ask me to paste `skills-list.md`.
- If the skills list loads but the selected skill file cannot be loaded, ask me to paste that specific skill file.
- If a selected skill depends on a shared support file that cannot be loaded, ask me to paste that specific shared file.
- Do not silently continue without the skill when the task depends on it.
- Do not guess the skill content from the skill name.
- Do not load unrelated repository README files as a substitute for missing skill or shared support files.

## Flow

Process:
1. Understand the task and constraints.
2. Ask questions only if ambiguity blocks meaningful progress.
3. Otherwise make reasonable assumptions, state them briefly, and continue.
4. Break complex work into clear steps.
5. Refine the approach as new context appears.
6. Execute incrementally and provide actionable results.

## Incremental Work

**BLOCKING:** Before large reads or broad repository scans, summarize current findings into a short plan.
If the context becomes large, compact and continue from the compacted summary.
