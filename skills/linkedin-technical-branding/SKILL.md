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

## Resources

** If a required resource cannot be fetched, ask the user to paste it; do not continue without it. **

** If resource is already fetched, skip re-fetching **

### Requires

- `general.md` from `__ROOT__/general.md`

### On Demand

- Fresh public examples, platform changes, profile/recruiting trends, or comparable
  posts/sources when the task depends on current LinkedIn behavior or niche market
  wording.

## Use

Create, review, improve, or optimize LinkedIn content for a senior software
engineer, lead backend engineer, platform engineer, distributed systems engineer,
or technical open source author.

Goal: strengthen credibility, technical authority, recruiter discoverability,
professional reputation, and measurable impact inside the Software Engineering
community.

Requires `general.md`. If not already loaded, fetch it.
If it cannot be fetched, ask the user to paste it; do not continue without it.

## Audience

Primary audience: software engineers, senior engineers, staff/principal engineers,
backend/platform engineers, engineering managers who still care about technical
substance, technical recruiters, and open source users.

Optimize for readers who understand production systems, trade-offs, metrics,
architecture, debugging, reliability, developer tooling, and practical constraints.

Do not write for a generic business audience unless the user explicitly asks.
Software engineers should feel that the post was written by someone who has built,
measured, debugged, or operated real systems.

## Positioning

Default roles: Lead Backend Engineer, Platform Engineer, Tech Lead,
Distributed Systems Engineer, Backend Engineer, Developer Tooling Engineer.

Primary expertise: Java, Kafka, AWS, Kubernetes, distributed systems,
event-driven architecture, microservices, platform engineering, scalability,
reliability, observability, performance, code intelligence, AI-agent tooling,
and developer productivity.

AI-related work is welcome when it supports the engineering story: tooling,
workflow optimization, productivity, platform capability, implementation detail,
measured value, code intelligence, structured retrieval, or agent infrastructure.
Position AI as engineering tooling, never as hype.

## Research-Driven Pattern Extraction

When creating or improving LinkedIn posts, use comparable high-signal examples as
models when available. Prefer public posts/sources with visible engagement,
well-known technical authors, engineering companies, open source maintainers, or
credible case studies.

If direct LinkedIn post popularity is not reliably accessible, say so briefly and
use the best available evidence: public examples with reported impressions,
LinkedIn/feed ranking research, recent platform guidance, engineering blog/social
patterns, and comparable technical posts.

Extract patterns before drafting when the user asks for research, trend matching,
or skill improvement:

- hook type: metric, surprising result, hard engineering constraint, failure mode,
  benchmark, trade-off, before/after, or practical release value
- opening lines: what creates curiosity without clickbait
- sequence of lines: result -> context -> method/change -> evidence -> implication
  -> limitation -> call to action
- wording: concrete engineering nouns, verbs, and metrics used by credible posts
- intonation: professional, precise, calm, friendly, and human
- credibility signals: codebase size, baseline, benchmark setup, production scale,
  limitation, repository link, PDF/chart, concrete artifact, or reproducible step
- platform fit: professional relevance, author expertise, and opportunity value
  are more important than shallow engagement bait

Use these patterns as a model, not as text to copy.

## Research Procedure For Current Posts

When the user asks for a post that depends on current trends, examples, or
popular wording:

1. Search for recent comparable examples or credible secondary sources.
2. Identify 3-5 recurring patterns in hooks, structure, wording, and tone.
3. Reject patterns that depend on clickbait, exaggerated claims, or generic AI
   hype.
4. Draft from the strongest matching pattern for the user's topic.
5. Run the Model-Based Quality Check before returning the post.

Do not claim that a pattern is based on "most popular LinkedIn posts" unless the
source exposes popularity or engagement. If popularity cannot be verified, phrase
the finding as "accessible high-signal examples suggest..." or "current public
evidence suggests...".

## Content Standards

These standards apply to every output of this skill.

Prefer:
- real engineering examples, production experience, architecture decisions,
  trade-offs, technical discoveries, open source contributions
- measurable outcomes: concrete metrics, benchmarks, throughput/latency/token/
  productivity/reliability gains, screenshots, diagrams, PDFs, repository links
- concise, professional, technically accurate, easy-to-scan writing with short
  paragraphs, direct statements, and clean spacing for LinkedIn copy-paste
- specific engineering language: measured, baseline, benchmark, bottleneck,
  throughput, latency, p95/p99, replay, DLQ, schema evolution, incremental,
  dependency graph, impact analysis, structured retrieval, code relationships,
  production constraint, trade-off, failure mode, observability, reproducible
- friendly professional phrasing: "I wanted to check", "the interesting part",
  "what surprised me", "small but useful", "practical result", "still bounded",
  "worth testing on more codebases"

Avoid:
- influencer language, engagement bait, clickbait, motivational storytelling,
  artificial excitement, marketing-style language
- exaggerated, universal, or unsupported claims; generic productivity advice;
  generic inspiration; AI hype and fear-of-missing-out messaging
- walls of text, excessive hashtags, excessive emojis, vague responsibilities,
  buzzword-heavy positioning
- AI-slop formulas and generic patterns: "It's not X, it's Y", "game changer",
  "revolutionary", "10x everything", "supercharge your workflow", "unlock the
  future", "I am thrilled/excited to announce", "here are 5 lessons", "this
  changes everything", "let that sink in"

Use evidence whenever available; otherwise keep claims careful and bounded
(e.g. "in this benchmark", "on this codebase", "in this release", "for this
workflow", "early result").

## Best Wording For Software Engineer Posts

Use wording that sounds like an engineer explaining a useful result to other
engineers.

Strong wording patterns:
- "I measured X against Y on Z."
- "The result was not uniform — the biggest gain appeared in <scenario>."
- "The bottleneck was not <obvious guess>; it was <actual finding>."
- "The useful part is not the feature itself, but what it lets the agent avoid."
- "This reduced repeated source scanning and made the context more structured."
- "The trade-off: <cost/limitation>. The benefit: <measured/practical gain>."
- "This is still an early benchmark, but it is a useful signal."
- "The next thing I want to validate is <concrete follow-up>."

Weak wording patterns:
- "I built an amazing AI tool."
- "This will transform how developers work."
- "Every engineer needs this."
- "Massive productivity boost."
- "AI is replacing the old way of coding."
- "This is the future of software development."

For release posts, prefer: "released", "added", "improved", "measured",
"validated", "reduced", "refined", "made easier", "now supports".
For benchmark posts, prefer: "baseline", "scenario", "token usage",
"absolute reduction", "percentage reduction", "same task", "same codebase",
"quality observation", "limitation".
For architecture posts, prefer: "boundary", "dependency", "flow", "contract",
"failure mode", "replay", "consistency", "operational behavior".

## Wording Bank By Post Goal

Use this as a starting vocabulary, not as a template to copy mechanically.

### Release / Open Source

Good:
- "released a new version"
- "added support for"
- "improved incremental updates"
- "reduced repeated work"
- "made the workflow easier to reproduce"
- "the main change is practical"

Avoid:
- "huge launch"
- "massive breakthrough"
- "finally changing developer productivity forever"

### Benchmark / Measurement

Good:
- "same task, same codebase"
- "baseline run"
- "Memgraph-assisted run"
- "absolute token reduction"
- "percentage reduction"
- "quality observation"
- "bounded benchmark"

Avoid:
- "proves that"
- "always faster"
- "guaranteed cost savings"
- "industry-changing result"

### Architecture / Technical Lesson

Good:
- "the boundary matters"
- "the failure mode was"
- "the bottleneck moved"
- "the trade-off was"
- "operationally, this means"
- "under production constraints"

Avoid:
- "clean architecture solves everything"
- "just use"
- "simple trick"

### AI Agent / Developer Tooling

Good:
- "agent context"
- "structured retrieval"
- "code relationships"
- "queryable project memory"
- "less repeated source scanning"
- "better investigation path"

Avoid:
- "AI magic"
- "autonomous developer"
- "replace engineers"
- "10x coding overnight"

## Best-Match Post Models

Pick the model that best matches the user's topic.

### Model A: Measured Result

Use for benchmark, performance, latency, token, cost, or reliability posts.

Sequence:
1. Strongest measured result.
2. Baseline and comparison.
3. What was tested.
4. Why the result happened.
5. Practical implication.
6. Limitation.
7. Link/attachment/technical CTA.

### Model B: Engineering Constraint

Use when the insight is about a real limitation, trade-off, or failure mode.

Sequence:
1. Name the constraint.
2. Explain why it appears in real systems.
3. Show the technical approach.
4. Explain the trade-off.
5. End with the lesson.

### Model C: Release Value

Use for open source and product/tool releases.

Sequence:
1. What engineers can do now that they could not do as easily before.
2. Release name or project name.
3. 3-5 technical changes.
4. Workflow impact.
5. Repository link or invitation to test.

### Model D: Build Log / Technical Journey

Use for personal project progress without strong benchmark data.

Sequence:
1. Small but specific technical problem.
2. Why it mattered.
3. What was built or changed.
4. What was learned.
5. What is next.

### Model E: Credibility / Profile Positioning

Use for summaries, headlines, and profile sections.

Sequence:
1. Technical identity.
2. Core systems and technologies.
3. Scale or impact.
4. Current direction.
5. Selected evidence such as patents, production systems, or open source work.

## Hook Rules

The first 1-3 lines must make the target audience want to read the next lines.
They must be interesting because they reveal a concrete result, tension, or
engineering question — not because they use artificial suspense.

Strong hook types:

1. Metric hook
   - "I reduced agent token usage by 65% on one real code investigation task."
   - "Same task. Same codebase. 250k fewer tokens."

2. Surprising technical finding
   - "The biggest gain did not come from a smarter prompt. It came from better
     code context."
   - "The slow part was not parsing. It was repeatedly rediscovering the same
     relationships."

3. Engineering constraint
   - "AI agents are fast until they need to understand a real codebase from zero
     every time."
   - "Large codebases create a boring but expensive problem: repeated context
     reconstruction."

4. Before/after
   - "Before: scan files again. After: query the code graph first."
   - "Before this release, incremental ingestion was useful. Now it is much
     cheaper to keep the graph fresh."

5. Release value
   - "New Memgraph Ingester release: faster ingestion, cleaner incremental
     updates, and better instructions for coding agents."

Avoid hooks that are vague, self-focused, or generic:
- "I'm excited to share..."
- "Big news!"
- "The future of coding is here."
- "Developers, this one is for you."
- "Let's talk about AI."

## Hook Lab

Before finalizing a post, create at least 3 candidate opening hooks internally:

1. Metric/result hook.
2. Technical tension hook.
3. Practical release/workflow hook.

Pick the hook that is:
- most concrete
- most credible
- least generic
- most aligned with Software Engineering audience
- strong enough to make line 2 feel necessary

Discard hooks that rely on artificial suspense, personal excitement, vague
urgency, or unsupported claims.

## Line Sequence For Posts

Default sequence for Software Engineering posts:

1. Hook: concrete result, constraint, or finding.
2. Context: what was being built, measured, released, or investigated.
3. Problem: what engineers/agents usually struggle with.
4. Change: what changed technically.
5. Evidence: metric, benchmark setup, codebase size, scenario, or production fact.
6. Meaning: why it matters for real workflows.
7. Limitation: what is bounded, still early, or needs more validation.
8. CTA: repository link, attached PDF, technical question, or invitation to test.

For release announcements:

1. Hook with user value or strongest measured improvement.
2. Name the release/update.
3. List 3-5 technical changes as short bullets.
4. Explain why these changes matter in practical workflows.
5. Add evidence/benchmark/link when available.
6. Close with a low-pressure technical CTA.

For benchmark posts:

1. Lead with strongest meaningful result.
2. State baseline and comparison clearly.
3. State codebase and scenarios.
4. Show total result and per-scenario highlight.
5. Explain quality observations, not only token/cost savings.
6. State limitations.
7. Point to PDF/repository.

For project/story posts:

1. Start with the engineering problem.
2. Explain why the obvious solution was not enough.
3. Describe the implementation approach.
4. Share the result or lesson.
5. End with what is next.

## Intonation

Default tone: senior technical, precise, grounded, readable, and lightly friendly.

Professional part:
- use accurate terms, bounded claims, and concrete metrics
- explain trade-offs and limitations
- avoid emotional overclaiming
- keep sentences short and readable

Friendly part:
- allow a small amount of human wording: "I wanted to test this properly",
  "the interesting part", "what surprised me", "this is small, but useful"
- use 0-3 relevant icons only when they improve scanning
- sound like a thoughtful engineer sharing work, not a marketer selling a product

Tone calibration:
- Too dry: reads like changelog only; add one sentence explaining why it matters.
- Too friendly: reads like personal diary; add technical evidence and constraints.
- Too promotional: reads like marketing; replace adjectives with measured facts.
- Too defensive: reads like an apology; state limitations calmly and move on.
- Too generic: could be posted by anyone; add artifact, codebase, metric, or trade-off.

## Profile Content

For headlines, summaries, experience, and project descriptions, optimize for
recruiter searchability, technical clarity, technologies used, system scale,
ownership, and production/business outcomes.

Keep the user positioned as a technical contributor unless they explicitly ask
for management positioning.

## Open Source Content

Project descriptions: problem, solution, why it matters, measurable benefits,
repository information when appropriate. Emphasize engineering value and
practical usage.

Release announcements: lead with user value, then what changed, why it matters,
what the project does, practical benefits, repository link, and a lightweight
discussion question. Avoid version-only announcements and internal implementation
lists without user value. If the release includes benchmark data, apply Benchmark
Content below and lead with the strongest measured result, mentioning the release
after it.

## AI Agent And Memgraph Ingester Content

For Memgraph Ingester:
- Describe it as a code and memory knowledge graph for AI agents.
- Explain that it helps agents query architecture, code relationships, and
  project memory instead of repeatedly scanning source files.
- Emphasize structured retrieval, context quality, lower token usage, better
  reasoning, and improved incremental ingestion when relevant.
- Connect features to workflows such as onboarding, performance investigation,
  impact analysis, semantic search, bug fixing, and CI triage.
- Never present it as only a parser, only a RAG tool, or only a Memgraph demo.

Preferred Memgraph Ingester framing:
- "code and memory knowledge graph for AI coding agents"
- "queryable project memory"
- "structured retrieval over code relationships"
- "less repeated source scanning"
- "better context before code changes"

## Benchmark Content

Benchmark posts cover: strongest measured result, setup, what was measured,
findings, practical implications. Include codebase, scenarios, methodology,
quality observations, and limitations when available.

When benchmark data exists:
- Lead with the percentage improvement, then the absolute numbers.
- Highlight the strongest meaningful per-task result and the total impact
  (fewer tokens, lower cost, faster investigation, reduced repeated scanning).
- State the baseline clearly, e.g. "Memgraph-assisted run vs regular tools only".
- Do not claim better engineering quality unless the benchmark includes quality
  observations or human review.

Good headline patterns:
- "Reduced agent token usage by 41% across 6 real-world software engineering tasks."
- "Used 250,608 fewer tokens in benchmark runs on a real codebase."
- "The biggest improvement appeared in performance investigation: 62% fewer tokens."
- "The useful part was not a longer prompt. It was a better project memory model."
- "AI agents need less guessing when the codebase has a queryable graph."

Benchmark PDFs/attachments: task descriptions before charts, codebase context,
methodology (tools, baseline, comparison, measurement), one clear chart per page
when possible, a small percentage-reduction summary table, callouts for
strongest/overall results, clean professional design, no overcrowding.

## LinkedIn Posts

Open with a result, metric, technical insight, surprising engineering finding,
hard constraint, or short release announcement. Never open with "I am excited to
share...", "Today I want to share...", "Here are three lessons...", or generic
personal storytelling.

Body default: result -> context -> problem -> technical change -> evidence ->
practical meaning -> limitation -> CTA.

Use bullet-like lines for features, entities, and benefits when they improve
readability.

Icons: a small number of professional icons as visual anchors when helpful
(e.g. ⚡ ⚙️ 🧩 🔗 📊 📦). Not on every sentence. Avoid emoji-heavy formatting.

Close with a lightweight call to action: invite discussion, ask a technical
question, link the repository, invite people to test the release, or point to an
attached PDF. Do not use engagement bait such as "comment YES" or generic
"what do you think?" when a more precise technical CTA is possible.

## Draft Variant Workflow

For important posts, generate variants internally before choosing the final text:

1. Variant A: metric/result-led.
2. Variant B: engineering-constraint-led.
3. Variant C: practical-release-led or human-build-log-led.

Score each variant with the Model-Based Quality Check. Return the strongest
variant by default. Mention alternates only if the user asks for options.

## Model-Based Quality Check

Before returning a post, perform a quality check against the best available model
patterns.

Score each category from 0-5. A strong post should usually score at least 24/30
and have no category below 3.

1. Hook strength
   - Are the first 1-3 lines concrete, interesting, and likely to pull a Software
     Engineer into the next lines?
2. Wording
   - Does it use precise engineering wording instead of generic marketing or
     AI-slop phrases?
3. Sequence of lines
   - Does the flow move cleanly from result/context to technical change,
     evidence, implication, and CTA?
4. Intonation
   - Is it professional, calm, credible, and lightly friendly?
5. Evidence and boundedness
   - Are metrics, baselines, codebase context, limitations, and claims clear?
6. Audience fit
   - Would a senior software engineer find the post technically credible and not
     embarrassing to share?

Additional hard gates:
- First lines must not be self-focused unless the personal context is the point.
- At least one concrete artifact should appear when available: metric, repo,
  codebase, benchmark, release, production constraint, architecture detail, or
  observed trade-off.
- Claims about speed, quality, or cost must name the scope or comparison.
- No generic AI hype, engagement bait, or unsupported universal claims.

If a generated post fails the quality check, revise it before returning it.
When multiple variants are generated, pick the best match according to this
rubric and briefly explain why it was selected if useful.

## Technical Credibility Checklist

Before publishing, verify:

- Is the strongest claim supported by the user's data or a clear assumption?
- Is the baseline/comparison explicit?
- Is the scope bounded?
- Is the post useful to another engineer?
- Is the wording specific enough that a recruiter can index the expertise?
- Is there a real artifact: repository, benchmark, PDF, graph, codebase, release,
  production result, or architecture decision?
- Does the post avoid pretending that one benchmark proves a universal rule?

## Recommendations And Branding Reviews

Recommendations: observable strengths, technical excellence, ownership,
reliability, communication, collaboration, authentic specifics.

Banner/branding reviews: evaluate positioning clarity, recruiter discoverability,
visual hierarchy, technical professionalism, and engineering-brand consistency.
Recommend only improvements that strengthen professional positioning.

## Output

- LinkedIn post: strong hook, main content, copy-ready post in a fenced `text`
  block when the user asks for post/copy-ready output, suggested attachment title
  if applicable, suggested hashtags, and optional quality-check notes when the
  user asks for review/improvement.
- LinkedIn summary: full summary plus optional recruiter optimization notes.
- Project description: one-line tagline, short version, medium version.
- Recommendation: short version, medium version.
- Banner review: strengths, weaknesses, recommended improvements.
- Skill improvement: changed behavior, research findings used, quality rubric,
  and files changed.

When the user asks directly for a LinkedIn post, default to a final post inside a
clean copy block unless another format is clearly requested.

## Completion

Content is complete only when it is technically accurate, claims are
evidence-backed or carefully bounded, positioning matches the Positioning
section, formatting is copy-paste ready when requested, and the Content Standards
are satisfied.

For Software Engineering community posts, completion additionally requires:
- first lines are strong enough to create honest curiosity
- wording is engineering-specific and not generic marketing
- sequence of lines is coherent and easy to scan
- intonation is professional with a friendly human touch
- claims are bounded by evidence, benchmark setup, or clearly stated assumptions
- the final selected post is the best match among plausible hook/sequence variants
