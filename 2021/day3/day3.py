import numpy as np
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
fopen = open(CURR_DIR+"/input.day3","r")
binaryNums = fopen.readlines()

initialize = True
gamma_rate = 0
epsilon_rate = 0

# Routine to count 1's in each 2's placeholder
def bitCounter(binaryNumList, newLine=False):
    initialize = True
    for binaryNum in binaryNumList:
        # Get rid of newline
        if newLine:
            binaryNum = binaryNum.split()
        # Initialize bitTracker variable if first time through
        if initialize:
            bitTracker = np.zeros(len(binaryNum[0]))
            initialize = False
        
        # Add bits to bitTracker
        for bit in range(len(binaryNum[0])):
            bitTracker[bit] += int(binaryNum[0][bit])
    return bitTracker

# Find the binary value for the particular life support rating
def life_support_calc(rating, bitLen, current_list):
    for bit in range(bitLen):
        updated_list = []
        if bit == 0:
            lifeBitTracker = bitCounter(current_list,True)
        else:
            lifeBitTracker = bitCounter(current_list)
        
        listLength = len(current_list)

        for binaryNum in current_list:
            if bit == 0:
                binaryNum = binaryNum.split()

            if rating == "oxy":
                if lifeBitTracker[bit] >= listLength/2:
                    if int(binaryNum[0][bit]) == 1:
                        updated_list.append(binaryNum)
                else:
                    if int(binaryNum[0][bit]) == 0:
                        updated_list.append(binaryNum)

            if rating == "co2":
                if lifeBitTracker[bit] >= listLength/2:
                    if int(binaryNum[0][bit]) == 0:
                        updated_list.append(binaryNum)
                else:
                    if int(binaryNum[0][bit]) == 1:
                        updated_list.append(binaryNum)
        current_list = updated_list
        if len(current_list) == 1:
            return current_list

    return current_list

# *** Part 1 ***

bitTracker = bitCounter(binaryNums, True)

print(bitTracker)
listLength = len(binaryNums)

for bit in range(len(bitTracker)):
    if bitTracker[bit] > listLength/2:
        gamma_rate += 2**(len(bitTracker)-(bit+1))
    else:
        epsilon_rate += 2**(len(bitTracker)-(bit+1))

print(gamma_rate)
print(epsilon_rate)
print("Power Consumption = ", gamma_rate * epsilon_rate)

# *** Part 2 ***

oxygen_gen_rate = 0
co2_gen_rate = 0

oxygen_list_current = binaryNums
co2_list_current = binaryNums

oxygen_list_current = life_support_calc("oxy", len(bitTracker), oxygen_list_current)
co2_list_current    = life_support_calc("co2", len(bitTracker), co2_list_current)

print(oxygen_list_current)
print(co2_list_current)

for i in range(len(oxygen_list_current[0][0])):
    if int(oxygen_list_current[0][0][i]) == 1:
        oxygen_gen_rate += 2**(len(bitTracker)-(i+1))

for i in range(len(co2_list_current[0][0])):
    if int(co2_list_current[0][0][i]) == 1:
        co2_gen_rate += 2**(len(bitTracker)-(i+1))

print(oxygen_gen_rate)
print(co2_gen_rate)

print("Life Support Rating = ", oxygen_gen_rate*co2_gen_rate)