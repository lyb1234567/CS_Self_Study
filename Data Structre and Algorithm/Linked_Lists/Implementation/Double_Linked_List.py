class Node:
    def __init__(self,data):
        self.data=data
        self.next_element=None
        self.previous_element=None

class double_linked_list:
    def __init__(self):
        self.head_Node=None
    # O（1）
    def get_head(self):
        return self.head_Node

    def get_tail(self):
        temp=self.head_Node
        while temp.next_element:
            temp=temp.next_element
        tail=temp
        return tail
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
    def remove_head(self):
        if self.is_empty():
            return False
        temp=self.get_head()
        self.head_Node=temp.next_element
        temp.next_element=None
        return True
    def is_empty(self):
        if self.head_Node==None:
            return True
        else:
            return False
    def insertion_head(self,data):
        if self.head_Node==None:
            self.head_Node=Node(data)
            self.head_Node.previous_element=None
            return
        temp_node=Node(data)
        temp_node.next_element=self.head_Node
        temp_node.next_element.previous_element=temp_node
        self.head_Node=temp_node
        return self.head_Node
    def insertion_tail(self,data):
        temp=Node(data)
        if self.is_empty():
            self.insertion_head(data)
        else:
            temp_node=self.head_Node
            while temp_node.next_element:
                temp_node=temp_node.next_element
            temp_node.next_element=temp
            temp.previous_element=temp_node

    def search(self,data):
        temp=self.get_head()
        while temp:
            if temp.data==data:
                return True
            temp=temp.next_element
        return False
    def deletion(self,data):
        cur=self.get_head()
        if self.search(data) is False:
            print("There is no such a value!!")
            return False

        if self.head_Node.data==data:
            temp=self.head_Node
            self.head_Node=temp.next_element
            temp.next_element=None
            return True
        while cur:
            if cur.data==data:
                cur.next_element.previous_element=cur.previous_element
                cur.previous_element.next_element=cur.next_element
                cur.next_element=None
                return True
            cur=cur.next_element
    def print_list(self):
        temp=self.head_Node
        if temp==None:
            print("The linked list is empty!!")
        else:
            while temp:
                print(str(temp.data)+"->",end="")
                temp=temp.next_element
            print("None")
    def print_list_reverse(self):
        temp = self.head_Node
        if temp == None:
            print("The linked list is empty!!")

        else:
            temp=self.get_tail()
            while temp:
                print(str(temp.data) + "->", end="")
                temp = temp.previous_element
            print("None")
    
