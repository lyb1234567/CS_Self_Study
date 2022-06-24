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