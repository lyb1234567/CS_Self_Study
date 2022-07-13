import matplotlib.pyplot as plt
import networkx as nx
from networkx.drawing.nx_pydot import graphviz_layout

T = nx.balanced_tree(2, 5)
print(T)