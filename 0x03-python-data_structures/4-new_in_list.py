#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    replaces an element at given index
    with new element
    """
    length = len(my_list) - 1
    cp_list = my_list[:]

    if (idx < 0) or (idx > length):
        return my_list

    for i in range(length):
        if (i == idx):
            cp_list[idx] = element
    
    return cp_list


