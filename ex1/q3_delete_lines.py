"""Experiment 1, Q3 - Delete specified line numbers from a text file.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Read lines from the user, then delete the line numbers given
and print the remaining lines.

Sample run (4 lines: one, two, three, four; delete line 2):
    one
    three
    four
"""

n = int(input("Enter number of lines: "))
lines = []

for i in range(n):
    lines.append(input("Enter line: "))

d = list(map(int, input("Enter line numbers to delete: ").split()))

for i in range(n):
    if i + 1 not in d:
        print(lines[i])
