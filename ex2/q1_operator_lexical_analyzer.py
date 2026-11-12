"""Experiment 2 - Operator validation.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Aim: To write a Python program that identifies and validates operators
in the given source code.

Sample input:  a = b + c * 10 >= 20
Sample output:
    Operators found:
    = -> Valid Operator
    + -> Valid Operator
    * -> Valid Operator
    >= -> Valid Operator
"""

import re

code = input("Enter source code: ")

operators = re.findall(r'==|!=|<=|>=|[+\-*/%=<>]', code)

print("Operators found:")
for op in operators:
    print(op, "-> Valid Operator")
