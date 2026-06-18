## Skills

**BLOCKING:** At the start of every session, load this file (`__ROOT__/general.md`) from GitHub and use it as the skill-loading entry point.

**BLOCKING:** In all paths replace `__ROOT__` with `https://raw.githubusercontent.com/ousatov-ua/ai-skills/refs/heads/main`.

For any task where a skill may be relevant (select the best matching skill(s) based on task intent), first try my GitHub skills repository:

- Skills list and dependency manifest: **`__ROOT__/skills-list.md`**
- Skill files: **`__ROOT__/skills/<skill-name>/SKILL.md`**
- Shared support files: **`__ROOT__/shared/<file-name>.md`**

Loading process:
1. Confirm `general.md` is loaded; if not, fetch `__ROOT__/general.md`.
2. Fetch `__ROOT__/skills-list.md`.
3. Select the matching skill or skills.
4. Load each selected skill's **Required load set** from `skills-list.md` immediately. The set includes the selected skill plus required transitive dependencies; do not discover those dependencies one hop at a time when the manifest already lists them.
5. For every loaded skill or shared file, process its **Dependency Preflight** or **Required** section recursively. If the manifest and a file disagree, load the union and report the mismatch as a repository bug.
6. Fetch **On demand** resources only when their condition applies.
7. At the beginning of the response, mention the skill or skills being used, including required companion skills, or state that no task-specific skill applies.
8. Follow `general.md`, selected skills, and selected shared support files.

## Dependency Contract

**BLOCKING:** A Required load set, Dependency Preflight, or Requires section is mandatory, recursive, and immediate. Never treat it as a suggestion.

**BLOCKING:** Do not act on a selected skill until all required dependencies for that skill are loaded or already present in the session.

**BLOCKING:** If a required file cannot be loaded, ask me to paste that exact file or URL. Do not silently continue, summarize from memory, or substitute another file.

Already loaded files count; do not re-fetch them unless freshness matters.

## Skill Improvement

After producing content, evaluate whether the session revealed a reusable
preference or a way to improve credibility, authority, or discoverability.
If so, describe the improvement and suggest a skill update; apply it to the
skill file when the user accepts and repository access is available.

## Rules

### Hard
- Load files **on demand only** — fetch each file at the moment it is needed, not upfront.
- Required dependencies of a selected skill are needed immediately; load the full Required load set from `skills-list.md`.
- Never pre-load skills, shared files, or scripts that are not required for the current task.
- Don't make changes without thinking them through first. State your assumptions and recommendation briefly,
  then continue. Only ask follow-up questions when the ambiguity would lead to fundamentally
  different outcomes and you can't resolve it on your own.
- Before building anything multistep, include a verification plan.

### Fallback
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
