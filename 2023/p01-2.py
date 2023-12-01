#!/usr/bin/python3
"""
--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""
from words2num import words2num

wordList = []
valueList = []

#Build a list of words
with open("p01-input.txt", 'r', newline='\n') as file:
    for line in file:
        wordList.append(line.rstrip())

for word in wordList:
    firstNumberIndex = 0
    lastNumberIndex = 0
    firstWordIndex = -1
    lastWordIndex = -1
    firstWord = ""
    lastWord = ""
    digit1 = ""
    digit2 = ""

    for i, char in enumerate(word):
        if char.isdigit():
            digit1 = char
            firstNumberIndex = i
            break
    for i, char in enumerate(reversed(word)):
        if char.isdigit():
            digit2 = char
            lastNumberIndex = len(word) - i 
            break

    # Get all substrings of string
    # Using nested loops
    for i in range(len(word)):
        for j in range(i+1, len(word)+1):
            try:
                if words2num(word[i:j]):
                    if firstWordIndex == -1: #If firstWordIndex isn't initialized, set it
                        firstWordIndex = i
                        firstWord = words2num(word[i:j])
                    if i >= lastWordIndex:
                        lastWordIndex = i
                        lastWord = words2num(word[i:j])          
            except:    
                continue
    if firstNumberIndex >= firstWordIndex and firstWord != "":
        digit1 = str(firstWord)[0] #Get first digit of first word2num
    if lastNumberIndex <= lastWordIndex and lastWord != "":
        digit2 = str(lastWord)[-1] #Get last digit of last word2num

    print(f"{word}: {digit1} , {digit2}")
    value = digit1 + digit2
    valueList.append(int(value))

print(f"The sum of calibration values (phase 2) is {sum(valueList)}")