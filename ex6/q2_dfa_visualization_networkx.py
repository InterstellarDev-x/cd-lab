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
plt.savefig("dfa_a_star_b.png")
print("DFA diagram saved to dfa_a_star_b.png")
