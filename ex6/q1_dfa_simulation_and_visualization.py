"""Experiment 6 - DFA creation and simulation from a regular expression.

From: Compiler Design Lab - Final Compact Edition (compiler_lab_programs.pdf)

Aim: To write a Python program to simulate a Deterministic Finite
Automaton (DFA) from a given regular expression and visualize the DFA
using NetworkX and Matplotlib.

The DFA here is for the regular expression a(b|c)* :
  states  q0 (start), q1 (final), qd (dead)
  q0 --a--> q1,  q0 --b,c--> qd
  q1 --a--> qd,  q1 --b,c--> q1
  qd loops to itself on a, b, c

Sample tests:
    abc -> String Accepted
    ba  -> String Rejected
    a   -> String Accepted

NOTE: this edition's DFA is a(b|c)*. The course manual's Experiment 6
uses a*b instead - that version lives in the companion repo
InterstellarDev-x/cd-lab (Ex 6). Both repos are kept, so both DFAs
stay available.

Install: pip install networkx matplotlib
"""

import networkx as nx
import matplotlib.pyplot as plt

states = ["q0", "q1", "qd"]
start_state = "q0"
final_state = "q1"

transitions = {
    ("q0", "a"): "q1",
    ("q0", "b"): "qd",
    ("q0", "c"): "qd",
    ("q1", "a"): "qd",
    ("q1", "b"): "q1",
    ("q1", "c"): "q1",
    ("qd", "a"): "qd",
    ("qd", "b"): "qd",
    ("qd", "c"): "qd",
}

s = input("Enter a string: ")

current_state = start_state

for ch in s:
    if (current_state, ch) in transitions:
        current_state = transitions[(current_state, ch)]
    else:
        current_state = "qd"
        break

if current_state == final_state:
    print("String Accepted")
else:
    print("String Rejected")

G = nx.DiGraph()

G.add_nodes_from(states)
edges = [
    ("q0", "q1", "a"),
    ("q0", "qd", "b,c"),
    ("q1", "qd", "a"),
    ("q1", "q1", "b,c"),
    ("qd", "qd", "a,b,c"),
]
for u, v, label in edges:
    G.add_edge(u, v, label=label)

pos = {"q0": (0, 1), "q1": (2, 1), "qd": (1, -1)}
nx.draw_networkx_nodes(G, pos, nodelist=["q0", "qd"], node_color="lightblue", node_size=1800)
nx.draw_networkx_nodes(G, pos, nodelist=["q1"], node_color="lightgreen", node_size=1800, node_shape="o", linewidths=3)
nx.draw_networkx_labels(G, pos, font_size=12)
nx.draw_networkx_edges(G, pos, arrows=True, connectionstyle="arc3,rad=0.15", arrowsize=20)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=nx.get_edge_attributes(G, "label"), font_size=10
)
plt.title("DFA for Regular Expression: a(b|c)*")
plt.axis("off")
plt.show()
