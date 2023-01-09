import os
from itertools import accumulate

with open(os.path.join(os.path.dirname(__file__), "day10.txt"), "r") as f:
    data = f.read().split()


def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


instructions = [int(x) if is_number(x) else 0 for x in data]

part_one = 0
part_two = []

for idx, x in enumerate(accumulate(instructions, initial=1), start=1):
    sprite = [x - 1, x, x + 1]
    if idx % 40 == 20:
        part_one += idx * x
    if (idx - 1) % 40 in sprite:
        part_two.append("#")
    else:
        part_two.append(" ")

print("Part 1: The sum of the six specified signal strengths:", part_one)
print("Part 2:")
part_two_visual = [print(part_two[40 * i : 40 * i + 40]) for i in range(6)]
