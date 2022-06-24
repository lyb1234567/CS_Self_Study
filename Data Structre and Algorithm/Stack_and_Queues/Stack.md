# Stack and Queue
This section explains some basic concepts of  stack and queue first, then it will give the implementations.

## Table and Contents
- [Stack](#stack)
- [Queue](#queue)
- [Leetcode](#leetcode)



## Stack
Stacks can be implemented using Lists or Linked Lists in Python language. Each implementation has its own advantages and disadvantages. Here, however, we will show an implementation of stacks using lists:
```python
class MyStack:
    def __init__(self):
        self.stack=[]
        self.stack_size=0

    def is_empty(self):
        return self.stack_size==0
    def push(self,data):
        self.stack_size=self.stack_size+1
        self.stack.append(data)

    def pop(self):
        data=self.peek()
        self.stack.remove(data)
        self.stack_size=self.stack_size-1
        return data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return self.stack_size
    def print_stack(self):
        print(self.stack)
```
The time complexity of the operation on stack:
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Stack%20and%20Queues/image/Complexity_stack.PNG?raw=true)
## Queue
Similar to the stack, a queue is another linear data structure that stores the elements in a sequential manner. The only significant difference between stacks and queues is that instead of using the LIFO principle, queues implement the FIFO method which is short for First in First Out.

Queues are implemented in many ways. They can be represented by using lists, Linked Lists, or even Stacks. But most commonly lists are used as the easiest way to implement Queues.

With typical arrays, however, the time complexity is O(n) when dequeuing an element from the beginning of the queue. This is because when an element is removed, the addresses of all the subsequent elements must be shifted by 1, which makes it less efficient. With linked lists and doubly linked lists, the operations become faster.

```python
from Linked_Lists.Implementation.Double_Linked_List import double_linked_list
class MyQueue:
    def __init__(self):
        self.items = double_linked_list()

    def is_empty(self):
        return self.items.len()==0

    def enqueue(self,data):
        return self.items.insertion_tail(data)

    def dequeue(self):
        temp=self.items.get_head().data
        self.items.remove_head()
        return temp

    def front(self):
        if self.is_empty():
            return None
        return self.items.get_head().data

    def rear(self):
        if self.is_empty():
            return None
        else:
            return self.items.get_tail().data

    def size(self):
        return self.items.len()

    def print_lst(self):
        self.items.print_list()
```

Time complexity of operation:
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Stack%20and%20Queues/image/Complexity_queue.PNG?raw=true)


## Leetcode