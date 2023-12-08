#!/usr/bin/python3
"""
--- Day 8: Haunted Wasteland ---
You're still riding a camel across Desert Island when you spot a sandstorm quickly approaching. When you turn to warn the Elf, she disappears before your eyes! To be fair, she had just finished warning you about ghosts a few minutes ago.

One of the camel's pouches is labeled "maps" - sure enough, it's full of documents (your puzzle input) about how to navigate the desert. At least, you're pretty sure that's what they are; one of the documents contains a list of left/right instructions, and the rest of the documents seem to describe some kind of network of labeled nodes.

It seems like you're meant to use the left/right instructions to navigate the network. Perhaps if you have the camel follow the same instructions, you can escape the haunted wasteland!

After examining the maps for a bit, two nodes stick out: AAA and ZZZ. You feel like AAA is where you are now, and you have to follow the left/right instructions until you reach ZZZ.

This format defines each node of the network individually. For example:

RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
Starting with AAA, you need to look up the next element based on the next left/right instruction in your input. In this example, start with AAA and go right (R) by choosing the right element of AAA, CCC. Then, L means to choose the left element of CCC, ZZZ. By following the left/right instructions, you reach ZZZ in 2 steps.

Of course, you might not find ZZZ right away. If you run out of left/right instructions, repeat the whole sequence of instructions as necessary: RL really means RLRLRLRLRLRLRLRL... and so on. For example, here is a situation that takes 6 steps to reach ZZZ:

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
Starting at AAA, follow the left/right instructions. How many steps are required to reach ZZZ?
"""

def find_next_point(current_point, direction):
    for dict_item in list_of_dicts:
        if current_point in dict_item:
            if direction == "L":
                return dict_item[current_point][0]
            else:
                return dict_item[current_point][1]

with open('p08-input.txt', 'r') as file:
    #read the first line
    instructions = file.readline().strip()
    # Skip the second line
    file.readline()

# Read the rest of the file and parse lines 3 onward into a list of dicts
    list_of_dicts = []
    for line in file:
        line = line.strip()
        if line:  # Check if the line is not empty
            key, value = line.split('=')
            key = key.strip()
            value = value.strip().strip('()').split(', ')
            list_of_dicts.append({key: value})

current_point = "AAA"
turns_taken = 0

while current_point != "ZZZ": #Loop until we find it
    for char in instructions:
        current_point = find_next_point(current_point, char)
        print(f"Current point is {current_point}, direction is {char}")
        turns_taken += 1
        if current_point == "ZZZ": #Break once we do
            break

# Output
print(f"Number of turns taken is {turns_taken}")