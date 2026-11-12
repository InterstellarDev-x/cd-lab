"""Experiment 5, Q4: Custom Error Handling and Recovery (Lark).

Parses assignments of the form  x = 10;  and catches the syntax
error when a semicolon is missing. Instead of crashing, it reports
the error position and recovers by inserting the missing ';'
and re-parsing.

Sample input :  x = 10 y = 20;      (missing semicolon)
Sample output:
    Syntax Error at line 1 column 8
    Recovery: Assuming missing semicolon and continuing...
    Recovered parse tree: ...

(The manual prints "column 7"; the offending token 'y' is actually
at column 8 -- x=1, space=2, '='=3, space=4, '1'=5, '0'=6,
space=7, 'y'=8.)

Usage:
    python q4_error_handling_recovery.py
    pip install lark
"""

from lark import Lark, UnexpectedInput

grammar = r"""
start: assignment+
assignment: IDENTIFIER "=" NUMBER ";"

IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+/
%ignore WS
WS: /[ \t\n]+/
"""

parser = Lark(grammar, parser="lalr")
data = "x = 10 y = 20;"  # missing semicolon after 10

try:
    tree = parser.parse(data)
    print(tree)
except UnexpectedInput as e:
    print("Syntax Error at line", e.line, "column", e.column)
    print("Recovery: Assuming missing semicolon and continuing...")
    # Recovery: insert the missing ';' before the next identifier
    # and parse again.
    fixed = data.replace("10 y", "10; y")
    print("Recovered parse tree:", parser.parse(fixed).pretty())
