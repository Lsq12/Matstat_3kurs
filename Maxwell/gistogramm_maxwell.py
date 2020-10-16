import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import maxwell



def CDF(array, ret):
    r = list()
    s = set(array)

    for i in st:
        r.append(np.count_nonzero(array == i))

    plt.bar(sorted(s),height=r)


def maxw(size = None):

    vx = np.random.normal(0, 9, size=size)
    vy = np.random.normal(0, 9, size=size)
    vz = np.random.normal(0, 9, size=size)
    return np.sqrt(vx*vx + vy*vy + vz*vz)


n = 10**5
mdata = maxw(n)

x = np.linspace(0.0, 40.0, 100)

CDF(mdata, x)
plt.title("Maxwell")
plt.show()