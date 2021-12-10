import numpy as np
import os
from support import *

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

size_list = []

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
    curr_value = lowValues_dict[key][0]

    found_list = []

    if i_index == 0:
        if heightMap[i_index+1, j_index] > curr_value and heightMap[i_index+1, j_index] != 9:
            if [i_index+1,j_index] not in found_list:
                found_list.append([i_index+1, j_index])
                count_found, found_list = searchBasin(i_index+1,j_index,"E", heightMap, found_list)
                E_count += count_found
        if j_index-1 >= 0:
            if heightMap[i_index,j_index-1] > curr_value and heightMap[i_index,j_index-1] != 9:
                if [i_index,j_index-1] not in found_list:
                    found_list.append([i_index,j_index-1])
                    count_found, found_list = searchBasin(i_index,j_index-1,"S", heightMap, found_list)
                    S_count += count_found
        
        if j_index+1 <= heightMap.shape[1]-1:
            if heightMap[i_index,j_index+1] > curr_value and heightMap[i_index,j_index+1] != 9:
                if [i_index,j_index+1] not in found_list:
                    found_list.append([i_index,j_index+1])
                    count_found, found_list = searchBasin(i_index,j_index+1,"N", heightMap, found_list)
                    N_count += count_found  
        
    elif i_index == heightMap.shape[0]-1:
        if heightMap[i_index-1,j_index] > curr_value and heightMap[i_index-1,j_index] != 9:
            if [i_index-1,j_index] not in found_list:
                found_list.append([i_index-1,j_index])
                count_found, found_list = searchBasin(i_index-1,j_index,"W", heightMap, found_list)
                W_count += count_found

        if j_index-1 >= 0:
            if heightMap[i_index,j_index-1] > curr_value and heightMap[i_index,j_index-1] != 9:
                if [i_index,j_index-1] not in found_list:
                    found_list.append([i_index,j_index-1])
                    count_found, found_list = searchBasin(i_index,j_index-1,"S", heightMap, found_list)
                    S_count += count_found
                
        if j_index+1 <= heightMap.shape[1]-1:
            if heightMap[i_index,j_index+1] > curr_value and heightMap[i_index,j_index+1] != 9:
                if [i_index,j_index+1] not in found_list:
                    found_list.append([i_index,j_index+1])
                    count_found, found_list = searchBasin(i_index,j_index+1,"N", heightMap, found_list)
                    N_count += count_found

    else:
        if heightMap[i_index-1,j_index] > curr_value and heightMap[i_index-1,j_index] != 9:
            if [i_index-1,j_index] not in found_list:
                found_list.append([i_index-1,j_index])
                count_found, found_list = searchBasin(i_index-1,j_index,"W", heightMap, found_list)
                W_count += count_found

        if heightMap[i_index+1,j_index] > curr_value and heightMap[i_index+1,j_index] != 9:
            if [i_index+1,j_index] not in found_list:
                found_list.append([i_index+1,j_index])
                count_found, found_list = searchBasin(i_index+1,j_index,"E", heightMap, found_list)
                E_count += count_found
            
        if j_index - 1 >= 0:
            if heightMap[i_index,j_index-1] > curr_value and heightMap[i_index,j_index-1] != 9:
                if [i_index,j_index-1] not in found_list:
                    found_list.append([i_index,j_index-1])
                    count_found, found_list = searchBasin(i_index,j_index-1,"S", heightMap, found_list)
                    S_count += count_found
                    
        if j_index + 1 <= heightMap.shape[1]-1:
            if heightMap[i_index,j_index+1] > curr_value and heightMap[i_index,j_index+1] != 9:
                if [i_index,j_index+1] not in found_list:
                    found_list.append([i_index,j_index+1])
                    count_found, found_list = searchBasin(i_index,j_index+1,"N", heightMap, found_list)
                    N_count += count_found

    size_list.append(1 + N_count + NE_count + E_count + SE_count + S_count + SW_count + W_count + NW_count)

size_list.sort(reverse=True)

print("Part 2: Multiplication = ", size_list[0]*size_list[1]*size_list[2])