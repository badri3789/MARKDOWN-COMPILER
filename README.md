# MARKDOWN-COMPILER

A small, dependency-light Python CLI and library to convert Markdown files to HTML using the Python-Markdown engine. Intended for local build pipelines, classroom labs, and simple static site generation.

Features
- Convert Markdown files or stdin to HTML
- Support for Markdown extensions via config file (JSON/YAML)
- Simple CLI and importable library API for programmatic use

Quick start

Recommended: create and activate a Python virtual environment.

Install runtime dependencies:

```bash
pip install -r requirements.txt
```

Usage (CLI)

Convert a Markdown file to stdout:

```bash
python -m markdown_compiler input.md
```

Write output to a file:

```bash
python -m markdown_compiler input.md --output out.html
```

Read from stdin:

```bash
cat input.md | python -m markdown_compiler --output out.html
```

Library usage

```py
from markdown_compiler import convert
html = convert("**bold**")
```

Development

- Run tests:

```bash
pip install -r requirements.txt
pytest
```

Contributing

- Open issues or pull requests against branch `restructure-readme`.
- Follow the existing style (black/flake8 recommended).

License

This project includes code derived from the Python-Markdown project (BSD license). The repository is released under the BSD 3-Clause license. See LICENSE for details.
