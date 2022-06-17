def Rearrange_(lst):
    temp=[]
    k=0
    d=0
    for i  in range(len(lst)):
        a = lst[0 + k]
        b = lst[-1 - d]
        if i%2==0:
            temp.append(b)
            d=d+1
        elif i%2==1:
            temp.append(a)
            k=k+1
    return temp

if __name__=="__main__":
    lst = [1, 2, 3,4,5,6,7]
    print(Rearrange_(lst))