"""Experiment 4, Q1 - PLY lexical analyzer: identifiers, numbers, operators.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code using PLY to implement a lexical analyzer
that recognizes identifiers (letters followed by letters/digits),
numbers (integers and floats), arithmetic operators (+, -, *, /) and
the assignment operator (=).

Install: python3 -m pip install ply

Example input:  a = 10 + b * 5.5
Example output:
    ID : a
    ASSIGN : =
    NUMBER : 10
    OPERATOR : +
    ID : b
    OPERATOR : *
    NUMBER : 5.5
"""

import ply.lex as lex

tokens = ('ID', 'NUMBER', 'OPERATOR', 'ASSIGN')

t_OPERATOR = r'[+\-*/]'
t_ASSIGN = r'='


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    return t


t_ignore = ' \t'


def t_error(t):
    print("Invalid character:", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

s = input("Enter code: ")
lexer.input(s)
for token in lexer:
    print(token.type, ":", token.value)
