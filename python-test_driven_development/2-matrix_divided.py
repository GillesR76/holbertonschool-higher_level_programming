#!/usr/bin/python3
"""
Write a function that divides all elements of a matrix
Matrix must be a list of lists of integers or floats
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matric
    """
    for row in matrix:
        if not all(isinstance(x, (int, float)) for x in matrix for x in row):
            raise TypeError("matrix must \
be a matrix (list of lists) of integers/floats")
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return [[round(column / div, 2) for column in row] for row in matrix]
