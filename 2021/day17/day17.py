import os
from math import sqrt

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day17","r")
target_range = fopen.readlines()

target_range = target_range[0].replace("\n","")
print(target_range)
x_range = target_range.split(" ")[2].replace(",","")
y_range = target_range.split(" ")[3]

x_min = int(x_range.split("..")[0][2:])
x_max = int(x_range.split("..")[1])

y_max = int(y_range.split("..")[0][2:])
y_min = int(y_range.split("..")[1])

# Given that the velocity in x eventually goes to zero after several steps,
# x_min and x_max can be used to dictate the "minimum" and "maximum" number of steps
# for the velocity in x to go to zero

# Gauss's Identity : summation of i = 0,n-1 = n(n-1)/2
steps_min = int(sqrt(x_min*2 - 1))
steps_max = int(sqrt(x_max*2 - 1))

print("Min steps =", steps_min)
# print("Max steps =", steps_max)

print("y_min =", y_min)
print("y_max =", y_max)

# Note : Remember conservation of energy...
max_height = 0
break_count = 0
step_height_list = []
yet_to_find = True

for start_y_vel in range(int(abs(y_max))):
    y_vel = start_y_vel
    y_disp = 0
    find_max_height = 0
    hit_found = False
    step = 0
    print("Testing Velocity =", y_vel)
    while(True):
        y_disp += y_vel
        print("Y displacement = ", y_disp)
        if y_disp > find_max_height:
            find_max_height = y_disp
        y_vel -= 1
        if y_disp <= y_min and y_disp >= y_max:
            print("Hit target!")
            if find_max_height > max_height:
                max_height = find_max_height
            hit_found = True
            yet_to_find = False
            break
        elif y_disp < y_max:
            break
        step += 1

    step_height_list.append([step-1, max_height, start_y_vel])
    start_y_vel += 1


max_height = 0
y_vel = 0
for step_height in step_height_list:
    print(step_height)
    if step_height[1] > max_height and step_height[0] >= steps_min:
        max_height = step_height[1]
        y_vel = step_height[2]

print("Max Height = ", max_height)
print("Y velocity =", y_vel)

# Part 2
# For every point in the target area, there is a cooresponding x_vel, y_vel that matches

possible_starting_vel = []

for i in range(x_min,x_max+1):
    for j in range(y_max, y_min+1):
        # print(i, j)
        possible_starting_vel.append([i, j])

# Depending on the x_max values, you can dictate the highest searchable velocity in x based on halving
# x_max

# For negative Y velocities, for those velocities which cannot be reached in 1 step, we can start at y_min and go to 0
# and work our way backwards to find x. Also note that x velocities can basically go from 0 to x_max/2+1 for this search


for y_vel in range(y_min,0):
    
    step_list = []

    y_disp = 0
    hit_found = False
    step = 0
    print("Testing Velocity =", y_vel)
    curr_y_vel = y_vel
    while(True):
        y_disp += curr_y_vel
        step += 1
        print("Y displacement = ", y_disp)
        curr_y_vel -= 1
        if y_disp <= y_min and y_disp >= y_max:
            print("Hit target!")
            hit_found = True
            step_list.append(step)
            # break
        elif y_disp < y_max:
            break
        

    for step in step_list:
        for x_vel in range(0,int(x_max/2)+2):
            x_disp = 0
            curr_x_vel = x_vel
            curr_step = 0
            hit_found = False
            while(curr_step != step):
                x_disp += curr_x_vel
                print("X Displacement = ", x_disp)
                if curr_x_vel != 0:
                    curr_x_vel -= 1
                curr_step += 1
                
            if x_disp >= x_min and x_disp <= x_max:
                print("Hit Target!")
                if [x_vel,y_vel] not in possible_starting_vel:
                    possible_starting_vel.append([x_vel,y_vel])
                    print("Possible velocity = [",x_vel,",",y_vel,"]")

# This basically does a brute search of the positive y velocities that will hit and searches possible range of x velocities to match them

yet_to_find = True
break_count = 0
for start_y_vel in range(int(abs(y_max))):
    y_vel = start_y_vel
    y_disp = 0
    step = 0
    print("Testing Y Velocity =", y_vel)
    while(True):
        y_disp += y_vel
        print("Y displacement = ", y_disp)
        step += 1
        y_vel -= 1
        if y_disp <= y_min and y_disp >= y_max:
            print("Hit target in Y!")
            for x_vel in range(0, int(x_max/2)+2):
                x_disp = 0
                print("Testing X Velocity =", x_vel)
                curr_x_vel = x_vel
                for curr_step in range(step):
                    x_disp += curr_x_vel
                    print("X displacement = ", x_disp)
                    if curr_x_vel != 0:
                        curr_x_vel -= 1
                if x_disp >= x_min and x_disp <= x_max:
                    print("Hit Target in X!")
                    if [x_vel,start_y_vel] not in possible_starting_vel:
                        possible_starting_vel.append([x_vel,start_y_vel])
                        print("Possible velocity = [",x_vel,",",start_y_vel,"]")
        elif y_disp < y_max:
            break


print("number of distinct velocities = ", len(possible_starting_vel))