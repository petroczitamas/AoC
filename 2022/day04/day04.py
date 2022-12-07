import os
import re

with open(os.path.join(os.path.dirname(__file__), 'day04.txt'), 'r') as f:
    data = f.read().splitlines()

subsets = 0
intersections = 0

for line in data:
    start_one, end_one, start_two, end_two = list(map(int, re.split(r'[,-]', line)))

    # This version is less performant
    # if set(range(start_one, end_one + 1)).issubset(set(range(start_two, end_two + 1))) or set(range(start_one, end_one + 1)).issuperset(set(range(start_two, end_two + 1))):
    #     subsets += 1  

    if start_one <= start_two and end_one >= end_two or start_two <= start_one and end_two >= end_one:
        subsets += 1

    if start_one <= start_two <= end_one or start_two <= start_one <= end_two:
        intersections += 1

print(subsets)
print(intersections)


