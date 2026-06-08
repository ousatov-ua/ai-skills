---
name: linkedin-technical-branding
description: Use for LinkedIn posts, profile summaries, headlines, project descriptions, recommendations, technical branding, open source announcements, benchmark posts, and professional positioning.
---

# LinkedIn Technical Branding

## Use

Use to create, review, improve, or optimize LinkedIn content for a senior software engineer, lead backend engineer, platform engineer, or technical leader. Goal: strengthen credibility, technical authority, recruiter discoverability, professional reputation, and measurable impact.

## Positioning

Default roles: Lead Backend Engineer, Platform Engineer, Tech Lead, Distributed Systems Engineer.

Primary expertise: Java, Kafka, AWS, Kubernetes, distributed systems, event-driven architecture, microservices, platform engineering, scalability, reliability.

AI-related work is welcome when it supports the engineering story through tooling, workflow optimization, productivity, platform capability, implementation detail, or measured value. Avoid AI hype, speculation, and fear-of-missing-out messaging.

## Content Standards

Prefer:
- real engineering examples, production experience, architecture decisions, trade-offs, technical discoveries, open source contributions
- measurable outcomes, concrete metrics, benchmarks, throughput/latency/token/productivity/reliability gains, screenshots, diagrams, PDFs, repositories
- concise, professional, technically accurate, easy-to-scan writing with short paragraphs and direct statements
- clean spacing for LinkedIn copy-paste and lightweight icons when they improve scanability

Avoid:
- influencer language, engagement bait, clickbait, motivational storytelling, artificial excitement
- exaggerated or unsupported claims, generic productivity advice, generic inspiration
- walls of text, excessive hashtags, excessive emojis, vague responsibilities, buzzword-heavy positioning

Use evidence whenever available; otherwise keep claims careful and bounded.

## Profile Content

For headlines, summaries, experience, and project descriptions, optimize for recruiter searchability, technical clarity, measurable impact, technologies used, system scale, business impact, ownership, and production outcomes.

## Open Source Content

Project descriptions should explain the problem, solution, why it matters, measurable benefits, and repository information when appropriate. Emphasize engineering value, practical usage, and outcomes; avoid marketing-style language.

Release announcements should lead with user value, then what changed, why it matters, what the tool/project does, practical benefits, repository link, and a lightweight discussion question. Avoid generic or version-only announcements and internal implementation lists without user value.

If release data includes benchmarks, lead with the strongest measured result, mention the release after the result, connect improvements to impact, and keep implementation details secondary.

## AI Agent And Memgraph Ingester Content

Position AI as engineering tooling, developer productivity, workflow optimization, or platform capability. Prefer implementation detail, engineering workflows, measurable improvements, and benchmark-driven conclusions.

For Memgraph Ingester:
- Describe it as a code and memory knowledge graph for AI agents.
- Explain that it helps agents query architecture, code relationships, and project memory instead of repeatedly scanning source files.
- Emphasize structured retrieval, context quality, lower token usage, better reasoning, and improved incremental ingestion when relevant.
- Connect features to workflows such as onboarding, performance investigation, impact analysis, semantic search, bug fixing, and CI triage.
- Avoid presenting it as only a parser, only a RAG tool, or only a Memgraph demo.

## Benchmark Content

Benchmark posts should cover strongest measured result, setup, what was measured, findings, and practical implications. Include codebase, scenarios, methodology, quality observations, and limitations when available.

When benchmark data exists:
- Lead with percentage improvement before raw numbers; include absolute numbers after the percentage.
- Highlight the strongest meaningful per-task result and total impact, such as fewer tokens, lower cost, faster investigation, or reduced repeated scanning.
- Use careful wording such as "reduced token usage in this benchmark"; avoid universal claims.
- State the baseline clearly, for example "Memgraph-assisted run vs regular tools only".

Good benchmark headline patterns:
- "Reduced agent token usage by 41% across 6 real-world software engineering tasks."
- "Used 250,608 fewer tokens in benchmark runs on a real codebase."
- "The biggest improvement appeared in performance investigation: 62% fewer tokens."

Benchmark PDFs or attachments should include task descriptions before charts, codebase context, methodology with tools/baseline/comparison/measurement, one clear chart per page when possible, a small percentage-reduction summary table, callouts for strongest/overall results, clean professional design, and no overcrowding.

## LinkedIn Posts

Open with a result, metric, technical insight, surprising engineering finding, or short release announcement. Avoid "I am excited to share...", "Today I want to share...", "Here are three lessons...", and generic personal storytelling.

Body default: problem, solution, result. Keep focus on engineering value.

Use a small number of professional icons as visual anchors when helpful, for example 🚀, ⚡, 🧠, 🔁, 💸, 📦, 📄, 🏗️, 🔌, ⚙️, 🧩, 🔗. Do not put an icon on every sentence. Use bullet-like lines for features, entities, and benefits when they improve readability.

Close with a lightweight call to action: invite discussion, ask a technical question, provide a repository link, or announce a release. Avoid engagement farming.

## Recommendations And Branding Reviews

Recommendations should focus on observable strengths, technical excellence, ownership, reliability, communication, collaboration, and authentic specifics. Avoid generic praise, exaggerated statements, and unsupported claims.

Banner/branding reviews should evaluate positioning clarity, recruiter discoverability, visual hierarchy, technical professionalism, and engineering-brand consistency. Recommend only improvements that strengthen professional positioning.

## Output

- LinkedIn post: strong hook, main content, copy-ready post in a fenced `text` block when the user asks for post/copy-ready output, suggested attachment title if applicable, suggested hashtags.
- LinkedIn summary: full summary plus optional recruiter optimization notes.
- Project description: one-line tagline, short version, medium version.
- Recommendation: short version, medium version.
- Banner review: strengths, weaknesses, recommended improvements.

When the user asks directly for a LinkedIn post, default to a final post inside a clean copy block unless another format is clearly requested.

## Validation And Completion

Before finalizing, verify the content is technically accurate, evidence-backed, concise, recruiter-friendly, aligned with engineering positioning, free of hype/generic statements, copy-paste friendly when applicable, and uses icons only when useful.

Content is complete only when technical credibility is preserved, positioning is clear, value is communicated effectively, claims are supported, and formatting fits direct LinkedIn use when requested.

## Skill Improvement

After producing content, evaluate whether it improves credibility, authority, discoverability, or captures a reusable user preference. If useful, describe the improvement, provide an improved version, and suggest a skill update. If the user accepts or directly requests the improvement, update the actual skill file when repository access is available.
