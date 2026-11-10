# BSM · UniPi

Appunti liberi del corso di laurea in Matematica (Università di Pisa), in stile wiki: lezioni per corso, più brevi voci di concetto collegate tra loro. Costruito con [Zola](https://www.getzola.org/) 0.22.1.

## Struttura

```
notes/
  <Corso>/<YYYY-MM-DD - Titolo>.md   una lezione per file (frontmatter + corpo)
  Voci/<Nome voce>.md                una voce per file (frontmatter: categoria, corsi, alias, sintesi, introdotta_in)
  _voci.md                           registro delle voci (tabella, non renderizzato)
scripts/
  build_content.py                   notes/ -> content/ e static/search.json
  dev.sh                             build + zola serve per l'anteprima locale
  import_status.py, check_math.py    confronto con il vault Obsidian (vedi sotto)
templates/                           Tera: base, home, corso, lezione, voce, indice voci
static/                              style.css (tema chiaro/scuro), ui.js, search.js, preview.js, math.js, font
```

`notes/` è l'unica fonte: `content/` e `static/search.json` sono generati e non vanno committati.

Gli URL sono: lezioni `/<corso>/<lezione>/`, corsi `/<corso>/`, voci `/voci/<voce>/`, indice A–Z `/voci/`.

## Generare il contenuto

```sh
python3 scripts/build_content.py            # rigenera content/ e static/search.json
python3 scripts/build_content.py --strict   # esce con codice 1 se c'è almeno un avviso
```

Lo script usa solo la libreria standard di Python. Gestisce:

- formule `$…$` e `$$…$$` (renderizzate da KaTeX nel browser);
- wikilink `[[…]]` risolti per nome file, titolo e alias delle voci, anche tra corsi diverse;
- callout Obsidian (`warning`, `note`, `important`, `tip`, `example`);
- backlink: ogni voce elenca dove compare; ogni lezione elenca le voci che usa.

Gli avvisi (link non risolti, data mancante, voce senza sintesi, …) finiscono su stderr; con `--strict` la build fallisce, ed è quello che fa la CI.

## Anteprima locale

```sh
scripts/dev.sh             # build + zola serve (l'URL locale è stampato da zola)
scripts/dev.sh --strict    # gli argomenti passano allo script di build
```

## Pubblicazione

Un push su `main` (o l'avvio manuale del workflow) esegue `build_content.py --strict`, poi `zola build` e pubblica `public/` su GitHub Pages.

## Skill per Claude Code

Le procedure di lavoro sono nelle skill di `.claude/skills/`:

- `/import-notes`: porta nuove lezioni dal vault Obsidian in `notes/` (crea o aggiorna le voci e il registro).
- `note-style`: regole di pulizia del testo e di stile per lezioni e voci.
- `wiki-structure`: convenzioni di formato di `notes/` e di URL.

`scripts/import_status.py` confronta il vault con `notes/` (nuove / modificate / invariate) e `scripts/check_math.py` confronta le formule tra una nota del vault e la lezione wiki corrispondente.

## Tema e accessibilità

Tema chiaro e scuro (sfondo scuro `#1E1E1E`). Di default segue il sistema; il pulsante in alto a destra fissa la scelta, salvata nel browser. Ricerca: tasto `/`, frecce e Invio.
