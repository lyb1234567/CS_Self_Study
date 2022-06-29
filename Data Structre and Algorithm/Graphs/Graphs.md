# Graphs
This section explains some basic concepts of Graphs first, then it will give the implementations of them

## Table of contents
- [Graphs](#graphs)
- [BFS](#bfs)
- [DFS](#dfs)
- [Leetcode](#leetcode)
  

## Graphs
A graph is a set of nodes that are connected to each other in the form of a network. First of all, we’ll define the two basic components of a graph.

**Vertex**
A vertex is the most essential part of a graph. A collection of vertices forms a graph. In that sense, vertices are similar to linked list nodes.

**Edge**
An edge is the link between two vertices. It can be uni-directional or bi-directional depending on your graph. An edge can also have a cost associated with it (will be discussed in detail later).
![grpahs](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Graphs/image/Graph.PNG?raw=true)

**Graph Terminologies**
1. Degree of a Vertex: The total number of edges incident on a vertex. There are two types of degrees:
   - **In-Degree**: The total number of incoming edges of a vertex.
   - **Out-Degree**: The total number of outgoing edges of a vertex.
2. **Parallel Edges**: Two undirected edges are parallel if they have the same end vertices. Two directed edges are parallel if they have the same starting and ending vertices.
3. **Self Loop**: This occurs when an edge starts and ends on the same vertex.
4. **Adjacency**: Two vertices are said to be adjacent if there is an edge connecting them directly.


**Types of Graphs**
1. Undirected Graph
In an undirected graph, the edges are bi-directional. For e.g., an ordered pair **(2, 3)** shows that there exists an edge between vertex 2 and 3 without any specific direction. You can go from vertex **2 to 3** or from **3 to 2.**

Let’s calculate the maximum number of edges for an undirected graph. We are denoting an edge between vertex a and b as **(a, b)**. So, the maximum possible edges of a graph with n vertices will be all possible pairs of vertices of that graph, assuming that there are no self-loops.

If a graph has n vertices, then there are C **(n,2)** possible pairs of vertices according to Combinatorics.  Solving C **(n,2)** by binomial coefficients gives us $\frac{n(n-1)}{2}$.Hence, there are $\frac{n(n-1)}{2}$ maximum possible edges in an undirected graph.
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Graphs/image/undirected_graph.PNG?raw=true)

2. Directed Graph
In a directed graph, the edges are unidirectional. For a pair **(2, 3)**, there exists an edge from vertex**2** towards vertex **3** and the only way to traverse is to go from**2 to 3**, not the other way around.
This changes the maximum number of edges that can exist in the graph. For a directed graph with n vertices, the minimum number of edges that can connect a vertex with every other vertex is **n-1**. This excludes self-loops.
If you have n vertices, then all the possible edges become **n(n-1).**
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Graphs/image/undirected_graph.PNG?raw=true)

Time Complexity of Operation on Graph
![complexity](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Graphs/image/Complexity.PNG?raw=true)
## BFS

## DFS

## Leetcode