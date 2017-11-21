import sorting_mods as mod
#import sys

def single_item_insertion_sort(some_list, item_pos):
    i = item_pos
    while i > 0 and some_list[i-1] > some_list[i]:
        some_list[i], some_list[i-1] = some_list[i-1], some_list[i]
        i -= 1
    return some_list


def instertion_sort_all_items(some_list):
    for i in range(1, len(some_list)):
        single_item_insertion_sort(some_list, i)
        mod.display_bar_chart(some_list)
    return some_list

some_list = mod.create_random_list(30)

instertion_sort_all_items(some_list)
