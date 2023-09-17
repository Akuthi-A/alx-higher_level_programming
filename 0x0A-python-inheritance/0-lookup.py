#!/usr/bin/python3
"""
This module contains a lookup function ``def lookup(obj)``
"""


def lookup(obj):
    """
    returns the list of available attributes & methods of an object

    args:
        obj (object): object for which to list the attributes & methods

    Returns:
        list of the attributes & methods
    """

    return dir(obj)
