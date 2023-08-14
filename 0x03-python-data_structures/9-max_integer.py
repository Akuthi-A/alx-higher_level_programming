#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    max_elem = 0
    for num in my_list:
        if num > max_elem:
            max_elem = num

    return max_elem
