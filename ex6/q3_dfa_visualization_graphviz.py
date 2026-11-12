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

dot = Digraph()

# States
dot.node("q0", "q0 (Start)")
dot.node("q1", "q1 (Final)", shape="doublecircle")

# Transitions
dot.edge("q0", "q0", label="a")
dot.edge("q0", "q1", label="b")

try:
    dot.render("dfa_a_star_b", view=False, cleanup=True)
    print("DFA diagram rendered to dfa_a_star_b.pdf")
except Exception as e:
    # 'dot' binary missing: keep the DOT source for later rendering.
    dot.save("dfa_a_star_b.gv")
    print("Could not render (Graphviz 'dot' not installed):", e)
    print("DOT source saved to dfa_a_star_b.gv")
