from Linked_Lists.Implementation.Node import Node


class linked_list:
    def __init__(self):
        self.head_Node = None

    # O（1）
    def get_head(self):
        return self.head_Node

    def is_empty(self):
        if self.head_Node == None:
            return True
        else:
            return False
    def len(self):
        temp=self.get_head()
        count=0
        if temp is None:
            return count
        else:
            while temp:
                count=count+1
                temp=temp.next_element
            return count
    def reverse
    def insertion_head(self, data):
        temp_node = Node(data)
        temp_node.next_element = self.head_Node
        self.head_Node = temp_node
        return self.head_Node

    def insertion_tail(self, data):
        temp = Node(data)
        if self.is_empty():
            self.insertion_head(data)
        else:
            temp_node = self.head_Node
            while temp_node.next_element:
                temp_node = temp_node.next_element
            temp_node.next_element = temp

    def search(self, data):
        temp = self.get_head()
        while temp:
            if temp.data == data:
                return True
            temp = temp.next_element
        return False

    def deletion(self, data):
        cur = self.get_head()
        prev = None
        if self.search(data) is False:
            print("There is no such a value!!")
            return False

        if self.head_Node.data == data:
            temp = self.head_Node
            self.head_Node = temp.next_element
            temp.next_element = None
            return True
        while cur:
            if cur.data == data:
                prev.next_element = cur.next_element
                cur.next_element = None
                return True
            prev = cur
            cur = cur.next_element

    def print_list(self):
        temp = self.head_Node
        if temp == None:
            print("The linked list is empty!!")
        else:
            while temp:
                print(str(temp.data) + "->", end="")
                temp = temp.next_element
            print("None")
