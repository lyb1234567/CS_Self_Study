from Node import Node

class Binary_Search_Tree:
    def __init__(self):
        self.root=None
        self.graph={}
    def insert(self,val):
        if self.root==None:
            self.root=Node(val)
            self.graph[str(self.root.val)]=[]
        else:
            self.insert_(val,self.root)

    # 如果插入值比目前所在节点的值小，那么就看目前所在节点有无左边子节点，如果没有，就直接插入，如果有，那么就和这个子节点继续进行比较，这里面就有递归的思想。
    def insert_(self,val,cur_node):
        if val<cur_node.val:
            if cur_node.left==None:
                cur_node.left=Node(val)
                cur_node.left.parent=cur_node
                self.graph[str(cur_node.val)].append(str(val))
                self.graph[str(cur_node.val)].sort()
                self.graph[str(val)]=[]
            else:
                self.insert_(val,cur_node.left)
        elif val>cur_node.val:
            if cur_node.right==None:
                cur_node.right=Node(val)
                cur_node.right.parent=cur_node
                self.graph[str(cur_node.val)].append(str(val))
                self.graph[str(cur_node.val)].sort()
                self.graph[str(val)] = []
            else:
                self.insert_(val,cur_node.right)

        else:
            print("The node is already in the tree")

    def print_tree(self):
        print(self.graph)




if __name__=="__main__":
     bst=Binary_Search_Tree()
     bst.insert(3)
     bst.insert(4)
     bst.insert(2)
     bst.insert(7)
     bst.insert(8)
     bst.insert(1)
     bst.print_tree()


