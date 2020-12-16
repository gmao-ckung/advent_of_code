import os
import math
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.test")
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

# *** Part 2 ***

# Note : It looks like the bus IDs are all prime numbers

bus_time_shift = []
bus_ID = []
shift = 0
for ID in bus_IDs_split:
    if ID != 'x':
        bus_time_shift.append(shift)
        bus_ID.append(int(ID))
    shift = shift+1

found = False
factor = 100002618000000

def is_prime(inputNum):
    result = True

    for i in range(2,inputNum):
        if inputNum%i == 0:
            print(i, "is a factor")
            result = False
            break
    
    return result

is_prime(6)

while not found:
    factor = factor + 1
    testValue =  bus_ID[0] * factor
    verify = 0
    for i in range(1,len(bus_ID)):
        if (testValue + bus_time_shift[i])%bus_ID[i] == 0:
            verify = verify+1
        else:
            break

    if verify == len(bus_ID) - 1:
        found = True

    if factor%1000000==0:
        print("Searched past", factor)

print("Initial Time =", bus_ID[0]*factor)

