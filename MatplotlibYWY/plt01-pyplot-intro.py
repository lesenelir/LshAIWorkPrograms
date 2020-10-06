import matplotlib.pyplot as plt

# plot operation

# prepare x y values
x1 = [1, 2, 3]
y1 = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

# draw a pic
plt.plot(x1, y1, label='First Line')
plt.plot(x2, y2, label='Second Line')

# add text description
plt.xlabel('plot number')
plt.ylabel('important var')
plt.title('Simple Test Graph')

plt.legend()
plt.show()

