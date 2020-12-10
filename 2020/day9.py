import numpy as np
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day9")

all_numbers = f1.readlines()

preamble_length = 25

number_list = []

# Create initial list based on preamble_length
for i in range(preamble_length):
    number_list.append(int(all_numbers[i].replace("\n","")))

# Search to see if the list has two numbers can be the sum of the upcoming number on the list
for loc in range(preamble_length,len(all_numbers)):
    found = False
    for i in range(len(number_list)):
        for j in range(i+1,len(number_list)):
            if (number_list[i] + number_list[j]) == int(all_numbers[loc].replace("\n","")):
                print("sum found for", all_numbers[loc], "by adding", number_list[i],"and",number_list[j])
                found = True
                break
        if found:
            break
    if not found:        
        break

    number_list = number_list[1:] + [int(all_numbers[loc].replace("\n",""))]

print("There's no combination for", all_numbers[loc])

invalid_number = int(all_numbers[loc].replace("\n",""))


for i in range(len(all_numbers)):
    contiguous_number_array = np.zeros(1,dtype=int)
    contiguous_number_array[0] = int(all_numbers[i])
    found = False
    for j in range(i+1,len(all_numbers)):
        contiguous_number_array = np.append(contiguous_number_array,int(all_numbers[j]))
        if np.sum(contiguous_number_array) > invalid_number:
            break
        if np.sum(contiguous_number_array) == invalid_number:
            found = True
            break
    if found:
        weakness = np.sort(contiguous_number_array)[0] + np.sort(contiguous_number_array)[-1]
        break

print("Weakness Number =", weakness)