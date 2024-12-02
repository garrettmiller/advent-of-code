#!/usr/bin/python3
"""
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?
"""

safeTotal = 0

#Just run is_safe multiple times with each level removed, we can accept any one error
def is_safe_with_dampener(report):
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1:]):
            return True

def is_safe(report):
    if len(report) < 2:
        return True  # A report with less than 2 levels is trivially safe
    increasing = None
    for i in range(len(report) - 1):
        if report[i] == report[i + 1]: # If levels are the same, unsafe
            return False
        if increasing is None: #we don't know if it's increasing or decreasing yet
            increasing = report[i] < report[i + 1]
        elif (increasing and report[i] > report[i + 1]) or (not increasing and report[i] < report[i + 1]):
            return False
        if abs(report[i] - report[i + 1]) > 3: #ensure the change is no greater than 3
            return False
    return True

# Open the file for reading
with open('p02-input.txt', 'r') as file:
    # Initialize an empty list to store the reports
    reports = []
    # Iterate over each line in the file
    for line in file:
        # Split the line into individual numbers and convert them to integers
        levels = list(map(int, line.strip().split()))
        # Append the list of levels to the reports list
        reports.append(levels)

for report in reports:
    if is_safe_with_dampener(report):
        print(f"{report} is safe")
        safeTotal += 1

print(f"Total safe reports: {safeTotal}")