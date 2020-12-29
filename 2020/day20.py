import os
import numpy as np
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day20")
tile_data = f1.readlines()

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

for i in range(len(keys)):
    i_matches = []
    for j in range(len(keys)):
        if i != j:
            # Check if "j" attaches to "i" from the south
            if np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][0,:]) or \
            np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][0,::-1]) or \
            np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][-1,:]) or \
            np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][-1,::-1]) or \
            np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][:,0]) or \
            np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][::-1,0]) or \
            np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][:,-1]) or \
            np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][::-1,-1]):
                i_matches.append(j)
            # Check if "j" attaches to "i" from the north
            elif np.array_equal(tile_image_data[keys[i]][-1,:],tile_image_data[keys[j]][0,:]) or \
                np.array_equal(tile_image_data[keys[i]][-1,:],tile_image_data[keys[j]][0,::-1]) or \
                np.array_equal(tile_image_data[keys[i]][-1,:],tile_image_data[keys[j]][-1,:]) or \
                np.array_equal(tile_image_data[keys[i]][-1,:],tile_image_data[keys[j]][-1,::-1]) or \
                np.array_equal(tile_image_data[keys[i]][-1,:],tile_image_data[keys[j]][:,0]) or \
                np.array_equal(tile_image_data[keys[i]][-1,:],tile_image_data[keys[j]][::-1,0]) or \
                np.array_equal(tile_image_data[keys[i]][-1,:],tile_image_data[keys[j]][:,-1]) or \
                np.array_equal(tile_image_data[keys[i]][-1,:],tile_image_data[keys[j]][::-1,-1]):
                i_matches.append(j)
            # Check if "j" attaches to "i" from the west
            elif np.array_equal(tile_image_data[keys[i]][:,0],tile_image_data[keys[j]][0,:]) or \
            np.array_equal(tile_image_data[keys[i]][:,0],tile_image_data[keys[j]][0,::-1]) or \
            np.array_equal(tile_image_data[keys[i]][:,0],tile_image_data[keys[j]][-1,:]) or \
            np.array_equal(tile_image_data[keys[i]][:,0],tile_image_data[keys[j]][-1,::-1]) or \
            np.array_equal(tile_image_data[keys[i]][:,0],tile_image_data[keys[j]][:,0]) or \
            np.array_equal(tile_image_data[keys[i]][:,0],tile_image_data[keys[j]][::-1,0]) or \
            np.array_equal(tile_image_data[keys[i]][:,0],tile_image_data[keys[j]][:,-1]) or \
            np.array_equal(tile_image_data[keys[i]][:,0],tile_image_data[keys[j]][::-1,-1]):
                i_matches.append(j)        
            # Check if "j" attaches to "i" from the east
            elif np.array_equal(tile_image_data[keys[i]][:,-1],tile_image_data[keys[j]][0,:]) or \
            np.array_equal(tile_image_data[keys[i]][:,-1],tile_image_data[keys[j]][0,::-1]) or \
            np.array_equal(tile_image_data[keys[i]][:,-1],tile_image_data[keys[j]][-1,:]) or \
            np.array_equal(tile_image_data[keys[i]][:,-1],tile_image_data[keys[j]][-1,::-1]) or \
            np.array_equal(tile_image_data[keys[i]][:,-1],tile_image_data[keys[j]][:,0]) or \
            np.array_equal(tile_image_data[keys[i]][:,-1],tile_image_data[keys[j]][::-1,0]) or \
            np.array_equal(tile_image_data[keys[i]][:,-1],tile_image_data[keys[j]][:,-1]) or \
            np.array_equal(tile_image_data[keys[i]][:,-1],tile_image_data[keys[j]][::-1,-1]):
                i_matches.append(j) 

    if len(i_matches) == 2:
        corner_keys.append(keys[i])

print("Part 1: Mutliplication of 4 corners =", corner_keys[0]* corner_keys[1]*corner_keys[2]*corner_keys[3])

