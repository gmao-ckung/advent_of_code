import os
import math

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/input.in","r")

# Read lines within input file and remove new line character at the line's end
time_distance_records = file.read().splitlines()

for line in time_distance_records:
    if "Time: " in line:
        times = line.replace("Time:","").split()
    if "Distance: " in line:
        distance = line.replace("Distance:","").split()

print(times)
print(distance)

# distance = (time - held_time) * held_time
#          = time * held_time - held_time^2

# d(distance)/d(held_time) = time - 2*held_time
# Set d(distance)/d(held_time) = 0 to Min/Max
# 0 = time - 2*held_time -> 2*held_time = time -> held_time = time/2

total_combinations = 1
for index in range(len(times)):
    optimal_hold_time = int(int(times[index]) / 2)
    
    combinations = 0
    # Search around the optimal holding time: Note that only integer times are valid
    if (int(times[index]) - optimal_hold_time) * optimal_hold_time > int(distance[index]):
        # print(optimal_hold_time)
        combinations += 1

    check_hold_time = optimal_hold_time+1
    while((int(times[index]) - check_hold_time) * check_hold_time > int(distance[index])):
        # print(check_hold_time)
        combinations += 1
        check_hold_time += 1   

    check_hold_time = optimal_hold_time - 1
    while((int(times[index]) - check_hold_time) * check_hold_time > int(distance[index])):
        # print(check_hold_time)
        combinations += 1
        check_hold_time -= 1
        
    total_combinations *= combinations

print("Part 1 : Total Combinations Found = ", total_combinations)

actual_time = ""
actual_distance = ""
for i in range(len(times)):
    actual_time += times[i]
    actual_distance += distance[i]
print(actual_time)
print(actual_distance)

actual_distance = int(actual_distance)
actual_time = int(actual_time)
optimal_hold_time = int(actual_time/2)
combinations = 0

# Faster way to solve is to find the roots (times) based on the actual distance
# (actual_time - hold_time)*hold_time = actual_distance
# 0 = hold_time^2 - hold_time*actual_time + actual_distance
# Quadratic Formula 
# hold_time = (-(-actual_time) +- sqrt((-actual_time)**2 - (4*1*actual_distance)))/2

hold_time_1 = (-(-actual_time) + math.sqrt((-actual_time)**2 - (4*1*actual_distance)))/2
hold_time_2 = (-(-actual_time) - math.sqrt((-actual_time)**2 - (4*1*actual_distance)))/2

hold_time_1 = int(hold_time_1)
hold_time_2 = int(hold_time_2)

# Take the difference of the roots(or hold times) to find the number of combinations

if hold_time_1 > hold_time_2:
    hold_time_2 += 1
    combinations = abs(hold_time_1 - hold_time_2) + 1
else:
    hold_time_1 += 1
    combinations = abs(hold_time_1 - hold_time_2) + 1

print("Part 2 : Total Combinations found = ", combinations)