"""Experiment 7, Q1: Arithmetic Expression Parser using PLY.

A PLY (Python Lex-Yacc) parser for arithmetic expressions that
validates the syntax and evaluates the result. Grammar:

    E -> E + T | E - T | T
    T -> T * F | T / F | F
    F -> (E) | NUMBER

The grammar itself encodes precedence (* and / bind tighter than
+ and -) and left associativity, and PLY implements it with LALR(1).

Sample input/output:
    3 + 4 * 2     -> Result = 11.0
    (5 + 3) * 2   -> Result = 16.0
    10 / 2 + 6    -> Result = 11.0

Usage:
    python q1_arithmetic_parser.py              # interactive prompt
    python q1_arithmetic_parser.py "3 + 4 * 2"  # evaluate and exit
    pip install ply
"""

import sys

import ply.lex as lex
import ply.yacc as yacc

# -------------------------
# Token List
# -------------------------
tokens = (
    "NUMBER",
    "PLUS", "MINUS", "TIMES", "DIVIDE",
    "LPAREN", "RPAREN",
)

# -------------------------
# Regular Expressions
# -------------------------
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"

t_ignore = " \t"


# -------------------------
# Number Token
# -------------------------
def t_NUMBER(t):
    r"\d+(\.\d+)?"
    t.value = float(t.value)
    return t


# -------------------------
# Newline Handling
# -------------------------
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# -------------------------
# Error Handling
# -------------------------
def t_error(t):
    print("Illegal character:", t.value[0])
    t.lexer.skip(1)


# Build Lexer
lexer = lex.lex()


# -------------------------
# Grammar Rules
# -------------------------
def p_expression_plus(p):
    "expression : expression PLUS term"
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    "expression : expression MINUS term"
    p[0] = p[1] - p[3]


def p_expression_term(p):
    "expression : term"
    p[0] = p[1]


def p_term_times(p):
    "term : term TIMES factor"
    p[0] = p[1] * p[3]


def p_term_divide(p):
    "term : term DIVIDE factor"
    if p[3] == 0:
        print("Error: division by zero")
        p[0] = 0
    else:
        p[0] = p[1] / p[3]


def p_term_factor(p):
    "term : factor"
    p[0] = p[1]


def p_factor_number(p):
    "factor : NUMBER"
    p[0] = p[1]


def p_factor_expr(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]


# -------------------------
# Syntax Error Rule
# -------------------------
def p_error(p):
    if p:
        print(f"Syntax Error at token: {p.type} ({p.value!r})")
    else:
        print("Syntax Error: unexpected end of input")


# Build Parser
parser = yacc.yacc()


# -------------------------
# Driver Code
# -------------------------
def evaluate(s):
    result = parser.parse(s, lexer=lexer)
    if result is not None:
        print("Result =", result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for expr in sys.argv[1:]:
            print(expr, "=>", end=" ")
            evaluate(expr)
    else:
        while True:
            try:
                s = input("Enter expression (or exit): ")
            except (EOFError, KeyboardInterrupt):
                break
            if s.strip() == "exit":
                break
            if not s.strip():
                continue
            try:
                evaluate(s)
            except Exception as e:
                print("Error:", e)
