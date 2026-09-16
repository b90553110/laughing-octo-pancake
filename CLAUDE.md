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

**Read [WRITING-STYLE.md](WRITING-STYLE.md) before writing or editing any lesson,
reference sheet or page.** It collects every style decision with the examples
that produced it, and it is the authority. The summary below exists so that a
session which has not opened it still avoids the worst mistakes.

Run the checker before every commit. It exits non-zero on any violation:

```sh
python3 tools/stop-slop-check.py --verbose
```

The seven rules, in short:

1. **Active voice.** Name the actor.
2. **Plain words, ordinary sentences.** Direct does not mean punchy. No
   fragments for emphasis, no one-line pronouncements.
3. **Do not inflate.** State what a thing does; let the reader judge importance.
4. **Explain in place.** Name the noun rather than "this mode". Quantify a cost
   or drop it. A cross-reference adds detail, it never carries the explanation.
5. **Technical precision.** Verify every version, default and error string
   against a jar, a POM, a registry or official docs. Say whether you ran the
   code.
6. **Rhythm.** Never stack short sentences. A single short imperative is fine.
7. **No em dashes.** Comma, colon or full stop.

Base rules come from the stop-slop skill at `.claude/skills/stop-slop/`.
`WRITING-STYLE.md` records four deliberate departures from it for technical
writing, covering adverbs, "never", Wh- openers in quiz stems, and enumerations
longer than two items. Do not reverse those without reading the reasoning.

## The teach skill

`.claude/skills/teach/` is a verbatim copy of
`skills/productivity/teach` from <https://github.com/mattpocock/skills>
(commit `3cca18b`). Keep it verbatim so it can be re-synced from upstream;
put local conventions in this file instead. Its MIT license is recorded in
`THIRD-PARTY-LICENSES.md`.

It sets `disable-model-invocation: true`, so it only runs when explicitly asked:
`/teach <topic>`.
