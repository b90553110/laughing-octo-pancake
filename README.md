# laughing-octo-pancake

A learning workspace that publishes itself.

Claude Code generates lessons and reference material here using the
[`teach` skill](.claude/skills/teach/SKILL.md); GitHub Pages serves them at
<https://b90553110.github.io/laughing-octo-pancake/> so they are readable
anywhere, including on a phone.

## Using it

Open this repository in Claude Code (web, desktop or phone) and run:

```
/teach <what you want to learn>
```

The first run interviews you about *why* you want to learn the topic and writes
`MISSION.md`. After that, each run produces a lesson in `lessons/`, links it from
`index.html`, and pushes — the site updates about a minute later.

## Layout

| Path | Purpose |
| --- | --- |
| `index.html`, `style.css` | The published index page linking to all material |
| `.claude/skills/teach/` | The teach skill, picked up automatically by Claude Code |
| `CLAUDE.md` | Conventions Claude follows when adding material |
| `lessons/` | Generated lessons (HTML, one per topic) |
| `reference/` | Cheat sheets and glossaries, built to print well |
| `learning-records/` | What you have demonstrably learned, steering what comes next |
| `MISSION.md`, `RESOURCES.md`, `NOTES.md` | Workspace state written by the skill |
| `.nojekyll` | Tells Pages to serve files as-is, without Jekyll |

Only `index.html`, `style.css`, the skill and this README exist yet — the rest
appear as the skill creates them.

## Publishing on GitHub Pages

**Settings → Pages → Build and deployment → Source: Deploy from a branch**,
branch `main`, folder `/ (root)`, then **Save**.

## Previewing locally

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000>.

## Credits

The `teach` skill is a verbatim copy of `skills/productivity/teach` from
[mattpocock/skills](https://github.com/mattpocock/skills).

The `teach` skill is MIT licensed — see [THIRD-PARTY-LICENSES.md](THIRD-PARTY-LICENSES.md).
