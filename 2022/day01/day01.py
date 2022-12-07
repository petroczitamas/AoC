import os

with open(os.path.join(os.path.dirname(__file__), 'day01.txt'), 'r') as f:
    data = f.read().splitlines()

elf_list = []
count = 0

for i in data:
    if i != '':
        count += int(i)
    else:
        elf_list.append(count)
        count = 0

elf_list.sort()

print(elf_list[-1])
print(sum(elf_list[-3:]))


# max = 0
# count = 0

# for i in data:
#     if i != '':
#         count += int(i)
#     else:
#         if count > max:
#             max = count
#          count = 0

# print(max)

