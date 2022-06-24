from Stack_and_Queues.Implementation.stack import MyStack

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

if __name__ == "__main__" :
    stack = MinStack()
    stack.push(5)
    stack.push(0)
    stack.push(-1)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(0)
    print("Main stack:", stack.main_stack.stack)
    print("Min stack:", stack.min_stack.stack)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    stack.push(-2)
    print("Main stack:", stack.main_stack.stack)
    print("Min stack:", stack.min_stack.stack)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    print("Main stack:", stack.main_stack.stack)
    print("Min stack:", stack.min_stack.stack)
    print("Minimum value: " + str(stack.min()))
