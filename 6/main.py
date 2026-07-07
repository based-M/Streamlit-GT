import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

#need to account for  -1
def main():
    adj_mat = np.array([
    [0, 10, 2, 4, -1, -1, -1, -1],
    [10, 0, 3, -1, 0, -1, -1, -1],
    [2, 3, 0, 2, -1, 8, -1, -1],
    [4, -1, 2, 0, -1, 2, 7, -1],
    [-1, 0, -1, -1, 0, 1, -1, 8],
    [-1, -1, 8, 2, 1, 0, 6, 9],
    [-1, -1, -1, 7, -1, 6, 0, 12],
    [-1, -1, -1, -1, 8, 9, 12, 0]
])

    print(adj_mat)
    G = nx.Graph()
    n = adj_mat.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            weight = adj_mat[i][j]
            if weight != -1 and weight != 0:
                G.add_edge(i, j, weight=weight)

    pos = {
        0: (0, 1),
        1: (1, 2),
        2: (1, 1),
        3: (1, 0),
        4: (2, 2),
        5: (2, 1),
        6: (2, 0),
        7: (3, 1)
    }

    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    nx.draw(G, pos, ax=axs[0], with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G,
        pos,
        ax=axs[0],
        edge_labels=edge_labels
    )

    axs[0].set_title("Original Graph")

    nx.draw(mst, pos, ax=axs[1], with_labels=True)

    mst_labels = nx.get_edge_attributes(mst, 'weight')

    nx.draw_networkx_edge_labels(
        mst,
        pos,
        ax=axs[1],
        edge_labels=mst_labels
    )

    axs[1].set_title("Minimum Spanning Tree")

    print("\nMST Edges:\n")

    total_weight = 0

    for u, v, w in mst.edges(data=True):

        print(f"{u} -- {v} = {w['weight']}")

        total_weight += w['weight']

    print("\nTotal Weight =", total_weight)

    plt.tight_layout()
    plt.show()

def run(g,pos):
    adj_mat = np.array(g)

    print(adj_mat)
    G = nx.Graph()
    n = adj_mat.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            weight = adj_mat[i][j]
            if weight != -1 and weight != 0:
                G.add_edge(i, j, weight=weight)
    mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    nx.draw(G, pos, ax=axs[0], with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(
        G,
        pos,
        ax=axs[0],
        edge_labels=edge_labels
    )

    axs[0].set_title("Original Graph")

    nx.draw(mst, pos, ax=axs[1], with_labels=True)

    mst_labels = nx.get_edge_attributes(mst, 'weight')

    nx.draw_networkx_edge_labels(
        mst,
        pos,
        ax=axs[1],
        edge_labels=mst_labels
    )

    axs[1].set_title("Minimum Spanning Tree")

    print("\nMST Edges:\n")

    total_weight = 0

    for u, v, w in mst.edges(data=True):

        print(f"{u} -- {v} = {w['weight']}")

        total_weight += w['weight']

    print("\nTotal Weight =", total_weight)

    plt.tight_layout()
    plt.show()

#main()
