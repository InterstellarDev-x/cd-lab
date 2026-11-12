"""Experiment 5, Q2 - Ignore whitespace and comments in Lark.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code to ignore spaces, tabs, newlines,
single-line comments (//) and block comments (/* */). Print only
meaningful tokens.

Sample input (type END to finish - one line of code per line):
    int a = 10;
    // variable
    /* This is a comment */
    float b = 3.14;
    END
Sample output (meaningful tokens only):
    KEYWORD : int
    IDENTIFIER : a
    OPERATOR : =
    NUMBER : 10
    DELIMITER : ;
    KEYWORD : float
    IDENTIFIER : b
    OPERATOR : =
    NUMBER : 3.14
    DELIMITER : ;

NOTE: a // comment runs to the end of its line, so anything typed after
// on the same line is also treated as a comment. Put the comment on
its own line (as above) when more code follows it.
"""

from lark import Lark

grammar = r"""
start: (KEYWORD | IDENTIFIER | NUMBER | OPERATOR | DELIMITER)*

KEYWORD.2: "int" | "float" | "if" | "else" | "while" | "return"
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /[0-9]+(\.[0-9]+)?/
OPERATOR: "==" | "!=" | "<=" | ">=" | "+" | "-" | "*" | "/" | "=" | "<" | ">"
DELIMITER: "(" | ")" | "{" | "}" | ";" | ","

COMMENT: /\/\/[^\n]*/ | /\/\*[\s\S]*?\*\//

%import common.WS
%ignore WS
%ignore COMMENT
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

print("Meaningful Tokens:")
for token in parser.lex(code):
    print(token.type, ":", token.value)
