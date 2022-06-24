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
        if self.is_empty():
            return None
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

if __name__ == "__main__" :
    stack_obj = MyStack()
    print("is_empty(): " + str(stack_obj.is_empty()))
    print("peek(): " + str(stack_obj.peek()))
    print("size(): " + str(stack_obj.size()))

    for i in range(5):
        stack_obj.push(i)
    stack_obj.print_stack()

    stack_obj.pop()
    stack_obj.pop()
    stack_obj.print_stack()