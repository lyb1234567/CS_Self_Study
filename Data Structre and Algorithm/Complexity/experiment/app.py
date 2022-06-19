import random
import matplotlib.pyplot as plt

"""
冒泡排序，每个元素每一轮遍历之中两两比较，进行交换，复杂度为O(N^2)
"""


def bubble(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst


def insertion_sort_ascedning(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        # 从当前位置前面n-1个元素开始遍历，每当发现前面一个元素笔记大，那么就进行，直到前面的元素比自己小，然后跳出循环
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j = j - 1
        # 在此插入迭代元素
        lst[j + 1] = key
    return lst


if __name__ == "__main__":
    lst = []
    x = [100, 1000, 10000]
    y1 = []
    y2 = []
    import timeit

    for n in range(len(x)):
        for i in range(x[n]):
            lst.append(random.randint(1, x[n]))
        start_bubble = timeit.default_timer()
        lst_bubble = bubble(lst)
        stop_bubble = timeit.default_timer()
        start_insert = timeit.default_timer()
        lst_insert = insertion_sort_ascedning(lst)
        stop_insert = timeit.default_timer()
        y1.append(stop_bubble - start_bubble)
        y2.append(stop_insert - start_insert)

    print(y1)
    print(y2)

    plt.plot(x, y1, x, y2)
    plt.xlabel("n")
    plt.ylabel("time(s)")
    plt.legend(["Bubble Sorting", "Quick Sorting"])
    plt.savefig("Comparison.png")
    plt.show()
