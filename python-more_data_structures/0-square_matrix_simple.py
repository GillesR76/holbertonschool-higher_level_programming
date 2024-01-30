#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[column * column for column in row] for row in matrix]
