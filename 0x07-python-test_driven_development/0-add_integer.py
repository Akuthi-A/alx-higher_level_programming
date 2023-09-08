#!/usr/bin/python3
"""
This module defines a function ``add_integer`` that adds two integers
"""

def add_integer(a, b=98):
    """
    takes the sum of two integers

    args
	a (int or float): num1
	b (int or float): num2

    Returns:
	sum of a and b (a + b)

    Raises:
	TypeError: raised if input is not a number
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if '__name__' == '__main__':
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
