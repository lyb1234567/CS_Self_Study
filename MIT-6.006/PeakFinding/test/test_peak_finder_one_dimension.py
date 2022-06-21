from Implementation.PeakFinding_one_dimension import peak_finder_normal,peak_finder_binary_search

if __name__=="__main__":
    import timeit
    import math
    import matplotlib.pyplot as plt
    import os
    n = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    noraml_time=[]
    binary_time=[]
    for j in range(len(n)):
        lst=[i for i in range(n[j])]
        lst[len(lst)-2]=lst[len(lst)-2]+10
        start_normal = timeit.default_timer()
        print(peak_finder_normal(lst))
        stop_noraml=timeit.default_timer()

        start_binary_search = timeit.default_timer()
        print(peak_finder_binary_search(lst))
        stop_binary_search = timeit.default_timer()

        noraml_time. append(math.ceil((stop_noraml-start_normal)*1e6))
        binary_time.append(math.ceil((stop_binary_search - start_binary_search) * 1e6))
        print("The normal peak finder will cost:{0} ms".format(math.ceil((stop_noraml-start_normal)*1e6)))
        print("The binary search peak finder will cost:{0} ms".format(math.ceil((stop_binary_search - start_binary_search) * 1e6)))
        print("\n\n")
    plt.plot(n, noraml_time, n, binary_time)
    plt.xlabel("n")
    plt.ylabel("time(ms)")
    plt.legend(["Normal Peak Finder", "Binary Search Peak Finder"])
    plt.savefig("image\Experiement.png")
    plt.show()
