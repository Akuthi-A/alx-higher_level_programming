#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("$\n")
        return None

    for row in matrix:
        for i in range(len(row)):
            print("{}".format(row[i]), end="$\n"if i is len(row) - 1 else " ")
