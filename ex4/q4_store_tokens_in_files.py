"""Experiment 4, Q4: Store Tokens in Separate Files (PLY).

Each token is appended to the file for its category as it is scanned:
    identifiers.txt  <- ID tokens
    numbers.txt      <- NUM tokens
    operators.txt    <- PLUS tokens
    keywords.txt     <- reserved words (int, float, if, else, while, return)

Files are cleared at the start so repeated runs do not duplicate rows.

Sample input :  abc 123 + xyz
Sample output:
    ID abc
    NUM 123
    PLUS +
    ID xyz
Files created: keywords.txt, identifiers.txt, operators.txt, numbers.txt

Usage:
    python q4_store_tokens_in_files.py
"""

import ply.lex as lex

# Reserved words are recognised inside t_ID and re-typed as KEYWORD.
RESERVED = {"int", "float", "if", "else", "while", "return"}

tokens = ("ID", "NUM", "PLUS", "KEYWORD")
t_ignore = " \t"


def t_PLUS(t):
    r"\+"
    _store(t)
    return t

FILES = {
    "ID": "identifiers.txt",
    "NUM": "numbers.txt",
    "PLUS": "operators.txt",
    "KEYWORD": "keywords.txt",
}


def _store(token):
    """Append *token* to its category file."""
    with open(FILES[token.type], "a") as f:
        f.write(token.value + "\n")


def t_ID(t):
    r"[a-zA-Z]+"
    if t.value in RESERVED:
        t.type = "KEYWORD"
    _store(t)
    return t


def t_NUM(t):
    r"\d+"
    _store(t)
    return t


def t_error(t):
    print(f"Illegal character: {t.value[0]!r}")
    t.lexer.skip(1)


# Clear the output files once, before scanning.
for filename in FILES.values():
    open(filename, "w").close()

lexer = lex.lex()
lexer.input("abc 123 + xyz")

for t in lexer:
    print(t.type, t.value)

print("Files created: keywords.txt, identifiers.txt, operators.txt, numbers.txt")
