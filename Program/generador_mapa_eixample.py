import matplotlib.pyplot as plt
import networkx as nx
import csv

def main():
    
    G = nx.DiGraph()

    with open(r'C:\Users\gaesc\OneDrive\Escritorio\Jesuïtes Casp\TR\.csv Files\BCN_GrafVial_Trams_ETRS89_CSV.csv') as csv_file:
        edges = csv.reader(csv_file)

        next(edges)
        for edge in edges:
            initial_node = edge[6]
            end_node = edge[7]
            
            if edge[9] == 'Eixample':
                G.add_edge(initial_node, end_node)
                G[initial_node][end_node]['weight'] = edge[2]

    nodes_list = [item for t in G.edges() for item in t]

    with open(r'C:\Users\gaesc\OneDrive\Escritorio\Jesuïtes Casp\TR\.csv Files\BCN_GrafVial_Nodes_ETRS89_CSV.csv') as csv_file:
        nodes = csv.reader(csv_file)

        next(nodes)
        pos = {}
        for node in nodes:
            node_id = node[1]
            node_x = float(node[2])
            node_y = float(node[3])

            if node_id in nodes_list:
                pos[node_id] = (node_x, node_y)     

    nx.draw_networkx_nodes(G, pos, node_size=0.5)
    nx.draw_networkx_edges(G, pos, width=0.2, edgelist=G.edges(), arrowsize=2, edge_color="black")

    plt.show()

    

if __name__ == '__main__':
    print("Executant...")
    main()

