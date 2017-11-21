import sorting_mods as mod
import sys

def selection_sort(some_list):
    for i in range(len(some_list)):
        smallest_value = i

        for j in range(i+ 1, len(some_list)):
            if some_list[j] < some_list[smallest_value]:
                smallest_value = j

        some_list[smallest_value], some_list[i] = some_list[i], some_list[smallest_value]
        mod.display_bar_chart(some_list)
    return some_list


if __name__ == "__main__":
    list_length = int(sys.argv[1])
    example_list = mod.create_random_list(list_length)
    selection_sort(example_list)
