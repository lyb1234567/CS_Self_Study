from Linked_Lists.Implementation.Node import Node
import math

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
    def reverse(self):
        if self.is_empty():
            return False
        else:
            if self.len()==1:
                return self.head_Node
            else:
                prev=None
                cur=self.get_head()
                next=None
                while cur:
                    next=cur.next_element
                    cur.next_element=prev
                    prev=cur
                    cur=next
                    self.head_Node=prev
                return True
    def detect_loop(self):
        if self.is_empty():
            return False
        else:
            first = self.get_head()
            second = self.get_head()
            while first and second :
                first = first.next_element
                second = second.next_element.next_element
                if second==first:
                    return True
            return False
    def find_middle(self):
        if self.is_empty():
            return False
        else:
            count=0
            L=self.len()
            temp = self.get_head()
            while temp:
                count=count+1
                if math.ceil(L/2)==count:
                    return temp.data
                temp=temp.next_element
    def remove_duplicate(self):
        if self.is_empty():
            return False
        else:
            if self.len()==1:
                return True
            else:
                temp=self.get_head()
                while temp:
                    inner=temp.next_element
                    prev=None
                    while inner:
                        if inner.data==temp.data:
                            prev.next_element=inner.next_element
                            inner.next_element=None
                        prev=inner
                        inner=inner.next_element
                    temp=temp.next_element
                return True
    def return_n(self,index):
        if self.is_empty():
            return False
        if index>self.len():
            return False
        else:
            temp=self.get_head()
            count=0
            while temp:
                count=count+1
                if count==7-index+1:
                    return temp.data
                temp=temp.next_element
            return False
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
