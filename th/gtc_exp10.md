#### **Experiment No**: 10	**Date**:07/05/26

# 

### **Aim :** To implement a method that determines if a Graph contains a Hamiltonian Circuit  i.e. a cycle that visits every vertex only once

**Theory:** Let [![][image1]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2) denote a connected simple graph characterized by a finite vertex set [![][image2]](https://www.codecogs.com/eqnedit.php?latex=V\(G\)#2) of order [![][image3]](https://www.codecogs.com/eqnedit.php?latex=%5Cnu#2) and an edge set [![][image4]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)#2). A Hamilton path is strictly defined as a spanning path—a sequence of adjacent, strictly distinct vertices that traverses every single vertex [![][image5]](https://www.codecogs.com/eqnedit.php?latex=v%20%5Cin%20V\(G\)#2) exactly once. When such a spanning path is topologically closed, meaning an edge exists between the initial and terminal vertices of the sequence, the resulting structure is formally classified as a Hamilton cycle. A graph that structurally possesses at least one Hamilton cycle is designated as a Hamiltonian graph.  
Unlike the theory of Eulerian graphs, which elegantly relies upon the localized parity of vertex degrees to dictate the existence of exhaustive edge traversals, Hamiltonian graphs are governed by the strict exhaustion of vertices. Due to this fundamental structural distinction, determining the existence of a Hamilton cycle poses a profoundly complex mathematical challenge. Graph theory currently possesses no simple, universal set of necessary and sufficient topological conditions that definitively guarantees Hamiltonianity for all arbitrary graphs. Instead, theorists must rely upon sufficient conditions derived from edge density and global connectivity. A paramount theoretical result in this domain is Dirac's Theorem, which rigorously dictates that if $G$ is a simple graph with order [![][image6]](https://www.codecogs.com/eqnedit.php?latex=%5Cnu%20%5Cge%203#2), and if the minimum degree of the graph satisfies [![][image7]](https://www.codecogs.com/eqnedit.php?latex=%5Cdelta\(G\)%20%5Cge%20%5Cnu%20%2F%202#2), then $G$ must necessarily be Hamiltonian. This theorem establishes that a sufficiently massive minimum connectivity universally forces the localized emergence of a spanning cycle.

Despite the existence of such sufficient bounding theorems, the generalized decision problem of computationally determining whether an arbitrary graph $G$ is Hamiltonian is notoriously classified as NP-complete. This rigorous classification signifies that no known deterministic algorithm is capable of definitively resolving the problem in polynomial time across all possible network topologies. Because algorithmic verification fundamentally necessitates the exhaustive enumeration of potential vertex sequences, the computational time required to mathematically evaluate all possible structural permutations inherently scales with a factorial worst-case complexity of [![][image8]](https://www.codecogs.com/eqnedit.php?latex=O\(%5Cnu!\)#2).

To systematically bypass this severe computational intractability in applied environments, graph theorists frequently reduce the discrete Hamiltonian decision problem into the continuous numerical optimization framework of the Travelling Salesman Problem (TSP). The mathematical reduction methodology is executed through the systematic construction of a proxy graph. Let the original graph be [![][image9]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2). One constructs a universally dense structural framework by generating a complete graph [![][image10]](https://www.codecogs.com/eqnedit.php?latex=K_%5Cnu#2), such that the vertex set remains strictly identical, [![][image11]](https://www.codecogs.com/eqnedit.php?latex=V\(K_%5Cnu\)%20%3D%20V\(G\)#2), guaranteeing that an edge inherently exists between every single unordered pair of distinct vertices.

Subsequently, one must map the localized constraints of $G$ onto the continuous geometry of [![][image12]](https://www.codecogs.com/eqnedit.php?latex=K_%5Cnu#2) by defining a strict, real-valued weight function [![][image13]](https://www.codecogs.com/eqnedit.php?latex=w%3A%20E\(K_%5Cnu\)%20%5Crightarrow%20%5Cmathbb%7BR%7D%5E%2B#2). For every edge [![][image14]](https://www.codecogs.com/eqnedit.php?latex=e%20%5Cin%20E\(K_%5Cnu\)#2), if the edge is a structural constituent of the original graph such that [![][image15]](https://www.codecogs.com/eqnedit.php?latex=e%20%5Cin%20E\(G\)#2), it is assigned a strictly minimal unitary weight, typically [![][image16]](https://www.codecogs.com/eqnedit.php?latex=w\(e\)%20%3D%201#2). Conversely, if the edge represents a non-existent spatial link in the original network such that [![][image17]](https://www.codecogs.com/eqnedit.php?latex=e%20%5Cnotin%20E\(G\)#2), it is assigned a mathematically massive penalty weight [![][image18]](https://www.codecogs.com/eqnedit.php?latex=w\(e\)%20%3D%20M#2), where the scalar [![][image19]](https://www.codecogs.com/eqnedit.php?latex=M%20%5Cgg%20%5Cnu#2).

Following this rigorous transformation, a TSP optimization algorithm is deployed over the fully connected proxy graph [![][image20]](https://www.codecogs.com/eqnedit.php?latex=K_%5Cnu#2) to compute the spanning cycle [![][image21]](https://www.codecogs.com/eqnedit.php?latex=C%5E*#2) that strictly minimizes the total aggregate weight [![][image22]](https://www.codecogs.com/eqnedit.php?latex=w\(C%5E*\)#2). The existence of a Hamilton cycle within the original graph $G$ is definitively extracted by observing this minimized continuous variable. If the optimal aggregate weight exactly satisfies [![][image23]](https://www.codecogs.com/eqnedit.php?latex=w\(C%5E*\)%20%3D%20%5Cnu#2), it mathematically proves that the tour was exclusively composed of unitary-weight edges native to [![][image24]](https://www.codecogs.com/eqnedit.php?latex=E\(G\)#2), thereby guaranteeing that $G$ inherently contains a valid Hamilton cycle. Conversely, if the optimal weight strictly exceeds [![][image25]](https://www.codecogs.com/eqnedit.php?latex=%5Cnu#2), it dictates that the minimization algorithm was structurally forced to traverse at least one heavily penalized non-native edge to complete the tour, definitively proving that a native Hamilton cycle is topologically impossible. In modern computational topology, while exact formulations of the TSP remain inherently prohibitive, theorists deploy advanced heuristic approximations upon this exact bipartite weight reduction to evaluate the Hamiltonian properties of exceedingly massive networks.

Networkx functions used  
In applied computational analysis, this theoretical TSP-reduction method can be mapped directly to specific functions within the NetworkX library. The operations used to execute this mathematical transformation include:

**nx.Graph()**: Initializes the fundamental mathematical structure to represent the undirected network $G$.

**G.nodes()** and **G.has\_edge()**: Used to interrogate the original graph's topology to determine which edges inherently exist and which must be computationally penalized.

**nx.complete\_graph()**: Generates the structural framework for [![][image26]](https://www.codecogs.com/eqnedit.php?latex=G'#2), a fully connected proxy graph containing all vertices from $G$, guaranteeing a theoretical TSP path exists regardless of the original graph's connectivity.

**nx.algorithms.approximation.traveling\_salesman\_problem()**: The core algorithmic engine. Because exact TSP solutions are computationally prohibitive for large graphs, this function utilizes advanced approximation heuristics (like the Christofides algorithm or greedy simulated annealing) to compute the minimum-weight tour through the complete proxy graph [![][image27]](https://www.codecogs.com/eqnedit.php?latex=G'#2).

**Code :**  
\# hamilton\_in.py (with NetworkX functions)  
import matplotlib.pyplot as plt  
import networkx as nx  
import networkx.algorithms.approximation as approx  
def create\_graphs():  
    G1 \= nx.Graph()  
    G1.add\_nodes\_from(range(0, 6))  
    e1\_edges \= \[(i, (i+1)%6) for i in range(6)\] \+ \[(0,2), (0,3), (1,4), (5,2)\]  
    G1.add\_edges\_from(e1\_edges)  
      
    G2 \= nx.Graph()  
    G2.add\_nodes\_from(range(0, 6))  
    e2\_edges \= \[(i, (i+1)%6) for i in range(5)\] \+ \[(i,5) for i in range(1,4)\] \+ \[(4,1), (4,0), (2,0), (3,0)\]  
    G2.add\_edges\_from(e2\_edges)  
    pos1 \= { 0: (-1,1), 1: (1,1), 2:(2,0), 3:(1, \-1), 4:(-1, \-1), 5:(-2,0) }  
    pos2 \= { 0: (0,2), 1: (1,1), 2:(1,-1), 3:(-1, \-1), 4:(-1, 1), 5:(0,0) }  
    return \[  
        {"name": "Graph 1", "G": G1, "pos": pos1},  
        {"name": "Graph 2", "G": G2, "pos": pos2}  
    \]  
def find\_hamiltonian\_nx(G):  
    nodes \= list(G.nodes())  
    n \= len(nodes)      
    complete\_G \= nx.complete\_graph(nodes)  
    for u, v in complete\_G.edges():  
        complete\_G\[u\]\[v\]\['weight'\] \= 1 if G.has\_edge(u, v) else 1000              
    try:  
        cycle \= approx.traveling\_salesman\_problem(complete\_G, weight='weight')         
        total\_weight \= sum(complete\_G\[cycle\[i\]\]\[cycle\[i+1\]\]\['weight'\] for i in range(len(cycle)-1))  
        if total\_weight \== n:  
            return cycle  
    except:  
        pass  
    return None  
def main():  
    graphs \= create\_graphs()  
    fig, axes \= plt.subplots(1, 2, figsize=(12, 5))      
    for i, config in enumerate(graphs):  
        G \= config\["G"\]  
        name \= config\["name"\]  
        pos \= config\["pos"\]          
        print(f"Finding Hamiltonian Cycle for {name} using NetworkX built-ins...")  
        cycle \= find\_hamiltonian\_nx(G)        
        nx.draw(G, pos, ax=axes\[i\], with\_labels=True, node\_color='lightgreen', edge\_color='gray')  
        if cycle:  
            print(f"{name}: Found {cycle}")  
            edges \= \[(cycle\[j\], cycle\[j+1\]) for j in range(len(cycle)-1)\]  
            nx.draw\_networkx\_edges(G, pos, edgelist=edges, ax=axes\[i\], edge\_color='red', width=3)  
            axes\[i\].set\_title(f"{name}: Hamiltonian Cycle\\n{cycle}")  
        else:  
            print(f"{name}: No Hamiltonian Cycle found.")  
            axes\[i\].set\_title(f"{name}: No Hamiltonian Cycle")      
    plt.tight\_layout()  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

// hamilton\_mn.py (without networkx functions)  
import matplotlib.pyplot as plt  
import networkx as nx  
def create\_graphs():  
    G1 \= nx.Graph()  
    G1.add\_nodes\_from(range(0, 6))  
    e1\_edges \= \[(i, (i+1)%6) for i in range(6)\] \+ \[(0,2), (0,3), (1,4), (5,2)\]  
    G1.add\_edges\_from(e1\_edges)      
    G2 \= nx.Graph()  
    G2.add\_nodes\_from(range(0, 6))  
    e2\_edges \= \[(i, (i+1)%6) for i in range(5)\] \+ \[(i,5) for i in range(1,4)\] \+ \[(4,1), (4,0), (2,0), (3,0)\]  
    G2.add\_edges\_from(e2\_edges)  
    pos1 \= { 0: (-1,1), 1: (1,1), 2:(2,0), 3:(1, \-1), 4:(-1, \-1), 5:(-2,0) }  
    pos2 \= { 0: (0,2), 1: (1,1), 2:(1,-1), 3:(-1, \-1), 4:(-1, 1), 5:(0,0) }  
    return \[  
        {"name": "Graph 1", "G": G1, "pos": pos1},  
        {"name": "Graph 2", "G": G2, "pos": pos2}  \]  
def find\_hamiltonian\_cycle(G):  
    nodes \= list(G.nodes())  
    n \= len(nodes)  
    if n \== 0: return None      
    start\_node \= nodes\[0\]  
    path \= \[start\_node\]      
    def backtrack(curr):  
        if len(path) \== n:  
            if G.has\_edge(path\[-1\], start\_node):  
                return path \+ \[start\_node\]  
            return None  
          
        for neighbor in G.neighbors(curr):  
            if neighbor not in path:  
                path.append(neighbor)  
                result \= backtrack(neighbor)  
                if result:  
                    return result  
                path.pop()  
        return None  
    return backtrack(start\_node)  
def draw\_cycle(G, pos, cycle, name, ax):  
    nx.draw(G, pos, ax=ax, with\_labels=True, node\_color='lightblue', edge\_color='gray', node\_size=500)  
    if cycle:  
        edges \= \[(cycle\[i\], cycle\[i+1\]) for i in range(len(cycle)-1)\]  
        nx.draw\_networkx\_edges(G, pos, edgelist=edges, ax=ax, edge\_color='red', width=3)  
        ax.set\_title(f"{name}: Hamiltonian Cycle Found\\n{cycle}")  
    else:  
        ax.set\_title(f"{name}: No Hamiltonian Cycle Found")  
def main():  
    graphs \= create\_graphs()  
    fig, axes \= plt.subplots(1, 2, figsize=(12, 6))      
    for i, config in enumerate(graphs):  
        G \= config\["G"\]  
        name \= config\["name"\]  
        pos \= config\["pos"\]          
        print(f"Finding Hamiltonian Cycle for {name}...")  
        cycle \= find\_hamiltonian\_cycle(G)        
        if cycle:  
            print(f"Found Cycle: {cycle}")  
        else:  
            print("No Hamiltonian Cycle exists.")        
        draw\_cycle(G, pos, cycle, name, axes\[i\])      
    plt.tight\_layout()  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:**

**Conclusion:**

### A python program to determine if a Graph contains a Hamiltonian Circuit  i.e. a cycle that visits every vertex only once was successfully implemented

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAECJEVGaJmbvN3e92qzLq0JJAAAAAEUlEQVR4XmP8z8DAwMRAkAAAKEEBDwZAssoAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAAARBAMAAAB9SazGAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJmRLuZInbs20X/AAAAGUlEQVR4XmP8z0AQfGRCF8EGRhWNKiJSEQDMQwISm0IW8wAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAANBAMAAAApsTHbAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAECJEVGaJmbvN3e92qzLq0JJAAAAAFElEQVR4XmP8z4AJmNAFQGCECAIAHe0BGRfx9HEAAAAASUVORK5CYII=>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFUAAAARBAMAAABeEv0TAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlSJu93Nq2aZEO9EMnZIbMhwAAAAHUlEQVR4XmP8z0As+MiELoIHjKqFgFG1EDAY1AIAtKkCEo1vKRwAAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAARBAMAAABdpfM7AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAMmaZq7vN3e+JVCJ2EEQiVSrZAAAAF0lEQVR4XmP8z4AJmNAFQGBUEA0QLwgAe8UBIZ8Qt8oAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAPBAMAAAAWtvJmAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAq+/dzbsQImZUdomZRDJRcMDgAAAAEklEQVR4XmP8zwADTHDWYGMCAK2sAR2ZwXt6AAAAAElFTkSuQmCC>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHAAAAARBAMAAAD3ZjWHAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIs3v3burVGZ2mUQQMon2aNJoAAAAHUlEQVR4XmP8z0AeYEIXIBaMasQDRjXiAaMa8QAACJYBIZtHi+EAAAAASUVORK5CYII=>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAPBAMAAAAWtvJmAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAq+/dzbsQImZUdomZRDJRcMDgAAAAEklEQVR4XmP8zwADTHDWYGMCAK2sAR2ZwXt6AAAAAElFTkSuQmCC>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAAATBAMAAACq4hgVAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAIElEQVR4XmP8z0AZYEIXIBWMGjBqAAiMGjBqAAhQbAAALfUBJU34vKoAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAE0AAAARBAMAAABqazwPAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAHUlEQVR4XmP8z0AM+MiELoIDjKrDDkbVYQfEqgMAL+UCElGCT9wAAAAASUVORK5CYII=>

[image15]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAARBAMAAACWfhfFAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARHaZzd3vuzIiiRBmq1TOzJOoAAAAGElEQVR4XmP8z0AIMKELYIJRJdjBiFQCAHmiASHVHlL7AAAAAElFTkSuQmCC>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAAARBAMAAACflbe/AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAGElEQVR4XmP8z4AfMKELoINRBRAwQhQAAFVgASEkxToXAAAAAElFTkSuQmCC>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEQAAAARCAMAAABTjvrEAAADAFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAywWXiAAAAEnRSTlMARHaZzd3vuzIiiRBmq1Reg+lPzhCoAAAA+UlEQVR4Xp2S2w7CMAiG2TJ1m9EsvP8zNiZq4iEeVgq00MYLv8QBPy2lWIAW6AVl8EJc2nmRGG/qHjbiBdVW8PKAzZM8o2d0H8FtkRE/2S2HfTKWgxcEPhW5qwdHVZFY3DZeBkRnFySQuyOff5kySj66k3GA8VXUbU0p9zZy9p2TRA/zOuO9hHRLU2gPIYgw07e+34BR1G0y71xnp56DVvI6Wzfe1o2EX1Ielk5QrZvRsvbmxvJJJqp39Sz9OX713QaEY04W0KlXPps70mQH02Rqx/dcROKkJfLnIZyWoE+vbq2efUEz2RAbUsHv7P806jYkgz5LIW74Ak7JLbYCcU9YAAAAAElFTkSuQmCC>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEwAAAARBAMAAACFqVcxAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAG0lEQVR4XmP8z0AMYEIXwA5GlaGBUWVogEhlAMImASH9hHm0AAAAAElFTkSuQmCC>

[image19]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADcAAAAMBAMAAAA0SDgbAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMARM27Imbvmat2EDLdiVRWT+/bAAAAF0lEQVR4XmP8z4ATfGRCF0EGo5IMBCQBmK8CCMMvBdwAAAAASUVORK5CYII=>

[image20]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAPBAMAAAAWtvJmAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAq+/dzbsQImZUdomZRDJRcMDgAAAAEklEQVR4XmP8zwADTHDWYGMCAK2sAR2ZwXt6AAAAAElFTkSuQmCC>

[image21]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAMBAMAAAB2C0uMAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAIlR2q7vN3e+JEESZMmZ6kRRHAAAAFElEQVR4XmP8zwABH5mgDAYGerAA5SACCJf6BGkAAAAASUVORK5CYII=>

[image22]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAARBAMAAABUTlNBAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAF0lEQVR4XmP8z4ANMKELQMCoMCagijAAoAcBIVwRQAIAAAAASUVORK5CYII=>

[image23]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAAARBAMAAAC4OzZXAAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAEFSr3e/NiTJ2IkSZu2aaTuJPAAAAHElEQVR4XmP8z0AcYEIXwAVGFeIFowrxAqIVAgDmaAEhx0Zv0gAAAABJRU5ErkJggg==>

[image24]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAARBAMAAACsrqi2AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAVJmrZrt2RBCJze/dIjJISVHlAAAAGElEQVR4XmP8z4ABPjKhi4DAqCAaIF4QALkVAhLGFC39AAAAAElFTkSuQmCC>

[image25]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAMFBMVEX///8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx9fPp3uAAAAD3RSTlMAECJEVGaJmbvN3e92qzLq0JJAAAAAEUlEQVR4XmP8z8DAwMRAkAAAKEEBDwZAssoAAAAASUVORK5CYII=>

[image26]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAANBAMAAABSlfMXAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAEUlEQVR4XmP8zwABTFCaHgwAefIBGSXIxQgAAAAASUVORK5CYII=>

[image27]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAANBAMAAABSlfMXAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAEUlEQVR4XmP8zwABTFCaHgwAefIBGSXIxQgAAAAASUVORK5CYII=>