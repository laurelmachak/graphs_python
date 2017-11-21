import matplotlib.pyplot as plt
from random import shuffle
from time import sleep
import matplotlib as mpl

plt.ion()
mpl.rcParams['lines.color'] = '#dee7e8'
plt.style.use('dark_background')

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

def display_bar_chart(array):
    plt.clf()
    plt.bar(range(len(array)), array)
    plt.pause(0.0001)

def display_scatter_chart(array):
    plt.clf()
    plt.scatter(range(len(array)), array)
    plt.pause(0.0001)

def display_plot_chart(array):
    plt.clf()
    plt.plot(range(len(array)), array)
    plt.pause(0.0001)
