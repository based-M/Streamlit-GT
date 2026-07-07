**Experiment No**: 5	**Date**: 12/03/2026

**Aim :** To implement conversion of a given graph into line graph where each vertex represents an edge of the original graph, and adjacency reflects shared endpoints

**Theory:** Let G be a simple graph characterized by its vertex set	and edge set	. The line graph of G, canonically denoted as	, is formally defined such that its vertex set exhibits a bijective

correspondence with the edge set of the primary graph, yielding	. Consequently, the order of the line graph is inherently equal to the size of the original graph, expressed mathematically as

. The topological framework of	is subsequently defined by its edge set

; two distinct vertices	are strictly adjacent if and only if their corresponding edges in G are incident to at least one common vertex. This systemic transformation alters the foundational object of analysis, permitting complex inter-edge dependencies to be evaluated as standard vertex-level interactions.

The localized topological structure within	is completely determinable through the degree parameters of the foundational graph G. Consider an arbitrary edge	defined by its distinct

endpoints	. Within the transformed space of	, the degree of the corresponding vertex e is algebraically quantified by the sum of the degrees of its original endpoints, diminished by exactly two to properly account for the internal incidence of e itself. This geometric relationship is formalized by the

equation	. As a direct structural consequence, an edge functioning as a densely connected hub in G—being incident to vertices of substantially high degree—will inherently map

to a vertex of proportionally high degree within the architecture of	.

A paramount theoretical result governing the reversibility of this geometric transformation is Whitney's Isomorphism Theorem. The theorem rigorously establishes that for any two connected graphs ![][image1] and ![][image2] possessing  an  order  of  ![][image3] ,  the  structural  equivalence  of  their  line  graphs,  denoted  as

, serves as a mathematically suﬃcient condition to strictly guarantee an isomorphism between the original primary graphs, ![][image4] . The mathematical necessity of the specific order constraint ![][image3] strictly precludes the singular isomorphic anomaly wherein the line graph of a complete graph on three vertices (the triangle) is structurally identical to the line graph of a complete bipartite claw

graph, precisely	. By formally isolating this well-documented exceptional case, graph theorists guarantee that the line graph operator predominantly acts as a structurally conservative transformation, uniquely preserving the primary network topology.

Furthermore, the theoretical utility of	extends profoundly into applied algorithmic domains, where intricate edge-dependent complexities are geometrically simplified into conventional vertex-dependent equivalents. The line graph allows properties that are computationally intensive to analyze at the edge

level within G to be resolved using simpler vertex-centric frameworks in	. For instance, the identification of an edge matching in G is topologically identical to evaluating an independent set of

vertices within	, thereby allowing robust methodologies from traditional vertex analysis to directly dictate solutions for edge-based network routing and connectivity limits.

NetworkX Functions Used

nx.line\_graph(G): The Line Graph function, denoted as	, performs a fundamental structural transformation by shifting the graph's topology from a vertex-centric perspective to an edge-centric one.

Formally, for a given graph	, the line graph	is constructed such that its vertex set is

exactly the edge set E of the original graph. Two nodes in	are connected by an edge if and only if their corresponding edges in G are incident to a common vertex. This transformation is particularly

powerful for analyzing link-based properties; for instance, finding a "node coloring" in	is mathematically equivalent to finding an "edge coloring" in G  
nx.to\_numpy\_array(G): The nx.to\_numpy\_array(G) function serves as the primary bridge between the symbolic world of graph theory and the numerical world of linear algebra. It generates a two-dimensional NumPy array representing the Adjacency Matrix A of the graph, where the dimensions are ![][image5] (with n

being the number of nodes). In this matrix, the element    typically holds a value of 1 if an edge exists

between node i and node j, and 0 otherwise; however, if the graph is weighted,  will instead store the specific weight value of that edge/

# **Code :**

\#lineg\_in.py (with NetworkX functions) import matplotlib.pyplot as plt

import networkx as nx def get\_adj():

nv \= int(input("Vertices: ")) v \= range(nv)

print("\\nAdjacency Matrix: ") adj \= \[\]

for i in v:

row \= tuple(int(e) for e in input(f"Row{i}: ").split(" "))

if len(row) \!= nv: print("Invalid Entry") break

adj.append(row) e \= set()

for i in range(nv): for j in range(nv):

if adj\[i\]\[j\] \== 1:

e.add((i,j) if i\<j else (j,i)) return v, e

def visualize(G, L\_G):

fig, (ax1, ax2) \= plt.subplots(1, 2, figsize=(12, 5))

nx.draw(G, ax=ax1, with\_labels=True, node\_color='lightblue') ax1.set\_title("Original G")

nx.draw(L\_G, ax=ax2, with\_labels=True, node\_color='lightcoral') ax2.set\_title("Line Graph L(G)")

plt.show() def main():

v, e \= get\_adj() G \= nx.Graph()

G.add\_nodes\_from(v) G.add\_edges\_from(e) LG \= nx.line\_graph(G) visualize(G, LG)

if  name	\== " main ": main()

\# lineg\_mn.py (without NetworkX functions) import matplotlib.pyplot as plt

import networkx as nx def get\_adj():

nv \= int(input("Vertices: ")) v \= range(nv)

print("\\nAdjacency Matrix: ") adj \= \[\]

for i in v:

row \= tuple(int(e) for e in input(f"Row{i}: ").split(" "))

if len(row) \!= nv: print("Invalid Entry") break

adj.append(row) e \= set()

for i in range(nv): for j in range(nv):

if adj\[i\]\[j\] \== 1:

e.add((i,j) if i\<j else (j,i)) return v, e

def line\_graph(G):

lv \= list(G.edges())

LG \= nx.Graph() LG.add\_nodes\_from(lv) le \= \[\]

for i in range(len(lv)):

for j in range(i+1, len(lv)):

if len({ \*lv\[i\], \*lv\[j\] }) \== 3:

le.append((lv\[i\], lv\[j\])) LG.add\_edges\_from(le) return LG

def visualize(G, L\_G):

fig, (ax1, ax2) \= plt.subplots(1, 2, figsize=(12, 5))

nx.draw(G, ax=ax1, with\_labels=True, node\_color='lightblue') ax1.set\_title("Original G")

nx.draw(L\_G, ax=ax2, with\_labels=True, node\_color='lightcoral') ax2.set\_title("Line Graph L(G)")

plt.show() def main():

v, e \= get\_adj() G \= nx.Graph()

G.add\_nodes\_from(v) G.add\_edges\_from(e) LG \= line\_graph(G) visualize(G, LG)

if  name	\== " main ": main()

# **Output:**

# **Conclusion:**

A program converting a given graph into its corresponding line graph was successfully implemented

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAPCAYAAAACsSQRAAAAhUlEQVR4XmNgwA7+Q3EIlIaB3UhsnOA9A6omGMAljgFAis6iCyIBgoYYMRBWREiesAIGAmrKGAgoIAbAYoIiADKgE12QSAAKSzAg5Ap8LnWBMUAK7iJJoANcBoAA3BAQwKcQnxyKITMZsCvG5xUQQDEEBmCa8GlEBlgNIRVQbAgoR4NdDADzQSXKfrusoAAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAPCAYAAAAGRPQsAAAAhElEQVR4XqWSgQ2AMAgEGcEZHNIdHMEZnMkZHEFL0lIC30D1ElLK40dIiTBniafEVWKreUPnIaNmro80h/0DRKQLmcZMj+wnIjTLjJdmarERf8zct3y5dQEQ9axUTZ07AOm2JncrWCKdceNalnoiTQP1nfrYvIcM0OgL/EYbh8qnaRNIvLwkMGmN36z0AAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAANCAYAAADbnyzoAAAAi0lEQVR4Xt2S7QmAMAxEbxZncgZHcBendAQlQiHmA9MYUXzQH314R1IEvskmRZYRhWWMJzqP0qriqh6TO4O2nMpPloTtoszI51VusCRs10umQ2WUgO2ieAt7rOKuslLIexTK9WYXKWB0cCG3iUB5erUqTgPyrdXkF/R+H8Ud8G3aLPz8G7mtd9L/5w4iGjf8NyNe8wAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD8AAAAPCAYAAABTJRdyAAABGklEQVR4XtWWDRHCMAyFKwENSEADEtCABDwgAQ1IQAMS0IAEWGDZhXf52625G99dD5qXJmnXrW1N5zW2y9Cu4/+1wzUfxl9pT2M5c/AlcIwoTqRLyPeIxoFN+2o3FDR6F4U8oO/lQ18LazwT6RMZx4yPhTUW7di3yDzVVKyUUyG8C7J13FvON/Q5tYTTyqB66WO8mDkrvha61etNfj+0LfQRa2wVeJQhu/b90hOydoLn+pSGqWPgJfO0CugBRDm1BypPEFqUj645Ip7uaVVEOUk/Kza1j4IkWhxPk3CcTONtaxHljHTix0cbwDZNYzytEspL7zfCC+ih6nx+qqLBHN8KuN5et8JZdA1WjKx18T2Brpf/MnneIVN7A3LRdQEV3T3XAAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAICAYAAABkkNZlAAAAlklEQVR4XqWTgQ2AIAwEO4JDOYLLOYMjOIszOIL6hir5vgJ6CYm9foGQaPafjQVR6jfhm+Wb1h7wlJtZCNS5oM+LPLTkjeRqwYWm9N0y56iZ4IIw7Up8mQE8tx5rJBdCqBFswffwF60FczzD9znFIFwLnOf6DZUNLgi7XXhygZoHT57hHGr/ca4eh4ByilKu1Acq01nyO2hdMifHtQw6AAAAAElFTkSuQmCC>