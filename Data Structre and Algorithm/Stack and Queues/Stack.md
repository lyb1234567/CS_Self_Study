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
## Queue

## Leetcode