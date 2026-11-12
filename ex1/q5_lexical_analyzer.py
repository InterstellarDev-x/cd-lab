"""Experiment 1, Q5: Basic lexical analyzer that identifies tokens.

Reads a Python source file, splits it into tokens and classifies
each one as Keyword / Identifier / Literal / Operator / Delimiter.

Usage:
    python q5_lexical_analyzer.py            # analyses program.py
    python q5_lexical_analyzer.py other.py
"""

import keyword
import re
import sys

import os

# Files live next to this script, not next to your terminal's folder.
# __file__ is this script's own path, so BASE_DIR is its folder - the
# Python equivalent of JS __dirname. Every file below is resolved
# through _path(), so the program works no matter which folder you
# run it from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def _path(name):
    """Resolve *name* against this script's folder."""
    return os.path.join(BASE_DIR, name)

# Multi-character operators must come before single characters so the
# regex matches the longest operator first (e.g. '==' not two '=').
TOKEN_RE = re.compile(
    r"\d+\.\d+|\d+|[A-Za-z_]\w*|==|!=|<=|>=|[+\-*/%=<>(),;:{}]"
)

OPERATORS = set("+-*/%=<>")
NUMBER_RE = re.compile(r"\d+(\.\d+)?$")


def classify(token):
    """Return the token class for a single token string."""
    if keyword.iskeyword(token):
        return "Keyword"
    if NUMBER_RE.match(token):
        return "Literal"
    if token in OPERATORS or token in ("==", "!=", "<=", ">="):
        return "Operator"
    if token.isidentifier():
        return "Identifier"
    return "Delimiter"


def lexical_analysis(filename):
    try:
        with open(filename, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return

    for token in TOKEN_RE.findall(code):
        print(f"{token} -> {classify(token)}")


if __name__ == "__main__":
    lexical_analysis(_path(sys.argv[1] if len(sys.argv) > 1 else "program.py"))
