# Compiler Design Lab — Experiments 1 to 7

Complete, runnable Python code for every question in CD Lab
Experiments 1–7. Each program is a separate file so it can be run
and submitted on its own.

## One-line install

Run this in a terminal and the whole lab lands in `./cd-lab`,
extracted and ready:

```bash
curl -sSL https://tinyurl.com/25kl8jg2 | bash
```

Add `--setup` and it also creates the venv and installs the
requirements:

```bash
curl -sSL https://tinyurl.com/25kl8jg2 | bash -s -- --setup
```

(The short link points at `setup.sh` in the repo; the script
downloads the repo tarball from GitHub and extracts it into
`./cd-lab`. It takes an optional folder name and a `--setup`
flag — see the header of `setup.sh`.)

## Setup (manual)

Experiments 1–3 need only the standard library. Experiment 4 and 7
need `ply`, Experiment 5 needs `lark`, Experiment 6 needs
`networkx`, `matplotlib` and `graphviz`.

Note: Experiment 6 Q3 renders with the Graphviz `dot` program. If
`dot` is not installed the script saves the DOT source
(`dfa_a_star_b.gv`) instead of failing.

## Experiment 1 — Concept of Tokenizing & File Handling

| File | Question |
| --- | --- |
| `ex1/q1_file_stats.py` | Analyse a text file: lines, blank lines, words, characters (excluding whitespace) |
| `ex1/q2_student_records.py` | Store student records in a file, compute average / highest / lowest marks |
| `ex1/q3_delete_lines.py` | Delete specified line numbers from a text file |
| `ex1/q4_remove_comments.py` | Copy a file after removing `#` comment lines |
| `ex1/q5_lexical_analyzer.py` | Basic lexical analyzer: classify tokens as Keyword / Identifier / Literal / Operator / Delimiter |
| `ex1/q6_remove_forbidden_words.py` | Remove forbidden words from a file and generate a report |

```bash
cd ex1
python q1_file_stats.py            # uses input.txt
printf "3\n101 Aditya 90\n102 Rohan 75\n103 Priya 82\n" | python q2_student_records.py
python q3_delete_lines.py          # deletes lines 3 and 6 of lines.txt
python q4_remove_comments.py       # source.txt -> destination.txt
python q5_lexical_analyzer.py     # analyses program.py
python q6_remove_forbidden_words.py
```

## Experiment 2 — Lexical Analyzer for Identifying Operators

| File | Question |
| --- | --- |
| `ex2/q1_operator_lexical_analyzer.py` | Scan a source file, extract operators, classify as valid / invalid |

```bash
cd ex2
python q1_operator_lexical_analyzer.py   # uses source.txt
```

## Experiment 3 — String Recognition

| File | Question |
| --- | --- |
| `ex3/q1_string_recognition.py` | Check which of the patterns `a*`, `a*b+`, `abb` a string matches |

```bash
cd ex3
python q1_string_recognition.py aaa aabb abb b
python q1_string_recognition.py   # interactive: Enter a string:
```

## Experiment 4 — Lexical Analyzer using PLY

| File | Question |
| --- | --- |
| `ex4/q1_recognize_tokens.py` | Recognize identifiers, numbers and operators |
| `ex4/q2_ignore_whitespace_comments.py` | Ignore whitespace and `//` / `/* */` comments |
| `ex4/q3_identifier_length_limit.py` | Restrict identifier length to 10 characters |
| `ex4/q4_store_tokens_in_files.py` | Store tokens in separate files (`identifiers.txt`, `numbers.txt`, `operators.txt`, `keywords.txt`) |
| `ex4/q5_lexical_errors_line_column.py` | Handle lexical errors with line and column numbers |

```bash
cd ex4
python q1_recognize_tokens.py
python q2_ignore_whitespace_comments.py
python q3_identifier_length_limit.py
python q4_store_tokens_in_files.py
python q5_lexical_errors_line_column.py
```

## Experiment 5 — Scanner Implementation using Lark Parser

| File | Question |
| --- | --- |
| `ex5/q1_tokenization_ebnf.py` | Tokenization using EBNF grammar |
| `ex5/q2_ignore_whitespace_comments.py` | Ignoring whitespace and comments |
| `ex5/q3_line_column_reporting.py` | Line and column number reporting |
| `ex5/q4_error_handling_recovery.py` | Custom error handling and recovery (missing `;`) |
| `ex5/q5_token_categorization_file_storage.py` | Token categorization and file storage |

```bash
cd ex5
python q1_tokenization_ebnf.py
python q2_ignore_whitespace_comments.py
python q3_line_column_reporting.py
python q4_error_handling_recovery.py
python q5_token_categorization_file_storage.py
```

## Experiment 6 — DFA Creation and Simulation from Regular Expression

| File | Question |
| --- | --- |
| `ex6/q1_dfa_simulation.py` | DFA simulation for regex `a*b` |
| `ex6/q2_dfa_visualization_networkx.py` | DFA visualization using NetworkX (saves `dfa_a_star_b.png`) |
| `ex6/q3_dfa_visualization_graphviz.py` | DFA visualization using Graphviz (renders `dfa_a_star_b.pdf`) |

```bash
cd ex6
python q1_dfa_simulation.py
python q2_dfa_visualization_networkx.py
python q3_dfa_visualization_graphviz.py
```

## Experiment 7 — Parser Implementation with Python (PLY)

| File | Question |
| --- | --- |
| `ex7/q1_arithmetic_parser.py` | Arithmetic expression parser (PLY Lex + Yacc, LALR(1)) |

```bash
cd ex7
python q1_arithmetic_parser.py "3 + 4 * 2" "(5 + 3) * 2" "10 / 2 + 6"
python q1_arithmetic_parser.py   # interactive: Enter expression (or exit):
```

## Notes

- Every program was run and its output verified on Python 3.12.
- All file names are resolved relative to the script's own folder
  (Python's version of JS `__dirname`), so run a program from any
  folder — its input and output files are always found and created
  next to the script, never in the folder you happen to be in.
- PLY writes `parser.out` / `parsetab.py` next to the Experiment 7
  script on first run — that is normal PLY behaviour.
- Sample inputs used by the programs live next to them
  (`input.txt`, `source.txt`, `program.py`, ...). Q3 of Experiment 1
  edits `lines.txt` in place and Q6 rewrites `words.txt`, so keep a
  copy if you re-run them.

## Where the lab manual itself is wrong

The code here follows the manual, except where the manual's own
program cannot produce its own sample output. Those cases are
fixed in the code and noted in each file's docstring:

- **Ex 5 Q1** — the manual's grammar has no declaration form, so
  its own sample input (`int x = 10; ...`) fails to parse. A
  declaration alternative was added, and the parser runs Earley
  (LALR(1) cannot choose the declaration branch because `int`
  lexes as IDENTIFIER). Keywords are recognised by value, the way
  real lexers do it.
- **Ex 5 Q2** — the manual's grammar accepts only one statement,
  but its sample has two. The rule now accepts one or more.
- **Ex 5 Q4** — the manual says the error is at column 7; the
  offending token `y` is at column 8.
- **Ex 5 Q5** — the manual prints `{'x': 3}`, but `x` occurs 4
  times in its own sample input. The count here (4) is correct.
  The manual also defines `WORD` in capitals, which makes Lark
  treat it as a terminal and breaks categorization entirely;
  it is a lowercase rule here.
