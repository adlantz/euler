"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""
import math

current_num = 1

prime_list = []

while current_num < 2000000:
    current_num += 1
    is_prime = True
    factor = 2
    while factor <= math.floor(math.sqrt(current_num)) and is_prime:
        if current_num % factor == 0:
            is_prime = False
        factor += 1

    if is_prime:
        prime_list.append(current_num)

print(sum(prime_list))
