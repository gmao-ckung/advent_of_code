import os
import math
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day15")
data = f1.readlines()

number_list = data[0].split(',')
#print(number_list)

number_dict = {}
for i in range(len(number_list)):
    number_dict[int(number_list[i])] = i+1

print(number_dict)

prev_num = 0
curr_turn = len(number_dict)+2
max_turns = 30000000

while curr_turn <= max_turns:
    if prev_num in number_dict.keys():
        #print("previous number found")
        turn_prev_spoken = curr_turn - 1
        turn_prev_prev_spoken = number_dict[prev_num]
        number_dict[prev_num] = curr_turn-1
        prev_num = turn_prev_spoken-turn_prev_prev_spoken
        curr_turn += 1
    else:
        number_dict[prev_num] = curr_turn-1
        prev_num = 0
        curr_turn += 1
    
    if curr_turn%100000 == 0:
        print("Current Turn = ", curr_turn)

print("The", str(max_turns)+"th","number is", prev_num)