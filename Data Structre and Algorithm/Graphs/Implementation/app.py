import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('A', 'None'), ('D', 'B'), ('E', 'None'), ('E', 'F'),
     ('B', 'H'), ('B', 'G'), ('B', 'F'), ('None', 'G')])

val_map = {'A': 1.0,
           'D': 0.5714285714285714,
           'B': 0.4,
           'None':0.5,
           'E':0.8,
           'F':0.2,
           'H': 0.1,
           'G':0.05}

values = [val_map.get(node, 0.25) for node in G.nodes()]

# Specify the edges you want here
# red_edges = [('A', 'C'), ('E', 'C')]
# edge_colours = ['black' if not edge in red_edges else 'red'
#                 for edge in G.edges()]
# black_edges = [edge for edge in G.edges() if edge not in red_edges]

# Need to create a layout when doing
# separate calls to draw nodes and edges
pos = nx.circular_layout(G)
print(val_map.get('A',0.25))
nx.draw(G, pos, cmap=plt.get_cmap('jet'),
                       node_color = values, node_size = 800,with_labels=True)
plt.show()