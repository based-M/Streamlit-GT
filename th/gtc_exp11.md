#### **Experiment No**: 11	**Date**:14/05/26

# 

### **Aim :** To implement greedy graph coloring algorithm that assigns colors to the vertices such as that no two adjacent vertices share the same color with the minimal chromatic number

**Theory:** Let [![][image1]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2) denote a finite, loopless graph of order [![][image2]](https://www.codecogs.com/eqnedit.php?latex=%5Cnu#2). A strictly proper vertex colouring of G is formally defined as an assignment of colours to the vertices of G, mathematically expressed as a surjective mapping [![][image3]](https://www.codecogs.com/eqnedit.php?latex=c%3A%20V\(G\)%20%5Crightarrow%20S#2) where S is a finite set of distinct colours, subject to the inviolable condition that adjacent vertices must receive distinct colours. Thus, for any edge [![][image4]](https://www.codecogs.com/eqnedit.php?latex=uv%20%5Cin%20E\(G\)#2), the inequality [![][image5]](https://www.codecogs.com/eqnedit.php?latex=c\(u\)%20%5Cneq%20c\(v\)#2) must hold. When [![][image6]](https://www.codecogs.com/eqnedit.php?latex=%7CS%7C%20%3D%20k#2), the mapping constitutes a k-colouring, and the graph G is defined as k-colourable. Topologically, a proper k-colouring partitions the vertex set [![][image7]](https://www.codecogs.com/eqnedit.php?latex=V\(G\)#2) into k disjoint independent sets, frequently termed colour classes, wherein no two vertices within the same class share an incident edge. The primary theoretical objective in this domain is to calculate the chromatic number of the graph, canonically denoted as [![][image8]](https://www.codecogs.com/eqnedit.php?latex=%5Cchi\(G\)#2), which represents the absolute minimum integer k for which G admits a proper k-colouring.Because the exact computational resolution of the chromatic number [![][image9]](https://www.codecogs.com/eqnedit.php?latex=%5Cchi\(G\)#2) is notoriously intractable for arbitrary, large-scale networks, researchers heavily rely upon the greedy colouring algorithm to deterministically establish valid structural upper bounds. This algorithmic procedure operates through a rigorous, locally optimized sequential paradigm. The protocol initiates by imposing an arbitrary but strict total ordering upon the complete vertex set, generating the deterministic sequence [![][image10]](https://www.codecogs.com/eqnedit.php?latex=\(v_1%2C%20v_2%2C%20%5Cdots%2C%20v_%5Cnu\)#2). The available colours are systematically represented by the well-ordered set of positive integers [![][image11]](https://www.codecogs.com/eqnedit.php?latex=%5Cmathbb%7BZ%7D%5E%2B%20%3D%20%5C%7B1%2C%202%2C%203%2C%20%5Cdots%5C%7D#2).The core execution of the algorithm proceeds iteratively across the established vertex sequence. In the foundational base step, the initial vertex [![][image12]](https://www.codecogs.com/eqnedit.php?latex=v_1#2) is trivially assigned the minimal integer colour, [![][image13]](https://www.codecogs.com/eqnedit.php?latex=c\(v_1\)%20%3D%201#2). For every subsequent vertex [![][image14]](https://www.codecogs.com/eqnedit.php?latex=v_i#2) where [![][image15]](https://www.codecogs.com/eqnedit.php?latex=2%20%5Cle%20i%20%5Cle%20%5Cnu#2), the algorithm conducts a precise structural evaluation of [![][image16]](https://www.codecogs.com/eqnedit.php?latex=v_i#2)'s localized neighborhood, restricted exclusively to its predecessors in the generated sequence. Let [![][image17]](https://www.codecogs.com/eqnedit.php?latex=N\(v_i\)#2) denote the open neighborhood of [![][image18]](https://www.codecogs.com/eqnedit.php?latex=v_i#2) within G. The algorithm calculates the active adjacency subset, defined algebraically as [![][image19]](https://www.codecogs.com/eqnedit.php?latex=N%5E-\(v_i\)%20%3D%20%5C%7Bv_j%20%5Cin%20N\(v_i\)%20%5Cmid%20j%20%3C%20i%5C%7D#2). The greedy assignment function then mandates that the vertex [![][image20]](https://www.codecogs.com/eqnedit.php?latex=v_i#2) accepts the strictly smallest positive integer that does not currently reside within the set of colours already distributed among its active predecessors. Mathematically, this minimal colour assignment is formalized as [![][image21]](https://www.codecogs.com/eqnedit.php?latex=c\(v_i\)%20%3D%20%5Cmin%20%5C%7B%20k%20%5Cin%20%5Cmathbb%7BZ%7D%5E%2B%20%5Cmid%20k%20%5Cnotin%20%5C%7Bc\(v_j\)%20%5Cmid%20v_j%20%5Cin%20N%5E-\(v_i\)%5C%7D%20%5C%7D#2). By continuously minimizing the integer value at each local step, the heuristic successfully enforces the proper colouring condition while strictly suppressing the arbitrary introduction of new colours.A paramount theoretical consequence of this sequential heuristic is the definitive establishment of a universal upper bound on the chromatic number relative to the maximum vertex degree of the graph, denoted as [![][image22]](https://www.codecogs.com/eqnedit.php?latex=%5CDelta\(G\)#2). For any arbitrary vertex [![][image23]](https://www.codecogs.com/eqnedit.php?latex=v_i%20%5Cin%20V\(G\)#2), the total cardinality of its open neighborhood is intrinsically bounded by the maximum degree, [![][image24]](https://www.codecogs.com/eqnedit.php?latex=%7CN\(v_i\)%7C%20%5Cle%20%5CDelta\(G\)#2). Consequently, the cardinality of its predecessor subset can never exceed this limit, meaning [![][image25]](https://www.codecogs.com/eqnedit.php?latex=%7CN%5E-\(v_i\)%7C%20%5Cle%20%5CDelta\(G\)#2). When the greedy algorithm attempts to colour [![][image26]](https://www.codecogs.com/eqnedit.php?latex=v_i#2), it is confronted by a maximum of [![][image27]](https://www.codecogs.com/eqnedit.php?latex=%5CDelta\(G\)#2) forbidden colours. By the strict application of the pigeonhole principle, at least one integer within the bounded interval [![][image28]](https://www.codecogs.com/eqnedit.php?latex=%5B1%2C%20%5CDelta\(G\)%20%2B%201%5D#2) must remain entirely unassigned among the predecessors. The algorithm will deterministically select this available integer, proving that it will never require a colour indexed higher than [![][image29]](https://www.codecogs.com/eqnedit.php?latex=%5CDelta\(G\)%20%2B%201#2). This mathematically guarantees the fundamental universal inequality [![][image30]](https://www.codecogs.com/eqnedit.php?latex=%5Cchi\(G\)%20%5Cle%20%5CDelta\(G\)%20%2B%201#2).Furthermore, graph theory rigorously dictates that the operational efficiency of the greedy algorithm is profoundly sensitive to the initial vertex ordering. A structurally adversarial ordering can force the heuristic to utilize a quantity of colours substantially greater than the true minimal value [![][image31]](https://www.codecogs.com/eqnedit.php?latex=%5Cchi\(G\)#2). Conversely, mathematical proofs guarantee that there exists at least one optimal vertex ordering for any graph G such that the greedy algorithm will converge perfectly upon exactly [![][image32]](https://www.codecogs.com/eqnedit.php?latex=%5Cchi\(G\)#2) colours. Finally, it must be noted that while the bound [![][image33]](https://www.codecogs.com/eqnedit.php?latex=%5CDelta\(G\)%20%2B%201#2) is universally applicable, theorists utilize advanced vertex sequence modifications to prove tighter constraints, most notably Brooks' Theorem. This theorem rigorously asserts that, with the singular exceptions of complete graphs and odd-length cycles, the chromatic number is strictly bounded by the maximum degree itself, yielding [![][image34]](https://www.codecogs.com/eqnedit.php?latex=%5Cchi\(G\)%20%5Cle%20%5CDelta\(G\)#2), a condition which can similarly be computationally realized through a highly specialized implementation of the greedy paradigm.

**Code :**  
\# color\_in.py (with NetworkX functions)  
import matplotlib.pyplot as plt   
import networkx as nx   
def create\_graph():  
    G \= nx.Graph()  
    nodes \= range(0,8)  
    node \= len(nodes)  
    G.add\_nodes\_from(nodes)  
    edges \= \[(i, (i+1)%node) for i in nodes\]  
    edges.extend(\[(i, (i+2)%node) for i in nodes\])  
    edges.extend(\[(i, (i+4)%node) for i in nodes\])  
    G.add\_edges\_from(edges)  
    pos \= {0: (-0.5,1), 1:(0.5,1), 2:(1, 0.5), 3:(1, \-0.5), 4:(0.5, \-1), 5:(-0.5,-1), 6:(-1, \-0.5), 7:(-1, 0.5)}  
    return G, pos  
def color(G):  
    colors \= \["red", "blue", "green", "yellow", "orange"\]  
    def my\_str(G , colors):  
        return list(range(0,8))  
    color\_scheme \= nx.greedy\_color(G,strategy=my\_str)  
    node\_colors \= \[colors\[color\_scheme\[node\]\] for node in G.nodes()\]  
    return node\_colors  
def main():  
    G, pos \= create\_graph()  
    node\_colors \= color(G)  
    fig, ax \= plt.subplots(1, 2, figsize=(12, 6))  
    fig.suptitle("Graph Coloring", fontsize=16)  
    ax\[0\].set\_title("Original Graph")  
    nx.draw(G, pos=pos, ax=ax\[0\], with\_labels=True, node\_color='lightblue',   
            node\_size=800, font\_size=12, font\_weight='bold', edge\_color='gray')  
    ax\[1\].set\_title("Colored Graph")  
    nx.draw(G, pos=pos, ax=ax\[1\], node\_color=node\_colors, with\_labels=True,   
            node\_size=800, font\_size=12, font\_weight='bold', edge\_color='gray')  
      
    plt.tight\_layout(rect=\[0, 0.03, 1, 0.95\])  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

// color\_mn.py (without networkx functions)  
import matplotlib.pyplot as plt   
import networkx as nx   
def create\_graph():  
    G \= nx.Graph()  
    nodes \= range(0,8)  
    node \= len(nodes)  
    G.add\_nodes\_from(nodes)  
    edges \= \[(i, (i+1)%node) for i in nodes\]  
    edges.extend(\[(i, (i+2)%node) for i in nodes\])  
    edges.extend(\[(i, (i+4)%node) for i in nodes\])  
    G.add\_edges\_from(edges)  
    pos \= {0: (-0.5,1), 1:(0.5,1), 2:(1, 0.5), 3:(1, \-0.5), 4:(0.5, \-1), 5:(-0.5,-1), 6:(-1, \-0.5), 7:(-1, 0.5)}  
    return G, pos  
def get\_adj(G):  
    e \= list(G.edges())  
    adj \= {node: \[\] for node in G.nodes()}  
    for e1, e2 in e:  
        adj\[e1\].append(e2)  
        adj\[e2\].append(e1)  
    return adj  
def color(G, colors):  
    color\_schm \= { node: "" for node in G.nodes()}   
    adj \= get\_adj(G)  
    for node in G.nodes():  
        neighbors \= {color\_schm\[neig\] for neig in adj\[node\]}  
        for color in colors:  
            if color not in neighbors:  
                color\_schm\[node\] \= color  
                break  
    return color\_schm.values()  
def main():  
    G, pos \= create\_graph()  
    fig, ax \= plt.subplots(1, 2, figsize=(12, 6))  
    fig.suptitle("Graph Coloring", fontsize=16)  
    colors \= \["red", "blue", "green", "yellow", "orange"\]  
    color\_schm \= color(G, colors)  
    ax\[0\].set\_title("Original Graph")  
    nx.draw(G, pos=pos, ax=ax\[0\], with\_labels=True, node\_color='lightblue',   
            node\_size=800, font\_size=12, font\_weight='bold', edge\_color='gray')  
    ax\[1\].set\_title("Colored Graph")  
    nx.draw(G, pos=pos, ax=ax\[1\], with\_labels=True, node\_color=color\_schm,   
            node\_size=800, font\_size=12, font\_weight='bold', edge\_color='gray')  
    plt.tight\_layout(rect=\[0, 0.03, 1, 0.95\])  
    plt.show()  
main()

// suduko\_mn.py  
import matplotlib.pyplot as plt  
import networkx as nx  
def create\_sudoku\_graph():  
    G \= nx.Graph()  
    size \= 4    
    box\_size \= 2       
    nodes \= \[(r, c) for r in range(size) for c in range(size)\]  
    G.add\_nodes\_from(nodes)      
    row\_edges \= \[\]  
    col\_edges \= \[\]  
    box\_edges \= \[\]      
    for r1, c1 in nodes:  
        for r2, c2 in nodes:  
            if (r1, c1) \>= (r2, c2):   
                continue                       
            if r1 \== r2:  
                G.add\_edge((r1, c1), (r2, c2))  
                row\_edges.append(((r1, c1), (r2, c2)))              
            elif c1 \== c2:  
                G.add\_edge((r1, c1), (r2, c2))  
                col\_edges.append(((r1, c1), (r2, c2)))              
            elif (r1 // box\_size \== r2 // box\_size) and (c1 // box\_size \== c2 // box\_size):  
                G.add\_edge((r1, c1), (r2, c2))  
                box\_edges.append(((r1, c1), (r2, c2)))                 
    pos \= {(r, c): (c, \-r) for r, c in nodes}  
    return G, pos, row\_edges, col\_edges, box\_edges  
def is\_safe(G, node, color, color\_schm):  
    for neighbor in G.neighbors(node):  
        if color\_schm\[neighbor\] \== color:  
            return False  
    return True  
def solve(G, nodes, index, color\_schm):  
    if index \== len(nodes):  
        return True      
    node \= nodes\[index\]  
    if color\_schm\[node\] \!= 0:  
        return solve(G, nodes, index \+ 1, color\_schm)      
    for color in range(1, 5):   
        if is\_safe(G, node, color, color\_schm):  
            color\_schm\[node\] \= color  
            if solve(G, nodes, index \+ 1, color\_schm):  
                return True  
            color\_schm\[node\] \= 0  
    return False  
def main():  
    G, pos, row\_e, col\_e, box\_e \= create\_sudoku\_graph()     
    puzzle \= {  
        (0, 0): 0, (0, 1): 0, (0, 2): 0, (0, 3): 2,  
        (1, 0): 0, (1, 1): 4, (1, 2): 0, (1, 3): 0,  
        (2, 0): 1, (2, 1): 0, (2, 2): 0, (2, 3): 0,  
        (3, 0): 0, (3, 1): 0, (3, 2): 0, (3, 3): 0  
    }      
    initial\_nodes \= \[node for node, val in puzzle.items() if val \!= 0\]  
    solved\_nodes \= \[node for node, val in puzzle.items() if val \== 0\]     
    color\_schm \= puzzle.copy()  
    nodes\_list \= list(G.nodes())  
    solve(G, nodes\_list, 0, color\_schm)      
    color\_map \= {1: '\#ff9999', 2: '\#9999ff', 3: '\#99ff99', 4: '\#ffff99'}      
    plt.figure(figsize=(14, 12))  
    plt.title("4x4 Sudoku Graph", fontsize=16)          
    def draw\_curved\_edges(edges, color, is\_row):  
        for u, v in edges:  
            dist \= abs(u\[1\] \- v\[1\]) if is\_row else abs(u\[0\] \- v\[0\])              
            rad \= 0.0 if dist \== 1 else (0.2 if dist \== 2 else 0.4)   
            nx.draw\_networkx\_edges(G, pos, edgelist=\[(u, v)\],   
                                   edge\_color=color, alpha=0.4, width=2,  
                                   arrows=True, arrowstyle='-',  
                                   connectionstyle=f"arc3,rad={rad}")      
    draw\_curved\_edges(row\_e, 'blue', True)  
    draw\_curved\_edges(col\_e, 'red', False)      
    nx.draw\_networkx\_edges(G, pos, edgelist=box\_e, edge\_color='green',   
                           alpha=0.6, width=2, label='Box Arcs')    
    nx.draw\_networkx\_nodes(G, pos, nodelist=solved\_nodes,   
                           node\_color=\[color\_map\[color\_schm\[n\]\] for n in solved\_nodes\],   
                           node\_size=1200, edgecolors='gray', linewidths=1)      
    nx.draw\_networkx\_nodes(G, pos, nodelist=initial\_nodes,   
                           node\_color=\[color\_map\[color\_schm\[n\]\] for n in initial\_nodes\],   
                           node\_size=1500, edgecolors='black', linewidths=5)    
    labels \= {n: color\_schm\[n\] for n in G.nodes()}  
    nx.draw\_networkx\_labels(G, pos, labels=labels, font\_size=18, font\_weight='bold')  
    plt.axis('off')  
    print("Sudoku Solved\! Curves ensure all 7 edges per node are visible.")  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:**  
**//** coloring

**//** sudoku

**Conclusion:**  
A python program to implement greedy graph coloring algorithm that assigns colors to the vertices such as that no two adjacent vertices share the same color with the minimal chromatic number was successfully implemented

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECJEVGaJmbvN3e92qzLq0JJAAAAAEUlEQVR4XmP8z8DAwMRAkAAAKEEBDwZAssoAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGcAAAARBAMAAAAyFK8WAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJu93vzZlEdhCrMma5B41NAAAAHklEQVR4XmP8z0Ay+MiELkIMGNUEBaOaoGBUExQAAN9xAhJwAiJcAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAARBAMAAAC4OzZXAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAHElEQVR4XmP8z0AcYEIXwAVGFeIFowrxAqIVAgDmaAEhx0Zv0gAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFMAAAARCAMAAACW/GBVAAADAFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALI7fhAAAAEnRSTlMAIlSJu93vzZlEdhCrMmbR+ck8x8t6AAAA/ElEQVR4Xn2UyQ7CMAxE3QhKRSkH//83BhBwAAEiSbPYkzRPonTGS1aVSDBLwVJ0kWVYBRrDnpa3V0pntPKBIxrUKjNoCOrsCQ2HBS2r6g6VUxnU8DjMc2QR4FN+tb1FuExVlh/WP+MvJSSr/CW03CxjQ+w2ZH6JyCYfKXzZmPaSqayOaBe6PJO0IbeNioSyd1K2tCd/7tciEnxDx5M7BFpDR8/QT/uBLxoOfqCDpI0z9+bhrttzEc7QmpimZMy8Xp84yuBuyBIPMOegcEzMYTbRX/LF6lYp4yzeNbjObs9FCgwWIKKqqqj83my3xJj+ShEdpJC3uI8s8wP8AUc7H6DyxousAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADQAAAARBAMAAABgN5JdAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAELvvZjKJIqvNRFTddpnqLXbqAAAAF0lEQVR4XmP8z4ALMKELIMCoFDIYJFIA6IsBIaN4xMUAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAARBAMAAABHmRO1AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARJnN7927q2YiMnaJEFT+4nNwAAAAFElEQVR4XmP8z4AOmNAFRoXwCgEAV4MBIahw8FIAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAARBAMAAABHmRO1AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARJnN7927q2YiMnaJEFT+4nNwAAAAFElEQVR4XmP8z4AOmNAFRoXwCgEAV4MBIahw8FIAAAAASUVORK5CYII=>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGgAAAARBAMAAADDH/SbAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIrvvMmZ2mc3dEESriVRKaaqQAAAAHElEQVR4XmP8z0A6YEIXIAaMaoKCUU1QMKoJCgDAAwEh7bmIrAAAAABJRU5ErkJggg==>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIgAAAATBAMAAAC5NVjhAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEKvvuzKZiVTdRGZ2Is1tOAuaAAAAJElEQVR4XmP8z0A5YEIXIAeMGoIJRg3BBKOGYIJRQzABVQwBAH+ZASXTm09pAAAAAElFTkSuQmCC>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAALBAMAAAC5XnFsAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAEUlEQVR4XmP8zwACTGCSUgoAT1ABFRIG5iYAAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEMAAAARBAMAAAB0ogy8AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJu93vzZlEdhCrMma5B41NAAAAGUlEQVR4XmP8z0AAfGRCF8EEo0qwgxGpBACJ4QISTjBwAwAAAABJRU5ErkJggg==>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAALBAMAAAC5XnFsAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAEUlEQVR4XmP8zwACTGCSUgoAT1ABFRIG5iYAAAAASUVORK5CYII=>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAANBAMAAAAJXW4mAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARHarzd3viVQQZruZIjKQBK3CAAAAF0lEQVR4XmP8z0AQfGRCF8EGRhUNSkUAm4gCCtCEabgAAAAASUVORK5CYII=>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAALBAMAAAC5XnFsAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAEUlEQVR4XmP8zwACTGCSUgoAT1ABFRIG5iYAAAAASUVORK5CYII=>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARBAMAAABdpfM7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAq++7EDLdzYkimVRmdkTnG+BQAAAAF0lEQVR4XmP8z4AJmNAFQGBUEA0QLwgAe8UBIZ8Qt8oAAAAASUVORK5CYII=>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAALBAMAAAC5XnFsAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAEUlEQVR4XmP8zwACTGCSUgoAT1ABFRIG5iYAAAAASUVORK5CYII=>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAAARBAMAAADZD9ZQAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAq++7EDLdzYkimVRmdkTnG+BQAAAAKElEQVR4XmP8z0Bf8JEJXYTmYNRGWoBRG2kBRm2kBRi1kRZg1EZaAADIlgISCsfS5QAAAABJRU5ErkJggg==>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAALBAMAAAC5XnFsAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAEUlEQVR4XmP8zwACTGCSUgoAT1ABFRIG5iYAAAAASUVORK5CYII=>

[image21]: <data:image/png;base64,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>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARBAMAAABdpfM7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMs3vuxCJRHZm3VSrIpmuo/zQAAAAF0lEQVR4XmP8z4AJmNAFQGBUEA0QLwgAe8UBIZ8Qt8oAAAAASUVORK5CYII=>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAARBAMAAABndUxIAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAHElEQVR4XmP8z0AE+MiELoIdjCpDA6PK0ACRygAOtAISZ8BdmwAAAABJRU5ErkJggg==>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHMAAAARBAMAAAAcUY6EAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAELvvZjKJIqvNRN2ZVHaa6BOOAAAAH0lEQVR4XmP8z0Am+MiELkI8GNVKFBjVShQY1UoUAACmpgISj9WxGAAAAABJRU5ErkJggg==>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAH0AAAARBAMAAAACmL43AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAELvvZjKJIqvNRN2ZVHaa6BOOAAAAH0lEQVR4XmP8z0AJ+MiELkIiGNVPGRjVTxkY1U8ZAABMqgISFhAf1gAAAABJRU5ErkJggg==>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAALBAMAAAC5XnFsAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAEUlEQVR4XmP8zwACTGCSUgoAT1ABFRIG5iYAAAAASUVORK5CYII=>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARBAMAAABdpfM7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMs3vuxCJRHZm3VSrIpmuo/zQAAAAF0lEQVR4XmP8z4AJmNAFQGBUEA0QLwgAe8UBIZ8Qt8oAAAAASUVORK5CYII=>

[image28]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF8AAAARBAMAAABJMG3aAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAq1TviSLddmaZELtEzTKkRfVBAAAAHUlEQVR4XmP8z0AS+MiELkIIjGogBoxqIAYMQg0AWq0CEiDS/DEAAAAASUVORK5CYII=>

[image29]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAARBAMAAAB5vHz7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMs3vuxCJRHZm3VSrIpmuo/zQAAAAGUlEQVR4XmP8z0AIfGRCF8ECRtXgByNZDQCrEgISxiCBFwAAAABJRU5ErkJggg==>

[image30]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAAARBAMAAADuwRlkAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARJnN7927q2YiMnaJEFT+4nNwAAAAIElEQVR4XmP8z0ApYEIXIB2MGoEAo0YgwKgRCDBsjAAAveABIcyr9kYAAAAASUVORK5CYII=>

[image31]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAARBAMAAABHmRO1AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARJnN7927q2YiMnaJEFT+4nNwAAAAFElEQVR4XmP8z4AOmNAFRoXwCgEAV4MBIahw8FIAAAAASUVORK5CYII=>

[image32]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAARBAMAAABHmRO1AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARJnN7927q2YiMnaJEFT+4nNwAAAAFElEQVR4XmP8z4AOmNAFRoXwCgEAV4MBIahw8FIAAAAASUVORK5CYII=>

[image33]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEUAAAARBAMAAAB5vHz7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMs3vuxCJRHZm3VSrIpmuo/zQAAAAGUlEQVR4XmP8z0AIfGRCF8ECRtXgByNZDQCrEgISxiCBFwAAAABJRU5ErkJggg==>

[image34]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGUAAAARBAMAAAA24X8rAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARJnN7927q2YiMnaJEFT+4nNwAAAAHUlEQVR4XmP8z0Aq+MiELkIEGNUzqgcERvUwMAAAvkACEhCDYuwAAAAASUVORK5CYII=>