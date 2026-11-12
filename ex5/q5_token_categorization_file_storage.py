"""Experiment 5, Q5: Token Categorization and File Storage (Lark).

Tokenizes a program, sorts the tokens into identifiers, numbers,
operators and keywords, writes each category to its own file, and
prints the frequency of every token.

Sample input :  int x = 10 x = x + 5 return x
Sample output:
    Identifier Frequency: {'x': 4}
    Number Frequency: {'10': 1, '5': 1}
    Operator Frequency: {'=': 2, '+': 1}
    Keyword Frequency: {'int': 1, 'return': 1}

(The manual prints {'x': 3}, but x occurs 4 times in its own
sample input -- after "int", after "10", after the second "=",
and after "return". The count here is the correct one.)

Notes on the manual's version:
- It defines WORD as an UPPERCASE name, which makes Lark treat it
  as a *terminal*: every token then has type WORD and the
  categorization finds nothing. WORD is a lowercase *rule* here,
  so tokens keep their own types.
- As in Q1, keywords are recognised by value ("int", "return"
  also match the identifier pattern), the way real lexers do it.

Usage:
    python q5_token_categorization_file_storage.py
    pip install lark
"""

from collections import Counter

from lark import Lark, Token

KEYWORDS = {"int", "float", "if", "else", "while", "return"}

grammar = r"""
start: word+

word: IDENTIFIER | NUMBER | OPERATOR | KEYWORD
IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+(\.\d+)?/
OPERATOR: "+" | "-" | "*" | "/" | "="
KEYWORD: "int" | "float" | "if" | "else" | "while" | "return"

%ignore WS
WS: /[ \t\n]+/
"""

parser = Lark(grammar, parser="lalr", propagate_positions=True)

data = "int x = 10 x = x + 5 return x"
tree = parser.parse(data)

ids, nums, ops, keys = [], [], [], []

for token in tree.scan_values(lambda v: isinstance(v, Token)):
    if token.value in KEYWORDS:
        keys.append(token.value)
    elif token.type == "IDENTIFIER":
        ids.append(token.value)
    elif token.type == "NUMBER":
        nums.append(token.value)
    elif token.type == "OPERATOR":
        ops.append(token.value)

open("identifiers.txt", "w").write("\n".join(ids))
open("numbers.txt", "w").write("\n".join(nums))
open("operators.txt", "w").write("\n".join(ops))
open("keywords.txt", "w").write("\n".join(keys))

print("Identifier Frequency:", Counter(ids))
print("Number Frequency:", Counter(nums))
print("Operator Frequency:", Counter(ops))
print("Keyword Frequency:", Counter(keys))
