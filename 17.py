"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""


def convert_number_to_words(num, num_word_dict):
    if num not in num_word_dict.keys():
        if len(str(num)) == 2:
            num_word_dict[
                num
            ] = f"{num_word_dict[int(str(num)[0])*10]}{num_word_dict[int(str(num)[1])]}"
        if len(str(num)) == 3:
            if str(num)[1:] == "00":
                num_word_dict[num] = f"{num_word_dict[int(str(num)[0])]}hundred"
            else:
                tens, num_word_dict = convert_number_to_words(
                    int(str(num)[1:]), num_word_dict
                )
                num_word_dict[
                    num
                ] = f"{num_word_dict[int(str(num)[0])]}hundredand{tens}"
        if len(str(num)) == 4:
            num_word_dict[num] = "onethousand"
    return num_word_dict[num], num_word_dict


num_word_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

for i in range(1, 1001):
    word, num_word_dict = convert_number_to_words(i, num_word_dict)


letter_count = 0
for key in num_word_dict.keys():
    letter_count += len(num_word_dict[key])

print(letter_count)
