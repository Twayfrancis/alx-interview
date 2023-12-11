#!/usr/bin/python3
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
    if n <= 1:
        return 0
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i
        for j in range(i - 1, 0, -1):
            if i % j == 0:
                dp[i] = dp[j] + i // j
                break
    return dp[n]
