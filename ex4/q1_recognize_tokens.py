"""Experiment 4, Q1: Recognize Identifiers, Numbers and Operators (PLY).

Builds a PLY lexer that tokenizes identifiers, numbers and the
operators +  -  *  /  =  and prints each token's type and value.

Sample input :  a = 10 + b
Sample output:
    ID a
    ASSIGN =
    NUM 10
    PLUS +
    ID b

Usage:
    python q1_recognize_tokens.py
"""

import ply.lex as lex

tokens = ("ID", "NUM", "PLUS", "MINUS", "MUL", "DIV", "ASSIGN")

t_PLUS = r"\+"
t_MINUS = r"-"
t_MUL = r"\*"
t_DIV = r"/"
t_ASSIGN = r"="
t_ignore = " \t"


def t_ID(t):
    r"[a-zA-Z][a-zA-Z0-9]*"
    return t


def t_NUM(t):
    r"\d+(\.\d+)?"
    return t


def t_error(t):
    print(f"Illegal character: {t.value[0]!r}")
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input("a = 10 + b")

for t in lexer:
    print(t.type, t.value)
