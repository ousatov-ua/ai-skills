# Autoresearch Run: linkedin-branding-jun16

## Run Specification

goal: improve `linkedin-technical-branding` so it produces LinkedIn content optimized for the Software Engineering community, with stronger first lines, better engineering wording, clearer line sequence, and professional/friendly intonation.

target_metric: manual rubric score out of 100.

comparison_rule: higher is better; ties go to clearer, more actionable, less bloated skill text.

evaluation_command: manual rubric review against fixed prompt set and current public research signals.

result_extraction: record score and keep/discard decision in `results.tsv`.

max_iterations: 12.

per_iteration_timeout: one bounded review/edit pass.

can_modify:
- `skills/linkedin-technical-branding/SKILL.md`
- `runs/autoresearch/linkedin-branding-jun16/program.md`
- `runs/autoresearch/linkedin-branding-jun16/results.tsv`

cannot_modify:
- `general.md`
- `skills-list.md`
- other skills

constraints:
- Keep the skill oriented to Software Engineers.
- Do not add clickbait, hype, or generic influencer formulas.
- Add actionable wording, sequencing, hook, intonation, and quality-check rules.
- Claims about public LinkedIn popularity must be bounded if exact engagement is not available.

## Fixed Evaluation Prompt Set

1. Generate a LinkedIn post for a Memgraph Ingester release focused on faster ingestion and improved incremental updates.
2. Generate a benchmark post comparing token usage with and without a code knowledge graph.
3. Generate an architecture lesson post about AI agents repeatedly rediscovering codebase relationships.
4. Rewrite a technical LinkedIn summary for a Lead Backend Engineer who wants to stay technical.
5. Review a generated post for wording, sequence of lines, hook strength, and intonation.

## Rubric

- Software Engineering audience fit: 20
- First-line/hook strength: 20
- Engineering wording quality: 20
- Sequence/structure clarity: 15
- Professional + friendly intonation: 10
- Evidence/boundedness: 10
- Operational usefulness of the skill: 5
