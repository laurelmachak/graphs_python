import matplotlib.pyplot as plt

y = [i for i in range(20,100,3)]
x = [i for i in range(len(y))]

#plt.scatter(x,y)
#plt.plot(x,y)
plt.bar(x,y)
plt.show()
