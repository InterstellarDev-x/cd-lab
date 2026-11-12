"""Experiment 4, Q2: Ignore Whitespace and Comments (PLY).

A PLY lexer that skips whitespace and both kinds of comments:
    // single-line comment
    /* multi-line comment */
Only real tokens (here: identifiers) are returned.

Sample input :  hello //comment
                /*test*/ world
Sample output:
    hello
    world

Usage:
    python q2_ignore_whitespace_comments.py
"""

import ply.lex as lex

tokens = ("ID",)
t_ignore = " \t"


def t_COMMENT(t):
    r"//.*|/\*[\s\S]*?\*/"
    pass  # no return value -> token is discarded


def t_ID(t):
    r"[a-zA-Z]+"
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Illegal character: {t.value[0]!r}")
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input("hello //comment\n/*test*/ world")

for t in lexer:
    print(t.value)
