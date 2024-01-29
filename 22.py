"""
https://projecteuler.net/problem=22
"""

char_to_int_map = {char: i + 1 for i, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}


def name_score(name: str) -> int:
    score = 0
    for char in name:
        score += char_to_int_map[char]
    return score


with open("22.txt", "r") as file:
    names_string = file.read()
names = [name.strip('"') for name in names_string.split(",")]


score_sum = 0
for i, name in enumerate(sorted(names)):
    score_sum += (i + 1) * name_score(name)

print(score_sum)
