import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)

f1 = open(CURR_DIR+"/input.day6")

all_answers = f1.readlines()

# *** Part 1 ***

total_group_sum = 0
curr_group_dictionary = {}

# Read entry on each line
for answer in all_answers:
    answer = answer.replace("\n", "")
    # This entry is not a new line
    if answer != "":
        # Examine each letter on a line
        for letter in answer:
            # If the letter has not been seen for a group, add it to 
            # the group dictionary
            if letter not in curr_group_dictionary:
                curr_group_dictionary[letter] = 1
    # Sum up the 'yes' answers for a group
    else:
        total_group_sum = total_group_sum + len(curr_group_dictionary)
        curr_group_dictionary = {}

total_group_sum = total_group_sum + len(curr_group_dictionary)
print("Part 1: Sum =", total_group_sum)

# *** Part 2 ***
total_group_sum = 0
people_per_group = 0
curr_group_dictionary = {}
for answer in all_answers:
    answer = answer.replace("\n", "")
    if answer != "":
        for letter in answer:
            if letter not in curr_group_dictionary:
                curr_group_dictionary[letter] = 1
            else:
                curr_group_dictionary[letter] = curr_group_dictionary[letter] + 1
        people_per_group = people_per_group + 1
    else:
        for key in curr_group_dictionary:
            if curr_group_dictionary[key] == people_per_group:
                total_group_sum = total_group_sum + 1
        curr_group_dictionary = {}
        people_per_group = 0

for key in curr_group_dictionary:
    if curr_group_dictionary[key] == people_per_group:
        total_group_sum = total_group_sum + 1
print("Part 2: Sum =", total_group_sum)