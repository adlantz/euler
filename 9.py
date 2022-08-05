"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math

a = 1
b = 1

found = False
while not found:
    b += 1
    c = math.sqrt(a ** 2 + b ** 2)
    if a + b + c > 1000:
        a += 1
        b = a + 1
    elif c.is_integer():
        if a + b + int(c) == 1000:
            found = True

print(a)
print(b)
print(int(c))
print(a * b * int(c))
