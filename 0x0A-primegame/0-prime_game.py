#!/usr/bin/python3
"""function to check if num is prime"""


def is_prime(n):
    """function to check if num is prime"""
    # Base cases
    if n <= 1:
        return False
    if n == 2:
        return True
    # Check for divisibility by 2
    if n % 2 == 0:
        return False
    # Check for divisibility by odd numbers up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    # If no divisor is found, n is prime
    return True


def count_prime_factors(n):
    """funct to count num of distinct prime factors of num"""
    # Initialize the count
    count = 0
    # Divide by 2 as long as possible
    while n % 2 == 0:
        n //= 2
        count += 1
    # Divide by odd numbers starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        # If i is prime factor incr count and div by i as long as possible
        if is_prime(i) and n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
    # If n is greater than 2, it is a prime factor
    if n > 2:
        count += 1
    # Return the count
    return count


def isWinner(x, nums):
    """func to determine winner of most rounds of game"""
    # Initialize the scores of Maria and Ben
    maria = 0
    ben = 0
    # Loop through the rounds
    for i in range(x):
        # Get the current value of n
        n = nums[i]
        # Initialize the nim-sum
        nim_sum = 0
        # Loop through the set of integers from 1 to n
        for j in range(1, n + 1):
            # If j is prime, add its nim-value to the nim-sum
            if is_prime(j):
                nim_sum ^= count_prime_factors(j)
        # If the nim-sum is zero, Ben wins the round
        if nim_sum == 0:
            ben += 1
        # Otherwise, Maria wins the round
        else:
            maria += 1
    # Compare the scores and return the winner or None
    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
