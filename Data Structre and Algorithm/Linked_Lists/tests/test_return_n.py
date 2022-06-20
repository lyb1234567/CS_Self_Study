from Linked_Lists.Implementation.Node import Node
from Linked_Lists.Implementation.Linked_List import linked_list

if __name__ == "__main__":
    import math
    a = linked_list()
    a.insertion_head(21)
    a.insertion_tail(18)
    a.insertion_tail(60)
    a.insertion_tail(78)
    a.insertion_tail(47)
    a.insertion_tail(39)
    a.insertion_tail(99)
    a.print_list()
    print(a.return_n(5))