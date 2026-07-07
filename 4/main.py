import networkx as nx
import matplotlib.pyplot as plt


def build_graph_from_degree_sequence(degree_sequence):
    if not nx.is_graphical(degree_sequence):
        print("This degree sequence is NOT graphical (no valid graph exists).")
        return None

    G = nx.havel_hakimi_graph(degree_sequence)
    return G


def get_properties(G):
    print("\n--- Graph Properties ---")
    print(f"Nodes: {G.number_of_nodes()}")
    print(f"Edges: {G.number_of_edges()}")
    print(f"Degree sequence: {sorted([d for _, d in G.degree()], reverse=True)}")
    print(f"Is connected: {nx.is_connected(G)}")


def visualize(G, degree_sequence):
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(7, 5))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=700,
        edge_color="black"
    )

    plt.title(f"Graph for degree sequence: {sorted(degree_sequence, reverse=True)}")
    plt.show()
    
def run(degree_sequence):
    G = build_graph_from_degree_sequence(degree_sequence)
    if G:
        get_properties(G)
        visualize(G, degree_sequence)

def main():
    degree_sequence = [5, 4, 4, 3, 2, 2, 1, 1]

    G = build_graph_from_degree_sequence(degree_sequence)

    if G:
        get_properties(G)
        visualize(G, degree_sequence)
