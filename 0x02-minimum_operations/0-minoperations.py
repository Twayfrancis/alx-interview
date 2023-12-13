#!/usr/bin/python3
"""minimum numbers of operations"""


def minOperations(n):
    """
    Calculate minimum number of operations needed to get `n` 'H' characters.

    function works by creating an array `dp` where `dp[i]` is the minimum
    number of operations to get `i` 'H' char. It initializes `dp[i]` to `i`
    because worst case is to copy and paste 'H' `i` times. Then it finds the
    largest factor of `i` and updates `dp[i]` to be min num of operations
    to get `j` 'H' char plus numb of times we can paste 'H' to get `i`
    'H' characters.

    Parameters:
    n (int): The number of 'H' characters to get.

    Returns:
    int: minimum number of operations needed to get `n` 'H' characters. If `n`
         is impossible to achieve, return 0.
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result
