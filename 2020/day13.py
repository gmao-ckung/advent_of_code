import os
import math
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day13")
data = f1.readlines()

depart_time = int(data[0].replace("\n",""))
bus_IDs = data[1].replace("\n","")

bus_IDs_split = bus_IDs.split(',')
time_dictionary = {}

for ID in bus_IDs_split:
    if ID != 'x':
        nearest_pre_depart_time = int(depart_time/int(ID)) * int(ID) + int(ID)
        #print(nearest_pre_depart_time)
        time_dictionary[nearest_pre_depart_time] = int(ID)

nearest_time = sorted(time_dictionary)[0]
print("Part 1: ID of bus with nearest departure time =", time_dictionary[nearest_time])
print("Part 1: Time to wait =", (nearest_time-depart_time)*time_dictionary[nearest_time])