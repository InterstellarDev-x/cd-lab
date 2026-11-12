"""Experiment 4, Q3 - PLY: restrict identifier length to 10 characters.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code to restrict identifier length to 10
characters and print an error message if an identifier exceeds this
limit.

Example input:  hello student programming
Example output:
    Identifier: hello
    Identifier: student
    Error: Identifier too long: programming
"""

import ply.lex as lex

tokens = ('ID',)


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if len(t.value) > 10:
        print("Error: Identifier too long:", t.value)
    else:
        return t


t_ignore = ' \t'


def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()

s = input("Enter identifiers: ")
lexer.input(s)
for token in lexer:
    print("Identifier:", token.value)
