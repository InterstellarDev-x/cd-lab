"""Experiment 1, Q4: Copy a file to another file after removing comments.

A line is treated as a comment when, after stripping leading
whitespace, it starts with '#'. All other lines are copied as-is.

Usage:
    python q4_remove_comments.py
    python q4_remove_comments.py source.txt destination.txt
"""

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


def copy_clean(src, dest):
    """Copy *src* to *dest*, skipping full-line '#' comments."""
    try:
        with open(src, "r") as s, open(dest, "w") as d:
            for line in s:
                if not line.strip().startswith("#"):
                    d.write(line)
    except FileNotFoundError:
        print(f"Error: file '{src}' not found.")
        return
    print(f"File copied after removing comments: '{src}' -> '{dest}'")


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "source.txt"
    dest = sys.argv[2] if len(sys.argv) > 2 else "destination.txt"
    copy_clean(_path(src), _path(dest))
