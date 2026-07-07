import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random


def draw_graph(G, pos, ax, title):
    nx.draw(
        G, pos, ax=ax,
        with_labels=True,
        node_color="skyblue",
        node_size=700,
        edge_color="black"
    )
    ax.set_title(title)

def run(g,pos):
    adjacency_matrix = np.array(g)

    G = nx.from_numpy_array(adjacency_matrix)
    nodes = random.sample(list(G.nodes), random.randint(2, G.number_of_nodes()))
    edges = random.sample(list(G.edges), random.randint(1, G.number_of_edges()))

    spanning_tree = nx.minimum_spanning_tree(G)
    node_subgraph = G.subgraph(nodes)
    edge_subgraph = G.edge_subgraph(edges)

    fig, axes = plt.subplots(2, 2, figsize=(8, 8))

    draw_graph(G, pos, axes[0, 0], "Original Graph")
    draw_graph(spanning_tree, pos, axes[0, 1], "Spanning Tree")
    draw_graph(node_subgraph, pos, axes[1, 0], "Node-Induced Subgraph")
    draw_graph(edge_subgraph, pos, axes[1, 1], "Edge-Induced Subgraph")

    plt.tight_layout()
    plt.show()
    
def main():
    adjacency_matrix = np.array([
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    ])

    G = nx.from_numpy_array(adjacency_matrix)

    pos = {
        0: (0, 4), 1: (6, 4), 2: (2, 3), 3: (4, 3),
        4: (1, 2), 5: (3, 2), 6: (5, 2), 7: (3, 1),
        8: (2, 0), 9: (5, 0), 10: (0, -1), 11: (6, -1)
    }

    nodes = random.sample(list(G.nodes), random.randint(2, G.number_of_nodes()))
    edges = random.sample(list(G.edges), random.randint(1, G.number_of_edges()))

    spanning_tree = nx.minimum_spanning_tree(G)
    node_subgraph = G.subgraph(nodes)
    edge_subgraph = G.edge_subgraph(edges)

    fig, axes = plt.subplots(2, 2, figsize=(8, 8))

    draw_graph(G, pos, axes[0, 0], "Original Graph")
    draw_graph(spanning_tree, pos, axes[0, 1], "Spanning Tree")
    draw_graph(node_subgraph, pos, axes[1, 0], "Node-Induced Subgraph")
    draw_graph(edge_subgraph, pos, axes[1, 1], "Edge-Induced Subgraph")

    plt.tight_layout()
    plt.show()


#main()
 
