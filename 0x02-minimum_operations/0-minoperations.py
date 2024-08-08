#!/usr/bin/python3
"""
This module defines the min_operations function that calculates the minimum
number of operations needed to get exactly n 'H' characters in a text file.
"""

def min_operations(n):
    """
    Calculate the minimum number of operations required to get exactly n 'H'
    characters in the file.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: The fewest number of operations needed, or 0 if impossible.
    """
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
