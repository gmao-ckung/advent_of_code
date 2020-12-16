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

print("Part 1: Total Sum of values in memory =", totalSum)

def compute_address(mask, curr_bit, part_addr_sum, ref_addr, mem_dict, write_value):
    if curr_bit == 35:
        if mask[curr_bit] == '1':
            address = part_addr_sum + 1
            mem_dict[address] = write_value
            return mem_dict
        elif mask[curr_bit] == '0':
            address = part_addr_sum + (ref_addr & 1 << (35 - curr_bit))
            mem_dict[address] = write_value
            return mem_dict
        else:
            mem_dict[part_addr_sum]   = write_value
            mem_dict[part_addr_sum+1] = write_value
            return mem_dict
    else:
        if mask[curr_bit] == '1':
            address = part_addr_sum + (1 << (35-curr_bit))
            mem_dict = compute_address(mask, \
                                       curr_bit + 1, \
                                       address,
                                       ref_addr,
                                       mem_dict,
                                       write_value)
            return mem_dict
        elif mask[curr_bit] == '0':
            address = part_addr_sum + (ref_addr & (1 << (35 - curr_bit)))
            mem_dict = compute_address(mask, \
                                       curr_bit + 1, \
                                       address,
                                       ref_addr,
                                       mem_dict,
                                       write_value)
            return mem_dict
        else:
            mem_dict = compute_address(mask, \
                                       curr_bit + 1, \
                                       part_addr_sum,
                                       ref_addr,
                                       mem_dict,
                                       write_value)

            address = part_addr_sum + (1 << (35-curr_bit))
            mem_dict = compute_address(mask, \
                                       curr_bit + 1, \
                                       address,
                                       ref_addr,
                                       mem_dict,
                                       write_value)

            return mem_dict

mem_dict = {}

for line in data:
    line_s = line.split(" ")
    if line_s[0] == "mask":
        bit_mask = line_s[2].replace("\n", "")
    else:
        mem_op = line.replace("\n","").split(" ")
        #print(mem_op)
        mem_num = mem_op[0][4:].split("]")[0]
        mem_val = mem_op[2]
        mem_dict = compute_address(bit_mask, 0, 0, int(mem_num), mem_dict, int(mem_val))

#print(mem_dict)

tSum = 0
for key in mem_dict.keys():
    tSum += mem_dict[key]

print("Part 2: Total Sum of Values in Memory =", tSum)
