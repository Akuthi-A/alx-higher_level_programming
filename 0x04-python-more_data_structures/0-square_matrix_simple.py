#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sub in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, sub)))

    return new_matrix
