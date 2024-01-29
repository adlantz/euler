"""
https://projecteuler.net/problem=23
"""


def list_divisors(n):
    divisors = [1]

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return divisors


def is_sum_of_two_abundant_numbers(n, abundant_numbers):
    head = 0
    tail = len(abundant_numbers) - 1

    while True:
        a_sum = abundant_numbers[head] + abundant_numbers[tail]

        if a_sum == n:
            return True

        if head == tail:
            return False

        if a_sum < n:
            head += 1
        elif a_sum > n:
            tail -= 1


# Generate all abundant numbers up to 28123/2
abundant_numbers = [12]
for i in range(13, 28124):
    if sum(list_divisors(i)) > i:
        abundant_numbers.append(i)


# Sum all numbers that can't be expressed as a sum of two abundant numbers
non_a_sum = 0
for i in range(1, 28124):
    if not is_sum_of_two_abundant_numbers(i):
        non_a_sum += i

print(non_a_sum)
