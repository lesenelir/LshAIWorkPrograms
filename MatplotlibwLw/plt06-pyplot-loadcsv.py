import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file_name = '../Numpy&PandaswLw/csv_file/TestPandas.csv'

x, y = pd.read_csv(file_name, delimiter=',', unpack=True)
plt.plot(x, y)

plt.show()
