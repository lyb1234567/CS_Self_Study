from Linked_Lists.Implementation.Linked_List import linked_list
import networkx as nx
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # Defining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.link_map={}
        self.array = []
        self.link=[]
        self.edege_num=0
        # Creating a new LinkedList for each vertex/index of the list
        for i in range(vertices):
            # Appending a new LinkedList on each array index
            self.array.append(linked_list())

    def add_edge(self,source,destination):
        if source<self.vertices and destination<self.vertices:
            self.array[source].insertion_head(destination)
            s1="A"+str(source)
            s2="A"+str(destination)
            self.edege_num=self.edege_num+1
    def return_edege_number(self):
        return self.edege_num
    def remove_edge(self,source,destination):
        if source>=0 and destination>=0:
            if self.array[source].deletion(destination):
                self.edege_num = self.edege_num-1
                return True

            else:
                return False
        else:
            return False


    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print("None")
    def return_link_map(self):
        dic={}
        for i in self.link:
            dic[i]=0
        count=0
        for j in self.link:
            dic[j]=int(dic[j])+1
            dic[j]=str(dic[j])
        self.link_map=dic
        return dic
    def add_link(self):
        for i in range(self.vertices):
            temp=self.array[i].get_head()
            while temp:
                if temp.next_element is not None:
                   s1="A"+str(temp.data)
                   s2="A"+str(temp.next_element.data)
                   self.link.append((s1,s2))
                else:
                    s1 = "A" + str(temp.data)
                    self.link.append((s1, "None"))
                temp=temp.next_element
        return self.link
    def return_link(self):
        return self.link
    def print_graph_visualization(self):
        ax = plt.gca()
        ax.set_title("Number of Edges:"+ str(self.edege_num)+", Number of Vertices:"+ str(self.vertices))
        G = nx.DiGraph()
        self.add_link()
        G.add_edges_from(self.return_link())
        val_map={}
        color=0.3
        color_div=1/self.vertices
        for i in G.nodes:
            s=i
            val_map[s]=color+color*color_div
            color=color+1
        values=[val_map.get(node) for node in G.nodes()]
        pos = nx.circular_layout(G)
        nx.draw(G, pos, cmap=plt.get_cmap('jet'),
                node_color=values, node_size=900, with_labels=True,connectionstyle='arc3, rad = 0.1',ax=ax)
        self.return_link_map()
        print(self.link_map)
        nx.draw_networkx_edge_labels(
            G, pos,
            edge_labels=self.link_map,
            font_color='red',
            label_pos=0.6,
            verticalalignment='center',
            horizontalalignment='center'
        )
        plt.show()
        print(self.link_map)
        self.link=[]
        self.link_map={}

if __name__=="__main__":
    import time
    g = Graph(4)
    g.add_edge(0,3)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(1,1)
    g.add_edge(2,1)
    g.add_edge(2,2)
    g.add_edge(3,2)
    g.add_edge(3,3)
    g.print_graph_visualization()
    plt.figure()
    g.remove_edge(3,2)
    g.print_graph_visualization()
    plt.figure()
    g.remove_edge(0, 3)
    g.print_graph_visualization()

