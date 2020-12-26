import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day19")
rules_and_dataToCheck = f1.readlines()

def traverse_rule_dictionary(instructions, rule_dict):
    combination_list = []
    combination_found = []
    for step in instructions:
        if step != '|':
            instruction = rule_dict[int(step)]
            #print(instruction)
            if len(instruction) == 1 and not instruction[0].isnumeric():
                combination_found.append(instruction)
            else:
                combination_found.append(traverse_rule_dictionary(instruction, rule_dict))
        else:
            if 2 == len(combination_found):
                for i in range(len(combination_found[0])):
                    for j in range(len(combination_found[1])):
                        combination_list.append(combination_found[0][i]+combination_found[1][j])
            elif 1 == len(combination_found):
                combination_list.append(combination_found[0])
            combination_found = []
                
    if 2 == len(combination_found):
        for i in range(len(combination_found[0])):
            for j in range(len(combination_found[1])):
                combination_list.append(combination_found[0][i]+combination_found[1][j])
    elif 1 == len(combination_found):
        for i in range(len(combination_found[0])):
            combination_list.append(combination_found[0][i])

    #print(combination_list)
    return combination_list

data_list = []
rule_dict = {}

for rule_or_data in rules_and_dataToCheck:
    rule_or_data = rule_or_data.replace("\n","")
    rule_or_data_s = rule_or_data.split(" ")
    #print(rule_or_data_s)
    #print(len(rule_or_data_s))
    # Rule line found
    if len(rule_or_data_s) > 1:
        if len(rule_or_data_s[1:]) == 1:
            rule_or_data_s[1] = rule_or_data_s[1].replace("\"","")
            if rule_or_data_s[1].isnumeric():
                rule_dict[int(rule_or_data_s[0].replace(":",""))] = [rule_or_data_s[1]]
            else:
                rule_dict[int(rule_or_data_s[0].replace(":",""))] = rule_or_data_s[1]
        else:
            rule_dict[int(rule_or_data_s[0].replace(":",""))] = rule_or_data_s[1:]
    # Data line found
    else:
        data_list.append(rule_or_data)

rule_0 = rule_dict[0]
rule_0_combination_dict = {}
rule_0_combination = ""
for rule in rule_0:
    #print(rule)
    instruction = rule_dict[int(rule)]
    #print(instruction)
    if len(instruction) == 1 and not instruction[0].isnumeric():
        rule_0_combination_dict[int(rule)] = instruction
    else:
        combination_list = traverse_rule_dictionary(instruction, rule_dict)
        rule_0_combination_dict[int(rule)] = combination_list

def assemble_potential_combinations(index, rule_0_dict, instruction, partial_combo, combo_list):
    curr_portion = rule_0_dict[int(instruction[index])]
    for part in curr_portion:
        curr_combo = partial_combo + part
        if index == len(instruction)-1:
            combo_list.append(curr_combo)
        else:
            assemble_potential_combinations(index+1,rule_0_dict, instruction, curr_combo, combo_list)
    return combo_list

# partial_combo = ""
# combo_list = []
# combo_list = assemble_potential_combinations(0, rule_0_combination_dict, rule_dict[0], partial_combo, combo_list)
# #print(combo_list)

# count = 0
# for data in data_list:
#     for combo in combo_list:
#         if combo == data:
#             count += 1

# print("Part 1: Matches to Rule 0 =", count)

# *** Part 2 ***

rule_8_size = len(rule_0_combination_dict[8][0])


# Extract "thirty-one"-type combinations
thirty_one_portions = []
for rule in rule_0_combination_dict[11]:
    if rule[rule_8_size:] not in thirty_one_portions:
        thirty_one_portions.append(rule[rule_8_size:])

count = 0

for data in data_list:
    forty_two_count = 0
    while data[forty_two_count*rule_8_size:(forty_two_count+1)*rule_8_size] in rule_0_combination_dict[8]:
        forty_two_count += 1
        print("42 count =", forty_two_count)
    
    found = False
    if(forty_two_count >= 2):
        thirty_one_count = 0
        FTC_2 = forty_two_count
        while data[FTC_2*rule_8_size:(FTC_2+1)*rule_8_size] in thirty_one_portions:
            thirty_one_count += 1
            FTC_2 += 1
            if FTC_2*rule_8_size >= len(data):
                if forty_two_count > thirty_one_count:
                    count += 1
                    found = True
                    break
        
    if found:
        print(data, "is a match!")

print("Part 2: Matches to Rule 0 =", count)
            