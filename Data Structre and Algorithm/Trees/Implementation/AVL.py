from AVL_Node import AVL_Node
class AVL:
    def __init__(self):
        self.root=None

    def __repr__(self):
        if self.root == None: return ''
        content = '\n'  # to hold final string
        cur_nodes = [self.root]  # all nodes at current level
        cur_height = self.get_height_node(self.root)+1 # height of nodes at current level
        print(cur_height)
        sep = ' ' * (2 ** (cur_height - 1))  # variable sized separator between elements
        while True:
            cur_height += -1  # decrement current height
            if len(cur_nodes) == 0: break
            cur_row = ' '
            next_row = ''
            next_nodes = []

            if all(n is None for n in cur_nodes):
                break

            for n in cur_nodes:

                if n == None:
                    cur_row += '   ' + sep
                    next_row += '   ' + sep
                    next_nodes.extend([None, None])
                    continue

                if n.val != None:
                    buf = ' ' * ((5 - len(str(n.val))) / 2)
                    cur_row += '%s%s%s' % (buf, str(n.val), buf) + sep
                else:
                    cur_row += ' ' * 5 + sep

                if n.left != None:
                    next_nodes.append(n.left)
                    next_row += ' /' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

                if n.right != None:
                    next_nodes.append(n.right)
                    next_row += '\ ' + sep
                else:
                    next_row += '  ' + sep
                    next_nodes.append(None)

            content += (cur_height * '   ' + cur_row + '\n' + cur_height * '   ' + next_row + '\n')
            cur_nodes = next_nodes
            sep = ' ' * (len(sep) / 2)  # cut separator size in half
        return content
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

    def insert(self,node):
        if self.root==None:
            self.root=node
        else:
            self.insert_(node,self.root)
    def insert_(self,node,cur_node):
        if node.val<cur_node.val:
            if cur_node.left==None:
                cur_node.left=node
                cur_node.left.parent=cur_node
                self.inspection_insertion(cur_node.left)
            else:
                self.insert_(node,cur_node.left)
        elif node.val>cur_node.val:
            if cur_node.right==None:
                cur_node.right=node
                cur_node.right.parent = cur_node
                self.inspection_insertion(cur_node.right)
            else:
                self.insert_(node,cur_node.right)
    def delete(self,node):
        if self.search(node.val)[0]==False:
            print("The node is not in the tree!!")
            return False
        else:
            node = self.search(node.val)[1]
            self.delete_node(node)

    def delete_node(self, node):
        child_num = self.child_num(node)
        node_parent = node.parent
        if child_num == 0:
            if node_parent.left == node:
                node_parent.left = None
            else:
                node_parent.right = None

        elif child_num == 1:
            child = None
            if node.left != None:
                child = node.left
            elif node.right != None:
                child = node.right
            if node_parent.left == node:
                node_parent.left = child
            elif node_parent.right == node:
                node_parent.right = child
            child.parent = node_parent
        elif child_num == 2:
            succssor = self.min_node(node)
            # 将替代者的值复制到所需删除节点的为止
            temp = node.val
            b = succssor.val
            succssor.val = temp
            node.val = b
            # 然后删除该节点，因为该节点一定是叶子节点（leaf node),所以类似于直接删除
            self.delete_node(succssor)
        if node_parent!=None:
            self.inspection_deletion(node_parent)
    def child_num(self,node):
        count=0
        if node.left!=None:
            count=count+1
        if node.right!=None:
            count=count+1
        return count
    def min_node(self,node):
        temp=node.right
        while temp.left:
            temp=temp.left
        return temp
    def inspection_insertion(self,cur_node,path=[]):
        if cur_node.parent==None:
            return
        bf = abs(self.get_bf((cur_node.parent)))
        path=path+[cur_node]
        if bf>1:
           path=path+[cur_node.parent]
           len_path=len(path)
           dif=len_path-3
           path=path[dif:]
           self.rebalance(path[2],path[1],path[0])
           return
        self.inspection_insertion(cur_node.parent, path)
    def inspection_deletion(self,cur_node):
        if cur_node == None: return
        bf=abs(self.get_bf(cur_node))
        if bf > 1:
            y = self.taller_child(cur_node)
            x = self.taller_child(y)
            self.rebalance(cur_node, y, x)

        self.inspection_deletion(cur_node.parent)


    def rebalance(self,z,y,x):
        # LL case
        if y==z.left and x==y.left:
            self.r_roate(z)
        # LR case
        if y==z.left and x==y.right:
            self.l_roate(y)
            self.r_roate(z)
        if y==z.right and x==y.right:
            self.l_roate(z)

        if y==z.right and x==y.left:
            self.r_roate(y)
            self.l_roate(z)
    def get_bf(self,node):
        if node.left==None:
            left=0
            return self.get_height_node(node)
        if node.right==None:
            right=0
            return self.get_height_node(node)
        if node.right==None and node.left==None:
            return 0
        elif  node.right!=None and node.left!=None:
           return (self.get_height_node(node.left)-self.get_height_node(node.right))
    def r_roate(self,z):
        sub_root=z.parent
        y=z.left
        t3=y.right
        y.right=z
        z.parent=y
        z.left=t3
        if t3 !=None:
            t3.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left==z:
                y.parent.left=y
            else:
                y.parent.right=y
    def l_roate(self,z):
        sub_root=z.parent
        y=z.right
        t2=y.left
        y.left=z
        z.parent=y
        z.right=t2
        if t2!=None:
            t2.parent=z
        y.parent=sub_root
        if y.parent==None:
            self.root=y
        else:
            if y.parent.left==z:
                y.parent.left=y
            else:
                y.parent.right=y
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
    def post_order(self,node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.val,end=" ")
    def in_order(self,node):
        if node:
            self.in_order(node.left)
            print(node.val,end=" ")
            self.in_order(node.right)
    def pre_order(self,node):
        print(node.val,end=" ")
        if node.left:
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)

    def taller_child(self,node):
        left=self.get_height_node(node.left)
        right=self.get_height_node(node.right)
        if left>=right:
            return node.left
        else:
            return node.right

if __name__=="__main__":
    from BST import Binary_Search_Tree
    avl=AVL()
    bst=Binary_Search_Tree()
    for i in range(3,9):
        avl.insert(AVL_Node(i))
        bst.insert(i)
    bst.pre_order(bst.root)
    print("\n")
    avl.pre_order(avl.root)
