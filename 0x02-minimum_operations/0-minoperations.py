#!/usr/bin/python3
"""
Module for calculating the minimum number of operations to achieve
n 'H' characters in a file starting from a single 'H'.
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
