"""Experiment 4, Q4 - PLY: store tokens in separate files by type.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code to store tokens in separate files based on
their type: keywords.txt, identifiers.txt, operators.txt, numbers.txt.

Example input:  int a = 10 + 20 if b * 5
Resulting files:
    keywords.txt    -> int, if
    identifiers.txt -> a, b
    operators.txt   -> =, +, *
    numbers.txt     -> 10, 20, 5
"""

import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'for': 'FOR',
    'int': 'INT',
}

tokens = ('ID', 'NUMBER', 'OPERATOR', 'ASSIGN') + tuple(reserved.values())

t_OPERATOR = r'[+\-*/]'
t_ASSIGN = r'='


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    return t


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


t_ignore = ' \t'


def t_error(t):
    t.lexer.skip(1)


lexer = lex.lex()

s = input("Enter code: ")
lexer.input(s)

files = {
    'keywords': open("keywords.txt", "w"),
    'identifiers': open("identifiers.txt", "w"),
    'operators': open("operators.txt", "w"),
    'numbers': open("numbers.txt", "w"),
}

for t in lexer:
    if t.type in reserved.values():
        files['keywords'].write(t.value + "\n")
    elif t.type == 'ID':
        files['identifiers'].write(t.value + "\n")
    elif t.type in ('OPERATOR', 'ASSIGN'):
        files['operators'].write(t.value + "\n")
    elif t.type == 'NUMBER':
        files['numbers'].write(t.value + "\n")

for f in files.values():
    f.close()

print("Tokens saved successfully!")
