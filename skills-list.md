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
- `__ROOT__/shared/compress.md`

On demand:
- `__ROOT__/skills/sonar-reviewer/SKILL.md` when changed or added code needs SonarQube, SonarLint, or static-analysis cleanup.
- `__ROOT__/scripts/maven-summary.sh` only for Maven verification.

### `code-reviewer`

Use for PR/code/change reviews, implementation validation, correctness, reliability, testing, production readiness.

Required load set:
- `__ROOT__/skills/code-reviewer/SKILL.md`
- `__ROOT__/shared/engineering.md`
- `__ROOT__/shared/compress.md`

On demand:
- `__ROOT__/skills/sonar-reviewer/SKILL.md` when static-analysis or Sonar cleanup checks are needed.
- `__ROOT__/scripts/maven-summary.sh` only for Maven verification.

### `sonar-reviewer`

Use for SonarQube/SonarLint cleanup, static-analysis validation, changed-code/test static-analysis issues.

Required load set:
- `__ROOT__/skills/sonar-reviewer/SKILL.md`
- `__ROOT__/shared/engineering.md`
- `__ROOT__/shared/compress.md`

On demand:
- `__ROOT__/scripts/maven-summary.sh` only for Maven verification.

### `linkedin-technical-branding`

Use for LinkedIn posts, profile content, professional branding, project/release/benchmark posts, recommendations.

Required load set:
- `__ROOT__/skills/linkedin-technical-branding/SKILL.md`

On demand:
- Fresh public examples, platform changes, profile/recruiting trends, or comparable posts/sources when the task depends on current LinkedIn behavior or niche market wording.

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
