import numpy as np

# 索引
# select operation
a = np.arange(20).reshape(4, 5)
print(a)
print(a[0][4])  # select one data
print(a[2])  # select one row
print(a[:-1])  # select multi row, but no include last row
print(a[:, 2])  # first step: select all row and then, select col numbers

print('----------------')

# 合并
# merge row data array operation
data1 = np.arange(6).reshape(2, 3)
data2 = np.random.randint(10, 20, size=(4, 3))
print(data1)
print(data2)
# method one: np.concatenate([array1, array2])
print(np.concatenate([data1, data2]))
# method two: np.vstack([array1, array2])
print(np.vstack([data1, data2]))
# method three: np.row_stack([array1, array2])
print(np.row_stack([data1, data2]))

# merge col data operation
array1 = np.arange(12).reshape(3, 4)
array2 = np.random.randint(10, 20, size=(3, 2))
print(array1)
print(array2)
# method one: np.concatenate([array1, array2], axis=1)
print(np.concatenate([array1, array2], axis=1))
# method two: np.hstack([array1, array2])
print(np.hstack([array1, array2]))
# method three: np.column_stack([array1, array2])
print(np.column_stack([array1, array2]))

print('----------------')

# 分割
# split data array operation
A = np.arange(20).reshape(4, 5)
print(A)
C = np.split(A, 2)  # 平均分割
print(C)
D = np.array_split(A, 3, axis=0) # 不平均分割
print(D)
