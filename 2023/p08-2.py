#!/usr/bin/python3
"""
--- Part Two ---
The sandstorm is upon you and you aren't any closer to escaping the wasteland. You had the camel follow the instructions, but you've barely left your starting position. It's going to take significantly more steps to escape!

What if the map isn't for people - what if the map is for ghosts? Are ghosts even bound by the laws of spacetime? Only one way to find out.

After examining the maps a bit longer, your attention is drawn to a curious fact: the number of nodes with names ending in A is equal to the number ending in Z! If you were a ghost, you'd probably just start at every node that ends with A and follow all of the paths at the same time until they all simultaneously end up at nodes that end with Z.

For example:

LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
Here, there are two starting nodes, 11A and 22A (because they both end with A). As you follow each left/right instruction, use that instruction to simultaneously navigate away from both nodes you're currently on. Repeat this process until all of the nodes you're currently on end with Z. (If only some of the nodes you're on end with Z, they act like any other node and you continue as normal.) In this example, you would proceed as follows:

Step 0: You are at 11A and 22A.
Step 1: You choose all of the left paths, leading you to 11B and 22B.
Step 2: You choose all of the right paths, leading you to 11Z and 22C.
Step 3: You choose all of the left paths, leading you to 11B and 22Z.
Step 4: You choose all of the right paths, leading you to 11Z and 22B.
Step 5: You choose all of the left paths, leading you to 11B and 22C.
Step 6: You choose all of the right paths, leading you to 11Z and 22Z.
So, in this example, you end up entirely on nodes that end in Z after 6 steps.

Simultaneously start on every node that ends with A. How many steps does it take before you're only on nodes that end with Z?
"""


def find_next_point(current_point, direction):
    for dict_item in list_of_dicts:
        if current_point in dict_item:
            if direction == "L":
                return dict_item[current_point][0]
            else:
                return dict_item[current_point][1]
            
# List to hold first nodes ending with 'A'
first_nodes = []

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
            if key.endswith('A'): #Append to a special list if it starts with A
                first_nodes.append(key)
            value = value.strip().strip('()').split(', ')
            list_of_dicts.append({key: value})

done_flag = False
turns_taken = 0

#There are 6 nodes which end with A: [AAA, MGA, DGA, TLA, RDA, DPA]
while done_flag == False: #Loop until we find it
    print(f"Turns taken is {turns_taken}")
    for char in instructions:
        turns_taken += 1
        for index, node in enumerate(first_nodes):
            first_nodes[index] = find_next_point(first_nodes[index], char)
        if all(item.endswith('Z') for item in first_nodes):
            done_flag = True
            break
     
# Output
print(f"Current points are {first_nodes}, number of turns taken is {turns_taken}")