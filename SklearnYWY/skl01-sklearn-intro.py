import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 特征矩阵data 预测结果向量target(price)
# X特征矩阵 y标签
# 1.get data
data, target = datasets.load_boston(return_X_y=True)

# ndarray
print(type(data))
print(type(target))

# show  shape
print(data.shape)  # (506, 13) 506行 13列
print(target.shape)  # (506,) target一维数组 506条 13个特征

# show the first three home feature information & target(price) information
print(data[:3])
print(target[:3])

# 2.split train test
X_train, X_test, y_train, y_test = train_test_split(data, target)

print(X_train.shape)  # (379, 13)
print(y_train.shape)  # (379,)

print(X_test.shape)  # (127, 13)
print(y_test.shape)  # (127,)

# 3.train model
clf = LinearRegression()  # create object
clf.fit(X_train, y_train)
print(clf.score(X_train, y_train))

# 4.predict data
print(clf.score(X_test, y_test))
# 预测结果
print(clf.predict(X_test[:3]))
# 实际结果
print(y_test[:3])
