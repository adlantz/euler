"""
https://projecteuler.net/problem=21
"""


def list_divisors(n):
    divisors = [1]

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    return divisors


i_sum_map = {}
amicable_pairs = []
N = 10_000

for i in range(1, N):
    divisor_sum = sum(list_divisors(i))

    if divisor_sum in i_sum_map:
        if i == i_sum_map[divisor_sum]:
            print(f"{i} is a pair with {divisor_sum}")
            amicable_pairs += [divisor_sum, i]
    i_sum_map[i] = divisor_sum

print(amicable_pairs)
print(sum(amicable_pairs))


# n = 8
# print(list_divisors(n))


# for i in range(1, 11):
#     print("_____________")
#     print(i)
#     print(list_divisors(i))
