from random import *
import numpy as np
import matplotlib.pyplot as plt

def CDF(array):
    r = np.zeros(2)

    for i in array:
        if i == 0.55:
            r[0] += 1
        else:
            r[1] += 1

    print(sorted(set(array)))
    print(r)
    plt.hist(sorted(set(array)), weights=r)
    plt.show()

n = 10

array = np.zeros(n)

p = 0.45
q = 0.55

for i in range(n):
    a = random()
    if a <= p:
        array[i] = p
    else:
        array[i] = q
CDF(array)