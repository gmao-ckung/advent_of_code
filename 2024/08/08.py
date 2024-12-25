import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.08","r")

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
    # print(key)
    for index0 in range(len(map_dict[key])):
        # print("Point 0:", map_dict[key][index0])
        for index1 in range(index0+1, len(map_dict[key])):
            # print("Point 1:",map_dict[key][index1])

            x_diff = abs(map_dict[key][index0][0] - map_dict[key][index1][0])
            y_diff = abs(map_dict[key][index0][1] - map_dict[key][index1][1])

            if(map_dict[key][index0][0] > map_dict[key][index1][0]):
                factor0 = 1
                factor1 = -1
            else:
                factor0 = -1
                factor1 = 1

            null_x_coord0 = map_dict[key][index0][0] + x_diff*factor0
            null_x_coord1 = map_dict[key][index1][0] + x_diff*factor1

            if(map_dict[key][index0][1] > map_dict[key][index1][1]):
                factor0 = 1
                factor1 = -1
            else:
                factor0 = -1
                factor1 = 1

            null_y_coord0 = map_dict[key][index0][1] + y_diff*factor0
            null_y_coord1 = map_dict[key][index1][1] + y_diff*factor1

            # print([null_x_coord0, null_y_coord0])
            # print([null_x_coord1, null_y_coord1])

            if null_x_coord0 < max_row and null_x_coord0 >= 0 and null_y_coord0 < max_col and null_y_coord0 >= 0:
                if [null_x_coord0, null_y_coord0] not in null_locations:
                    null_locations.append([null_x_coord0, null_y_coord0])
            if null_x_coord1 < max_row and null_x_coord1 >= 0 and null_y_coord1 < max_col and null_y_coord1 >= 0:
                if [null_x_coord1, null_y_coord1] not in null_locations:
                    null_locations.append([null_x_coord1, null_y_coord1])
            # print("----")

print('Part 1: Number of Unique Null Locations =', len(null_locations))

null_locations = []

for key in map_dict.keys():
    # print(key)
    for index0 in range(len(map_dict[key])):
        # print("Point 0:", map_dict[key][index0])
        for index1 in range(index0+1, len(map_dict[key])):
            # print("Point 1:",map_dict[key][index1])

            x_diff = abs(map_dict[key][index0][0] - map_dict[key][index1][0])
            y_diff = abs(map_dict[key][index0][1] - map_dict[key][index1][1])

            if(map_dict[key][index0][0] > map_dict[key][index1][0]):
                factor0_0 = 1
                factor1_0 = -1
            else:
                factor0_0 = -1
                factor1_0 = 1

            if(map_dict[key][index0][1] > map_dict[key][index1][1]):
                factor0_1 = 1
                factor1_1 = -1
            else:
                factor0_1 = -1
                factor1_1 = 1

            out_of_bounds = False
            scale_factor = 1
            while not out_of_bounds:

                null_x_coord0 = map_dict[key][index0][0] + x_diff*factor0_0*scale_factor
                null_y_coord0 = map_dict[key][index0][1] + y_diff*factor0_1*scale_factor
                
                if null_x_coord0 < max_row and null_x_coord0 >= 0 and null_y_coord0 < max_col and null_y_coord0 >= 0:
                    if [null_x_coord0, null_y_coord0] not in null_locations:
                        null_locations.append([null_x_coord0, null_y_coord0])
                    scale_factor += 1
                else:
                    out_of_bounds = True

            out_of_bounds = False
            scale_factor = 1
            while not out_of_bounds:

                null_x_coord1 = map_dict[key][index1][0] + x_diff*factor1_0*scale_factor
                null_y_coord1 = map_dict[key][index1][1] + y_diff*factor1_1*scale_factor

                if null_x_coord1 < max_row and null_x_coord1 >= 0 and null_y_coord1 < max_col and null_y_coord1 >= 0:
                    if [null_x_coord1, null_y_coord1] not in null_locations:
                        null_locations.append([null_x_coord1, null_y_coord1])
                    scale_factor += 1
                else:
                    out_of_bounds = True

total_antennas = 0
for key in map_dict.keys():
    for ant_coord in map_dict[key]:
        if ant_coord not in null_locations:
            total_antennas += 1

print('Part 2: Number of Unique Null Locations =', len(null_locations) + total_antennas)