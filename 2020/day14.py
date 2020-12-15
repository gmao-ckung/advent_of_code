import os
import math
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day14")
data = f1.readlines()

mem_dict = {}

for line in data:
    line_s = line.split(" ")
    if line_s[0] == "mask":
        bit_mask = line_s[2].replace("\n", "")

        #print(bit_mask)

        bit_mask_dict = {}
        # Note : Bitmask length is 36 bits
        #        Leftmost bit is most significant (2^35)
        for i in range(len(bit_mask)):
            if bit_mask[i] == '1':
                bit_mask_dict[35-i] = 1
            elif bit_mask[i] == '0':
                bit_mask_dict[35-i] = 0
    else:

        for i in range(1,len(line_s)):
            mem_op = line.replace("\n","").split(" ")
            #print(mem_op)
            mem_num = mem_op[0][4:].split("]")[0]
            mem_val = mem_op[2]

            mem_dict[int(mem_num)] = int(mem_val)
            #print("Original Value =", mem_val)

            for key in bit_mask_dict.keys():
                if bit_mask_dict[key]:
                    mask = 1 << key
                    mem_dict[int(mem_num)] |= mask
                else:
                    mask = 1 << key
                    mem_dict[int(mem_num)] &= ~mask
                #print(mask)
                

#print(mem_dict)
totalSum = 0
for key in mem_dict.keys():
    totalSum += mem_dict[key]

print("Total Sum of values in memory =", totalSum)