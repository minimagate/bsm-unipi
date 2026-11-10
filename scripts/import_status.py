#!/usr/bin/env python3
"""Compare the Obsidian lecture vault with the wiki lessons in notes/.

Usage:
  python3 scripts/import_status.py [--vault PATH] [--json]
  python3 scripts/import_status.py --hash FILE

Vault root: --vault PATH, else $BSM_VAULT, else the default iCloud Obsidian path.

Per vault note (Notes/<Course>/Lectures/*.md):
  new        no wiki lesson matches it
  changed    wiki lesson exists but its vault_hash != sha256 of the vault file
  unchanged  wiki lesson exists and vault_hash matches
Wiki lessons (notes/<Course>/*.md) whose vault note has disappeared are "orphan".

A wiki lesson is matched by its `vault_path` frontmatter key. Lessons without
that key fall back to the vault note with the same course and file name.

Informational: exits 0 in status mode. `--hash FILE` prints the sha256 of FILE
and exits 1 only if FILE cannot be read.
Python standard library only.
"""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_VAULT = "~/Library/Mobile Documents/iCloud~md~obsidian/Documents/University"
FM_KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*$")
STATUS_ORDER = ["new", "changed", "unchanged", "orphan"]


def resolve_vault(arg=None):
    raw = arg or os.environ.get("BSM_VAULT") or DEFAULT_VAULT
    return Path(os.path.expanduser(raw))


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def read_frontmatter(path):
    """Top-level scalar keys of the YAML frontmatter (empty dict if none)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {}
    lines = text.lstrip("﻿").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    data = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        m = FM_KEY_RE.match(line)  # unindented "key: value" only; skips "- item" lines
        if m:
            data[m.group(1)] = unquote(m.group(2))
    return data


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def scan_vault(vault):
    """{vault_path: {course, stem, path}} for Notes/<Course>/Lectures/*.md."""
    found = {}
    notes_dir = vault / "Notes"
    if not notes_dir.is_dir():
        return found
    for course_dir in sorted(notes_dir.iterdir()):
        if not course_dir.is_dir() or course_dir.name.startswith("."):
            continue
        lectures = course_dir / "Lectures"
        if not lectures.is_dir():
            continue
        for f in sorted(lectures.glob("*.md")):
            key = f"Notes/{course_dir.name}/Lectures/{f.name}"
            found[key] = {"course": course_dir.name, "stem": f.stem, "path": f}
    return found


def scan_wiki(repo=REPO):
    """List of {course, stem, path, fm} for notes/<Course>/*.md.

    Skips notes/Voci and any file directly under notes/ (e.g. _voci.md)."""
    lessons = []
    notes_dir = repo / "notes"
    if not notes_dir.is_dir():
        return lessons
    for course_dir in sorted(notes_dir.iterdir()):
        if not course_dir.is_dir() or course_dir.name in ("Voci",) or course_dir.name.startswith((".", "_")):
            continue
        for f in sorted(course_dir.glob("*.md")):
            lessons.append({"course": course_dir.name, "stem": f.stem, "path": f, "fm": read_frontmatter(f)})
    return lessons


def pair_lessons(vault_notes, lessons):
    """Match wiki lessons to vault notes.

    Returns (pairs, orphans): pairs maps vault_path -> lesson; orphans is the
    list of lessons that match no vault note."""
    pairs = {}
    leftovers = []
    for lesson in lessons:
        vp = lesson["fm"].get("vault_path", "")
        if vp and vp in vault_notes and vp not in pairs:
            pairs[vp] = lesson
        else:
            leftovers.append(lesson)
    orphans = []
    for lesson in leftovers:
        if lesson["fm"].get("vault_path"):
            # explicit key that does not resolve: the vault note is gone or was renamed
            orphans.append(lesson)
            continue
        key = f"Notes/{lesson['course']}/Lectures/{lesson['stem']}.md"
        if key in vault_notes and key not in pairs:
            pairs[key] = lesson
        else:
            orphans.append(lesson)
    return pairs, orphans


def build_records(vault, repo=REPO):
    vault_notes = scan_vault(vault)
    pairs, orphans = pair_lessons(vault_notes, scan_wiki(repo))
    records = []
    for vp, info in sorted(vault_notes.items(), key=lambda kv: (kv[1]["course"], kv[1]["stem"])):
        digest = file_sha256(info["path"])
        lesson = pairs.get(vp)
        if lesson is None:
            status, wiki_path = "new", None
        else:
            wiki_path = lesson["path"].relative_to(repo).as_posix()
            status = "unchanged" if lesson["fm"].get("vault_hash") == digest else "changed"
        records.append({
            "status": status,
            "course": info["course"],
            "stem": info["stem"],
            "vault_path": vp,
            "wiki_path": wiki_path,
            "vault_hash": digest,
        })
    for lesson in sorted(orphans, key=lambda l: (l["course"], l["stem"])):
        vp = lesson["fm"].get("vault_path") or f"Notes/{lesson['course']}/Lectures/{lesson['stem']}.md"
        records.append({
            "status": "orphan",
            "course": lesson["course"],
            "stem": lesson["stem"],
            "vault_path": vp,
            "wiki_path": lesson["path"].relative_to(repo).as_posix(),
            "vault_hash": None,
        })
    return records, len(vault_notes), len(scan_wiki(repo))


def print_human(records, vault, n_vault, n_wiki):
    counts = {s: 0 for s in STATUS_ORDER}
    for r in records:
        counts[r["status"]] += 1
    print(f"Vault: {vault}")
    print(f"Vault notes: {n_vault}   Wiki lessons: {n_wiki}")
    print("  " + "   ".join(f"{s}: {counts[s]}" for s in STATUS_ORDER))
    for status in STATUS_ORDER:
        group = [r for r in records if r["status"] == status]
        if not group:
            continue
        print(f"\n{status.upper()} ({len(group)})")
        for r in group:
            line = f"  {r['course']}  |  {r['stem']}"
            if status == "orphan":
                line += f"   (wiki: {r['wiki_path']})"
            print(line)
    to_import = counts["new"] + counts["changed"]
    print()
    if to_import == 0:
        print("Nothing new or changed.")
    else:
        print(f"To import: {counts['new']} new, {counts['changed']} changed.")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Vault vs wiki import status (informational).")
    parser.add_argument("--vault", help="vault root (default: $BSM_VAULT or the iCloud Obsidian path)")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    parser.add_argument("--hash", metavar="FILE", help="print the sha256 of FILE and exit")
    args = parser.parse_args(argv)

    if args.hash:
        try:
            print(file_sha256(Path(args.hash)))
        except OSError as e:
            print(f"error: cannot read {args.hash}: {e}", file=sys.stderr)
            return 1
        return 0

    vault = resolve_vault(args.vault)
    if not (vault / "Notes").is_dir():
        print(f"warning: no Notes/ folder under vault {vault} (use --vault or BSM_VAULT)", file=sys.stderr)

    records, n_vault, n_wiki = build_records(vault)
    if args.json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
    else:
        print_human(records, vault, n_vault, n_wiki)
    return 0


if __name__ == "__main__":
    sys.exit(main())
