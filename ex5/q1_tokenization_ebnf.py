"""Experiment 5, Q1 - Scanner with Lark: tokenize and categorize tokens.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code using Lark to tokenize a program, separate
identifiers, numbers, operators and keywords into different files and
print a frequency report for each file.

Install: python3 -m pip show lark   (install with: pip install lark)

Sample input (type END to finish):
    int foo = 10; int bar = 20; foo = f00 + bar;
    END
Result: identifiers.txt, numbers.txt, operators.txt, keywords.txt are
created, each followed by a value : count report, e.g. identifiers.txt
lists foo : 2, bar : 2, f00 : 1.
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
