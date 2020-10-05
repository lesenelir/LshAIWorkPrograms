import pandas as pd

# merge operation

# 1.create dataframe from python dictionary
data1 = {
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3'],
    'E': ['E0', 'E1', 'E2', 'E3'],
}
df1 = pd.DataFrame(data1)
print(df1)

# 2.create dataframe only through pandas
df2 = pd.DataFrame({
    'A': ['A4', 'A5', 'A6', 'A7'],
    'B': ['B4', 'B5', 'B6', 'B7'],
    'C': ['C4', 'C5', 'C6', 'C7'],
    'D': ['D4', 'D5', 'D6', 'D7'],
    'F': ['F4', 'F5', 'F6', 'F7'],
})
print(df2)

# 3.use concat function to merge dataframe
print(pd.concat([df1, df2]))
# join参数默认是outer join此时包含所有的行列，innerjoin会过滤合并dataframe共同没有的行列
print(pd.concat([df1, df2], ignore_index=True, join='inner'))

# 4.add columns
# add one column
s1 = pd.Series(list(range(4)), name='F')
print(pd.concat([df1, s1], axis=1))
# add various different columns
s2 = df1.apply(lambda x: x['A'] + '_GG', axis=1)
print(s2)
print(pd.concat([df1, s1, s2], axis=1))

# 5.use append function to merge dataframe rows
dataf1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print(dataf1)
dataf2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
print(dataf2)
# append function
print(dataf1.append(dataf2))
