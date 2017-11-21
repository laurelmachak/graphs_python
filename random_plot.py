import matplotlib.pyplot as plt
from time import sleep
from random import shuffle

# turn on interactive plotting
plt.ion()

y = [i for i in range(100)]
x = [i for i in range(len(y))]

# use a loop to update the graph and keep shuffling
# the y list around so that the values keep changing

for i in range(20):
    plt.clf() ## clear the plot
    plt.bar(x,y) ## plot a bar chart
    #plt.draw() ## draw the bar chart
    plt.pause(0.0001)
    sleep(0.5) ## pause for 1/2 second
    shuffle(y) ## shuffle the data
