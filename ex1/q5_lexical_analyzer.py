"""Experiment 1, Q5 - Basic lexical analyzer to identify tokens.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Identify tokens in a line of code and classify each as
Keyword, Identifier, Literal, Operator or Delimiter.

Sample run (input: "int a = 10 + b;"):
    int -> Identifier
    a -> Identifier
    = -> Operator
    10 -> Literal
    + -> Operator
    b -> Identifier

NOTE (kept as in the PDF): the token regex does not include ';', so a
semicolon produces no token, and "int" is a Python builtin rather than
a keyword, so keyword.iskeyword("int") is False and it classifies as
an Identifier. Both are the PDF program's own behaviour, preserved here.
"""

import keyword
import re

code = input("Enter code: ")

tokens = re.findall(r'\b\w+\b|[+\-*/%=<>(),]', code)

for t in tokens:
    if keyword.iskeyword(t):
        print(t, "-> Keyword")
    elif t.isidentifier():
        print(t, "-> Identifier")
    elif t.isnumeric():
        print(t, "-> Literal")
    elif t in "+-*/%=<>":
        print(t, "-> Operator")
    else:
        print(t, "-> Delimiter")
