# import math # Used in Part 1 solution only
import os

import numpy as np

with open(os.path.join(os.path.dirname(__file__), "day09.txt"), "r") as f:
    data = f.read().splitlines()

# Unified solution

instructions = [i.split() for i in data]


def rope_simulation(length) -> int:
    rope = [(0j) for i in range(length)]
    tail_visited = {0j}

    directional_movement = {
        "U": 1j,
        "D": -1j,
        "L": (-1 + 0j),
        "R": (1 + 0j),
    }

    for line in instructions:
        for _ in range(int(line[1])):
            rope[0] = rope[0] + directional_movement[line[0]]
            for i in range(length - 1):
                diff_x, diff_y = (
                    rope[i].real - rope[i + 1].real,
                    rope[i].imag - rope[i + 1].imag,
                )
                if abs(diff_x) > 1 or abs(diff_y) > 1:
                    rope[i + 1] = complex(
                        rope[i + 1].real + np.sign(diff_x),
                        rope[i + 1].imag + np.sign(diff_y),
                    )
                tail_visited.add(rope[-1])
    return len(tail_visited)


print("Part 1: The tail of the rope visits", rope_simulation(2), "locations.")
print("Part 1: The tail of the rope visits", rope_simulation(10), "locations.")

# Original Part 1 solution - not applicable to Part 2

# head = 0j
# tail = 0j
# tail_history = {0j}

# directional_movement = {
#     "U": 1j,
#     "D": -1j,
#     "L": (-1 + 0j),
#     "R": (1 + 0j),
# }

# for line in instructions:
#     for _ in range(int(i[1])):
#         previous_head = head
#         head = head + directional_movement[i[0]]
#         distance = math.sqrt(
#             (head.real - tail.real) ** 2 + (head.imag - tail.imag) ** 2
#         )
#         if math.floor(distance) = 2:
#             tail = previous_head
#             tail_history.add(tail)
#         else:
#             continue

# print("Part 1: The tail of the rope visits", len(tail_history), "locations.")
