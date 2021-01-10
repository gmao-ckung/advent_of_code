import os
import math
import numpy as np
import numpy.ma as ma
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day20")
tile_data = f1.readlines()

def check_borders(tile_image_data_0, tile_image_data_1):
    temp_image = tile_image_data_1
    
    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "south" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[0,:], temp_image[-1,:]):
            return True, temp_image
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)
        
    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "north" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[-1,:], temp_image[0,:]):
            return True, temp_image
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)

    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "west" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[:,0], temp_image[:,-1]):
            return True, temp_image
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)

    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "east" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[:,-1], temp_image[:,0]):
            return True, temp_image
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)


    return False, 0

def find_direction(tile_image_data_0, tile_image_data_1):
    temp_image = tile_image_data_1

    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "south" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[0,:], temp_image[-1,:]):
            return "south", temp_image
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)
    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "north" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[-1,:], temp_image[0,:]):
            return "north", temp_image
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)

    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "west" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[:,0], temp_image[:,-1]):
            return "west", temp_image
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)
    # Testing for match by rotating tile_image_data_1 and seeing if it attaches to the "east" of
    # tile_image_data_0
    for i in range(8):
        if np.array_equal(tile_image_data_0[:,-1], temp_image[:,0]):
            return "east", temp_image
        else:
            temp_image = np.rot90(temp_image)
            if i == 3:
                temp_image = np.fliplr(temp_image)
    return "null", 0

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
            #
            # tile_image_data[keys[j]] = adjustedArray
            border_tiles[keys[i]].append(keys[j])
            border_tiles[keys[j]].append(keys[i])
            

for i in range(len(keys)):
    if len(border_tiles[keys[i]]) == 2:
        corner_keys.append(keys[i])

print("Part 1: Mutliplication of 4 corners =", corner_keys[0]* corner_keys[1]*corner_keys[2]*corner_keys[3])

# ***Part 2 ***

# Establish dimensions of overall image
squares_per_side = int(math.sqrt(len(keys)))
x_len_overall_image = squares_per_side * (tile_image_data[keys[0]].shape[0]-2)
overall_image = np.zeros((x_len_overall_image,x_len_overall_image),dtype=int)

# Start building image from a tile corner
current_tile_num = corner_keys[0]
#print("Current Tile =", current_tile_num)
W_found = False
E_found = False
N_found = False
S_found = False

for i in range(len(border_tiles[current_tile_num])):
    if border_tiles[current_tile_num][i] in keys:
        direction, adjustedArray = find_direction(tile_image_data[current_tile_num], \
                                                tile_image_data[border_tiles[current_tile_num][i]])
        if direction == "east":
            E_found = True
            tile_image_data[border_tiles[current_tile_num][i]] = adjustedArray
        elif direction == "west":
            W_found = True
            tile_image_data[border_tiles[current_tile_num][i]] = adjustedArray
        elif direction == "north":
            N_found = True
            tile_image_data[border_tiles[current_tile_num][i]] = adjustedArray
            next_tile_num = border_tiles[current_tile_num][i]
        elif direction == "south":
            S_found = True
            tile_image_data[border_tiles[current_tile_num][i]] = adjustedArray
            next_tile_num = border_tiles[current_tile_num][i]

if E_found and S_found:
    tile_origin = [(squares_per_side-1)*8,0]
    
elif E_found and N_found:
    tile_origin = [0,0]

elif W_found and S_found:
    tile_origin = [(squares_per_side-1)*8,(squares_per_side-1)*8]

elif W_found and N_found:
    tile_origin = [0, (squares_per_side-1)*8]

overall_image[tile_origin[0]:tile_origin[0]+8,
                tile_origin[1]:tile_origin[1]+8] = tile_image_data[current_tile_num][1:-1,1:-1]

if S_found:
    tile_origin[0] -= 8

elif N_found:
    tile_origin[0] += 8

keys.remove(current_tile_num)
current_tile_num = next_tile_num

while len(keys) > 0:
    #print("Current tile =",current_tile_num)
    keys.remove(current_tile_num)
    overall_image[tile_origin[0]:tile_origin[0]+8,
                tile_origin[1]:tile_origin[1]+8] = tile_image_data[current_tile_num][1:-1,1:-1]
    N_or_S_found = False
    E_or_W_index = 0
    for i in range(len(border_tiles[current_tile_num])):
        if border_tiles[current_tile_num][i] in keys:
            E_or_W_index = i
            #print(border_tiles[current_tile_num][i])
            direction, adjustedArray = find_direction(tile_image_data[current_tile_num], \
                                                    tile_image_data[border_tiles[current_tile_num][i]])
            #print(border_tiles[current_tile_num][i],"is going in the direction =", direction)

            if direction == "south" or direction == "north":
                N_or_S_found = True
                if direction == "south":
                    tile_origin[0] -= 8
                if direction == "north":
                    tile_origin[0] += 8
                current_tile_num = border_tiles[current_tile_num][i]
                tile_image_data[current_tile_num] = adjustedArray
                break

    if N_or_S_found == False:
       # print("N or S not found!")
        current_tile_num = border_tiles[current_tile_num][E_or_W_index]
        tile_image_data[current_tile_num] = adjustedArray
        if direction == "east":
            tile_origin[1] += 8
        if direction == "west":
            tile_origin[1] -= 8

#print(overall_image)

# Create Sea Monster
sea_monster = np.zeros((3,20),dtype=int)
sea_monster[0,1] = True
sea_monster[0,4] = True
sea_monster[0,7] = True
sea_monster[0,10] = True
sea_monster[0,13] = True
sea_monster[0,16] = True
sea_monster[1,0] = True
sea_monster[1,5] = True
sea_monster[1,6] = True
sea_monster[1,11] = True
sea_monster[1,12] = True
sea_monster[1,17] = True
sea_monster[1,18] = True
sea_monster[1,19] = True
sea_monster[2,18] = True
#print(sea_monster)

def paint_monster(row_start, col_start, sea_monster):
    sea_monster[row_start,col_start+1] = 2
    sea_monster[row_start,col_start+4] = 2
    sea_monster[row_start,col_start+7] = 2
    sea_monster[row_start,col_start+10] = 2
    sea_monster[row_start,col_start+13] = 2
    sea_monster[row_start,col_start+16] = 2
    sea_monster[row_start+1,col_start+0] = 2
    sea_monster[row_start+1,col_start+5] = 2
    sea_monster[row_start+1,col_start+6] = 2
    sea_monster[row_start+1,col_start+11] = 2
    sea_monster[row_start+1,col_start+12] = 2
    sea_monster[row_start+1,col_start+17] = 2
    sea_monster[row_start+1,col_start+18] = 2
    sea_monster[row_start+1,col_start+19] = 2
    sea_monster[row_start+2,col_start+18] = 2

f_sea_monster = 1-sea_monster

transforms = []

temp_image = overall_image

for transpose_index in range(2):
    for rotate_index in range(4):
        for row_index in range(overall_image.shape[0]-3):
            for col_index in range(overall_image.shape[1]-20):
                image_portion = temp_image[row_index:row_index+3,col_index:col_index+20]
                #print(image_portion)
                check_dragon_dots = ma.masked_array(image_portion,mask=f_sea_monster)
                if check_dragon_dots.sum() == 15:
                    transforms.append([transpose_index, rotate_index, row_index, col_index])
        temp_image = np.rot90(temp_image)
    temp_image = np.transpose(temp_image)

#print(overall_image)

for transpose_index in range(2):
    for rotate_index in range(4):
        for row_index in range(overall_image.shape[0]-3):
            for col_index in range(overall_image.shape[1]-20):
                for transform in transforms:
                    if transpose_index == transform[0] \
                    and rotate_index == transform[1] \
                    and row_index == transform[2] \
                    and col_index == transform[3]:
                        paint_monster(row_index, col_index, overall_image)
        overall_image = np.rot90(overall_image)
    overall_image = np.transpose(overall_image)


unique_elements, count_elements = np.unique(overall_image, return_counts=True)

#print(unique_elements)
#print(count_elements)

print("Part 2: Number of # =", count_elements[1])