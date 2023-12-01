import os

# Open file with input data and read lines into list.
with open(os.path.join(os.path.dirname(__file__), "day01.txt"), "r") as f:
    data: list[str] = f.read().splitlines()

# Initialize empty list for the corrected data
corrected_data: list[str] = []

# Correct the input data by iterating over list values and replacing number-words with a string that includes the number.
# The replacement strings are constructed to preserve integrity of following words ("oneight", "twone", "threeight", "fiveight", "sevenine", "eightwo", "eighthree", "nineight")
for i in data:
    corrected_data.append(i.replace('one', 'one1one').replace('two', 'two2two').replace('three', 'three3three').replace('four', 'four4four').replace('five', 'five5five').replace('six', 'six6six').replace('seven', 'seven7seven').replace('eight', 'eight8eight').replace('nine', 'nine9nine'))

# Declare calibration_sum variable that will hold the result for Part 1.
calibration_sum: int = 0
 
# Iterate over the input data list.
# Iterate over every character of each string in the list - filter for digits with list comprehension.
# Declare calibration_value variable that will hold the first and last digit found in strings (can be the same digit).
# Add calibration_value to calibration_sum.
for i in corrected_data:
    digits: list[str] = [char for char in i if char.isdigit()]
    calibration_value: str = digits[0] + digits[-1]
    calibration_sum += int(calibration_value)

# Print the result for Part 1.
print(calibration_sum)

# Part 1 result: 54239
# Part 2 result: 55343