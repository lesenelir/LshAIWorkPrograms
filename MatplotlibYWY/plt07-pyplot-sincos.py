import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 6, 0.1) # start0 stop6 step0.1
# if no step --> polyline

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, label='cos', color='blue')

plt.legend()
plt.show()
