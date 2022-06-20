from Linked_Lists.Implementation.Node import Node
from Linked_Lists.Implementation.Linked_List import linked_list

if __name__ == "__main__":
    import math
    a = linked_list()
    a.insertion_head(0)
    a.insertion_tail(4)
    a.insertion_tail(3)
    a.insertion_tail(4)
    a.insertion_tail(5)
    a.insertion_tail(3)
    a.insertion_tail(7)
    a.insertion_tail(5)
    a.print_list()
    a.remove_duplicate()
    a.print_list()