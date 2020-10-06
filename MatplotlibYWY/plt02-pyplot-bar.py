import matplotlib.pyplot as plt

# prepare x y value
x1 = [1, 3, 5, 7, 9]
y1 = [5, 2, 7, 8, 2]

x2 = [2, 4, 6, 8, 10]
y2 = [8, 6, 2, 5, 6]

# draw a bar pic
plt.bar(x1, y1, label='Example One', color='red')
plt.bar(x2, y2, label='Example Two', color='pink')

plt.legend()  # show legend

plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Bar Graph')

plt.show()
