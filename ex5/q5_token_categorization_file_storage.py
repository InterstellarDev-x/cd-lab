"""Experiment 5, Q5 - Separate tokens into different files using Lark.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Aim: To write a Python program using Lark that separates identifiers,
numbers, operators, and keywords into different files and generates a
frequency report.

Sample input (type END to finish):
    int foo = 10; int bar = 20; foo = foo + bar;
    END

NOTE: in the PDF this program is the same tokenize-and-categorize
program as Q1 (only the sample input differs), so it is identical to
q1_tokenization_ebnf.py apart from this docstring.
"""

from lark import Lark
from collections import Counter

grammar = r"""
start: (KEYWORD | IDENTIFIER | NUMBER | OPERATOR | DELIMITER)*

KEYWORD.2: "int" | "float" | "if" | "else" | "while" | "return"
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /[0-9]+(\.[0-9]+)?/
OPERATOR: "==" | "!=" | "<=" | ">=" | "+" | "-" | "*" | "/" | "=" | "<" | ">"
DELIMITER: "(" | ")" | "{" | "}" | ";" | ","

%import common.WS
%ignore WS
"""

parser = Lark(grammar, parser="lalr", lexer="basic")

print("Enter program (type END to finish):")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

code = "\n".join(lines)

data = {"IDENTIFIER": [], "NUMBER": [], "OPERATOR": [], "KEYWORD": []}

for token in parser.lex(code):
    if token.type in data:
        data[token.type].append(token.value)

files = {
    "IDENTIFIER": "identifiers.txt",
    "NUMBER": "numbers.txt",
    "OPERATOR": "operators.txt",
    "KEYWORD": "keywords.txt",
}

for category, filename in files.items():
    with open(filename, "w") as f:
        for value in data[category]:
            f.write(value + "\n")
    print("\n" + filename)
    for value, count in Counter(data[category]).items():
        print(value, ":", count)

print("\nFiles created successfully!")
