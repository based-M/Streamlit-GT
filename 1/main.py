import matplotlib.pyplot as plt
import networkx as nx

def main():
    N = nx.empty_graph(5)

    K_5 = nx.complete_graph(5)

    P = nx.path_graph(5)

    C = nx.cycle_graph(5)

    K_25 = nx.complete_bipartite_graph(2, 3)

    W5 = nx.wheel_graph(5)

    fig, axe = plt.subplots(2, 3, figsize=(15,10))

    nx.draw(N, nx.spring_layout(N, seed=0), ax=axe[0, 0], with_labels=True, node_size=700, node_color="lightgray")
    axe[0,0].set_title("Null Graph")

    nx.draw(K_5, nx.spring_layout(K_5, seed=1), ax=axe[0, 1], with_labels=True, node_size=700, node_color="skyblue")
    axe[0,1].set_title("K5")

    nx.draw(P, nx.spring_layout(P, seed=2), ax=axe[0, 2], with_labels=True, node_size=700, node_color="black")
    axe[0,2].set_title("P5")

    nx.draw(C, nx.spring_layout(C, seed=3), ax=axe[1, 0], with_labels=True, node_size=700, node_color="brown")
    axe[1,0].set_title("C5")

    L = [(0,1),(1,1),(2,0),(1,0),(0,0)]
    nx.draw(K_25, L, ax=axe[1, 1], with_labels=True, node_size=700, node_color="pink")
    axe[1,1].set_title("K(2,3)")

    nx.draw(W5, nx.spring_layout(W5, seed=4), ax=axe[1, 2], with_labels=True, node_size=700, node_color="red")
    axe[1,2].set_title("W5")

    plt.show()
