class Node:
    def __init__(self,val):
        self.val=val
        self.next_element=None
class linked_list:
    def __init__(self):
        self.head=None
    def insert(self,val):
        if not self.head:
            self.head=Node(val)
        else:
            temp=self.head
            while temp.next_element:
                temp=temp.next_element
            temp.next_element=Node(val)
    def display(self):
        if not self.head:
            print(None)
        if self.head and not self.head.next_element:
            print(self.head.val)
        else:
            temp=self.head
            while temp:
                if temp.next_element:
                    print(str(temp.val)+"->",end="")
                else:
                    print(str(temp.val)+"->None")
                temp=temp.next_element
    def find(self,key):
        count=0
        if not self.head:
            return -1
        else:
            temp=self.head
            while temp:
                if temp.val==key:
                    return count
                count+=1
                temp=temp.next_element
            return -1
    def search(self,index):
        pos=0
        if not self.head:
            return -1
        else:
            temp=self.head
            while temp:
                if pos==index:
                    return temp.val
                pos+=1
                temp=temp.next_element
            return -1
def Hashing(key,size):
    return key%size
def display_hash(store):
    count=0
    for i in store:
        if i:
            print("{0}:".format(count),end="")
            i[0].display()
            count+=1
        else:
            print("{0}:".format(count))
            count += 1
def find(store,key):
    size=len(store)
    index=Hashing(key,size)
    k=store[index][1].find(key)
    if k!=-1:
        return store[index][0].search(k)
    else:
        print("Key not in the hash table")
store=[None]*10
Value=['a','b','c','d','e','f','k','sad','sada','sad']
key=[1,3,10,20,11,18,6,7,9,13]
for k in key:
    index=Hashing(k,len(store))
    if not store[index]:
        temp=[]
        hash_value=linked_list()
        hash_value.insert(Value.pop(0))
        temp.append(hash_value)
        hash_key=linked_list()
        hash_key.insert(k)
        temp.append(hash_key)
        store[index]=temp
    else:
        store[index][0].insert(Value.pop(0))
        store[index][1].insert(k)

for k in key:
    value=find(store,k)
    print("Key {0}:{1}".format(k,value))