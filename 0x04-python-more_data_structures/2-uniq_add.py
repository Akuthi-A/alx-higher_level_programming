#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)

    total_sum = 0
    for num in my_set:
        total_sum += num

    return total_sum
