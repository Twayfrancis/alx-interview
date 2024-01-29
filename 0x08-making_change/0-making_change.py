#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """base case: if total is 0 or less, return 0"""
    if total <= 0:
        return 0
    # initialize a large value to represent infinity
    INF = float('inf')

    # create a dp array of size total + 1, fill it with INF, except dp[0] = 0
    dp = [INF] * (total + 1)
    dp[0] = 0

    # loop through the coins list
    for c in coins:
        # loop through the dp array from c to total
        for i in range(c, total + 1):
            # update dp[i] by comparing it with dp[i - c] + 1
            dp[i] = min(dp[i], dp[i - c] + 1)

    # return dp[total] if it is not equal to INF, or -1 otherwise
    return dp[total] if dp[total] != INF else -1
