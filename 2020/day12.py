import os
import math
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day12")
directions = f1.readlines()

# Note: Initial direction is eastward

rotation_deg = 0
EW_position = 0
NS_position = 0

def rad(degrees):
    return degrees*math.pi/180

for direction in directions:
    direction = direction.replace("\n","")
    action = direction[0]
    value = int(direction[1:])

    if action == 'F':
        EW_position = EW_position + math.cos(rad(rotation_deg)) * value
        NS_position = NS_position + math.sin(rad(rotation_deg)) * value

    elif action == 'N':
        NS_position = NS_position + value

    elif action == 'S':
        NS_position = NS_position - value
    
    elif action == 'E':
        EW_position = EW_position + value

    elif action == 'W':
        EW_position = EW_position - value

    elif action == 'L':
        rotation_deg = rotation_deg + value

    elif action == 'R':
        rotation_deg = rotation_deg - value

man_dist = abs(EW_position) + abs(NS_position)

print("Part 1: Manhattan Distance =", man_dist)