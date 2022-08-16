from Implementation.MaxHeap import MaxHeap
def minHeapify(heap, index):
    left=(2*index)+1
    right=(2*index)+2
    smallest=index
    if len(heap)>left and heap[left]<heap[smallest]:
        smallest=left
    if len(heap)>right and heap[right]<heap[smallest]:
        smallest=right
    if smallest!=index:
        temp=heap[smallest]
        heap[smallest]=heap[index]
        heap[index]=temp
        minHeapify(heap,smallest)
    return heap
#O(logn)
def convertMax(maxHeap):
    for i in range(len(maxHeap)//2,-1,-1):
        print(i)
        maxHeap = minHeapify(maxHeap, i)
        print(maxHeap)
    return maxHeap
maxHeap = [9, 4, 7, 1, -2, 6, 5]
convertMax(maxHeap)