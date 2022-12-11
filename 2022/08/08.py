import numpy as np
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
tree_grid_data = open(CURR_DIR+"/input.08","r")

tree_grid_data = tree_grid_data.readlines()

tree_grid_list = []

for row in tree_grid_data:
    row = [int(letter) for letter in row.replace("\n","")]    
    # print(row)
    tree_grid_list.append(row)
tree_grid_np = np.asarray(tree_grid_list)
# print(tree_grid_np)

visible_num_trees = tree_grid_np.shape[0] * 2 + 2*(tree_grid_np.shape[1]-2)
index_max_hgt_dict = {}

# print(visible_num_trees)

# Look for visible trees at each row
for row in range(1,tree_grid_np.shape[0]-1):
    # print(tree_grid_np[row])
    row_values = tree_grid_np[row]
    max_height_from_left = 0
    max_height_from_right = 0
    # print("Going left to right")
    for col in range(1,len(row_values)-1):
        # print(row_values[col])
        if row_values[col] > max_height_from_left and row_values[col] > int(row_values[0]):
            visible_num_trees += 1
            # print("New tallest tree from left : ", row_values[col])
            max_height_from_left = row_values[col]
            index_max_hgt_dict[str(row) + "," + str(col)] = max_height_from_left
    # print("Current Dict of Max Heights : ", index_max_hgt_dict)
    # print("Going right to left")
    for col in range(len(row_values)-2,0,-1):
        # print(row_values[col])
        if row_values[col] > max_height_from_right and row_values[col] > int(row_values[len(row_values)-1]):
            if(str(row) + "," + str(col) not in index_max_hgt_dict.keys()):
                visible_num_trees += 1
                # print("New tallest tree from right : ", row_values[col])
                max_height_from_right= row_values[col]
                index_max_hgt_dict[str(row) + "," + str(col)] = max_height_from_right
    # print("Current Dict of Max Heights : ", index_max_hgt_dict)

# Look for visable trees at each column
for col in range(1, len(tree_grid_np[0])-1):
    max_height_from_top = 0
    max_height_from_bottom = 0
    # print("Going from top to bottom")
    for row in range(1,tree_grid_np.shape[0]-1):
        height = tree_grid_np[row][col]
        # print(height)
        if(height > max_height_from_top and height > tree_grid_np[0][col]):
            max_height_from_top = height
            if(str(row) + "," + str(col) not in index_max_hgt_dict.keys()):
                visible_num_trees += 1
                # print("New tallest tree from top : ", height)
                index_max_hgt_dict[str(row) + "," + str(col)] = height
    # print("Current Dict of Max Heights : ", index_max_hgt_dict)
    # print("Going from bottom to top")
    for row in range(tree_grid_np.shape[0]-2,0,-1):
        height = tree_grid_np[row][col]
        # print(height)
        if(height > max_height_from_bottom and height > tree_grid_np[tree_grid_np.shape[0]-1][col]):
            max_height_from_bottom = height
            if(str(row) + "," + str(col) not in index_max_hgt_dict.keys()):
                visible_num_trees += 1
                # print("New tallest tree from bottom = ", height)
                max_height_from_bottom = height
                index_max_hgt_dict[str(row) + "," + str(col)] = height
    # print("Current Dict of Max Heights : ", index_max_hgt_dict)

print("Part 1 : Number of Visible Trees from outside the grid = ", visible_num_trees)

# Test edge trees to gauge how many trees they can observe

max_scenic_score = 0

index_keys = index_max_hgt_dict.keys()

for key in index_keys:
    # print(key)
    coord = key.split(",")
    # print(coord)

    south_score = 0
    curr_height = tree_grid_np[int(coord[0])][int(coord[1])]
    #Search South
    for index in range(int(coord[0])+1,tree_grid_np.shape[0]):
        if curr_height > tree_grid_np[index][int(coord[1])]:
            south_score += 1
        else:
            south_score += 1
            break

    north_score = 0
    #Search North
    for index in range(int(coord[0])-1, -1, -1):
        if curr_height > tree_grid_np[index][int(coord[1])]:
            north_score += 1
        else:
            north_score += 1
            break

    east_score = 0
    for index in range(int(coord[1])+1, tree_grid_np.shape[1]):
        if curr_height > tree_grid_np[int(coord[0])][index]:
            east_score += 1
        else:
            east_score += 1
            break

    west_score = 0
    for index in range(int(coord[1])-1, -1, -1):
        if curr_height > tree_grid_np[int(coord[0])][index]:
            west_score += 1
        else:
            west_score += 1
            break

    if max_scenic_score < north_score * west_score * east_score * south_score:
        max_scenic_score = north_score * west_score * east_score * south_score

print("Part 2: Max Score = ", max_scenic_score)

