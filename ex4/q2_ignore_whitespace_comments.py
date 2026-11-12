"""Experiment 4, Q2 - PLY: ignore whitespace, tabs and comments.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code to ignore whitespace, tabs, and comments
(// single-line and /* multi-line */) in the input source program
using PLY.

Example input:  a + 10 // comment
Example output:
    ID : a
    PLUS : +
    NUMBER : 10
"""

import ply.lex as lex

tokens = ('ID', 'NUMBER', 'PLUS')

t_PLUS = r'\+'


def t_COMMENT(t):
    r'//.*|/\*[\s\S]*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t


def t_NUMBER(t):
    r'\d+'
    return t


t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()

s = input("Enter code: ")
lexer.input(s)
for token in lexer:
    print(token.type, ":", token.value)
