"""Experiment 7, Q1 - Arithmetic expression parser using PLY.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Question: Write Python code using PLY to parse and evaluate arithmetic
expressions with +, -, *, / and parentheses, respecting operator
precedence.

Install: python3 -m pip install ply

Sample session:
    Enter expression (or exit): 3 + 4 * 2
    Result = 11.0
    Enter expression (or exit): (2 + 3) * 4
    Result = 20.0
    Enter expression (or exit): exit
"""

import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

t_ignore = ' \t'


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]


def p_expression_term(p):
    'expression : term'
    p[0] = p[1]


def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]


def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]


def p_error(p):
    print("Syntax Error at token:", p)


parser = yacc.yacc()

while True:
    try:
        s = input("Enter expression (or exit): ")
        if s == "exit":
            break
        result = parser.parse(s)
        print("Result =", result)
    except Exception as e:
        print("Error:", e)
