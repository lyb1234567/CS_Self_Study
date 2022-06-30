import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import seaborn.apionly as sns
import matplotlib.animation

G = nx.Graph()
K3 = nx.Graph([(0, 0)])
G.add_nodes_from(K3)
G.add_nodes_from(K3)
val_map = {}
color = 0.02
color_div = 1 / 3
for i in G.nodes:
            s = i
            val_map[s] = color + color * color_div
            color = color + 1
values = [val_map.get(node) for node in G.nodes()]
pos = nx.circular_layout(G)
nx.draw(G, pos, cmap=plt.get_cmap('jet'),
node_color=values, node_size=900, with_labels=True, connectionstyle='arc3, rad = 0.1')
plt.show()