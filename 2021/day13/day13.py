import os
from matplotlib import pyplot as plt

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day13","r")
directions = fopen.readlines()

dot_map = []

for direction in directions:
    newD = direction.replace("\n","")
    if newD[0:4] != "fold" and newD != "":
        dot_map.append(newD)

    if newD[0:4] == "fold":
        fold_location = newD.split("=")
        if fold_location[0][-1] == 'y':
            folded_dot_map = []
            for dot_location in dot_map:
                key_coord = dot_location.split(",")
                if int(key_coord[1]) > int(fold_location[1]):
                    new_location = key_coord[0] + "," + str(int(key_coord[1])-2*(int(key_coord[1])-int(fold_location[1])))
                    if new_location not in folded_dot_map:
                        folded_dot_map.append(new_location)
                else:
                    if dot_location not in folded_dot_map:
                        folded_dot_map.append(dot_location)
            dot_map = folded_dot_map
            # print("Part 1: Number of points = ", len(dot_map))
            # break
            
        elif fold_location[0][-1] == 'x':
            folded_dot_map = []
            for dot_location in dot_map:
                key_coord = dot_location.split(",")
                if int(key_coord[0]) > int(fold_location[1]):
                    new_location = str(int(key_coord[0])-2*(int(key_coord[0])-int(fold_location[1]))) + "," + key_coord[1]
                    if new_location not in folded_dot_map:
                        folded_dot_map.append(new_location)
                else:
                    if dot_location not in folded_dot_map:
                        folded_dot_map.append(dot_location)
            dot_map = folded_dot_map
            # print("Part 1: Number of points = ", len(dot_map))
            # break


x = []
y = []

for dot in dot_map:
    point = dot.split(",")
    x.append(int(point[0]))
    y.append(int(point[1]))

plt.scatter(x,y)
plt.show()