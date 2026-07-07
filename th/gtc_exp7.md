#### **Experiment No**: 7	 **Date**: 09/04/2026

# 

### **Aim :** To implement shortest path algorithm in order to compute the shortest path from the source vertex to all the other vertices in a weighted graph 

**Theory:** Let [![][image1]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2) denote a connected, undirected simple graph. To mathematically model real-world constraints such as physical distance, transit time, or economic cost, one defines a weighted graph by introducing a real-valued weight function [![][image2]](https://www.codecogs.com/eqnedit.php?latex=w%3A%20E%20%5Crightarrow%20%5Cmathbb%7BR%7D%5E%2B#2), which assigns a strictly non-negative scalar quantity [![][image3]](https://www.codecogs.com/eqnedit.php?latex=w\(e\)#2) to each edge [![][image4]](https://www.codecogs.com/eqnedit.php?latex=e%20%5Cin%20E\(G\)#2). For any arbitrary path P traversing G, the total aggregate weight of the path, denoted as [![][image5]](https://www.codecogs.com/eqnedit.php?latex=w\(P\)#2), is defined as the summation of the individual weights of its constituent edges, expressed algebraically as [![][image6]](https://www.codecogs.com/eqnedit.php?latex=w\(P\)%20%3D%20%5Csum_%7Be%20%5Cin%20E\(P\)%7D%20w\(e\)#2). The fundamental shortest path problem seeks to definitively identify an optimal path [![][image7]](https://www.codecogs.com/eqnedit.php?latex=P%5E*#2) between a designated source vertex [![][image8]](https://www.codecogs.com/eqnedit.php?latex=u_0#2) and an arbitrary destination vertex v, such that the structural weight [![][image9]](https://www.codecogs.com/eqnedit.php?latex=w\(P%5E*\)#2) is strictly minimized over the set of all possible paths connecting [![][image10]](https://www.codecogs.com/eqnedit.php?latex=u_0#2) and v. This minimized scalar value mathematically defines the distance function [![][image11]](https://www.codecogs.com/eqnedit.php?latex=d\(u_0%2C%20v\)#2) between the respective vertices.  
To systematically resolve the problem of determining the shortest paths from a singular source vertex [![][image12]](https://www.codecogs.com/eqnedit.php?latex=u_0#2) to all other vertices [![][image13]](https://www.codecogs.com/eqnedit.php?latex=v%20%5Cin%20V\(G\)#2), theorists rely upon the optimal greedy paradigm formulated by E. W. Dijkstra. This algorithmic procedure operates by iteratively constructing a spanning arborescence—a connected, acyclic tree structure—of shortest paths radiating from the source node. The operational methodology relies on maintaining a strict partition of the vertex set [![][image14]](https://www.codecogs.com/eqnedit.php?latex=V\(G\)#2) into two mutually exclusive subsets at each stage i: a confirmed set [![][image15]](https://www.codecogs.com/eqnedit.php?latex=S_i#2), encompassing those vertices for which the absolute minimum distance from [![][image16]](https://www.codecogs.com/eqnedit.php?latex=u_0#2) has been mathematically proven and permanently established, and its structural complement [![][image17]](https://www.codecogs.com/eqnedit.php?latex=%5Cbar%7BS%7D_i%20%3D%20V%20%5Csetminus%20S_i#2), representing the remaining vertices possessing only a tentative upper-bound distance estimate. Throughout the procedure, each vertex v carries a tentative distance label [![][image18]](https://www.codecogs.com/eqnedit.php?latex=l\(v\)#2), which serves as a strict upper bound on the true shortest distance.

The quintessential procedural realization of this methodology, adhering explicitly to the formal algorithm provided in the primary text, is executed through the following iterative sequence:

**Step 1\.** Set [![][image19]](https://www.codecogs.com/eqnedit.php?latex=l\(u_0\)%20%3D%200#2), [![][image20]](https://www.codecogs.com/eqnedit.php?latex=l\(v\)%20%3D%20%5Cinfty#2) for [![][image21]](https://www.codecogs.com/eqnedit.php?latex=v%20%5Cneq%20u_0#2), [![][image22]](https://www.codecogs.com/eqnedit.php?latex=S_0%20%3D%20%5C%7Bu_0%5C%7D#2) and [![][image23]](https://www.codecogs.com/eqnedit.php?latex=i%20%3D%200#2).

**Step 2\.** For each [![][image24]](https://www.codecogs.com/eqnedit.php?latex=v%20%5Cin%20%5Cbar%7BS%7D_i#2), replace [![][image25]](https://www.codecogs.com/eqnedit.php?latex=l\(v\)#2) by [![][image26]](https://www.codecogs.com/eqnedit.php?latex=%5Cmin%5C%7Bl\(v\)%2C%20l\(u_i\)%20%2B%20w\(u_iv\)%5C%7D#2). Compute [![][image27]](https://www.codecogs.com/eqnedit.php?latex=%5Cmin_%7Bv%20%5Cin%20%5Cbar%7BS%7D_i%7D%20%5C%7Bl\(v\)%5C%7D#2) and let [![][image28]](https://www.codecogs.com/eqnedit.php?latex=u_%7Bi%2B1%7D#2) denote a vertex for which this minimum is attained.

Set [![][image29]](https://www.codecogs.com/eqnedit.php?latex=S_%7Bi%2B1%7D%20%3D%20S_i%20%5Ccup%20%5C%7Bu_%7Bi%2B1%7D%5C%7D#2).

**Step 3\.** If [![][image30]](https://www.codecogs.com/eqnedit.php?latex=i%20%3D%20%5Cnu%20-%201#2), stop. If [![][image31]](https://www.codecogs.com/eqnedit.php?latex=i%20%3C%20%5Cnu%20-%201#2), replace i by [![][image32]](https://www.codecogs.com/eqnedit.php?latex=i%20%2B%201#2) and go to step 2\.

When the algorithm terminates, the absolute distance from the source [![][image33]](https://www.codecogs.com/eqnedit.php?latex=u_0#2) to any reachable vertex v is definitively given by the final established value of the label [![][image34]](https://www.codecogs.com/eqnedit.php?latex=l\(v\)#2), thereby definitively establishing the optimal routing tree for all geometrically reachable vertices within the network.

It is absolutely imperative to establish that a rigorous mathematical prerequisite for the topological validity of Dijkstra's algorithm is the strict non-negativity of the weight function w. The inductive proof securing the algorithm's global optimality inherently relies upon the monotonic, non-decreasing nature of accumulating path weights. Should negative edge weights be structurally permitted within [![][image35]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)#2), the foundational greedy assumption—that the absolute minimum tentative label in [![][image36]](https://www.codecogs.com/eqnedit.php?latex=%5Cbar%7BS%7D_i#2) constitutes a permanently finalized shortest distance—would be catastrophically violated, as subsequent path extensions could theoretically diminish the total aggregate weight below the presumed minimum, thereby necessitating alternative and computationally heavier dynamic programming paradigms to resolve the network.

---

NetworkX Functions Used  
The function nx.single\_source\_dijkstra(G, source) in the NetworkX library computes both the shortest path lengths and the paths themselves from a specified {source} node to all other reachable nodes in a weighted graph G. By implementing Dijkstra's algorithm with a binary heap-based priority queue, it achieves a computational complexity of [![][image37]](https://www.codecogs.com/eqnedit.php?latex=%5Cmathcal%7BO%7D\(\(E%20%2B%20V\)%20%5Clog%20V\)#2), provided that all edge weights [![][image38]](https://www.codecogs.com/eqnedit.php?latex=w\(e\)%20%5Cgeq%200#2). The function returns a tuple [![][image39]](https://www.codecogs.com/eqnedit.php?latex=\(%5Cmathcal%7BD%7D%2C%20%5Cmathcal%7BP%7D\)#2), where [![][image40]](https://www.codecogs.com/eqnedit.php?latex=%5Cmathcal%7BD%7D#2) is a dictionary mapping each target node t to its minimum cumulative distance [![][image41]](https://www.codecogs.com/eqnedit.php?latex=d\(s%2C%20t\)#2) and [![][image42]](https://www.codecogs.com/eqnedit.php?latex=%5Cmathcal%7BP%7D#2) is a dictionary mapping each target node to the list of nodes [![][image43]](https://www.codecogs.com/eqnedit.php?latex=%5Bs%2C%20%5Cdots%2C%20t%5D#2) comprising the optimal traversal sequence.

**Code :**  
\# shortpath\_in.py (with NetworkX functions)  
import matplotlib.pyplot as plt  
import networkx as nx  
def main():  
    G \= nx.Graph()  
    edges \= \[  
        (1, 2, 6), (1, 3, 7), (2, 3, 8), (2, 4, 9), (2, 6, 14),  
        (3, 4, 5), (3, 5, 4), (4, 5, 6), (4, 6, 10), (5, 7, 7),  
        (6, 7, 11), (6, 8, 8), (7, 8, 6\)  
    \]  
    G.add\_weighted\_edges\_from(edges)  
    pos \= {1: (0, 0), 2: (1, 1), 3: (1, \-1), 4: (2, 0),   
           5: (2, \-2), 6: (3, 1), 7: (3, \-1), 8: (4, 0)}  
    source \= 1  
    print(f"Dijkstra's Algorithm using NetworkX (Source: {source})")  
    print("-" \* 40\)  
    lengths, paths \= nx.single\_source\_dijkstra(G, source=source)  
    print(f"{'Node':\<10} {'Distance':\<10} {'Shortest Path'}")  
    for node in sorted(lengths):  
        print(f"{node:\<10} {lengths\[node\]:\<10} {paths\[node\]}")  
    plt.figure(figsize=(10, 6))  
    nx.draw\_networkx\_nodes(G, pos, node\_color='white', edgecolors='black', node\_size=600)  
    nx.draw\_networkx\_labels(G, pos)  
    nx.draw\_networkx\_edges(G, pos, alpha=0.3, style='dashed')      
    path\_edges \= \[\]  
    for node in paths:  
        path \= paths\[node\]  
        for i in range(len(path) \- 1):  
            path\_edges.append((path\[i\], path\[i+1\]))       
    nx.draw\_networkx\_edges(G, pos, edgelist=path\_edges, edge\_color='blue', width=2)  
    labels \= nx.get\_edge\_attributes(G, 'weight')  
    nx.draw\_networkx\_edge\_labels(G, pos, edge\_labels=labels)  
      
    plt.title(f"Shortest Path Tree (Inbuilt) from Source {source}")  
    plt.axis('off')  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:** 

\# shortpath\_mn.py (without NetworkX functions)  
import matplotlib.pyplot as plt  
import networkx as nx  
def create\_graph():  
    G \= nx.Graph()  
    edges \= \[  
        (1, 2, 6), (1, 3, 7), (2, 3, 8), (2, 4, 9), (2, 6, 14),  
        (3, 4, 5), (3, 5, 4), (4, 5, 6), (4, 6, 10), (5, 7, 7),  
        (6, 7, 11), (6, 8, 8), (7, 8, 6\)  
    \]  
    G.add\_weighted\_edges\_from(edges)  
    pos \= {1: (0, 0), 2: (1, 1), 3: (1, \-1), 4: (2, 0),   
           5: (2, \-2), 6: (3, 1), 7: (3, \-1), 8: (4, 0)}  
    return G, pos  
def dijkstra(G, start):  
    dist \= {n: float('inf') for n in G.nodes()}  
    dist\[start\] \= 0  
    pred \= {n: None for n in G.nodes()}  
    unvisited \= list(G.nodes())  
    visited \= \[\]  
    steps \= \[{'sel': '-', 'dist': dist.copy(), 'visited': \[\]}\]  
    while unvisited:  
        curr \= min(unvisited, key=lambda n: dist\[n\])  
        if dist\[curr\] \== float('inf'): break  
        unvisited.remove(curr)  
        visited.append(curr)  
          
        for nbr in G.neighbors(curr):  
            if nbr in unvisited:  
                alt \= dist\[curr\] \+ G\[curr\]\[nbr\]\['weight'\]  
                if alt \< dist\[nbr\]:  
                    dist\[nbr\] \= alt  
                    pred\[nbr\] \= curr  
        steps.append({'sel': curr, 'dist': dist.copy(), 'visited': list(visited)})  
    return dist, pred, steps  
def print\_table(nodes, steps):  
    nodes \= sorted(list(nodes))  
    header \= f"{'S':\<20} " \+ " ".join(f"{str(n):\<4}" for n in nodes) \+ "  u"  
    print(header)  
    for s in steps:  
        v\_set \= "{" \+ ",".join(map(str, sorted(s\['visited'\]))) \+ "}"  
        dists \= \[f"{str(s\['dist'\]\[n\]) if s\['dist'\]\[n\] \!= float('inf') else '∞':\<4}" for n in nodes\]  
        print(f"{v\_set:\<20} " \+ " ".join(dists) \+ f"  {s\['sel'\]}")  
def visualize(G, pos, pred, start):  
    plt.figure(figsize=(10, 6))  
    nx.draw\_networkx\_nodes(G, pos, node\_color='white', edgecolors='black', node\_size=600)  
    nx.draw\_networkx\_labels(G, pos)  
    nx.draw\_networkx\_edges(G, pos, alpha=0.3, style='dashed')     
    path\_edges \= \[(p, n) for n, p in pred.items() if p is not None\]  
    nx.draw\_networkx\_edges(G, pos, edgelist=path\_edges, edge\_color='red', width=2)  
    labels \= nx.get\_edge\_attributes(G, 'weight')  
    nx.draw\_networkx\_edge\_labels(G, pos, edge\_labels=labels)    
    plt.title(f"Shortest Path Graph from Source {start}")  
    plt.axis('off')  
    plt.show()  
def main():  
    G, pos \= create\_graph()  
    source \= 1  
    dist, pred, steps \= dijkstra(G, source)  
    print(f"Dijkstra's Algorithm (Source: {source})")  
    print\_table(G.nodes(), steps)  
      
    print("\\nShortest Distances:")  
    for n in sorted(dist):  
        print(f"{n}: {dist\[n\]}")    
    visualize(G, pos, pred, source)  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:**

**Conclusion:**  
A program implementing shortest path algorithm in order to compute the shortest path from the source vertex to all the other vertices in a weighted graph  was successfully implemented

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFsAAAAPBAMAAAB5B65LAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAHUlEQVR4XmP8z0AC+MiELoIfjCrHBUaV4wIkKgcAVf4CDmDSF5AAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAARBAMAAABOcrPPAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAEklEQVR4XmP8z4AKmND4I10AADNBASE5o7/MAAAAAElFTkSuQmCC>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAARBAMAAACWfhfFAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAGElEQVR4XmP8z0AIMKELYIJRJdjBiFQCAHmiASHVHlL7AAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAARBAMAAACoW3iLAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAFklEQVR4XmP8z4AOPjKhiwDBqBjxYgCX5AIS5S5w5wAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJAAAAAbBAMAAABhHxuQAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAALElEQVR4XmP8z0AdwIQuQC4YNYgwGDWIMBg1iDAYNYgwGDWIMBg1iDCgmkEAgloBNcz3/UoAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAMBAMAAAB2C0uMAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAid3vzburmXZEVBBmMiJm6649AAAAFElEQVR4XmP8zwABH5mgDAYGerAA5SACCJf6BGkAAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAALBAMAAABSacpvAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAFElEQVR4XmP8zwAGH5kgNAMD1RkAu+0CBiZoofUAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAARBAMAAABUTlNBAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAF0lEQVR4XmP8z4ANMKELQMCoMCagijAAoAcBIVwRQAIAAAAASUVORK5CYII=>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAALBAMAAABSacpvAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAFElEQVR4XmP8zwAGH5kgNAMD1RkAu+0CBiZoofUAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAARBAMAAACP9fljAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAGUlEQVR4XmP8z4ALfGRCF0ECo3LYwWCSAwChewISezwUnwAAAABJRU5ErkJggg==>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAALBAMAAABSacpvAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAFElEQVR4XmP8zwAGH5kgNAMD1RkAu+0CBiZoofUAAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAARBAMAAAB9SazGAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAGUlEQVR4XmP8z0AQfGRCF8EGRhWNKiJSEQDMQwISm0IW8wAAAABJRU5ErkJggg==>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPBAMAAADNDVhEAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq83d73ZEZpm7EDJZAI1hAAAAFElEQVR4XmP8zwACH5nAFAMDvWgA6GoCDhySdwQAAAAASUVORK5CYII=>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAALBAMAAABSacpvAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAFElEQVR4XmP8zwAGH5kgNAMD1RkAu+0CBiZoofUAAAAASUVORK5CYII=>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFQAAAAUBAMAAADhHQeeAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARFTd7yKJq812Zpm7EDJbs3WNAAAAGElEQVR4XmP8z0AsYEIXwA1GlY4qHVUKAJ5eASdVOrLzAAAAAElFTkSuQmCC>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAARBAMAAADalBo9AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECJEVHaJq7vd782ZMma2ofpDAAAAFUlEQVR4XmP8z4AAH5mQOAwMw48HANCvAhI5WM/SAAAAAElFTkSuQmCC>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEMAAAARBAMAAAB0ogy8AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECJEVHaJq7vd782ZMma2ofpDAAAAGUlEQVR4XmP8z0AAfGRCF8EEo0qwgxGpBACJ4QISTjBwAwAAAABJRU5ErkJggg==>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAARBAMAAACWfhfFAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECJEVHaJq7vd782ZMma2ofpDAAAAGElEQVR4XmP8z0AIMKELYIJRJdjBiFQCAHmiASHVHlL7AAAAAElFTkSuQmCC>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAQCAMAAABncAyDAAADAFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALI7fhAAAAEnRSTlMAEFSr3e/NiTJmRLuZInbR+cl2WyLoAAAAlElEQVR4Xq2Q0QqDMAxFo3YwHTLM/39jX33YQNs0ae1VEdkOtMm9QZOU6ARG49/cbTCikWnRSDzQqAjtuR5hq1jU0yzHPgZvWmMMUrAwfJKyIjVF7zaOUizHZYel1JH8OX89NY5ekmt/rcptVkzyAFModiYMeCKdqE9JS/4NQ/NmP6UPZ0bzGu2AwBP9xHj0twOrYgX2vBBKsSLZDAAAAABJRU5ErkJggg==>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEkAAAARBAMAAABjgJx1AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq83d73ZEZpm7EDJZAI1hAAAAHElEQVR4XmP8z0AYfGRCF8EKRlXBwKgqGCBOFQDtdAISwC2qFwAAAABJRU5ErkJggg==>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAMBAMAAAD40QLwAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAid3NZkSrVBDvuzKZdiJR1kIBAAAAEklEQVR4XmP8z4AOmNAFhroQAO2xARfGlft3AAAAAElFTkSuQmCC>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAARBAMAAABUTlNBAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAF0lEQVR4XmP8z4ANMKELQMCoMCagijAAoAcBIVwRQAIAAAAASUVORK5CYII=>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAARBAMAAADalBo9AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECJEVHaJq7vd782ZMma2ofpDAAAAFUlEQVR4XmP8z4AAH5mQOAwMw48HANCvAhI5WM/SAAAAAElFTkSuQmCC>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALwAAAARBAMAAACV5duoAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIjJEZnaJmbvN3RDvq1TL0YZVAAAAJklEQVR4XmP8z0BLwIQuQF0wajweMGo8HjBqPB4wajweMGo8HgAAuZoBIdcXbvMAAAAASUVORK5CYII=>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEkAAAAcBAMAAADfHo+rAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIjJEZnaJmbvN3RDvq1TL0YZVAAAAIElEQVR4XmP8z0AYfGRCF8EKRlXBwKgqGBhVBQNDWxUAYqwCKMb1VXUAAAAASUVORK5CYII=>

[image28]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAMBAMAAACD9cA8AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAEklEQVR4XmP8z4AMmFB4g5QLALtxARcM/TCoAAAAAElFTkSuQmCC>

[image29]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIkAAAARBAMAAAAbP5LUAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq83d73ZEZpm7EDJZAI1hAAAAIklEQVR4XmP8z0A5+MiELkIWGDUFOxg1BTsYNQU7GH6mAAAT3wISPdCViwAAAABJRU5ErkJggg==>

[image30]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAAMBAMAAAApNgaAAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAid3NZkSrVBDvuzKZdiJR1kIBAAAAGElEQVR4XmP8z0AIMKELYIJRJdgBdZQAALbAARcipRovAAAAAElFTkSuQmCC>

[image31]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAAMBAMAAAApNgaAAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAid3NZkSrVBDvuzKZdiJR1kIBAAAAGElEQVR4XmP8z0AIMKELYIJRJdgBdZQAALbAARcipRovAAAAAElFTkSuQmCC>

[image32]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACMAAAAMBAMAAAAaDRmJAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAid3NZkSrVBDvuzKZdiJR1kIBAAAAFUlEQVR4XmP8z4AGPjKhizAwDG0hALNyAgj712MsAAAAAElFTkSuQmCC>

[image33]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA8AAAALBAMAAABSacpvAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJEmXa7ImZ1g+4bAAAAFElEQVR4XmP8zwAGH5kgNAMD1RkAu+0CBiZoofUAAAAASUVORK5CYII=>

[image34]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAARBAMAAADalBo9AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECJEVHaJq7vd782ZMma2ofpDAAAAFUlEQVR4XmP8z4AAH5mQOAwMw48HANCvAhI5WM/SAAAAAElFTkSuQmCC>

[image35]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image36]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAARBAMAAAD00TuvAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMARFTd7yKJq812Zpm7EDJbs3WNAAAAFElEQVR4XmP8zwACH5nAFAPDQNEACYkCEo8+PXwAAAAASUVORK5CYII=>

[image37]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIQAAAARBAMAAADuwRlkAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAVLvvImaZ3YkQRDKrzXZh6hUrAAAAIElEQVR4XmP8z0ApYEIXIB2MGoEAo0YgwKgRCDBsjAAAveABIcyr9kYAAAAASUVORK5CYII=>

[image38]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEEAAAARBAMAAABwV9yBAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAGUlEQVR4XmP8z4AffGRCF8EAoypQwchSAQBosAISO1QX3gAAAABJRU5ErkJggg==>

[image39]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC0AAAARBAMAAAC7jDh/AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIrvvMmZ2mc3dEESriVRKaaqQAAAAGElEQVR4XmP8z4ANfGRCF4GCUXEIoLU4ABy3AhIkJSMRAAAAAElFTkSuQmCC>

[image40]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMBAMAAACkW0HUAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEERUdomZq7vN3e8yImbKO59XAAAAEUlEQVR4XmP8zwACTGCSShQAVvEBF2ROGQoAAAAASUVORK5CYII=>

[image41]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAARBAMAAAC2kkg4AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAGElEQVR4XmP8z4AFfGRCF4GAUWFMQBVhAPt3AhJOYoCQAAAAAElFTkSuQmCC>

[image42]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAMBAMAAACkW0HUAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAMmaJmau7zd3vEFREdiI0CF8jAAAAEUlEQVR4XmP8zwACTGCSShQAVvEBF2ROGQoAAAAASUVORK5CYII=>

[image43]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADwAAAARBAMAAABz4NKpAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAq1TviSLdRHaZzTJmuxByi3LMAAAAGElEQVR4XmP8z4APMKELoIJRaaxg6EoDADEeASFPfq+6AAAAAElFTkSuQmCC>