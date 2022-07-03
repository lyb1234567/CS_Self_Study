from Linked_Lists.Implementation.Linked_List import linked_list
from Stack_and_Queues.Implementation.queue import MyQueue
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
            if self.edege_num>=1:
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

            else:
                if self.vertices==1:
                    self.link.append(("A0", "A0"))
                if i+1==self.vertices:
                    break
                if i+1==self.vertices-1:
                    s1 = "A" + str(i + 1)
                    s2 = "None"
                    self.link.append((s1, s2))
                else:
                    s1="A"+str(i+1)
                    s2="A"+str(i+1+1)
                    self.link.append((s1,s2))
        return self.link
    def return_link(self):
        return self.link
    def print_graph_visualization(self):
        ax = plt.gca()
        ax.set_title("Number of Edges:"+ str(self.edege_num)+", Number of Vertices:"+ str(self.vertices))
        G = nx.DiGraph()
        if self.edege_num>=1:
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
            nx.draw_networkx_edge_labels(
                G, pos,
                edge_labels=self.link_map,
                font_color='red',
                label_pos=0.6,
                verticalalignment='center',
                horizontalalignment='center'
            )
            self.link=[]
            self.link_map={}
            plt.show()
        else:
            self.add_link()
            K3 = nx.Graph(self.link)
            G.add_nodes_from(K3)
            val_map = {}
            color = 0.02
            color_div = 1 / self.vertices
            for i in G.nodes:
                s = i
                val_map[s] = color + color * color_div
                color = color + 1
            values = [val_map.get(node) for node in G.nodes()]
            pos = nx.circular_layout(G)
            nx.draw(G, pos, cmap=plt.get_cmap('jet'),
                    node_color=values, node_size=900, with_labels=True, connectionstyle='arc3, rad = 0.1', ax=ax)
            self.link=[]
            plt.show()
    def bfs(self,point):
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
    def dfs(self,visited,point):
       if point not in visited:
           visited.append(point)
           temp=self.array[int(point)].get_head()
           while temp:
               self.dfs(visited,str(temp.data))
               temp=temp.next_element
       return visited
    def anime(self):
        ani = FuncAnimation(fig, update, frames=6, interval=1000, repeat=True)
        plt.show()
fig, ax = plt.subplots(figsize=(6,4))
def update(num):
    ax.clear()
    g = Graph(num+1)
    source=num
    destination=num
    print(num)
    g.print_graph_visualization()
if __name__=="__main__":
    g=Graph(3)
    g.add_edge(0, 2)
    g.add_edge(0, 1)
    g.add_edge(0, 0)
    g.add_edge(1, 0)
    g.add_edge(1,2)
    g.print_graph()
    g.print_graph_visualization()

