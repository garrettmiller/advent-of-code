#!/usr/bin/python3
"""
--- Part Two ---
The Elf says they've stopped producing snow because they aren't getting any water! He isn't sure why the water stopped; however, he can show you how to get to the water source to check it out for yourself. It's just up ahead!

As you continue your walk, the Elf poses a second question: in each game you played, what is the fewest number of cubes of each color that could have been in the bag to make the game possible?

Again consider the example games from earlier:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively. Adding up these five powers produces the sum 2286.

For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
"""

import re

sum = 0

# Initialize a dictionary to store game data
games_data = {}

#Build a list of games
with open("p02-input.txt", 'r') as file:
    for line in file:
        # Extract the game number using regular expression
        game_number = int(re.search(r'Game (\d+)', line).group(1))

        # Split the line into game title and trials
        _, trials = line.split(': ')
        trials = trials.strip().split('; ')

        # Initialize a dictionary for each game
        games_data[game_number] = []

        # Process each trial
        for trial in trials:
            trial_data = {}
            # Split the trial into color counts
            colors = trial.split(', ')
            for color in colors:
                count, color_name = color.split(' ')
                trial_data[color_name] = int(count)
            games_data[game_number].append(trial_data)

for game, trials in games_data.items():
    minRed = 0
    minGreen = 0
    minBlue = 0 
    for trial in trials:
        for color, count in trial.items():
            if color == "red" and count >= minRed:
                minRed = count
            if color == "blue" and count >= minBlue:
                minBlue = count
            if color == "green" and count >= minGreen:
                minGreen = count

    sum = sum + (minRed * minGreen * minBlue)            

print(f"The sum of game numbers of possible games is {sum}")
