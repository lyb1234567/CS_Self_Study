# O(n^2)
def find_two_number(lst,target):
    for i in range(len(lst)):
        temp=lst[i]
        for j in range(i+1,len(lst)):
            if (target-temp)== lst[j]:
                return [temp,lst[j]]

    return -1

#O(nlogn)
def binary_search(lst,target):
    small=0
    high=len(lst)-1
    mid=(small+high)//2
    while high>small+1:
        if lst[small]==target:
            return small
        elif lst[high]==target:
            return high
        if lst[mid]==target:
            return mid
        elif lst[mid]>target:
            high=mid
            print(high)
        elif lst[mid]<target:
            small=mid
        mid = (small + high)//2
    return -1

def find_sum(lst,target):
    lst.sort()
    for i in range(len(lst)):
        temp=target-lst[i]
        index=binary_search(lst,temp)
        if temp==lst[index]:
            return [lst[i],lst[index]]
    return -1
if __name__=="__main__":
    import random
    import timeit
    lst1 = [1, 21, 3, 14, 5, 20, 7, 6,61,65,98,67,53,87,98,101]
    k = 108
    start_normal = timeit.default_timer()
    print(find_two_number(lst1,k))
    stop_normal = timeit.default_timer()
    start_binary = timeit.default_timer()
    print(find_sum(lst1,k))
    stop_binary = timeit.default_timer()

    print("Brute Force:",stop_normal-start_normal)
    print("Binary:",stop_binary-start_binary)

