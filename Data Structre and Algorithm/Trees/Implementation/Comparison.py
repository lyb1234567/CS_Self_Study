import math

from AVL_Node import AVL_Node
from AVL import AVL
from BST import Binary_Search_Tree

if __name__=="__main__":
    import timeit
    avl = AVL()
    bst = Binary_Search_Tree()
    for i in range(1, 100):
        avl.insert(AVL_Node(i))
        bst.insert(i)

    start_search_avl=timeit.default_timer()
    node_avl=avl.search(51)
    stop_search_avl = timeit.default_timer()

    start_search_bst = timeit.default_timer()
    node_bst = bst.search(51)
    stop_search_bst = timeit.default_timer()
    print("Search in AVL tree costs {0} μs".format(math.ceil((stop_search_avl-start_search_avl)*pow(10,6))))
    print("Search in BST tree costs {0} μs".format(math.ceil((stop_search_bst - start_search_bst)*pow(10,6))))