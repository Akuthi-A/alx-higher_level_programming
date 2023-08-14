#!/usr/bin/python3

def element_at(my_list, idx):
    """
    returns the element at given index
    """
    length = len(my_list) - 1

    if (idx < 0) or (idx > length):
        return None

    for i in range(length):
        if (i == idx):
            return my_list[idx]
