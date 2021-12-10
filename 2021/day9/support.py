import numpy as np

def searchBasin(i_index, j_index, direction, heightMap, found_list):

    count = 1

    curr_value = heightMap[i_index,j_index]

    if direction == "N":
        if j_index+1 <= heightMap.shape[1]-1: 
            if heightMap[i_index,j_index+1] > curr_value and heightMap[i_index,j_index+1] < 9:
                if [i_index,j_index+1] not in found_list:
                    found_list.append([i_index,j_index+1])
                    count_found, found_list = searchBasin(i_index,j_index+1,"N", heightMap, found_list)
                    count += count_found

        if i_index-1 >= 0:
            if heightMap[i_index-1,j_index] > curr_value and heightMap[i_index-1,j_index] < 9:
                if [i_index-1,j_index] not in found_list:
                    found_list.append([i_index-1,j_index])
                    count_found, found_list = searchBasin(i_index-1,j_index,"W", heightMap, found_list)
                    count += count_found

        if i_index+1 <= heightMap.shape[0]-1:
            if heightMap[i_index+1,j_index] > curr_value and heightMap[i_index+1,j_index] < 9:
                if [i_index+1,j_index] not in found_list:
                    found_list.append([i_index+1,j_index])
                    count_found, found_list = searchBasin(i_index+1,j_index,"E", heightMap, found_list)
                    count += count_found

    if direction == "W":
        if i_index-1 >= 0:
            if heightMap[i_index-1,j_index] > curr_value and heightMap[i_index-1,j_index] < 9:
                if [i_index-1,j_index] not in found_list:
                    found_list.append([i_index-1,j_index])
                    count_found, found_list = searchBasin(i_index-1,j_index,"W", heightMap, found_list)
                    count += count_found

        if j_index+1 <= heightMap.shape[1]-1: 
            if heightMap[i_index,j_index+1] > curr_value and heightMap[i_index,j_index+1] < 9:
                if [i_index,j_index+1] not in found_list:
                    found_list.append([i_index,j_index+1])
                    count_found, found_list = searchBasin(i_index,j_index+1,"N", heightMap, found_list)
                    count += count_found

        if j_index-1 >= 0:
            if heightMap[i_index,j_index-1] > curr_value and heightMap[i_index,j_index-1] < 9:
                if [i_index,j_index-1] not in found_list:
                    found_list.append([i_index,j_index-1])
                    count_found, found_list = searchBasin(i_index,j_index-1,"S", heightMap, found_list)
                    count += count_found

    if direction == "S":
        if j_index-1 >= 0:
            if heightMap[i_index,j_index-1] > curr_value and heightMap[i_index,j_index-1] < 9:
                if [i_index,j_index-1] not in found_list:
                    found_list.append([i_index,j_index-1])
                    count_found, found_list = searchBasin(i_index,j_index-1,"S", heightMap, found_list)
                    count += count_found

        if i_index-1 >= 0:
            if heightMap[i_index-1,j_index] > curr_value and heightMap[i_index-1,j_index] < 9:
                if [i_index-1,j_index] not in found_list:
                    found_list.append([i_index-1,j_index])
                    count_found, found_list = searchBasin(i_index-1,j_index,"W", heightMap, found_list)
                    count += count_found

        if i_index+1 <= heightMap.shape[0]-1:
            if heightMap[i_index+1,j_index] > curr_value and heightMap[i_index+1,j_index] < 9:
                if [i_index+1,j_index] not in found_list:
                    found_list.append([i_index+1,j_index])
                    count_found, found_list = searchBasin(i_index+1,j_index,"E", heightMap, found_list)
                    count += count_found

    if direction == "E":
        if i_index+1 <= heightMap.shape[0]-1:
            if heightMap[i_index+1,j_index] > curr_value and heightMap[i_index+1,j_index] < 9:
                if [i_index+1,j_index] not in found_list:
                    found_list.append([i_index+1,j_index])
                    count_found, found_list = searchBasin(i_index+1,j_index,"E", heightMap, found_list)
                    count += count_found

        if j_index+1 <= heightMap.shape[1]-1: 
            if heightMap[i_index,j_index+1] > curr_value and heightMap[i_index,j_index+1] < 9:
                if [i_index,j_index+1] not in found_list:
                    found_list.append([i_index,j_index+1])
                    count_found, found_list = searchBasin(i_index,j_index+1,"N", heightMap, found_list)
                    count += count_found

        if j_index-1 >= 0:
            if heightMap[i_index,j_index-1] > curr_value and heightMap[i_index,j_index-1] < 9:
                if [i_index,j_index-1] not in found_list:
                    found_list.append([i_index,j_index-1])
                    count_found, found_list = searchBasin(i_index,j_index-1,"S", heightMap, found_list)
                    count += count_found
    
    return count, found_list