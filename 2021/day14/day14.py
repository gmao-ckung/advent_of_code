import os
import sys

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")
poly_template = fopen.readlines()

start_template = list(poly_template[0].replace("\n",""))

pair_insertion_rules = {}

for i in range(2,len(poly_template)):
    rule = poly_template[i].replace("\n","").split(" -> ")
    pair_insertion_rules[rule[0]] = rule[1]

# print(pair_insertion_rules)

# steps = 10
# for step in range(steps):
#     print("Step =",step)
#     print("Start Template Length =",len(start_template))
#     new_template = []
#     for i in range(len(start_template)-1):
#         new_template.append(start_template[i])
#         new_template.append(pair_insertion_rules[start_template[i]+start_template[i+1]])
#     new_template.append(start_template[-1])
#     start_template = new_template

# # print(start_template)

# letters = "ABCDEFGHIJKLMNOPQURSTUWXYZ"

# letter_count = {}
# max_count = 0
# min_count = len(start_template)
# for letter in letters:
#     if start_template.count(letter) > max_count:
#         max_count = start_template.count(letter)
#     if start_template.count(letter) < min_count and start_template.count(letter) != 0:
#         min_count = start_template.count(letter)

# print("Part 1 : Most Common - Least Common = ", max_count- min_count)

start_template = list(poly_template[0].replace("\n",""))

letters = "ABCDEFGHIJKLMNOPQURSTUWXYZ"
letter_counter = {}

for letter in letters:
    letter_counter[letter] = 0

def recursive_count(letter1, letter2, curr_step, tot_step, pair_insertion_rules, letter_counter, count_letter=True):
    # print("curr_step = ", curr_step)
    if curr_step < tot_step:
        # print("Letter 1 =", letter1)
        # print("Letter 2 =", letter2)
       
        recursive_count(letter1, pair_insertion_rules[letter1+letter2],curr_step+1,tot_step,pair_insertion_rules, letter_counter, count_letter)
        recursive_count(pair_insertion_rules[letter1+letter2], letter2, curr_step+1,tot_step,pair_insertion_rules,letter_counter, False)
    else:
        # print("Letter 1 =", letter1)
        # print("Letter 2 =", letter2)
        if count_letter:
            letter_counter[letter1] = +1
        letter_counter[letter2] += 1
        return

steps = 20
for i in range(len(start_template)-1):
    print(i, "of", len(start_template))
    if i == 0:
        recursive_count(start_template[i], start_template[i+1], 0, steps, pair_insertion_rules, letter_counter)
    else:
        recursive_count(start_template[i], start_template[i+1], 0, steps, pair_insertion_rules, letter_counter, False)

print(letter_counter)

max_count = 0
min_count = sys.maxsize
for letter in letter_counter.keys():
    if letter_counter[letter] > max_count:
        max_count = letter_counter[letter]
    if letter_counter[letter] < min_count and letter_counter[letter] != 0:
        min_count = letter_counter[letter]

print("Part 1 : Most Common - Least Common = ", max_count- min_count)