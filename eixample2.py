import matplotlib.pyplot as plt
import networkx as nx
from networkx.utils.random_sequence import weighted_choice

G = nx.DiGraph()
G.add_weighted_edges_from([(1, 2, 1.0), (2, 3, 1.0), (3, 4, 1.0), (4, 8, 1.0), (8, 7, 1.0), (7, 6, 1.0), (6, 5, 1.0), (1, 5, 7.1)])


pos = { 1:(0, 0), 2:(1, 0), 3:(2, 0), 4:(3, 0), 5:(0, 1), 6:(1, 1), 7:(2, 1), 8:(3, 1)}
labels = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_nodes(G, pos, node_size=500)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color="black")
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print(nx.shortest_path(G, 1, 5, weight='weight'))
plt.show()