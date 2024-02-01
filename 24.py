"""
https://projecteuler.net/problem=24
"""
"""
I figured this goofy algorithm out on my own but it still confuses me.
I know 1023456789 is the (9! = 362880)th permutation
because lexigraphically it needs to fully exhaust all permutations
of the 9 digits before it can move the zero out of the greatest sig dig.
If you do that twice you get 2013456789 is (2*9! = 725760) permutations
but if you do it three times you go over 1 million (3*9! = 1_088_640) permutations.
So you now know that 2 is the greatest sig dig and now you run the same process
for the next nine digits 2[013456789].

The permutation gets built as follows:
|0123456789
2|013456789
27|01345689
278|0134569
2783|014569
27839|01456
27839|01456
278391|0456
2783915|046
2783915460|


The algorithm goes something like this
number of permutations p(n) = n!

find largest n1 for p(n1) < 999_999
find largest n2 for p(n2) < 999_999 - p(n1)
find largest n3 for p(n3) < 999_999 - p(n1) - p(n2)
...
continue until 999_999 - p(n1) - p(n2) ... == 0
"""
import math

from collections import defaultdict

dig_list = [i for i in range(10)]

dig_increment_counts = defaultdict(int)

num = 999_999

while num > 0:
    n = 0
    while math.factorial(n) <= num:
        n += 1
    dig_increment_counts[n] += 1
    num -= math.factorial((n - 1))


millionth_perm = []
for i in range(10, 0, -1):
    millionth_perm.append(dig_list.pop(dig_increment_counts[i]))


print("".join(map(str, millionth_perm)))


"""
EVERYTHING BELOW IS JUST ALL THE DIFFERENT METHODS I TRIED TO APPROACH THIS PROBLEM WITH (UNSUCCESSFULLY)
"""

"""
0123456789
0123456798
0123456879
0123456897
0123457689
...

0123456789
0123456798
0123456879
0123456897
0123457689
0123457698
0123457869
0123457896
0123465789



0987654321
1023456789


1234567890
2345678901

2013456789


012
021
102
120
201
210
"""


# Look at least significant digit
# If it's greater than the digit to the left, insert least sig dig to the left of it
# If it's smaller than the digit to the, compare to the next digit to the left
# repeat until you get to the end of the string or find one that's greater
# if you hit the end of the string, look at next least significant digit

# dig_list = [i for i in range(5)]
# N = 10
# for i in range(N):
#     print("".join(map(str, dig_list)))
#     least_sig_dig = dig_list[-1]
#     first_digit = 0

#     d = 1
#     while True:
#         if -1 - d == 5:
#             # we've reached the most significant digit
#             # increment first_digit add it to the front, and sort the rest
#             first_digit += 1
#             dig_list = [first_digit] + [i for i in range(10) if i != first_digit]
#             break
#         if least_sig_dig > dig_list[-1 - d]:
#             # insert least sig dig to left of next digit that's smaller
#             dig_list = dig_list[: -1 - d] + [least_sig_dig] + dig_list[-1 - d : -1]
#             break
#         d += 1


# print(dig_list)


"""
89
98

7|89
7|98
8|7|9
9|7|8
"""


# def lexical_order_2d(a, b):
#     # Assumes a < b
#     return [[a, b], [b, a]]


# def lexical_order_3d(a, b, c):
#     # Assumes a < b < c

#     out_list = []

#     for perm in lexical_order_2d(b, c):
#         out_list.append([a, *perm])

#     for perm in lexical_order_2d(a, c):
#         out_list.append([b, *perm])

#     for perm in lexical_order_2d(a, b):
#         out_list.append([b, *perm])

#     return out_list


# print(lexical_order_3d(0, 1, 2))


"""
01234[56]
01234[65] --> in reverse order, take smallest that's larger than next sig dig and swap with next sig dig
01235[46]
01235[64] --> in reverse order, take smallest that's larger than next sig dig and swap with next sig dig
01236[45]
01236[54] --> in reverse order, no digit is larger than next sig dig, expand scope --> 0123[654] --> in reverse order, do sig dig swap
0124[356] --> greater than 2 and in order --> minimize scope --> 01243[56]
01243[65] --> in reverse order bla bla
...
01246[53] --> 0124[653] --> 0125[346]

...

01265[43] -- > 0126[543] --> 012[6543] --> 013[2456] --> 0132[456] --> 01324[56]
...
0[654321]
1[023456]

01234


"""

# dig_list = [i for i in range(5)]

# scope_size = 2
# N = 10
# i = 0
# while i < N:
#     print("-------------")
#     print("scope", scope_size)
#     print("".join(map(str, dig_list)))

#     if dig_list[-scope_size:] == sorted(dig_list[-scope_size:], reverse=True):
#         # scope in reverse order
#         scope_minimum =
#         scope_size += 1

#         dig_list = dig_list[:-scope_size] + sorted(dig_list[-scope_size:])
#     elif scope_size == 2:
#         # only two digits, swap em
#         dig_list[-2], dig_list[-1] = dig_list[-1], dig_list[-2]
#     elif dig_list[-scope_size:] == sorted(dig_list[-scope_size:]):
#         # in sorted order
#         scope_size -= 1  # reduce scope
#         i -= 1  # don't count this as a permutation
#     i += 1
#     print("".join(map(str, dig_list)))
#     print("-------------")

# print("".join(map(str, dig_list)))
