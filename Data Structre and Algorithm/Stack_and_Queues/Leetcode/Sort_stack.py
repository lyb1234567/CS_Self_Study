from Stack_and_Queues.Implementation.stack import MyStack

def sort_stack(stack_sup):
    for i in range(stack_sup.size()):
        for j in range(i, stack_sup.size()):
            if stack_sup.stack[i]<stack_sup.stack[j]:
                temp=stack_sup.stack[i]
                stack_sup.stack[i]=stack_sup.stack[j]
                stack_sup.stack[j]=temp
    return stack_sup
if __name__=="__main__":
    stack_sup=MyStack()
    stack_sup.push(7)
    stack_sup.push(9)
    stack_sup.push(1)
    sort_stack(stack_sup)
    stack_sup.print_stack()
