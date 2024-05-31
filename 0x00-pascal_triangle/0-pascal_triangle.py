#!/usr/bin/python3
"""
Pascal's Triangle Module
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of height n.

    Args:
        n (int): The height of the triangle.

    Returns:
        List[List[int]]: A list of lists of integers
        representing the Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)

    return triangle
