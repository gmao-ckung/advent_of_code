import numpy as np
import os
from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day8","r")
initialDataList = fopen.readlines()

outputDigits = grabOutputDigits(initialDataList)

# print(outputDigits)

# Since 1, 4, 7, or 8 have 2, 4, 3, and 7 segments respectively,
# search outputDigits for entries with length 2, 4, 3, or 7

count_1_4_7_8 = 0

for output in outputDigits:
    numbers = output.split(" ")
    for number in numbers:
        if len(number) == 2 or len(number) == 4 or len(number) == 3 or len(number) == 7:
            count_1_4_7_8 += 1

print("Part 1 : Total number of 1's, 4's, 7's, and 8's in output =", count_1_4_7_8)