#!/usr/bin/python3
"""
This module defines a function that checks
if an object is an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    checks if `obj` is an  instance of `a_class`

    args:
        obj (object): object to be checked
        a_class (class): a class
    """
    return isinstance(obj, a_class)
