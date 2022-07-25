from Node import Node

class Binary_Search_Tree:
    def __init__(self):
        self.root=None
        self.graph={}
        self.graph_tree={}
        self.lst_tree=[]
    def insert(self,val):
        if self.root==None:
            self.root=Node(val)
            self.graph[str(self.root.val)]=[]
            self.lst_tree.append(self.root.val)
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
                self.lst_tree.append(val)
                self.graph[str(cur_node.val)].append(str(val))
                self.graph[str(cur_node.val)].sort()
                self.graph[str(val)]=[]
            else:
                self.insert_(val,cur_node.left)
        elif val>cur_node.val:
            if cur_node.right==None:
                cur_node.right=Node(val)
                cur_node.right.parent=cur_node
                self.lst_tree.append(val)
                self.graph[str(cur_node.val)].append(str(val))
                self.graph[str(cur_node.val)].sort()
                self.graph[str(val)] = []
            else:
                self.insert_(val,cur_node.right)

        else:
            print("The node is already in the tree")

    def search(self,val):
        if self.root.val==val:
            return [True,self.root]
        else:
            return self.search_(val,self.root)
    def search_(self,val,cur_node):
        if val<=cur_node.val:
            if cur_node.left==None:
                return [False,None]
            if cur_node.left.val==val:
                return [True,cur_node.left]
            else:
                return self.search_(val,cur_node.left)

        elif val>=cur_node.val:
            if cur_node.right==None:
                return [False,None]
            if cur_node.right.val==val:
                return [True,cur_node.right]
            else:
                return self.search_(val,cur_node.right)

    def child_num(self,node):
        count=0
        if node.left!=None:
            count=count+1
        if node.right!=None:
            count=count+1
        return count

    def get_height_tree(self):
        if self.root==None:
            return 0
        else:
            cur_height=0
            return self.get_height_tree_(self.root,cur_height)-1
    def get_height_tree_(self,cur_node,height):
           if cur_node==None:
               return height
           left=self.get_height_tree_(cur_node.left,height+1)
           right=self.get_height_tree_(cur_node.right,height+1)
           return max(left,right)
    def get_height_node(self,node):
        if node==None:
            return 0
        else:
            if node.left==None and node.right==None:
                return max(self.get_height_node(node.left),self.get_height_node(node.right))
            else:
                return max(self.get_height_node(node.left), self.get_height_node(node.right))+1
    def min_node(self,node):
        temp=node.right
        while temp.left:
            temp=temp.left
        return temp
    def delete_value(self,val):
        if self.search(val)[0]==False:
            print("The node is not in the tree!!")
            return False
        else:
            node=self.search(val)[1]
            self.delete_node(node)

    def delete_node(self,node):
        child_num=self.child_num(node)
        node_parent=node.parent
        if child_num==0:
            if node_parent.left==node:
                node_parent.left=None
            else:
                node_parent.right=None

        elif child_num==1:
            child=None
            if node.left!=None:
                child=node.left
            elif node.right!=None:
                child=node.right
            if node_parent.left==node:
                node_parent.left=child
            elif node_parent.right==node:
                node_parent.right=child
            child.parent = node_parent
        elif child_num==2:
            succssor = self.min_node(node)
            # 将替代者的值复制到所需删除节点的为止
            temp=node.val
            b=succssor.val
            succssor.val=temp
            node.val = b
            # 然后删除该节点，因为该节点一定是叶子节点（leaf node),所以类似于直接删除
            self.delete_node(succssor)
        print(node.parent.val)
    def pre_order(self,node):
        print(node.val,end=" ")
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)

    def post_order(self,node,lst):
        if node:
            self.post_order(node.left,lst)
            self.post_order(node.right,lst)
            print(node.val,end=" ")
            lst.append(node.val)
        return lst

    def in_order(self,node,lst):
        if node:
            self.in_order(node.left,lst)
            print(node.val,end=" ")
            lst.append(node.val)
            self.in_order(node.right,lst)
        return lst

    def find_min(self):
        min=self.root.val
        if self.root.left==None and self.root.right==None:
            return min
        else:
            return self.find_min_(self.root,min)

    def find_min_(self,node,min):
        if node.left:
            if node.left.val<min:
                min=node.left.val
            min=self.find_min_(node.left,min)
            return min

        if node.right:
            if node.right.val<min:
                min=node.right.val
            min=self.find_min_(node.right,min)
            return min
        return min
    def find_K_th_Max(self,k):
         tree=[]
         lst=self.in_order(self.root,tree)
         return lst[-k]
    def find_ancestors(self,k):
        lst=[]
        if not self.root:
            return None

        if k==self.root.val:
            return None
        else:
            current=self.root
            while current:
                if k<current.val:
                    lst.append(current.val)
                    current=current.left
                elif k>current.val:
                    lst.append(current.val)
                    current=current.right
                else:
                    return lst[::-1]
            return []
    def find_K_node(self,k):
        lst=[]
        if not self.root:
            return None
        if k==0:
            return [self.root.val]
        else:
            cur=self.root
            self.find_K_node_(cur,k,lst)
            return lst

    def find_K_node_(self,cur,k,lst):
         if cur==None:
             return
         if k==0:
             lst.append(cur.val)
         else:
             self.find_K_node_(cur.left,k-1,lst)
             self.find_K_node_(cur.right,k-1,lst)
def test_find_min(lst):
    bst = Binary_Search_Tree()
    for i in lst:
        bst.insert(i)
    bst.pre_order(bst.root)
    print("\n")
    print(bst.find_min())


def test_find_K_Max(lst,n):
    bst = Binary_Search_Tree()
    for i in lst:
        bst.insert(i)
    bst.pre_order(bst.root)
    print("\n")
    tree=[]
    print(bst.find_K_th_Max(n))

def test_find_ancestors(lst):
    bst = Binary_Search_Tree()
    for i in lst:
        bst.insert(i)
    print(bst.find_ancestors(-19))
if __name__=="__main__":
     bst=Binary_Search_Tree()
     bst.insert(30)
     bst.insert(10)
     bst.insert(-14)
     bst.insert(-19)
     bst.insert(16)
     bst.insert(12)
     print(bst.find_K_node(2))



