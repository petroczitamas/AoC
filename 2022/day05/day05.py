import os
import re
from collections import deque

# Separating crane setup information from stacking instructions
with open(os.path.join(os.path.dirname(__file__), "day05.txt"), "r") as f:
    crane_data, job_data = f.read().split("\n\n")

# Preparing the separated information for processing
starting_positions = crane_data.splitlines()

instructions = job_data.splitlines()

# Transforming crane setup to stacks
crane_setup = []

for line in starting_positions:
    for y in line[1::4]:
        crane_setup.append(y)

crane_setup.reverse()

cranes = [deque() for x in range(9)]

# Sorting the original data between the cranes (deques)
for idx, x in enumerate(crane_setup):
    if x == " ":
        continue
    cranes[idx % 9].append(x)

cranes.reverse()

# Reading instructions
instruction_list = [[int(i) for i in re.findall(r"\d+", j)] for j in instructions]

# Operating the cranes (Part 1)
# for i in instruction_list:
#     for j in range(i[0]):
#         cranes[i[2] - 1].append(cranes[i[1] - 1].pop())

# Operating the cranes (Part 2)
for i in instruction_list:
    crate_cache = deque()
    for j in range(i[0]):
        crate_cache.append(cranes[i[1] - 1].pop())
    for k in range(i[0]):
        cranes[i[2] - 1].append(crate_cache.pop())

for i in cranes:
    print(i[-1])
