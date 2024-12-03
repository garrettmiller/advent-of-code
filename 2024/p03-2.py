#!/usr/bin/python3
"""
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""
import re

totalProduct = 0
do_positions = []
dont_positions = []
enabled_ranges = []

# Define a regex pattern for valid instructions: mul(X,Y)
# (I used ChatGPT 4o to help me with this pattern)
pattern = r'mul\(\d+,\d+\)'
do_pattern = r'\bdo\(\)'       # Matches `do()`
dont_pattern = r"\bdon't\(\)"  # Matches `don't()`

# We start enabled
do_positions.append(0)

# Open the file for reading
with open('p03-input.txt', 'r') as file:
    content = file.read()
    do_matches = re.finditer(do_pattern, content)
    dont_matches = re.finditer(dont_pattern, content)
    for do_match in do_matches:
        do_positions.append((do_match.end()))
    for dont_match in dont_matches:
        dont_positions.append((dont_match.end()))

    print(f"do_positions: {do_positions}")
    print(f"dont_positions: {dont_positions}")   

# Find ranges of enablement
for i in range(len(do_positions)):
    try:
        #print(f"do_positions: {do_positions}")
        next_dont_list = [x for x in dont_positions if x > do_positions[i]]
        #print(f"next_dont_list: {next_dont_list}")
        next_dont = min(next_dont_list)
        enabled_ranges.append((do_positions[i], next_dont))
        do_positions = [x for x in do_positions if x > next_dont or x <= do_positions[i]]
    except:
        pass #  ¯\_(ツ)_/¯ not proud of this but easier than figuring out the indexing errors

enabled_ranges.append((do_positions[-1], len(content)))  #  ¯\_(ツ)_/¯  last element missing for some reason, add it
# slice enabled sections out and put them into a new string
enabled_content = ""
for enabled_range in enabled_ranges:
    enabled_content = enabled_content + content[enabled_range[0]:enabled_range[1]]

print(f"Enabled ranges:{enabled_ranges}")
print(f"Content length:{len(content)}")
print(f"Enabled length:{len(enabled_content)}")
# Then, find all mul instructions in the new string
matches = re.findall(pattern, enabled_content)
# Iterate over the matches
for match in matches:
    # Extract the two numbers from the match
    numbers = re.findall(r'\d+', match)
    # Multiply the two numbers and add the product to the total
    totalProduct += int(numbers[0]) * int(numbers[1])

print(f"The total product of all valid instructions is: {totalProduct}")
#print(enabled_content)