#!/usr/bin/python3
"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
"""

lineList = []
numbers = []
# Special characters
special_chars = set('#@%&$[]_`~-+*=/!-')

with open("p03-input.txt", 'r') as file:
    for line in file:
        lineList.append(line.strip()) # Strip removes newlines

# Function to check for special characters around the number
def has_special_char_around(lineList, digit_positions):
    for line_index, char_index in digit_positions:
        # Check adjacent characters including diagonals
        for i in range(max(0, line_index - 1), min(line_index + 2, len(lineList))):
            for j in range(max(0, char_index - 1), min(char_index + 2, len(lineList[i]))):
                if (i, j) != (line_index, char_index) and lineList[i][j] in special_chars:
                    return True
    return False

# Iterate over each line and each character
for line_index, line in enumerate(lineList):
    myNumString = ''  # Reset for each new line
    digit_positions = []  # Track positions of digits in the number

    for char_index, char in enumerate(line):
        if char.isdigit():
            digit_positions.append((line_index, char_index))
            myNumString += char  # Append digit to the string
        else:
            if myNumString and has_special_char_around(lineList, digit_positions):
                numbers.append(int(myNumString))
            myNumString = ''  # Reset the string for next number
            digit_positions = []

    # Check for last number in line
    if myNumString and has_special_char_around(lineList, digit_positions):
        numbers.append(int(myNumString))

print(f"Our set of numbers is {numbers}")
print(f"The sum of valid part numbers is {sum(numbers)}")

