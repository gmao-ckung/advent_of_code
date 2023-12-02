import os
import re
# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/input1.test","r")

# Read lines within input file and remove new line character at the line's end
lines = file.read().splitlines()

# *** Part 1 ***
sum = 0

for line in lines:
    # Store numbers found in each line
    num_list = []
    # Step through line character by character to determine if it's a digit.
    # If so, append the digit (as a character/string) into num_list
    for char in line:
        if(char.isdigit()):
            num_list.append(char)
    # print(num_list)
    # Create an integer based on the first and last numbers of the list
    number = int(num_list[0] + num_list[-1])
    sum += number

print("Part 1 : Sum = ", sum)

file.close()
# *** Part 2 ***
file = open(CURR_DIR+"/input.in","r")
lines = file.read().splitlines()

# Python's "regular expressions" can find string occurances and their locations

num_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", 
            "1","2","3","4","5","6","7","8","9"]
sum = 0
for line in lines:
    start_num = ""
    start_loc = len(line)
    end_num = ""
    end_loc = 0
    for num in num_list:
        for loc in re.finditer(num, line):
            # print("In ", line, " : ", num, " found at", loc.start())
            if(loc.start() <= start_loc):
                start_loc = loc.start()
                start_num = num
            if(loc.start() >= end_loc):
                end_loc = loc.start()
                end_num = num
    # print("line = ", line)
    # print("start_num = ", start_num)
    # print("end_num = ", end_num)

    # Identify location in num_list that contains start_number and end_number
    start_number = [i for i,x in enumerate(num_list) if x == start_num]
    end_number = [i for i,x in enumerate(num_list) if x == end_num]

    # Perform a modulo calculation that transforms the location to the actual number
    # print("start number = ", start_number[0]%9+1)
    # print("end number = ", end_number[0]%9+1)

    # Scale start_number by 10 to get proper location in sum
    sum += (start_number[0]%9+1)*10 + end_number[0]%9+1

print("Part 2 : Sum = ", sum)
file.close()