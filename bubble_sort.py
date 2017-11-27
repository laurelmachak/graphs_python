import matplotlib.pyplot as plt
from random import shuffle
from time import sleep
import matplotlib as mpl
import sys

mpl.rcParams['lines.color'] = '#dee7e8'
plt.style.use('dark_background')
plt.ion()

def create_random_list(length):
    some_list = [i for i in range(length)]
    shuffle(some_list)
    return some_list

def display_bar_chart(array):
    plt.clf()
    plt.bar(range(len(array)), array)
    plt.pause(0.0001)

def bubble_sort(some_list):
    is_sorted = False
    while not is_sorted:
        swaps = False
        for i in range(len(some_list)-1):
            next_item = i + 1
            if some_list[i] > some_list[next_item]:
                some_list[i], some_list[next_item] = some_list[next_item], some_list[i]
                swaps = True
        display_bar_chart(some_list)
        sleep(0.2)
        if swaps == False:
            is_sorted = True
    return some_list

'''
example_list = create_random_list(20)
bubble_sort(example_list)
print(plt.style.available)
'''

if __name__ == "__main__":
    list_length = int(sys.argv[1])
    example_list = create_random_list(list_length)
    bubble_sort(example_list)
    print(plt.style.available)
