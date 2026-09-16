#!/usr/bin/env python3
"""Check published prose against the stop-slop skill in .claude/skills/stop-slop.

Reads the HTML in lessons/, reference/ and index.html, strips code blocks and
markup, and reports the patterns the skill bans. Carve-outs for technical
writing live in CLAUDE.md and are implemented here; see ALLOW_* below.

Usage:  python3 tools/stop-slop-check.py [--verbose]
Exit 1 when any violation remains.
"""
import glob, html as H, re, sys

VERBOSE = "--verbose" in sys.argv
INFO = {}

PHRASES = [
    "here's the thing", "here's what", "here's why", "here's how", "the uncomfortable truth",
    "it turns out", "let me be clear", "the truth is", "i'm going to be honest",
    "full stop.", "let that sink in", "this matters because", "make no mistake",
    "here's why that matters", "at its core", "in today's", "it's worth noting",
    "at the end of the day", "when it comes to", "in a world where", "the reality is",
    "plot twist", "spoiler:", "you already know this", "let me walk you through",
    "in this section", "as we'll see", "i want to explore", "take a step back",
    "moving forward", "circle back", "on the same page", "deep dive", "double down",
    "game-changer", "lean into", "unpack", "navigate the", "the landscape",
]
ADVERBS = ["really", "just ", "literally", "genuinely", "honestly", "simply", "actually",
           "deeply", "truly", "fundamentally", "inherently", "inevitably", "interestingly",
           "importantly", "crucially"]
BINARY = [r"\bnot because\b.{0,40}\bbut because\b", r"\bisn't the problem\b",
          r"\bthe answer isn't\b", r"\bthe question isn't\b",
          r"\bit's not\b[^.]{0,40}\bit's\b", r"\bisn't\b[^.]{0,30}\bit's\b",
          r"\bstops being\b.{0,30}\bstarts being\b", r"\bnot just\b.{0,30}\bbut also\b"]
AGENCY = [r"\bthe data tells\b", r"\bthe decision emerges\b", r"\bthe culture shifts\b",
          r"\bthe market rewards\b", r"\bthe conversation moves\b"]
EXTREMES = [r"\beveryone\b", r"\beverybody\b", r"\bnobody\b", r"\balways\b"]
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?(\w+ed|\w+en)\b", re.I)

# Claims of importance that name no specific. Say what the thing does and let
# the reader rank it. "This setting matters more than the others" tells the
# reader nothing; "this setting records a trace on the first retry" does.
INFLATION = [
    r"matters more than", r"more than the others", r"the most important",
    r"the single most", r"what matters most", r"the most valuable",
    r"most consequential", r"highest[- ]leverage", r"the most useful",
    r"the biggest", r"is what actually", r"the real \w+ is",
    r"accounts for most", r"worth more than", r"more than any(?:thing| other)",
    r"is everything", r"proves more than", r"deserves a closer look",
    r"a large share", r"the difficult one", r"the hard part",
    r"cannot be overstated", r"game[- ]changer", r"catastroph\w*",
    r"\bdisaster\b", r"career[- ]limiting", r"the key to \w+",
    r"your whole \w+", r"the whole point",
]

# Claims the reader cannot check, because the sentence never says what is being
# spent or what the pronoun points at. State the unit, or name the noun.
UNEXPLAINED = [
    r"costs? nothing", r"\bfor free\b", r"at no cost", r"without paying",
    r"\bthis mode\b", r"\bthat mode\b", r"\bthe mode\b",
    r"is cheap\b", r"being cheap\b", r"\bpretty fast\b", r"\bquite slow\b",
]

# Carve-outs recorded in CLAUDE.md. Technical writing needs these.
ALLOW_ADVERB_CONTEXT = ["concurrently", "automatically", "explicitly", "implicitly",
                        "independently", "transactionally", "quietly", "silently"]
ALLOW_PASSIVE = {"is disabled", "is enabled", "be visible", "be stable", "be present",
                 "be attached", "be applied", "is derived", "be skipped", "is shared",
                 "is managed", "be injected", "is generated", "be scoped", "be expressed", "is exactly", "be installed"}
# "never" is allowed: the migration rule is a precise absolute, not false authority.

def markdown_body(path):
    """Prose lines of a Markdown file.

    Skips fenced code, tables, blockquotes and headings. The style guide quotes
    the phrasings it bans inside tables and blockquotes, so counting those would
    flag the document for the examples it exists to warn about.
    """
    out, in_fence = [], False
    for line in open(path).read().split("\n"):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not stripped:
            continue
        if stripped[0] in "|>#":
            continue
        stripped = re.sub(r"`[^`]*`", "CODE", stripped)
        # A phrase in quotes is being discussed, not used. The guide quotes the
        # wordings it bans, so checking them would flag it for its own examples.
        stripped = re.sub(r'"[^"]*"', "QUOTED", stripped)
        out.append(stripped)
    return out


def prose_of(path):
    """All human-readable text, minus code."""
    if path.endswith(".md"):
        return re.sub(r"\s+", " ", " ".join(markdown_body(path)))
    raw = open(path).read()
    body = re.sub(r"<pre>.*?</pre>", " ", raw, flags=re.S)
    body = re.sub(r"<code>.*?</code>", " CODE ", body, flags=re.S)
    text = H.unescape(re.sub(r"<[^>]+>", " ", body))
    return re.sub(r"\s+", " ", text)

def body_paragraphs(path):
    """Only <p> prose (or Markdown prose lines). Excludes tables, list items, labels and metadata lines,
    which are telegraphic by design and must not count as fragmentation."""
    if path.endswith(".md"):
        return markdown_body(path)
    raw = open(path).read()
    body = re.sub(r"<pre>.*?</pre>", " ", raw, flags=re.S)
    body = re.sub(r"<table.*?</table>", " ", body, flags=re.S)
    # Inline code often contains "!" or "." and would split sentences wrongly.
    body = re.sub(r"<code>.*?</code>", "CODE", body, flags=re.S)
    out = []
    for m in re.finditer(r"<p(?: class=\"(?:why|section-note)\")?>(.*?)</p>", body, re.S):
        t = H.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))
        out.append(re.sub(r"\s+", " ", t).strip())
    return [t for t in out if t]

def sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?]) ", text) if s.strip()]

def check(path):
    text = prose_of(path)
    low = text.lower()
    found = {}

    n = text.count("—")
    if n: found["em-dash"] = [f"{n} occurrences"]

    hits = [p for p in PHRASES if p in low]
    if hits: found["banned-phrase"] = hits

    adv = []
    for a in ADVERBS:
        for m in re.finditer(re.escape(a), low):
            ctx = low[max(0, m.start()-40):m.end()+40]
            if not any(w in ctx for w in ALLOW_ADVERB_CONTEXT):
                adv.append(a.strip())
    if adv: found["adverb"] = sorted(set(adv))

    for name, pats in (("binary-contrast", BINARY), ("false-agency", AGENCY),
                       ("lazy-extreme", EXTREMES), ("inflation", INFLATION),
                       ("unexplained", UNEXPLAINED)):
        hits = [m.group(0) for p in pats for m in re.finditer(p, low)]
        if hits: found[name] = sorted(set(hits))

    # Words ending in -en/-ed that are not participles.
    NOT_PARTICIPLE = {"when", "then", "often", "even", "open", "seen", "oven",
                      "green", "between", "hidden", "wooden", "need", "indeed"}
    pas = [m.group(0) for m in PASSIVE.finditer(text)
           if m.group(0).lower() not in ALLOW_PASSIVE
           and m.group(2).lower() not in NOT_PARTICIPLE]
    if pas: found["passive"] = sorted(set(pas))

    # Dramatic fragmentation. The skill bans STACKED short sentences, so the
    # check looks for runs of two or more, not for every short sentence.
    # Exempt: sentences ending in a colon (lead-ins to a code block or list),
    # and reference sheets, which are telegraphic by design.
    if not path.startswith("reference/") and not path.endswith(".md"):
        runs, ratio_hits, total = [], 0, 0
        for para in body_paragraphs(path):
            sents = [s for s in sentences(para) if not s.rstrip().endswith(":")]
            total += len(sents)
            run = []
            for s in sents:
                if 0 < len(s.split()) <= 6:
                    run.append(s); ratio_hits += 1
                else:
                    if len(run) >= 2: runs.append(" / ".join(run))
                    run = []
            if len(run) >= 2: runs.append(" / ".join(run))
        if runs:
            found["staccato"] = runs
        # Informational only. Stacked short sentences are the defect; a plain
        # short imperative ("Use constructors.") is the directness the learner
        # asked for. Reported so drift stays visible, not counted as a failure.
        if total:
            INFO[path] = f"{ratio_hits}/{total} = {ratio_hits/total:.0%}"

    return found

def main():
    files = sorted(glob.glob("lessons/**/*.html", recursive=True)) \
          + sorted(glob.glob("reference/*.html")) + ["index.html", "WRITING-STYLE.md"]
    total = 0
    for f in files:
        found = check(f)
        count = sum(len(v) for v in found.values())
        total += count
        status = "clean" if not found else ", ".join(f"{k}({len(v)})" for k, v in found.items())
        ratio = f"  [short sentences {INFO[f]}]" if f in INFO else ""
        print(f"  {f:56} {status}{ratio}")
        if VERBOSE and found:
            for k, v in found.items():
                print(f"       {k}: {v[:6]}")
    print(f"\n  total findings: {total}")
    return 1 if total else 0

if __name__ == "__main__":
    sys.exit(main())
