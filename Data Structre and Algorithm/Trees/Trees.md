# Trees
This section explains some basic concepts of Trees first, then it will give the implementations of them.
- [Concept](#concept)
- [Binary Search Tree](#binary_search_tree)
- [AVL Tree](#avl_tree)
- [Red Black Tree](#red_black_tree)
- -[2-3 Trees](#red_black_tree) 
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
查看一个二叉树是否是height-balanced,主要就是看每个节点对应的左边的子二叉树和子右二叉树是否高度一致，或者说差距不能大于1.


## Binary Search Tree

## AVL Tree

## Red Black Tree

## 2-3 Trees

## Leetcode