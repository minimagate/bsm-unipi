#!/usr/bin/env python3
"""Check that the math of a vault lecture note survives in its wiki lesson.

Usage:
  python3 scripts/check_math.py <vault_note.md> <wiki_lesson.md>
  python3 scripts/check_math.py --all [--vault PATH]

Extracts display math ($$...$$, may span lines) and inline math ($...$) from
both files, ignoring fenced code blocks. Each formula is normalised (whitespace
removed, \\, \\; \\! \\quad \\qquad and a backslash-space removed, trailing . , ; removed)
and the two files are compared as multisets:
  MISSING  formula in the vault note but not in the wiki lesson (fidelity problem)
  added    formula only in the wiki lesson (e.g. from an added example), only counted
Delimiter issues in the wiki lesson: odd number of "$$", or a line that is
exactly "\\]" or "\\[".

Exit status: 0 if no missing formula and no delimiter issue, 1 otherwise
(2 for an unusable vault in --all mode). Python standard library only.
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import import_status as st  # noqa: E402  (same folder: vault + pairing helpers)

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
DISPLAY_RE = re.compile(r"\$\$(.*?)\$\$", re.S)
INLINE_RE = re.compile(r"(?<!\\)\$([^$\n]+?)(?<!\\)\$")
SPACING_RE = re.compile(r"\\(qquad|quad|,|;|!| )")
TRAILING_PUNCT = ".,;"
MAX_SHOW = 120


def body_lines(text):
    """(lineno, line) for every line outside fenced code blocks."""
    out = []
    fence = None
    for no, line in enumerate(text.splitlines(), 1):
        m = FENCE_RE.match(line)
        if fence is None:
            if m:
                fence = m.group(1)
                continue
            out.append((no, line))
        elif m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and line.strip() == m.group(1):
            fence = None
    return out


def normalize(formula):
    s = SPACING_RE.sub("", formula)
    s = re.sub(r"\s+", "", s)
    return s.rstrip(TRAILING_PUNCT)


def extract(text):
    """List of (normalized, raw) formulas, in document order (display first, then inline)."""
    body = "\n".join(line for _, line in body_lines(text))
    raw = [m.group(1) for m in DISPLAY_RE.finditer(body)]
    rest = DISPLAY_RE.sub(" ", body)
    raw += [m.group(1) for m in INLINE_RE.finditer(rest)]
    result = []
    for r in raw:
        n = normalize(r)
        if n:
            result.append((n, " ".join(r.split())))
    return result


def delimiter_issues(text):
    lines = body_lines(text)
    issues = []
    count = "\n".join(line for _, line in lines).count("$$")
    if count % 2:
        issues.append(f"unbalanced $$ (found {count} occurrences)")
    for no, line in lines:
        if line.strip() in ("\\]", "\\["):
            issues.append(f"line {no}: stray '{line.strip()}' delimiter")
    return issues


def compare(vault_text, wiki_text):
    vault = extract(vault_text)
    wiki = extract(wiki_text)
    v_count = Counter(n for n, _ in vault)
    w_count = Counter(n for n, _ in wiki)
    raw_of = {}
    for n, r in vault:
        raw_of.setdefault(n, r)
    missing = [raw_of[n] for n in (v_count - w_count).elements()]
    return {
        "formulas": len(vault),
        "missing": missing,
        "added": sum((w_count - v_count).values()),
        "delimiters": delimiter_issues(wiki_text),
    }


def truncate(s):
    return s if len(s) <= MAX_SHOW else s[: MAX_SHOW - 3] + "..."


def has_issues(res):
    return bool(res["missing"] or res["delimiters"])


def report(vault_label, wiki_label, res):
    print(f"{vault_label}  vs  {wiki_label}")
    if not has_issues(res):
        print(f"  OK ({res['formulas']} formulas in vault note, {res['added']} added in lesson)")
        return
    for m in res["missing"]:
        print(f"  MISSING: {truncate(m)}")
    if res["added"]:
        print(f"  added in lesson: {res['added']}")
    for d in res["delimiters"]:
        print(f"  DELIMITER: {d}")


def read(path):
    return Path(path).read_text(encoding="utf-8", errors="replace")


def run_pair(vault_note, wiki_lesson):
    res = compare(read(vault_note), read(wiki_lesson))
    report(vault_note, wiki_lesson, res)
    return 1 if has_issues(res) else 0


def run_all(vault_arg):
    vault = st.resolve_vault(vault_arg)
    if not (vault / "Notes").is_dir():
        print(f"error: no Notes/ folder under vault {vault} (use --vault or BSM_VAULT)", file=sys.stderr)
        return 2
    notes = st.scan_vault(vault)
    lessons = st.scan_wiki()
    pairs, orphans = st.pair_lessons(notes, lessons)

    rows = []
    for vp, lesson in sorted(pairs.items(), key=lambda kv: kv[1]["path"]):
        res = compare(read(notes[vp]["path"]), read(lesson["path"]))
        rows.append((lesson["path"].relative_to(st.REPO).as_posix(), res))

    if not rows:
        print("No wiki lessons paired with a vault note.")
        return 0
    width = max(len(name) for name, _ in rows)
    print(f"{'file':<{width}}  missing  added  delimiters")
    for name, res in rows:
        print(f"{name:<{width}}  {len(res['missing']):>7}  {res['added']:>5}  {len(res['delimiters']):>10}")
    for name, res in rows:
        if has_issues(res):
            print()
            report(name, "", res)
    for lesson in orphans:
        print(f"skipped (no vault note): {lesson['path'].relative_to(st.REPO).as_posix()}")

    bad = [name for name, res in rows if has_issues(res)]
    print()
    if bad:
        print(f"{len(bad)} file(s) with missing formulas or delimiter issues.")
        return 1
    print("All paired lessons OK.")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="Compare math between a vault note and its wiki lesson.")
    parser.add_argument("vault_note", nargs="?", help="vault note (.md)")
    parser.add_argument("wiki_lesson", nargs="?", help="wiki lesson (.md)")
    parser.add_argument("--all", action="store_true", help="check every wiki lesson against its vault note")
    parser.add_argument("--vault", help="vault root for --all (default: $BSM_VAULT or the iCloud Obsidian path)")
    args = parser.parse_args(argv)

    if args.all:
        return run_all(args.vault)
    if not (args.vault_note and args.wiki_lesson):
        parser.error("give <vault_note.md> <wiki_lesson.md>, or --all")
    return run_pair(args.vault_note, args.wiki_lesson)


if __name__ == "__main__":
    sys.exit(main())
