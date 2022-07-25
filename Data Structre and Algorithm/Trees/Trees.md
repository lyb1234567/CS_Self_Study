# Trees
This section explains some basic concepts of Trees first, then it will give the implementations of them.
- [Concept](#concept)
- [Binary Tree](#binary-tree)
- [Binary Search Tree](#binary-search-tree)
- [AVL Tree](#avl-tree)
- [Red Black Tree](#red-black-tree)
- -[2-3 Trees](#2-3-trees) 
- [Leetcode](#leetcode)




## Concept
Trees consist of vertices (nodes) and edges that connect them. Unlike the linear data structures that we have studied so far, trees are hierarchical. They are similar to Graphs, except that a **cycle** cannot exist in a Tree-they are **acyclic**. In other words, there is always exactly one path between any two nodes.
- **Root Node:**
A node with no parent nodes. Generally, trees don’t have to have a root. However, rooted trees have one distinguished node and are largely what we will use in this course.
- **Child Node:**
A Node which is linked to an upper node (**Parent Node**)
- **Parent Node**
A Node that has links to one or more 

- **Sibling Node**
Nodes that share same Parent Nodes
- **Leaf Node**
A node that doesn’t have any *Child Node*
- **Ancestor Nodes**
The nodes on the path from a node d to the root node. Ancestor nodes include node d’s parents, grandparents, and so on

![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Trees/image/Trees.PNG?raw=true)
In the figure above, **1 **is the Root as well as parent node to child nodes **2,3, and 4**. **Node 3** is a parent node to child nodes **6 and 7**. And as **nodes 2,3, and 4** share the same parent **node 1**, so they are siblings to each other. Similarly, **6 and 7** are also **sibling nodes** as their parent is same, that is **3**.

**Some other terminologies and Formula**
- **Sub-tree**
For a particular non-leaf node, a collection of nodes, essentially the tree, starting from its child node. The tree formed by a node and its descendants.
- **Degree of a node**
Total number of children of a node
- **Length of a path**
The number of edges in a path
- **Depth of a node n**
The length of the path from a node n to the root node. The depth of the root node is 0.
- **Level of a node n**
 (Depth of a Node)+1
- **Height of a node n**
The length of the path from n to its deepest descendant. So the height of the tree itself is the height of the root node and the height of leaf nodes is always 0.
- **Height of a Tree**
Height of its root node

**Height-Balanced Tree**
查看一个二叉树是否是height-balanced,主要就是看每个节点对应的左边的子二叉树和子右二叉树是否高度一致，或者说差距不能大于1.比如说下图，对于根节点1来说，它左边的子二叉树的高度为2，右子二叉树高度为1，就符合条件，同理，当子节点2，它的左边为1，右边为0，所以差距为1，也符合条件。所一次类推，这个二叉树就是height-balanced的。
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Trees/image/height-balanced.PNG?raw=true)


## Binary Tree
**Complete Binary Tree**
A complete binary tree is a binary tree in which all the levels of the tree are fully filled, except for perhaps the last level which can be filled from left to right.
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Trees/image/Complete%20Binary%20Tree.PNG?raw=true)

**Full Binary Tree**
- In a full or ‘proper’ binary tree, every node has 0 or 2 children. No node can have 1 child.
- The total number of nodes in a full binary tree of height ‘h’ can be expressed as:
$2h+1\le$total number of nodes$\le2^{(h+1)}-1$

**Perfect Binary Tree**
A Binary tree is said to be Perfect if all its internal nodes have two children and all leaves are at the same level.
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Trees/image/Perfect%20Binary%20Tree.PNG?raw=true)
## Binary Search Tree
The basic structure of a binary search tree is that, for each node, its right child node should be bigger than the current node, and its left child node should be smaller than the current node:
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Trees/image/BST.PNG?raw=true)

**Insersion**
插节点的基本思想就是递归，首先判断是否有根节点，如果没有，那么根节点就是需要插入的节点，如果已经有根节点，那么就判断当前节点是否大于需要插入的节点，如果是，那么将它插在右边，这时候又需要判断当前节点是否右边已经存在节点，如果否，那么就直接插入，如果没有，那么就继续搜索，如果插入的值比当前节点的值大，那么从右开始同理
```python
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
```
**Search in the Binary Search Tree**
搜索的思想和插入节点的思想差不多，也是递归深度遍历，如果遇到相同的值，那么代表找到了目标值，那么返回 **True**  如果没有找到就继续搜索，知道发现子节点为空，那么就代表书中没有目标节点，那么返回 **False**.
```python
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
```
**Deletion in the Binary Search Tree**
在BST中删除某个节点的思想主要分为三种情况
- 删除的节点没有子节点，也就是说可以直接删除
- 删除的节点有一个子节点，那么删除该结点之后，删除节点的父节点的子节点，就是删除节点的子节点
- 删除的节点有两个子节点，需要判断删除的该节点的右边子二叉树中的节点中哪个节点最小，也就是搜索其右边子二叉树的左边分支，找到目标节点之后，与需要删除的节点进行替换即可。
```python
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
                self.lst_tree.remove(str(node.val))
                node_parent.left=None
            else:
                self.lst_tree.remove(str(node.val))
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
            self.lst_tree.remove(str(node.val))
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
```
**Three different types of Binary Search Tree**
- Pre-order Traversal
- Post-order Traversal
- In-order Traversal

**Pre-order Traversal**
这个遍历就是从父节点/根节点开始遍历完所有根节点，那么我们所需要做的就是对每个父节点进行左右深度搜索，这便又是一个递归的思想，在每次递归之前先打印当前父节点，同时先遍历左边子节点，当无法在左边继续进行深度搜索时，那么就开始回到上一层节点，往右遍历。
```python
    def pre_order(self,node):
        print(node.val,end=" ")
        if node.lef
            self.pre_order(node.left)
        if node.right:
            self.pre_order(node.right)
```
**Post-order Traversal**
这个遍历就是，上面的遍历方式反过来，从子节点，从左往右开始遍历。从下方代码可以看出，我们先进行左右深度遍历，当没有节点可以遍历时，我们遍可以打印当前节点。
```python
    def post_order(self,node):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.val,end=" ")
```
**In-order Traversal**
这个遍历方式，就是从子节点，从左往右一次遍历，在当前遍历结束，就返回上一层，所以打印出来的就是从小到大的顺序节点
```python
    def in_order(self,node):
        if node:
            self.in_order(node.left)
            print(node.val,end=" ")
            self.in_order(node.right)
```
## AVL Tree
AVL树称为高度平衡的二叉搜索树，首先要满足二叉搜索树的性质。然后做了一定改进，能够使二叉搜索树及其子树的左右分支的分支高度平衡。这样能够大大的提高查找效率。对于AVL树，如果它有N个结点，其高度可保持在 log 2 N，搜索时间复杂度O(log2N).

**Insertion and Deletion on AVL Tree**
要在AVL树中增加一个节点，首先我们需要了解四种情况下， AVL需要实现自3平衡（self-balancing:.
LL LR RR RF.详情可见：（https://www.educative.io/courses/data-structures-coding-interviews-python/qVDlKBGDE6y）. 这就代表我们需要进行不同的两种操作：右旋和左旋。在删除某节点的时候同理
```python
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
```
**Comparison between the AVL Tree and BST**
搜索某个节点，AVL的速度大概是普通BST速度的三倍左右
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Trees/image/Comparison_AVL_BST.PNG?raw=true)
## Red Black Tree

## 2-3 Trees

## Leetcode
- [Find minimum value in Binary Search Tree](#find-minimum-value-in-binary-search-tree)
- [Find kth maximum value](#find-kth-maximum-value)
- [Find ancestors of a node](#find-the-anscetors-of-a-node)
- [Find Nodes at "k" distance from the Root](#find-nodes-at-k-distance-from-the-root)


### Find minimum value in Binary Search Tree
对二分查找树进行遍历递归，使用一个temp_min作为辅助，找到即可找到最小值,思路跟查找某个值是一样的
```python
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
```

### Find kth maximum value
最简单的做法就是用一个辅助数组，然后对BST进行内序遍历，这样就会得到一个从小到大排列好的数组然后就可以，想要获得第K个最大值，则返回lst[-k]即可
```python
    def in_order(self,node,lst):
        if node:
            self.in_order(node.left,lst)
            print(node.val,end=" ")
            lst.append(node.val)
            self.in_order(node.right,lst)
        return lst
```

### Find the anscetors of a node
本题思路就是从头节点开始遍历，对每个节点进行比较，如果大于目前节点就右拐小于目前节点就左拐，并将遍历过的节点存入数组中。
```python
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
```

### Find Nodes at "k" distance from the Root
本题思路也可以遍历所有节点，对每个目前节点进行左子二叉树和右子二叉树的递归，每递归一次，k值就减1，知道k值为0，此时就可以存入数组中
```python
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
```