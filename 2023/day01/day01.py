import os

with open(os.path.join(os.path.dirname(__file__), "day01.txt"), "r") as f:
    data: list[str] = f.read().splitlines()

corrected_data: list[str] = []

# Correct the input data by iterating over list values and replacing number-words with a string that includes the number.
# The replacement strings are constructed to preserve integrity of following words ("oneight", "twone", "threeight", "fiveight", "sevenine", "eightwo", "eighthree", "nineight")
for i in data:
    corrected_data.append(i.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', 'f4r').replace('five', 'f5e').replace('six', 's6x').replace('seven', 's7n').replace('eight', 'e8t').replace('nine', 'n9e'))

calibration_sum: int = 0
 
for i in corrected_data:
    digits: list[str] = [char for char in i if char.isdigit()]
    calibration_value: str = digits[0] + digits[-1]
    calibration_sum += int(calibration_value)

print(calibration_sum)

# Part 1 result: 54239
# Part 2 result: 55343