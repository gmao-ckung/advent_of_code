import numpy as np
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
joltage_list = np.sort(np.loadtxt(CURR_DIR+"/input.test",dtype=int))
print(joltage_list)

max_joltage = joltage_list[-1] + 3
current_joltage_to_match = 0
joltage_difference = np.zeros(len(joltage_list)+1,dtype=int)

adaptor_list = np.zeros(1,dtype=int)

for i in range(len(joltage_list)):
    if (joltage_list[i] - 3) <= current_joltage_to_match and joltage_list[i] < max_joltage:
        joltage_difference[i] = joltage_list[i] - current_joltage_to_match
        current_joltage_to_match = joltage_list[i]
        adaptor_list = np.append(adaptor_list,joltage_list[i])
        print(current_joltage_to_match)     

joltage_difference[-1] = 3

print("Count of difference of 1 =", np.count_nonzero(joltage_difference==1))
print("Count of difference of 2 =", np.count_nonzero(joltage_difference==2))
print("Count of difference of 3 =", np.count_nonzero(joltage_difference==3))