#!/usr/bin/python3

"""
Defines a function that divides all elements in a matrix
"""


def matrix_divided(matrix, div):
	"""
	divides all elements of a matrix with div

	args:
		matrix (int[][]): matrix (list of lists of integers)
		div (int or float): number to divide with

	Returns:
		new matrix

	Raises:
		TypeError: matrix must be matrix of numbers
		TypeError: each row must have the same size
		TypeError: div must be a number
		ZeroDivisionError: division by zero
	"""

	if not matrix or (any(elem for row in matrix for elem in row) not in [int, float]):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats\n")
	
	num_columns = len(matrix[0])
	if not all(len(row) == num_columns for row in matrix):
		raise TypeError("Each row of the matrix must have the same size\n")

	if div == 0:
		raise ZeroDivisionError("division by zero\n")

	new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

	return new_matrix


if '__name__' == '__main__':
	import doctest
	doctest.testfile("./tests/2-matrix_divided.txt")
