from Graphs.Implementation.Graph import Graph
graph = {
  '0' : ['1','2'],
  '1':[ '3' ],
  '2':[ '3'],
  '3':['4','5'],
  '4':['6','7'],
  '5':['8','9'],
  '6':[ ],
  '7':[ ],
  '8':[ ],
  '9':[ ]
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0)
    print(s,end=" ")
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
  for i in graph.keys():
    if i not in visited:
      visited.append(i)
# Driver Code
bfs(visited, graph, '1')
