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

