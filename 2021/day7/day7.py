import numpy as np
import os
from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day7","r")
initialCrabPos = np.array(separateViaDelin(fopen.readlines()[0]),dtype=int)

maxPos = max(initialCrabPos)
print("max distance = ", maxPos)

# *** Part 1: Brute Force Search ***
for pos in range(maxPos+1):
    if pos == 0:
        minTotFuelSpent = 0
        posMinFuel = 0
    totFuelSpent = sum(abs(pos-initialCrabPos))
    
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
    totFuelSpent2 = 0
    for i in range(len(initialCrabPos)):
        totFuelSpent += sum(range(1,abs(pos - initialCrabPos[i])+1))
    
    if pos == 0:
        minTotFuelSpent = totFuelSpent
    else:
        if totFuelSpent < minTotFuelSpent:
            minTotFuelSpent = totFuelSpent
            posMinFuel = pos

print("Part 2 : Minimum Fuel Spent at position", posMinFuel)
print("Part 2 : Fuel Spent =", minTotFuelSpent)