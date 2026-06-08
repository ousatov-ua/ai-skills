## Skills

**BLOCKING** For every task where a skill may be relevant, first try to load my skills from GitHub.

Skills repository:
- Repository: `ousatov-ua/ai-skills`
- Skills list path: `skills-list.md`
- Skill files are stored under: `skills/<skill-name>.md`

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
5. Research/analyze provided code, files, docs, APIs, or current sources when useful.
6. Refine the approach as new context appears.
7. Execute incrementally and provide actionable results.

Coding principles:
- Prefer clean, maintainable, production-ready code.
- Favor simplicity over cleverness.
- Follow language/framework idioms and apply SOLID/DRY pragmatically.
- Keep methods/classes focused and cyclomatic complexity low.
- Use explicit error handling and cover edge cases.
- Comment only non-obvious logic.
- Prefer concrete implementations/examples over abstract advice.
- Include validation, testing, risks, or verification steps when relevant.
- Use available tools when they improve accuracy or completeness.

## Incremental Work

**BLOCKING:** Before large reads or broad repository scans, summarize current findings into a short plan.
If the context becomes large, compact and continue from the compacted summary.
Avoid huge generated files, `target/classes`, `node_modules`, build outputs, logs, and binaries.

## Java Docs

**BLOCKING** Please add short Java Docs. Also, please add "@author Oleksii Usatov" on Class level.
**BLOCKING** Don't embed SQL, cypher etc queries into the Java source code (**allow for Junit tests**): keep them in appropriate file (.sql, .cypher) in appropriate folder.

## Git

- Don't add verification and validation information into the commit message, e.g. ("Verification passed", "Validation", etc):
 a) No information about passed tests
 b) No `git diff` information
 c) No `mvn ...` information
- Preserve only `What changed` section of commit message.

## Maven

**BLOCKING** Use `-q` argument whenever you need to check only errors and severe problems
**BLOCKING** When you run all/specific tests in the project, e.g. `mvn test`, `mvn -q test` always use additional filtering for errors if your intention is to only check if all tests pass.
