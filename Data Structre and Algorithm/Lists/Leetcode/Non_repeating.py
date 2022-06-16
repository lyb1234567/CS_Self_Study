def find_non_repeating(lst):
    dict={}
    set_lst=set(lst)
    lst_new=list(set_lst)
    temp=[]
    for i in range(len(set_lst)):
        dict[lst_new[i]]=0

    for i in range(len(lst)):
        dict[lst[i]]=dict[lst[i]]+1

    for j in range(len(lst)):
        if dict[lst[j]]==1:
           return lst[j]




if __name__=="__main__":
    lst=[4,5,1,2,0,4]
    print(find_non_repeating(lst))