## Skills

**BLOCKING:** At the start of every session, load this file (`general.md`) from GitHub and use it as the skill-loading entry point.

For any task where a skill may be relevant, first try my GitHub skills repository:

- Repository: `ousatov-ua/ai-skills`
- Skills list: `skills-list.md`
- Skill files: `skills/<skill-name>/SKILL.md`
- Shared support files: `shared/<file-name>.md`

Loading process:
1. Confirm `general.md` is loaded; if not, fetch `https://ousatov-ua.github.io/ai-skills/general.md`.
2. Fetch `skills-list.md`, select the matching skill or skills, then fetch each selected `SKILL.md`.
3. Fetch any shared support files required by the selected skills.
4. At the beginning of the response, mention the skill or skills being used, or state that no task-specific skill applies.
5. Follow `general.md`, selected skills, and selected shared support files.

Fetch URL pattern (always use GitHub Pages):
`https://ousatov-ua.github.io/ai-skills/<path>`

Load files **on demand only** — fetch each file at the moment it is needed, not upfront.
Never pre-load skills, shared files, or scripts that are not required for the current task.

Fallback rules:
- If a required file cannot be loaded, ask me to paste that specific file.
- Do not silently continue without a required skill or shared file.
- Do not guess missing skill content or substitute unrelated README files.

## Flow

1. Understand the task and constraints.
2. Ask only questions that block meaningful progress.
3. Otherwise make reasonable assumptions, state them briefly, and continue.
4. Break complex work into clear steps, refine as context appears, and execute incrementally.

## Incremental Work

**BLOCKING:** Before broad reads or repository scans, summarize current findings into a short plan. If context grows large, compact and continue from the compacted summary.
