import numpy as np
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
data = np.loadtxt(CURR_DIR+'/input.day1')

# Part 1
for i in range(data.size):
    for j in range(i+1,data.size):
        if data[i] + data[j] == 2020:
            print("First Entry : ", data[i])
            print("Second Entry : ", data[j])
            print("Multiply Output = ", data[i] * data[j])

# Part 2
for i in range(data.size):
    for j in range(i+1,data.size):
        for k in range(j+1, data.size):
            if data[i] + data[j] + data[k] == 2020:
                print("First Entry : ", data[i])
                print("Second Entry : ", data[j])
                print("Third Entry : ", data[k])
                print("Multiply Output = ", data[i] * data[j] * data[k])
