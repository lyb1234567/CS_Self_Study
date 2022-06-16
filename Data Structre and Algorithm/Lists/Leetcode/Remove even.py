def remove_even_number(lst):
    temp=[]
    for i in range(len(lst)):
        if lst[i] % 2!=0:
            temp.append(lst[i])
    return temp
if __name__=="__main__":
    lst=[1,2,3,4,5,6,7,8,9,10]
    lst=remove_even_number(lst)
    print(lst)