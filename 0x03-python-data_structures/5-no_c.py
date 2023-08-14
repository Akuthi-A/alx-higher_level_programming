#!/usr/bin/env python3

def no_c(my_string):
    """
    removes all characters of c & C
    """
    new_string = ""
    for letter in my_string:
        if (letter == "c") or (letter == "C"):
            pass
        else:
            new_string += letter

    return new_string
