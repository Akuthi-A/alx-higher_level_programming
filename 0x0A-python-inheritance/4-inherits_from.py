#!/usr/bin/python3
"""
This module contains a function that 
checks if an object is an instance of a class
"""


def inherits_from(obj, a_class):
    """
    chekcs if an object is an instance of a class

    Args:
        obj (object): object
        a_class (class): class
    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; otherwise False.
    """
    return issubclass(obj, a_class)
