import os
import numpy as np
from collections import Counter

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day11","r")
initialDataList = fopen.readlines()

# print(initialDataList)
octoArray = np.zeros((10,10), dtype=int)
lineNum = 0
for line in initialDataList:
    line = line.replace("\n","")
    octoArray[lineNum,:] = np.array(list(line))
    lineNum += 1
# print(octoArray)

numSteps = 100
flashes = 0

for step in range(1000):
    octoArray += 1

    while(np.any(octoArray >= 10)):
        ten_location = np.where(octoArray >= 10)

        #i-1, j-1,
        condition0 = np.where((ten_location[0]-1) >= 0)
        condition1 = np.where((ten_location[1][condition0]-1) >= 0)
        octoArray[ten_location[0][condition0][condition1]-1,ten_location[1][condition0][condition1]-1] += 1

        #i, j-1
        condition = np.where((ten_location[1]-1) >= 0)
        octoArray[ten_location[0][condition],ten_location[1][condition]-1] += 1

        #i+1, j-1
        condition0 = np.where((ten_location[0]+1) < 10)
        condition1 = np.where((ten_location[1][condition0]-1) >= 0)
        octoArray[ten_location[0][condition0][condition1]+1,ten_location[1][condition0][condition1]-1] += 1

        #i-1, j
        condition = np.where((ten_location[0]-1) >= 0)
        octoArray[ten_location[0][condition]-1, ten_location[1][condition]] += 1

        #i+1, j
        condition = np.where((ten_location[0]+1) < 10)
        octoArray[ten_location[0][condition]+1, ten_location[1][condition]] += 1

        #i-1, j+1
        condition0 = np.where((ten_location[0]-1) >= 0)
        condition1 = np.where((ten_location[1][condition0]+1) < 10)
        octoArray[ten_location[0][condition0][condition1]-1, ten_location[1][condition0][condition1]+1] += 1

        #i, j+1,
        condition = np.where((ten_location[1]+1) < 10)
        octoArray[ten_location[0][condition],ten_location[1][condition]+1] += 1

        #i+1, j+1
        condition0 = np.where((ten_location[0]+1) < 10)
        condition1 = np.where(ten_location[1][condition0]+1 < 10)
        octoArray[ten_location[0][condition0][condition1]+1, ten_location[1][condition0][condition1]+1] += 1

        octoArray[ten_location] = -1000
    
    zero_loc = np.where(octoArray <= 0)
    flashes += zero_loc[0].shape[0]
    octoArray[zero_loc] = 0

    if(np.all(octoArray == 0)):
        print("Part 2: Step = ", step+1)
        break
    # print(octoArray)

print(octoArray)

print("Part 1: Number of flashes =", flashes)