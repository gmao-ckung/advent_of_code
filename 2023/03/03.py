import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/input.in","r")

# Read lines within input file and remove new line character at the line's end
engine_schematic_file = file.read().splitlines()

number_location = {}
symbol_location = {}

row = 0
for line in engine_schematic_file:
    number = ""
    number_coord = []
    column = 0
    for char in line:
        if char.isdigit():
            number += char
            number_coord.append([row, column])
        elif char == ".":
            if number != "":
                if number not in number_location.keys():
                    number_location[number] = [number_coord]
                else:
                    number_location[number].append(number_coord)
                number = ""
                number_coord = []
        else:
            if number != "":
                if number not in number_location.keys():
                    number_location[number] = [number_coord]
                else:
                    number_location[number].append(number_coord)
                number = ""
                number_coord = []
            if char not in symbol_location.keys():
                symbol_location[char] = [[row,column]]
            else:
                symbol_location[char].append([row,column])
        column += 1
    
    if number != "":
        if number not in number_location.keys():
            number_location[number] = [number_coord]
        else:
            number_location[number].append(number_coord)
    row += 1
    
# *** Parts 1 and 2 ***

sum_part1 = 0
sum_part2 = 0

for symbol in symbol_location.keys():
    # print(symbol)
    for symbol_coord in symbol_location[symbol]:
        # print(symbol_coord)
        neighboring_parts = []
        for number in number_location.keys():
            # print(number)
            # print(number_location[number])

            for number_coord_L1 in number_location[number]:
                for number_coord in number_coord_L1:
                    # print(number_coord)
                    # Check whether symbol is in same row as the number
                    if(symbol_coord[0] == number_coord[0]):
                        if(abs(symbol_coord[1] - number_coord[1]) == 1):
                            # print("Number = ", number)
                            # print("Adjacent number to symbol ", symbol)
                            # print("Symbol Coord = ", symbol_coord)
                            # print("Number Coord = ", number_location[number])
                            # print("***")
                            sum_part1 += int(number)
                            neighboring_parts.append(int(number))
                            break
                    
                    # Check whether symbol is above the number
                    elif(symbol_coord[0]+1 == number_coord[0]):
                        if(abs(symbol_coord[1] - number_coord[1]) <= 1):
                            # print("Number = ", number)
                            # print("Adjacent number to symbol ", symbol)
                            # print("Symbol Coord = ", symbol_coord)
                            # print("Number Coord = ", number_location[number])
                            # print("***")
                            sum_part1 += int(number)
                            neighboring_parts.append(int(number))
                            break

                    # Check whether symbol is below the number
                    elif(symbol_coord[0]-1 == number_coord[0]):
                        if(abs(symbol_coord[1] - number_coord[1]) <= 1):
                            # print("Number = ", number)
                            # print("Adjacent number to symbol ", symbol)
                            # print("Symbol Coord = ", symbol_coord)
                            # print("Number Coord = ", number_location[number])
                            # print("***")
                            sum_part1 += int(number)
                            neighboring_parts.append(int(number))
                            break
        if(len(neighboring_parts) == 2):
            sum_part2 += neighboring_parts[0] * neighboring_parts[1]

print("Part 1: Sum of parts = ", sum_part1)
print('Sum of gear ratios = ', sum_part2)
