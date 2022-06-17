def find_max_sublist(lst):
    temp=[]
    if len(lst)<1:
        return -1
    else:
        cur_max=lst[0]
        global_max=lst[0]
        for i in range(1,len(lst)):
            if cur_max<0:
                cur_max=lst[i]
            else:
                cur_max=cur_max+lst[i]
            if global_max<cur_max:
                global_max=cur_max
        return global_max


if __name__=="__main__":
    lst=[-4,2,-5,1,2,3,6,-5,1]
    print(find_max_sublist(lst))