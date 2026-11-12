"""Experiment 2: Lexical Analyzer for Identifying Operators.

Simulates a lexical analyzer that scans a source code file, extracts
every operator, and classifies it as VALID or INVALID against the
predefined lexical rules of the language.

Operator categories (from the experiment theory):
    Arithmetic:          +  -  *  /  %
    Relational:          == != <  >  <= >=
    Assignment:          =  += -= *= /= %=
    Logical:             && || !
    Increment/Decrement: ++ --

Any other symbol used as an operator (e.g. @, &, |, ~, ^) is INVALID.

Usage:
    python q1_operator_lexical_analyzer.py            # analyses source.txt
    python q1_operator_lexical_analyzer.py other.txt
"""

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

CATEGORIES = {
    "Arithmetic": {"+", "-", "*", "/", "%"},
    "Relational": {"==", "!=", "<", ">", "<=", ">="},
    "Assignment": {"=", "+=", "-=", "*=", "/=", "%="},
    "Logical": {"&&", "||", "!"},
    "Increment/Decrement": {"++", "--"},
}

VALID_OPERATORS = set().union(*CATEGORIES.values())

# Longest match first: '++', '+=', '==', '&&' ... before '+', '=', '&'.
# A lone '&' or '|' is NOT a valid operator here, so it is not matched
# as an operator at all; any other non-alphanumeric symbol that appears
# in operator position (e.g. '@') is caught by the final alternative
# and reported invalid.
OPERATOR_RE = re.compile(
    r"\+\+|--|\+=|-=|\*=|/=|%=|==|!=|<=|>=|&&|\|\||[+\-*/%=<>!@&|^~]"
)


def category_of(op):
    """Return the category name of a valid operator, else None."""
    for name, ops in CATEGORIES.items():
        if op in ops:
            return name
    return None


def lexical_analyzer(filename):
    """Scan *filename*, list operators and classify them."""
    try:
        with open(filename, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return

    operators = OPERATOR_RE.findall(code)
    valid = [op for op in operators if op in VALID_OPERATORS]
    invalid = [op for op in operators if op not in VALID_OPERATORS]

    print("Operators found:", operators)
    print("Valid operators:", valid)
    print("Invalid operators:", invalid)

    print("\nClassification:")
    for op in operators:
        category = category_of(op)
        if category:
            print(f"  {op!r:6} -> Valid ({category})")
        else:
            print(f"  {op!r:6} -> Invalid operator")


if __name__ == "__main__":
    lexical_analyzer(_path(sys.argv[1] if len(sys.argv) > 1 else "source.txt"))
