def second_max(lst):
    first = float("-inf")
    second = float("-inf")
    for i in range(len(lst)):
        if first <= lst[i]:
            first = lst[i]

    print(first)
    lst.remove(first)
    for j in lst:
        if second <= j:
            second = j
    return second


if __name__ == "__main__":
    lst = [9, 2, 3, 6]
    print(second_max(lst))
