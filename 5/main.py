import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def main():
    A = np.array([[0,1,1,0],[1,0,1,1],[1,1,0,0],[0,1,0,0]])
    G = nx.from_numpy_array(A)

    L = nx.line_graph(G)

    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700)
    plt.title("Original Graph G")

    plt.subplot(1,2,2)
    pos2 = nx.spring_layout(L)
    nx.draw(L, pos2, with_labels=True, node_size=700)
    plt.title("Line Graph L(G)")

    plt.show()    
    
def run(g, pos):
    A = np.array(g)

    G = nx.from_numpy_array(A)

    L = nx.line_graph(G)

    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    #pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700)
    plt.title("Original Graph G")

    plt.subplot(1,2,2)
    pos2 = nx.spring_layout(L)
    nx.draw(L, pos2, with_labels=True, node_size=700)
    plt.title("Line Graph L(G)")

    plt.show()    
