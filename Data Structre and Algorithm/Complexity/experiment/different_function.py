import random
import matplotlib.pyplot as plt
import numpy as np

number = np.linspace(1, 10, 10)

x1 = number
x2 = np.power(number, 2)
x3 = np.power(number, 3)
x4 = np.ones(10)
x5 = np.multiply(np.log2(number), number)
x6 = np.log2(number)
x7 = np.power(2, number)


plt.plot(
    number, x1, number, x2, number, x3, number, x4, number, x5, number, x6, number, x7
)
plt.xlabel("n")
plt.ylabel("f(n)")
plt.title("Comparison of increasing rate")
plt.legend(["linear", "power 2", "power 3", "constant", "nlogn", "logn", "a^n"])
plt.savefig("image/Experiement.png")
plt.show()
