from stack import MyStack
from queue import MyQueue
def binary_converter(n):
    sup_queue=MyQueue()
    res=[]
    if n==0:
        return None
    else:
        sup_queue.enqueue("1")
        for i in range(n):
          res.append(sup_queue.dequeue())
          s1=res[i]+"0"
          s2=res[i]+"1"
          sup_queue.enqueue(s1)
          sup_queue.enqueue(s2)
        return res

def evaluate_post_fix(exp):
    stack = MyStack()
    try:
        for char in exp:
            if char.isdigit():
                # Push numbers in stack
                stack.push(char)
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
def Next_Greater(lst):
    stack=MyStack()
    res=[-1]*len(lst)
    for i in range(len(lst)-1,-1,-1):
        while not stack.is_empty() and stack.peek()<=lst[i]:
            stack.pop()
        if not stack.is_empty():
            res [i]=stack.peek()

        stack.push(lst[i])
    return res
def is_balanced(exp):
    right=["}","]",")"]
    stack=MyStack()
    for char in exp:
        if char not in right:
            stack.push(char)
        if char in right:
            if char=="}" and stack.peek()!="{":
                return False
            if char== "]" and stack.peek()!="[":
                return False
            if char== ")" and stack.peek()!="(":
                return False
            stack.pop()
    if not stack.is_empty():
        return False
    return True

if __name__=="__main__":
    print(binary_converter(5))
    print(Next_Greater([4, 6, 3, 2, 8, 1]))
    print(is_balanced("{}"))