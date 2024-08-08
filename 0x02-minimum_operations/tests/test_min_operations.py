#!/usr/bin/python3
"""
Test script for the min_operations function.
"""

from minoperations import min_operations

def run_tests():
    """
    Run a series of test cases to verify the correctness of min_operations function.
    """
    test_cases = [
        (1, 0),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 5),
        (9, 6),
        (10, 7),
        (15, 8),
        (16, 8)
    ]

    for n, expected in test_cases:
        result = min_operations(n)
        print(f"min_operations({n}) = {result}, expected = {expected}")
        assert result == expected, f"Test case failed: min_operations({n}) = {result}, expected = {expected}"

if __name__ == "__main__":
    run_tests()
