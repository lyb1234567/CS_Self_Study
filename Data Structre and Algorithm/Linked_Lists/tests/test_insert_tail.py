from Linked_Lists.Implementation.Node import Node
from Linked_Lists.Implementation.Linked_List import linked_list

if __name__ == "__main__":
    a = linked_list()
    a.insertion_head(0)
    a.insertion_tail(3)
    a.insertion_tail(4)
    a.insertion_tail(7)
    a.print_list()
