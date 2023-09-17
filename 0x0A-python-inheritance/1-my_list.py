#!/usr/bin/python3
"""
This module contains a class that inherits from list
"""


class MyList(list):
    """
    Blueprint for MyList
    """

    def print_sorted(self):
        """
        sorts and prints list in ascending order
        """
        print(sorted(self))
