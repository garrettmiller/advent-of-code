#!/usr/bin/python3
"""
--- Part Two ---
Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate backwards as well, right?

For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

In particular, here is what the third example history looks like when extrapolating back in time:

5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0
Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history. Adding all three new values together produces 2.

Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?
"""

#!/usr/bin/python3
"""
--- Part Two ---
Of course, it would be nice to have even more history included in your report. Surely it's safe to just extrapolate backwards as well, right?

For each history, repeat the process of finding differences until the sequence of differences is entirely zero. Then, rather than adding a zero to the end and filling in the next values of each previous sequence, you should instead add a zero to the beginning of your sequence of zeroes, then fill in new first values for each previous sequence.

In particular, here is what the third example history looks like when extrapolating back in time:

5  10  13  16  21  30  45
  5   3   3   5   9  15
   -2   0   2   4   6
      2   2   2   2
        0   0   0
Adding the new values on the left side of each sequence from bottom to top eventually reveals the new left-most history value: 5.

Doing this for the remaining example data above results in previous values of -3 for the first history and 0 for the second history. Adding all three new values together produces 2.

Analyze your OASIS report again, this time extrapolating the previous value for each history. What is the sum of these extrapolated values?
"""

total_sum = 0

def calculate_differences(lst):
    differences = []  # Initialize an empty list to store the differences
    for i in range(len(lst) - 1):
        diff = lst[i+1] - lst[i]  # Calculate the difference between adjacent elements
        differences.append(diff)  # Append the difference to the differences list
    return differences

# Open the file for reading
with open('p09-input.txt', 'r') as file:
  # Iterate over each line in the file
  for line in file:
    list_of_lists = []
    current_list = []

    # Split the line into elements
    elements = line.split()

    # Convert each element from a string to an integer and add to the current list
    for num in elements:
      current_list.append(int(num))

    # Append the current list of integers to the main list
    list_of_lists.append(current_list)

    next_difference = calculate_differences(list_of_lists[0])
    list_of_lists.append(next_difference)

    # Generate difference sequences until all differences are zero
    while not all(element == 0 for element in next_difference):
      next_difference = calculate_differences(next_difference)
      list_of_lists.append(next_difference)

    # Calculate the next extrapolated value
    for index in range(len(list_of_lists) - 1, 0, -1):
        list_of_lists[index - 1].insert(0,list_of_lists[index - 1][0] - list_of_lists[index][0])

    # Add the first element of the current list to the total sum
    total_sum += current_list[0]
    print(list_of_lists)

print(f"Sum of extrapolated values is {total_sum}")
