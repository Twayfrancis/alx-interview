#!/usr/bin/python3
""" generate Pascal's triangle up to the nth row
    args:
    - n: an int repr number of rows
    Returns:
    - list of list repr Pascal's triangle
"""


def pascal_triangle(n):
    """function return list of int"""
    if n <= 0:
        return []
    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        triangle.append(row)
    return (triangle)
