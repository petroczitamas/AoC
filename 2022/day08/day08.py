import os
import numpy as np

with open(os.path.join(os.path.dirname(__file__), "day08.txt"), "r") as f:
    data = np.array([list(i.strip()) for i in f], int)

# Part 1 solution
part_one = np.zeros_like(data)

for _ in range(4):
    for idx_y, y in enumerate(data):
        current_max = -1
        for idx_x, x in enumerate(y):
            if x > current_max:
                part_one[idx_y, idx_x] = 1
                current_max = x
    data = np.rot90(data)
    part_one = np.rot90(part_one)

print(
    "Part 1: The number of trees visible from outside the grid:",
    np.sum(part_one),
)

# Part 2 solution
part_two = np.zeros_like(data)
cols, rows = data.shape


def visible_trees(location, line) -> int:
    visibility = 0
    if line.size > 0:
        for tree in line:
            if tree < location:
                visibility += 1
            else:
                return visibility + 1
        return visibility
    else:
        return 0


for y in range(rows):
    for x in range(cols):
        part_two[y, x] = (
            visible_trees(data[y, x], np.flip(data[:y, x]))
            * visible_trees(data[y, x], np.flip(data[y, :x]))
            * visible_trees(data[y, x], data[y + 1 :, x])
            * visible_trees(data[y, x], data[y, x + 1 :])
        )

print("Part 2: The highest scenic score possible:", np.amax(part_two))
