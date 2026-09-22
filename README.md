# Introduction to Data Analytics for Business and Economics

This is the repository for the book *Introduction to Data Analytics for Business and Economics*,
a practical, hands-on introduction to data analytics in Python for business and economics
students.

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

**[Read the book online, for free →](https://matthbogaert.github.io/IDAFBE-book/)**

A paperback and ebook edition are also planned via Amazon KDP.

## Summary

This book stems from years of experience teaching introductory and advanced data analytics
courses across different institutions. There are excellent theoretical handbooks like *An
Introduction to Statistical Learning* and excellent applied books like *Hands-On Machine
Learning*, but none of them focus on what business and economics students actually need most: the
tools and methods to turn a messy, real-world business problem into a proper data analytics
project. That's what this book does differently: no lengthy mathematical derivations, but plenty
of hands-on code, built around a single running case study (predicting customer churn) that
carries through every chapter, from raw data to a working, evaluated predictive model.

The book offers a gentle introduction to Python, so no prior programming experience is strictly
required to start. That said, a light background in programming and statistics helps, since the
material focuses on what you need for data analytics specifically rather than re-teaching either
subject from scratch. It's a good fit for undergraduate or Bachelor-level teaching, and is used as
the primary material for the Data Analytics course at UNamur.

## Repository structure

- `chapters/` — the book chapters, as Quarto (`.qmd`) source files.
- `notebooks_student/` — companion Jupyter notebooks for students: the same material as the
  chapters, in runnable notebook form.
- `data/` — the (anonymised/processed) datasets used throughout the book.
- `images/` — figures and diagrams used in the chapters.
- `references.bib` — the book's bibliography.
- `scripts/` — helper scripts, e.g. the one that regenerates the student notebooks from the
  chapters.

## Citing this book

If you use this book in your teaching or research, please cite it as:

```
Bogaert, Matthias. Introduction to Data Analytics for Business and Economics: Using Python for
Data Preprocessing, Visualization, and Modeling. 2026.
Available at: https://matthbogaert.github.io/IDAFBE-book/
```

Or as BibTeX:

```bibtex
@book{bogaert2026,
  title={Introduction to Data Analytics for Business and Economics},
  subtitle={Using Python for Data Preprocessing, Visualization, and Modeling},
  author={Bogaert, Matthias},
  year={2026},
  url={https://matthbogaert.github.io/IDAFBE-book/}
}
```

## Found an error?

If you spot a mistake, typo, or bug in the code, please
[open an issue](https://github.com/MatthBogaert/IDAFBE-book/issues).

## License

This book is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/)
(see [LICENSE.txt](LICENSE.txt)).

You are free to share and adapt this material for any noncommercial purpose, as long as you give
appropriate credit and release your adaptation under the same license. Commercial use, including
resale, requires permission from the author. The paperback/ebook edition sold via Amazon KDP is
the author's own authorized commercial edition of this same content.
