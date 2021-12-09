import numpy as np
import os
from support import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day8","r")
initialDataList = fopen.readlines()

patternDigits, outputDigits = grabDigits(initialDataList)

# print(outputDigits)

# Since 1, 4, 7, or 8 have 2, 4, 3, and 7 segments respectively,
# search outputDigits for entries with length 2, 4, 3, or 7

count_1_4_7_8 = 0

for output in outputDigits:
    numbers = output.split(" ")
    for number in numbers:
        if len(number) == 2 or len(number) == 4 or len(number) == 3 or len(number) == 7:
            # print(number)
            count_1_4_7_8 += 1

print("Part 1 : Total number of 1's, 4's, 7's, and 8's in output =", count_1_4_7_8)

totalSum = 0

for digit in range(len(patternDigits)):
    pattern_dict = create_init_pattern_dict(patternDigits[digit],outputDigits[digit])

    # Find "a" segment
    # a_segment = 
    a_segment = [x for x in set(sorted(list(pattern_dict[7]))).difference(set(sorted(list(pattern_dict[1]))))]
    # Find "b" and "d" segments, but not know which one is which
    bd_segments = [x for x in set(sorted(list(pattern_dict[4]))).difference(set(sorted(list(pattern_dict[1]))))]

    # Find "g" segment by finding nine
    patterns_len_6 = findPattern(patternDigits[digit],6)
    for pattern in patterns_len_6:
        if set(list(pattern_dict[4])).issubset(list(pattern)):
            g_segment = [x for x in set(sorted(list(pattern))).difference(set(sorted(list(pattern_dict[4]) + a_segment)))]
            pattern_dict[9] = pattern
            break

    # Find "e" segment by looking at eight
    e_segment = [x for x in set(sorted(list(pattern_dict[8]))).difference(set(sorted(list(a_segment + list(pattern_dict[4]) + g_segment))))]

    # Find zero and "d" segment
    for pattern in patterns_len_6:
        if set(list(pattern_dict[1]) + e_segment).issubset(list(pattern)):
            pattern_dict[0] = pattern
            d_segment = [x for x in set(sorted(list(pattern_dict[8]))).difference(set(sorted(list(pattern_dict[0]))))]

    # Find six by process of elimination
    patterns_len_6.remove(pattern_dict[9])
    patterns_len_6.remove(pattern_dict[0])
    pattern_dict[6] = patterns_len_6[0]

    # find segments "c" and "f"
    f_segment = [letter for letter in pattern_dict[1] if letter in pattern_dict[6]]
    c_segment = [letter for letter in pattern_dict[1] if letter is not f_segment[0]]

    patterns_len_5 = findPattern(patternDigits[digit], 5)

    pattern_dict[2] = a_segment[0]+c_segment[0]+d_segment[0]+e_segment[0]+g_segment[0]
    for pattern in patterns_len_5:
        if set(list(pattern)).issubset(list(pattern_dict[6])):
            pattern_dict[5] = pattern

    pattern_dict[3] = a_segment[0] + c_segment[0] + d_segment[0] + f_segment[0] + g_segment[0]

    number_str = ""
    
    for output in createList(outputDigits[digit]):
        sorted_O_list = sorted(list(output))
        for key in pattern_dict:
            compare_list = sorted(list(pattern_dict[key]))
            if compare_list == sorted_O_list:
                number_str += str(key)
                break
            
    totalSum += int(number_str)

print("Part 2: Sum of Output values = ", totalSum)