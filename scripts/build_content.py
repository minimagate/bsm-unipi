#!/usr/bin/env python3
"""Regenerate content/ from an Obsidian vault. Python standard library only.

Usage: python3 scripts/build_content.py <vault_root>

Reads <vault_root>/Notes/<Course>/**/*.md and writes Zola content into
<repo>/content/ (wiped first). Math, wikilinks and callouts are rewritten
into Zola-friendly markdown + HTML.
"""

import re
import shutil
import sys
import textwrap
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
NOTES_DIR = "Notes"

CALLOUT_LABELS = {
    "note": "Nota",
    "warning": "Attenzione",
    "important": "Importante",
    "tip": "Suggerimento",
}

FENCE_OPEN_RE = re.compile(r"^\s*(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")
DISPLAY_OWN_LINE_RE = re.compile(r"^([ \t]*)\$\$((?:(?!\$\$)[\s\S])*?)\$\$[ \t]*$", re.M)
DISPLAY_RE = re.compile(r"\$\$((?:(?!\$\$)[\s\S])*?)\$\$")
INLINE_MATH_RE = re.compile(r"(?<![\\$])\$(?![\s$])((?:\\.|[^$\\\n])*?)(?<![\s\\])\$")
WIKILINK_RE = re.compile(r"(!?)\[\[([^\[\]\n]+?)\]\]")
CALLOUT_RE = re.compile(r"^([ \t]*>[ \t]*)\[!([A-Za-z][\w-]*)\]([+-]?)[ \t]*(.*?)[ \t]*$")
H1_RE = re.compile(r"^#[ \t]+[^\n]*\n?", re.M)
TOKEN_RE = re.compile("(\\d+)")
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
STEM_DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\s+-\s+")

warnings = 0


def warn(msg):
    global warnings
    warnings += 1
    print(f"WARNING: {msg}", file=sys.stderr)


def slugify(text):
    text = unicodedata.normalize("NFKD", text)
    text = "".join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return text.strip("-")


def title_part(stem):
    return STEM_DATE_PREFIX_RE.sub("", stem)


# ---------------------------------------------------------------- frontmatter

def unquote(raw):
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] == "'":
        return raw[1:-1].replace("''", "'")
    if len(raw) >= 2 and raw[0] == raw[-1] == '"':
        escapes = {"n": "\n", "t": "\t", "r": "\r"}
        return re.sub(r"\\(.)", lambda m: escapes.get(m.group(1), m.group(1)), raw[1:-1])
    return raw


def parse_frontmatter(text):
    """Return (ordered dict of key -> str | list[str], body). Simple YAML only."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, text
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}, text
    data = {}
    key = None
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_][\w-]*):(?:\s+(.*))?$", line)
        if m and not line[:1].isspace():
            key = m.group(1)
            val = (m.group(2) or "").strip()
            data[key] = [] if val == "" else unquote(val)
            continue
        m = re.match(r"^\s*-\s+(.*)$", line)
        if m and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(unquote(m.group(1)))
    for k, v in data.items():
        if isinstance(v, list) and not v:
            data[k] = ""
    body = "\n".join(lines[end + 1:])
    return data, body


# ---------------------------------------------------------------- TOML output

def toml_str(s):
    out = []
    for ch in s:
        if ch == "\\":
            out.append("\\\\")
        elif ch == '"':
            out.append('\\"')
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\r":
            out.append("\\r")
        elif ch == "\t":
            out.append("\\t")
        elif ord(ch) < 0x20 or ord(ch) == 0x7F:
            out.append(f"\\u{ord(ch):04X}")
        else:
            out.append(ch)
    return '"' + "".join(out) + '"'


def toml_key(k):
    return k if re.fullmatch(r"[A-Za-z0-9_-]+", k) else toml_str(k)


def toml_value(v):
    if isinstance(v, list):
        return "[" + ", ".join(toml_str(x) for x in v) + "]"
    return toml_str(v)


# ---------------------------------------------------------------- body transforms

def math_span(tex, kind):
    esc = (
        tex.replace("&", "&amp;")
        .replace('"', "&quot;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "&#10;")
        .replace("{", "&#123;")
        .replace("}", "&#125;")
    )
    return f'<span class="math {kind}" data-tex="{esc}"></span>'


def split_fences(body):
    """Split body into [(is_code, text)] chunks; fenced blocks are code."""
    chunks, buf = [], []
    fence = None  # (char, length) while inside a fenced block
    for line in body.split("\n"):
        if fence is None:
            m = FENCE_OPEN_RE.match(line)
            if m:
                if buf:
                    chunks.append((False, "\n".join(buf)))
                    buf = []
                fence = (m.group(1)[0], len(m.group(1)))
            buf.append(line)
        else:
            buf.append(line)
            s = line.strip()
            if s and set(s) == {fence[0]} and len(s) >= fence[1]:
                chunks.append((True, "\n".join(buf)))
                buf = []
                fence = None
    if buf:
        chunks.append((fence is not None, "\n".join(buf)))
    return chunks


def convert_callouts(text):
    lines = text.split("\n")
    out = []
    for i, line in enumerate(lines):
        m = CALLOUT_RE.match(line)
        if not m:
            out.append(line)
            continue
        prefix, ctype, _fold, title = m.groups()
        ctype = ctype.lower()
        title = title or CALLOUT_LABELS.get(ctype, ctype.capitalize())
        out.append(f'{prefix}<span class="callout-title" data-type="{ctype}">{title}</span>')
        # Keep the body in its own paragraph: add an empty quote line after the title.
        if i + 1 < len(lines) and re.match(r"^[ \t]*>[ \t]*\S", lines[i + 1]):
            out.append(re.match(r"^([ \t]*>)", lines[i + 1]).group(1))
    return "\n".join(out)


def convert_wikilink(m, ctx, current, label):
    embed, inner = m.group(1), m.group(2)
    target, _, alias = inner.partition("|")
    alias = alias.strip() or None
    note_part, _, heading = target.partition("#")
    note_part = note_part.strip()
    heading = heading.strip()

    name = note_part.split("/")[-1].strip()
    if name.endswith(".md"):
        name = name[:-3]
    resolved = current if not name else ctx["stems"].get(name)

    if embed:
        warn(f"{label}: embed ![[{inner}]] rendered as plain text")
        return alias or title_part(name) or heading
    if resolved is None:
        warn(f"{label}: unresolved wikilink [[{inner}]]")
        return alias or title_part(name) or heading

    cslug, nslug, stem = resolved
    text = alias or title_part(stem)
    text = text.replace("[", "\\[").replace("]", "\\]")
    url = f"@/{cslug}/{nslug}.md"
    anchor = slugify(heading) if heading else ""
    if anchor:
        url += f"#{anchor}"
    return f"[{text}]({url})"


def restore(text, stash):
    while True:
        new = TOKEN_RE.sub(lambda m: stash[int(m.group(1))], text)
        if new == text:
            return text
        text = new


def convert_text(text, ctx, current, label):
    """Convert one non-code chunk. Generated HTML is stashed behind tokens so
    later passes (wikilinks, callouts) never touch it."""
    stash = []

    def hold(s):
        stash.append(s)
        return f"{len(stash) - 1}"

    text = INLINE_CODE_RE.sub(lambda m: hold(m.group(0)), text)

    def own_line(m):
        tex = textwrap.dedent(m.group(2)).strip()
        if not tex:
            return m.group(0)
        return m.group(1) + hold(math_span(tex, "display"))

    text = DISPLAY_OWN_LINE_RE.sub(own_line, text)

    def display(m):
        tex = m.group(1).strip()
        return hold(math_span(tex, "display")) if tex else m.group(0)

    text = DISPLAY_RE.sub(display, text)
    text = INLINE_MATH_RE.sub(lambda m: hold(math_span(m.group(1), "inline")), text)
    text = WIKILINK_RE.sub(lambda m: convert_wikilink(m, ctx, current, label), text)
    text = convert_callouts(text)
    return restore(text, stash)


def convert_body(body, ctx, current, label):
    out = []
    dropped_h1 = False
    for is_code, text in split_fences(body):
        if not is_code:
            if not dropped_h1:
                text, n = H1_RE.subn("", text, count=1)
                dropped_h1 = dropped_h1 or n > 0
            text = convert_text(text, ctx, current, label)
        out.append(text)
    return "\n".join(out).strip("\n") + "\n"


# ---------------------------------------------------------------- output

def note_page(title, date, extra, body):
    lines = ["+++", f"title = {toml_str(title)}"]
    if date:
        lines.append(f"date = {toml_str(date)}")
    lines += ["", "[extra]"]
    for k, v in extra.items():
        lines.append(f"{toml_key(k)} = {toml_value(v)}")
    lines.append("+++")
    return "\n".join(lines) + "\n\n" + body


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main(argv):
    if len(argv) != 2:
        print("usage: build_content.py <vault_root>", file=sys.stderr)
        return 2
    notes_root = Path(argv[1]).expanduser() / NOTES_DIR
    if not notes_root.is_dir():
        print(f"error: {notes_root} is not a directory", file=sys.stderr)
        return 1

    # Phase 1: collect every note so wikilinks can be resolved across courses.
    courses = []  # dicts: title, slug, notes
    stems = {}  # filename stem -> (course_slug, note_slug, stem)
    course_slugs = set()
    for course_dir in sorted(p for p in notes_root.iterdir() if p.is_dir() and not p.name.startswith(".")):
        files = sorted(p for p in course_dir.rglob("*.md") if not p.name.startswith("."))
        if not files:
            continue
        cslug = slugify(course_dir.name)
        if cslug in course_slugs:
            warn(f"duplicate course slug '{cslug}' for folder '{course_dir.name}'")
        course_slugs.add(cslug)

        used, notes = set(), []
        for f in files:
            stem = f.stem
            fm, body = parse_frontmatter(f.read_text(encoding="utf-8").replace("\r\n", "\n"))

            nslug = slugify(stem) or "note"
            base, n = nslug, 2
            while nslug in used:
                nslug, n = f"{base}-{n}", n + 1
            used.add(nslug)

            title = fm.get("title") or title_part(stem)
            if not isinstance(title, str):
                title = title_part(stem)

            date = ""
            fm_date = fm.get("date")
            if isinstance(fm_date, str) and DATE_RE.match(fm_date.strip()):
                date = DATE_RE.match(fm_date.strip()).group(1)
            elif DATE_RE.match(stem):
                date = DATE_RE.match(stem).group(1)
            if not date:
                warn(f"{f}: no date found")

            extra = {k: v for k, v in fm.items() if k not in ("title", "date")}

            if stem in stems:
                warn(f"duplicate note stem '{stem}' (wikilinks resolve to the first one)")
            else:
                stems[stem] = (cslug, nslug, stem)

            notes.append({"path": f, "stem": stem, "slug": nslug, "title": title,
                          "date": date, "extra": extra, "body": body})
        courses.append({"title": course_dir.name, "slug": cslug, "notes": notes})

    # Phase 2: wipe and write content/.
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir(parents=True)
    write(CONTENT / "_index.md",
          '+++\ntitle = "BSM · UniPi"\nsort_by = "none"\ntemplate = "index.html"\n+++\n')

    ctx = {"stems": stems}
    page_count = 0
    for course in courses:
        write(CONTENT / course["slug"] / "_index.md",
              f"+++\ntitle = {toml_str(course['title'])}\nsort_by = \"date\"\n"
              "template = \"section.html\"\npage_template = \"page.html\"\n+++\n")
        for note in course["notes"]:
            label = str(note["path"].relative_to(notes_root.parent))
            current = (course["slug"], note["slug"], note["stem"])
            body = convert_body(note["body"], ctx, current, label)
            write(CONTENT / course["slug"] / f"{note['slug']}.md",
                  note_page(note["title"], note["date"], note["extra"], body))
            page_count += 1

    print(f"courses: {len(courses)}")
    print(f"pages: {page_count}")
    print(f"warnings: {warnings}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
