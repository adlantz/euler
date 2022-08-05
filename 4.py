"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math


def product_of_two_threes(num):
    for n in range(100, math.ceil(math.sqrt(num))):
        if num % n == 0:
            if len(str(n)) == 3 and len(str(num // n)) == 3:
                print(n)
                print(num // n)
                print(num)
                return True
    return False


max_product = 999 * 999
for product in range(max_product, 0, -1):
    if str(product) == str(product)[::-1] and product_of_two_threes(product):
        break
