"""Experiment 6, Q2: DFA Visualization using NetworkX.

Draws the DFA for the regex a*b as a directed graph and saves it
as dfa_a_star_b.png (the Agg backend is used so it works without
a display; the image opens with any image viewer).

    States: q0 (start), q1 (final)
    Transitions: q0 --a--> q0,  q0 --b--> q1

Usage:
    python q2_dfa_visualization_networkx.py
    pip install networkx matplotlib
"""

import matplotlib

matplotlib.use("Agg")  # headless: save to file instead of showing a window
import matplotlib.pyplot as plt
import networkx as nx

import os

# Files live next to this script, not next to your terminal's folder.
# __file__ is this script's own path, so BASE_DIR is its folder - the
# Python equivalent of JS __dirname. Every file below is resolved
# through _path(), so the program works no matter which folder you
# run it from.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def _path(name):
    """Resolve *name* against this script's folder."""
    return os.path.join(BASE_DIR, name)

# DFA structure
dfa = {
    "q0": {"a": "q0", "b": "q1"},
    "q1": {},
}

G = nx.DiGraph()

# Add edges
for state, transitions in dfa.items():
    for symbol, next_state in transitions.items():
        G.add_edge(state, next_state, label=symbol)

# Draw graph
pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000)
edge_labels = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("DFA for Regular Expression a*b")
plt.savefig(_path("dfa_a_star_b.png"))
print(f"DFA diagram saved to {_path('dfa_a_star_b.png')}")
