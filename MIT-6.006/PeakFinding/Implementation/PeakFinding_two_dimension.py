
import numpy as np
def slice_column(lst,index):
    if len(lst)<=1:
        return lst[lst[0][index]]
    else:
        temp=[]
        for i in range(len(lst)):
            temp.append(lst[i][index])
        return temp

def slice_column_multiple(lst,start,stop):
    if len(lst)<=1:
        return lst[start:stop]
    else:
        temp=[]
        for i in range(len(lst)):
            temp.append(lst[i][start:stop+1])
        return temp
def array_to_lst(lst):
    temp=[]
    for i in range(len(lst)):
        temp.append(lst[i][0])
    return temp

def peak_finder_binary(lst):
    sub_lst=lst[0]
    support_lst=lst
    length=len(sub_lst)
    middle=(len(sub_lst)-1)>>1
    low=0
    high=len(sub_lst)-1
    find_peak=False
    peak=[]
    while middle>=low and middle<=high:
        temp=slice_column(lst,middle)
        temp_max=max(temp)
        temp_max_index=temp.index(temp_max)
        sublist=lst[0]
        if len(sublist)==1:
            lst=array_to_lst(lst)
            peak.append(max(lst))
            return peak
        if lst[temp_max_index][middle]>=lst[temp_max_index][middle-1] and lst[temp_max_index][middle]>=lst[temp_max_index][middle+1]:
            peak.append(lst[temp_max_index][middle])
            break
        elif lst[temp_max_index][middle]<lst[temp_max_index][middle-1]:
            if middle==0:
                middle = middle + 1
                lst = slice_column_multiple(lst, middle, high)
                temp_list = lst[0]
                high = len(temp_list) - 1
                middle = high >> 1
                continue
            middle=middle-1
            lst=slice_column_multiple(lst,low,middle)
            temp_lst=lst[0]
            middle=len(temp_lst)-1
        elif lst[temp_max_index][middle]<lst[temp_max_index][middle+1]:
            middle=middle+1
            lst = slice_column_multiple(lst, middle,high)
            temp_list=lst[0]
            high=len(temp_list)-1
            middle=high>>1
    return peak

def peak_finder_noraml(lst):
    peak=[]
    for i in range(len(lst)):
        sublst=lst[i]
        for j in range(len(sublst)):
            if i==0 and j==0:
                if lst[i][j]>=lst[i+1][j] and lst[i][j]>=lst[i][j+1]:
                    peak.append(lst[i][j])
                    return peak
            if i==0 and j==len(lst[0])-1:
                if lst[i][j] >= lst[i + 1][j] and lst[i][j] >= lst[i][j-1]:
                    peak.append(lst[i][j])
                    return peak
            if i==len(lst)-1 and j==0:
                if lst[i][j] >= lst[i-1][j] and lst[i][j] >= lst[i][j+1]:
                    peak.append(lst[i][j])
                    return peak
            if i==len(lst)-1 and j==len(lst[0])-1:
                if lst[i][j] >= lst[i-1][j] and lst[i][j] >= lst[i][j-1]:
                    peak.append(lst[i][j])
                    return peak
            if i==0 and j>0 and j<len(lst[0])-1:
                if lst[i][j]>=lst[i][j+1] and lst[i][j]>=lst[i][j-1] and lst[i][j]>=lst[i+1][j]:
                    peak.append(lst[i][j])
                    return peak
            if i==len(lst)-1 and j>0 and j<len(lst[0])-1:
                if lst[i][j]>=lst[i][j+1] and lst[i][j]>=lst[i][j-1] and lst[i][j]>=lst[i-1][j]:
                    peak.append(lst[i][j])
                    return peak
            if i>0 and i<len(lst)-1 and j>0 and j<len(lst[0])-1:
                if lst[i][j] >= lst[i][j + 1] and lst[i][j] >= lst[i][j - 1] and lst[i][j] >= lst[i - 1][j] and lst[i][j]>=lst[i+1][j]:
                    peak.append(lst[i][j])
                    return peak
            if j==0 and i>0 and i<len(lst)-1:
                if lst[i][j]>=lst[i+1][j] and lst[i][j]>=lst[i-1][j] and lst[i][j]>=lst[i][j+1]:
                    peak.append(lst[i][j])
                    return peak
            if j==len(lst[0])-1 and i>0 and i<len(lst)-1:
                if lst[i][j]>=lst[i+1][j] and lst[i][j]>=lst[i-1][j] and lst[i][j]>=lst[i][j-1]:
                    peak.append(lst[i][j])
                    return peak
    return peak

if __name__=="__main__":
    import timeit
    import math
    lst=[[10,8,10,10],[14,13,12,11],[15,9,11,19],[16,17,19,20],[21,22,23,24],[25,27,26,28]]
    start_normal = timeit.default_timer()
    print(peak_finder_noraml(lst))
    stop_noraml = timeit.default_timer()

    start_binary_search = timeit.default_timer()
    print(peak_finder_binary(lst))
    stop_binary_search = timeit.default_timer()

    print("The normal peak finder will cost:{0} ms".format(math.ceil((stop_noraml - start_normal) * 1e6)))
    print("The binary search peak finder will cost:{0} ms".format(
        math.ceil((stop_binary_search - start_binary_search) * 1e6)))

