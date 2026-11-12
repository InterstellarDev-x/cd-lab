"""Experiment 1, Q1: Analyse a text file and report statistics.

Reports number of lines, blank lines, words, and characters
(excluding all whitespace).

Usage:
    python q1_file_stats.py            # analyses input.txt
    python q1_file_stats.py other.txt  # analyses another file
"""

import sys


def analyze_file(filename):
    """Read *filename* and print line/word/character statistics."""
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found.")
        return

    total_lines = len(lines)
    blank_lines = sum(1 for line in lines if line.strip() == "")
    total_words = sum(len(line.split()) for line in lines)
    # characters excluding ALL whitespace (spaces, tabs, newlines)
    total_chars = sum(1 for line in lines for ch in line if not ch.isspace())

    print("Lines:", total_lines)
    print("Blank Lines:", blank_lines)
    print("Words:", total_words)
    print("Characters:", total_chars)


if __name__ == "__main__":
    analyze_file(sys.argv[1] if len(sys.argv) > 1 else "input.txt")
