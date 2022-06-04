import matplotlib.pyplot as plt
import numpy as np
import random
x1=[]
x2=[]

for i in range(1000):
    x1.append(i)

for i in range(50):
    x2.append(x1[i]+random.randint(20,30))

for n in range(50,1000):
    x2.append(x1[n]-random.randint(20,30))
y=np.linspace(1,1000,1000)
print(len(x2))
plt.plot(y,x1,y,x2)
plt.show()