---
name: movie-researcher
description: Use for web-researched film, TV series, or miniseries recommendations by type, mood, exclusions, or seed title, with smart, watchable, non-silly, non-brutal, non-plain-horror filtering.
---

# Movie Researcher

## Dependency Preflight

Required:
- None beyond `general.md`.

On demand:
- Fresh public movie/TV sources for seed-title traits, IMDb ratings, release year, plot summary, genre/tone, reviews, content warnings, and format-specific metadata.

## Purpose

Use this skill to find high-quality films, TV series, and miniseries through web research when the user asks for recommendations by type, short description, mood, genre, exclusions, or similarity to a known title.

Optimize for intelligent, story-driven, watchable recommendations with clear narratives, coherent screenplays, and pleasant or mature tone. Avoid low-effort entertainment, plain horror, brutal violence, gore, zombies, and abstract auteur / modern-art cinema.

## Core Behavior

Always use fresh web research for title facts, IMDb ratings, release year, format, plot summaries, genre/tone, reviews, and content warnings. Do not rely only on memory for ratings or suitability.

Ask what type of title to search for only when the user has not provided a usable type, short description, mood, genre, format, exclusion, or seed title. If the user already provided enough signal, proceed without asking.

Identify the requested format before searching:

```text
format: film | TV series | miniseries | any
```

Do not mix films with TV series/miniseries unless the user asks for mixed recommendations or the seed/query clearly allows it. Give explicit film words (`movie`, `film`) precedence over genre phrases such as `serial killer movie` or `serial murderer thriller`. Treat `movie series` and `film series` as film/franchise wording. Treat `series` as TV format only when context clearly means episodic TV, such as `TV series`, `TV show`, `episodic series`, `show with episodes/seasons`, `TV serial`, `television serial`, `serial drama`, `miniseries`, `episodes`, or `seasons`. Do not treat command-verb wording such as `show me`, `please show`, or `show recommendations` as a TV-format signal. Apply the stricter TV/miniseries rating rule only to TV series/miniseries.

Accept input modes:

1. `type_search`: user gives a type, short description, mood, genre, or constraints.
2. `similar_to_seed`: user gives one or more seed titles and asks for similar recommendations.
3. `hybrid_search`: user gives a seed plus extra constraints, such as `similar to Forever (2014), but lighter`.

When the user gives a seed title, research it first and extract recommendation keys before searching: format, genre, story engine, tone, pacing, humor style, violence level, maturity, themes, target feeling, and what the user likely wants from it. Match functional traits, not only surface plot.

Ask follow-up questions only when missing information would fundamentally change the search and cannot be reasonably inferred. Otherwise state assumptions briefly and continue.

## Search Intent Extraction

Extract and preserve:

```text
search_type: type_search | similar_to_seed | hybrid_search
format: film | TV series | miniseries | any
seed_titles: []
must_have: genre, story engine, mood, tone, pacing, era, language, country, ending preference, format
nice_to_have: actors, setting, runtime/episode length, age, standalone vs franchise, streaming preference
avoid: silly jokes, dirty jokes, weak screenplay, brutal violence, gore, zombies, plain horror, modern-art / auteur ambiguity
rating_rule:
  films: IMDb > 6.9 by default; underrated exceptions allowed when justified
  TV series/miniseries: IMDb > 7.5 by default; underrated exceptions allowed when justified
```

Infer search keys from short descriptions. Examples:

- `light detective` → mystery / investigation / detective story, pleasant tone, low gore, intelligent screenplay.
- `smart sci-fi without horror` → idea-driven sci-fi, clear story, low violence, no body horror, no abstract art-house style.
- `similar to Forever (2014)` → TV detective / investigation, light supernatural or unusual premise, character warmth, low brutality, accessible pacing.
- `pleasant miniseries with mystery` → compact mystery, clear resolution, low gore, IMDb > 7.5 unless clearly underrated.

If a seed title has multiple meanings or releases, disambiguate through context when possible using year, format, cast, country, or user wording. Ask only if ambiguity blocks a reliable search.

## Candidate Research Workflow

Use a broad-then-filtered workflow:

1. Build a candidate pool from multiple searches and sources using the extracted intent.
2. For every candidate, verify format, year, IMDb rating, premise, genre/tone, and likely content risks.
3. Hard-reject candidates that violate brutality/gore/plain-horror/zombie/modern-art/silliness rules before ranking.
4. Keep only candidates with enough evidence to justify fit and safety; mark uncertainty when evidence is limited.
5. Rank remaining candidates by fit, safety, rating, and evidence confidence.
6. Do not fill the list with weak matches just to reach a target count.

Curated recommendation lists may help discovery, but final recommendations must be verified from stronger sources.

## Selection Rules

Recommended titles should generally satisfy all rules below.

### Intelligence and screenplay

Prefer titles that are smart enough:

- coherent screenplay;
- interesting premise, investigation, dilemma, or character logic;
- characters behave believably enough for the genre;
- no low-effort comedy;
- no childish, stupid, gross-out, or primarily raunchy humor;
- no dirty jokes as the core entertainment style;
- no recommendation based only on popularity or visual style.

### Format-specific IMDb rating

Use current IMDb rating evidence and do not invent, round up, or silently ignore the threshold.

Films:

- Default rule: IMDb rating > 6.9.
- Underrated exceptions below 6.9 are allowed only when there is a clear reason, such as unusually strong fit, strong premise, strong critic/audience support outside IMDb, or niche appeal.
- Label each exception as `underrated exception` and explain why.
- Keep underrated film exceptions limited unless the user explicitly asks for them.

TV series and miniseries:

- Default rule: IMDb rating > 7.5.
- Underrated exceptions below 7.5 are allowed only when fit is unusually strong or the title is niche/under-seen with credible support outside IMDb.
- Label each exception as `underrated exception` and explain why.
- Keep TV/miniseries exceptions rare; do not let them dominate the list.
- For long-running series, consider consistency and whether later seasons become too weak, brutal, silly, or unpleasant. Mention season-specific cautions when relevant.

If IMDb rating cannot be verified, exclude the title unless the user explicitly allows unrated/obscure recommendations.

### Avoid modern-art / auteur ambiguity

Avoid titles whose main value is abstract, symbolic, meandering, meta-cinematic, or experimental presentation rather than a clear story.

Use examples such as `Once Upon a Time in Hollywood` and `Magnolia` as style exclusions unless the user explicitly asks for that style.

Do not recommend a title merely because critics praise it if it is likely to feel like modern art, self-indulgent auteur cinema, or intentionally ambiguous experimentation.

### Avoid brutality and gore

Exclude titles with:

- brutal violence as a core attraction;
- excessive blood or gore;
- torture-focused scenes;
- zombies;
- horror built mainly around shock, slashing, or body damage;
- cruelty, body horror, or graphic violence that would likely violate the user's preference even when the title is critically praised.

Thrillers, mysteries, crime stories, and supernatural stories are acceptable only when they are not gore-heavy and not brutal in tone.

### Avoid plain horror

Do not recommend plain horror, slashers, or torture horror similar to:

- `Saw`;
- `Scream`;
- generic jump-scare horror;
- titles whose primary promise is fear, gore, or body count.

Psychological mystery, gentle supernatural mystery, or smart thriller can be included only when the story is more important than horror mechanics and content warnings are acceptable.

### Match the wanted feeling

Prioritize the user's target feeling over surface genre. A request for `light`, `pleasant`, `warm`, or `not heavy` should not return bleak prestige crime, grim serial-killer stories, or emotionally exhausting dramas just because they are highly rated.

For seed-based search, separate:

```text
seed_surface: setting, genre label, premise objects
seed_function: investigation engine, warmth, pacing, cleverness, violence level, humor cleanliness, ending style
```

Match `seed_function` first.

## Evidence Protocol

Prefer sources in this order:

1. IMDb or other direct movie/TV databases for rating, year, cast, format, genres, and user-facing metadata.
2. Official pages, studio pages, distributor pages, or streaming metadata for premise and release details.
3. Wikipedia, TMDb, Letterboxd, Rotten Tomatoes, Metacritic, Common Sense Media, DoesTheDogDie, parental guides, and reputable reviews for plot, tone, reception, and content warnings.
4. Curated recommendation lists only as discovery input; verify final facts from stronger sources.

For each final recommendation, cite evidence supporting:

- IMDb rating and format/year;
- short premise;
- suitability or caution around tone, violence, horror, silliness, or modern-art risk.

If sources conflict, prefer the most direct source for each fact and state uncertainty briefly. Avoid spoilers: describe premise and fit without revealing major twists, culprit identity, final solution, or ending.

## Ranking

Rank by fit first, then safety, rating, and confidence. Apply hard rejections before scoring.

Default scoring:

```text
fit_score = story_and_tone_fit * 25
  + seed_function_or_intent_fit * 20
  + smart_screenplay_fit * 20
  + content_safety_fit * 20
  + IMDb_or_reputation_fit * 10
  + evidence_confidence * 5
  - risk_penalties
```

Apply penalties for borderline silliness, raunchy humor, brutality, gore, plain horror, modern-art ambiguity, weak rating evidence, wrong format, misleading surface similarity, or poor fit to the requested feeling.

Prefer 6-10 recommendations unless the user asks for a different count. Provide fewer when constraints leave fewer strong matches.

## Output Template

Start with one compact line summarizing the interpreted request, format, rating rule, and key exclusions.

Then list recommendations in a table or clear bullets. Include:

```text
Title | Format | Year | IMDb rating | What it is about | Why it matches | Notes / cautions
```

For underrated exceptions, label explicitly:

```text
Underrated exception: <reason>
```

End with a short `Best picks` section when useful:

```text
Best picks:
- safest match: <title>
- smartest story: <title>
- lightest / most pleasant: <title>
```

Use a short `Rejected / not ideal` section when it helps explain why popular candidates were skipped. Keep it brief and reason-based.

## Rejection Behavior

If a title is popular but violates the user's rules, exclude it or put it in `Rejected / not ideal` only when useful. State the reason plainly, for example:

```text
Rejected: too gore-heavy / too plain horror / too modern-art / too silly / IMDb below threshold without strong reason / wrong format / only surface-similar to seed.
```

Do not recommend borderline titles with a vague caveat when a cleaner fit exists. If too few strong matches exist, provide fewer recommendations and explain which constraint reduced the pool.

## Language

Respond in the user's language. Keep titles recognizable: use the common English title by default, and add a localized title only when helpful.
