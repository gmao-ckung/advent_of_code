import numpy as np
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
fopen = open(CURR_DIR+"/input.day3","r")
binaryNums = fopen.readlines()

initialize = True
gamma_rate = 0
epsilon_rate = 0

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

for bit in range(len(bitTracker)):
    oxygen_list_updated = []
    if bit == 0:
        oxyBitTracker = bitCounter(oxygen_list_current,True)
    else:
        oxyBitTracker = bitCounter(oxygen_list_current)
    
    listLength = len(oxygen_list_current)

    for binaryNum in oxygen_list_current:
        if bit == 0:
            binaryNum = binaryNum.split()
        if oxyBitTracker[bit] >= listLength/2:
            if int(binaryNum[0][bit]) == 1:
                oxygen_list_updated.append(binaryNum)
        else:
            if int(binaryNum[0][bit]) == 0:
                oxygen_list_updated.append(binaryNum)

    oxygen_list_current = oxygen_list_updated
    if len(oxygen_list_current) == 1:
        break    


for bit in range(len(bitTracker)):
    co2_list_updated = []
    if bit == 0:
        co2BitTracker = bitCounter(co2_list_current,True)
    else:
        co2BitTracker = bitCounter(co2_list_current)

    listLength = len(co2_list_current)

    for binaryNum in co2_list_current:
        if bit == 0:
            binaryNum = binaryNum.split()
        if co2BitTracker[bit] >= listLength/2:
            if int(binaryNum[0][bit]) == 0:
                co2_list_updated.append(binaryNum)
        else:
            if int(binaryNum[0][bit]) == 1:
                co2_list_updated.append(binaryNum)

    co2_list_current = co2_list_updated
    if len(co2_list_current) == 1:
        break 

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