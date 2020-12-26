import os
import numpy as np
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.test")
tile_data = f1.readlines()

tile_data = {}

for line in tile_data:
    line = line.replace("\n","")
    print(line)
    if line[0:4] == 'Tile':
        tile_data = np.zeros((10,10), dtype=int)
        print(tile_data)