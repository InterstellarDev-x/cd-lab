"""Experiment 4, Q3: Restrict Identifier Length to 10 Characters (PLY).

Identifiers longer than 10 characters are rejected as invalid:
the lexer prints an "Invalid" message and drops the token instead
of returning it.

Sample input :  hello student123456
Sample output:
    hello
    Invalid: student123456

Usage:
    python q3_identifier_length_limit.py
"""

import ply.lex as lex

tokens = ("ID",)
t_ignore = " \t"
MAX_ID_LENGTH = 10


def t_ID(t):
    r"[a-zA-Z][a-zA-Z0-9]*"
    if len(t.value) > MAX_ID_LENGTH:
        print("Invalid:", t.value)
        # no return -> token is discarded
    else:
        return t


def t_error(t):
    print(f"Illegal character: {t.value[0]!r}")
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input("hello student123456")

for t in lexer:
    print(t.value)
