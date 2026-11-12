"""Experiment 1, Q6 - Remove forbidden words from a file, generate report.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Remove forbidden words from a text file and write a report
file giving how many times each forbidden word occurred.

Sample run (source: source.txt, report: drop.txt,
text: "hello world hello", forbidden: "hello"):
    Words removed and report generated!
    source.txt then contains "world"
    drop.txt then contains "hello : 2 times"
"""

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

source = input("Enter source file: ")
drop = input("Enter report file: ")

text = input("Enter text: ")
forbidden = input("Enter forbidden words: ").split()

source = _path(source)
drop = _path(drop)

f = open(source, "w")
f.write(text)
f.close()

count = Counter(text.split())
new = [w for w in text.split() if w not in forbidden]

f = open(source, "w")
f.write(" ".join(new))
f.close()

f = open(drop, "w")
for w in forbidden:
    f.write(w + " : " + str(count[w]) + " times\n")
f.close()
print("Words removed and report generated!")
