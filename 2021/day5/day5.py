import numpy as np
import os
from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day5","r")
inputData = fopen.readlines()

directionList = createDirectionList(inputData)

maxX, maxY = findMax_X_Y(directionList)

map = createMap(maxX, maxY)

find_horiz_or_vert_dir(directionList, map)

print("Two lines overlap", sum(sum(map>1)), "times")

find_diag_dir(directionList, map)

print("Two lines overlap", sum(sum(map>1)), "times")