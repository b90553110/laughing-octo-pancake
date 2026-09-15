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

## After generating material

`index.html` is the front door. It is static, so it cannot discover new files on
its own — whenever you add material, do all of these:

1. Write the file to its usual place (`lessons/0001-<slug>.html`,
   `reference/<slug>.html`, and so on).
2. Add a link to it in `index.html`, in `#lesson-list` or `#reference-list`.
   Newest lesson last. Use a relative `href` so links keep working under the
   `/laughing-octo-pancake/` path. One entry looks like:

   ```html
   <li>
     <a href="lessons/0001-german-cases.html">German cases: the accusative</a>
     <span class="meta">Lesson 1 · 2026-09-08</span>
   </li>
   ```
3. When `MISSION.md` is first written or changes, replace the placeholder text in
   the `#mission` section with a short summary of it.
4. Commit and push to `main`. Pages redeploys automatically, within a minute or
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

Every lesson and reference document follows these rules. They are not stylistic
preferences; the learner set them explicitly.

- **Active voice.** Name the actor. Write "Flyway applies the migration", not
  "the migration is applied". Scan drafts for "is/are/was/were + past participle"
  and rewrite each occurrence.
- **No ambiguous phrasing.** Replace "this", "that" and "it" with the noun they
  refer to whenever more than one referent is possible. State defaults, versions
  and artifact names exactly rather than describing them approximately.
- **No casual metaphors.** Drop analogies, jokes and figurative comparisons.
  Describe the mechanism directly. "Three annotations in a trench coat" is
  prohibited; "@SpringBootApplication combines three annotations" is correct.
- **Direct and authoritative.** Give the instruction, then the reason. Write
  "Add the starter" rather than "you might want to add the starter". Make
  recommendations as recommendations, and mark genuine uncertainty as uncertainty.
- **Technical precision over readability flourishes.** Quote exact error strings,
  exact property names and exact defaults. Verify each against the source — a jar,
  a POM, or official documentation — before publishing.

Lesson 01 predates these rules and still uses the older conversational voice.
Rewrite it when convenient; do not write anything new in that voice.

## The teach skill

`.claude/skills/teach/` is a verbatim copy of
`skills/productivity/teach` from <https://github.com/mattpocock/skills>
(commit `3cca18b`). Keep it verbatim so it can be re-synced from upstream;
put local conventions in this file instead. Its MIT license is recorded in
`THIRD-PARTY-LICENSES.md`.

It sets `disable-model-invocation: true`, so it only runs when explicitly asked:
`/teach <topic>`.
