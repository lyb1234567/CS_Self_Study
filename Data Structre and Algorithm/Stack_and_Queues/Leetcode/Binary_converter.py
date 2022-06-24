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




if __name__=="__main__":
    print(find_bin(5))


