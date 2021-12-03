import numpy as np

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