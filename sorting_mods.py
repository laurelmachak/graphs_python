import matplotlib.pyplot as plt
from random import shuffle
from time import sleep

plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

def display_bar_chart(array):
    plt.clf()
    plt.bar(range(len(array)), array)
    plt.pause(0.0001)
