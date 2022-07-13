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

    def check_leaf(self,node):
        if node.left==None and node.right==None:
            return True
        else:
            return False
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

    def search(self,val):
        if self.root.val==val:
            print("Find the node " + str(val))
            return True
        else:
            self.search_(val,self.root)
    def search_(self,val,cur_node):
        if val<=cur_node.val:
            if cur_node.left==None:
                print("The node is not in the tree")
                return False
            if cur_node.left.val==val:
                print("Find the node " + str(val))
                return True
            else:
                self.search_(val,cur_node.left)
        elif val>=cur_node.val:
            if cur_node.right==None:
                print("The node is not in the tree")
                return False
            if cur_node.right.val==val:
                print("Find the node "+str(val))
                return True
            else:
                self.search_(val,cur_node.right)
    def delete(self,val):
        if self.root==None:
            print("The tree is empty")
            return False
        else:
            if self.root.val==val:
                self.root=None
                return True
            else:
                 self.delete_(val,self.root)
    def delete_(self,val,cur_node):
        if val<cur_node.val:
            if cur_node.left.val==val and self.check_leaf(cur_node.left):
                self.graph[str(cur_node.val)].remove(str(cur_node.left.val))
                del self.graph[str(cur_node.left.val)]
                cur_node.left = None
                return True
            if cur_node.left.val==val and cur_node.left.left!=None and cur_node.left.right==None:
               print(cur_node.left.left)
               del self.graph[str(cur_node.left.val)]
               self.graph[str(cur_node.val)].remove(str(cur_node.left.val))
               cur_node.left=cur_node.left.left
               cur_node.left.left.parent=cur_node
               self.graph[str(cur_node.val)].append(str(cur_node.left.left.val))
               self.graph[str(cur_node.val)].sort()
               return True
            if cur_node.left.val == val and cur_node.left.left == None and cur_node.left.right != None:
                del self.graph[str(cur_node.left.val)]
                self.graph[str(cur_node.val)].remove(str(cur_node.left.val))
                cur_node.left = cur_node.left.right
                cur_node.left.right.parent = cur_node
                self.graph[str(cur_node.val)].append(str(cur_node.left.right.val))
                del self.graph[str(cur_node.left.val)]
                self.graph[str(cur_node.val)].sort()
                return True
            else:
                self.delete_(val,cur_node.left)
        if val>cur_node.val:
            if cur_node.right.val==val and self.check_leaf(cur_node.right):
                self.graph[str(cur_node.val)].remove(str(cur_node.right.val))
                del self.graph[str(cur_node.right.val)]
                cur_node.right = None
                return True
            if cur_node.right.val == val and cur_node.right.left != None and cur_node.right.right == None:
                del self.graph[str(cur_node.right.val)]
                self.graph[str(cur_node.val)].remove(str(cur_node.right.val))
                cur_node.right = cur_node.right.left
                cur_node.right.left.parent = cur_node
                self.graph[str(cur_node.val)].append(str(cur_node.right.left.val))
                self.graph[str(cur_node.val)].sort()
                return True
            if cur_node.left.val == val and cur_node.right.left == None and cur_node.right.right != None:
                del self.graph[str(cur_node.right.val)]
                self.graph[str(cur_node.val)].remove(str(cur_node.right.val))
                cur_node.right = cur_node.right.right
                cur_node.right.right.parent = cur_node
                self.graph[str(cur_node.val)].append(str(cur_node.right.right.val))
                self.graph[str(cur_node.val)].sort()
                return True
            else:
                self.delete_(val,cur_node.right)

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
     bst.insert(0)
     bst.delete(1)
     bst.print_tree()

