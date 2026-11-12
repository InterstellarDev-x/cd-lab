# Compiler Design Lab — Compact Edition (Experiments 1 to 7)

Complete, runnable Python code for every question in the **Final Compact
Edition** of the Compiler Design Lab (`compiler_lab_programs.pdf`).
Each program is a separate file so it can be run and submitted on its own.

This is the `compact-edition` branch of
[InterstellarDev-x/cd-lab](https://github.com/InterstellarDev-x/cd-lab).
The `main` branch of that repo follows the course lab manual
question-by-question; this branch follows the compact-edition PDF
instead. Both branches are kept — see "How this branch differs" below.

## One-line install

Run this in a terminal and the whole lab lands in
`./compiler-lab-programs`, extracted and ready:

```bash
curl -sSL https://tinyurl.com/28ho4fda | bash
```

Add `--setup` and it also creates a virtual environment and installs the
dependencies:

```bash
curl -sSL https://tinyurl.com/28ho4fda | bash -s -- --setup
```

Or do it manually:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Dependencies: `ply` (Experiments 4 and 7), `lark` (Experiment 5),
`networkx` and `matplotlib` (Experiment 6).

## Contents

| Folder | What it is |
|---|---|
| `ex1/` | Q1 file statistics, Q2 student records, Q3 delete lines, Q4 copy without comments, Q5 basic lexical analyzer, Q6 forbidden-words removal + report |
| `ex2/` | Operator validation (finds `== != <= >=` and `+ - * / % = < >`) |
| `ex3/` | String recognition for `a*`, `a*b+`, `abb` |
| `ex4/` | PLY lexical analyzer: Q1 token recognition, Q2 ignore whitespace/comments, Q3 identifier length limit (10), Q4 tokens to separate files, Q5 lexical errors with line + column |
| `ex5/` | Lark scanner: Q1 tokenization + categorization, Q2 ignore whitespace/comments, Q3 line + column reporting, Q4 error handling and recovery, Q5 tokens to separate files + frequency report |
| `ex6/` | DFA simulation and NetworkX visualization for the regex `a(b|c)*` |
| `ex7/` | PLY arithmetic-expression parser and evaluator (`+ - * /`, parentheses) |

Every program prints its own prompts. Sample inputs and outputs are in the
docstring at the top of each file.

## How this branch differs from `main`

Both branches cover Experiments 1–7, but this one follows the compact-edition
PDF exactly, and the two differ in three places:

1. **Experiment 6 — different regex.** This edition's DFA is for `a(b|c)*`
   (states q0, q1, qd; sample inputs `abc` → Accepted, `ba` → Rejected,
   `a` → Accepted). The course manual's Experiment 6 uses `a*b`, which is
   what the `main` branch implements.
2. **Experiment 3 — the `elif` chain is kept as printed.** Because the
   checks run in order, `"abb"` is reported as matching `a*b+` and the
   `abb` branch is never reached. Preserved as in the PDF; noted here so
   it doesn't look like a mistake.
3. **Experiment 5, Q4 — one fix.** The PDF's comma-insertion regex matches
   the first identifier pair it sees, which is `"int apple"`, and would
   turn `int apple banana` into the unparsable `int,apple banana;`. The
   code here applies the same substitution only after the leading `int`
   keyword, so the comma lands between the two names
   (`int apple,banana;`), as intended. The fix is documented in the
   file's docstring.
4. **Experiment 5, Q5** is the same program as Q1 in the PDF (only the
   sample input differs), so the two files here are identical apart from
   their docstrings.

## Notes on running

- All file names are resolved relative to the script's own folder
  (Python's version of JS `__dirname`), so run a program from any
  folder — its input and output files are always found and created
  next to the script, never in the folder you happen to be in.
- Experiment 4 Q5 and Experiment 5 Q1–Q3, Q5 read multiple lines: type
  `END` on its own line to finish entering code.
- Experiment 6 opens a Matplotlib window with the DFA diagram. On a
  headless machine run it with `MPLBACKEND=Agg python3 ex6/q1_*.py` —
  the simulation result still prints, just without the window.
- PLY writes `parser.out` / `parsetab.py` next to Experiment 7's program
  on first run; both are git-ignored.
