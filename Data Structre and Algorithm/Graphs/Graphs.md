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
The BFS algorithm earns its name because it grows breadth-wise. All the nodes at a certain level are traversed before moving on to the next level.

The level-wise expansion ensures that for any starting vertex, you can reach all others, one level at a time.

To implement the BFS algorith, we can use the data structure: queue. We add each node into the queue, and check if the current and its  child node has already been traversed. If so, then pop it. If not, then mark it as a visited node,and try to traverse its child node next time.
使用队列的主要原因就在于，它的deque方法，可以模拟头节点出列。
```python
queue=MyQueue()
        visited=[]
        queue.enqueue(int(point))
        visited.append(int(point))
        while not queue.is_empty():
             s=int(queue.dequeue())
             temp=self.array[s].get_head()
             while temp:
                 if temp.data not in visited:
                     visited.append(temp.data)
                     queue.enqueue(temp.data)
                 temp=temp.next_element
        #这段代码可加可不加，本身bfs算法，并没有要求一定要所有的节点都被遍历到
        for i in range(self.vertices):
            if i not in visited:
                visited.append(i)
        return visited
```

## DFS
The DFS algorithm is the opposite of BFS in the sense that it grows depth-wise.

Starting from any node, we keep moving to an adjacent node until we reach the farthest level. Then we move back to the starting point and pick another adjacent node. Once again, we probe to the farthest level and move back. This process continues until all nodes are visited.

与BFS大同小异，只是我们每次遍历一个节点，我们可以需要遍历到最深处而不是直接遍历相邻节点，直到最深的节点再无子节点，那么重返上一级，遍历邻接点，我的实现是使用了递归。
```python
 def dfs(self,visited,point):
       if point not in visited:
           visited.append(point)
           temp=self.array[int(point)].get_head()
           while temp:
               self.dfs(visited,str(temp.data))
               temp=temp.next_element
       return visited
```
这样会比正常用一个辅助函数的速度稍微长一些。
```python
def dfs_traversal_helper(g, source, visited):
    result = ""
    # Create Stack(Implemented in previous lesson) for Depth First Traversal
    # and Push source in it
    stack=[]
    stack.append(source)
    visited[int(source)] = True
    # Traverse while stack is not empty
    while stack :
        # Pop a vertex/node from stack and add it to the result
        current_node = stack.pop(-1)
        result += str(current_node)
        # Get adjacent vertices to the current_node from the array,
        # and if they are not already visited then push them in the stack
        temp = g[str(current_node)]
        for neighbour in temp:
            if not visited[int(neighbour)]:
                stack.append(int(neighbour))
                # Visit the node
                visited[int(neighbour)] = True
    return result, visited  # For the above graph it should return "12453"

def dfs_traversal(g, source):
    result = ""
    num_of_vertices = len(g.keys())
    if num_of_vertices ==0:
        return result
    # A list to hold the history of visited nodes
    # Make a node visited whenever you enqueue it into queue
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = dfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return list(result)
```
## Leetcode
- [Detect Cycyle](#detect-cycle)
- [Find Mother vertex](#find-mother-vertex)
- [Count the number of Edges](#count-the-number-of-edges)
- [Check mother vertex](#find-mother-vertex)
- [Check if a graph is a tree](#check-if-a-graph-is-a-tree)
- [Minimum Path](#find-the-minimun-path-between-two-vertex)
### Detect cycle
```python
graph = {
    '0' : ['1'],
    '1':['2','0'],
    '2':[ ]
}

def cycle_detect(g):
    visited=set()
    for i in g.keys():
        visited.add(i)
        for neighbour in g[i]:
            if neighbour in visited:
                return True
    print(visited)
    return False

if __name__=="__main__":
    print(cycle_detect(graph))
```
### Find mother Vertex
直接dfs，遍历所有从目标节点开始遍历，如果它是母节点，那么所有节点都应该被遍历，否则就不是母节点
```python
graph = {
    '0' : ['1'],
    '1':['2'],
    '2':['3'],
    '3':['0']
}
visited=[]
def dfs(visited,point,g):
    if point not in visited:
        visited.append(point)
        for neighbour in g[point]:
            dfs(visited,neighbour,g)
    return visited
def mother_vertex(g,visited):
   mother=[]
   for i in g.keys():
       visited=dfs(visited,i,g)
       if len(visited)==len(g.keys()):
           mother.append(i)
   if len(mother)==0:
       return -1
   return mother
```

### Count the number of Edges
```python
def count_edges(g):
    count=0
    for i in g.keys():
        count=count+len(g[i])
    return count/2

```
### Check if a graph is a tree
就是查找Graph是否有cycle
```python
def is_tree(g):
    visited=set()
    for i in range(g.vertices):
        temp=g.array[i].get_head()
        visited.add(i)
        while temp:
            if temp.data in visited:
                return False
            temp=temp.next_element
    return True
```
### Find the minimun path between two vertex
我们可以使用BFS来解这道题。因为BFS 是广度遍历，所以当我们找到所需要的终点节点，之前的距离肯定是最短的，因为是横向而不是纵向。所以当我们计算距离时，对于每一个图中，每遍历一个头节点节点，它的子节点距离都增加1，而当目标节点，是此节点的子节点时，直接返回距离即可。可以理解为 distanc[s] 指的是目前的层级
```python
graph = {
    '0' : ['1','5'],
    '1':['2'],
    '2':['3','4'],
    '3':['5'],
    '4':[ ],
    '5':['7','6' ],
    '6':[ '8'],
    '7':[ '7'],
    '8':[ ]
}
visited=[]
def bfs(visited,g,source,destination):
    queue=[]
    distance=[0]*len(g.keys())
    queue.append(source)
    visited.append(source)
    while queue:
        s=queue.pop(0)
        for neighbour in g[s]:
            if neighbour not in visited or neighbour==destination:
                visited.append(neighbour)
                queue.append(neighbour)
                distance[int(neighbour)]=distance[int(s)]+1
                if neighbour==destination:
                    return distance[int(neighbour)]
    return -1

print(bfs(visited,graph,'0','8'))
```

