import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def main():
    adj_mat1 = np.array([
        [0,1,0,0,1,1,1,0,0,0],
        [1,0,1,1,0,0,0,1,0,0],
        [0,1,0,1,0,0,1,1,1,1],
        [0,1,1,0,1,0,0,0,0,1],
        [1,0,0,1,0,1,1,0,0,0],
        [1,0,0,0,1,0,1,0,1,0],
        [1,0,1,0,1,1,0,0,0,0],
        [0,1,1,0,0,0,0,0,0,0],
        [0,0,1,0,0,1,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0]
    ])

    adj_mat2 = np.array([
        [0,1,0,0,0,1,0,0,1],
        [1,0,1,0,1,0,0,0,0],
        [0,1,0,1,0,0,0,0,0],
        [0,0,1,0,1,0,0,0,1],
        [0,1,0,1,0,1,0,1,0],
        [1,0,0,0,1,0,1,0,0],
        [0,0,0,0,0,1,0,1,0],
        [0,0,0,0,1,0,1,0,1],
        [1,0,0,1,0,0,0,1,0]
    ])

    G1 = nx.from_numpy_array(adj_mat1)
    G2 = nx.from_numpy_array(adj_mat2)

    pos1 = {
        0:(1,2),
        1:(3,2),
        2:(4,1),
        3:(3,0),
        4:(1,0),
        5:(0,1),
        6:(2,1),
        7:(5,2),
        8:(5,1),
        9:(5,0)
    }

    pos2 = {
        0:(0,2),
        1:(1,2),
        2:(2,2),
        3:(2,1),
        4:(1,1),
        5:(0,1),
        6:(0,0),
        7:(1,0),
        8:(2,0)
    }

    closed_walk1 = nx.find_cycle(G1)
    trail1 = list(nx.eulerian_path(G1)) if nx.has_eulerian_path(G1) else []
    path1 = nx.shortest_path(G1, 0, 5) if nx.has_path(G1, 0, 5) else []

    closed_walk2 = nx.find_cycle(G2)
    trail2 = list(nx.eulerian_path(G2)) if nx.has_eulerian_path(G2) else []
    path2 = nx.shortest_path(G2, 0, 5) if nx.has_path(G2, 0, 5) else []

    fig, axs = plt.subplots(2, 3, figsize=(18, 10))

    nx.draw(G1, pos1, ax=axs[0,0], with_labels=True)
    axs[0,0].set_title("G1")

    nx.draw(G1, pos1, ax=axs[0,1], with_labels=True)
    nx.draw_networkx_edges(
        G1,
        pos1,
        ax=axs[0,1],
        edgelist=closed_walk1,
        width=3
    )
    axs[0,1].set_title("G1 Closed Walk")

    nx.draw(G1, pos1, ax=axs[0,2], with_labels=True)

    if len(trail1) > 0:
        nx.draw_networkx_edges(
            G1,
            pos1,
            ax=axs[0,2],
            edgelist=trail1,
            width=3
        )

    if len(path1) > 1:
        nx.draw_networkx_edges(
            G1,
            pos1,
            ax=axs[0,2],
            edgelist=list(zip(path1,path1[1:])),
            width=3
        )

    axs[0,2].set_title("G1 Trail and Path")

    nx.draw(G2, pos2, ax=axs[1,0], with_labels=True)
    axs[1,0].set_title("G2")

    nx.draw(G2, pos2, ax=axs[1,1], with_labels=True)
    nx.draw_networkx_edges(
        G2,
        pos2,
        ax=axs[1,1],
        edgelist=closed_walk2,
        width=3
    )
    axs[1,1].set_title("G2 Closed Walk")

    nx.draw(G2, pos2, ax=axs[1,2], with_labels=True)

    if len(trail2) > 0:
        nx.draw_networkx_edges(
            G2,
            pos2,
            ax=axs[1,2],
            edgelist=trail2,
            width=3
        )

    if len(path2) > 1:
        nx.draw_networkx_edges(
            G2,
            pos2,
            ax=axs[1,2],
            edgelist=list(zip(path2,path2[1:])),
            width=3
        )

    axs[1,2].set_title("G2 Trail and Path")

    plt.tight_layout()
    plt.show()
    
def run(g, pos):
    pos1 = pos
    adj_mat1 = np.array(g)
    G1 = nx.from_numpy_array(adj_mat1)
    closed_walk1 = nx.find_cycle(G1)
    trail1 = list(nx.eulerian_path(G1)) if nx.has_eulerian_path(G1) else []
    path1 = nx.shortest_path(G1, 0, 5) if nx.has_path(G1, 0, 5) else []
    
    fig, axs = plt.subplots(1, 3, figsize=(18, 10))

    nx.draw(G1, pos1, ax=axs[0,0], with_labels=True)
    axs[0,0].set_title("G1")

    nx.draw(G1, pos1, ax=axs[0,1], with_labels=True)
    nx.draw_networkx_edges(
        G1,
        pos1,
        ax=axs[0,1],
        edgelist=closed_walk1,
        width=3
    )
    axs[0,1].set_title("G1 Closed Walk")

    nx.draw(G1, pos1, ax=axs[0,2], with_labels=True)

    if len(trail1) > 0:
        nx.draw_networkx_edges(
            G1,
            pos1,
            ax=axs[0,2],
            edgelist=trail1,
            width=3
        )

    if len(path1) > 1:
        nx.draw_networkx_edges(
            G1,
            pos1,
            ax=axs[0,2],
            edgelist=list(zip(path1,path1[1:])),
            width=3
        )

    axs[0,2].set_title("G1 Trail and Path")
    plt.tight_layout()
    plt.show()
