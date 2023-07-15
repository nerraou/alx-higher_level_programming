#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        print_space = False
        for col in row:
            if print_space is True:
                print(" ", end="")
            print("{:d}".format(col), end="")
            print_space = True
        print()
