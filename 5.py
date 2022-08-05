"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import math


def factors(num):
    factor_set = set([1])
    for n in range(1, math.ceil(math.sqrt(num)) + 1):
        if num % n == 0:
            factor_set.add(n)
            factor_set.add(num // n)
    return factor_set


def least_common_multiple(n1, n2):
    gcd = max(factors(n1).intersection(factors(n2)))
    return (n1 * n2) // gcd


num = 1
for i in range(1, 21):
    print(f"{i}, {num}")
    num = least_common_multiple(i, num)
    print(num)
