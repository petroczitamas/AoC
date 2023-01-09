import os
import string

with open(os.path.join(os.path.dirname(__file__), "day03.txt"), "r") as f:
    data = f.read().splitlines()

letters_found = [False] * 52

priorities = dict(zip(list(string.ascii_letters), range(52)))

duplicate_total = 0

for i in data:
    half = len(i) // 2
    first, second = set(i[:half]), set(i[half:])
    for j in first:
        letters_found[priorities[j]] = True
    for k in second:
        if letters_found[priorities[k]]:
            duplicate_total += priorities[k] + 1
            break
    letters_found = [False] * 52

print(duplicate_total)

badge_total = 0

for i in range(0, len(data), 3):
    j = i + 1
    k = i + 2

    first = set(data[i])
    second = set(data[j])
    third = set(data[k])
    intersect = set.pop(set.intersection(first, second, third))

    badge_total += priorities[str(intersect)] + 1

print(badge_total)
