graph = {
    '0' : ['1','2'],
    '1' : ['3'],
    '2' : ['3'],
    '3' : ['4','5'],
    '4' : ['6','7'],
    '5' : ['8','9'],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
}
visited_dfs=set()
# visited = [] # List to keep track of visited nodes.
# queue = []     #Initialize a queue
def dfs(visited_dfs,graph,node):
    if node not in visited_dfs:
        visited_dfs.add(node)
        print(node,end=" ")
        for neighbour in graph[node]:
           dfs(visited_dfs,graph,neighbour)
    # for i in graph.keys():
    #     if i not in visited_dfs:
    #         visited_dfs.add(str(i))
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
if __name__=="__main__":
 import timeit
 import math
start_1=timeit.default_timer()
print(dfs(visited_dfs, graph, '1'))
print("\n")
stop_1=timeit.default_timer()
start_2=timeit.default_timer()
print(dfs_traversal(graph,'1'))
stop_2=timeit.default_timer()

print("The first Implementation cost {0} µs".format(math.ceil((stop_1-start_1)*pow(10,6))))
print("The Second Implementation cost {0} µs".format(math.ceil((stop_2-start_2)*pow(10,6))))
