"""Experiment 6, Q1: DFA Simulation from Regular Expression a*b.

DFA for the regex a*b (zero or more 'a' followed by one 'b'):
    States: q0 (start), q1 (final)
    Transitions: q0 --a--> q0,  q0 --b--> q1

Sample output:
    b -> Accepted
    ab -> Accepted
    aaab -> Accepted
    a -> Rejected
    abb -> Rejected

Usage:
    python q1_dfa_simulation.py
"""

dfa = {
    "q0": {"a": "q0", "b": "q1"},
    "q1": {},
}

start_state = "q0"
final_states = ["q1"]


def simulate_dfa(string):
    """Walk the DFA over *string*; True if it ends in a final state."""
    state = start_state
    for char in string:
        if char in dfa[state]:
            state = dfa[state][char]
        else:
            return False  # no transition for this symbol
    return state in final_states


test_strings = ["b", "ab", "aaab", "a", "abb"]

for s in test_strings:
    print(s, "->", "Accepted" if simulate_dfa(s) else "Rejected")
