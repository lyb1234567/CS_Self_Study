from Linked_Lists.Implementation.Node import Node
from Linked_Lists.Implementation.Linked_List import linked_list

if __name__ == "__main__":
    a = linked_list()
    a.insertion_head(0)
    a.insertion_tail(3)
    a.insertion_tail(4)
    a.insertion_tail(5)
    head=a.get_head()
    node=a.get_head()
    while node:
        if node.next_element is None:
            node.next_element=head.next_element
            break
        node=node.next_element
    print(a.detect_loop())