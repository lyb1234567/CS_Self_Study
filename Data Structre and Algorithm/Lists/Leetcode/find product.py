import copy
def find_product(lst):
    temp=[]
    for i in range(len(lst)):
        temp_lst=copy.deepcopy(lst)
        temp_lst.remove(lst[i])
        temp_remove=temp_lst
        product=1
        for j in range(len(temp_remove)):
            product=product*temp_remove[j]
        temp.append(product)
    return temp
if __name__=="__main__":
    arr = [4,2,1,5,0]
    b=arr
    b.remove(2)
    print(arr)