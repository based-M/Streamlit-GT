#### **Experiment No**: 6	**Date**: 09/04/26

# 

### **Aim :** To implement finding the minimum spanning tree for a given graph using Kruskal's algorithm, ensuring all vertices are connected with the minimum possible total edge weight and without forming cycles

### **Theory:**Let [![][image1]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2) denote a connected, undirected simple graph, characterized by a finite vertex set [![][image2]](https://www.codecogs.com/eqnedit.php?latex=V\(G\)#2) of order [![][image3]](https://www.codecogs.com/eqnedit.php?latex=%5Cnu#2) and an edge set [![][image4]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)#2) of size [![][image5]](https://www.codecogs.com/eqnedit.php?latex=%5Cvarepsilon#2). To model operational costs inherent in applied networks---such as transport grids or circuitry---one defines a weighted graph by introducing a real-valued weight function [![][image6]](https://www.codecogs.com/eqnedit.php?latex=w%3A%20E%20%5Crightarrow%20%5Cmathbb%7BR%7D#2), assigning a distinct scalar cost to each edge [![][image7]](https://www.codecogs.com/eqnedit.php?latex=e%20%5Cin%20E\(G\)#2). The analytical objective is to extract a spanning tree, T, formally defined as a connected, acyclic spanning subgraph such that [![][image8]](https://www.codecogs.com/eqnedit.php?latex=V\(T\)%20%3D%20V\(G\)#2). Topologically, the requisite acyclic connectivity mandates that the cardinality of the edge set for any spanning tree is precisely [![][image9]](https://www.codecogs.com/eqnedit.php?latex=%7CE\(T\)%7C%20%3D%20%5Cnu%20-%201#2). An optimal tree, or minimum spanning tree, denoted as [![][image10]](https://www.codecogs.com/eqnedit.php?latex=T%5E*#2), is defined as a spanning tree that minimizes the total aggregate edge weight, expressed mathematically as [![][image11]](https://www.codecogs.com/eqnedit.php?latex=w\(T%5E*\)%20%3D%20%5Csum_%7Be%20%5Cin%20E\(T%5E*\)%7D%20w\(e\)#2). It must be noted that while the minimized scalar weight [![][image12]](https://www.codecogs.com/eqnedit.php?latex=w\(T%5E*\)#2) is a strict invariant of G, the specific structural composition of [![][image13]](https://www.codecogs.com/eqnedit.php?latex=T%5E*#2) may not be mathematically unique, particularly within graphs exhibiting non-distinct edge weights.

The deterministic construction of an optimal tree relies upon two foundational graph-theoretic invariants: the cut property and the cycle property. The cut property dictates that for any proper, non-empty vertex partition [![][image14]](https://www.codecogs.com/eqnedit.php?latex=S%20%5Csubset%20V\(G\)#2), if an edge e possessing the strictly minimum weight is incident to exactly one vertex in S and one vertex in [![][image15]](https://www.codecogs.com/eqnedit.php?latex=V\(G\)%20%5Csetminus%20S#2), then e must necessarily be a constituent element of at least one minimum spanning tree [![][image16]](https://www.codecogs.com/eqnedit.php?latex=T%5E*#2). Conversely, the cycle property operates as an exclusionary condition; for any arbitrary cycle C embedded within G, the edge exhibiting the strictly maximum weight within [![][image17]](https://www.codecogs.com/eqnedit.php?latex=E\(C\)#2) cannot be structurally incorporated into any minimum spanning tree. These dual properties mathematically validate the deployment of greedy algorithmic heuristics, guaranteeing that locally optimal structural selections monotonically converge upon a globally optimal topological configuration.

The quintessential procedural realization of this greedy methodology is Kruskal's algorithm. In accordance with the formal sequence of operations provided in the primary text, the algorithm is executed through the following proper steps:

Step 1\. Choose a link [![][image18]](https://www.codecogs.com/eqnedit.php?latex=e_1#2) such that [![][image19]](https://www.codecogs.com/eqnedit.php?latex=w\(e_1\)#2) is as small as possible.

Step 2\. If edges [![][image20]](https://www.codecogs.com/eqnedit.php?latex=e_1%2C%20e_2%2C%20%5Cdots%2C%20e_i#2) have been chosen, then choose an edge [![][image21]](https://www.codecogs.com/eqnedit.php?latex=e_%7Bi%2B1%7D#2) from [![][image22]](https://www.codecogs.com/eqnedit.php?latex=E%20%5Csetminus%20%5C%7Be_1%2C%20e_2%2C%20%5Cdots%2C%20e_i%5C%7D#2) in such a way that: (i) [![][image23]](https://www.codecogs.com/eqnedit.php?latex=G%5B%5C%7Be_1%2C%20e_2%2C%20%5Cdots%2C%20e_%7Bi%2B1%7D%5C%7D%5D#2) is acyclic; (ii) [![][image24]](https://www.codecogs.com/eqnedit.php?latex=w\(e_%7Bi%2B1%7D\)#2) is as small as possible subject to condition (i).

Step 3\. Stop when step 2 cannot be implemented further.

Upon reaching the termination condition in the final step, the accumulated edge set forms a maximal acyclic subgraph. Because the original graph G is assumed to be connected, this subgraph mathematically satisfies all criteria for the optimal minimum spanning tree [![][image25]](https://www.codecogs.com/eqnedit.php?latex=T%5E*#2), thereby formally resolving the fundamental connector problem

---

## NetworkX Functions Used

The nx.minimum\_spanning\_tree(G) function extracts a fundamental structural subgraph T from a connected, undirected, weighted graph [![][image26]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2). Specifically, it guarantees that T is a tree encompassing every vertex in V while strictly minimizing the total sum of its edge weights. By default, NetworkX implements Kruskal's algorithm for this computation, which utilizes a greedy approach: it sorts all edges in ascending order of their weights and iteratively adds them to the growing spanning tree, provided that the new edge does not introduce a cycle (a condition efficiently monitored using a disjoint-set data structure).

**Code :**  
\#mst\_in.py (with NetworkX functions)  
import matplotlib.pyplot as plt   
import networkx as nx   
def create\_graph():  
    G \= nx.Graph()  
    v \= range(1,10)  
    G.add\_nodes\_from(v)  
    e \= \[  
            (1, 2, 14),(1, 3, 5),(1, 4, 2), (2, 3, 9),(2, 4, 8),  
(2, 5, 15),(3, 5, 13),(3, 6, 8),(4, 5, 10),(4, 8, 11),  
            (5, 6, 1),(5, 7, 7),(5, 8, 5),(6, 7, 10),(6, 9, 11),  
            (7, 8, 0),(7, 9, 12),(8, 9, 6)\]  
    G.add\_weighted\_edges\_from(e)  
    return G  
def create\_mst(G):  
    mst \= nx.minimum\_spanning\_tree(G)  
    return mst  
def main():  
    G \= create\_graph()  
    mst \= create\_mst(G)  
    total\_cost \= mst.size(weight='weight')  
    fig, ax \= plt.subplots(2, figsize=(8, 10))  
    pos \= {  
            1: (-1, 0),2: (-0.5, 0),3: (-0.5, 1),4: (-0.5, \-1),  
            5: (0, 0),6: (0.5, 1),7: (0.5, 0),8: (0.5, \-1),9: (1, 0),}  
      
    nx.draw(G, ax=ax\[0\], pos=pos, with\_labels=True, node\_color='lightblue')  
    edge\_labels\_G \= nx.get\_edge\_attributes(G, "weight")  
    nx.draw\_networkx\_edge\_labels(G, pos, edge\_labels=edge\_labels\_G, ax=ax\[0\])  
    ax\[0\].set\_title("Original Graph")  
    nx.draw(mst, ax=ax\[1\], pos=pos, with\_labels=True, node\_color='lightgreen')  
    edge\_labels\_mst \= nx.get\_edge\_attributes(mst, "weight")  
    nx.draw\_networkx\_edge\_labels(mst, pos, edge\_labels=edge\_labels\_mst, ax=ax\[1\])  
    ax\[1\].set\_title(f"Minimum Spanning Tree (Total Cost: {total\_cost})")  
    plt.tight\_layout()  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:** 

\# mst\_mn.py (without NetworkX functions)  
import matplotlib.pyplot as plt  
import networkx as nx  
from itertools import groupby  
def create\_graph():  
    G \= nx.Graph()  
    G.add\_weighted\_edges\_from(\[  
        (1, 2, 14), (1, 3, 5), (1, 4, 2), (2, 3, 9), (2, 4, 8), (2, 5, 15),  
        (3, 5, 13), (3, 6, 8), (4, 5, 10), (4, 8, 11), (5, 6, 1), (5, 7, 7),  
        (5, 8, 5), (6, 7, 10), (6, 9, 11), (7, 8, 0), (7, 9, 12), (8, 9, 6\)  
    \])  
    return G  
class UnionFind:  
    def \_\_init\_\_(self, nodes):  
        self.parent \= {n: n for n in nodes}  
        self.rank \= {n: 0 for n in nodes}  
    def find(self, i):  
        if self.parent\[i\] \== i: return i  
        self.parent\[i\] \= self.find(self.parent\[i\])  
        return self.parent\[i\]  
    def union(self, u, v):  
        root\_u, root\_v \= self.find(u), self.find(v)  
        if root\_u \== root\_v: return False  
        if self.rank\[root\_u\] \< self.rank\[root\_v\]: self.parent\[root\_u\] \= root\_v  
        elif self.rank\[root\_u\] \> self.rank\[root\_v\]: self.parent\[root\_v\] \= root\_u  
        else:  
            self.parent\[root\_v\] \= root\_u  
            self.rank\[root\_u\] \+= 1  
        return True  
def kruskal\_steps(G):  
    mst, uf \= nx.Graph(), UnionFind(G.nodes())  
    mst.add\_nodes\_from(G.nodes())  
    edges \= sorted(G.edges(data=True), key=lambda x: x\[2\]\['weight'\])  
    cost \= 0  
    for w, group in groupby(edges, key=lambda x: x\[2\]\['weight'\]):  
        group \= list(group)  
        acc, rej \= \[\], \[\]  
        for u, v, d in group:  
            if uf.union(u, v):  
                mst.add\_edge(u, v, weight=w)  
                acc.append((u, v))  
                cost \+= w  
            else: rej.append((u, v))  
        if acc: yield w, acc, rej, mst.copy(), cost, nx.number\_connected\_components(mst)  
def draw\_graph(G, pos, title, metrics=None, \*\*kwargs):  
    plt.figure(figsize=(10, 7))  
    nx.draw(G, pos, with\_labels=True, font\_weight='bold', node\_size=700, \*\*kwargs)  
    nx.draw\_networkx\_edge\_labels(G, pos, edge\_labels=nx.get\_edge\_attributes(G, 'weight'))  
    plt.title(title)  
    if metrics:  
        plt.text(0.02, 0.95, metrics, transform=plt.gca().transAxes, fontsize=16,   
                 verticalalignment='top', fontweight='bold')  
def main():  
    G, pos \= create\_graph(), {1:(-1,0), 2:(-0.5,0), 3:(-0.5,1), 4:(-0.5,-1), 5:(0,0), 6:(0.5,1), 7:(0.5,0), 8:(0.5,-1), 9:(1,0)}  
    draw\_graph(G, pos, "Original Graph", node\_color='lightblue')  
      
    for w, acc, rej, mst, cost, comps in kruskal\_steps(G):  
        acc\_s, rej\_s \= ", ".join(f"{u}-{v}" for u,v in acc), ", ".join(f"{u}-{v}" for u,v in rej)  
        title \= f"Step: Weight {w}\\nAccepted: {acc\_s}" \+ (f"\\nRejected: {rej\_s}" if rej else "")  
        draw\_graph(mst, pos, title, f"Cost: {cost}\\nComponents: {comps}", node\_color='lightgreen', edge\_color='red', width=2)  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:**

**Conclusion:**

### A program finding the minimum spanning tree for a given graph using Kruskal's algorithm was successfully implemented

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAECJEVGaJmbvN3e92qzLq0JJAAAAAEUlEQVR4XmP8z8DAwMRAkAAAKEEBDwZAssoAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAIBAMAAADHKvg1AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARHaZq7vN791mMhAiiVQBKChAAAAAEklEQVR4XmP8z8DwkYkBCPATAEolAgAXAr04AAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAAMBAMAAADosUwsAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAGUlEQVR4XmP8z0Ac+MiELoITjKokBgysSgDCrQIIlxX1SAAAAABJRU5ErkJggg==>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAARBAMAAACWfhfFAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAGElEQVR4XmP8z0AIMKELYIJRJdjBiFQCAHmiASHVHlL7AAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGcAAAARBAMAAAAyFK8WAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAHklEQVR4XmP8z0Ay+MiELkIMGNUEBaOaoGBUExQAAN9xAhJwAiJcAAAAAElFTkSuQmCC>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAG8AAAARBAMAAAAhw+/iAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAELvvZjKJIqvNRFSZdt3sD9Z/AAAAHklEQVR4XmP8z0AW+MiELkIsGNWIB4xqxANGNeIBAGREAhLD2H4mAAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAMBAMAAAB2C0uMAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEDKrIkRU77uJZnaZzd0kpKYjAAAAFElEQVR4XmP8zwABH5mgDAYGerAA5SACCJf6BGkAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJwAAAAiBAMAAABYVq17AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAALUlEQVR4Xu3MIQIAAATAQPz/z3RxxF1cWHZ8qh1u3HHuOHecO84d545zx7njBuJiAUO2cGZvAAAAAElFTkSuQmCC>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAARBAMAAABUTlNBAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAF0lEQVR4XmP8z4ANMKELQMCoMCagijAAoAcBIVwRQAIAAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAMBAMAAAB2C0uMAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEDKrIkRU77uJZnaZzd0kpKYjAAAAFElEQVR4XmP8zwABH5mgDAYGerAA5SACCJf6BGkAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAARBAMAAABndUxIAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlSJq83d73ZEZpm7EDJZAI1hAAAAHElEQVR4XmP8z0AE+MiELoIdjCpDA6PK0ACRygAOtAISZ8BdmwAAAABJRU5ErkJggg==>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAARBAMAAACWfhfFAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAGElEQVR4XmP8z0AIMKELYIJRJdjBiFQCAHmiASHVHlL7AAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAMBAMAAAB2C0uMAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEDKrIkRU77uJZnaZzd0kpKYjAAAAFElEQVR4XmP8zwABH5mgDAYGerAA5SACCJf6BGkAAAAASUVORK5CYII=>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAALBAMAAAC5XnFsAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAEUlEQVR4XmP8zwACTGCSUgoAT1ABFRIG5iYAAAAASUVORK5CYII=>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARBAMAAABdpfM7AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAF0lEQVR4XmP8z4AJmNAFQGBUEA0QLwgAe8UBIZ8Qt8oAAAAASUVORK5CYII=>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFgAAAALBAMAAAAJoVdeAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAGElEQVR4XmP8z0A8YEIXwAdGFSODQaIYAANkARVhyUF1AAAAAElFTkSuQmCC>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAMBAMAAABhKdtFAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAFUlEQVR4XmP8z4AEPjIh8xgYBicXAFfGAggqBj+YAAAAAElFTkSuQmCC>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIkAAAARBAMAAAAbP5LUAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAIklEQVR4XmP8z0A5+MiELkIWGDUFOxg1BTsYNQU7GH6mAAAT3wISPdCViwAAAABJRU5ErkJggg==>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJEAAAARBAMAAAAvRlPIAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAIklEQVR4XmP8z0Ad8JEJXYRsMGoScWDUJOLAqEnEgeFtEgCYowISf2fcJwAAAABJRU5ErkJggg==>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAARBAMAAACP9fljAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAGUlEQVR4XmP8z4ALfGRCF0ECo3LYwWCSAwChewISezwUnwAAAABJRU5ErkJggg==>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAMBAMAAAB2C0uMAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEDKrIkRU77uJZnaZzd0kpKYjAAAAFElEQVR4XmP8zwABH5mgDAYGerAA5SACCJf6BGkAAAAASUVORK5CYII=>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>