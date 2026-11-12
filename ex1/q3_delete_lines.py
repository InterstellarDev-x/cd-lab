"""Experiment 1, Q3: Delete specified line numbers from a text file.

Removes the given 1-based line numbers in place and reports what
was deleted. Lines that do not exist are ignored.

Usage:
    python q3_delete_lines.py            # deletes lines 3 and 6 of lines.txt
    python q3_delete_lines.py file.txt 2 5
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


def delete_lines(filename, remove_lines):
    """Delete lines whose 1-based numbers are in *remove_lines*."""
    remove = set(remove_lines)
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return

    removed = [i for i in sorted(remove) if 1 <= i <= len(lines)]
    kept = [line for i, line in enumerate(lines, start=1) if i not in remove]

    with open(filename, "w") as f:
        f.writelines(kept)

    if removed:
        print(f"Removed line(s) {removed} from '{filename}'.")
    else:
        print("No matching lines to remove.")
    print("Specified lines removed successfully.")


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "lines.txt"
    numbers = [int(a) for a in sys.argv[2:]] if len(sys.argv) > 2 else [3, 6]
    delete_lines(_path(filename), numbers)
