import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def fleury(G, name):

    if not (
        nx.is_eulerian(G) or
        nx.has_eulerian_path(G)
    ):
        print(f"No Euler Trail/Circuit exists for {name}")
        return None

    print(f"\nFor Graph: {name}")

    if nx.is_eulerian(G):
        print("Graph is Eulerian (Circuit exists)")
    else:
        print("Graph has Eulerian Path")

    trail_edges = list(nx.eulerian_path(G))

    step = 1

    for u, v in trail_edges:
        print(f"Step {step}: Traversed edge ({u}, {v})")
        step += 1

    trail = [trail_edges[0][0]]

    for u, v in trail_edges:
        trail.append(v)

    if trail[0] == trail[-1]:
        print("\nEuler Circuit:")
    else:
        print("\nEuler Trail:")

    print(trail)

    return trail


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

    fig, axes = plt.subplots(2, 2, figsize=(10, 10))


    for i, (G, pos, name) in enumerate([
        (G1, pos1, "Graph 1"),
        (G2, pos2, "Graph 2")
    ]):

        trail = fleury(G, name)

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            node_size=800,
            ax=axes[i][0]
        )

        axes[i][0].set_title(f"{name} Graph")

        if trail:

            edges = [
                (trail[j], trail[j+1])
                for j in range(len(trail)-1)
            ]

            nx.draw_networkx_nodes(
                G,
                pos,
                node_color="lightgreen",
                node_size=800,
                ax=axes[i][1]
            )

            nx.draw_networkx_labels(
                G,
                pos,
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

            if trail[0] == trail[-1]:
                axes[i][1].set_title(
                    f"{name} Euler Circuit"
                )
            else:
                axes[i][1].set_title(
                    f"{name} Euler Trail"
                )

        else:

            axes[i][1].axis("off")

            axes[i][1].text(
                0.5,
                0.5,
                "No Euler Trail/Circuit exists",
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
    fig, axes = plt.subplots(1, 2, figsize=(10, 10))


    for i, (G, pos, name) in enumerate([(G1, pos1, "Graph 1")]):
        trail = fleury(G, name)
        nx.draw(
            G,
            pos,
            with_labels=True,
            node_color="lightblue",
            node_size=800,
            ax=axes[0]
        )

        axes[0].set_title(f"{name} Graph")

        if trail:

            edges = [
                (trail[j], trail[j+1])
                for j in range(len(trail)-1)
            ]

            nx.draw_networkx_nodes(
                G,
                pos,
                node_color="lightgreen",
                node_size=800,
                ax=axes[1]
            )

            nx.draw_networkx_labels(
                G,
                pos,
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

            if trail[0] == trail[-1]:
                axes[1].set_title(
                    f"{name} Euler Circuit"
                )
            else:
                axes[1].set_title(
                    f"{name} Euler Trail"
                )

        else:

            axes[1].axis("off")

            axes[1].text(
                0.5,
                0.5,
                "No Euler Trail/Circuit exists",
                ha="center",
                va="center",
                fontsize=12
            )

    plt.tight_layout()
    plt.show()
