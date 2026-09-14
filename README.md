# my-book

A Quarto book project, built from Jupyter notebooks.

## Layout

- `_quarto.yml` — master config: chapter order, output formats (html/pdf/epub), theme.
- `index.qmd` — preface / landing page.
- `chapters/` — the actual book chapters, as plain-text `.qmd` files.
- `notebooks_source/` — your ORIGINAL `.ipynb` files, untouched. Source of truth / backup.
  Never rendered by Quarto (excluded in `_quarto.yml`).
- `notebooks_student/` — hand-authored notebooks you actually hand to students: minimal
  explanation, task prompts, code stubs/TODOs. Also never rendered by Quarto — these are
  plain files you (or Claude Code) write and maintain directly, independent of the book.
- `data/raw/` — original datasets, untouched.
- `data/processed/` — cleaned/derived data used by chapters.
- `images/` — figures, diagrams, cover art.
- `references.bib` — bibliography (BibTeX), cited in chapters as `[@key]`.

## Workflow

1. Put an original notebook in `notebooks_source/`.
2. Convert it to a starting chapter:
   ```
   quarto convert notebooks_source/02-linear-models.ipynb -o chapters/02-linear-models.qmd
   ```
3. Add the new chapter to the `chapters:` list in `_quarto.yml`.
4. Edit the `.qmd` file directly — full explanations, code, citations, worked solutions.
5. Preview the book as you go:
   ```
   quarto preview
   ```
6. When ready, render the other book formats:
   ```
   quarto render --to pdf
   quarto render --to epub
   ```
7. Separately, write or update the matching student notebook in `notebooks_student/` — a
   trimmed-down version with minimal explanation and task prompts instead of full solutions.
   This is a manual step: when you meaningfully change a chapter, update its student notebook
   to match. Claude Code can do this well if you ask it to "update notebooks_student/02-....ipynb
   to match the changes in chapters/02-....qmd" — treat that as a normal part of editing a
   chapter, not an afterthought, so the two don't drift apart.

## Publishing

- `epub` output → Kindle via Amazon KDP.
- `pdf` output → paperback interior via Amazon KDP (adjust `geometry`/trim size in
  `_quarto.yml` to match KDP's requirements before final export).
