#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Calculates the fewest number of operations needed to result in
    exactly n H characters in the file."""
    if n <= 1:
        return 0
    div = 2
    operations = 0
    while n > 1:
        if n % div == 0:
            operations += div
            n = n / div
        else:
            div += 1
    return operations
