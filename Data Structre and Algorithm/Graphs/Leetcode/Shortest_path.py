from Graphs.Implementation.Graph import Graph
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