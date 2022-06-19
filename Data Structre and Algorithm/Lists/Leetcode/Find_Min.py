def fin_min(lst):
    min = lst[0]
    for i in range(len(lst)):
        if min >= lst[i]:
            min = lst[i]
    return min


if __name__ == "__main__":
    lst = [1, 3, 2, 7, 10, -1]
    print(fin_min(lst))
