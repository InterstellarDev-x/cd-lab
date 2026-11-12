"""Experiment 5, Q3: Line and Column Number Reporting (Lark).

With propagate_positions=True every token carries its line and
column, which is how a real compiler points at the exact place
an error or token came from.

Sample input :  hello world
                compiler lab
Sample output:
    WORD : hello @ line 1, column 1
    WORD : world @ line 1, column 7
    WORD : compiler @ line 2, column 1
    WORD : lab @ line 2, column 10

Usage:
    python q3_line_column_reporting.py
    pip install lark
"""

from lark import Lark, Token

grammar = r"""
start: WORD+
WORD: /[a-zA-Z_]+/
%ignore WS
WS: /[ \t\n]+/
"""

parser = Lark(grammar, parser="lalr", propagate_positions=True)

data = "hello world\ncompiler lab"
tree = parser.parse(data)

for token in tree.scan_values(lambda v: isinstance(v, Token)):
    print(f"{token.type} : {token.value} @ line {token.line}, column {token.column}")
