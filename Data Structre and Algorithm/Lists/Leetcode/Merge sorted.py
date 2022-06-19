def Merge_sorted_lst(lst1, lst2):
    len1 = len(lst1)
    len2 = len(lst2)
    temp = []
    a = 0
    b = 0
    while (a < len1) and (b < len2):
        if lst1[a] <= lst2[b]:
            temp.append(lst1[a])
            a = a + 1
        else:
            temp.append(lst2[b])
            b = b + 1
    if a >= len1:
        temp_new = lst2[b:]
        temp = temp + temp_new
    elif b >= len2:
        print(a)
        temp_new = lst1[a:]
        temp = temp + temp_new
    return temp


if __name__ == "__main__":
    lst1 = [1, 3, 4, 7, 21, 23, 24, 251, 321]
    lst2 = [2, 8, 10, 11, 180, 190, 200]
    print(Merge_sorted_lst(lst1, lst2))
