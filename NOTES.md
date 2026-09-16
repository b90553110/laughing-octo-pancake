# Working notes

Preferences and observations that shape how lessons get written.

## Stated preferences

- **Maven, never Gradle.** Explicit.
- **Teach in the voice of a tech lead.** Requested directly: reasons, trade-offs,
  and what matters in code review — not step-by-step instructions alone.
- Self-described as a newbie, but answered "comfortable with Java, new to Spring".
  Treat the Java as real and do not pad lessons with language basics; the newbie
  part is Spring and the ecosystem around it.

## Observations

- Reads on a phone. Keep lessons short, and keep code blocks narrow enough that
  horizontal scrolling is rare.
- The mission is deliberately unsharpened (see `MISSION.md`). Revisit it once a
  concrete project appears; until then, bias lessons toward fundamentals that pay
  off regardless of what gets built.

## Teaching decisions made

- Lesson 01 chose `@SpringBootTest` + `@AutoConfigureMockMvc` over the faster
  `@WebMvcTest` slice. Rationale: lesson 01 is about *the whole app starting*, so
  the test should exercise that. Introduce slices later, as an optimisation with a
  reason, rather than as unexplained ceremony.
- Every command in lesson 01 was executed before publishing. Continue this: a
  lesson that does not run is worse than no lesson, and this ecosystem punishes
  recalled knowledge.

## Session 2 (10 Sep 2026)

- Asked for Flyway next, ahead of the beans/dependency-injection lesson promised
  at the end of Lesson 01. Follow the learner's pull: they are evidently thinking
  about real services (databases, deploys) rather than framework internals. Keep
  the beans lesson queued, but do not force the order.
- Explicitly said not to verify code by building it in a sandbox. Lesson 02 is
  therefore version-checked but not executed, and says so in its header. Keep
  that disclosure on any lesson that was not run — the distinction matters, and
  claiming otherwise would poison the trust the whole workspace runs on.
- Signal to watch: the tech-lead framing is landing on *operational* questions
  (what breaks in production) more than on API surface. Weight future lessons
  accordingly — migration design, rolling deploys, testing strategy.

## Session 3 (15 Sep 2026)

- Set a standing style directive: active voice, no ambiguous phrasing, no casual
  metaphors, direct and authoritative engineering tone, technical precision first.
  Recorded in `CLAUDE.md` so every future session follows it, not just this one.
- Rewrote Lesson 02 to that standard. Lesson 01 still carries the older
  conversational voice and needs the same treatment.
- Asked for Flyway practice lessons covering team conflicts and frequent
  development-environment schema changes. Both topics are operational rather than
  API-level, which matches the pattern noted in session 2. Keep weighting lessons
  toward operations.
- Correction worth remembering: Spring Boot sets `spring.flyway.clean-disabled`
  to `true`, which differs from Flyway's own default. Several web sources state
  the opposite. Read `FlywayProperties` in the Boot sources jar for defaults.

## Session 4 (15 Sep 2026)

- Restructured lessons into **tracks**. `lessons/spring/` and
  `lessons/playwright/`, numbered independently. Moving the four existing Spring
  lessons changed their published URLs; the repository is new enough that the
  cost is near zero, and delaying the move would raise it.
- Added the Playwright track: TypeScript, targeting an Angular front end with
  Angular Material. The learner named Angular when choosing the language, which
  is more specific than the question asked — build on that and use Material's
  ARIA roles in examples rather than generic HTML.
- Recorded a deliberate deviation in `MISSION.md`: the skill requires one mission
  per workspace, and this workspace now holds two. The reasoning sits in the file
  so a future session does not "fix" it.
- Spring track now covers setup, Flyway (three lessons), beans, and the three
  layers. The `users` table finally has Java code reading it.
- Teaching decision: Spring Lesson 06 mentions `@Transactional` without
  explaining it, and flags that the transactions lesson is owed. Deliberate — the
  layers lesson needs the annotation present to be honest about where the
  transaction boundary sits.

## Session 5 (15 Sep 2026)

- The learner rejected the Playwright track's voice as "weirdly punchy" and asked
  for clarity and plain words. The cause was mine: I read the earlier "direct and
  authoritative" instruction as licence for short declarative fragments, dramatic
  openings and one-line pronouncements. Direct means stating the point plainly,
  not compressing it for effect.
- Rewrote both Playwright lessons. Measured before and after by counting prose
  sentences of six words or fewer: both fell from roughly twenty percent to under
  five. That count is a usable proxy for the problem and now sits in `CLAUDE.md`.
- The same measurement shows the Spring lessons run between fifteen and twenty-nine
  percent, so they carry the same fault. The learner named only the Playwright
  track, so I left them and reported the numbers instead of rewriting six files
  unasked.

## Session 6 (15 Sep 2026)

- The learner pointed at the stop-slop skill and asked for it to drive the style.
  Installed it verbatim at `.claude/skills/stop-slop/`, recorded its MIT licence,
  and made `CLAUDE.md` defer to it as the base rule set.
- Wrote `tools/stop-slop-check.py` so the rules are enforceable rather than a
  matter of my judgement. The workspace passes with zero findings.
- Four of the skill's rules conflict with technical writing and with what the
  learner asked for earlier. Adverbs that carry meaning, `never` as a precise
  absolute, Wh- openers in quiz stems, and enumerations longer than two items all
  stay. The reasoning sits in `CLAUDE.md` so nobody reverses it silently.
- Removed all 71 em dashes. Rewrote Spring lesson 01, which was the last file in
  the old conversational voice and the worst offender on every measure.
- Refined the rhythm check twice while building it. Counting every short sentence
  flagged plain imperatives such as "Use constructors.", which the learner asked
  for. The real defect is stacked short sentences, so the checker now fails on
  runs of two or more and reports the ratio as information only.

## Session 7 (15 Sep 2026)

- The learner flagged a third style fault: inflating importance. Two examples,
  both mine: "Section 04 explains why this setting matters more than the others"
  claims rank without saying anything, and "quietly reduces your whole CI run to
  a single test" dresses up a plain fact with intensifiers.
- Scanned the workspace rather than fixing only the two, and found thirteen. Most
  sat in the Playwright track and Spring lesson 01, which are the files I wrote
  most recently, so the habit is current rather than historic.
- Added an `inflation` category to the checker with a before-and-after table in
  `CLAUDE.md`. Literal scope statements stay: "starts the whole application
  context" describes what `@SpringBootTest` does.
- Pattern across sessions 5, 6 and 7: my drafts reach for emphasis when the plain
  statement would do. Directness, plain words and no inflation are three faces of
  the same correction.

## Session 8 (15 Sep 2026)

- The learner could not parse a sentence I wrote in session 7: "Section 04 covers
  what a trace contains and why this mode costs nothing while tests pass." They
  were right. "Mode" appears nowhere else in the lesson, "costs nothing" names no
  resource, and the bullet defers to a later section while its three neighbours
  explain themselves.
- Cause worth remembering: I fixed an inflated claim by deleting words rather
  than by replacing the claim with the mechanism. Compression is not the cure for
  inflation. Both leave the reader without the fact.
- Rewrote the bullet to define a trace at first mention, state what
  `on-first-retry` does on a pass and on a failure, and give the cost of the
  alternative in seconds and gigabytes. Found three more unquantified cost claims
  elsewhere and fixed those too.
- Added an `unexplained` category to the checker and an "Explain in place"
  section to `CLAUDE.md`.

## Session 9 (16 Sep 2026)

- Collated every style decision into `WRITING-STYLE.md` and cut the style section
  of `CLAUDE.md` down to a pointer plus a seven-line summary. `CLAUDE.md` went
  from about 190 lines to 116, which matters because it loads on every session
  while the style guide loads when someone writes prose.
- The guide keeps the worked examples rather than only the rules. The rules on
  their own read as platitudes; "Section 04 explains why this setting matters
  more than the others" next to its replacement does not.
- Added a final table mapping each correction the learner made to the rule it
  produced, so a future session can see intent rather than guessing at it.
- Extended the checker to read Markdown so the guide obeys its own rules. It
  skips fenced code, tables, blockquotes, headings and quoted phrases, because
  the guide quotes the wordings it bans. Checking the guide found four passives
  I had written into it.

