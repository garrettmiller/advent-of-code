#!/usr/bin/python3
"""
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""
import re

totalProduct = 0

# Define a regex pattern for valid instructions: mul(X,Y)
# (I used ChatGPT 4o to help me with this pattern)
pattern = r'mul\(\d+,\d+\)'
       
# Open the file for reading
with open('p03-input.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Find all matches in the input string
        matches = re.findall(pattern, line)
        # Iterate over the matches
        for match in matches:
            # Extract the two numbers from the match
            numbers = re.findall(r'\d+', match)
            # Multiply the two numbers and add the product to the total
            totalProduct += int(numbers[0]) * int(numbers[1])

print(f"The total product of all valid instructions is: {totalProduct}")