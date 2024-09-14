#!/usr/bin/python3
<<<<<<< HEAD
""" Minimum Operations"""

=======
>>>>>>> origin/main

def minOperations(n):
    """ Minimum Operations"""
    if n <= 1:
        return 0
<<<<<<< HEAD
    i = 2
    result = 0
    while i <= n:
        if n % i == 0:
            result += i
            n = n / i
        else:
            i += 1
    return result
=======

    ops = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1

    return ops

if __name__ == "__main__":
    print(minOperations(4))  # Test with example values
    print(minOperations(12))
>>>>>>> origin/main
