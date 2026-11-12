"""Experiment 4, Q5 - PLY: handle lexical errors gracefully.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code to handle lexical errors gracefully:
detect illegal characters, print the line and column number of the
error, skip the invalid character and continue scanning.

Example input (type END to finish):
    a + 10 b @ 20
    END
Example output:
    ID : a
    PLUS : +
    NUMBER : 10
    ID : b
    Illegal character: @ Line: 1 Column: 10
    NUMBER : 20
"""

import ply.lex as lex

tokens = ('ID', 'NUMBER', 'PLUS')

t_PLUS = r'\+'


def t_ID(t):
    r'[a-zA-Z]+'
    return t


def t_NUMBER(t):
    r'\d+'
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    line = t.lexer.lineno
    col = t.lexpos - t.lexer.lexdata.rfind('\n', 0, t.lexpos)
    print("Illegal character:", t.value[0], "Line:", line, "Column:", col)
    t.lexer.skip(1)


lexer = lex.lex()

print("Enter code (type END to finish):")
s = ""
while True:
    line = input()
    if line == "END":
        break
    s += line + "\n"

lexer.input(s)
for token in lexer:
    print(token.type, ":", token.value)
