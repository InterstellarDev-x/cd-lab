"""Experiment 5, Q4 - Custom error handling using Lark.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code using LALR parsing and an on_error callback
to handle unexpected tokens. Insert a missing comma or semicolon and
resume parsing.

Test input:  int apple banana
Expected output:
    Missing semicolon inserted
    Corrected code: int apple,banana;
    (then the corrected parse tree)

FIX vs the PDF: the PDF's comma-insertion regex
    re.sub(r'([a-zA-Z_][a-zA-Z0-9_]*)\\s+([a-zA-Z_][a-zA-Z0-9_]*)',
           r'\\1,\\2', code, count=1)
matches the FIRST identifier pair it sees, which is "int apple" - it
would turn the code into "int,apple banana;", which then fails to
parse. The fix below applies the same substitution only to the part
after the leading "int" keyword, so the comma lands between the two
names ("apple banana" -> "apple,banana") as intended.
"""

import re
from lark import Lark

grammar = """
start: INT NAME (COMMA NAME)* SEMICOLON

INT: "int"
NAME: /[a-zA-Z_][a-zA-Z0-9_]*/
COMMA: ","
SEMICOLON: ";"

%import common.WS
%ignore WS
"""

parser = Lark(grammar, parser="lalr")

code = input("Enter code: ").strip()

if not code.endswith(";"):
    code += ";"
    print("Missing semicolon inserted")

# Insert a comma between two names that are missing one, without
# touching the leading "int" keyword (see the FIX note above).
head, sep, rest = code.partition(" ")
if sep:
    rest = re.sub(
        r'([a-zA-Z_][a-zA-Z0-9_]*)\s+([a-zA-Z_][a-zA-Z0-9_]*)',
        r'\1,\2', rest, count=1,
    )
    code = head + sep + rest

print("Corrected code:", code)

try:
    tree = parser.parse(code)
    print("\nCorrected Parse Tree:")
    print(tree.pretty())
except Exception as e:
    print("Syntax Error:", e)
