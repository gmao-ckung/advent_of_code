import numpy as np

f1 = open("/home/ckung/Code/advent_of_code/2015/input.day6")

directions = f1.readlines()

light_array = np.zeros((1000,1000),dtype=np.int)

for direction in directions:
    split_directions = direction.split()
    # Determining whether directions are a "toggle" or a "turn" based
    # on the number of entries in split_directions
    
    if len(split_directions) == 4: # This is a "toggle" instruction
        coord_1 = split_directions[1].split(",")
        coord_2 = split_directions[3].split(",")
        for x in range(int(coord_1[0]),int(coord_2[0])+1):
            for y in range(int(coord_1[1]), int(coord_2[1])+1): # Use the XOR to toggle the light
                light_array[x,y] = light_array[x,y] ^ 1
    else: # This is a turn "on" or "off" instruction
        coord_1 = split_directions[2].split(",")
        coord_2 = split_directions[4].split(",")
        for x in range(int(coord_1[0]),int(coord_2[0])+1):
            for y in range(int(coord_1[1]), int(coord_2[1])+1):
                if split_directions[1] == "off":
                    light_array[x,y] = 0
                else:
                    light_array[x,y] = 1

print("Number of lights on =", sum(sum(light_array)))

light_array = np.zeros((1000,1000),dtype=np.int)

for direction in directions:
    split_directions = direction.split()
    # Determining whether directions are a "toggle" or a "turn" based
    # on the number of entries in split_directions
    
    if len(split_directions) == 4: # This is a "toggle" instruction
        coord_1 = split_directions[1].split(",")
        coord_2 = split_directions[3].split(",")
        for x in range(int(coord_1[0]),int(coord_2[0])+1):
            for y in range(int(coord_1[1]), int(coord_2[1])+1):
                light_array[x,y] = light_array[x,y] + 2
    else: # This is a turn "on" or "off" instruction
        coord_1 = split_directions[2].split(",")
        coord_2 = split_directions[4].split(",")
        for x in range(int(coord_1[0]),int(coord_2[0])+1):
            for y in range(int(coord_1[1]), int(coord_2[1])+1):
                if split_directions[1] == "off":
                    if(light_array[x,y] != 0):
                        light_array[x,y] = light_array[x,y] - 1
                else:
                    light_array[x,y] = light_array[x,y] + 1

print("Total Brightness of lights =", sum(sum(light_array)))