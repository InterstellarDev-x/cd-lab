"""Experiment 5, Q2: Ignoring Whitespace and Comments (Lark).

%ignore rules drop whitespace, // single-line comments and
/* multi-line comments */ before parsing, so only real statements
reach the parser.

Sample input:
    // single line comment
    x = 10; /* multi-line comment */
    y = 20;

Output: only the two valid statements are parsed; comments and
spaces are ignored.

Note: the manual's grammar allows only ONE statement
("start: IDENTIFIER ..."), so its own two-statement sample fails
to parse. The rule below accepts one or more statements.

Usage:
    python q2_ignore_whitespace_comments.py
    pip install lark
"""

from lark import Lark

grammar = r"""
start: statement+

statement: IDENTIFIER "=" NUMBER ";"

IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+/

%ignore WS
%ignore /\/\/.*/
%ignore /\/\*[\s\S]*?\*\//

WS: /[ \t\n]+/
"""

parser = Lark(grammar, parser="lalr")

data = """
// single line comment
x = 10; /* multi-line comment */
y = 20;
"""

print(parser.parse(data).pretty())
print("Only valid statements are parsed; comments and spaces are ignored.")
