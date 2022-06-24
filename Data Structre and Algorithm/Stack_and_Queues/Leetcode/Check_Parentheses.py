from Stack_and_Queues.Implementation.stack import MyStack
def is_balanced(exp):
    # Write your code here
    right=["}","]",")"]
    exp_lst=list(exp)
    stack=MyStack()
    for chr in exp_lst:
        if chr not in right:
            stack.push(chr)
        if chr in right:
            if stack.is_empty():
                return False
            top_element = stack.pop()
            if chr == "}" and top_element != "{":
                print(1)
                return False
            if chr == ")" and top_element != "(":
                print(2)
                return False
            if chr == "]" and top_element != "[":
                print(3)
                return False
    if not stack.is_empty():
        return False
    return True

if __name__=="__main__":
    # Example 1
    input_string = "{[()]}"  # balanced string
    result = str(is_balanced(input_string))
    print("Input string \"" + input_string + "\" is balanced: " + result)