"""Experiment 6, Q3: DFA Visualization using Graphviz.

Draws the DFA for the regex a*b (q0 = start, q1 = final shown as a
double circle) and renders it to dfa_a_star_b.pdf.

Note: rendering needs the Graphviz 'dot' program installed on the
system. If it is missing, the script still writes the DOT source to
dfa_a_star_b.gv so the diagram can be rendered later with:
    dot -Tpng dfa_a_star_b.gv -o dfa.png

Usage:
    python q3_dfa_visualization_graphviz.py
    pip install graphviz
"""

from graphviz import Digraph

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

dot = Digraph()

# States
dot.node("q0", "q0 (Start)")
dot.node("q1", "q1 (Final)", shape="doublecircle")

# Transitions
dot.edge("q0", "q0", label="a")
dot.edge("q0", "q1", label="b")

try:
    dot.render(_path("dfa_a_star_b"), view=False, cleanup=True)
    print(f"DFA diagram rendered to {_path('dfa_a_star_b.pdf')}")
except Exception as e:
    # 'dot' binary missing: keep the DOT source for later rendering.
    dot.save(_path("dfa_a_star_b.gv"))
    print("Could not render (Graphviz 'dot' not installed):", e)
    print(f"DOT source saved to {_path('dfa_a_star_b.gv')}")
