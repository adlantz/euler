"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

import math

num = 600851475143
prime_factor_set = set()
factor_list = [num]
while len(factor_list) > 0:
    current_num = factor_list.pop()
    is_prime = True
    for n in range(2, math.ceil(math.sqrt(current_num))):
        if current_num % n == 0:
            is_prime = False
            factor_list.append(n)
            factor_list.append(int(current_num / n))
    if is_prime:
        prime_factor_set.add(current_num)


print(max(prime_factor_set))
