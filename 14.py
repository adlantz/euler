"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def chain_length(num, chain_length_dict):
    if num not in chain_length_dict.keys():
        if num % 2 == 0:
            next_num = num // 2
        else:
            next_num = (3 * num) + 1
        ch_len, chain_length_dict = chain_length(next_num, chain_length_dict)
        chain_length_dict[num] = 1 + ch_len
    return chain_length_dict[num], chain_length_dict


chain_length_dict = {1: 1}

for i in range(1, 1000000):
    length, chain_length_dict = chain_length(i, chain_length_dict)


max_k = 0
max_v = 0

for k in chain_length_dict.keys():
    if chain_length_dict[k] > max_v:
        max_v = chain_length_dict[k]
        max_k = k

print(f"number: {max_k}, chain length: {max_v}")
