import pandas as pd
import numpy as np

# pandas dataframe and Series

# 1.Series
# 1.1 create Series
s1 = pd.Series([1, 'a', 2, 3.7])  # Series can create different data type
print(s1)
print(s1.index)
print(s1.values)

# 1.2 create Series corresponding different index
s2 = pd.Series([1, 'a', 2, 3.7], index=['z', 'x', 'y', 'm'])
print(s2)
print(s2.index)
print(s2.values)

# 1.3 create Series from python dictionary
sdic = {'name': 'lesenelir', 'sex': 'man', 'height': 180}
s3 = pd.Series(sdic)
print(s3)
print(s3.index)
print(s3.values)

# 2. get Series data
print(s2['z'])
print(type(s2['z']))
print(s2[['z', 'x']])
print(type(s2[['z', 'x']]))

print('-------------------------')

# 3.DataFrame
# 3.1 create dataframe from python dictionary
# 通过字典生成pandas的Series和DataFrame区别在于，Series字典value是值，DataFrame字典value是列表
data = {
    'state': ['ohio', 'ohio', 'nevada'],
    'year': [2000, 2001, 2002],
    'pop': [1.5, 1.7, 1.9],
}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
print(df.columns)
print(df.index)

# 3.2 get Series from DataFrame
# select one col return pd.Series
print(df['year'])
# select multi-cols return pd.DataFrame
print(df[['year', 'pop']])

# 4. use numpy with create pandas
array1 = np.array([1, 2, 3])
data1 = pd.Series(array1)
print(data1)
print(data1.index)
print(data1.values)
