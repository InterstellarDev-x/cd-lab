"""Experiment 1, Q6: Remove forbidden words from a file and report.

Reads the forbidden words from *drop* file, removes every occurrence
from *source* file (rewriting it in place), and writes a report file
with how many times each forbidden word occurred.

Usage:
    python q6_remove_forbidden_words.py
    python q6_remove_forbidden_words.py source.txt drop.txt report.txt
"""

import sys
from collections import Counter

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


def sanitize(source, drop, report):
    """Remove forbidden words from *source* and write *report*."""
    try:
        with open(drop, "r") as f:
            forbidden = f.read().split()
        with open(source, "r") as f:
            words = f.read().split()
    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")
        return

    count = Counter(words)
    forbidden_set = set(forbidden)
    filtered = [w for w in words if w not in forbidden_set]

    with open(source, "w") as f:
        f.write(" ".join(filtered))

    with open(report, "w") as f:
        for word in forbidden:
            f.write(f"{word} : {count[word]} times\n")

    print("Forbidden words removed and report generated.")
    print(f"Report written to '{report}'.")


if __name__ == "__main__":
    source = sys.argv[1] if len(sys.argv) > 1 else "words.txt"
    drop = sys.argv[2] if len(sys.argv) > 2 else "drop.txt"
    report = sys.argv[3] if len(sys.argv) > 3 else "report.txt"
    sanitize(_path(source), _path(drop), _path(report))
