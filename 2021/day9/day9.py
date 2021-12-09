import numpy as np
import os
# from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day9","r")
initialDataList = fopen.readlines()

heightMap = np.zeros((len(initialDataList[0])-1,len(initialDataList)),dtype=int)

colNum = 0
for line in initialDataList:
    heightMap[:,colNum]=np.array(list(line.replace("\n",""))).astype(int)
    colNum += 1


lowValues_dict = {}
dict_index = 0

for j in range(0,heightMap.shape[1]):
    for i in range(0,heightMap.shape[0]):
        if i == 0: 
            if j == 0:
                if heightMap[i,j] < heightMap[i,j+1] and \
                    heightMap[i,j] < heightMap[i+1,j]:
                    lowValues_dict[dict_index] = [heightMap[i,j], i, j]                    
            elif j == heightMap.shape[1]-1:
                if heightMap[i,j] < heightMap[i,j-1] and \
                     heightMap[i,j] < heightMap[i+1,j]:
                    lowValues_dict[dict_index] = [heightMap[i,j], i, j]
            else:
                if heightMap[i,j] < heightMap[i,j+1] and \
                    heightMap[i,j] < heightMap[i,j-1] and \
                    heightMap[i,j] < heightMap[i+1,j]:
                    lowValues_dict[dict_index] = [heightMap[i,j], i, j]
            dict_index += 1
        elif i == heightMap.shape[0]-1:
            if j == 0:
                if heightMap[i,j] < heightMap[i,j+1] and \
                   heightMap[i,j] < heightMap[i-1,j]:
                   lowValues_dict[dict_index] = [heightMap[i,j], i, j]
            elif j == heightMap.shape[1]-1:
                if heightMap[i,j] < heightMap[i,j-1] and \
                   heightMap[i,j] < heightMap[i-1,j]:
                   lowValues_dict[dict_index] = [heightMap[i,j], i, j]
            else:
                if heightMap[i,j] < heightMap[i,j+1] and \
                    heightMap[i,j] < heightMap[i,j-1] and \
                    heightMap[i,j] < heightMap[i-1,j]:
                    lowValues_dict[dict_index] = [heightMap[i,j], i, j]
            dict_index += 1
        else:
            if j == 0:
                if heightMap[i,j] < heightMap[i+1,j] and \
                heightMap[i,j] < heightMap[i,j+1] and \
                heightMap[i,j] < heightMap[i-1,j]:                
                    lowValues_dict[dict_index] = [heightMap[i,j], i, j]
            elif j == heightMap.shape[1]-1:
                if heightMap[i,j] < heightMap[i+1,j] and \
                heightMap[i,j] < heightMap[i-1,j] and \
                heightMap[i,j] < heightMap[i,j-1]:
                    lowValues_dict[dict_index] = [heightMap[i,j], i, j]
            else:
                if heightMap[i,j] < heightMap[i+1,j] and \
                heightMap[i,j] < heightMap[i,j+1] and \
                heightMap[i,j] < heightMap[i-1,j] and \
                heightMap[i,j] < heightMap[i,j-1]:
                   lowValues_dict[dict_index] = [heightMap[i,j], i, j]
            dict_index += 1

sum_risk = 0
for key in lowValues_dict:
    sum_risk += lowValues_dict[key][0] + 1

print("Part 1: Sum of risk levels from low points =", sum_risk)

for key in lowValues_dict:
    N_count = 0
    S_count = 0
    E_count = 0
    W_count = 0
    NE_count = 0
    NW_count = 0
    SE_count = 0
    SW_count = 0

    i_index = lowValues_dict[key][1]
    j_index = lowValues_dict[key][2]

    if i_index == 0:
        if j_index-1 >= 0:
            print("Search S")
            print("Search SE")
        if j_index+1 <= heightMap.shape[1]-1:
            print("Search N")
            print("Search NE")
        print("Search E")
    elif i_index == heightMap.shape[0]-1:
        if j_index-1 >= 0:
            print("Search S")
            print("Search SW")
        if j_index+1 <= heightMap.shape[1]-1:
            print("Search N")
            print("Search NW")
        print("Search W")
    else:
        if j_index - 1 >= 0:
            print("Search S")
            print("Search SW")
            print("Search SE")
        if j_index + 1 <= heightMap.shape[1]-1:
            print("Search N")
            print("Search NW")
            print("Search NE")
        print("Search W")
        print("Search E")