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

print(mother_vertex(graph,visited))