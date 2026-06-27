# Skills List and Dependency Manifest

**BLOCKING:** After selecting a skill, load its full Required load set before using the skill. Required load sets include transitive dependencies so agents do not need to discover dependency chains one hop at a time.

**BLOCKING:** Required load set = mandatory. On demand = conditional. If a required file cannot be fetched, ask the user to paste that exact URL and stop.

`__ROOT__` = `https://raw.githubusercontent.com/ousatov-ua/ai-skills/refs/heads/main`

## Skills

### `pragmatic-software-engineer`

Use for implementation, debugging, bug fixing, code investigation, refactoring, logs, troubleshooting.

Required load set:
- `__ROOT__/skills/pragmatic-software-engineer/SKILL.md`
- `__ROOT__/shared/engineering.md`

On demand:
- `__ROOT__/scripts/maven-summary.sh` only for Maven verification.

### `code-reviewer`

Use for PR/code/change reviews, implementation validation, correctness, reliability, testing, production readiness.

Required load set:
- `__ROOT__/skills/code-reviewer/SKILL.md`
- `__ROOT__/shared/engineering.md`

On demand:
- `__ROOT__/scripts/maven-summary.sh` only for Maven verification.

### `eval-runner`

Use for turning a prompt, AI workflow, model behavior, or agent task into a light, medium, or hard evaluation; collecting the minimum needed inputs; creating a self-contained eval spec; running it through in-chat, local, repository-native, or user-provided execution; and reporting results. Do not route to external eval providers.

Required load set:
- `__ROOT__/skills/eval-runner/SKILL.md`

On demand:
- User-provided datasets, logs, existing outputs, repository-native eval/test commands, local scripts, or manual scoring procedures only when needed.

### `linkedin-technical-branding`

Use for LinkedIn posts, profile content, professional branding, project/release/benchmark posts, recommendations.

Required load set:
- `__ROOT__/skills/linkedin-technical-branding/SKILL.md`

On demand:
- Fresh public examples, platform changes, profile/recruiting trends, or comparable posts/sources when the task depends on current LinkedIn behavior or niche market wording.

### `movie-researcher`

Use for web-researched film, TV series, or miniseries recommendations by format/type, short description, mood, genre, exclusions, or similarity to a seed title.

Required load set:
- `__ROOT__/skills/movie-researcher/SKILL.md`

On demand:
- Fresh public movie/TV sources for seed-title traits, IMDb ratings, release year, format, plot summary, genre/tone, reviews, content warnings, and format-specific metadata.

### `sales-investigator`

Use for evidence-based real estate purchase/sale investigation, property price analysis, buy-vs-wait decisions, negotiation preparation, affordability modeling, and legal/transaction risk screening.

Required load set:
- `__ROOT__/skills/sales-investigator/SKILL.md`

On demand:
- Current market, legal, macroeconomic, credit, exchange-rate, policy, or pricing sources whenever the decision depends on facts that can change.

### `autoresearcher`

Use only when specified directly or when the user asks for an autonomous improvement loop.

Required load set:
- `__ROOT__/skills/autoresearcher/SKILL.md`

On demand:
- None.
