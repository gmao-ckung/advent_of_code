import numpy as np
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day2","r")
passLine = fopen.readlines()

# print(passLine)
horiz_len = 0
depth_len = 0

# *** Part 1 ***
for line in passLine:
    # Split each line entry into a list
    split_direction_len = line.split(" ")

    direction = split_direction_len[0]
    # Removes the newline character from the number
    length = split_direction_len[1].replace("\n","")
    # print(direction)
    # print(length)

    if direction == "forward":
        horiz_len += int(length)

    if direction == "up":
        depth_len -= int(length)

    if direction == "down":
        depth_len += int(length)

print("For part 1...")
print("Horizontal Length = ", horiz_len)
print("Depth = ", depth_len)
print("Multiplication = ", horiz_len*depth_len)

# *** Part 2 ***

aim = 0
horiz_len = 0
depth_len = 0

for line in passLine:
    # Split each line entry into a list
    split_direction_len = line.split(" ")

    direction = split_direction_len[0]
    # Removes the newline character from the number
    length = split_direction_len[1].replace("\n","")
    
    if direction == "forward":
        horiz_len += int(length)
        depth_len += aim * int(length)

    if direction == "up":
        aim -= int(length)

    if direction == "down":
        aim += int(length)

print("For part 2...")
print("Horizontal Length = ", horiz_len)
print("Depth = ", depth_len)
print("Multiplication = ", horiz_len*depth_len)