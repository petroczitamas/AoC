import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), "day07.txt"), "r") as f:
    data = f.read().splitlines()

dir_sizes = defaultdict(int)
stack = ["root"]

for i in data:
    if i == "$ cd /" or i.startswith("$ ls") or i.startswith("dir"):
        continue
    if i.startswith("$ cd"):
        working_folder = i.split()[2]
        if working_folder != "..":
            path = f"{stack[-1]}\\{working_folder}"
            stack.append(path)
        else:
            stack.pop()
    else:
        filesize, filename = i.split()
        for path in stack:
            dir_sizes[path] += int(filesize)

print(
    "The sum of the size of directories with a total size of at most 100000 is:",
    sum(i for i in dir_sizes.values() if i <= 100000),
)

currently_free = 70000000 - dir_sizes["root"]
target_size = 30000000 - currently_free
for size in sorted(dir_sizes.values()):
    if size > target_size:
        print("Size of the smallest directory to delete is:", size)
        break
