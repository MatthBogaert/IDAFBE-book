"""Generate a student notebook from a book chapter .qmd file.

Usage: python gen_student_nb.py <qmd_path> <out_path> [--no-colab] [--with-text]

By default the notebook is LEAN: only the chapter title, the section headers that
contain code, and the code cells. The book's prose is not copied (students read it in the
book). Pass --with-text to also keep the prose cells (not recommended: it duplicates the
chapter and carries Quarto-only syntax such as [@cite] and footnotes).
Exception: the installation guide (appendix-installation) keeps its text, because students
actually need to read it there. Generate it with --with-text.

Parses the chapter line-by-line: level 2-4 headers become their own markdown
cells, ```{python} fences become code cells (cells marked `#| eval: false`
are dropped, other `#|` option lines are stripped), and content inside
::: {.callout-*} ... ::: divs is skipped entirely (that's book narration,
not something a student runs). Unless --no-colab is passed, a Google Colab
setup cell (mount Drive, cd into the shared course folder) is inserted right
after the title cell, matching this course's Drive layout: a "Colab
Notebooks/Data Analytics/2026" folder on MyDrive containing notebooks_student/
and data/, mirroring this repo's own top-level layout. Update the year in
COLAB_CHDIR_CELL below when this is reused for a future cohort.
"""
import json
import re
import sys
import uuid

HEADER_RE = re.compile(r"^(#{2,4})\s+(.*)")
CALLOUT_OPEN_RE = re.compile(r"^:::+\s*\{\.callout")
CALLOUT_CLOSE_RE = re.compile(r"^:::+\s*$")
CODE_FENCE_RE = re.compile(r"^```\{python\}")

COLAB_DRIVE_CELL = [
    "# Only run this cell if you're using Google Colab, not if you're running locally.\n",
    "from google.colab import drive\n",
    "drive.mount('/content/drive')\n",
]
COLAB_CHDIR_CELL = [
    "import os\n",
    'os.chdir("/content/drive/MyDrive/Colab Notebooks/Data Analytics/2026/notebooks_student")\n',
]


def new_cell(cell_type, source_lines):
    cell = {
        "cell_type": cell_type,
        "id": uuid.uuid4().hex[:8],
        "metadata": {},
        "source": source_lines,
    }
    if cell_type == "code":
        cell["execution_count"] = None
        cell["outputs"] = []
    return cell


def parse_qmd(qmd_path):
    cells = []
    callout_depth = 0
    in_code = False
    code_lines = []
    code_skip = False  # this code cell is #| eval: false -> drop entirely
    md_lines = []

    def flush_md():
        nonlocal md_lines
        text = "".join(md_lines).strip("\n")
        if text.strip():
            cells.append(new_cell("markdown", [l + "\n" for l in text.split("\n")]))
        md_lines = []

    with open(qmd_path, encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if callout_depth > 0:
            if CALLOUT_OPEN_RE.match(line):
                callout_depth += 1
            elif CALLOUT_CLOSE_RE.match(line):
                callout_depth -= 1
            continue

        if CALLOUT_OPEN_RE.match(line):
            callout_depth += 1
            continue

        if in_code:
            if line.startswith("```"):
                in_code = False
                if not code_skip and code_lines:
                    cells.append(new_cell("code", code_lines))
                code_lines = []
                code_skip = False
                continue
            if line.strip().startswith("#|"):
                if "eval: false" in line or "eval:false" in line:
                    code_skip = True
                continue
            code_lines.append(line)
            continue

        if CODE_FENCE_RE.match(line):
            flush_md()
            in_code = True
            code_lines = []
            code_skip = False
            continue

        m = HEADER_RE.match(line)
        if m:
            flush_md()
            cells.append(new_cell("markdown", [line.rstrip("\n") + "\n"]))
            continue

        md_lines.append(line)

    flush_md()
    return cells


HEADER_ANY_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*(\{[^}]*\})?\s*$")


def lean_cells(cells):
    """Keep the chapter title, headers of sections that contain code, and all code cells.
    Drop every prose markdown cell."""
    items = []  # (kind, header level, cell)
    for c in cells:
        if c["cell_type"] == "code":
            items.append(("code", 0, c))
            continue
        text = "".join(c["source"]).strip()
        first = text.split("\n")[0]
        m = HEADER_ANY_RE.match(first)
        if m and (text == first or len(m.group(1)) == 1):
            nc = dict(c)
            nc["source"] = [f"{m.group(1)} {m.group(2)}\n"]
            items.append(("hdr", len(m.group(1)), nc))
        # anything else is prose and is dropped
    out = []
    for i, (kind, level, c) in enumerate(items):
        if kind == "code" or level == 1:
            out.append(c)
            continue
        for kind2, level2, _ in items[i + 1:]:
            if kind2 == "hdr" and level2 <= level:
                break
            if kind2 == "code":
                out.append(c)
                break
    return out


def insert_colab_cell(cells):
    # Insert right after the first cell (the chapter title / intro markdown).
    insert_at = 1 if cells else 0
    cells.insert(insert_at, new_cell("code", list(COLAB_CHDIR_CELL)))
    cells.insert(insert_at, new_cell("code", list(COLAB_DRIVE_CELL)))
    return cells


def write_notebook(cells, out_path):
    nb = {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "DA2026",
                "language": "python",
                "name": "python3",
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
        f.write("\n")


if __name__ == "__main__":
    qmd_path = sys.argv[1]
    out_path = sys.argv[2]
    no_colab = "--no-colab" in sys.argv[3:]

    with_text = "--with-text" in sys.argv[3:]

    cells = parse_qmd(qmd_path)
    if not with_text:
        cells = lean_cells(cells)
    if not no_colab:
        cells = insert_colab_cell(cells)
    write_notebook(cells, out_path)
    print(f"Wrote {len(cells)} cells to {out_path}")
