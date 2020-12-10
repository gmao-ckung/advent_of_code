import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)

f1 = open(CURR_DIR+"/input.day3")

landscape = f1.readlines()

horizontal_pos = 0
vertical_pos = 0
tree_count = 0

# *** Part 1 ***
for treeline in landscape:
    #print(treeline)
    treeline = treeline.replace("\n","")
    if vertical_pos > 0 and treeline[horizontal_pos] == '#':
        tree_count = tree_count + 1
    vertical_pos = vertical_pos + 1
    # Use modulo to wrap around the treeline
    horizontal_pos = (horizontal_pos + 3) % len(treeline)

print("Part 1: Trees encountered =", tree_count)

slopes_horizon = [1, 3, 5, 7, 1]
slopes_vert    = [1, 1, 1, 1, 2]

mult_tree_count = 1

for slope_id in range(len(slopes_horizon)):
    horizontal_pos = 0
    vertical_pos = 0
    tree_count = 0
    for treeline in landscape:
        #print(treeline)
        treeline = treeline.replace("\n","")
        if vertical_pos > 0 and \
           vertical_pos % slopes_vert[slope_id] == 0:
            
            # Use modulo to wrap around the treeline
            horizontal_pos = (horizontal_pos + slopes_horizon[slope_id]) % len(treeline)
            if treeline[horizontal_pos] == '#':
                tree_count = tree_count + 1
        vertical_pos = vertical_pos + 1
        
    #print("Trees encountered =", tree_count)
    mult_tree_count = mult_tree_count * tree_count

print("Part 2: Multiplication Tree Count =", mult_tree_count)