# Repository conventions

This repository is two things at once:

1. A **teaching workspace** for the `teach` skill (`.claude/skills/teach/`).
2. A **GitHub Pages site** that publishes what the skill produces, so it is
   readable on a phone at
   <https://b90553110.github.io/laughing-octo-pancake/>.

The repository root *is* the teaching workspace root, so the paths in
`.claude/skills/teach/SKILL.md` (`MISSION.md`, `RESOURCES.md`, `GLOSSARY.md`,
`NOTES.md`, `lessons/`, `reference/`, `learning-records/`, `assets/`) all live at
the root and are served directly by Pages.

## Tracks

Lessons belong to a **track**: one subject, numbered independently, read in order.
Each track owns a directory under `lessons/`:

```
lessons/spring/0001-...html      Spring Boot, Maven, Flyway, JPA
lessons/playwright/0001-...html  Playwright end-to-end tests (TypeScript, Angular)
```

Numbering restarts per track, so "Spring lesson 5" and "Playwright lesson 1" are
both unambiguous. Reference sheets stay flat in `reference/` and take a subject
name (`flyway-cheatsheet.html`, `playwright-cheatsheet.html`).

Lessons sit two directories deep, so their links to shared assets use `../../`:
`../../assets/lesson.css`, `../../index.html`, `../../reference/<sheet>.html`.
Links between lessons in the same track stay bare (`0002-....html`).

To add a track: create `lessons/<track>/`, add a `<section>` for it in
`index.html` with its own `<ol class="list">`, and add a mission section to
`MISSION.md`.

## After generating material

`index.html` is the front door. It is static, so it cannot discover new files on
its own — whenever you add material, do all of these:

1. Write the file into its track (`lessons/<track>/000N-<slug>.html`) or, for a
   reference sheet, into `reference/<slug>.html`.
2. Add a link to it in `index.html`, inside that track's `<ol>` or the reference
   `<ul>`. Newest lesson last. Use a relative `href` so links keep working under
   the `/laughing-octo-pancake/` path. One entry looks like:

   ```html
   <li>
     <a href="lessons/spring/0007-transactions.html">Transactions</a>
     <span class="meta">Lesson 7 · ~20 min · the proxy self-invocation trap</span>
   </li>
   ```
3. Update the track's "Queued:" note in `index.html` when the plan changes, and
   the track's section in `MISSION.md` when its goal changes.
4. Verify every relative link resolves on disk before committing. Moving a lesson
   between directories breaks `../` paths silently.
5. Commit and push to `main`. Pages redeploys automatically, within a minute or
   so.

Material that is prose-only (`MISSION.md`, `learning-records/*.md`) does not need
a link — it is read in the repository, not on the site.

## Site conventions

- No build step, no frameworks, no external requests. Plain HTML and CSS.
- Shared lesson styling belongs in `assets/` as the skill describes; `style.css`
  is for this index page only.
- Colours come from the CSS variables at the top of `style.css`, which have light
  and dark values. Reuse them rather than hard-coding colours.
- `.nojekyll` is deliberate: it stops Pages running Jekyll, so files under
  directories like `assets/` are served exactly as committed.

## Writing style for lessons

The base rules come from the **stop-slop** skill in `.claude/skills/stop-slop/`,
a verbatim copy of <https://github.com/hardikpandya/stop-slop>. Read
`SKILL.md` and its three reference files before writing prose. They cover banned
phrases, structural cliches, false agency, passive voice and rhythm.

`tools/stop-slop-check.py` enforces the machine-checkable parts across
`lessons/`, `reference/` and `index.html`. Run it before every commit:

```
python3 tools/stop-slop-check.py --verbose
```

It exits non-zero on any violation. The whole workspace passes as of this
writing.

### Carve-outs for technical writing

stop-slop targets essays. Four of its rules damage technical documentation, so
this workspace departs from them deliberately. Do not "fix" these.

- **Adverbs.** stop-slop says remove all of them. Keep the ones that carry
  technical meaning: `CREATE INDEX CONCURRENTLY` is a SQL keyword, and
  "Spring injects that constructor automatically", "fails silently" and "runs
  transactionally" each state a fact that costs a clause to say otherwise. The
  checker still bans the empty ones: really, just, simply, actually, genuinely,
  honestly, literally, truly, deeply, fundamentally.
- **"Never" and "always".** stop-slop calls these lazy extremes. "Never modify a
  migration that has run elsewhere" is a precise absolute, not false authority,
  so `never` stays allowed. `everyone`, `everybody`, `nobody` and `always` remain
  banned, because they hide the actor.
- **Wh- sentence openers.** stop-slop bans them. Quiz stems must be questions
  ("What does Flyway store in the history table?"), so the checker does not test
  for this. Avoid Wh- openers in body prose.
- **Three-item lists.** stop-slop prefers two. A technical enumeration reports
  a fact: Spring Boot has three layers and Flyway has three per-database module
  naming patterns, so list however many exist. The rule applies to rhetorical
  triads in prose, not to enumerations.

Reference sheets are exempt from the sentence-rhythm checks. A cheat sheet is
telegraphic on purpose.

### Rhythm

The defect to avoid is **stacked** short sentences, which read as manufactured
emphasis: "No waits. No sleeps. No CSS selectors." The checker fails any run of
two or more consecutive sentences of six words or fewer, excluding lead-ins that
end in a colon.

A single short imperative is fine and often correct. "Use constructors." is the
directness the learner asked for.

The checker also reports a short-sentence ratio per file. It does not fail on
that number, because ordinary imperatives push it up without making the prose
clipped. Treat it as drift detection. The Playwright lessons sit near five
percent and the Spring lessons between eight and twenty-three.

### Em dashes

Removed from the workspace entirely, per stop-slop. Use a comma for an aside, a
colon before a definition or a list, and a full stop between two complete
thoughts.

## The teach skill

`.claude/skills/teach/` is a verbatim copy of
`skills/productivity/teach` from <https://github.com/mattpocock/skills>
(commit `3cca18b`). Keep it verbatim so it can be re-synced from upstream;
put local conventions in this file instead. Its MIT license is recorded in
`THIRD-PARTY-LICENSES.md`.

It sets `disable-model-invocation: true`, so it only runs when explicitly asked:
`/teach <topic>`.
