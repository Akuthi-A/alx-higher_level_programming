#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = dict(sorted(a_dictionary.items()))
    for key in new_dict:
        value = new_dict[key]
        print(f"{key}: {value}")
