"""Experiment 1, Q1 - Analyze text and report statistics.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write a program to analyze a text file and report the number of
lines, words, characters (excluding whitespace) and blank lines.

Sample run (type 3 lines: "Hello world", "", "Python is fun"):
    Lines: 3
    Words: 5
    Characters: 21
    Blank Lines: 1
"""

s = ""
n = int(input("Enter number of lines: "))
for i in range(n):
    s += input() + "\n"

l = s.splitlines()

print("Lines:", len(l))
print("Words:", len(s.split()))
print("Characters:", len("".join(s.split())))
print("Blank Lines:", sum(not x.strip() for x in l))
