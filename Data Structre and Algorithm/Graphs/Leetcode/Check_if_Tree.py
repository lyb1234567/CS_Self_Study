from Graphs.Implementation.Graph import Graph

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

if __name__ == "__main__" :

    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 0)
    g.add_edge(2, 0)
    g.add_edge(3, 0)
    g.add_edge(3, 4)
    g.add_edge(4, 3)
    g.add_edge(4,5)
    g.add_edge(5,4)
    g.print_graph()
    print(is_tree(g))

