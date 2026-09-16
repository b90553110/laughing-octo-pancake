# Writing style

Read this before writing or editing any lesson, reference sheet or page in this
repository. It collects every style decision made so far, with the examples that
produced each one.

Run the checker before every commit:

```sh
python3 tools/stop-slop-check.py --verbose
```

It exits non-zero on any violation and passes on the current workspace.

## Where the rules come from

The base rules are the **stop-slop** skill at `.claude/skills/stop-slop/`, a
verbatim copy of <https://github.com/hardikpandya/stop-slop> (MIT, recorded in
`THIRD-PARTY-LICENSES.md`). Read its `SKILL.md` and the three files under
`references/` for the full treatment of banned phrases, structural cliches,
false agency and rhythm.

Everything below either applies those rules to technical writing, or departs
from them on purpose. Each departure carries its reasoning.

## The seven rules

### 1. Active voice

Name the actor. Scan drafts for "is/are/was/were" followed by a past participle
and rewrite each one.

| Instead of | Write |
|---|---|
| "the migration is applied" | "Flyway applies the migration" |
| "the file is quietly rewritten" | "Flyway rewrites the file" |
| "Nothing has been applied and nothing is corrupted" | "It applied nothing and corrupted nothing" |

### 2. Plain words, ordinary sentences

Direct does not mean punchy. Write complete sentences of ordinary length, joined
by the words that carry the reasoning: because, so, which means, rather than.
Prefer the plain word over the vivid one.

| Instead of | Write |
|---|---|
| "Most end-to-end suites die the same way" | "End-to-end suites usually become unusable in the same way" |
| "the highest-leverage decision" | "the decision that determines whether the suite survives" |
| "Spend them deliberately." | "It is worth being selective about what you cover with them." |

Four constructions to avoid:

- **Fragments used for emphasis.** "No waits. No sleeps. No CSS selectors."
  Write "There are no explicit waits, no sleeps and no CSS selectors."
- **One-line paragraphs that pronounce.** Explain what to do and why in a normal
  sentence.
- **Dramatic framing.** "That clause is the whole difficulty" overstates.
- **Build-up before the point.** Say the thing, then explain it.

### 3. Do not inflate

State what a thing does and let the reader judge its importance. Ranking claims
carry no information.

| Instead of | Write |
|---|---|
| "Section 04 explains why this setting matters more than the others." | "Section 04 covers what a trace contains." |
| "the most useful tool available when a test fails in CI" | "Open it when a test fails only in CI." |
| "This is the most consequential decision in the track." | Cut it. The sentence before already says what the decision controls. |
| "responsible for a large share of flaky tests" | "A test written this way passes or fails depending on how quickly the page renders." |
| "That inversion accounts for most of the framework." | "Spring is built around that inversion, and its other features assume it." |
| "This single check proves more than the other two combined." | "This check runs the SQL rather than inspecting filenames, so it catches errors the other two cannot see." |

Describe consequences without intensifiers:

| Instead of | Write |
|---|---|
| "quietly reduces your whole CI run to a single test" | "CI runs that one test and skips the rest." |
| "the silence makes this expensive to diagnose" | "the missing tables are the only symptom, which sends people to check their migration files long before their dependencies" |

A literal scope statement is not inflation. "Starts the whole application
context" describes what `@SpringBootTest` does, so it stays.

### 4. Explain in place

Removing an inflated claim does not mean compressing the sentence. Compression
produced this, which the learner could not parse:

> "Section 04 covers what a trace contains and why this mode costs nothing while
> tests pass."

Three faults sit in one sentence. The lesson never introduces the word "mode",
so the referent is missing. "Costs nothing" names no resource, so there is no
claim to check. The bullet defers to a later section while the three bullets
around it explain themselves.

- **Name the noun.** Write "the value `'on-first-retry'`", not "this mode". A
  demonstrative works only when its referent sits in the same sentence.
- **Quantify a cost or drop it.** "Saving a trace for every run adds seconds to
  each test and produces files that reach gigabytes" gives the reader a number to
  disagree with.
- **Explain where the reader is.** A bullet that introduces a setting says what
  the setting does, in that bullet. Cross-references add detail for someone who
  wants more; they never carry the explanation.

### 5. Technical precision

Quote exact error strings, property names and defaults, and verify each against
a source before publishing: a jar, a POM, the npm registry, or official
documentation. Two corrections from this workspace show why:

- Spring Boot sets `spring.flyway.clean-disabled` to `true`, the opposite of
  what several web articles claim. Read `FlywayProperties.java` in the Boot
  sources jar.
- Flyway's checksum-mismatch output follows the template
  `Migration %s mismatch for migration %s`. An earlier lesson quoted two
  advisory lines that Flyway never prints.

Say whether you ran the code. The meta line of each lesson carries either
"I ran every command below end to end" or "I did not execute this code."

### 6. Rhythm

The defect is **stacked** short sentences, which read as manufactured emphasis.
The checker fails any run of two or more consecutive sentences of six words or
fewer, ignoring lead-ins that end in a colon.

A single short imperative is correct and often best. "Use constructors." is the
directness the learner asked for.

The checker also reports a short-sentence ratio per file and does not fail on
it, because ordinary imperatives raise the number without making prose clipped.
Treat it as drift detection. The Playwright lessons sit near five percent, the
Spring lessons between eight and twenty-three.

### 7. No em dashes

Removed from the workspace. Use a comma for an aside, a colon before a
definition or a list, and a full stop between two complete thoughts.

## Carve-outs for technical writing

stop-slop targets essays. Four of its rules damage technical documentation, so
this workspace departs from them. Do not reverse these.

| stop-slop says | This workspace does | Why |
|---|---|---|
| Remove all adverbs | Keep adverbs that carry technical meaning | `CREATE INDEX CONCURRENTLY` is a SQL keyword. "Injects automatically" and "fails silently" each state a fact. The checker still bans really, just, simply, actually, genuinely, honestly, literally, truly, deeply, fundamentally. |
| "Never" and "always" are lazy extremes | `never` stays, `always` goes | "Never modify a migration that has run elsewhere" is a precise absolute. `everyone`, `everybody`, `nobody` and `always` stay banned because they hide the actor. |
| No Wh- sentence openers | Quiz stems stay as questions | A quiz stem has to ask something. Avoid Wh- openers in body prose. |
| Two items beat three | List however many exist | Spring has three layers. An enumeration reports a fact rather than building a rhetorical triad. |

Reference sheets are exempt from the rhythm checks. A cheat sheet is
telegraphic on purpose.

## Quizzes

- Every option in a question carries the **same number of words**, with
  character counts as close as practical, so formatting leaks no clue.
- Vary which index holds the correct answer across the questions in a lesson.
  Three questions answered by the first option is its own tell.
- Each question needs a `<p class="why" hidden>` explaining the answer.
- Verify both rules mechanically before committing. Counting words by eye fails.

## Lesson anatomy

Lessons follow one shape, which `assets/lesson.css` styles:

1. `masthead` with breadcrumb, title, standfirst, and a meta line carrying
   versions and whether you ran the code.
2. Numbered `<h2>` sections, each with a `<span class="num">`.
3. `note` callouts for recommendations, constraints and traps. `note plain` for
   asides.
4. `task` blocks for "Do this" steps.
5. A quiz.
6. A "Read this next" section naming one primary source.
7. An "Ask me" note inviting follow-up questions.
8. Numbered sources with anchors, cited from the body by superscript.

## The checker

`tools/stop-slop-check.py` strips code and markup, then reports:

| Category | Catches |
|---|---|
| `em-dash` | Any em dash |
| `banned-phrase` | Throat-clearing openers, emphasis crutches, business jargon, meta-commentary |
| `adverb` | The empty adverbs, with context allowances for the technical ones |
| `binary-contrast` | "Not X, it's Y" and its variants |
| `false-agency` | Inanimate subjects doing human verbs |
| `lazy-extreme` | everyone, everybody, nobody, always |
| `passive` | Passive constructions, minus an allow-list and non-participles |
| `inflation` | Ranking claims and vague magnitude |
| `unexplained` | Unquantified cost claims, and "this mode" dangling referents |
| `staccato` | Runs of two or more short sentences |

The allow-lists implement the carve-outs above. When a finding turns out to be a
false positive, fix the checker rather than the prose, and say so.

## Pre-publish checklist

1. Run `python3 tools/stop-slop-check.py --verbose` and reach zero findings.
2. Verify every relative link resolves on disk.
3. Confirm quiz options match on word count and that answer indices vary.
4. Check code blocks are narrow enough to read on a phone, roughly 72 characters.
5. Confirm every version, default and error string came from a source you read.
6. Say in the meta line whether you ran the code.

## How these rules arrived

Each rule replaced a habit the learner had to correct, and the sequence matters
for understanding the intent.

| Correction | Rule it produced |
|---|---|
| "Avoid passive voice, prioritise clarity and technical precision, adopt a direct authoritative tone" | Rules 1 and 5 |
| "The Playwright track is weirdly punchy, I prefer clarity and plain words" | Rule 2 |
| "Use stop-slop to change style" | The base rules, the carve-outs, and the checker |
| "There's another issue, making things sound overly impactful" | Rule 3 |
| "I don't understand what this means, it's compressed and doesn't make sense" | Rule 4 |

Rules 2, 3 and 4 are one fault seen from three angles: reaching for emphasis
when the plain statement carries more. Watch for it in first drafts.
