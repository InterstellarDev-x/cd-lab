"""Experiment 5, Q1: Tokenization Using EBNF Grammar (Lark).

Defines a mini-language grammar in EBNF and uses Lark to tokenize
a program: keywords, identifiers, numbers, operators and delimiters.

Sample input :  int x = 10; y = x + 3.14;
Sample output:
    KEYWORD int
    IDENTIFIER x
    OP =
    NUMBER 10
    DELIM ;
    IDENTIFIER y
    OP =
    IDENTIFIER x
    OP +
    NUMBER 3.14
    DELIM ;

Two fixes were needed to make the manual's program actually run:

1. The manual's grammar has no declaration form, so its own sample
   input ("int x = 10; ...") fails to parse. A declaration
   alternative (KEYWORD IDENTIFIER "=" expr ";") was added.
2. Lark's lexer returns "int" as an IDENTIFIER (the identifier
   pattern also matches it), so keywords are recognised by value
   against a keyword table -- exactly how real lexers do it. The
   anonymous "=" and ";" terminals are shown as OP / DELIM.

(The manual prints an abbreviated sample: only the KEYWORD /
IDENTIFIER / NUMBER lines. This program prints the full stream.)

Usage:
    python q1_tokenization_ebnf.py
    pip install lark
"""

from lark import Lark

KEYWORDS = {"int", "float", "if", "else", "while", "return"}

# Anonymous "=" and ";" in the rules surface as EQUAL / SEMICOLON.
DISPLAY = {"EQUAL": "OP", "SEMICOLON": "DELIM"}

grammar = r"""
?start: statement+

statement: IDENTIFIER "=" expr ";" | KEYWORD IDENTIFIER "=" expr ";"
?expr: term (OP term)*
?term: NUMBER | IDENTIFIER

KEYWORD: "int" | "float" | "if" | "else" | "while" | "return"
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+(\.\d+)?/
OP: "+" | "-" | "*" | "/" | "==" | "!=" | "<" | ">" | "<=" | ">="

%ignore WS
WS: /[ \t\n]+/
"""

# Earley + dynamic lexer: the manual's LALR grammar cannot accept its
# own sample input, because "int" lexes as IDENTIFIER and LALR(1)
# cannot then choose the declaration alternative.
parser = Lark(grammar, parser="earley", lexer="dynamic")
data = "int x = 10; y = x + 3.14;"

# Validate the syntax first, then stream the tokens.
parser.parse(data)

for token in parser.lex(data):
    if token.type == "IDENTIFIER" and token.value in KEYWORDS:
        shown = "KEYWORD"
    else:
        shown = DISPLAY.get(token.type, token.type)
    print(shown, token.value)
