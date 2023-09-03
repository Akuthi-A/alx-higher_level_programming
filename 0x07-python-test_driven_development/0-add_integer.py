#!/usr/bin/python3

def add_integer(a, b=98):
    """
    takes the sum of two integers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer\n")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer\n")
    return int(a) + int(b)


if '__name__' == '__main__':
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
