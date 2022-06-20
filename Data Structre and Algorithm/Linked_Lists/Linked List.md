## Linked Lists
This section explains some basic concepts of linked lists first, then it will give the implementations of two types of linked list: Single linked list and Double linked list in Python.

### Table of  contents
- [Concept](#concept)
- [Single linked list](#single-linked-list)
- [Double linked list](#double-linked-list)
- [Operation on Single linked list](#operation-on-single-linked-list)
- [Operation on Double linked list](#operation-on-double-linked-list)
- [Test](#test)

#### Concept
The main difference between lists and linked lists is in the way elements are inserted and deleted. As for linked lists, insertion and deletion at the head happen in a constant amount of time, whereas at tail, it takes **O(n)** time. In the case of lists, it takes **O(n)** time to insert or delete a value. This is because of the different memory layouts of both the data structures. Lists are arranged contiguously in the memory, while nodes of a linked list may be dispersed in the memory. This memory layout also affects access operation; contiguous layout of lists allows us to index the list; thus, access operation in the list is O(1), whereas, for a linked list, we need to perform a traversal thus, it becomes **O(n)**. The following table sums up the performance tradeoff between list and linked list:

![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Linked_Lists/image/Comparison%20of%20lists%20and%20Linked%20list.PNG?raw=true)
#### Single linked list
In the single linked list, there is only one direction for the operation. The baisc Implementation will be:
```python
class Node:
    def __init__(self,data):
        self.data=data
        self.next_element=None
class linked_list:
    def __init__(self):
        self.head_Node=None
```

#### Double linked list
In the double linked list, it has two different directions. The basic implementation will be:
```python
class Node:
    def __init__(self,data):
        self.data=data
        self.next_element=None
        self.previous_element=None

class double_linked_list:
    def __init__(self):
        self.head_Node=None
```

#### Operation on Single linked list

**Insertion at head**
```python
    def insertion_head(self,data):
        temp_node=Node(data)
        temp_node.next_element=self.head_Node
        self.head_Node=temp_node
        return self.head_Node
```
**Insertion at tail**
```python
    def insertion_tail(self,data):
        temp=Node(data)
        if self.is_empty():
            self.insertion_head(data)
        else:
            temp_node=self.head_Node
            while temp_node.next_element:
                temp_node=temp_node.next_element
            temp_node.next_element=temp
```
**Search in Single linked list**
```python
    def search(self,data):
        temp=self.get_head()
        while temp:
            if temp.data==data:
                return True
            temp=temp.next_element
        return False
```
**Deletion by value**
```python
 def deletion(self,data):
        cur=self.get_head()
        prev=None
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
                prev.next_element=cur.next_element
                cur.next_element=None
                return True
            prev=cur
            cur=cur.next_element
```

**Find Length**
```python
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
```
**Reverse**
思路：
1.首先检查链表是否为空，如果是空的，那么返回False
2.如果仅有一个头节点，链表本身反转不变
3.如果链表长度超过1，那么首先遍历整条链表，每次遍历一个节点，保存期prev和next节点，并将cur节点的下一个节点，设置为prev节点，同时将cur节点设为赋给prev节点，同时将cur更新为下一节点。
4.将头节点更新为prev节点，那么反转完成，复杂度为 $O（n）$
```python
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
```
**Detect loop**
Use the method of double pointers, and when we iterate each pointer, if we come across the situation when both of them are equal to each other, then we can say we find a loop.
The time complexity: $O(n)$
```python
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
```

**Find the middle**
```python
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
```
**Remove the duplicate**
So,for each node, we interate the reaming list once, and then check there is a duplicate in the remaining linked list. If so, use the same method that we use when implementing the deletion.
Time Complexity: $O(n^2)$
```python
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
```
**Return N-th Node**
```python
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
```
#### Operation on Double linked list
**Insertion at head**
```python
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
```

**inseration at tail**
```python
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
```
**Deletion by value**
```python
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
```

#### Test
- Test for inseration at head in single linked list
- Test for inseration at tail single linked list
- Test for searching value in single linked list
- Test for Deletion by value in single linked list
- Test for detecting the loop in single linked list
- Test for finding the middle node in single linked list
- Test for removing the duplicate in single linked list
- Test for insertation at head at double linked list
- Test for inseration at tail at double linked list
- Test for Deletion by valuee in double linked list