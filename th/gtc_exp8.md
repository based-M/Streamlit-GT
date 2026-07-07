#### **Experiment No**: 8	 **Date**: 30/04/2026

# 

### **Aim :** Implement generation of close walks, trail and path in a connected graph 

**Theory:** The topological structure and dynamic connectivity of a graph [![][image1]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2) are fundamentally characterized through sequential traversals. The most generalized formalization of such a topological traversal is the walk. A walk W within G is rigorously defined as a finite, non-null, alternating sequence of vertices and edges, denoted algebraically as [![][image2]](https://www.codecogs.com/eqnedit.php?latex=W%20%3D%20v_0%20e_1%20v_1%20%5Cdots%20e_k%20v_k#2), wherein for every index [![][image3]](https://www.codecogs.com/eqnedit.php?latex=1%20%5Cle%20i%20%5Cle%20k#2), the specific endpoints of the edge [![][image4]](https://www.codecogs.com/eqnedit.php?latex=e_i#2) are strictly defined as [![][image5]](https://www.codecogs.com/eqnedit.php?latex=v_%7Bi-1%7D#2) and [![][image6]](https://www.codecogs.com/eqnedit.php?latex=v_i#2). The integer k represents the exact length of the walk. Within this foundational framework, both vertices and edges may be traversed with unconstrained multiplicity. If the initial sequence vertex strictly coincides with the terminal vertex, satisfying the condition [![][image7]](https://www.codecogs.com/eqnedit.php?latex=v_0%20%3D%20v_k#2), the traversal is formally designated as a closed walk. The mathematical formalization of closed walks is intrinsically necessary for the analysis of stochastic processes distributed over networks, providing the underlying geometric architecture for Markovian state transitions and random walk paradigms wherein an entity ultimately returns to its initial spatial state.  
By systematically imposing structural constraints upon the repetition of elements within the sequence W, one mathematically derives more specialized traversal paradigms. If all constituent edges [![][image8]](https://www.codecogs.com/eqnedit.php?latex=e_1%2C%20e_2%2C%20%5Cdots%2C%20e_k#2) within the walk are strictly distinct, the sequence W is formally defined as a trail. While a trail inherently precludes edge repetition, it permissively allows for incidence upon the same vertex multiple times. This specific topological configuration underpins the foundation of Eulerian graph theory, wherein an Eulerian trail is structurally defined as a sequence that traverses the entirety of the edge set [![][image9]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)#2) exactly once. Furthermore, a trail that satisfies the closed boundary condition [![][image10]](https://www.codecogs.com/eqnedit.php?latex=v_0%20%3D%20v_k#2) is formally classified as a circuit. The analytical properties of circuits are paramount in the modeling of capacity-constrained physical systems, guaranteeing that discrete connective links—such as logistical pathways or electrical branches—remain strictly non-overlapping, irrespective of repeated vertex intersections.

The application of the strictest sequence constraints yields the fundamental concept of a path, rigorously defined as a walk wherein all vertices [![][image11]](https://www.codecogs.com/eqnedit.php?latex=v_0%2C%20v_1%2C%20%5Cdots%2C%20v_k#2) are completely distinct. Because vertex repetition is prohibited, the distinctness of all constituent edges is mathematically guaranteed. Paths operate as the central topological structures utilized in the determination of geodesic distances, which correspond to the minimum possible sequence length connecting two arbitrary vertices. When the path condition is modified such that [![][image12]](https://www.codecogs.com/eqnedit.php?latex=v_0%20%3D%20v_k#2) and the length satisfies [![][image13]](https://www.codecogs.com/eqnedit.php?latex=k%20%5Cge%203#2), with all internal vertices remaining strictly distinct, the resulting cohesive substructure is formalized as a cycle. The identification of cycles within G is theoretically linked to the algebraic formalization of a cycle space defined over the finite field [![][image14]](https://www.codecogs.com/eqnedit.php?latex=GF\(2\)#2). Any arbitrary closed trail or Eulerian subgraph can be mathematically reconstructed through the symmetric difference of a fundamental cycle basis, representing a minimal set of independent cycles requisite to span the topological cycle space of the network.

In the domain of applied computational graph theory, the theoretical extraction of these structures is realized through deterministic traversal algorithms and software architectures. The programmatic initialization of the graph establishes the foundational mathematical structure [![][image15]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2), universally implemented via dynamic adjacency lists to map the localized neighborhoods of all vertices [![][image16]](https://www.codecogs.com/eqnedit.php?latex=v%20%5Cin%20V\(G\)#2). The geometric isolation of an optimal geodesic path between two specified vertices is generally calculated through breadth-first search heuristics or Dijkstra's algorithm, depending upon the existence of an edge weight function w. In contexts requiring the purposeful closure of an arbitrary walk, these algorithms ascertain the minimal-cost return sequence to the origin vertex. Furthermore, the algorithmic isolation of cycles is predominantly executed through recursive depth-first search paradigms. By sequentially exploring the adjacency structures, the algorithm identifies topological back-edges—links directed towards an already-visited ancestor node—which inherently signals the existence of a closed path. Upon halting and returning the localized vertex sequence, a fundamental cycle is successfully verified. Advanced linear algebraic routines are subsequently invoked to systematically compute the fundamental cycle basis, computing the strict minimal independent set of cycles required to mathematically model all closed flows within the graph's overall topology.

Networkx functions used  
nx.Graph(): Initializes the foundational mathematical structure $G \= (V, E)$, allowing for the representation of undirected edges.

nx.find\_cycle(): Algorithmically traverses the graph to identify a closed path (cycle), halting and returning the first cycle encountered. This is directly analogous to finding a basic closed path where no intermediate vertices repeat.

nx.cycle\_basis(): Computes a minimal set of independent cycles that form a basis for the cycle space of the graph. Any closed trail or Eulerian circuit in the graph can be expressed as a symmetric difference of these basis cycles.

nx.shortest\_path(): Calculates the geodesic (minimum-edge) path between two specified vertices. In the context of random or arbitrary walks, this function is mathematically employed to forcefully "close" a sequence by finding the most efficient route back to the origin vertex.

G.nodes() and G.neighbors(): Core traversal properties utilized to dynamically explore the adjacency list of a given vertex, facilitating the step-by-step construction of arbitrary walks.

**Code :**  
\# walk\_in.py (with NetworkX functions)  
import matplotlib.pyplot as plt  
import networkx as nx   
def create\_graphs():  
    G1, G2 \= nx.Graph(), nx.Graph()  
    e1 \= \[(i, (i+1)%6) for i in range(6)\] \+ \[(0,2), (0,3), (1,4), (5,2)\]  
    e2 \= \[(i, (i+1)%6) for i in range(5)\] \+ \[(i,5) for i in range(1,4)\] \+ \[(4,1), (4,0), (2,0), (3,0)\]  
    G1.add\_edges\_from(e1); G2.add\_edges\_from(e2)  
    pos1 \= {0: (-1,1), 1: (1,1), 2:(2,0), 3:(1, \-1), 4:(-1, \-1), 5:(-2,0)}  
    pos2 \= {0: (0,2), 1: (1,1), 2:(1,-1), 3:(-1, \-1), 4:(-1, 1), 5:(0,0)}  
    return (G1, pos1), (G2, pos2)  
def get\_sequences(G):  
    start\_node \= sorted(list(G.nodes()))\[0\]    
    cycle\_edges \= nx.find\_cycle(G, source=start\_node, orientation='ignore')  
    path \= \[edge\[0\] for edge in cycle\_edges\] \+ \[cycle\_edges\[0\]\[0\]\]   
    cycles \= nx.cycle\_basis(G)  
    cycles.sort(key=len)  
    trail\_nodes \= cycles\[-1\] if len(cycles) \> 1 else cycles\[0\]  
    trail \= trail\_nodes \+ \[trail\_nodes\[0\]\]   
    walk \= \[start\_node\]  
    curr \= start\_node  
    for i in range(10):  
        neighbors \= sorted(list(G.neighbors(curr)))  
        curr \= neighbors\[(i \+ 1\) % len(neighbors)\]  
        walk.append(curr)  
    if walk\[-1\] \!= start\_node:  
        back\_path \= nx.shortest\_path(G, source=walk\[-1\], target=start\_node)  
        walk.extend(back\_path\[1:\])   
    return walk, trail, path  
def draw(G, pos, ax, seq, title, color):  
    nx.draw(G, pos, ax=ax, node\_color='lightgrey', edge\_color='lightgrey', with\_labels=True)  
    if seq:  
        from collections import Counter  
        edge\_list \= \[tuple(sorted((seq\[i\], seq\[i+1\]))) for i in range(len(seq)-1)\]  
        counts \= Counter(edge\_list)  
        single\_edges \= \[e for e, c in counts.items() if c \== 1\]  
        multi\_edges \= \[e for e, c in counts.items() if c \> 1\]   
        nx.draw\_networkx\_nodes(G, pos, nodelist=seq, ax=ax, node\_color=color)  
        nx.draw\_networkx\_edges(G, pos, edgelist=single\_edges, ax=ax, edge\_color=color, width=2)  
        dark\_colors \= {'red': 'darkred', 'green': 'darkgreen', 'blue': 'darkblue'}  
        dark\_color \= dark\_colors.get(color, 'black')  
        nx.draw\_networkx\_edges(G, pos, edgelist=multi\_edges, ax=ax, edge\_color=dark\_color, width=5)    
    ax.set\_title(f"{title}\\n{seq}")  
def main():  
    (G1, p1), (G2, p2) \= create\_graphs()  
    plt.figure(1)  
    ax1, ax2 \= plt.subplot(121), plt.subplot(122)  
    draw(G1, p1, ax1, None, "Original G1", "grey")  
    draw(G2, p2, ax2, None, "Original G2", "grey")  
    fig, axes \= plt.subplots(2, 3, figsize=(15, 8), num=2)  
    for i, (G, p, name) in enumerate(\[(G1, p1, "G1"), (G2, p2, "G2")\]):  
        walk, trail, path \= get\_sequences(G)  
        draw(G, p, axes\[i,0\], walk, f"{name} Walk", "red")  
        draw(G, p, axes\[i,1\], trail, f"{name} Trail", "green")  
        draw(G, p, axes\[i,2\], path, f"{name} Path", "blue")   
    plt.tight\_layout()  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

\# walk\_mn.py  
import matplotlib.pyplot as plt  
import networkx as nx   
def create\_graphs():  
    G1, G2 \= nx.Graph(), nx.Graph()  
    e1 \= \[(i, (i+1)%6) for i in range(6)\] \+ \[(0,2), (0,3), (1,4), (5,2)\]  
    e2 \= \[(i, (i+1)%6) for i in range(5)\] \+ \[(i,5) for i in range(1,4)\] \+ \[(4,1), (4,0), (2,0), (3,0)\]  
    G1.add\_edges\_from(e1); G2.add\_edges\_from(e2)  
    pos1 \= {0: (-1,1), 1: (1,1), 2:(2,0), 3:(1, \-1), 4:(-1, \-1), 5:(-2,0)}  
    pos2 \= {0: (0,2), 1: (1,1), 2:(1,-1), 3:(-1, \-1), 4:(-1, 1), 5:(0,0)}  
    return (G1, pos1), (G2, pos2)  
def find\_closed\_path(G, start, curr=None, visited=None, path=None):  
    if curr is None: curr \= start  
    if visited is None: visited \= {start}  
    if path is None: path \= \[start\]  
    if len(path) \>= 5 and G.has\_edge(curr, start):  
        return path \+ \[start\]   
    for n in sorted(list(G.neighbors(curr))):  
        if n not in visited:  
            res \= find\_closed\_path(G, start, n, visited | {n}, path \+ \[n\])  
            if res: return res      
    if len(path) \>= 3 and G.has\_edge(curr, start):  
            return path \+ \[start\]  
    return None  
def find\_closed\_trail(G, start, curr=None, visited\_edges=None, path=None):  
    if curr is None: curr \= start  
    if visited\_edges is None: visited\_edges \= set()  
    if path is None: path \= \[start\]  
    if len(path) \>= 8 and G.has\_edge(curr, start):  
        edge\_to\_start \= tuple(sorted((curr, start)))  
        if edge\_to\_start not in visited\_edges:  
            return path \+ \[start\]         
    for n in sorted(list(G.neighbors(curr))):  
        edge \= tuple(sorted((curr, n)))  
        if edge not in visited\_edges:  
            res \= find\_closed\_trail(G, start, n, visited\_edges | {edge}, path \+ \[n\])  
            if res: return res              
    if len(path) \>= 3 and G.has\_edge(curr, start):  
        edge\_to\_start \= tuple(sorted((curr, start)))  
        if edge\_to\_start not in visited\_edges:  
            return path \+ \[start\]  
    return None  
def find\_closed\_walk(G, start):  
    path \= \[start\]  
    curr \= start  
    for i in range(12):  
        neighbors \= sorted(list(G.neighbors(curr)))  
        curr \= neighbors\[(i \+ 1\) % len(neighbors)\]  
        path.append(curr)      
    for \_ in range(10):  
        if G.has\_edge(curr, start):  
            path.append(start)  
            return path  
        neighbors \= sorted(list(G.neighbors(curr)))  
        curr \= neighbors\[0\]   
        path.append(curr)    
    if path\[-1\] \!= start:  
        path.append(start)  
    return path  
def find\_sequence(G, start, type='path'):  
    if type \== 'path':  
        return find\_closed\_path(G, start)  
    if type \== 'trail':  
        return find\_closed\_trail(G, start)  
    if type \== 'walk':  
        return find\_closed\_walk(G, start)  
    return None  
def draw(G, pos, ax, seq, title, color):  
    nx.draw(G, pos, ax=ax, node\_color='lightgrey', edge\_color='lightgrey', with\_labels=True)  
    if seq:  
        from collections import Counter  
        edge\_list \= \[tuple(sorted((seq\[i\], seq\[i+1\]))) for i in range(len(seq)-1)\]  
        counts \= Counter(edge\_list)  
        single\_edges \= \[e for e, c in counts.items() if c \== 1\]  
        multi\_edges \= \[e for e, c in counts.items() if c \> 1\]   
        nx.draw\_networkx\_nodes(G, pos, nodelist=seq, ax=ax, node\_color=color)       
        nx.draw\_networkx\_edges(G, pos, edgelist=single\_edges, ax=ax, edge\_color=color, width=2)     
        dark\_colors \= {'red': 'darkred', 'green': 'darkgreen', 'blue': 'darkblue'}  
        dark\_color \= dark\_colors.get(color, 'black')  
        nx.draw\_networkx\_edges(G, pos, edgelist=multi\_edges, ax=ax, edge\_color=dark\_color, width=5)        
    ax.set\_title(f"{title}\\n{seq}")  
def main():  
    (G1, p1), (G2, p2) \= create\_graphs()      
    plt.figure(1)  
    ax1, ax2 \= plt.subplot(121), plt.subplot(122)  
    draw(G1, p1, ax1, None, "Original G1", "grey")  
    draw(G2, p2, ax2, None, "Original G2", "grey")  
    fig, axes \= plt.subplots(2, 3, figsize=(15, 8), num=2)  
    for i, (G, p, name) in enumerate(\[(G1, p1, "G1"), (G2, p2, "G2")\]):  
        start \= sorted(list(G.nodes()))\[0\]  
        draw(G, p, axes\[i,0\], find\_sequence(G, start, 'walk'), f"{name} Walk", "red")  
        draw(G, p, axes\[i,1\], find\_sequence(G, start, 'trail'), f"{name} Trail", "green")  
        draw(G, p, axes\[i,2\], find\_sequence(G, start, 'path'), f"{name} Path", "blue")  
    plt.tight\_layout()  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:**

**//** Using networkx functions  
// Without Networkx functions

**Conclusion:**  
A python program for generation of close walks, trail and path in a connected graph was successfully implemented

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJAAAAAPBAMAAAD5WFsdAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAMt3vzburZhCJIplEVHbghmtJAAAAIElEQVR4XmP8z0AdwIQuQC4YNYgwGDWIMBg1iDCgmkEAhmYBHTr11KQAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAAPBAMAAABAYB8QAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAdu9mmRC7RM1UMiKJq90p5NcAAAAAGUlEQVR4XmP8z0AIfGRCF8ECRtXgB0NRDQAWSgIOvJLaywAAAABJRU5ErkJggg==>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAALBAMAAABbgmoVAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAFElEQVR4XmP8zwAEH5lAJAMDhRQAkicCBm41e8MAAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAALBAMAAAB8LOv9AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAFUlEQVR4XmP8z4AEPjIh8xgYBgkXADlOAgZm45pWAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAALBAMAAAC5XnFsAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAEUlEQVR4XmP8zwACTGCSUgoAT1ABFRIG5iYAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAALBAMAAAAtuNieAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAFUlEQVR4XmP8z4ALfGRCF0ECI1kOAEjkAgY+6kASAAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFsAAAALBAMAAADiluxdAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAGUlEQVR4XmP8z0AC+MiELoIfjCrHBQaVcgDVzAIGP1hEuAAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAALBAMAAAAtuNieAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAFUlEQVR4XmP8z4ALfGRCF0ECI1kOAEjkAgY+6kASAAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFwAAAALBAMAAAAASvckAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAGElEQVR4XmP8z0AKYEIXwA9GleMCg0o5ABpWARX24bLFAAAAAElFTkSuQmCC>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAALBAMAAAAtuNieAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAFUlEQVR4XmP8z4ALfGRCF0ECI1kOAEjkAgY+6kASAAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAPBAMAAABkeZDQAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAECJEVHaJq7vd75nNZjIrqulnAAAAFUlEQVR4XmP8z4AJmNAFQGBUEA0AAEyFAR3SgC4SAAAAAElFTkSuQmCC>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAARBAMAAABp3DInAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAF0lEQVR4XmP8z4AdMKELwMCoBAaghwQAxEkBITi/uGwAAAAASUVORK5CYII=>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAARBAMAAAB9SazGAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAGUlEQVR4XmP8z0AQfGRCF8EGRhWNKiJSEQDMQwISm0IW8wAAAABJRU5ErkJggg==>