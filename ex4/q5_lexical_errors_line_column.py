"""Experiment 4, Q5: Handle Lexical Errors with Line and Column (PLY).

Illegal characters are reported with their exact line and column
numbers instead of crashing the lexer; scanning then continues
with the next character.

Sample input :  hello
                world @ test
Sample output:
    hello
    world
    Invalid: @ Line: 2 Column: 7
    test

Usage:
    python q5_lexical_errors_line_column.py
"""

import ply.lex as lex

tokens = ("ID",)
t_ignore = " \t"


def t_ID(t):
    r"[a-zA-Z]+"
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    # column = characters since the previous newline (1-based)
    line_start = t.lexer.lexdata.rfind("\n", 0, t.lexpos)
    col = t.lexpos - line_start
    print(f"Invalid: {t.value[0]} Line: {t.lineno} Column: {col}")
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input("hello\nworld @ test")

for t in lexer:
    print(t.value)
