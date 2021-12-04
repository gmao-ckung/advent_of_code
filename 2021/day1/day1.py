import numpy as np
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
data = np.loadtxt(CURR_DIR+'/input.day1')

# *** Part 1 ***

increase_count = 0

for i in range(1,len(data)):
    if data[i-1] < data[i]:
        increase_count += 1

print("Values increased", increase_count,  "times")

# *** Part 2 ***

increase_count = 0

for i in range(len(data)):
    window1_value = 0
    window2_value = 0
    
    if i < len(data):
        window1_value += data[i]
    if (i+i) < len(data):
        window1_value += data[i+1]
        window2_value += data[i+1]
    if (i+2) < len(data):
        window1_value += data[i+2]
        window2_value += data[i+2]
    if (i+3) < len(data):
        window2_value += data[i+3]

    if window1_value < window2_value:
        increase_count += 1

print("There are", increase_count, "sums larger than the previous sum")