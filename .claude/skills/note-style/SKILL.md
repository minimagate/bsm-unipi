---
name: note-style
description: Style guide for cleaning up one university lecture note into a bsm-unipi wiki lesson (light touch, Italian, keep headings, formulas and callouts, add at most a few examples, link voci). Use when writing, reviewing or fixing a lesson in notes/<Course>/ during an import, or when asked what the lesson style is.
---

# Note style (wiki lessons)

A wiki lesson is the vault lecture note, lightly cleaned up. It is **not** a rewrite and not a textbook chapter. The reader is a student who already has the lecture notes open next to the wiki. The mathematics must be exactly what the vault says.

Read this together with `wiki-structure` (file formats, voci, links). Output is always **Italian**.

## Non-negotiables

1. **Math fidelity.** Never change the meaning of a statement, a formula, a hypothesis, a quantifier or a case distinction. Keep every `$...$` and `$$...$$` formula. Do not rewrite a formula unless it is an obvious typo (a missing bracket, `\frac` written as `\fract`). If in doubt, leave it exactly as it is and mention it in your report.
2. **Keep the structure.** Keep every section and every heading with its text identical. Other notes link to `#Heading` anchors, so renaming a heading breaks links. Keep the frontmatter of the vault note unchanged (you only append `vault_path` and `vault_hash`, see `wiki-structure`).
3. **Keep the content.** Every definition, theorem, proof, example, callout, existing `[[link]]` and every remark about uncertainty in the source ("non sono sicuro", "il prof non ha detto", "da verificare") stays.
4. **Length within ±15%** of the vault note, counting the examples you add. Light touch: most sentences change a few words, not all of them.
5. **No emojis.** Not in text, not in headings, not in callouts.
6. **Italian only.** If the vault note has an English sentence, leave it. Do not translate.

## What you change

- **Simplify heavy sentences.** Split a 60-word sentence with three subordinate clauses into two. Remove bureaucratic phrasing ("si procede nel seguente modo" → "procediamo così", "si evince che" → "quindi").
- **Cut repetition.** If the note says the same thing twice in one paragraph, keep the clearer one. Do not cut repetition that is part of a proof.
- **Relax the tone a bit.** Direct and friendly. Typical phrases: "in pratica", "l'idea è…", "occhio:", "nota bene", "vediamo perché". Use them sparingly, at most one or two per section. No slang, no jokes in every paragraph.
- **Fix obvious typos** and **broken delimiters**: `$$` must come in pairs, a display formula closes with `$$` and never with `\]`. A stray `\[` or `\]` alone on a line is always a bug.
- **Remove the duplicated H1** at the top of the note if the template already shows the title. This is optional, the build strips it anyway.

## Examples: add sparingly

- Add **1 to 3 short worked examples per lesson**, and only where a concept introduced in the lesson has none.
- Never add an example to a lesson that already has a worked example for each new concept.
- Examples are **added material**, so mark each one with a callout. Keep the numbers small and check the arithmetic twice:
  ```
  > [!example] Esempio
  > Con $a = 252$ e $b = 198$: …
  ```
- An example must not introduce a new definition or a new result. It only illustrates something the lesson already says.

## Callouts

Obsidian callouts carry over. The build knows these types: `warning` (Attenzione), `note` (Nota), `important` (Importante), `tip` (Suggerimento), `example` (Esempio). Keep the vault's type when it is one of these. Do not invent new types. Callout bodies follow the same rules as normal text (fidelity, no emojis).

## Voci links

A **voce** is a short concept article (see `wiki-structure`). Link to a voce from the lesson the first time its concept appears in running text:

- Form: `[[Nome voce|testo come appare nella frase]]`, for example `[[Divisione euclidea|divisione euclidea]]`. Use the exact voce title, or one of its aliases, before the `|`.
- **At most one link per concept per lesson.** A second link to the same voce is allowed only in a much later H2 section where it really helps.
- **Do not link** inside headings, inside formulas (`$...$`, `$$...$$`), inside code, or inside a callout title.
- Link only concepts that have a voce in `notes/_voci.md` (or one you are creating now). Do not invent links to voci that do not exist: the build fails on unresolved links.
- Existing Obsidian links `[[stem#Heading|alias]]` between lessons are kept as they are.

## Before and after

Vault note (BEFORE):

```
## Algoritmo di Euclide

Dati due interi $a$ e $b$ con $b \neq 0$, si procede nel seguente modo, la cui correttezza andrà poi giustificata opportunamente in seguito: si calcola il resto della divisione euclidea di $a$ per $b$, ovvero si scrive $a = qb + r$ con $0 \le r < b$.

$$
\mathrm{MCD}(a,b) = \mathrm{MCD}(b, r)
$$

Il procedimento si itera finché il resto non si annulla.
```

Wiki lesson (AFTER):

```
## Algoritmo di Euclide

Dati due interi $a$ e $b$ con $b \neq 0$, l'idea è questa: calcoliamo il resto $r$ della [[Divisione euclidea|divisione euclidea]] di $a$ per $b$, cioè $a = qb + r$ con $0 \le r < b$. La correttezza la vedremo più avanti.

$$
\mathrm{MCD}(a,b) = \mathrm{MCD}(b, r)
$$

In pratica il problema si sposta su una coppia più piccola. Si ripete finché il resto non si annulla.

> [!example] Esempio
> Con $a = 252$ e $b = 198$: $252 = 1 \cdot 198 + 54$, poi $198 = 3 \cdot 54 + 36$, $54 = 1 \cdot 36 + 18$, $36 = 2 \cdot 18 + 0$. Quindi $\mathrm{MCD}(252, 198) = 18$.
```

What happened: the sentence was split and made plainer, the formula is byte-for-byte the same, the forward reference was shortened, there is one voce link at the first mention, the repetition "si itera" became "si ripete", and one example was added in a callout (and checked: $54 = 1 \cdot 36 + 18$ and $36 = 2 \cdot 18$).

## Checklist before you hand a lesson back

- [ ] Every heading text is identical to the vault note, same level, same order.
- [ ] Every formula from the vault note is present (run `python3 scripts/check_math.py <vault note> <lesson>`; it must print OK, or you must explain each MISSING line).
- [ ] `$$` pairs are balanced; no line is exactly `\]` or `\[`.
- [ ] Length is within about ±15% of the vault note (plus the added examples).
- [ ] At most one voce link per concept, none in headings or formulas, every link target exists.
- [ ] At most 3 added examples, each in a `> [!example] Esempio` callout, each arithmetically checked.
- [ ] No emojis, Italian throughout, no "Dove compare" section (the build generates it).
