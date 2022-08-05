"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""

import math

prime_count = 0
current_num = 1

nth_prime = 10001

while prime_count != nth_prime:
    current_num += 1
    is_prime = True
    factor = 2
    while factor <= math.floor(math.sqrt(current_num)) and is_prime:
        if current_num % factor == 0:
            is_prime = False
        factor += 1

    if is_prime:
        prime_count += 1

print(current_num)
