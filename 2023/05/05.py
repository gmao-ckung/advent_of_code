import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/input.test","r")

# Read lines within input file and remove new line character at the line's end
almanac = file.read().splitlines()

mapping = {}

for entry in almanac:
    if "seeds:" in entry:
        seed_numbers = entry.replace("seeds: ","").split()

    elif "map:" in entry:
        map_prefix = entry.split()[0].split("-")
        start_prefix = map_prefix[0]
        end_prefix   = map_prefix[2]

        if start_prefix not in mapping:
            mapping[start_prefix] = {}
            mapping[start_prefix]["mapto"] = end_prefix
            mapping[start_prefix]["indexing"] = []

    elif entry != "":
        ranges = entry.split()
        # print(ranges)
        mapping[start_prefix]["indexing"].append([int(ranges[1]), int(ranges[2]), int(ranges[0])])


for map in mapping:
    mapping[map]["low_high"] = []
    low_location = -1
    high_location = -1
    for index in mapping[map]["indexing"]:
        if low_location == -1:
            low_location = index[0]
            high_location = index[0] + index[1]
        else:
            if low_location > index[0]:
                low_location = index[0]
            if high_location < index[0] + index[1]:
                high_location = index[0] + index[1]

    print(low_location, high_location)
    mapping[map]["low_high"] = [low_location, high_location]

low_location = -1

for seed_index in seed_numbers:
    start_prefix = 'seed'
    mapping_value = int(seed_index)
    while(start_prefix != 'location'):
        found_index = False
        if mapping_value > mapping[start_prefix]["low_high"][0] and \
           mapping_value < mapping[start_prefix]["low_high"][1]:
            for index in mapping[start_prefix]["indexing"]:
                start_index    = index[0]
                number_indexes = index[1]
                mapped_index   = index[2]

                if mapping_value in range(start_index, start_index+1+number_indexes):
                    mapping_value = mapped_index + (mapping_value - start_index)
                    start_prefix = mapping[start_prefix]["mapto"]
                    # print(start_prefix)
                    # print(mapping_value)
                    found_index = True
                    break
            
            if(not found_index):
                start_prefix = mapping[start_prefix]["mapto"]
                # print(start_prefix)
                # print(mapping_value)
        else:
            start_prefix = mapping[start_prefix]["mapto"]

    if(low_location == -1):
        low_location = mapping_value
    elif(low_location > mapping_value):
        low_location = mapping_value

print("Part 1 : Lowest location number = ", low_location)

low_location = -1

# loop_index = 0
# for seed_index in seed_numbers:
#     if(loop_index%2 == 0):
#         start_index = int(seed_index)
#     else:
#         for mapping_value in range(start_index,int(seed_index)+start_index):
#             start_value = mapping_value
#             start_prefix = 'seed'
#             while(start_prefix != 'location'):
#                 if mapping_value > mapping[start_prefix]["low_high"][0] and \
#                     mapping_value < mapping[start_prefix]["low_high"][1]:
#                     found_index = False
#                     for index in mapping[start_prefix]["indexing"]:
#                         start_index    = index[0]
#                         number_indexes = index[1]
#                         mapped_index   = index[2]

#                         if mapping_value in range(start_index, start_index+1+number_indexes):
#                             mapping_value = mapped_index + (mapping_value - start_index)
#                             start_prefix = mapping[start_prefix]["mapto"]
#                             # print(start_prefix)
#                             # print(mapping_value)
#                             found_index = True
#                             break
                    
#                     if(not found_index):
#                         start_prefix = mapping[start_prefix]["mapto"]
#                         # print(start_prefix)
#                         # print(mapping_value)
#                 else:
#                     start_prefix = mapping[start_prefix]["mapto"]
                        

#             if(low_location == -1):
#                 low_location = mapping_value
#             elif(low_location > mapping_value):
#                 low_location = mapping_value
#     #         print(start_value, mapping_value, low_location)
#     print(seed_index)
#     loop_index += 1
# print("Part 2 : Lowest location number = ", low_location)

loop_index = 0
for seed_index in seed_numbers:
    if(loop_index%2 == 0):
        start_index = int(seed_index)
    else:
        range_list = [start_index, int(seed_index) + start_index-1]

        start_prefix = 'seed'
        
        while(start_prefix != 'location'):
            for index in mapping[start_prefix]["indexing"]:
                start_index    = index[0]
                number_indexes = index[1]
                mapped_index   = index[2]

                updated_range_list= []

                for range_index in range(len(range_list)-1):

                    left_index = range_list[range_index]
                    right_index = range_list[range_index+1]

                    if left_index < start_index:
                        updated_range_list.append(left_index)
                        
                        if(right_index < start_index):
                            updated_range_list.append(right_index)
                        elif (start_index <= right_index) and (right_index < start_index+number_indexes):
                            print("find intersection and parse appropriately")
                        else:
                            print("find intersection and parse appropriately")
                    elif (start_index <= left_index) and (left_index < start_index+number_indexes):
                        updated_range_list.append(mapped_index + (left_index - start_index)) 

                        if(right_index < start_index+number_indexes)
                    else:
                        updated_range_list.append(left_index)


            
            if(not found_index):
                start_prefix = mapping[start_prefix]["mapto"]
                # print(start_prefix)
                # print(mapping_value)
            print()
    loop_index += 1