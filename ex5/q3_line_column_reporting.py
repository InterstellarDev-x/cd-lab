"""Experiment 5, Q3 - Display line and column numbers for each token.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code to access token metadata (line and column)
in Lark and print token type, value, line number, and column number.

Sample input (type END to finish):
    int a = 10;
    float b = 3.14;
    END
Sample output:
    KEYWORD : int @ line 1 , column 1
    IDENTIFIER : a @ line 1 , column 5
    OPERATOR : = @ line 1 , column 7
    NUMBER : 10 @ line 1 , column 9
    DELIMITER : ; @ line 1 , column 11
    KEYWORD : float @ line 2 , column 1
    ...
"""

from lark import Lark

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

print("Enter code (type END to finish):")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

code = "\n".join(lines)

print("\nToken Information:")

for token in parser.lex(code):
    print(
        token.type, ":", token.value,
        "@ line", token.line, ", column", token.column,
    )
