#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    replaces an element at given index
    with new element
    """
    length = len(my_list) - 1

    if (idx >= 0) and (idx < length):
        my_list[idx] = element

    return my_list
