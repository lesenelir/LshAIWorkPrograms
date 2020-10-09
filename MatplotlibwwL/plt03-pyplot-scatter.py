import matplotlib.pyplot as plt

# prepare x y value
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 6]

# draw a scatter pic
plt.scatter(x, y, label='scatterLabel', color='blue', s=25)

plt.legend()

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Graph')

plt.show()
