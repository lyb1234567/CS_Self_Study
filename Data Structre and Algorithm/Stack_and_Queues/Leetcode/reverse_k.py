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