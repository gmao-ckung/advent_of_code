import os
import numpy as np

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day11","r")
initialDataList = fopen.readlines()