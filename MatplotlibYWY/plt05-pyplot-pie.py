import matplotlib.pyplot as plt

# prepare data values

sclices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']

# draw a pic
plt.pie(sclices,labels=activities,autopct='%1.1f%%')

plt.title('Pie Graph')
plt.show()