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
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Stack_and_Queues/image/Complexity_queue.PNG?raw=true)
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

Time complexity of operation on Queue:
![image](https://github.com/lyb1234567/CS_Self_Study/blob/master/Data%20Structre%20and%20Algorithm/Stack_and_Queues/image/Complexity_queue.PNG?raw=true)


## Leetcode
- [x] [binary converter](#binary-converter)
- [x] [Reverse K element](#reverse-k-element)
- [x] [Implement Queue](#implement-queue-using-stack)
- [x] [Sort Stack](#sort-stack)
- [ ] [Post-fix Expression](#post-fix-expression)
- [ ] [Next Greater Element Using a Stack](#next-greater-element-using-a-stack)
- [x] [Check Balanced Parentheses using Stack](#check-balanced-parentheses-using-stack)
- [x] [min( ) Function Using a Stack](#min-function-using-a-stack)




### Binary Converter
we first initialize a queue object and push a 1. Then, for each loop, it will deque an element, and each of them will be both added a "1" and "0".
```python
from Stack_and_Queues.Implementation.queue import MyQueue
def find_bin(n):
    temp=[]
    if n==0:
        return temp
    else:
        sup_queue=MyQueue()
        sup_queue.enqueue(1)
        for i in range(n):
            temp.append(str(sup_queue.dequeue()))
            s1=temp[i]+"0"
            s2=temp[i]+"1"
            sup_queue.enqueue(s1)
            sup_queue.enqueue(s2)
        return temp
```

### Reverse K element
```python
def reverse(queue,k):
    if k>queue.size():
        return None
    else:
        stack=MyStack()
        sup_queue=MyQueue()
        for i in range(k):
            stack.push(queue.dequeue())
        for i in range(k):
            sup_queue.enqueue(stack.pop())
        for i in range(queue.size()):
            sup_queue.enqueue(queue.dequeue())
        queue=sup_queue
        return queue
```

### Implement Queue using Stack
```python
from Stack_and_Queues.Implementation.stack import MyStack
class NewQueue:
        def __init__(self):
            self.main_stack = MyStack()
            self.items=self.main_stack.stack
            # Write your code here
        def is_empty(self):
            return self.main_stack.size()==0
        # Inserts Element in the Queue
        def enqueue(self, value):
            # Write your code here
            self.items.append(value)
        # Removes Element From Queue
        def dequeue(self):
            # Write your code here
            pop=self.items[0]
            self.items.remove(pop)
            return pop
        def print_lst(self):
            print(self.items)
if __name__=="__main__":
    stack=MyStack()
    queue=NewQueue()
    queue.enqueue(5)
    queue.enqueue(6)
    queue.dequeue()
    queue.print_lst()
```

### Reverse K elements
```python
from Stack_and_Queues.Implementation.stack import MyStack
from Stack_and_Queues.Implementation.queue import MyQueue
def reverse(queue,k):
    if k>queue.size():
        return None
    else:
        stack=MyStack()
        sup_queue=MyQueue()
        for i in range(k):
            stack.push(queue.dequeue())
        for i in range(k):
            sup_queue.enqueue(stack.pop())
        for i in range(queue.size()):
            sup_queue.enqueue(queue.dequeue())
        queue=sup_queue
        return queue
if __name__=="__main__":
    Queue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 10
    queue=MyQueue()
    for i in range(len(Queue)):
        queue.enqueue(Queue[i])
    queue.print_lst()
    queue=reverse(queue,k)
    queue.print_lst()
```
### Sort Stack

```python
from Stack_and_Queues.Implementation.stack import MyStack
def sort_stack(stack_sup):
    for i in range(stack_sup.size()):
        for j in range(i, stack_sup.size()):
            if stack_sup.stack[i]<stack_sup.stack[j]:
                temp=stack_sup.stack[i]
                stack_sup.stack[i]=stack_sup.stack[j]
                stack_sup.stack[j]=temp
    return stack_sup
if __name__=="__main__":
    stack_sup=MyStack()
    stack_sup.push(7)
    stack_sup.push(9)
    stack_sup.push(1)
    sort_stack(stack_sup)
    stack_sup.print_stack()
```

### Post-fix expression
We check each character of the string from left to right. If we find a digit, it is pushed into the stack.

If we find an operand, we pop two elements from the stack (there have to be at least two present or else this postfix expression is invalid) and solve the expression. The resulting value is pushed back into the stack.

The process continues until we reach the end of the string.

**Time Complexity**: $O(n)$
```python
from Stack_and_Queues.Implementation.stack import MyStack
def evaluate_post_fix(exp):
    stack = MyStack()
    try:
        for char in exp:
            if char.isdigit():
                # Push numbers in stack
                stack.push(char)
                stack.print_stack()
            else:
                # use top two numbers and evaluate
                right = stack.pop()
                left = stack.pop()
                ''' Using Python's eval () method that takes a str expression, 
                evaluates it and returns an integer '''
                stack.push(str(eval(left + char + right)))
        # final answer should be a number
        return int(float(stack.pop()))
    except TypeError:
        return "Invalid Sequence"
```
### Next Greater Element Using a Stack

**Brute Force**
```python
def next_greater(lst):
    temp=[]
    for i in range(len(lst)):
        sub_lst=lst[i+1:]
        find=False
        for j in sub_lst:
            if j>lst[i]:
                temp.append(j)
                find=True
                break
        if find==False:
            temp.append(-1)
    return temp
```

**Stack Iteration**
我们首先从尾部开始遍历列表，每次遍历，我们都可以检查一下我们的栈中是否有比目前遍历的元素大的数字
如果有，那么我们就取最外一层的元素作为比目前元素下一个更大的元素，这也是为什么我们需要从尾部开始遍历。如果目前的栈中没有比我们目前元素的大的数字，那么栈中所有元素都弹出去，并把目前的元素推入栈中。

Time Complexity:$O(n)$
```python
def next_greater_element(lst):
    stack = MyStack()
    res = [-1] * len(lst)
    # Reverse iterate list
    for i in range(len(lst) - 1, -1, -1):
        ''' While stack has elements and current element is greater 
        than top element, pop all elements '''
        stack.print_stack()
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()
        ''' If stack has an element, top element will be 
        greater than ith element '''
        if not stack.is_empty():
            res[i] = stack.peek()
        # push in the current element in stack
        stack.push(lst[i])
        print(res)
    return res
```

### Check Balanced Parentheses using Stack
我们首先声明一个列表：
``` python 
right=["}","]",")"]
```
然后我们遍历字符串，如果不在这个列表里面，我就将一个元素推入辅助栈。 假如说是闭环的话，那么久后续辅助栈每次弹出最外的元素应该和列表的元素对应，不然程序就终止，返回 **False**. 如果完全形成闭环，那么理论上来说，辅助栈应该为空。假如不为空，那就说明，有一个括号没有形成对应，那么程序就将返回 **False**.

Time Complexity: $O(n)$
```python
def is_balanced(exp):
    # Write your code here
    right=["}","]",")"]
    exp_lst=list(exp)
    stack=MyStack()
    for chr in exp_lst:
        if chr not in right:
            stack.push(chr)
        if chr in right:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if chr == "}" and top_element != "{":
                print(1)
                return False
            if chr == ")" and top_element != "(":
                print(2)
                return False
            if chr == "]" and top_element != "[":
                print(3)
                return False
    if not stack.is_empty():
        return False
    return True
```

### Min  Function Using a Stack

题目要求：
You have to implement the MinStack class which will have a min() function. Whenever min() is called, the minimum value of the stack is returned in O(1) time. The element is not popped from the stack. Its value is simply returned.
也就是说，当我执行min() 函数的时候，返回值所花费的时间是 O（1），那么我们最快的办法就是使外围的数据始终为最小值，那么这就要求我们，每次插入值需要判断所插入的值与目前栈中的值哪个更小，如果插入的更小，那么我们就把插入的值放在最外一层。否则就插入当前栈中最小的数。

```python
class MinStack:
    # Constructor
    def __init__(self):
        self.min_stack = MyStack()
        self.main_stack = MyStack()
    # Removes and returns value from min_stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()
    # Pushes values into min_stack
    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > value:
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())
    # Returns minimum value from newStack in O(1) Time
    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()
        # In case the stack is empty
        return None
```