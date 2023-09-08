#!/usr/bin/python3

"""
This module defines the print_square function
"""


def print_square(size):
	"""
	prints a sqaure with the # character

	args:
		size (int): length of square
	Raises:
		TypeError: if size is not int
		ValueError: if size is negative
	"""

	if not isinstance(size, int):
		raise TypeError("size must be an integer\n")
	if size < 0:
		raise ValueError("size must be >= 0\n")

	for i in range(size):
		for j in range(size):
			print("#", end="")
                print("\n")


if '__name__' == '__main__':
    import doctest
    doctest.testfile("./tests/4-print_square.txt")
