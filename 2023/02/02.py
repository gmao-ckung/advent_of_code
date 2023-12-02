import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/input.in","r")

# Read lines within input file and remove new line character at the line's end
games = file.read().splitlines()

bag_contains = {'red': 12, 'green': 13, 'blue': 14}

# *** Part 1 ***

idSum = 0
for game in games:
    # print(game)
    # Parse out game number
    game_label = game.split(":")[0]
    game_number = game_label.split(" ")[1]
    # print(game_number)

    # Parse out color groupings
    color_groups = game.split(": ")[1].split("; ")
    # print(color_groups)

    num_invalid_groups = 0
    for group in color_groups:
        # print(group)
        
        # Parse out subgroups of colors
        color_grouping = group.split(", ")
        # print(color_grouping)

        # Iterate over color subgroups to determine whether their
        # configuration is valid
        for num_and_color in color_grouping:
            number = num_and_color.split(" ")[0]
            color = num_and_color.split(" ")[1]
            if bag_contains[color] < int(number):
                num_invalid_groups += 1
    if num_invalid_groups == 0:
        idSum += int(game_number)

print("Part 1 : Sum of IDs = ", idSum)

power_sum = 0

for game in games:
    # Start with empty bag
    bag_contains = {'red': 0, 'green': 0, 'blue': 0}
    color_groups = game.split(": ")[1].split("; ")
    # print(color_groups)

    # Iterate over color subgroups
    for group in color_groups:
        color_grouping = group.split(", ")
        # Isolate number and color within each subgroup and determine
        # whether more of a particular color should be added to the bag
        for num_and_color in color_grouping:
            number = num_and_color.split(" ")[0]
            color = num_and_color.split(" ")[1]
            if bag_contains[color] < int(number):
                bag_contains[color] = int(number)
    
    # Calculate power of each game
    power = 1
    for id in bag_contains.keys():
        # print("Color ", id, " has ", bag_contains[id])
        power = power*int(bag_contains[id])

    # Add to power sum
    # print("Game ", game_number, ": Power = ", power)
    power_sum += power

print("Part 2 : Power Sum = ", power_sum)
file.close()