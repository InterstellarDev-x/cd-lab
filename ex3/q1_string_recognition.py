"""Experiment 3: String Recognition.

Checks whether an input string matches any of the regular expression
patterns:
    a*    - zero or more 'a'            (matches "", "a", "aa", "aaa", ...)
    a*b+  - zero or more 'a' then one or more 'b'
                                        (matches "b", "ab", "aab", "abb", ...)
    abb   - the exact sequence "abb"    (matches only "abb")

A string can match more than one pattern: "abb" matches both a*b+
and abb, so both are reported. Matching is done with re.fullmatch,
so the WHOLE string must match the pattern.

Usage:
    python q1_string_recognition.py          # interactive prompt
    python q1_string_recognition.py aaa      # check one string
    python q1_string_recognition.py aaa aabb abb b
"""

import re
import sys

PATTERNS = {
    "a*": r"a*",
    "a*b+": r"a*b+",
    "abb": r"abb",
}


def match_patterns(string):
    """Return the list of pattern names the whole *string* matches."""
    return [name for name, pat in PATTERNS.items()
            if re.fullmatch(pat, string)]


def check(string):
    """Print which pattern(s) *string* matched."""
    matched = match_patterns(string)
    if matched:
        print(f"String matched: {', '.join(matched)}")
    else:
        print("String matched: no pattern")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for s in sys.argv[1:]:
            print(f"Enter a string: {s}")
            check(s)
    else:
        while True:
            try:
                s = input("Enter a string: ")
            except (EOFError, KeyboardInterrupt):
                break
            if s == "":
                break
            check(s)
