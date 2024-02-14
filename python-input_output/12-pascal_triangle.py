#!/usr/bin/python3


"""
* Create a function def pascal_triangle(n):
that returnsa list of lists of integers
representing the Pascals triangle of n:
* Returns an empty list if n <= 0
* You can assume n will be always an integer
* You are not allowed to import any module
"""


def pascal_triangle(n):
    """Function that represents the Pascal triangle"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        preview_row = triangle[-1]
        row = [1]
        for j in range(1, len(preview_row)):
            row.append(preview_row[j - 1] + preview_row[j])
        row.append(1)
        triangle.append(row)
    return triangle
