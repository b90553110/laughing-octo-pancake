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
