
from Implementation.MinHeap import MinHeap
def find_k_smallest_element(lst,k):
    minheap=MinHeap()
    minheap.buildHeap(lst)
    ans=[]
    for i in range(k):
        ans.append(minheap.getMin())
        minheap.removeMin()
    return ans




lst = [9,4,7,1,-2,6,5]
k =7
print(find_k_smallest_element(lst,k))
