# graph = {
#     '0' : ['2','5'],
#     '1' : [ ],
#     '2' : ['3','4'],
#     '3' : ['6'],
#     '4' : [ ],
#     '5' : ['3','6'],
#     '6': ['4','7','8'],
#     '7': ['8'],
#     '8': [],
# }
from Graphs.Implementation.Graph import Graph
visited=[ ]
def dfs(g,visited,point):
    if str(point) not in visited:
           visited.append(point)
           temp=g.array[int(point)].get_head()
           while temp:
               dfs(g,visited,str(temp.data))
               temp=temp.next_element
    return visited
def check_path(g, source, destination):
    # Write your code here
    visited=[ ]
    a=dfs(g,visited,source)
    if str(destination) in a:
        return True
    return False
if __name__ == "__main__" :

    g1 = Graph(9)
    g1.add_edge(0, 2)
    g1.add_edge(0, 5)
    g1.add_edge(2, 3)
    g1.add_edge(2, 4)
    g1.add_edge(5, 3)
    g1.add_edge(5, 6)
    g1.add_edge(3, 6)
    g1.add_edge(6, 7)
    g1.add_edge(6, 8)
    g1.add_edge(6, 4)
    g1.add_edge(7, 8)
    g2 = Graph(4)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)
    print(check_path(g1, 3, 2))
    print(check_path(g2, 3, 0))