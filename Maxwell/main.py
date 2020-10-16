import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import maxwell


def kv(arr, kvant):

    s1 = set(arr)
    s = sorted(s1)

    r = list()
    ss = len(arr)
    current = 0
    pp = 0

    for i in s:
        current += np.count_nonzero(arr == i) / ss
        if current > kvant:
            return pp
        r.append(current)
        pp = i

    return pp


def maxw(size = None):

    vx = np.random.normal(0, 9, size=size)
    vy = np.random.normal(0, 9, size=size)
    vz = np.random.normal(0, 9, size=size)
    return np.sqrt(vx*vx + vy*vy + vz*vz)


n = 10**5
mdata = maxw(n)

h, bins = np.histogram(mdata, bins = 101, range=(0.0, 40.0))

x = np.linspace(0.0, 40.0, 100)
rv = maxwell(0, 9)

fig, ax = plt.subplots(1, 1)

ax.hist(mdata, bins = bins, density=True)
ax.step(x, rv.pdf(x), 'k-', lw=2, label='Maxwell pdf')
plt.title("Maxwell")
plt.show()


print(kv(mdata, 0.7))
for i in range(5):
     print('n = ', sorted(set(maxw(10))))
