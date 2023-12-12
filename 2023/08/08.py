import os
import math

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/input.in","r")

map_directions = file.read().splitlines()

pattern = map_directions[0]

node_mapping = {}
for node in range(2,len(map_directions)):
    # print(map_directions[node])
    node_split = map_directions[node].split(" = ")
    # print(node_split)
    if node_split[0] not in node_mapping:
        node_mapping[node_split[0]] = {}
        node_mapping[node_split[0]]['L'] = node_split[1][1:9].split(', ')[0]
        node_mapping[node_split[0]]['R'] = node_split[1][1:9].split(', ')[1]
        # print(node_mapping[node_split[0]])

steps = 0
curr_node = 'AAA'
while(curr_node != 'ZZZ'):
    curr_node = node_mapping[curr_node][pattern[steps%len(pattern)]]
    # print(curr_node)
    steps += 1

print(f"Part 1 : Steps = {steps}")

current_nodes = []

for node in node_mapping:
    if node[2] == 'A':
        current_nodes.append(node)

steps = []
for i in range(len(current_nodes)):
    curr_steps = 0
    third_letter = ''
    while(third_letter != 'Z'):
        current_nodes[i] = node_mapping[current_nodes[i]][pattern[curr_steps%len(pattern)]]
        third_letter = current_nodes[i][2]
        # print(solution)
        curr_steps += 1
    steps.append(curr_steps)

print(f"Part 2 : Steps = {math.lcm(*steps)}")