import numpy as np

# Python List
a = np.array([1, 2, 3, 4, 5])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype.name)

print('--------')

b = np.array([
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [4, 3, 2, 1, 0],
])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype.name)

print('--------')

c = np.array([
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
])
print(c)
print(c.ndim)
print(c.shape)
print(c.size)
print(c.dtype.name)
