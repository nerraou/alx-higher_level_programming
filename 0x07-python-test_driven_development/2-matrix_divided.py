#!/usr/bin/python3
"""Module for matrix divided method"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix by div"""

    if div == float('inf') or div == -float('inf') or div != div:
        raise TypeError("div must be a number")
    if (type(div) is not int and type(div) is not float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix "
            "(list of lists) of integers/floats"
        )
    new_matrix = []
    row_len = None
    for row in matrix:
        if type(row) is not list or len(matrix[0]) == 0:
            raise TypeError(
                "matrix must be a matrix "
                "(list of lists) of integers/floats"
            )
        if row_len is None:
            row_len = len(row)
        if row_len is not len(row):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError(
                    "matrix must be a matrix "
                    "(list of lists) of integers/floats"
                )
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)
    return new_matrix
