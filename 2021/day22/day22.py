import os
import sys

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")
cube_coords = fopen.readlines()

min_range = -50
max_range = 50

cube_dict = {}

step = 0

for directions in cube_coords:

    directions = directions.replace("\n","").split(" ")
    on_or_off = directions[0]
    x_range = directions[1].split(",")[0].replace("x=","").split("..")
    y_range = directions[1].split(",")[1].replace("y=","").split("..")
    z_range = directions[1].split(",")[2].replace("z=","").split("..")
    

    if int(x_range[0]) >= min_range: 
        if int(x_range[0]) <= max_range:
            x_min = int(x_range[0])
        else:
            continue
    elif int(x_range[0]) <= max_range:
        x_min = min_range
    else:
        continue
    
    if int(x_range[1]) <= max_range:
        if int(x_range[0]) >= min_range:
            x_max = int(x_range[1])
        else:
            continue
    elif int(x_range[0]) >= min_range:
        x_max = max_range
    else:
        continue

    if int(y_range[0]) >= min_range: 
        if int(y_range[0]) <= max_range:
            y_min = int(y_range[0])
        else:
            continue
    elif int(y_range[0]) <= max_range:
        y_min = min_range
    else:
        continue
    
    if int(y_range[1]) <= max_range:
        if int(y_range[0]) >= min_range:
            y_max = int(y_range[1])
        else:
            continue
    elif int(y_range[0]) >= min_range:
        y_max = max_range
    else:
        continue

    if int(z_range[0]) >= min_range: 
        if int(z_range[0]) <= max_range:
            z_min = int(z_range[0])
        else:
            continue
    elif int(z_range[0]) <= max_range:
        z_min = min_range
    else:
        continue
    
    if int(z_range[1]) <= max_range:
        if int(z_range[0]) >= min_range:
            z_max = int(z_range[1])
        else:
            continue
    elif int(z_range[0]) >= min_range:
        z_max = max_range
    else:
        continue


    for z_index in range(z_min, z_max+1):
        for y_index in range(y_min, y_max+1):
            for x_index in range(x_min, x_max+1):
                index_key = str(x_index)+","+str(y_index)+","+str(z_index)
                if on_or_off == "on":
                    if index_key not in cube_dict.keys():
                        cube_dict[index_key] = 1
                elif on_or_off == "off":
                    if index_key in cube_dict.keys():
                        cube_dict.pop(index_key)

print("Length of cube_dict = ", len(cube_dict))

num_cubes = 0
range_covered = {}
for directions in cube_coords:
    directions = directions.replace("\n","").split(" ")
    on_or_off = directions[0]
    x_range = directions[1].split(",")[0].replace("x=","").split("..")
    y_range = directions[1].split(",")[1].replace("y=","").split("..")
    z_range = directions[1].split(",")[2].replace("z=","").split("..")

    if on_or_off == "on":
        if len(range_covered) == 0:
            x_len = int(x_range[1]) - int(x_range[0]) + 1
            y_len = int(y_range[1]) - int(y_range[0]) + 1
            z_len = int(z_range[1]) - int(z_range[0]) + 1

            num_cubes += x_len * y_len * z_len

print("Number of cubes = ", num_cubes)