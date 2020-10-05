import pandas as pd
import numpy as np

file_path = "csv_file/TestPandas.csv"
data = pd.read_csv(file_path)
print(data)

# check data
print(data.head())
# check data shape and return rows & cols
print(data.shape)
# check index columns
print(data.index)
# check columns name
print(data.columns)
# check type of csv data
print(data.dtypes)
