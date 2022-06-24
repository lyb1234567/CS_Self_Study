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
if __name__ == "__main__" :
    queue_obj = MyQueue()
    print("queue.enqueue(2);")
    queue_obj.enqueue(2)
    print("queue.enqueue(4);")
    queue_obj.enqueue(4)
    print("queue.enqueue(6);")
    queue_obj.enqueue(6)
    print("queue.enqueue(8);")
    queue_obj.enqueue(8)
    print("queue.enqueue(10);")
    queue_obj.enqueue(10)

    queue_obj.print_lst()

    print("is_empty(): " + str(queue_obj.is_empty()))
    print("front(): " + str(queue_obj.front()))
    print("rear(): " + str(queue_obj.rear()))
    print("size(): " + str(queue_obj.size()))
    print("Dequeue(): " + str(queue_obj.dequeue()))
    print("Dequeue(): " + str(queue_obj.dequeue()))
    print("queue.enqueue(12);")
    queue_obj.enqueue(12)
    print("queue.enqueue(14);")
    queue_obj.enqueue(14)

    while queue_obj.is_empty() is False:
        print("Dequeue(): " + str(queue_obj.dequeue()))
        queue_obj.print_lst()

    print("is_empty(): " + str(queue_obj.is_empty()))

