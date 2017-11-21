some_list = [4,3,6,2]
i = 0
smallest_value = i

def slection_sort(some_list):
    start_pos = 0
    smallest_value = start_pos
    for i in range(start_pos + 1, len(some_list)):
        if some_list[i] < some_list[smallest_value]:
            smallest_value = i 
