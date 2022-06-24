from Stack_and_Queues.Implementation.stack import MyStack


def next_greater(lst):
    temp=[]
    for i in range(len(lst)):
        sub_lst=lst[i+1:]
        find=False
        for j in sub_lst:
            if j>lst[i]:
                temp.append(j)
                find=True
                break
        if find==False:
            temp.append(-1)
    return temp

def next_greater_element(lst):
    stack=MyStack()
    temp=[-1]*len(lst)
    for i in range(len(lst)-1,-1,-1):
        #当目前栈不为空，且栈最外的元素都比目前的元素大，就需要将栈中的元素弹出
        while stack.is_empty() is not True and stack.peek()<=lst[i]:
            stack.pop()

        #上述元素会将栈中比目前小的元素全部弹出，栈此时不为空，这就证明，此时栈中有满足条件的元素，那么这就是我们要找的元素，我们就可以将它放到temp中
        if stack.is_empty() is not True:
            temp[i]=stack.peek()

        stack.push(lst[i])
    return temp
if __name__=="__main__":
    lst = [4, 6, 3, 2, 8, 1]
    print(next_greater_element(lst))
