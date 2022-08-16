class MaxHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,val):
        self.heap.append(val)
        self.__precolateup(len(self.heap)-1)
    def getMax(self):
        if self.heap:
            return self.heap[0]
    def removeMax(self):
        if len(self.heap)>=1:
            max=self.heap[0]
            self.heap[0]=self.heap[-1]
            del self.heap[-1]
            self.__maxHeapify(0)
            return max
        elif len(self.heap) == 1:
            max = self.heap[0]
            del self.heap[0]
            return max
        else:
            return None

    #This function will swap the values at parent-child nodes until the heap property is restored
    def __precolateup(self,index):
        parent=(index-1)//2
        if index<=0:
            return
        elif self.heap[parent] < self.heap[index]:
            tmp = self.heap[parent]
            self.heap[parent] = self.heap[index]
            self.heap[index] = tmp
            self.__precolateup(parent)
    #在我们删除堆的最大值的时候，我们也就是善除恶第一个点也就是heap[0]
    #也就是说，我们能从头节点开始，进行删除，先将头节点和最小的叶子节点进行互换，接着将新的头节点和其
    #左右节点进行比较，如果在左右节点中，选出一个最大的节点进行互换
    #如果此时左右节点均小于换好的头节点，那么递归结束，否则就继续
    def __maxHeapify(self, index):
        left = (index * 2) + 1
        right = (index * 2) + 2
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        #当左右节点均满足最大堆，那么就不需要进行交换节点了。
        if largest != index:
            tmp = self.heap[largest]
            self.heap[largest] = self.heap[index]
            self.heap[index] = tmp
            self.__maxHeapify(largest)

    def buildHeap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.__maxHeapify(i)
