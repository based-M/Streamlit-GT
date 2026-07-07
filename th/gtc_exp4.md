#### **Experiment No**: 4	 **Date**: 05/02/2026

# 

**Aim :** To check if the given degree sequence is graphical or not graphical using Handshaking Lemma and Havel-Hakimi Theorem.  

**Theory:** A finite sequence of non-negative integers [![][image1]](https://www.codecogs.com/eqnedit.php?latex=D%20%3D%20\(d_1%2C%20d_2%2C%20%5Cdots%2C%20d_%5Cnu\)#2) is defined as the degree sequence of a simple graph [![][image2]](https://www.codecogs.com/eqnedit.php?latex=G%20%3D%20\(V%2C%20E\)#2) if there exists a bijective mapping from the elements of D to the vertex set V such that each [![][image3]](https://www.codecogs.com/eqnedit.php?latex=d_i#2) represents the exact degree of its corresponding vertex. The core theoretical inquiry, termed graphicality, asks: given an arbitrary sequence D, does there exist a simple, unweighted, undirected graph devoid of loops and multiple edges that realizes this sequence? If such a graph can be constructed, the sequence D is formally classified as graphical.  
Prior to the deployment of recursive algorithms, any candidate sequence must satisfy foundational necessary conditions. The most fundamental constraint is derived from the handshaking lemma, which dictates that the sum of all vertex degrees must strictly equal twice the cardinality of the edge set, . ![][image4]Consequently, any sequence exhibiting an odd sum inherently implies an impossible fractional edge and is immediately classified as non-graphic. Furthermore, structural topology dictates a strict upper bound; in any simple graph of order [![][image5]](https://www.codecogs.com/eqnedit.php?latex=%5Cnu#2), the maximum possible degree of a single vertex is bounded by [![][image6]](https://www.codecogs.com/eqnedit.php?latex=%5Cnu%20-%201#2). Therefore, if any term [![][image7]](https://www.codecogs.com/eqnedit.php?latex=d_i%20%5Cge%20%5Cnu#2), the sequence fails the maximum degree constraint.

While analytical models exist, such as the Erdős-Gallai condition which establishes a non-recursive inequality bounding the degrees of the k highest-degree vertices against the remaining capacity of the graph, graphicality is most frequently verified via constructive computation.

The algorithmic procedure, formally known as the Havel-Hakimi algorithm, provides a deterministic, recursive method for this verification. This algorithm operates on a combinatorial reduction strategy utilizing a greedy heuristic. Let the sequence be sorted into non-increasing order: [![][image8]](https://www.codecogs.com/eqnedit.php?latex=D%20%3D%20\(d_1%2C%20d_2%2C%20%5Cdots%2C%20d_%5Cnu\)#2) where [![][image9]](https://www.codecogs.com/eqnedit.php?latex=d_1%20%5Cge%20d_2%20%5Cge%20%5Cdots%20%5Cge%20d_%5Cnu#2). The Havel-Hakimi theorem states that the sequence D is graphic if and only if the reduced sequence [![][image10]](https://www.codecogs.com/eqnedit.php?latex=D'%20%3D%20\(d_2%20-%201%2C%20d_3%20-%201%2C%20%5Cdots%2C%20d_%7Bd_1%2B1%7D%20-%201%2C%20d_%7Bd_1%2B2%7D%2C%20%5Cdots%2C%20d_%5Cnu\)#2) is graphic.

Procedurally, the Havel-Haikimi algorithm executes the following steps:

* Sort: Ensure the current sequence is ordered such that terms are non-increasing.  
* Base Case Evaluation: If all elements are precisely zero, the sequence is graphical, representing a completely disconnected null graph.  
* Reduction: Excise the leading maximum term [![][image11]](https://www.codecogs.com/eqnedit.php?latex=d_1#2) from the sequence.  
* Decrement: Strictly subtract 1 from the subsequent [![][image12]](https://www.codecogs.com/eqnedit.php?latex=d_1#2) terms in the remaining sequence. This mathematical operation simulates the structural connection of the highest-degree vertex to the [![][image13]](https://www.codecogs.com/eqnedit.php?latex=d_1#2) vertices currently requiring the highest number of adjacent edges.  
* Validation: If the decrement operation drives any term to a negative integer (i.e., [![][image14]](https://www.codecogs.com/eqnedit.php?latex=d_i%20%3C%200#2)), an impossible localized adjacency requirement has been generated. The algorithm immediately terminates, and the initial sequence is proven non-graphic. Otherwise, the reduced sequence is re-sorted, and the procedure loops back to Step 2\.

This iterative elimination fundamentally ensures that higher degree demands are satisfied first, preventing the structural exhaustion of available degree capacity on lower-demand vertices, thereby efficiently resolving the question of graphicality.

---

## NetworkX Functions used

While manual implementations involve sorting and list manipulation, the NetworkX library encapsulates these mathematical properties into optimized functions that handle large sequences efficiently.

nx.is\_graphical(sequence): This is the high-level validator. Under the hood, NetworkX does not just run Havel-Hakimi; it often uses the Erdős–Gallai criteria for faster verification on large datasets.

Performance: It is highly optimized for O(n) or O(n log n) performance, whereas a naive manual recursion might struggle with deep call stacks on very long sequences.

nx.havel\_hakimi\_graph(sequence): If the goal is not just to *know* if it's graphical, but to *see* the graph, this function is used.  
Construction Logic: It implements the algorithm literally. It picks the node with the highest degree and creates edges to the nodes with the next highest degrees.Refinement: Unlike a manual implementation that just tracks integers, this function returns a nx.Graph object, complete with an adjacency list representation that can be used for further analysis or visualization.

### Nx.degree\_sequence\_similarity: In real-world data science, we often deal with noisy data where a sequence *should* be graphical but isn't due to missing edges. This function helps determine how "close" a sequence is to being a valid graph.

**Code :**  
\#graphical\_mn.py  
import matplotlib.pyplot as plt   
import networkx as nx   
def iteration(G, deg\_map):  
    it \= iter(deg\_map)  
    first \= next(it)  
    if deg\_map\[first\] \>= len(deg\_map):  
        deg\_map\[first\] \= \-1  
        return deg\_map  
    for \_ in range(deg\_map\[first\]):  
        key \= next(it)  
        deg\_map\[key\] \-= 1  
        if deg\_map\[key\] \< 0:  
            return deg\_map  
        G.add\_edge(first, key)  
    del deg\_map\[first\]  
    return deg\_map  
def is\_graphical(deg\_map):  
    ver \= len(deg\_map)  
    G \= nx.Graph()  
    G.add\_nodes\_from(range(0,ver))  
    sum\_deg \= 0  
    for deg in deg\_map.values():  
        if deg \>= ver:  
            return False  
        sum\_deg \+= deg;  
    if (sum\_deg % 2 \!= 0):  
        return False  
    sort\_deg \= dict(sorted(deg\_map.items(), key=lambda item: item\[1\], reverse=True))  
    iteration\_count \= 1  
    for \_ in range(0, ver):  
        if not sort\_deg or all(v \== 0 for v in sort\_deg.values()):   
            break    
        deg\_map \= iteration(G, sort\_deg)  
        print(f"Iteration {iteration\_count}: {deg\_map}")  
        for deg in deg\_map.values():  
            if deg \< 0:  
                return False  
        plt.figure(figsize \= (6,4))  
        plt.title(f"After Iteration {iteration\_count}")  
        nx.draw(G, with\_labels=True, node\_color='lightblue')  
        iteration\_count \+= 1  
        sort\_deg \= dict(sorted(deg\_map.items(), key=lambda item: item\[1\], reverse=True))  
    return True  
def main():  
    deg\_seq \= \[int(n) for n in input("Enter the Degree Sequence: ").split(',')\]  
    deg\_seq.sort(reverse=True)  
    deg\_map \= {}  
    for i in range(0, len(deg\_seq)):  
        deg\_map\[i\] \= deg\_seq\[i\]  
    result \= is\_graphical(deg\_map)  
    if result:  
        print("The degree sequence is Graphical")  
    else:  
        print("The degree sequence is Non-Graphical")  
    plt.show()  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

\# graphical\_in.py  
import matplotlib.pyplot as plt   
import networkx as nx   
def visualize\_havel\_hakimi(deg\_seq):  
    if not nx.is\_graphical(deg\_seq):  
        print("The degree sequence is Non-Graphical")  
        return False  
    print("The degree sequence is Graphical")  
    n \= len(deg\_seq)  
    sequence \= \[\[d, i\] for i, d in enumerate(deg\_seq)\]  
    G \= nx.Graph()  
    G.add\_nodes\_from(range(n))  
    iteration\_count \= 1  
    while True:  
        sequence.sort(key=lambda x: x\[0\], reverse=True)  
        if not sequence or sequence\[0\]\[0\] \== 0:  
            break     
        d, u \= sequence.pop(0)  
        for i in range(d):  
            sequence\[i\]\[0\] \-= 1  
            v \= sequence\[i\]\[1\]  
            G.add\_edge(u, v)        
        current\_deg\_map \= {item\[1\]: item\[0\] for item in sequence}  
        print(f"Iteration {iteration\_count}: {current\_deg\_map}")  
        plt.figure(figsize=(6, 4))  
        plt.title(f"After Iteration {iteration\_count}: Node {u} connected")  
        nx.draw(G,   
                with\_labels=True,   
                node\_color='lightblue',   
                edge\_color='gray',   
                node\_size=500,   
                font\_weight='bold')  
        iteration\_count \+= 1  
    return True  
def main():  
    try:  
        user\_input \= input("Enter the Degree Sequence (comma separated): ")  
        deg\_seq \= \[int(n.strip()) for n in user\_input.split(',')\]  
        deg\_seq.sort(reverse=True)  
        if visualize\_havel\_hakimi(deg\_seq):  
            plt.show()  
    except ValueError:  
        print("Invalid input. Please enter a sequence of integers.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  
if \_\_name\_\_ \== "\_\_main\_\_":  
    main()

**Output:**

**Conclusion:**  
A program to  check if the given degree sequence is graphical or not graphical using Handshaking Lemma and Havel-Hakimi Theorem was successfully implemented 

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJEAAAARBAMAAAAvRlPIAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAid3vzatmMkS7dhBUmSL1zwcfAAAAIklEQVR4XmP8z0Ad8JEJXYRsMGoScWDUJOLAqEnEgeFtEgCYowISf2fcJwAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFEAAAARBAMAAABX+V1pAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAIlSJq7vN3e+ZZjIQdkTYCWZ8AAAAHUlEQVR4XmP8z0Ac+MiELoITjKokBoyqJAYQrxIAckcCEjQe32YAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAPBAMAAAAizzN6AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAEUlEQVR4XmP8zwACTGCSlhQAbigBHV8/R9QAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADoAAAAdBAMAAAAJPGKVAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAEDJEZnaJq7vN71TdIpmhbdoxAAAAHElEQVR4XmP8z4AHMKELoIBRWWQwKosMRmWRAQDHvAE5PdnYqgAAAABJRU5ErkJggg==>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIBAMAAAA2IaO4AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECJEVGaJmbvN3e92qzLq0JJAAAAAEUlEQVR4XmP8z8DAwMRAkAAAKEEBDwZAssoAAAAASUVORK5CYII=>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAAMBAMAAAAXE2nOAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECJEVGaJmbvN3e92qzLq0JJAAAAAFUlEQVR4XmP8z4AOPjKhiwDBcBEDAMpdAghiVY48AAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAC8AAAAPBAMAAACGpYupAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAGElEQVR4XmP8z4AVfGRCF4GBUQkMQLoEANaHAg79gbJ2AAAAAElFTkSuQmCC>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJEAAAARBAMAAAAvRlPIAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAid3vzatmMkS7dhBUmSL1zwcfAAAAIklEQVR4XmP8z0Ad8JEJXYRsMGoScWDUJOLAqEnEgeFtEgCYowISf2fcJwAAAABJRU5ErkJggg==>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIwAAAAPBAMAAADEyjp7AAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAIElEQVR4XmP8z0ANwIQuQB4YNQY3GDUGNxg1BjegkjEAZqQBHQ7wmFoAAAAASUVORK5CYII=>

[image10]: <data:image/png;base64,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>

[image11]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPBAMAAADNDVhEAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAFElEQVR4XmP8zwACH5nAFAMDvWgA6GoCDhySdwQAAAAASUVORK5CYII=>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPBAMAAADNDVhEAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAFElEQVR4XmP8zwACH5nAFAMDvWgA6GoCDhySdwQAAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA0AAAAPBAMAAADNDVhEAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAFElEQVR4XmP8zwACH5nAFAMDvWgA6GoCDhySdwQAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAPBAMAAABtkjCqAAAAMFBMVEX///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv3aB7AAAAD3RSTlMAECIyVHaJq7vN70SZ3WY3t8peAAAAF0lEQVR4XmP8z4ANMKELQMCoMCbAIQwAbEcBHdmAAAIAAAAASUVORK5CYII=>