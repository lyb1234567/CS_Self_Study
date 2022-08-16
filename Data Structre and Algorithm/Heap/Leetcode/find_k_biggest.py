from Implementation.MaxHeap import MaxHeap
def find_k_biggest_element(lst,k):
    maxheap = MaxHeap()
    maxheap.buildHeap(lst)
    ans=[]
    for i in range(k):
        ans.append(maxheap.getMax())
        maxheap.removeMax()
    return ans
lst = [9,4,7,1,-2,6,5]
k =3
print(find_k_biggest_element(lst,k))