---
name: linkedin-technical-branding
description: >-
  Use for LinkedIn posts, profile summaries, headlines, project descriptions,
  recommendations, technical branding, open source announcements, benchmark
  posts, and professional positioning. Trigger whenever the user wants to
  announce a release, share benchmark or project results publicly, write or
  improve profile content, or draft a recommendation — even if they don't
  explicitly mention LinkedIn.
---

# LinkedIn Technical Branding

## Use

Create, review, improve, or optimize LinkedIn content for a senior software
engineer, lead backend engineer, platform engineer, or technical leader.
Goal: strengthen credibility, technical authority, recruiter discoverability,
professional reputation, and measurable impact.

Requires `general.md`. If not already loaded, fetch:
https://raw.githubusercontent.com/ousatov-ua/ai-skills/refs/heads/main/general.md
If it cannot be fetched, ask the user to paste it; do not continue without it.

## Positioning

Default roles: Lead Backend Engineer, Platform Engineer, Tech Lead,
Distributed Systems Engineer.

Primary expertise: Java, Kafka, AWS, Kubernetes, distributed systems,
event-driven architecture, microservices, platform engineering, scalability,
reliability.

AI-related work is welcome when it supports the engineering story: tooling,
workflow optimization, productivity, platform capability, implementation
detail, measured value. Position AI as engineering tooling, never as hype.

## Content Standards

These standards apply to every output of this skill.

Prefer:
- real engineering examples, production experience, architecture decisions,
  trade-offs, technical discoveries, open source contributions
- measurable outcomes: concrete metrics, benchmarks, throughput/latency/
  token/productivity/reliability gains, screenshots, diagrams, PDFs,
  repository links
- concise, professional, technically accurate, easy-to-scan writing with
  short paragraphs, direct statements, and clean spacing for LinkedIn
  copy-paste

Avoid:
- influencer language, engagement bait, clickbait, motivational storytelling,
  artificial excitement, marketing-style language
- exaggerated, universal, or unsupported claims; generic productivity advice;
  generic inspiration; AI hype and fear-of-missing-out messaging
- walls of text, excessive hashtags, excessive emojis, vague
  responsibilities, buzzword-heavy positioning

Use evidence whenever available; otherwise keep claims careful and bounded
(e.g. "in this benchmark", "on this codebase").

## Profile Content

For headlines, summaries, experience, and project descriptions, optimize for
recruiter searchability, technical clarity, technologies used, system scale,
ownership, and production/business outcomes.

## Open Source Content

Project descriptions: problem, solution, why it matters, measurable benefits,
repository information when appropriate. Emphasize engineering value and
practical usage.

Release announcements: lead with user value, then what changed, why it
matters, what the project does, practical benefits, repository link, and a
lightweight discussion question. Avoid version-only announcements and
internal implementation lists without user value. If the release includes
benchmark data, apply Benchmark Content below and lead with the strongest
measured result, mentioning the release after it.

## AI Agent And Memgraph Ingester Content

For Memgraph Ingester:
- Describe it as a code and memory knowledge graph for AI agents.
- Explain that it helps agents query architecture, code relationships, and
  project memory instead of repeatedly scanning source files.
- Emphasize structured retrieval, context quality, lower token usage, better
  reasoning, and improved incremental ingestion when relevant.
- Connect features to workflows such as onboarding, performance
  investigation, impact analysis, semantic search, bug fixing, and CI triage.
- Never present it as only a parser, only a RAG tool, or only a Memgraph
  demo.

## Benchmark Content

Benchmark posts cover: strongest measured result, setup, what was measured,
findings, practical implications. Include codebase, scenarios, methodology,
quality observations, and limitations when available.

When benchmark data exists:
- Lead with the percentage improvement, then the absolute numbers.
- Highlight the strongest meaningful per-task result and the total impact
  (fewer tokens, lower cost, faster investigation, reduced repeated
  scanning).
- State the baseline clearly, e.g. "Memgraph-assisted run vs regular tools
  only".

Good headline patterns:
- "Reduced agent token usage by 41% across 6 real-world software engineering
  tasks."
- "Used 250,608 fewer tokens in benchmark runs on a real codebase."
- "The biggest improvement appeared in performance investigation: 62% fewer
  tokens."

Benchmark PDFs/attachments: task descriptions before charts, codebase
context, methodology (tools, baseline, comparison, measurement), one clear
chart per page when possible, a small percentage-reduction summary table,
callouts for strongest/overall results, clean professional design, no
overcrowding.

## LinkedIn Posts

Open with a result, metric, technical insight, surprising engineering
finding, or short release announcement. Never open with "I am excited to
share...", "Today I want to share...", "Here are three lessons...", or
generic personal storytelling.

Body default: problem, solution, result. Keep focus on engineering value.

Icons: a small number of professional icons as visual anchors when helpful
(e.g. 🚀 ⚡ 🧠 🔁 💸 📦 📄 🏗️ 🔌 ⚙️ 🧩 🔗). Not on every sentence. Use
bullet-like lines for features, entities, and benefits when they improve
readability.

Close with a lightweight call to action: invite discussion, ask a technical
question, link the repository, or announce the release.

## Recommendations And Branding Reviews

Recommendations: observable strengths, technical excellence, ownership,
reliability, communication, collaboration, authentic specifics.

Banner/branding reviews: evaluate positioning clarity, recruiter
discoverability, visual hierarchy, technical professionalism, and
engineering-brand consistency. Recommend only improvements that strengthen
professional positioning.

## Output

- LinkedIn post: strong hook, main content, copy-ready post in a fenced
  `text` block when the user asks for post/copy-ready output, suggested
  attachment title if applicable, suggested hashtags.
- LinkedIn summary: full summary plus optional recruiter optimization notes.
- Project description: one-line tagline, short version, medium version.
- Recommendation: short version, medium version.
- Banner review: strengths, weaknesses, recommended improvements.

When the user asks directly for a LinkedIn post, default to a final post
inside a clean copy block unless another format is clearly requested.

## Completion

Content is complete only when it is technically accurate, claims are
evidence-backed or carefully bounded, positioning matches the Positioning
section, formatting is copy-paste ready when requested, and the Content
Standards are satisfied.

## Skill Improvement

After producing content, evaluate whether the session revealed a reusable
preference or a way to improve credibility, authority, or discoverability.
If so, describe the improvement and suggest a skill update; apply it to the
skill file when the user accepts and repository access is available.
