#### **Experiment No**: 3	 **Date**: 05/02/2026

# 

### **Aim :** To implement generation of various subgraphs such induced subgraphs, spanning subgraphs and edge deleted subgraphs

**Theory:** Let [![][image1]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2) denote a graph, characterized by a non-empty, finite vertex set [![][image2]](https://www.codecogs.com/eqnedit.php?latex=V\(G\)#2) and an edge set [![][image3]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)#2). The analytical deconstruction of G into more localized, topologically tractable units necessitates the formal definition of a subgraph. A graph H is defined as a subgraph of G, denoted mathematically as [![][image4]](https://www.codecogs.com/eqnedit.php?latex=H%20%5Csubseteq%20G#2), if and only if its vertex set satisfies [![][image5]](https://www.codecogs.com/eqnedit.php?latex=V\(H\)%20%5Csubseteq%20V\(G\)#2) and its edge set satisfies [![][image6]](https://www.codecogs.com/eqnedit.php?latex=E\(H\)%20%5Csubseteq%20E\(G\)#2), alongside the fundamental requirement that every edge [![][image7]](https://www.codecogs.com/eqnedit.php?latex=e%20%5Cin%20E\(H\)#2) exclusively links vertices resident within [![][image8]](https://www.codecogs.com/eqnedit.php?latex=V\(H\)#2). By isolating such substructures, researchers are mathematically equipped to analyze localized properties and hierarchal systems embedded within complex macroscopic networks.  
A principal methodology for structural decomposition involves the construction of induced subgraphs. 

Let [![][image9]](https://www.codecogs.com/eqnedit.php?latex=S%20%5Csubseteq%20V\(G\)#2) represent an arbitrary, non-empty subset of the vertex set of G. The subgraph induced by S, formally denoted as [![][image10]](https://www.codecogs.com/eqnedit.php?latex=G%5BS%5D#2), is constructed such that its vertex set is strictly [![][image11]](https://www.codecogs.com/eqnedit.php?latex=V\(G%5BS%5D\)%20%3D%20S#2), and its edge set encapsulates precisely all edges from [![][image12]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)#2) that possess both endpoints entirely within S. Algebraically, this edge set is defined as [![][image13]](https://www.codecogs.com/eqnedit.php?latex=E\(G%5BS%5D\)%20%3D%20%5C%7Buv%20%5Cin%20E\(G\)%20%5Cmid%20u%2C%20v%20%5Cin%20S%5C%7D#2). The defining paradigm of an induced subgraph is the strict topological preservation of localized adjacency; if a specific incidence relation exists between two vertices in the primary graph G, that precise relation must necessarily be preserved within [![][image14]](https://www.codecogs.com/eqnedit.php?latex=G%5BS%5D#2). This property is strictly requisite for the identification of maximum cohesive substructures, such as cliques, where the induced subgraph must intrinsically manifest as a complete graph [![][image15]](https://www.codecogs.com/eqnedit.php?latex=K_n#2).

A fundamentally distinct class of subgraphs arises when the entirety of the primary vertex set is preserved, yielding a spanning subgraph. A subgraph [![][image16]](https://www.codecogs.com/eqnedit.php?latex=H%20%5Csubseteq%20G#2) is designated as a spanning subgraph if it satisfies the structural equality [![][image17]](https://www.codecogs.com/eqnedit.php?latex=V\(H\)%20%3D%20V\(G\)#2), implying that the edge set [![][image18]](https://www.codecogs.com/eqnedit.php?latex=E\(H\)%20%5Csubseteq%20E\(G\)#2) acts as the sole variable of the substructure. Such graphs essentially represent the skeletal topological framework of a network. The most universally applied instantiation of this concept is the spanning tree, denoted as T. A spanning tree is formally defined as a connected, acyclic spanning subgraph of G. The generation and optimization of spanning trees are critical to determining connectivity utilizing minimum structural size, a process algorithmically realized through foundational graph traversals such as breadth-first search or depth-first search, thereby ensuring universal vertex reachability whilst rigorously precluding redundant cyclic trails.

Furthermore, analytical investigations into network reliability and structural robustness heavily necessitate the examination of edge-deleted subgraphs. For any given edge [![][image19]](https://www.codecogs.com/eqnedit.php?latex=e%20%5Cin%20E\(G\)#2), the edge-deleted subgraph, universally denoted as [![][image20]](https://www.codecogs.com/eqnedit.php?latex=G%20-%20e#2), is uniquely defined as the spanning subgraph resulting from the specific excision of e, leaving the vertex set wholly invariant while the new edge set becomes [![][image21]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)%20%5Csetminus%20%5C%7Be%5C%7D#2). The systematic evaluation of edge-deleted subgraphs allows theorists to quantify network vulnerability and efficiency decay. Crucially, if the structural removal of a single edge e strictly increases the total number of connected components within the graph—expressed mathematically as [![][image22]](https://www.codecogs.com/eqnedit.php?latex=%5Comega\(G%20-%20e\)%20%3E%20%5Comega\(G\)#2), where [![][image23]](https://www.codecogs.com/eqnedit.php?latex=%5Comega#2) denotes the component cardinality—that specific edge is formally classified as a cut edge. The identification of cut edges serves as a primary metric for determining the connectivity constraints and critical failure points within a given theoretical network

---

Computational Implementation via NetworkX  
While graph algorithms can be implemented manually using adjacency lists or matrices, the NetworkX library in Python provides optimized, high-level functions that utilize specialized data structures for performance.

Logic of nx.subgraph(G, nodes)  
The most direct way to generate an Induced Subgraph is through this function.Theoretical Mechanism: Instead of creating a brand-new adjacency structure, NetworkX creates a SubGraph View. This is a read-only representation that points back to the original graph.Efficiency: This is an O(V' \+ E') operation where V' and E' are the sizes of the subgraph. It avoids the O(V^2) cost associated with scanning a full adjacency matrix.

Logic of nx.bfs\_edges(G, source) and nx.SpanningTree  
To generate a Spanning Subgraph, computational tools often rely on tree-generation functions.BFS-based Spanning: Using nx.bfs\_edges(G, source) returns edges in the order they are discovered. This creates a spanning subgraph that minimizes the distance (number of hops) from the source node to all other nodes.

Optimization: If the edges have "weights" (e.g., distance or cost), nx.minimum\_spanning\_tree(G) uses Kruskal’s or Prim’s Algorithm to find the spanning subgraph with the least total weight, a common requirement in infrastructure planning.

Logic of nx.edge\_subgraph(edges) vs G.remove\_edges\_from()  
For Edge-Deleted Subgraphs, there are two primary computational approaches:

Destructive (Modify original): G.remove\_edges\_from(\[(u, v), ...\]) directly alters the existing adjacency dictionaries. This is efficient for memory but permanent.

Constructive (Create view): nx.edge\_subgraph(edges) allows the user to specify which edges to *keep*. To perform edge deletion here, the user would pass the set-difference of all edges and the edges to be deleted: E setminus E\_{deleted}.

 **Code :**  
\# subgraph.py  
import matplotlib.pyplot as plt   
import networkx as nx  
from collections import deque  
def create\_graph(G):  
    G.add\_nodes\_from(range(12))   
    G.add\_edges\_from(\[(0,1), (1,2), (2,3), (3,0),  
                  (0,5), (1,6), (2,7), (3,4),  
                  (5,11), (6,11), (8,10), (9,10), (10,11),  
                  (5,7), (7,8), (8,9), (9,4), (4,6)\])  
    pos \= {  
        0: (-2, 2),      
        1: (2, 2),       
        2: (2, \-2),      
        3: (-2, \-2),          
        4: (-1.5, \-0.5),   
        5: (-1, 1),        
        6: (1, 1),         
        7: (1.5, \-0.5),    
        8: (0.5, \-1.5),    
        9: (-0.5, \-1.5),     
        10: (0, \-1),       
        11: (0, 0\)         
    }  
    fig, (ax1, ax2, ax3) \= plt.subplots(1, 3, figsize=(18, 6))  
    plt.figure(figsize=(6, 6))  
    nx.draw(G,   
            pos,   
            with\_labels=True,   
            node\_color='black',  
            font\_color='white',  
            edge\_color='red')  
      
    plt.title("Graph Layout")  
    induced\_nodes \= \[0, 1, 5, 6, 11\]  
    create\_induced\_subgraph(G, induced\_nodes, ax1, pos)  
    create\_spanning\_subgraph(G, ax2, pos)  
    edges\_to\_delete \= \[(0,1), (1,2), (2,3), (3,0)\]  
    create\_edge\_deleted\_subgraph(G, edges\_to\_delete, ax3, pos)  
def get\_adj(G):  
    ver \= list(G.nodes())  
    edges \= list(G.edges())  
    adj \= \[\[\] for \_ in ver\]  
    for e1, e2 in edges:  
        adj\[e1\].append(e2)  
        adj\[e2\].append(e1)  
    return adj  
def create\_induced\_subgraph(G, nodes\_to\_keep, ax, pos):  
    subgraph \= nx.Graph()  
    subgraph.add\_nodes\_from(nodes\_to\_keep)  
    adj \= get\_adj(G)  
    for node in nodes\_to\_keep:  
        subgraph.add\_edges\_from((node, nb) for nb in adj\[node\] if nb in nodes\_to\_keep)  
    nx.draw(subgraph,  
            pos,  
            ax=ax,  
            with\_labels=True,  
            node\_color='red',   
            font\_color='white',  
            edge\_color='black')  
    ax.set\_title("Induced Subgraph")  
def create\_spanning\_subgraph(G, ax, pos):  
    subgraph \= nx.Graph()  
    ver \= list(G.nodes())  
    subgraph.add\_nodes\_from(ver)  
    adj \= get\_adj(G)  
    visited \= \[0\] \* len(ver)  
    for root in ver:   
        if (visited\[root\] \!= 0):  
            continue  
        visited\[root\] \= 1  
        q \= deque(\[root\])  
        while q:  
            cur \= q.popleft()  
              
            for node in adj\[cur\]:  
                if visited\[node\] \== 1:  
                    continue  
                subgraph.add\_edge(cur, node)  
                q.append(node)  
                visited\[node\] \= 1  
    nx.draw(subgraph,   
            pos,   
            ax=ax,   
            with\_labels=True,   
            node\_color='blue',   
            edge\_color='black')  
    ax.set\_title("Spanning Subgraph")  
def create\_edge\_deleted\_subgraph(G, edges\_to\_remove, ax, pos):  
    subgraph \= G.copy()  
    subgraph.remove\_edges\_from(edges\_to\_remove)  
    nx.draw(subgraph,  
            pos,  
            ax=ax,  
            with\_labels=True,  
            node\_color='green',   
            edge\_color='black')  
    ax.set\_title(f"Edge Deleted Subgraph")  
def main():  
    G \= nx.Graph()  
    create\_graph(G);  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

\#iso\_in.py  
import matplotlib.pyplot as plt   
import networkx as nx  
def create\_graph(G):  
    G.add\_nodes\_from(range(12))   
    G.add\_edges\_from(\[(0,1), (1,2), (2,3), (3,0),  
                  (0,5), (1,6), (2,7), (3,4),  
                  (5,11), (6,11), (8,10), (9,10), (10,11),  
                  (5,7), (7,8), (8,9), (9,4), (4,6)\])  
    pos \= {  
        0: (-2, 2),      
        1: (2, 2),       
        2: (2, \-2),      
        3: (-2, \-2),     
        4: (-1.5, \-0.5),   
        5: (-1, 1),        
        6: (1, 1),         
        7: (1.5, \-0.5),    
        8: (0.5, \-1.5),    
        9: (-0.5, \-1.5),  
        10: (0, \-1),       
        11: (0, 0\)         
    }  
    plt.figure(figsize=(6, 6))  
    nx.draw(G,   
            pos,   
            with\_labels=True,   
            node\_color='black',  
            font\_color='white',  
            edge\_color='red')  
    plt.title("Graph Layout")  
    fig, (ax1, ax2, ax3) \= plt.subplots(1, 3, figsize=(18, 6))  
    induced\_nodes \= \[0, 1, 5, 6, 11\]  
    create\_induced\_subgraph(G, induced\_nodes, ax1, pos)  
    create\_spanning\_subgraph(G, ax2, pos)  
    edges\_to\_delete \= \[(0,1), (1,2), (2,3), (3,0)\]  
    create\_edge\_deleted\_subgraph(G, edges\_to\_delete, ax3, pos)  
def create\_induced\_subgraph(G, nodes\_to\_keep, ax, pos):  
    subgraph \= G.subgraph(nodes\_to\_keep)  
    nx.draw(subgraph,  
            pos,  
            ax=ax,  
            with\_labels=True,  
            node\_color='red',   
            font\_color='white',  
            edge\_color='black')  
    ax.set\_title("Induced Subgraph")  
def create\_spanning\_subgraph(G, ax, pos):  
    subgraph \= nx.Graph()  
    subgraph.add\_nodes\_from(G.nodes())  
        for component in nx.connected\_components(G):  
        root \= list(component)\[0\]  
        tree \= nx.bfs\_tree(G, root).to\_undirected()  
        subgraph.add\_edges\_from(tree.edges())  
    nx.draw(subgraph,   
            pos,   
            ax=ax,   
            with\_labels=True,   
            node\_color='blue',   
            edge\_color='black')  
    ax.set\_title("Spanning Subgraph (BFS Forest)")  
def create\_edge\_deleted\_subgraph(G, edges\_to\_remove, ax, pos):  
    subgraph \= G.copy()  
    subgraph.remove\_edges\_from(edges\_to\_remove)  
    nx.draw(subgraph,  
            pos,  
            ax=ax,  
            with\_labels=True,  
            node\_color='green',   
            edge\_color='black')  
    ax.set\_title("Edge Deleted Subgraph")  
def main():  
    G \= nx.Graph()  
    create\_graph(G)  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:**

**Conclusion:**

### A program generating various subgraphs such induced subgraphs, spanning subgraphs and edge deleted subgraphs was successfully implemented

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAPBAMAAABZ6/G2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAu+/dzasQIolURJkyZnZtUmbLAAAAF0lEQVR4XmP8z4ALMKELIMCoFDKguhQAq8sBHRbJ61MAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGsAAAARBAMAAAAoKE+YAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAHklEQVR4XmP8z0AG+MiELkIcGNWGAUa1YYBRbRgAACHiAhJqYJLbAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGsAAAARBAMAAAAoKE+YAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAHklEQVR4XmP8z0AG+MiELkIcGNWGAUa1YYBRbRgAACHiAhJqYJLbAAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAARBAMAAAB9SazGAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAGUlEQVR4XmP8z0AQfGRCF8EGRhWNKiJSEQDMQwISm0IW8wAAAABJRU5ErkJggg==>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARBAMAAABdpfM7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAF0lEQVR4XmP8z4AJmNAFQGBUEA0QLwgAe8UBIZ8Qt8oAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAARBAMAAABndUxIAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq83d73ZEZpm7EDJZAI1hAAAAHElEQVR4XmP8z0AE+MiELoIdjCpDA6PK0ACRygAOtAISZ8BdmwAAAABJRU5ErkJggg==>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAARBAMAAABOcrPPAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAEklEQVR4XmP8z4AKmND4I10AADNBASE5o7/MAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAAARBAMAAADQyLRvAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAHElEQVR4XmP8z0AaYEIXIARGNRADRjUQAwahBgB3fwEhAiXjQAAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQQAAAARBAMAAADJSs+lAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAALklEQVR4Xu3OoREAMAjAwNL9d4aLZQBA5GVUIt+238M8F+ACXIALcAEuwAUcWChGawEhoMcYqAAAAABJRU5ErkJggg==>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAARBAMAAABOcrPPAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAEklEQVR4XmP8z4AKmND4I10AADNBASE5o7/MAAAAAElFTkSuQmCC>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAPBAMAAAAWtvJmAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAq+/dzbsQImZUdomZRDJRcMDgAAAAEklEQVR4XmP8zwADTHDWYGMCAK2sAR2ZwXt6AAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAAPBAMAAABZ6/G2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAu+/dzasQIolURJkyZnZtUmbLAAAAF0lEQVR4XmP8z4ALMKELIMCoFDKguhQAq8sBHRbJ61MAAAAASUVORK5CYII=>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGkAAAARBAMAAAAs3Z+lAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAHklEQVR4XmP8z0A6+MiELkIUGNWFDEZ1IYNRXcgAAACxAhLUoXclAAAAAElFTkSuQmCC>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGsAAAARBAMAAAAoKE+YAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAHklEQVR4XmP8z0AG+MiELkIcGNWGAUa1YYBRbRgAACHiAhJqYJLbAAAAAElFTkSuQmCC>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAARBAMAAACWfhfFAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAGElEQVR4XmP8z0AIMKELYIJRJdjBiFQCAHmiASHVHlL7AAAAAElFTkSuQmCC>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACkAAAAMBAMAAAANL4lAAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAFUlEQVR4XmP8z4AJPjKhi4DBcBYFAPgzAggUxIO0AAAAAElFTkSuQmCC>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFMAAAARBAMAAABTDI1UAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGUlEQVR4XmP8z0Ak+MiELoIbjCodVTrgSgGTeAISoVGdQQAAAABJRU5ErkJggg==>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIEAAAARBAMAAAAI6NIgAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEGZ2VKuZiTLdzUS7Iu9dShvpAAAAIUlEQVR4XmP8z0AZ+MiELkIyGDUBAkZNgIBREyBgeJgAAI8MAhJldYqNAAAAAElFTkSuQmCC>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAIBAMAAADdFhi7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEGZ2VKuZiTLdzUS7Iu9dShvpAAAAFElEQVR4XmP8zwAEH5lAJAMD8RQAZ9MCAJwEF1cAAAAASUVORK5CYII=>