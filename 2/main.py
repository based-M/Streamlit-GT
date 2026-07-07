import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import itertools as it


def run(graphs, positions):
    fig, axes = plt.subplots(1, len(graphs), figsize=(12, 8))
    Gr = []
    for g in graphs:
        Gr.append(nx.from_numpy_array(g))
    #graphs = [G1, G2, G3]

    for i, (ax, G) in enumerate(zip(axes.flatten(), Gr)):
        nx.draw(G, pos[i], ax=ax, with_labels=True, node_size=500)

    plt.show()

    for i, j in it.combinations(range(len(Gr)), 2):
        print(f"\nChecking Graph {i+1} & Graph {j+1}")
        GM = nx.isomorphism.GraphMatcher(Gr[i], Gr[j])
        print("Isomorphic:", GM.is_isomorphic())
        if GM.is_isomorphic():
            print("Mapping:", GM.mapping)


def main():
    G1 = nx.from_numpy_array(np.array([
        [0,1,1,0,1,0,1,1],
        [1,0,1,1,0,1,0,1],
        [1,1,0,1,1,0,1,0],
        [0,1,1,0,1,1,0,1],
        [1,0,1,1,0,1,1,0],
        [0,1,0,1,1,0,1,1],
        [1,0,1,0,1,1,0,1],
        [1,1,0,1,0,1,1,0]
    ]))

    G2 = nx.from_numpy_array(np.array([
        [0,1,0,1,1,1,0,1],
        [1,0,1,0,1,1,1,0],
        [0,1,0,1,0,1,1,1],
        [1,0,1,0,1,0,1,1],
        [1,1,0,1,0,1,0,1],
        [1,1,1,0,1,0,1,0],
        [0,1,1,1,0,1,0,1],
        [1,0,1,1,1,0,1,0]
    ]))

    G3 = nx.from_numpy_array(np.array([
        [0,1,1,0,1,1,0,1],
        [1,0,1,1,0,1,0,1],
        [1,1,0,1,0,0,1,1],
        [0,1,1,0,1,1,1,0],
        [1,0,0,1,0,1,1,1],
        [1,1,0,1,1,0,1,0],
        [0,0,1,1,1,1,0,1],
        [1,1,1,0,1,0,1,0]
    ]))

    fig, axes = plt.subplots(1, 3, figsize=(12, 8))

    pos1 = {
        0: (1,3), 1: (2,3), 2: (3,2), 3: (3,1),
        4: (2,0), 5: (1,0), 6: (0,1), 7: (0,2)
    }

    pos2 = {
        0: (2,4), 1: (4,3), 2: (4,1), 3: (2,0),
        4: (0,1), 5: (0,3), 6: (1,2), 7: (3,2)
    }

    graphs = [G1, G2, G3]

    for i, (ax, G) in enumerate(zip(axes.flatten(), graphs)):
        pos = pos1 if i < 2 else pos2
        nx.draw(G, pos, ax=ax, with_labels=True, node_size=500)

    plt.show()

    for i, j in it.combinations(range(len(graphs)), 2):
        print(f"\nChecking Graph {i+1} & Graph {j+1}")
        GM = nx.isomorphism.GraphMatcher(graphs[i], graphs[j])
        print("Isomorphic:", GM.is_isomorphic())
        if GM.is_isomorphic():
            print("Mapping:", GM.mapping)


#main()
