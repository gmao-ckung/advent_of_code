import os
from math import sqrt

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")
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
print("Max steps =", steps_max)

print("y_min =", y_min)
print("y_max =", y_max)


# start_y_vel = 129
start_y_vel = -10
max_height = 0
break_count = 0
step_height_list = []
yet_to_find = True

while(True):
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

    if hit_found == False:
        if yet_to_find == False:
            break_count += 1
            if break_count == 1:
                break
            yet_to_find = True
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