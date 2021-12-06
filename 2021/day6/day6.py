import numpy as np
import os
from support import *
import time

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day6","r")
initialFishList = fopen.readlines()

initialFishList = separateViaDelin(initialFishList[0])
fishArray = createFishArray(initialFishList)

# *** Part 1 ***

iterationDays = 80

# *** "Slow, descriptive" Implementation ***

t1 = time.perf_counter()
fishArray = iterateFishLife(fishArray, iterationDays)
t2 = time.perf_counter()
print("Part 1: Total Number of Fish = ", fishArray.shape[0])
print("Version 1 runtime :", t2-t1)

fishArray = createFishArray(initialFishList)

totFish = 0

# *** "Fast, recursive" Implementation *** 

t1 = time.perf_counter()
for i in range(fishArray.shape[0]):
    numFish = interateFishLife_recursive(fishArray[i], iterationDays)
    totFish += numFish
t2 = time.perf_counter()
print("Part 1: Total Number of Fish = ", totFish)
print("Version 2 runtime :", t2-t1)

# *** Part 2 ***

totFish = 0

fishBucket = np.zeros(6,dtype=np.int64)

# Recusive code on Python is really slow for some reason, so I wrote up the
# recursive fish counter code in Fortran to get these "bucket" numbers that
# can be used to compute the total number of fish
fishBucket[0] = 6703087164
fishBucket[1] = 6206821033
fishBucket[2] = 5617089148
fishBucket[3] = 5217223242
fishBucket[4] = 4726100874
fishBucket[5] = 4368232009

for i in range(fishArray.shape[0]):
    totFish += fishBucket[fishArray[i]]

print("Part 2: Number of fish = ", totFish)