import numpy as np

# np.arange(startNum, stopNum, step)  <-> rang(startNum, stopNum, step)
a = np.arange(1, 10)
print(a)

# arange is sort order to reshape; the arange size must satisfy to reshape
b = np.arange(0, 10).reshape(2, 5)
print(b)
# 3d array
c = np.arange(24).reshape(2, 3, 4)
print(c)

# random function create ndarray
d = np.random.randn(3, 2)
print(d)
e = np.random.randn(3, 2, 4)
print(e)

print('-------------------')

# arange create & operation
# create
arrayOP = np.arange(12).reshape(3, 4)
print(arrayOP)
print(arrayOP.shape)
print(arrayOP.ndim)
print(arrayOP.size)
# operation
print(arrayOP + 1)
print(arrayOP ** 2)
