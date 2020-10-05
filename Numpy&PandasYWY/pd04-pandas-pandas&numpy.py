import numpy as np
import pandas as pd

# 1.numpy to pandas
# 1.1 numpy one-dimensional array to pandas Series
arr1 = np.arange(10)
print(arr1)
series = pd.Series(arr1)
print(series)

# 1.2 numpy second-dimensional array to pandas DataFrame
arr2 = np.random.randint(1, 10, size=(5, 4))
print(arr2)
df = pd.DataFrame(arr2, columns=["ca", "cb", " cc", "cd"])
print(df)

# 2.pandas to numpy
# 2.1 pandas Series to numpy array
s = pd.Series(range(10))
print(s)
# method one: series to numpy array
print(s.values)
print(s.values.ndim)
print(s.values.shape)
print(s.values.size)
# method two: series to numpy array
print(s.to_numpy())

# 2.2 pandas DataFrame to numpy array
dataframe = pd.DataFrame(
    [
        [11, 12.2, 13],
        [12, 19.2, 14],
        [13, 18.2, 15],
        [14, 17.2, 16],
    ],
    columns=["feature_a", "feature_b", "feature_c"],
)
print(dataframe)
# method one: dataframe to numpy array
print(dataframe.values)
print(dataframe.values.ndim)
print(dataframe.values.shape)
print(dataframe.values.size)
# method two: dataframe to numpy array
print(dataframe.to_numpy())

