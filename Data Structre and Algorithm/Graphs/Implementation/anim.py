import numpy as np
import matplotlib.pyplot as plt
import time
plt.axis([0,50,60,80])
for i in np.arange(1,5):
    z = 68 + 4 * np.random.randn(50)
    zm = np.cumsum(z) / range(1,len(z)+1)
    plt.plot(zm)
    plt.show()
    time.sleep(1)
    plt.hold(True)

n = np.arange(1,51)
su = 68 + 4 / np.sqrt(n)
sl = 68 - 4 / np.sqrt(n)

plt.plot(n,su,n,sl)
