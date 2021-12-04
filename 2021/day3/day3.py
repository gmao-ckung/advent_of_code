import numpy as np
import os
from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day3","r")
binaryNums = fopen.readlines()

gamma_rate = 0
epsilon_rate = 0

# *** Part 1 ***

bitTracker = bitCounter(binaryNums, True)
listLength = len(binaryNums)

for bit in range(len(bitTracker)):
    if bitTracker[bit] > listLength/2:
        gamma_rate += 2**(len(bitTracker)-(bit+1))
    else:
        epsilon_rate += 2**(len(bitTracker)-(bit+1))

print("Power Consumption = ", gamma_rate * epsilon_rate)

# *** Part 2 ***

oxygen_gen_rate = 0
co2_gen_rate = 0

oxygen_list_current = binaryNums
co2_list_current = binaryNums

oxygen_list_current = life_support_calc("oxy", len(bitTracker), oxygen_list_current)
co2_list_current    = life_support_calc("co2", len(bitTracker), co2_list_current)

for i in range(len(oxygen_list_current[0][0])):
    if int(oxygen_list_current[0][0][i]) == 1:
        oxygen_gen_rate += 2**(len(bitTracker)-(i+1))

for i in range(len(co2_list_current[0][0])):
    if int(co2_list_current[0][0][i]) == 1:
        co2_gen_rate += 2**(len(bitTracker)-(i+1))

print("Life Support Rating = ", oxygen_gen_rate*co2_gen_rate)