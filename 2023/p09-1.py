#!/usr/bin/python3
"""
--- Day 9: Mirage Maintenance ---
You ride the camel through the sandstorm and stop where the ghost's maps told you to stop. The sandstorm subsequently subsides, somehow seeing you standing at an oasis!

The camel goes to get some water and you stretch your neck. As you look up, you discover what must be yet another giant floating island, this one made of metal! That must be where the parts to fix the sand machines come from.

There's even a hang glider partially buried in the sand here; once the sun rises and heats up the sand, you might be able to use the glider and the hot air to get all the way up to the metal island!

While you wait for the sun to rise, you admire the oasis hidden here in the middle of Desert Island. It must have a delicate ecosystem; you might as well take some ecological readings while you wait. Maybe you can report any environmental instabilities you find to someone so the oasis can be around for the next sandstorm-worn traveler.

You pull out your handy Oasis And Sand Instability Sensor and analyze your surroundings. The OASIS produces a report of many values and how they are changing over time (your puzzle input). Each line in the report contains the history of a single value. For example:

0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
To best protect the oasis, your environmental report should include a prediction of the next value in each history. To do this, start by making a new sequence from the difference at each step of your history. If that sequence is not all zeroes, repeat this process, using the sequence you just generated as the input sequence. Once all of the values in your latest sequence are zeroes, you can extrapolate what the next value of the original history should be.

In the above dataset, the first history is 0 3 6 9 12 15. Because the values increase by 3 each step, the first sequence of differences that you generate will be 3 3 3 3 3. Note that this sequence has one fewer value than the input sequence because at each step it considers two numbers from the input. Since these values aren't all zero, repeat the process: the values differ by 0 at each step, so the next sequence is 0 0 0 0. This means you have enough information to extrapolate the history! Visually, these sequences can be arranged like this:

0   3   6   9  12  15
  3   3   3   3   3
    0   0   0   0
To extrapolate, start by adding a new zero to the end of your list of zeroes; because the zeroes represent differences between the two values above them, this also means there is now a placeholder in every sequence above it:

0   3   6   9  12  15   B
  3   3   3   3   3   A
    0   0   0   0   0
You can then start filling in placeholders from the bottom up. A needs to be the result of increasing 3 (the value to its left) by 0 (the value below it); this means A must be 3:

0   3   6   9  12  15   B
  3   3   3   3   3   3
    0   0   0   0   0
Finally, you can fill in B, which needs to be the result of increasing 15 (the value to its left) by 3 (the value below it), or 18:

0   3   6   9  12  15  18
  3   3   3   3   3   3
    0   0   0   0   0
So, the next value of the first history is 18.

Finding all-zero differences for the second history requires an additional sequence:

1   3   6  10  15  21
  2   3   4   5   6
    1   1   1   1
      0   0   0
Then, following the same process as before, work out the next value in each sequence from the bottom up:

1   3   6  10  15  21  28
  2   3   4   5   6   7
    1   1   1   1   1
      0   0   0   0
So, the next value of the second history is 28.

The third history requires even more sequences, but its next value can be found the same way:

10  13  16  21  30  45  68
   3   3   5   9  15  23
     0   2   4   6   8
       2   2   2   2
         0   0   0
So, the next value of the third history is 68.

If you find the next value for each history in this example and add them together, you get 114.

Analyze your OASIS report and extrapolate the next value for each history. What is the sum of these extrapolated values?
"""

import numpy as np 

total_sum = 0

# import data from numpy
data = np.loadtxt("p09-input.txt", dtype='int') 

for row in data:
    diff_list = [row]
    # Determine the number of rows needed
    num_rows = len(row) - 1

    # Iteratively calculate differences
    while True:
        # Compute the differences of the last row in the list
        current_diff = np.diff(diff_list[-1])

        # Append the differences to the list
        diff_list.append(current_diff)

        # Break if the length of current_diff is 1 (cannot compute further differences)
        if len(current_diff) == 1:
            break

        # Check if all elements in the current row are 0 (or NaN, but NaNs are not expected here)
        if np.all(current_diff == 0):
            break

    # Convert the list of arrays into a 2D array, filling with NaN for missing values
    max_length = max(len(row) for row in diff_list)
    diff_matrix = np.full((len(diff_list), max_length), np.nan)

    for i, row in enumerate(diff_list):
        diff_matrix[i, :len(row)] = row

    print(f"Original table: ")
    print(diff_matrix)

    # Find the index of the first NaN element in the second to last row
    nan_index = np.where(np.isnan(diff_matrix[-2]))[0][0]

    #For this NaN element, replace it with its value to the left
    diff_matrix[-2][nan_index] = diff_matrix[-2][nan_index-1]
    print(f"New diff matrix is:")
    print(diff_matrix)
    
    #Then for every OTHER first NaN element, it should be the sum of the value to the left, plus the value beneath it

print(f"Sum of extrapolated values is {total_sum}")