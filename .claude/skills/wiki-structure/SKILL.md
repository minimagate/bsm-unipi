---
name: wiki-structure
description: Reference for the bsm-unipi wiki layout: lesson and voce file formats, the voci registry (notes/_voci.md), when to create a voce, linking rules, and the build check. Use when creating or editing anything under notes/ (lessons, voci, registry), or when a build fails on links.
---

# Wiki structure (bsm-unipi)

The site is a Wikipedia-style wiki in Italian, built with Zola 0.22.1 and deployed to GitHub Pages. Its content lives in `notes/`. The build copies it into `content/` (generated, gitignored). Never edit `content/` by hand and never commit it.

## Repo layout

```
notes/
  _voci.md                              # concept registry (a table). Not rendered.
  <Course>/<YYYY-MM-DD - Titolo>.md     # one cleaned lesson per vault note, SAME file name
  Voci/<Nome voce>.md                   # one concept article per file; file name = voce title
scripts/build_content.py                # notes/ -> content/, then the Zola build
scripts/import_status.py                # vault vs notes/: new / changed / unchanged / orphan
scripts/check_math.py                   # formulas of a vault note vs its wiki lesson
```

Course folder names are the vault course names exactly: `Analisi 1`, `Aritmetica`, `Fondamenti di Programmazione`, `Geometria 1`. Lesson file names are the vault file names exactly, date first, for example `2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout.md`. There is no `Lectures/` subfolder in `notes/`.

URLs (for your information, you never write them): lessons `/<course-slug>/<lesson-slug>/`, voci `/voci/<voce-slug>/`, course portals `/<course-slug>/`, the A-Z index `/voci/`.

## Lesson file format: `notes/<Course>/<stem>.md`

The frontmatter is the vault note's frontmatter **unchanged**, plus two keys appended at the end:

```yaml
---
<every key of the vault note, exactly as in the vault>
vault_path: "Notes/Aritmetica/Lectures/2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout.md"
vault_hash: "<64 hex characters from scripts/import_status.py --hash>"
---
```

- `vault_path` is the path of the vault note relative to the vault root.
- `vault_hash` is the sha256 of the vault file's bytes at import time. Get it with `python3 scripts/import_status.py --hash "<full path to vault file>"`. Never type a hash by hand.
- YAML must stay simple: `key: value`, quoted scalars, and dash lists (`- item` on the following lines). No inline lists like `[a, b]`, no nested maps.
- The body is the cleaned text, see `note-style`.

## Voce file format: `notes/Voci/<Nome>.md`

One voce per concept. The file name is the voce title (for example `Identità di Bézout.md`). The frontmatter:

```yaml
---
title: Identità di Bézout
type: voce
categoria: teorema            # one of: definizione | teorema | oggetto | metodo | notazione
corsi:
- Aritmetica                  # every course that uses it (course folder names)
introdotta_in: 2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout   # lesson stem where it first appears
alias:
- Bézout                      # other names, plurals, short forms used in links (optional)
sintesi: Ogni massimo comun divisore di due interi si scrive come loro combinazione lineare a coefficienti interi.   # one plain sentence, NO math
---
```

Rules for the frontmatter:

- `sintesi` is one plain-text sentence with no formulas and no colon. It is used for hover previews and the meta description. Quote it with double quotes if it contains `:` or `#`.
- `introdotta_in` is the stem (file name without `.md`) of the lesson where the concept first appears. It must match an existing lesson file.
- `corsi` lists every course that uses the voce. Keep it in sync with the registry.
- `alias` may be left out entirely (remove the key) if there are none.

### Complete example voce (Italian)

This is the reference shape. The body is 150-400 words, faithful to the notation of the course notes.

```markdown
---
title: Identità di Bézout
type: voce
categoria: teorema
corsi:
- Aritmetica
introdotta_in: 2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout
alias:
- Bézout
sintesi: Ogni massimo comun divisore di due interi si scrive come loro combinazione lineare a coefficienti interi.
---

L'**identità di Bézout** afferma che il massimo comun divisore di due interi si può sempre esprimere come combinazione lineare dei due numeri, con coefficienti interi. È uno dei risultati più usati dell'aritmetica elementare.

## Enunciato

Siano $a, b \in \mathbb{Z}$ non entrambi nulli e sia $d = \mathrm{MCD}(a, b)$. Allora esistono $x, y \in \mathbb{Z}$ tali che

$$
d = ax + by.
$$

## Intuizione

Pensa a $ax + by$ come a un modo di "mescolare" $a$ e $b$ con coefficienti interi, anche negativi. Bézout dice che tra tutti questi risultati c'è proprio il massimo comun divisore.

## Esempi

- $\mathrm{MCD}(4, 6) = 2$ e $2 = 4 \cdot (-1) + 6 \cdot 1$: qui serve un coefficiente negativo.
- $\mathrm{MCD}(252, 198) = 18$ e $18 = 252 \cdot 4 - 198 \cdot 5$.

## Come si dimostra

L'idea è considerare il più piccolo intero positivo della forma $ax + by$ e mostrare, con la divisione euclidea, che divide sia $a$ sia $b$. Dettagli [[2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout#Identità di Bézout|nella lezione del 5 ottobre]].

## Vedi anche

- [[Divisione euclidea]]
- [[Massimo comun divisore]]
- [[Equazioni diofantee lineari]]
```

Notes on the example: the `## Come si dimostra` link targets a heading of the lesson, so the heading must exist exactly as written. The `Vedi anche` targets must be voci that exist (or aliases). Do not copy this example's links if the targets do not exist yet; create the target or drop the link.

### Body sections, in order

1. **Lead paragraph** (no heading), Wikipedia style: starts with the term in bold, e.g. "L'**identità di Bézout** afferma che…". One to three plain sentences.
2. `## Definizione` or `## Enunciato` (choose by `categoria`): precise, with hypotheses.
3. `## Intuizione`: short and casual, why it matters or how to picture it.
4. `## Esempi`: one or two small worked examples with checked arithmetic.
5. `## Come si dimostra` (optional): 2 to 5 lines of the proof idea, plus a link to the lesson section where the course proves it, `[[stem#Heading|nella lezione del …]]`.
6. `## Vedi anche`: a bullet list of 2 to 5 related voci as `[[Nome voce]]`.

Do **not** write a "Dove compare" / backlinks section. The build generates it from the links. Writing it by hand duplicates it.

## Registry: `notes/_voci.md`

A Markdown table with one row per voce, exactly this header:

```
| Voce | Alias | Categoria | Corsi | Introdotta in |
|---|---|---|---|---|
| Identità di Bézout | Bézout | teorema | Aritmetica | 2026-10-05 - Divisione euclidea, massimo comun divisore e identità di Bézout |
```

- Sort rows by course, then by date (the date at the start of `Introdotta in`). For a voce with several courses, sort by its first course.
- `Alias` and `Corsi` cells are comma-separated. An empty alias cell is allowed.
- The row must mirror the voce file's frontmatter (title, alias, categoria, corsi, introdotta_in). When you change one, change the other.
- Titles are Italian, singular, sentence case, as a Wikipedia article would be: "Teorema cinese del resto", "Massimo comun divisore", "Spazio vettoriale", "Tripla di Hoare".

## When to create a voce

Create one when a **new** term, definition, mathematical object, theorem or method is introduced for the first time in the course **and** it is reused later in the course or is central to it.

- Rough guide: 1 to 4 new voci per lesson where something genuinely new appears, zero for review and exercise lessons.
- Do not create voci for one-off examples, exercises, trivial words, or every lemma.
- **One voce per concept across the whole site.** If a concept already has a voce (check `notes/_voci.md` and the `Voci/` folder, and also check aliases), reuse it. Do not create a second voce with another name.
- If a later course uses an existing voce, do not create a new one. Instead add the course to `corsi` in the voce file **and** in the registry row, and add a link from the new lesson where appropriate.
- `introdotta_in` stays the first lesson that introduced it. Do not change it when a later course reuses the voce.

## Linking rules

- Link to a voce with `[[Nome voce]]` or `[[Nome voce|testo]]`. The alias works too: `[[Bézout]]` resolves to the voce with alias `Bézout`. The text after `|` is what the reader sees in the sentence.
- In lessons, link the **first meaningful mention** of each registered concept, at most once per concept per lesson.
- Never link inside headings, inside formulas (`$...$`, `$$...$$`), or inside code.
- Links must resolve. A link to a missing voce or alias makes the build fail (`--strict`). Keep `#Heading` anchors pointing at headings that exist in the target lesson.
- Existing Obsidian links between lessons (`[[stem#Heading|alias]]`) are kept as they are.

## Build and check

From the repo root:

```sh
python3 scripts/build_content.py --strict && zola build
```

`--strict` makes the build fail on any unresolved link. Fix every reported link (usually: create the missing voce, fix the spelling, or drop the link), then rebuild. Zola is at `/opt/homebrew/bin/zola` if it is not on the PATH.

Math check, per lesson or for all paired lessons:

```sh
python3 scripts/check_math.py "<vault note>" notes/<Course>/<stem>.md
python3 scripts/check_math.py --all
```

Run them after writing a lesson. Missing formulas are fidelity problems and must be fixed or explained.
