#!/usr/bin/env python3
"""Regenerate the Zola site sources from notes/. Python standard library only.

Usage: python3 scripts/build_content.py [--strict]

Reads:
  notes/<Course>/**/*.md   lecture notes ("lezioni"), one per file
  notes/Voci/*.md          concept articles ("voci")
Top-level files in notes/ (such as _voci.md) are ignored.

Writes (wiped first, generated, gitignored):
  content/<course-slug>/_index.md and content/<course-slug>/<lesson-slug>.md
  content/voci/_index.md and content/voci/<voce-slug>.md
  content/_index.md          home page data (recent lessons, counts)
  static/search.json         client-side search index

Math, wikilinks and callouts are rewritten into Zola-friendly markdown. Wikilinks
are resolved across courses and voci: lesson links by filename stem only, voce
links by filename stem, title or alias. Backlinks and "voci in this lesson"
lists are stored in [extra] for the templates.

--strict makes the script exit with status 1 when any warning was emitted.
"""

import argparse
import html
import json
import re
import shutil
import sys
import textwrap
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTENT = REPO / "content"
SEARCH_INDEX = REPO / "static" / "search.json"
DEFAULT_NOTES = REPO / "notes"
VOCI_DIR = "Voci"
VOCI_SECTION = "voci"
RECENT_COUNT = 8

CALLOUT_LABELS = {
    "note": "Nota",
    "warning": "Attenzione",
    "important": "Importante",
    "tip": "Suggerimento",
    "example": "Esempio",
}

FENCE_OPEN_RE = re.compile(r"^\s*(`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(`+)(.+?)\1")
DISPLAY_OWN_LINE_RE = re.compile(r"^([ \t]*)\$\$((?:(?!\$\$)[\s\S])*?)\$\$[ \t]*$", re.M)
DISPLAY_RE = re.compile(r"\$\$((?:(?!\$\$)[\s\S])*?)\$\$")
INLINE_MATH_RE = re.compile(r"(?<![\\$])\$(?![\s$])((?:\\.|[^$\\\n])*?)(?<![\s\\])\$")
WIKILINK_RE = re.compile(r"(!?)\[\[([^\[\]\n]+?)\]\]")
CALLOUT_RE = re.compile(r"^([ \t]*>[ \t]*)\[!([A-Za-z][\w-]*)\]([+-]?)[ \t]*(.*?)[ \t]*$")
H1_RE = re.compile(r"^#[ \t]+[^\n]*\n?", re.M)
TOKEN_RE = re.compile("\ue000(\\d+)\ue001")  # stash placeholders, never present in notes
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
STEM_DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\s+-\s+")
SLUG_DATE_PREFIX_RE = re.compile(r"^\d{4}-\d{2}-\d{2}-")

warnings = 0


def warn(msg):
    global warnings
    warnings += 1
    print(f"WARNING: {msg}", file=sys.stderr)


def slugify(text):
    text = strip_accents(text)
    text = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return text.strip("-")


def strip_accents(text):
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c))


def fold(text):
    """Loose key for matching link targets: no accents, lower case, single spaces."""
    return re.sub(r"\s+", " ", strip_accents(text)).strip().lower()


def title_part(stem):
    return STEM_DATE_PREFIX_RE.sub("", stem)


def zola_slug(file_slug):
    """The slug Zola derives from a content filename: a leading YYYY-MM-DD- is dropped."""
    return SLUG_DATE_PREFIX_RE.sub("", file_slug, count=1) or file_slug


def unique(base, used):
    """Return base, or base-2, base-3, ... the first one not in used; records it."""
    slug, n = base, 2
    while slug in used:
        slug, n = f"{base}-{n}", n + 1
    used.add(slug)
    return slug


def as_list(value):
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return [v for v in value if v]
    return [value]


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
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, (list, tuple)):
        return "[" + ", ".join(toml_value(x) for x in v) + "]"
    return toml_str(str(v))


def front_matter(top, extra=None):
    """top: ordered (key, value) pairs; extra: rendered into the [extra] table."""
    lines = ["+++"]
    for k, v in top:
        if v is not None and v != "":
            lines.append(f"{toml_key(k)} = {toml_value(v)}")
    if extra:
        lines += ["", "[extra]"]
        for k, v in extra.items():
            lines.append(f"{toml_key(k)} = {toml_value(v)}")
    lines.append("+++")
    return "\n".join(lines) + "\n"


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
        out.append(f'{prefix}<span class="callout-title" data-type="{ctype}">{html.escape(title)}</span>')
        # Keep the body in its own paragraph: add an empty quote line after the title.
        if i + 1 < len(lines) and re.match(r"^[ \t]*>[ \t]*\S", lines[i + 1]):
            out.append(re.match(r"^([ \t]*>)", lines[i + 1]).group(1))
    return "\n".join(out)


class Registry:
    """Maps link keys (filename stems, voce titles, voce aliases) to targets."""

    def __init__(self):
        self.exact = {}
        self.folded = {}

    def add(self, key, target, label):
        key = key.strip()
        if not key:
            return
        if key in self.exact:
            if self.exact[key]["path"] != target["path"]:
                warn(f"{label}: '{key}' already points to {self.exact[key]['path']}, ignored for {target['path']}")
            return
        self.exact[key] = target
        self.folded.setdefault(fold(key), target)

    def get(self, key):
        return self.exact.get(key) or self.folded.get(fold(key))


def convert_wikilink(m, reg, src, label, refs):
    embed, inner = m.group(1), m.group(2)
    target, _, alias = inner.partition("|")
    alias = alias.strip() or None
    note_part, _, heading = target.partition("#")
    note_part = note_part.strip()
    heading = heading.strip()

    name = note_part.split("/")[-1].strip()
    if name.endswith(".md"):
        name = name[:-3]

    if embed:
        warn(f"{label}: embed ![[{inner}]] rendered as plain text")
        return alias or title_part(name) or heading

    resolved = reg.get(name) if name else None
    if resolved is None:
        warn(f"{label}: unresolved wikilink [[{inner}]]")
        return alias or title_part(name) or heading

    if resolved["kind"] == "voce" and resolved["path"] != src["path"]:
        refs.setdefault(src["path"], {})[resolved["path"]] = None

    if resolved["kind"] == "voce":
        text = alias or name
    else:
        text = alias or resolved["text"]
    text = text.replace("[", "\\[").replace("]", "\\]")
    url = f"@/{resolved['path']}"
    # Zola drops inline math from heading ids, so strip stash tokens and $...$ spans first.
    anchor_text = TOKEN_RE.sub("", heading)
    anchor_text = re.sub(r"\$[^$]*\$", "", anchor_text)
    anchor = slugify(anchor_text) if heading else ""
    if anchor:
        url += f"#{anchor}"
    return f"[{text}]({url})"


def restore(text, stash):
    while True:
        new = TOKEN_RE.sub(lambda m: stash[int(m.group(1))], text)
        if new == text:
            return text
        text = new


def convert_text(text, reg, src, label, refs):
    """Convert one non-code chunk. Generated HTML is stashed behind tokens so
    later passes (wikilinks, callouts) never touch it."""
    stash = []

    def hold(s):
        stash.append(s)
        return f"\ue000{len(stash) - 1}\ue001"

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
    text = WIKILINK_RE.sub(lambda m: convert_wikilink(m, reg, src, label, refs), text)
    text = convert_callouts(text)
    return restore(text, stash)


def convert_body(body, reg, src, label, refs):
    out = []
    dropped_h1 = False
    for is_code, text in split_fences(body):
        if not is_code:
            if not dropped_h1:
                text, n = H1_RE.subn("", text, count=1)
                dropped_h1 = dropped_h1 or n > 0
            text = convert_text(text, reg, src, label, refs)
        out.append(text)
    return "\n".join(out).strip("\n") + "\n"


# ---------------------------------------------------------------- collection

def read_note(path):
    return parse_frontmatter(path.read_text(encoding="utf-8").replace("\r\n", "\n"))


def load_lessons(notes_root, reg, courses):
    """Lesson records, one per file under notes/<Course>/. Registers their stems."""
    lessons = []
    course_slugs = set()
    for course_dir in sorted(notes_root.iterdir()):
        if not course_dir.is_dir() or course_dir.name.startswith(".") or course_dir.name == VOCI_DIR:
            continue
        files = sorted(p for p in course_dir.rglob("*.md") if not p.name.startswith("."))
        if not files:
            continue
        cslug = slugify(course_dir.name) or "corso"
        if cslug in course_slugs:
            warn(f"duplicate course slug '{cslug}' for folder '{course_dir.name}'")
        course_slugs.add(cslug)
        course = {"title": course_dir.name, "slug": cslug, "lessons": []}
        courses.append(course)

        used = set()         # content file slugs (unique file names)
        used_public = set()  # URL slugs, as Zola derives them (date stripped)
        for f in files:
            stem = f.stem
            label = str(f.relative_to(notes_root.parent))
            fm, body = read_note(f)

            nslug = unique(slugify(stem) or "lezione", used)
            pslug = unique(zola_slug(nslug), used_public)

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
                warn(f"{label}: no date found")

            extra = {k: v for k, v in fm.items() if k not in ("title", "date")}
            lesson = {
                "course": course, "stem": stem, "title": title, "date": date,
                "extra": extra, "body": body, "label": label,
                "path": f"{cslug}/{nslug}.md",
                "slug": pslug, "url": f"{cslug}/{pslug}/",
                "kind": "lesson",
            }
            course["lessons"].append(lesson)
            lessons.append(lesson)
            reg.add(stem, {"kind": "lesson", "path": lesson["path"], "text": title_part(stem)}, label)
    return lessons


def load_voci(notes_root, reg, course_titles):
    voci_dir = notes_root / VOCI_DIR
    voci = []
    if not voci_dir.is_dir():
        return voci
    used = set()
    used_public = set()
    for f in sorted(p for p in voci_dir.glob("*.md") if not p.name.startswith(".")):
        label = str(f.relative_to(notes_root.parent))
        fm, body = read_note(f)
        stem = f.stem
        slug = unique(slugify(stem) or "voce", used)
        pslug = unique(zola_slug(slug), used_public)

        title = fm.get("title") if isinstance(fm.get("title"), str) and fm.get("title") else stem
        sintesi = fm.get("sintesi") if isinstance(fm.get("sintesi"), str) else ""
        if not sintesi:
            warn(f"{label}: missing sintesi")
        corsi = as_list(fm.get("corsi"))
        alias = as_list(fm.get("alias"))
        for c in corsi:
            if c not in course_titles:
                warn(f"{label}: corsi lists '{c}', which has no notes/ folder")

        extra = {k: v for k, v in fm.items() if k not in ("title", "sintesi")}
        if not extra.get("categoria"):
            warn(f"{label}: missing categoria")
        extra["corsi"] = corsi
        extra["alias"] = alias
        letter = slugify(title)[:1].upper()
        extra["letter"] = letter if letter.isalpha() else "#"

        voce = {
            "title": title, "slug": pslug, "stem": stem, "sintesi": sintesi, "extra": extra,
            "body": body, "label": label, "path": f"{VOCI_SECTION}/{slug}.md",
            "url": f"{VOCI_SECTION}/{pslug}/", "kind": "voce",
            "corsi": corsi, "alias": alias, "letter": extra["letter"],
            "introdotta": fm.get("introdotta_in", "") if isinstance(fm.get("introdotta_in"), str) else "",
        }
        voci.append(voce)
        reg.add(title, {"kind": "voce", "path": voce["path"], "text": title}, label)
        reg.add(stem, {"kind": "voce", "path": voce["path"], "text": title}, label)
        for a in alias:
            reg.add(a, {"kind": "voce", "path": voce["path"], "text": a}, label)
    return voci


# ---------------------------------------------------------------- main

def main(argv):
    parser = argparse.ArgumentParser(description="Generate the Zola content from notes/.")
    parser.add_argument("--strict", action="store_true", help="exit 1 if any warning was emitted")
    parser.add_argument("--notes-dir", type=Path, default=DEFAULT_NOTES, help=argparse.SUPPRESS)
    args = parser.parse_args(argv[1:])

    notes_root = args.notes_dir.expanduser()
    if not notes_root.is_dir():
        print(f"error: {notes_root} is not a directory", file=sys.stderr)
        return 1

    # Phase 1: collect everything so links can be resolved across courses and voci.
    reg = Registry()
    courses = []
    lessons = load_lessons(notes_root, reg, courses)
    course_titles = {c["title"] for c in courses}
    voci = load_voci(notes_root, reg, course_titles)
    lesson_by_path = {l["path"]: l for l in lessons}
    voce_by_path = {v["path"]: v for v in voci}

    # Phase 2: convert bodies. refs[src] = ordered voce paths that src links to.
    refs = {}
    for lesson in lessons:
        lesson["html"] = convert_body(lesson["body"], reg, lesson, lesson["label"], refs)
    for voce in voci:
        voce["html"] = convert_body(voce["body"], reg, voce, voce["label"], refs)

    # Phase 3: backlinks (inverse of refs), introdotta_in and per-lesson voci.
    incoming = {}
    for src, targets in refs.items():
        for tgt in targets:
            incoming.setdefault(tgt, []).append(src)

    for voce in voci:
        srcs = incoming.get(voce["path"], [])
        les = sorted((s for s in srcs if s in lesson_by_path),
                     key=lambda s: (lesson_by_path[s]["date"], s))
        vs = sorted((s for s in srcs if s in voce_by_path), key=lambda s: voce_by_path[s]["title"])
        voce["extra"]["backlinks"] = les + vs

        intro = voce["introdotta"]
        intro_path = ""
        if intro:
            hit = reg.get(intro)
            if hit is not None and hit["kind"] == "lesson":
                intro_path = hit["path"]
            else:
                warn(f"{voce['label']}: introdotta_in '{intro}' is not a lesson")
        voce["extra"]["introdotta_in_path"] = intro_path

    for lesson in lessons:
        lesson["extra"]["voci"] = list(refs.get(lesson["path"], {}).keys())

    # Phase 4: wipe and write content/ and static/search.json.
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir(parents=True)

    letters = sorted({v["letter"] for v in voci})
    recent = [l["path"] for l in sorted(lessons, key=lambda l: (l["date"], l["path"]), reverse=True)[:RECENT_COUNT]]
    write(CONTENT / "_index.md",
          front_matter([("title", "BSM · UniPi"), ("sort_by", "none"), ("template", "index.html")],
                       {"recent": recent}))

    for course in courses:
        write(CONTENT / course["slug"] / "_index.md",
              front_matter([("title", course["title"]), ("sort_by", "date"),
                            ("template", "section.html"), ("page_template", "page.html")],
                           {"kind": "corso"}))
        for lesson in course["lessons"]:
            extra = dict(lesson["extra"])
            fm = front_matter([("title", lesson["title"]), ("date", lesson["date"]), ("slug", lesson["slug"])],
                              extra)
            write(CONTENT / lesson["path"], fm + "\n" + lesson["html"])

    write(CONTENT / VOCI_SECTION / "_index.md",
          front_matter([("title", "Voci"), ("sort_by", "title"), ("template", "voci.html"),
                        ("page_template", "voce.html")],
                       {"kind": "voci", "letters": letters}))
    for voce in voci:
        fm = front_matter([("title", voce["title"]), ("description", voce["sintesi"]), ("slug", voce["slug"])],
                          voce["extra"])
        write(CONTENT / voce["path"], fm + "\n" + voce["html"])

    search = []
    for course in courses:
        for lesson in course["lessons"]:
            search.append({"title": lesson["title"], "url": lesson["url"],
                           "kind": "lezione", "corso": course["title"], "alias": ""})
    for voce in voci:
        search.append({"title": voce["title"], "url": voce["url"],
                       "kind": "voce", "corso": ", ".join(voce["corsi"]),
                       "alias": ", ".join(voce["alias"])})
    SEARCH_INDEX.parent.mkdir(parents=True, exist_ok=True)
    SEARCH_INDEX.write_text(json.dumps(search, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    print(f"courses: {len(courses)}")
    print(f"lessons: {len(lessons)}")
    print(f"voci: {len(voci)}")
    print(f"warnings: {warnings}")
    if args.strict and warnings:
        return 1
    return 0


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
