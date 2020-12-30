import os
import numpy as np
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.test")
tile_data = f1.readlines()

def check_borders(tile_image_data_0, tile_image_data_1):
    temp_image = tile_image_data_1
    
    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "south" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[0,:], temp_image[-1,:]):
            return True, temp_image
            break
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)
        
    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "north" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[-1,:], temp_image[0,:]):
            return True, temp_image
            break
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)

    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "west" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[:,0], temp_image[:,-1]):
            return True, temp_image
            break
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)

    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "east" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[:,-1], temp_image[:,0]):
            return True, temp_image
            break
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)


    return False, 0

tile_image_data = {}

for line in tile_data:
    line = line.replace("\n","")
    #print(line)
    if line[0:4] == 'Tile':
        tile_number = int((line.split(" ")[1].replace(":","")))
        tile_data = np.zeros((10,10), dtype=int)
        #print(tile_data)
        curr_row = 0
    
    elif line != "":
        #print(curr_row)
        for i in range(len(line)):
            if line[i] == '#':
                tile_data[curr_row,i] = 1
        curr_row += 1

    else:
        tile_image_data[tile_number] = tile_data

tile_image_data[tile_number] = tile_data

keys = list(tile_image_data.keys())

corner_keys = []

border_tiles = {}
for key in keys:
    border_tiles[key] = []

for i in range(len(keys)):
    for j in range(i+1,len(keys)):
        found, adjustedArray = check_borders(tile_image_data[keys[i]], tile_image_data[keys[j]])
        if found:
            tile_image_data[keys[j]] = adjustedArray
            border_tiles[keys[i]].append(keys[j])
            border_tiles[keys[j]].append(keys[i])
            

for i in range(len(keys)):
    if len(border_tiles[keys[i]]) == 2:
        corner_keys.append(keys[i])

print("Part 1: Mutliplication of 4 corners =", corner_keys[0]* corner_keys[1]*corner_keys[2]*corner_keys[3])

# # Find number of tiles in each direction starting from a corner

# current_tile = tile_image_data[corner_keys[0]]

# print(current_tile)

# #Going either north or south to find "height"
# height_not_found = True

# while(height_not_found):
#     while 