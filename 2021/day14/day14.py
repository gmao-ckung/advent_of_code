import os
import sys

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day14","r")
poly_template = fopen.readlines()

start_template = list(poly_template[0].replace("\n",""))

pair_insertion_rules = {}

for i in range(2,len(poly_template)):
    rule = poly_template[i].replace("\n","").split(" -> ")
    pair_insertion_rules[rule[0]] = rule[1]

start_template = list(poly_template[0].replace("\n",""))

letter_counter = {}
letter_pair_counter = {}

for letter in start_template:
    if letter not in letter_counter.keys():
        letter_counter[letter] = 1
    else:
        letter_counter[letter] += 1

for i in range(len(start_template)-1):
    if start_template[i]+start_template[i+1] not in letter_pair_counter.keys():
        letter_pair_counter[start_template[i]+start_template[i+1]] = 1
    else:
        letter_pair_counter[start_template[i]+start_template[i+1]] += 1

steps = 10
for i in range(steps):
    new_letter_pair_counter = {}
    for key in letter_pair_counter.keys():
        added_letter = pair_insertion_rules[key]
        if added_letter not in letter_counter.keys():
            letter_counter[added_letter] = 1 * letter_pair_counter[key]
        else:
            letter_counter[added_letter] += 1 * letter_pair_counter[key]
        pair1 = key[0]+added_letter
        pair2 = added_letter+key[1]

        if pair1 not in new_letter_pair_counter.keys():
            new_letter_pair_counter[pair1] = 1* letter_pair_counter[key]
        else:
            new_letter_pair_counter[pair1] += 1* letter_pair_counter[key]

        if pair2 not in new_letter_pair_counter.keys():
            new_letter_pair_counter[pair2] = 1* letter_pair_counter[key]
        else:
            new_letter_pair_counter[pair2] += 1* letter_pair_counter[key]
            
    letter_pair_counter = new_letter_pair_counter

max_count = 0
min_count = sys.maxsize
for letter in letter_counter.keys():
    if letter_counter[letter] > max_count:
        max_count = letter_counter[letter]
    if letter_counter[letter] < min_count:
        min_count = letter_counter[letter]

print("Part 1 : Most Common - Least Common = ", max_count- min_count)

letter_counter = {}
letter_pair_counter = {}

for letter in start_template:
    if letter not in letter_counter.keys():
        letter_counter[letter] = 1
    else:
        letter_counter[letter] += 1

for i in range(len(start_template)-1):
    if start_template[i]+start_template[i+1] not in letter_pair_counter.keys():
        letter_pair_counter[start_template[i]+start_template[i+1]] = 1
    else:
        letter_pair_counter[start_template[i]+start_template[i+1]] += 1

steps = 40
for i in range(steps):
    new_letter_pair_counter = {}
    for key in letter_pair_counter.keys():
        added_letter = pair_insertion_rules[key]
        if added_letter not in letter_counter.keys():
            letter_counter[added_letter] = 1 * letter_pair_counter[key]
        else:
            letter_counter[added_letter] += 1 * letter_pair_counter[key]
        pair1 = key[0]+added_letter
        pair2 = added_letter+key[1]

        if pair1 not in new_letter_pair_counter.keys():
            new_letter_pair_counter[pair1] = 1* letter_pair_counter[key]
        else:
            new_letter_pair_counter[pair1] += 1* letter_pair_counter[key]

        if pair2 not in new_letter_pair_counter.keys():
            new_letter_pair_counter[pair2] = 1* letter_pair_counter[key]
        else:
            new_letter_pair_counter[pair2] += 1* letter_pair_counter[key]
            
    letter_pair_counter = new_letter_pair_counter

max_count = 0
min_count = sys.maxsize
for letter in letter_counter.keys():
    if letter_counter[letter] > max_count:
        max_count = letter_counter[letter]
    if letter_counter[letter] < min_count:
        min_count = letter_counter[letter]

print("Part 2 : Most Common - Least Common = ", max_count- min_count)