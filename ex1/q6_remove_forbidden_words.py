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

source = input("Enter source file: ")
drop = input("Enter report file: ")

text = input("Enter text: ")
forbidden = input("Enter forbidden words: ").split()

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
