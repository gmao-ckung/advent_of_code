import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.test","r")

map = file.read().splitlines()

map_dict = {}
row = 0
for map_line in map:
    col = 0
    for char in map_line:
        if char != '.':
            if char not in map_dict.keys():
                map_dict[char] = [[row, col]]
            else:
                map_dict[char].append([row, col])
        col += 1
    row += 1

max_row = row
max_col = col

# print(map_dict)

null_locations = []

for key in map_dict.keys():
    print(key)
    for index0 in range(len(map_dict[key])):
        print("Point 0:", map_dict[key][index0])
        for index1 in range(index0+1, len(map_dict[key])):
            print("Point 1:",map_dict[key][index1])

            x_diff = abs(map_dict[key][index0][0] - map_dict[key][index1][0])
            y_diff = abs(map_dict[key][index0][1] - map_dict[key][index1][1])
            if(x_diff > 0):
                # Look at index0 point
                if(map_dict[key][index0][0] > map_dict[key][index1][0]):
                    factor0 = 1
                    factor1 = -1
                else:
                    factor0 = -1
                    factor1 = 1

                null_x_coord0 = map_dict[key][index0][0] + x_diff*factor0
                null_x_coord1 = map_dict[key][index1][0] + x_diff*factor1
            if (y_diff > 0):
                # Look at index0 point
                if(map_dict[key][index0][1] > map_dict[key][index1][1]):
                    factor0 = 1
                    factor1 = -1
                else:
                    factor0 = -1
                    factor1 = 1

                null_y_coord0 = map_dict[key][index0][1] + y_diff*factor0
                null_y_coord1 = map_dict[key][index1][1] + y_diff*factor1

            print([null_x_coord0, null_y_coord0])
            print([null_x_coord1, null_y_coord1])

            if null_x_coord0 < max_row and null_x_coord0 >= 0 and null_y_coord0 < max_col and null_y_coord0 >= 0:
                if [null_x_coord0, null_y_coord0] not in null_locations:
                    null_locations.append([null_x_coord0, null_y_coord0])
            if null_x_coord1 < max_row and null_x_coord1 >= 0 and null_y_coord1 < max_col and null_y_coord1 >= 0:
                if [null_x_coord1, null_y_coord1] not in null_locations:
                    null_locations.append([null_x_coord1, null_y_coord1])
            print("----")

shared_location = 0
for null in null_locations:
    for key in map_dict.keys():
        if null in map_dict[key]:
            print("Shared Location:", null)
            shared_location += 1

print('Number of Unique Null Locations =', len(null_locations)- shared_location)