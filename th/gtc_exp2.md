#### **Experiment No**: 2	 **Date**: 05/02/2026

# 

**Aim :** To implement graph isomorphism verification inorder to compare structural equivalence of the 2 graphs.   

### **Theory:** Let G and H denote two finite, undirected simple graphs characterized by their respective vertex sets [![][image1]](https://www.codecogs.com/eqnedit.php?latex=V\(G\)#2) and [![][image2]](https://www.codecogs.com/eqnedit.php?latex=V\(H\)#2), and their edge sets [![][image3]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)#2) and [![][image4]](https://www.codecogs.com/eqnedit.php?latex=E\(H\)#2). The graphs G and H are defined to be isomorphic, denoted mathematically as [![][image5]](https://www.codecogs.com/eqnedit.php?latex=G%20%5Ccong%20H#2), if there exists a bijective mapping ![][image6] that fundamentally preserves the adjacency relation. Specifically, this theoretical condition requires that for any pair of vertices [![][image7]](https://www.codecogs.com/eqnedit.php?latex=u%2C%20v%20%5Cin%20V\(G\)#2), the edge [![][image8]](https://www.codecogs.com/eqnedit.php?latex=uv#2) is an element of [![][image9]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)#2) if and only if the corresponding edge [![][image10]](https://www.codecogs.com/eqnedit.php?latex=%5Ctheta\(u\)%5Ctheta\(v\)#2) is an element of [![][image11]](https://www.codecogs.com/eqnedit.php?latex=E\(H\)#2). This isomorphic mapping [![][image12]](https://www.codecogs.com/eqnedit.php?latex=%5Ctheta#2) establishes that G and H possess identical structural topologies, indicating that one graph may be obtained from the other purely through a permutation of the vertex labels, thereby rendering them indistinguishable from a strictly graph-theoretic perspective.

Due to the inherent computational complexity associated with discovering such a bijective mapping across all possible factorial permutations, the analytical verification of isomorphism heavily relies upon the evaluation of structural invariants. An invariant is defined as a measurable graph property that is rigorously preserved under any isomorphic mapping. The most fundamental necessary conditions dictate that isomorphic graphs must exhibit an identical order, denoted as [![][image13]](https://www.codecogs.com/eqnedit.php?latex=%5Cnu\(G\)%20%3D%20%7CV\(G\)%7C#2), and an identical size, denoted as [![][image14]](https://www.codecogs.com/eqnedit.php?latex=%5Cvarepsilon\(G\)%20%3D%20%7CE\(G\)%7C#2). Consequently, if [![][image15]](https://www.codecogs.com/eqnedit.php?latex=%5Cnu\(G\)%20%5Cneq%20%5Cnu\(H\)#2) or [![][image16]](https://www.codecogs.com/eqnedit.php?latex=%5Cvarepsilon\(G\)%20%5Cneq%20%5Cvarepsilon\(H\)#2), one immediately deduces that [![][image17]](https://www.codecogs.com/eqnedit.php?latex=G%20%5Cnot%5Ccong%20H#2). Furthermore, the bijection strictly preserves vertex degrees, implying that [![][image18]](https://www.codecogs.com/eqnedit.php?latex=d_G\(v\)%20%3D%20d_H\(%5Ctheta\(v\)\)#2) for all [![][image19]](https://www.codecogs.com/eqnedit.php?latex=v%20%5Cin%20V\(G\)#2). This mathematically necessitates that the degree sequence—the monotonically non-increasing ordered list of all vertex degrees within the graph—must be entirely identical for both G and H. However, it is imperative to establish that the equivalence of degree sequences constitutes a necessary but globally insufficient condition for isomorphism, as non-isomorphic graphs exhibiting identical degree sequences, formally termed degree-equivalent or isogonal graphs, are thoroughly documented in discrete mathematics.

Beyond fundamental vertex metrics, the condition of isomorphism mandates the strict topological preservation of higher-order cyclic and cohesive substructures. Any arbitrary cycle [![][image20]](https://www.codecogs.com/eqnedit.php?latex=C_k#2) of length k embedded within G must map bijectively to a corresponding cycle of identical length within H. Consequently, global cyclic properties, such as the girth, denoted as [![][image21]](https://www.codecogs.com/eqnedit.php?latex=g\(G\)#2) and defined as the length of the shortest cycle in the graph, must rigorously satisfy the equality [![][image22]](https://www.codecogs.com/eqnedit.php?latex=g\(G\)%20%3D%20g\(H\)#2). Because the exhaustive enumeration of cycle bases typically demands exponential time complexity through depth-first search traversals, theorists frequently examine supplementary invariants to systematically prune the algorithmic search space. These advanced structural invariants include the clique number [![][image23]](https://www.codecogs.com/eqnedit.php?latex=%5Comega\(G\)#2), which defines the maximum cardinality of a complete subgraph [![][image24]](https://www.codecogs.com/eqnedit.php?latex=K_n#2) contained within G; the chromatic number [![][image25]](https://www.codecogs.com/eqnedit.php?latex=%5Cchi\(G\)#2), representing the minimum number of independent sets into which [![][image26]](https://www.codecogs.com/eqnedit.php?latex=V\(G\)#2) can be validly partitioned; and the connectivity parameters, specifically the vertex connectivity [![][image27]](https://www.codecogs.com/eqnedit.php?latex=%5Ckappa\(G\)#2) and the edge connectivity [![][image28]](https://www.codecogs.com/eqnedit.php?latex=%5Ckappa'\(G\)#2). A structural divergence localized within any single invariant definitively precludes the possibility of an isomorphic relation.

In the absence of a generalized polynomial-time resolution for the graph isomorphism problem, exact algorithmic methodologies predominantly rely upon sophisticated backtracking paradigms. The canonical state-space search algorithm systematically constructs the putative bijection [![][image29]](https://www.codecogs.com/eqnedit.php?latex=%5Ctheta#2) by iteratively mapping a candidate vertex [![][image30]](https://www.codecogs.com/eqnedit.php?latex=u%20%5Cin%20V\(G\)#2) to a vertex [![][image31]](https://www.codecogs.com/eqnedit.php?latex=v%20%5Cin%20V\(H\)#2) under the strict initial constraint that [![][image32]](https://www.codecogs.com/eqnedit.php?latex=d_G\(u\)%20%3D%20d_H\(v\)#2). The procedure advances recursively, continuously verifying that the local adjacency of the currently maintained partial mapping remains strictly inviolate. Should a structural conflict manifest—for instance, if the edge [![][image33]](https://www.codecogs.com/eqnedit.php?latex=uw%20%5Cin%20E\(G\)#2) exists but the corresponding mapped vertices remain non-adjacent in the target graph H—the algorithm formally backtracks, discarding the structurally invalid partial mapping and traversing an alternative branch of the search space. Modern computational implementations frequently utilize advanced search heuristics, such as those formalized in the VF2 algorithm, which significantly augment standard backtracking processes. By integrating rigorous feasibility rules, these state-based algorithms preemptively evaluate the localized neighborhood topologies of both mapped and unmapped vertices concurrently. This continuous state evaluation mechanism aggressively prunes invalid mapping trajectories exceedingly early in the recursive generation tree, vastly reducing the overall computational overhead required to definitively establish [![][image34]](https://www.codecogs.com/eqnedit.php?latex=G%20%5Ccong%20H#2) or geometrically confirm non-isomorphism.

---

### NetworkX Functionality for Isomorphism

## nx.is\_isomorphic(G1, G2): This is the primary high-level function. It acts as a wrapper that automatically selects the most efficient algorithm based on the graph type.

Under the Hood: For most general graphs, it utilizes a version of the VF2 algorithm. It first checks basic invariants (node/edge counts) before proceeding to the more complex structural mapping.

## nx.isomorphism.GraphMatcher: For cases where you need more than a simple "True/False" answer, the GraphMatcher class is utilized.

Mapping Extraction: After confirming isomorphism, you can use .mapping to retrieve the actual dictionary showing which node in G1 corresponds to which node in G2.Sub-isomorphism: It can also determine if G1 is a subgraph isomorphism of G2 (i.e., whether G1 exists as a part of the larger graph G2).

## Nx.degree\_sequence\_similarity: While not a direct test for isomorphism, NetworkX provides utilities to compare degree distributions. This is often used as a Pre-Filter. If the degree sequence similarity is not 1.0, there is no need to run the expensive VF2 algorithm.

**Code :**

\# iso\_in.py (with NetworkX functions)  
import matplotlib.pyplot as plt   
import networkx as nx   
fig, ax \= plt.subplots(1, 3, figsize=(15, 5))  
def create\_graph():  
    nodes \= list(range(1, 8))  
    cycle\_edges \= \[(i, i % 7 \+ 1\) for i in nodes\]  
    G1 \= nx.Graph()  
    G1.add\_nodes\_from(nodes)  
    innr\_ring1 \= \[(i, (i+1)% 7 \+ 1 ) for i in nodes\]  
    G1.add\_edges\_from(cycle\_edges \+ innr\_ring1)  
    G2 \= nx.Graph()  
    G2.add\_nodes\_from(nodes)  
    innr\_ring2 \= \[(1,3), (1,6), (2,4), (2,6), (3,5), (4,7), (5,7)\]  
    G2.add\_edges\_from(cycle\_edges \+ innr\_ring2)  
    G3 \= nx.Graph()  
    G3.add\_nodes\_from(nodes)  
    innr\_ring3 \= \[(1,4), (1,5), (2,6), (2,7), (3,5), (3,7), (4,6)\]  
    G3.add\_edges\_from(cycle\_edges \+ innr\_ring3)  
    return G1, G2, G3  
def plot\_graph(g, idx, title):  
    pos \= nx.circular\_layout(g)  
    nx.draw(  
            g,  
            pos=pos,  
            ax=ax\[idx\],  
            with\_labels=True,  
            node\_color="cyan",  
            edge\_color="blue"  
            )  
    ax\[idx\].set\_title(title)  
def is\_iso(g1, g2):  
    GM \= nx.isomorphism.GraphMatcher(g1, g2)  
    if GM.is\_isomorphic():  
        print("Graphs are Isomorphic")  
        print(f"|v| \= {g1.number\_of\_nodes()}   |e| \= {g1.number\_of\_edges()}")  
        print(f"Mapping: {GM.mapping}")  
    else:  
        print("Graphs are NOT Isomorphic")  
def main():  
    g1, g2, g3 \= create\_graph()  
    print("\\n--- For G1 n G2 \---")  
    is\_iso(g1, g2)  
    print("\\n--- For G2 n G3 \---")  
    is\_iso(g2, g3)  
    print("\\n--- For G1 n G3 \---")  
    is\_iso(g1, g3)  
    plot\_graph(g1, 0, "G1")  
    plot\_graph(g2, 1, "G2")  
    plot\_graph(g3, 2, "G3")  
    plt.tight\_layout()  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

\# iso\_mn.py (without using NetworkX functions)  
import matplotlib.pyplot as plt   
import networkx as nx   
fig, ax \= plt.subplots(1, 3, figsize=(15, 5))  
def create\_graph():  
    nodes \= list(range(1, 8))  
    cycle\_edges \= \[(i, i % 7 \+ 1\) for i in nodes\]  
    G1 \= nx.Graph()  
    G1.add\_nodes\_from(nodes)  
    innr\_ring1 \= \[(i, (i+1)% 7 \+ 1 ) for i in nodes\]  
    G1.add\_edges\_from(cycle\_edges \+ innr\_ring1)  
    G2 \= nx.Graph()  
    G2.add\_nodes\_from(nodes)  
    innr\_ring2 \= \[(1,3), (1,6), (2,4), (2,6), (3,5), (4,7), (5,7)\]  
    G2.add\_edges\_from(cycle\_edges \+ innr\_ring2)  
    G3 \= nx.Graph()  
    G3.add\_nodes\_from(nodes)  
    innr\_ring3 \= \[(1,4), (1,5), (2,6), (2,7), (3,5), (3,7), (4,6)\]  
    G3.add\_edges\_from(cycle\_edges \+ innr\_ring3)  
    return G1, G2, G3  
def plot\_graph(g, idx, title):  
    pos \= nx.circular\_layout(g);  
    nx.draw(  
            g,  
            pos=pos,  
            ax= ax\[idx\],  
            with\_labels=True,  
            node\_color="cyan",  
            edge\_color="blue"  
            )  
    ax\[idx\].set\_title(title)  
def deg\_seq(G):  
    ds \= sorted(\[d for \_, d in nx.degree(G)\], reverse=True)  
    return ds  
def get\_adj\_list(G):  
    vertices \= list(G.nodes())  
    edges \= list(G.edges())  
    adj \= {v: \[\] for v in vertices}  
    for e0,e1 in edges:  
        adj\[e0\].append(e1)  
        adj\[e1\].append(e0)  
    return adj  
def cycles(G):  
    vertices \= list(G.nodes())  
    edges \= list(G.edges())  
    adj\_list \= get\_adj\_list(G)  
    cycles\_path \= set()  
    def dfs(cur, parent, path):  
        if cur \== root and len(path)\>=3:  
            norm\_cyl \= tuple(sorted(path))  
            cycles\_path.add(norm\_cyl)  
            return    
        for v in adj\_list\[cur\]:  
            if v \== parent:  
                continue  
            if v \< root:  
                continue  
            if vis\[v\] \== True and v\!=root:  
                continue  
              
            if v \!= root:  
                vis\[v\] \= True  
            dfs(v, cur, path \+ \[v\])  
            if v \!= root:  
                vis\[v\] \= False  
    for root in vertices:  
        vis \= {v: False for v in vertices};  
        vis\[root\] \= True  
        dfs(root, \-1, \[root\])  
    return cycles\_path  
def cyl\_degree(G, cycles):  
    cyl\_deg \= \[\]  
    for cyl in cycles:  
        node \= sorted(\[G.degree(n) for n in cyl\])  
        cyl\_deg.append(node)  
    return sorted(cyl\_deg)  
def bi\_map(g1, g2):  
    def solve(mapping, unmapped1, unmapped2):  
        if not unmapped1:  
            return mapping  
        u \= unmapped1\[0\]  
          
        for v in unmapped2:  
            if g1.degree(u) \== g2.degree(v):  
                is\_consistent \= True  
                for u\_mapped, v\_mapped in mapping.items():  
                    if g1.has\_edge(u, u\_mapped) \!= g2.has\_edge(v, v\_mapped):  
                        is\_consistent \= False  
                        break  
                  
                if is\_consistent:  
                    new\_mapping \= mapping.copy()  
                    new\_mapping\[u\] \= v  
                    solution \= solve(new\_mapping, unmapped1\[1:\], \[n for n in unmapped2 if n \!= v\])  
                    if solution:  
                        return solution  
        return None  
    nodes1 \= sorted(list(g1.nodes()), key=g1.degree, reverse=True)  
    nodes2 \= list(g2.nodes())  
    return solve(mapping={}, unmapped1=nodes1, unmapped2=nodes2)  
def is\_iso(g1, g2):  
    v1 \= nx.number\_of\_nodes(g1)  
    v2 \= nx.number\_of\_nodes(g2)  
    if(v1 \!= v2):  
        print("Not isomorphic (Vertex mismatch)")  
        print(f"v1 \= {v1} v2 \= {v2}")  
        return   
    e1 \= nx.number\_of\_edges(g1)  
    e2 \= nx.number\_of\_edges(g2)  
    if(e1 \!= e2):  
        print("Not isomorphic (Edges mismatch)")  
        print(f"e1 \= {e1} e2 \= {e2}")  
        return  
    d1 \= deg\_seq(g1)  
    d2 \= deg\_seq(g2)  
    if(d1 \!= d2):  
        print("Not isomorphic (Degree Sequence mismatch)")  
        print(f"d1 \= {d1} d2 \= {d2}")  
        return   
      
    cyl1 \= cycles(g1)  
    cyl2 \= cycles(g2)  
    if(len(cyl1) \!= len(cyl2)):  
        print("Not isomorphic (Cycle Count mismatch)")  
        print(f"cyl1 \= {len(cyl1)} cyl2 \= {len(cyl2)}")  
        return   
    cyl\_deg1 \= sorted(cyl\_degree(g1, cyl1))  
    cyl\_deg2 \= sorted(cyl\_degree(g2, cyl2))  
    if(cyl\_deg1 \!= cyl\_deg2):  
        print("Not isomorphic (Cycle degree mismatch)")  
        return  
    mapping \= bi\_map(g1, g2)  
    if not mapping:  
        print("Graphs are not isomorphic (bijection not found).")  
        return  
    print("Graphs are Isomorphic")  
    print(f"|v1| \= {v1}     |v2| \= {v2}")  
    print(f"|e1| \= {e1}     |e2| \= {e2}")  
    print(f"deg1 \= {d1}     d2 \= {d2}")  
    print(f"Mapping: {mapping}")  
def main():  
    g1, g2, g3 \= create\_graph()  
    print("\\n--- For G1 n G2 \---")  
    is\_iso(g1, g2)  
    print("\\n--- For G2 n G3 \---")  
    is\_iso(g2, g3)  
    print("\\n--- For G1 n G3 \---")  
    is\_iso(g1, g3)  
    plot\_graph(g1, 0, "G1")  
    plot\_graph(g2, 1, "G2")  
    plot\_graph(g3, 2, "G3")  
    plt.tight\_layout()  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:**

**Conclusion:**  
A program checking graph isomorphism verification inorder to compare structural equivalence of the 2 graphs was successfully implemented

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARBAMAAABdpfM7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAF0lEQVR4XmP8z4AJmNAFQGBUEA0QLwgAe8UBIZ8Qt8oAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARBAMAAABdpfM7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAF0lEQVR4XmP8z4AJmNAFQGBUEA0QLwgAe8UBIZ8Qt8oAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAMBAMAAADff4MYAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAFUlEQVR4XmP8z4ALMKELIMCoFDIAAFJAARcdQ4qvAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIUAAAARBAMAAAABA3JaAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMomrze9EIt1mEJl2VLuxdC03AAAAIUlEQVR4XmP8z0Ap+MiELkIGGDUDFYyagQpGzUAFw8kMANFuAhJa+Fq9AAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAARBAMAAACr7HajAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAHElEQVR4XmP8z0A8YEIXwAdGFSODUcXIYJAoBgAu+wEhYVrUUAAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAIBAMAAADtmgmaAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAFElEQVR4XmP8zwABH5mgDAYGSlgAlFgCAEI0TvcAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAARBAMAAABz4NKpAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMomrze9EIt1mEJl2VLuxdC03AAAAGElEQVR4XmP8z4APMKELoIJRaaxg6EoDADEeASFPfq+6AAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARBAMAAABdpfM7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAF0lEQVR4XmP8z4AJmNAFQGBUEA0QLwgAe8UBIZ8Qt8oAAAAASUVORK5CYII=>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAMBAMAAABcu7ojAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMomrze9EIt1mEJl2VLuxdC03AAAAEklEQVR4XmP8z8DwkYkBCEgnAHKJAghwVQU8AAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGwAAAARBAMAAADK9FThAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECJEVGaJmbvN3e92qzLq0JJAAAAAHUlEQVR4XmP8z0AOYEIXIA6MasMAo9owwKg2DAAA5EUBITcd9moAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGwAAAARBAMAAADK9FThAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARHaZq7vN791mMhAiiVQBKChAAAAAHUlEQVR4XmP8z0AOYEIXIA6MasMAo9owwKg2DAAA5EUBITcd9moAAAAASUVORK5CYII=>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGEAAAARCAMAAAD6+jJQAAADAFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALI7fhAAAAEnRSTlMAECJEVGaJmbvN3e92qzLR+cnh8hGTAAABO0lEQVR4XqWU227CMAyGQ+lAHXST/P7PmI0ViQ3YIU7ixCeE0P6LOvl8StK0IQit5PQhgQYeeq52hy7AAK8lRUnVaoAqpsMmmrdgxpgcxJSzkhkV5xKN1sxR5DdolJZHZiAHg5Gx8O0XvKdNGw1z2VWvc68iXwDANpsQtkRr6X2dRhgXU/JAA7EXVxG+0hNO6W7gALWv9VryGOAd+SeBdC596EieYdGJT4q/Lzu98Z9kNjpvfgoUvPrljrbDpumqibgf5U3bhS2xbVQ0ALHDnDd9MFLv6GsnuYNtgDpqgLKRMvml2g4HOKqYSEd45rRK34oESvJCwCxhTC9WwdRimUN8kzRrMvkELnmZUFqiOZcjUMfjfej5wpPMFrpuuBT2ojijz+gfsi1mPrFuJtdp4aTm3s/7lpyfOjb4AxuVPpLGEyAHAAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF8AAAARCAMAAACMwIDbAAADAFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALI7fhAAAAEnRSTlMARHaZq7vN791mMhAiiVTR+clMvi1kAAABNUlEQVR4Xq2U0W7DIAxFnSxLuqSdVP//NzJpVbdV67QFsI1tSKRKOw8N9sXGgCnAPzF5BwB6BzNFBaO+eGkLyoUrAGP++AXYlLnKp2i4io9j2W5glzkVYYeN/Ag9C8UXyL6k32eyhFZpEtORLcpAFk9Q0kl8moPxmtCVM33JF3BY17Z53njQTA/zVxkv13qO294gabhVflnKqHQROYnIdFVGJskdbyPmP463n5jkKZ03XefwCjT3Y6mTMAHvF1MOFV/Sa7Io3UODmWzyGotuswpCeTbYjzz0fOfPwXo16I4S5M7KlvujDDOBa8ntaTGnv4neZFdajIMRPl8g8LHvpZTQ6cbm+z1dLqcywfFOK/Q/kOs9xYZi3m96ax7U3ZOqfIDZ7b3egFlyo8hEU9vpjYdpLBBdfzBnOskEE/zsAAAAAElFTkSuQmCC>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAQCAMAAABum6z5AAADAFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALI7fhAAAAFnRSTlMAIlSJq7vN3e+ZZjIQdkT7/XzZ8ZHBHs21wgAAAL9JREFUeF6Nkd0OwiAMhc/mlqib3sn7Px/ZjWYaTdRIS/kpaPC7aEvLoVAAxhjjbOcXEcr9xBdZx0wSGiWT2LmenOXVLVTHyVraIXlNkuqAvWvW60bSfQaGrBAOZm+pcI81xJusTnSIe0vK/EpmJtPvdCWRXy2xJ0OD+EpXNApnLCDRpcgKJ70Ert69QaKjKgXqcYuIGPhHoBr5kXN4fkhOnq6/Z9TXq6aQ/ZKw3cRQqER/0NBUPZjXs8y0aTTCB0PvHRpXhJU6AAAAAElFTkSuQmCC>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIEAAAARBAMAAAAI6NIgAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAIUlEQVR4XmP8z0AZ+MiELkIyGDUBAkZNgIBREyBgeJgAAI8MAhJldYqNAAAAAElFTkSuQmCC>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAARBAMAAAB9SazGAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAGUlEQVR4XmP8z0AQfGRCF8EGRhWNKiJSEQDMQwISm0IW8wAAAABJRU5ErkJggg==>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAPBAMAAADwnzkiAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlR2q7vN3e+JEESZMmZ6kRRHAAAAFUlEQVR4XmP8zwABH5mgDAaGgWcBACKXAg4rJRX6AAAAAElFTkSuQmCC>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAARBAMAAAClRQjMAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAImarzd2JRO8yuxCZdlRn2aP5AAAAF0lEQVR4XmP8z4AGPjKhizAwjArhEQIAdrMCEncGwcoAAAAASUVORK5CYII=>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAAARBAMAAADQyLRvAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAImarzd2JRO8yuxCZdlRn2aP5AAAAHElEQVR4XmP8z0AaYEIXIARGNRADRjUQAwahBgB3fwEhAiXjQAAAAABJRU5ErkJggg==>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAARBAMAAABHmRO1AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEGZ2VKuZiTLdzUS7Iu9dShvpAAAAFElEQVR4XmP8z4AOmNAFRoXwCgEAV4MBIahw8FIAAAAASUVORK5CYII=>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAPBAMAAAAWtvJmAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAq+/dzbsQImZUdomZRDJRcMDgAAAAEklEQVR4XmP8zwADTHDWYGMCAK2sAR2ZwXt6AAAAAElFTkSuQmCC>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAARBAMAAABHmRO1AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARJnN7927q2YiMnaJEFT+4nNwAAAAFElEQVR4XmP8z4AOmNAFRoXwCgEAV4MBIahw8FIAAAAASUVORK5CYII=>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAARBAMAAAClRQjMAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMpnvzVRmRLvdIhB2iasAeVe9AAAAF0lEQVR4XmP8z4AGPjKhizAwjArhEQIAdrMCEncGwcoAAAAASUVORK5CYII=>

[image28]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMpnvzVRmRLvdIhB2iasAeVe9AAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image29]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAMBAMAAABcu7ojAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMomrze9EIt1mEJl2VLuxdC03AAAAEklEQVR4XmP8z8DwkYkBCEgnAHKJAghwVQU8AAAAAElFTkSuQmCC>

[image30]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAARBAMAAAB9SazGAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAGUlEQVR4XmP8z0AQfGRCF8EGRhWNKiJSEQDMQwISm0IW8wAAAABJRU5ErkJggg==>

[image31]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAARBAMAAACMQvdLAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAGElEQVR4XmP8z0AYMKELYAOjikYVEakIAJ3kASFjDJSjAAAAAElFTkSuQmCC>

[image32]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGwAAAARBAMAAADK9FThAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAHUlEQVR4XmP8z0AOYEIXIA6MasMAo9owwKg2DAAA5EUBITcd9moAAAAASUVORK5CYII=>

[image33]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFQAAAARBAMAAACx0JYtAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAGElEQVR4XmP8z0AsYEIXwA1GlY4qHXClAAq5ASFXGRIQAAAAAElFTkSuQmCC>

[image34]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAMBAMAAADff4MYAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAFUlEQVR4XmP8z4ALMKELIMCoFDIAAFJAARcdQ4qvAAAAAElFTkSuQmCC>