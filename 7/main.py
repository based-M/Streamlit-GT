import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

def main():
    adj_matrix = np.array([
        [0, 32, 20, 15, math.inf, math.inf, math.inf, math.inf],
        [32, 0, math.inf, 30, math.inf, math.inf, 18, math.inf],
        [20, math.inf, 0, 10, math.inf, 42, math.inf, math.inf],
        [15, 30, 10, 0, 47, 53, math.inf, math.inf],
        [math.inf, math.inf, math.inf, 47, 0, 45, 24, 20],
        [math.inf, math.inf, 42, 53, 45, 0, math.inf, math.inf],
        [math.inf, 18, math.inf, math.inf, 24, math.inf, 0, 40],
        [math.inf, math.inf, math.inf, math.inf, 20, math.inf, 40, 0]
    ])

    G = nx.Graph()
    n = len(adj_matrix)

    for i in range(n):
        for j in range(i + 1, n):
            weight = adj_matrix[i][j]

            if weight != math.inf and weight != 0:
                G.add_edge(i, j, weight=weight)

    pos = {
        0: (0, 1),
        1: (1, 2),
        2: (1, 0),
        3: (2, 1),
        4: (4, 1),
        5: (3, 0),
        6: (4, 2),
        7: (5, 1)
    }

    source = 0

    distances, paths = nx.single_source_dijkstra(G, source)

    SPT = nx.Graph()

    for node in paths:
        path = paths[node]

        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]

            weight = G[u][v]['weight']

            SPT.add_edge(u, v, weight=weight)
    distances = {key: float(value) for key, value in distances.items()}
    print(distances)

    fig, axs = plt.subplots(1, 2, figsize=(16, 8))

    nx.draw(G, pos, ax=axs[0], with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, ax=axs[0], edge_labels=edge_labels)
    axs[0].set_title("Weighted Graph")

    nx.draw(SPT, pos, ax=axs[1], with_labels=True)
    spt_labels = nx.get_edge_attributes(SPT, 'weight')
    nx.draw_networkx_edge_labels(SPT, pos, ax=axs[1], edge_labels=spt_labels)
    axs[1].set_title("Shortest Path Tree")

    plt.tight_layout()
    plt.show()
    
def run(g, pos):
    adj_matrix = np.array(g)

    G = nx.Graph()
    n = len(adj_matrix)

    for i in range(n):
        for j in range(i + 1, n):
            weight = adj_matrix[i][j]

            if weight != math.inf and weight != 0:
                G.add_edge(i, j, weight=weight)
    source = 0
    distances, paths = nx.single_source_dijkstra(G, source)
    SPT = nx.Graph()
    for node in paths:
        path = paths[node]
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            weight = G[u][v]['weight']
            SPT.add_edge(u, v, weight=weight)
    distances = {key: float(value) for key, value in distances.items()}
    print(distances)
    fig, axs = plt.subplots(1, 2, figsize=(16, 8))
    nx.draw(G, pos, ax=axs[0], with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, ax=axs[0], edge_labels=edge_labels)
    axs[0].set_title("Weighted Graph")
    nx.draw(SPT, pos, ax=axs[1], with_labels=True)
    spt_labels = nx.get_edge_attributes(SPT, 'weight')
    nx.draw_networkx_edge_labels(SPT, pos, ax=axs[1], edge_labels=spt_labels)
    axs[1].set_title("Shortest Path Tree")
    plt.tight_layout()
    plt.show()
