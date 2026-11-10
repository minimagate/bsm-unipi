# BSM · UniPi

Static site with study notes (Analisi 1, Aritmetica, Fondamenti di Programmazione, Geometria 1), built with [Zola](https://www.getzola.org/).

## How it works

- The notes live in a separate Obsidian vault (`Notes/<Course>/**/*.md`). This repo never stores them.
- `scripts/build_content.py <vault_root>` reads the vault and regenerates `content/`: frontmatter becomes Zola front matter, `$...$` / `$$...$$` math is turned into `data-tex` spans rendered by KaTeX, wikilinks become internal links, and Obsidian callouts become styled blockquotes. It uses only the Python standard library.
- A GitHub Action runs every day at 05:00 UTC and on each push to `main`. It checks out the vault repo (`minimagate/University`) into `university/`, runs the script, builds with Zola 0.22.1 and deploys to GitHub Pages.

## Local preview

```sh
BSM_VAULT="/path/to/University" scripts/dev.sh
# or
scripts/dev.sh /path/to/University
```

The vault is read-only input; nothing is written to it.
