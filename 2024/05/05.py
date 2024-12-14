import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.05","r")

rule = {}
updates = []
puzzle = file.read().splitlines()
for line in puzzle:
    if '|' in line:
        # print(line)
        separate_line = line.split('|')
        # print(separate_line)

        if separate_line[0] not in rule.keys():
            rule[separate_line[0]] = [separate_line[1]]
        else:
            rule[separate_line[0]].append(separate_line[1])

    elif line != '':
        updates.append(line.split(','))

MPN_sum = 0

for update in updates:
    correctUpdate = True
    for curr_index in range(len(update)):
        for check_index in range(curr_index+1,len(update)):
            # print('curr_index = ', curr_index, update[curr_index])
            # print('check_index = ', check_index, update[check_index])
            # print('rule :', rule[update[curr_index]])
            if update[curr_index] in rule.keys():
                if update[check_index] not in rule[update[curr_index]]:
                    correctUpdate = False
            else:
                correctUpdate = False
            
    if correctUpdate:
        MPN_sum += int(update[int(len(update)/2)])

print("Part 1: Middle Page Number sum = ", MPN_sum)

MPN_sum = 0

for update in updates:
    correctUpdate = True
    for curr_index in range(len(update)):
        for check_index in range(curr_index+1,len(update)):
            # print('curr_index = ', curr_index, update[curr_index])
            # print('check_index = ', check_index, update[check_index])
            # print('rule :', rule[update[curr_index]])
            if update[curr_index] in rule.keys():
                if update[check_index] not in rule[update[curr_index]]:
                    correctUpdate = False
            else:
                correctUpdate = False
    

    if not correctUpdate:
        midpoint = int(len(update)/2)
        for curr_index in range(len(update)):
            num_in_rule = 0
            for check_index in range(len(update)):
                if curr_index != check_index and update[curr_index] in rule.keys():
                    if update[check_index] in rule[update[curr_index]]:
                        num_in_rule += 1
            if num_in_rule == midpoint:
                MPN_sum += int(update[curr_index])
                break

print("Part 2 : Middle Page Number sum = ", MPN_sum)