import os
import numpy as np
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.test")
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

for i in range(len(keys)):
    for j in range(i,len(keys)):
        # Check if "j" attaches to "i" from the south
        if np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][0,:]) or \
           np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][0,::-1]) or \
           np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][-1,:]) or \
           np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][-1,::-1]) or \
           np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][:,0]) or \
           np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][::-1,0]) or \
           np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][:,-1]) or \
           np.array_equal(tile_image_data[keys[i]][0,:],tile_image_data[keys[j]][::-1,-1]):
            print("Combo Found!")
        # Check if "j" attaches to "i" from the north
        # Check if "j" attaches to "i" from the west
        # Check if "j" attaches to "i" from the east