import os
import numpy as np

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.03","r")

memory = file.read().splitlines()

do_compute = True

total_result = 0
for section in memory:
    index = 0
    while index < len(section)-4:
        if section[index:index+4] == 'mul(':
            # print('index = ', index)
            # print(section[index:index+4])
            index = index+4
            left = ''
            right = ''
            while(section[index].isdigit()):
                left += section[index]
                index += 1
            if(section[index] == ','):
                index += 1
                while(section[index].isdigit()):
                    right += section[index]
                    index += 1
                if(section[index] == ')'):
                    # print("Valid combination found!")
                    left = int(left)
                    right = int(right)
                    total_result += left * right
                    index += 1
                else:
                    # print("Invalid combination found!")
                    index += 1
            else:
                # print("Invalid combination found!")
                index += 1
        else:
            index += 1

print("Part 1 : Result = ", total_result)

total_result = 0
for section in memory:
    index = 0
    while index < len(section)-4:
        if section[index:index+4] == 'mul(' and do_compute:
            # print('index = ', index)
            # print(section[index:index+4])
            index = index+4
            left = ''
            right = ''
            while(section[index].isdigit()):
                left += section[index]
                index += 1
            if(section[index] == ','):
                index += 1
                while(section[index].isdigit()):
                    right += section[index]
                    index += 1
                if(section[index] == ')'):
                    # print("Valid combination found!")
                    left = int(left)
                    right = int(right)
                    total_result += left * right
                    index += 1
                else:
                    # print("Invalid combination found!")
                    index += 1
            else:
                # print("Invalid combination found!")
                index += 1
        elif section[index:index+4] == 'do()':
            index += 4
            do_compute = True
        elif section[index:index+7] == "don't()":
            index += 7
            do_compute = False
        else:
            index += 1

print("Part 2 : Result = ", total_result)