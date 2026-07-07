import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def hamiltonian_circuit(G):
    n = len(G.nodes())
    DG = nx.DiGraph(G)
    for cycle in nx.simple_cycles(DG):
        if len(cycle) == n:
            return cycle + [cycle[0]]
    return None    
    
    
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

    G1 = nx.from_numpy_array(adj_mat1)
    G2 = nx.from_numpy_array(adj_mat2)



    fig, axes = plt.subplots(2,2,figsize=(10,10))
    graphs = [
        (G1,pos1,"G1"),
        (G2,pos2,"G2")
    ]

    for i, (G,pos,name) in enumerate(graphs):
        circuit = hamiltonian_circuit(G)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            node_size=800,
            ax=axes[i][0]
        )
        axes[i][0].set_title(f"{name} Graph")
        if circuit:
            edges = [
                (circuit[j], circuit[j+1])
                for j in range(len(circuit)-1)
            ]
            nx.draw(
                G,
                pos,
                with_labels=True,
                node_color="lightgreen",
                node_size=800,
                ax=axes[i][1]
            )
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=edges,
                edge_color="red",
                width=3,
                ax=axes[i][1]
            )
            axes[i][1].set_title(
                f"{name} Hamiltonian Circuit"
            )
            axes[i][1].text(
                0.5,
                -0.05,
                f"Circuit: {circuit}",
                transform=axes[i][1].transAxes,
                ha="center",
                fontsize=10
            )
        else:
            axes[i][1].axis("off")

            axes[i][1].text(
                0.5,
                0.5,
                "No Hamiltonian Circuit is present",
                ha="center",
                va="center",
                fontsize=12
            )
    plt.tight_layout()
    plt.show()
    
def run(g, pos):
    pos1 = pos
    adj_mat1 = np.array(g)
    G1 = nx.from_numpy_array(adj_mat1)
    fig, axes = plt.subplots(1,2,figsize=(10,10))
    graphs = [
        (G1,pos1,"G1")
    ]

    for i, (G,pos,name) in enumerate(graphs):
        circuit = hamiltonian_circuit(G)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            node_size=800,
            ax=axes[0]
        )
        axes[0].set_title(f"{name} Graph")
        if circuit:
            edges = [
                (circuit[j], circuit[j+1])
                for j in range(len(circuit)-1)
            ]
            nx.draw(
                G,
                pos,
                with_labels=True,
                node_color="lightgreen",
                node_size=800,
                ax=axes[1]
            )
            nx.draw_networkx_edges(
                G,
                pos,
                edgelist=edges,
                edge_color="red",
                width=3,
                ax=axes[1]
            )
            axes[1].set_title(
                f"{name} Hamiltonian Circuit"
            )
            axes[1].text(
                0.5,
                -0.05,
                f"Circuit: {circuit}",
                transform=axes[1].transAxes,
                ha="center",
                fontsize=10
            )
        else:
            axes[1].axis("off")

            axes[1].text(
                0.5,
                0.5,
                "No Hamiltonian Circuit is present",
                ha="center",
                va="center",
                fontsize=12
            )
    plt.tight_layout()
    plt.show()
