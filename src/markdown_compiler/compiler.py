"""
A small wrapper package that exposes a convert() function and a CLI for
converting Markdown to HTML using the `markdown` package.

This module preserves the original copyright header from the Python-Markdown
project where applicable.
"""

# Preserve original attribution header (trimmed)
# Copyright 2007-2018 The Python Markdown Project (v. 1.7 and later)
# Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b)
# Copyright 2004 Manfred Stienstra (the original version)
# License: BSD (see LICENSE for details)

import sys
import codecs
import logging
from typing import Optional, List, Dict

import markdown

logger = logging.getLogger(__name__)


def convert(
    text: str,
    extensions: Optional[List[str]] = None,
    extension_configs: Optional[Dict] = None,
    output_format: str = "xhtml",
) -> str:
    """Convert Markdown text to HTML.

    Args:
        text: Markdown source text.
        extensions: list of extension names to load (optional).
        extension_configs: mapping of extension configuration (optional).
        output_format: 'xhtml' or 'html'.

    Returns:
        HTML string.
    """
    if extensions is None:
        extensions = []
    if extension_configs is None:
        extension_configs = {}

    return markdown.markdown(
        text, extensions=extensions, extension_configs=extension_configs, output_format=output_format
    )


# CLI helpers (lightweight)
import argparse


def parse_args(argv=None):
    parser = argparse.ArgumentParser(prog="markdown_compiler")
    parser.add_argument("input", nargs="?", help="Input Markdown file (defaults to stdin)")
    parser.add_argument("-o", "--output", dest="output", help="Write output to OUTPUT_FILE. Defaults to stdout.")
    parser.add_argument("-e", "--encoding", dest="encoding", default="utf-8", help="Encoding for input and output files.")
    parser.add_argument("-x", "--extension", action="append", dest="extensions", help="Load extension EXTENSION.")
    parser.add_argument("-c", "--config", dest="configfile", help="JSON/YAML file for extension configs.")
    parser.add_argument("--output-format", dest="output_format", choices=["xhtml", "html"], default="xhtml")
    return parser.parse_args(argv)


def _read_config(path, encoding="utf-8"):
    import json
    try:
        import yaml
        loader = yaml.safe_load
    except Exception:
        loader = json.load

    with codecs.open(path, "r", encoding=encoding) as fp:
        return loader(fp)


def main(argv=None):
    args = parse_args(argv)

    if args.input:
        with codecs.open(args.input, "r", encoding=args.encoding) as fp:
            md = fp.read()
    else:
        # read from stdin
        md = sys.stdin.read()

    extension_configs = {}
    if args.configfile:
        try:
            extension_configs = _read_config(args.configfile, args.encoding)
        except Exception as e:
            logger.error("Failed to parse config file %s: %s", args.configfile, e)
            sys.exit(2)

    html = convert(md, extensions=args.extensions or [], extension_configs=extension_configs, output_format=args.output_format)

    if args.output:
        with codecs.open(args.output, "w", encoding=args.encoding) as fp:
            fp.write(html)
    else:
        sys.stdout.write(html)


if __name__ == "__main__":
    main()
