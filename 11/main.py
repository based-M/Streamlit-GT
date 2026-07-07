import sys
import networkx as nx
import matplotlib
#matplotlib.use("TkAgg")
import string
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors



def main():
    adj = np.array([
    #A  B  C  D  E  O  T
    [0, 1, 0, 1, 0, 1, 0],  # A
    [1, 0, 1, 1, 1, 1, 0],  # B
    [0, 1, 0, 0, 1, 1, 0],  # C
    [1, 1, 0, 0, 1, 0, 1],  # D
    [0, 1, 1, 1, 0, 0, 1],  # E
    [1, 1, 1, 0, 0, 0, 0],  # O
    [0, 0, 0, 1, 1, 0, 0],  # T
])

    labels = {i: c for i, c in enumerate("ABCDEOT")}
    pos = {labels[i]: (x, y) for i, (x, y) in enumerate([
    (1, 2),  # A
    (2, 1),  # B
    (1, 0),  # C
    (3, 2),  # D
    (3, 0),  # E
    (0, 1),  # O
    (4, 1),  # T
])}
    G = nx.from_numpy_array(adj)
    pos = {i: pos[labels[i]] for i in G.nodes()}

    

    colouring = nx.coloring.greedy_color(G, strategy="largest_first")
    num_colours = max(colouring.values()) + 1
    print(f"\nColours used: {num_colours}")
    for node, colour in sorted(colouring.items()):
        print(f"  {node} → colour {colour}")

 
    node_colours = [colouring[n] for n in G.nodes()]
    fig, ax = plt.subplots(figsize=(7, 5))
    nx.draw_networkx(
        G, pos,
        labels = labels,
        with_labels = True,
        node_color=node_colours,
        node_size=800,
        font_color="white",
        font_weight="bold",
        edge_color="#555555",
        ax=ax,
    )
    ax.set_title(f"Greedy graph colouring  ({num_colours} colours)", pad=14)
    ax.axis("off")
    plt.tight_layout()
    plt.show()

def run(g, pos):
    adj = np.array(g)

    labels = {
    i: string.ascii_lowercase[i]
    for i in range(len(g))}
    G = nx.from_numpy_array(adj)
    #pos = {i: pos[labels[i]] for i in G.nodes()}
    colouring = nx.coloring.greedy_color(G, strategy="largest_first")
    num_colours = max(colouring.values()) + 1
    print(f"\nColours used: {num_colours}")
    for node, colour in sorted(colouring.items()):
        print(f"  {node} → colour {colour}")

    node_colours = [colouring[n] for n in G.nodes()]
    fig, ax = plt.subplots(figsize=(7, 5))
    nx.draw_networkx(
        G, pos,
        labels = labels,
        with_labels = True,
        node_color=node_colours,
        node_size=800,
        font_color="white",
        font_weight="bold",
        edge_color="#555555",
        ax=ax,
    )
    ax.set_title(f"Greedy graph colouring  ({num_colours} colours)", pad=14)
    ax.axis("off")
    plt.tight_layout()
    plt.show()
    
#if __name__ == "__main__":
#    main()
