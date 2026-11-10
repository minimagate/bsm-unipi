---
name: import-notes
description: Import new or changed lecture notes from the University vault into the bsm-unipi wiki: clean them up, add examples, create concept articles (voci) and links, build, verify and commit. Use when the user runs /import-notes or asks to import/sync/update notes.
---

# /import-notes: import lecture notes into the wiki

You are the **orchestrator**. You plan, delegate, verify and report. You do not write lesson or voce content yourself, except for small fixes you verify.

Repo: `/Users/michelangelogubinelli/Github/bsm-unipi`. Vault (READ-ONLY, never write to it): `~/Library/Mobile Documents/iCloud~md~obsidian/Documents/University`, or `$BSM_VAULT` if set. Use `--vault PATH` with the scripts to override.

## Repo rules (apply to every step)

- Plan first. Anything beyond importing (renaming courses, changing the layout, editing templates, rebuilding the whole site design) needs the user's confirmation first.
- Content work (lesson cleanup, voci) is delegated to subagents on **Sonnet** (`model: "sonnet"` in the Agent call). Math fidelity matters, so this tier is approved for content. Mechanical or code fixes go to **Haiku** (`model: "haiku"`).
- Every subagent gets a **self-contained brief** (see the template below). It must not rely on this conversation.
- You verify the results yourself (step 4). You commit only after the user has seen the summary and said OK.
- Commits and PRs: no co-author trailers, no "generated with" lines, and never name the tool, harness or model. Plain message only.
- Never modify the vault.
- Do not touch unrelated files. Other work may be happening in `templates/`, `static/`, `scripts/build_content.py` and `notes/`. Only change the files this import needs.

## Step 0: load the rules

Read these two skills before doing anything else, and make sure the subagent briefs point to them:

- `/Users/michelangelogubinelli/Github/bsm-unipi/.claude/skills/note-style/SKILL.md`
- `/Users/michelangelogubinelli/Github/bsm-unipi/.claude/skills/wiki-structure/SKILL.md`

## Step 1: what is new or changed

```sh
cd /Users/michelangelogubinelli/Github/bsm-unipi
python3 scripts/import_status.py            # human summary
python3 scripts/import_status.py --json     # machine-readable list
```

Statuses: `new` (no wiki lesson), `changed` (vault file differs from the `vault_hash` recorded in the wiki lesson), `unchanged`, `orphan` (wiki lesson whose vault note is gone; report it, do not delete it without asking).

If there is nothing `new` or `changed`, say so ("Nothing new or changed") and stop.

## Step 2: registry and changed notes

1. Read `notes/_voci.md` fully. You need it to brief subagents on existing voci.
2. For each `changed` note, warn the user that the wiki version may contain manual edits. Show the history of that file:
   ```sh
   git log --oneline -- notes/<Course>/<stem>.md
   ```
   Ask whether to **re-import (overwrite)** or **skip** each one. Group the question if there are many. Do not overwrite a changed lesson without an answer.
3. Only `new` notes and the `changed` notes the user chose to re-import go on to step 3.

## Step 3: plan the batches and delegate

1. Group the selected notes **by course**, in **chronological order** (the date at the start of the file name). Split a course group into batches of at most about 8 notes, one subagent per batch.
2. Spawn the subagents in parallel with the Agent tool, `model: "sonnet"`. Each one gets the brief below, filled in.
3. **Registry merge.** Subagents must not append to `notes/_voci.md` themselves when several run in parallel (write conflicts). Each subagent **returns its proposed registry rows** and the list of voci files it wrote. You then:
   - check for duplicates: the same concept proposed by two batches. Keep one voce, owned by the **earlier** lesson (`introdotta_in`). For the later batch, instruct a Haiku fix subagent to replace the duplicate voce with a link to the existing one (and to add the course to `corsi`);
   - append the new rows to `notes/_voci.md` in sort order (course, then date) yourself;
   - check that every voce file's `corsi` and the registry row agree.
4. Voci file ownership: the subagent whose lesson introduces a voce writes `notes/Voci/<Nome>.md`. A later batch that reuses an existing voce only edits its `corsi` line (and adds links), and it reports that edit back to you.

### Subagent brief template

Fill every `{...}`. Send it as the Agent prompt.

```
You are cleaning up lecture notes for the bsm-unipi wiki (Italian, Zola site). Work only in these paths:
- Write: /Users/michelangelogubinelli/Github/bsm-unipi/notes/{Course}/<stem>.md (one per note below)
- Write: /Users/michelangelogubinelli/Github/bsm-unipi/notes/Voci/<Nome>.md (only for NEW voci you decide to create, see below)
- Edit (only the corsi line): existing voce files listed below, if a reused voce needs its corsi updated
- Read only: the vault notes below, the registry, and the two skills.
- Do NOT edit notes/_voci.md (the orchestrator merges registry rows), templates/, static/, scripts/, or any other file. Do NOT modify the vault. Do NOT run git commit or git push.

Read first, fully:
1. /Users/michelangelogubinelli/Github/bsm-unipi/.claude/skills/note-style/SKILL.md
2. /Users/michelangelogubinelli/Github/bsm-unipi/.claude/skills/wiki-structure/SKILL.md
3. /Users/michelangelogubinelli/Github/bsm-unipi/notes/_voci.md (existing concepts; reuse them, never duplicate)

Vault notes to import (absolute paths, READ-ONLY):
- {absolute path to vault note 1}
- {absolute path to vault note 2}
Course: {Course}. Vault root: {vault root}.

Steps:
A. Read every vault note in full. Decide which genuinely NEW concepts need a voce (wiki-structure: "When to create a voce"; typically 0 to 4 per lesson, zero for review/exercise lessons). Do not create a voce for something an existing row in _voci.md already covers.
B. For each note, write the lesson to notes/{Course}/<same file name as the vault note>.md:
   - Frontmatter: every key of the vault note exactly as it is, then append:
       vault_path: "<path relative to vault root, e.g. Notes/{Course}/Lectures/<file>.md>"
       vault_hash: "<output of: python3 /Users/michelangelogubinelli/Github/bsm-unipi/scripts/import_status.py --hash "<absolute vault path>">"
     Run that command with the Bash tool; do not type a hash yourself.
   - Body: cleaned per note-style. Keep all headings identical, all formulas, all definitions and proofs. Light touch. Max 3 short examples, each in a > [!example] Esempio callout.
   - Link the first mention of each concept that has a voce (new or existing), at most once per concept per lesson, as [[Nome voce|testo nella frase]]. Never in headings or formulas.
C. Write each NEW voce to notes/Voci/<Titolo>.md following wiki-structure exactly (frontmatter with dash lists, Italian body 150-400 words, sections in order, Vedi anche with 2-5 existing or new voci, no "Dove compare"). introdotta_in = this lesson's file stem. Only link voci that exist or that you create in this batch.
D. For each EXISTING voce from _voci.md that this lesson uses: if the course is not in its corsi list, add the course to the corsi list in its file (one line edit). Do not change anything else in it. Report the file.
E. Run: python3 /Users/michelangelogubinelli/Github/bsm-unipi/scripts/check_math.py "<absolute vault path>" "<absolute path of the lesson you wrote>"
   Every MISSING formula must be fixed in the lesson (restore it exactly as in the vault). If a formula is intentionally different, you must not change it: report it instead. Re-run until OK (added examples are fine).
F. Check the lesson: no emojis, no duplicated H1, $$ balanced, no line that is exactly \] or \[ .

Return to the orchestrator, in this exact form (plain text, no preamble):
LESSONS: <one line per lesson: file name, vault length in chars, lesson length in chars, number of added examples, number of voce links>
NEW_VOCI: <file name per voce, and its introdotta_in>
REGISTRY_ROWS: <the exact markdown table rows to append to notes/_voci.md, one per new voce, in the format
| Voce | Alias | Categoria | Corsi | Introdotta in |>
CORSI_UPDATED: <existing voce files you edited, and what you added>
MATH_ISSUES: <formulas you could not fix, or "none">
PROBLEMS: <anything you were unsure about, or "none">
```

## Step 4: verify (orchestrator)

Run everything yourself. Do not trust the subagents' reports alone.

1. Merge the registry rows (step 3) and check sort order.
2. Build with strict link checking, then the Zola build:
   ```sh
   cd /Users/michelangelogubinelli/Github/bsm-unipi
   python3 scripts/build_content.py --strict && /opt/homebrew/bin/zola build
   ```
   If the build fails, read the reported unresolved links. Fix them with a Haiku subagent (mechanical) or a Sonnet subagent (content), then rebuild.
3. Math for every paired lesson:
   ```sh
   python3 scripts/check_math.py --all
   ```
   Exit 1 means missing formulas or delimiter issues. Send each to a Sonnet subagent with the exact MISSING lines and the vault note path, and have it restore the formula exactly as in the vault. Re-run until exit 0.
4. Read the diff of a sample of lessons (at least 2 per course, and every lesson with a new voce). Compare with the vault note:
   ```sh
   diff "<vault note>" notes/<Course>/<stem>.md
   ```
   Check: headings identical, nothing important dropped, tone light, no emojis, voce links only on first mention, frontmatter keys intact, `vault_hash` present. Also read each new voce: Italian, length, correct frontmatter, no "Dove compare".
5. Check that the `vault_hash` of each imported lesson is the current one:
   ```sh
   python3 scripts/import_status.py
   ```
   The imported notes must now show as `unchanged`.
6. Fix problems with a subagent: Haiku for mechanical issues (frontmatter, spacing, a missing course in `corsi`), Sonnet for content (wording, a dropped sentence, a wrong link). Never fix content yourself by rewriting it.

## Step 5: summary, then commit after OK

Show the user a short summary:

- lessons imported (per course, with new / re-imported counts);
- new voci (title, course, categoria);
- existing voci whose `corsi` changed;
- warnings: changed notes skipped, orphans, formulas that could not be verified, build results;
- the `git status --short` list of files that will be committed.

Wait for the user's OK. Then:

```sh
cd /Users/michelangelogubinelli/Github/bsm-unipi
git status --short notes/                 # check what is there first
git add <only the lesson, voce and registry files of this import>
git commit -m "notes: import <N> lezioni (<courses>)"
git push origin main
```

- `<N>` is the number of lessons imported, `<courses>` the course names, comma-separated, for example `notes: import 12 lezioni (Aritmetica, Geometria 1)`.
- Do not add `content/`, `public/` or anything outside `notes/` unless the user approved it. `content/` is generated and gitignored.
- The commit message has no co-author line and no "generated" line.
- GitHub Pages deploys automatically after the push to `main`. Report the commit hash and the push result.

If the user says skip or does not confirm, leave the working tree as it is and report what is uncommitted.
