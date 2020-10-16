import numpy as np
import matplotlib.pyplot as plt


n = [5, 10, 100, 1000, 10**5]

def fun(x, p):
    if x <= 0:
        return 0
    if x > 0 and x <= 1:
        return 1-p
    if x >= 1:
        return 1

def CDF():
    stepp = 0.1
    xlist = np.arange(0, 2, stepp)
    ylist = [fun(x, 0.45) for x in xlist]
    plt.step(xlist, ylist, label='cdf', color='red')

def cdf_ex(array):
    r = list()
    size = len(array)
    current = 0

    setted = set(array)
    sort_arr = sorted(setted)

    print(sort_arr)

    for i in sort_arr:
        current += np.count_nonzero(array == i) / size
        r.append(current)

    p = np.array(list(setted));
    p.sort()
    r.insert(0, 0)
    print(len(p))
    p = np.insert(p, 0, 0)
    print(r)
    print(p)

    plt.step(p, r, where='post', label='experiment')

p = 0.45
q = 1 - p
n = 10

arr = np.zeros(n)
for i in range(n):
        a = np.random.rand()
        if a <= p:
            arr[i] = 1
        else:
            arr[i] = 0

CDF()
cdf_ex(arr)
plt.legend()
plt.show()
