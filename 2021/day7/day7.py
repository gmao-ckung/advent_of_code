import os
from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day7","r")
initialCrabPosList = fopen.readlines()

initialCrabPosList = separateViaDelin(initialCrabPosList[0])

maxPos = 0
for i in range(len(initialCrabPosList)):
    if maxPos < int(initialCrabPosList[i]):
        maxPos = int(initialCrabPosList[i])

print("max distance = ", maxPos)


# *** Part 1: Brute Force Search ***
for pos in range(maxPos+1):
    if pos == 0:
        minTotFuelSpent = 0
        posMinFuel = 0
    totFuelSpent = 0
    for i in range(len(initialCrabPosList)):
        totFuelSpent += abs(pos - int(initialCrabPosList[i]))
    
    if pos == 0:
        minTotFuelSpent = totFuelSpent
    else:
        if totFuelSpent < minTotFuelSpent:
            minTotFuelSpent = totFuelSpent
            posMinFuel = pos

print("Part 1 : Minimum Fuel Spent at position", posMinFuel)
print("Part 1 : Fuel Spent =", minTotFuelSpent)

# *** Part 2: Brute Force Search ***
for pos in range(maxPos+1):
    if pos == 0:
        minTotFuelSpent = 0
        posMinFuel = 0
    totFuelSpent = 0
    for i in range(len(initialCrabPosList)):
        totFuelSpent += sum(range(1,abs(pos - int(initialCrabPosList[i]))+1))
    
    if pos == 0:
        minTotFuelSpent = totFuelSpent
    else:
        if totFuelSpent < minTotFuelSpent:
            minTotFuelSpent = totFuelSpent
            posMinFuel = pos

print("Part 2 : Minimum Fuel Spent at position", posMinFuel)
print("Part 2 : Fuel Spent =", minTotFuelSpent)