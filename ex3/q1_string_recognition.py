"""Experiment 3 - String recognition for a*, a*b+ and abb.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Aim: To write a Python program to recognize strings matching the
patterns a*, a*b+, and abb.

Sample input:  aaa
Sample output: Matches a*

NOTE (kept as in the PDF): the checks are an if/elif chain, so "abb"
is reported as "Matches a*b+" - the a*b+ branch matches first and the
"abb" branch is never reached. The chain is preserved here exactly as
the PDF prints it.
"""

import re

s = input("Enter a string: ")

if re.fullmatch("a*", s):
    print("Matches a*")
elif re.fullmatch("a*b+", s):
    print("Matches a*b+")
elif re.fullmatch("abb", s):
    print("Matches abb")
else:
    print("String not matched")
