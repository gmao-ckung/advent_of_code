import os
import copy

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.06","r")

map = file.read().splitlines()

row = 0
roadblock_row = {}
guard = [None, None, None] # Direction, Row, Col
for map_line in map:
    index = 0
    # Find roadblock_rows
    while index < len(map_line):
        index = map_line.find('#',index)
        if index == -1:
            break
        if(row not in roadblock_row.keys()):
            roadblock_row[row] = [index]
        else:
            roadblock_row[row].append(index)
        # print(roadblock_row)
        index += 1
    # Find guard looking North
    index = 0
    while index < len(map_line):
        index = map_line.find('^',index)
        if index == -1:
            break
        
        guard[0] = 'N'
        guard[1] = row
        guard[2] = index
        break

    # Find guard looking South
    index = 0
    while index < len(map_line):
        index = map_line.find('v',index)
        if index == -1:
            break
        
        guard[0] = 'S'
        guard[1] = row
        guard[2] = index
        break

    # Find guard looking East
    index = 0
    while index < len(map_line):
        index = map_line.find('>',index)
        if index == -1:
            break
        
        guard[0] = 'E'
        guard[1] = row
        guard[2] = index
        break

    # Find guard looking West
    index = 0
    while index < len(map_line):
        index = map_line.find('<',index)
        if index == -1:
            break
        
        guard[0] = 'W'
        guard[1] = row
        guard[2] = index
        break

    row += 1
    
total_rows = row
total_cols = len(map_line)

roadblock_col = {}
for key in roadblock_row.keys():
    for col in roadblock_row[key]:
        if col not in roadblock_col.keys():
            roadblock_col[col] = [key]
        else:
            roadblock_col[col].append(key)

escape = False
num_steps = 0

orig_direction = guard[0]
visited_spots = [[guard[1], guard[2]]]


while escape == False:
    match guard[0]:
        case 'N':
            if(guard[2] in roadblock_col.keys()):
                distance = None
                for row_loc in roadblock_col[guard[2]]:
                    if (guard[1] - row_loc) > 0:
                        if (distance is None or ((guard[1]-row_loc) < distance)):
                            distance = guard[1] - row_loc

                if distance != None:
                    num_steps += distance - 1
                    for i in range(1,distance):
                        guard[1] -= 1
                        if [guard[1], guard[2]] not in visited_spots:
                            visited_spots.append([guard[1], guard[2]])
                    # guard[1] = guard[1] - (distance - 1)
                else:
                    num_steps += guard[1]
                    for i in range(1,guard[1]+1):
                        guard[1] -= 1
                        if [guard[1], guard[2]] not in visited_spots:
                            visited_spots.append([guard[1], guard[2]])
                    escape = True
            guard[0] = 'E'
        case 'S':
            if(guard[2] in roadblock_col.keys()):
                distance = None
                for row_loc in roadblock_col[guard[2]]:
                    if (row_loc - guard[1]) > 0:
                        if distance is None or (row_loc - guard[1] < distance):
                            distance = row_loc - guard[1]

                if distance != None:
                    num_steps += distance - 1
                    for i in range(1,distance):
                        guard[1] += 1
                        if [guard[1], guard[2]] not in visited_spots:
                            visited_spots.append([guard[1], guard[2]])
                    # guard[1] = guard[1] + (distance - 1)
                else:
                    num_steps += total_rows - guard[1] - 1
                    for i in range(1,total_rows - guard[1]):
                        guard[1] += 1
                        if [guard[1], guard[2]] not in visited_spots:
                            visited_spots.append([guard[1], guard[2]])
                    escape = True
            guard[0] = 'W'
        case 'E':
            if(guard[1] in roadblock_row.keys()):
                distance = None
                for col_loc in roadblock_row[guard[1]]:
                    if (col_loc - guard[2]) > 0:
                        if distance is None or ((col_loc - guard[2]) < distance):
                            distance = col_loc - guard[2]
                        
                if distance != None:
                    num_steps += distance - 1
                    for i in range(1,distance):
                        guard[2] += 1
                        if [guard[1], guard[2]] not in visited_spots:
                            visited_spots.append([guard[1], guard[2]])
                    # guard[2] = guard[2] + (distance - 1)
                else:
                    num_steps += total_cols - guard[2] - 1
                    for i in range(1,total_cols - guard[2]):
                        guard[2] += 1
                        if [guard[1], guard[2]] not in visited_spots:
                            visited_spots.append([guard[1], guard[2]])
                    escape = True
            guard[0] = 'S'
        case 'W':
            if(guard[1] in roadblock_row.keys()):
                distance = None
                for col_loc in roadblock_row[guard[1]]:
                    if (guard[2] - col_loc) > 0:
                        if distance is None or ((guard[2] - col_loc) < distance):
                            distance = guard[2] - col_loc
                        
                if distance != None:
                    num_steps += distance - 1
                    for i in range(1,distance):
                        guard[2] -= 1
                        if [guard[1], guard[2]] not in visited_spots:
                            visited_spots.append([guard[1], guard[2]])
                    # guard[2] = guard[2] - (distance - 1)
                else:
                    num_steps += guard[2]
                    for i in range(1,guard[2]+1):
                        guard[2] -= 1
                        if [guard[1], guard[2]] not in visited_spots:
                            visited_spots.append([guard[1], guard[2]])
                    escape = True
            guard[0] = 'N'
    # print(visited_spots)
print('Number of unique visited spots = ', len(visited_spots))


# Note, very slow!
num_steps_block = 100000
num_obstructions = 0

for spot in visited_spots[1:]:
    print(spot)

    visited_spots_2 = [visited_spots[0].copy()]
    guard = [orig_direction, visited_spots[0][0], visited_spots[0][1]]
    escape = False

    roadblock_col_2 = copy.deepcopy(roadblock_col)
    roadblock_row_2 = copy.deepcopy(roadblock_row)

    if spot[0] not in roadblock_row_2.keys():
        roadblock_row_2[spot[0]] = spot[1]
    else:
        roadblock_row_2[spot[0]].append(spot[1])

    if spot[1] not in roadblock_col_2.keys():
        roadblock_col_2[spot[1]] = spot[0]
    else:
        roadblock_col_2[spot[1]].append(spot[0])

    num_steps = 0
    while escape == False:
        # print(num_steps)
        if num_steps_block < num_steps:
            # print()
            num_obstructions += 1
            break
        match guard[0]:
            case 'N':
                if(guard[2] in roadblock_col_2.keys()):
                    distance = None
                    for row_loc in roadblock_col_2[guard[2]]:
                        if (guard[1] - row_loc) > 0:
                            if (distance is None or ((guard[1]-row_loc) < distance)):
                                distance = guard[1] - row_loc

                    if distance != None:
                        num_steps += distance - 1
                        for i in range(1,distance):
                            guard[1] -= 1
                            if [guard[1], guard[2]] not in visited_spots_2:
                                visited_spots_2.append([guard[1], guard[2]])
                        # guard[1] = guard[1] - (distance - 1)
                    else:
                        num_steps += guard[1]
                        for i in range(1,guard[1]+1):
                            guard[1] -= 1
                            if [guard[1], guard[2]] not in visited_spots_2:
                                visited_spots_2.append([guard[1], guard[2]])
                        escape = True
                else:
                    num_steps += guard[1]
                    for i in range(1,guard[1]+1):
                        guard[1] -= 1
                        if [guard[1], guard[2]] not in visited_spots_2:
                            visited_spots_2.append([guard[1], guard[2]])
                    escape = True
                guard[0] = 'E'
            case 'S':
                if(guard[2] in roadblock_col_2.keys()):
                    distance = None
                    for row_loc in roadblock_col_2[guard[2]]:
                        if (row_loc - guard[1]) > 0:
                            if distance is None or (row_loc - guard[1] < distance):
                                distance = row_loc - guard[1]

                    if distance != None:
                        num_steps += distance - 1
                        for i in range(1,distance):
                            guard[1] += 1
                            if [guard[1], guard[2]] not in visited_spots_2:
                                visited_spots_2.append([guard[1], guard[2]])
                        # guard[1] = guard[1] + (distance - 1)
                    else:
                        num_steps += total_rows - guard[1] - 1
                        for i in range(1,total_rows - guard[1]):
                            guard[1] += 1
                            if [guard[1], guard[2]] not in visited_spots_2:
                                visited_spots_2.append([guard[1], guard[2]])
                        escape = True
                else:
                    num_steps += total_rows - guard[1] - 1
                    for i in range(1,total_rows - guard[1]):
                        guard[1] += 1
                        if [guard[1], guard[2]] not in visited_spots_2:
                            visited_spots_2.append([guard[1], guard[2]])
                    escape = True
                guard[0] = 'W'
            case 'E':
                if(guard[1] in roadblock_row_2.keys()):
                    distance = None
                    for col_loc in roadblock_row_2[guard[1]]:
                        if (col_loc - guard[2]) > 0:
                            if distance is None or ((col_loc - guard[2]) < distance):
                                distance = col_loc - guard[2]
                            
                    if distance != None:
                        num_steps += distance - 1
                        for i in range(1,distance):
                            guard[2] += 1
                            if [guard[1], guard[2]] not in visited_spots_2:
                                visited_spots_2.append([guard[1], guard[2]])
                        # guard[2] = guard[2] + (distance - 1)
                    else:
                        num_steps += total_cols - guard[2] - 1
                        for i in range(1,total_cols - guard[2]):
                            guard[2] += 1
                            if [guard[1], guard[2]] not in visited_spots_2:
                                visited_spots_2.append([guard[1], guard[2]])
                        escape = True
                else:
                    num_steps += total_cols - guard[2] - 1
                    for i in range(1,total_cols - guard[2]):
                        guard[2] += 1
                        if [guard[1], guard[2]] not in visited_spots_2:
                            visited_spots_2.append([guard[1], guard[2]])
                    escape = True
                guard[0] = 'S'
            case 'W':
                if(guard[1] in roadblock_row_2.keys()):
                    distance = None
                    for col_loc in roadblock_row_2[guard[1]]:
                        if (guard[2] - col_loc) > 0:
                            if distance is None or ((guard[2] - col_loc) < distance):
                                distance = guard[2] - col_loc
                            
                    if distance != None:
                        num_steps += distance - 1
                        for i in range(1,distance):
                            guard[2] -= 1
                            if [guard[1], guard[2]] not in visited_spots_2:
                                visited_spots_2.append([guard[1], guard[2]])
                        # guard[2] = guard[2] - (distance - 1)
                    else:
                        num_steps += guard[2]
                        for i in range(1,guard[2]+1):
                            guard[2] -= 1
                            if [guard[1], guard[2]] not in visited_spots_2:
                                visited_spots_2.append([guard[1], guard[2]])
                        escape = True
                else:
                    num_steps += guard[2]
                    for i in range(1,guard[2]+1):
                        guard[2] -= 1
                        if [guard[1], guard[2]] not in visited_spots_2:
                            visited_spots_2.append([guard[1], guard[2]])
                    escape = True
                guard[0] = 'N'
    print("Escaped!")

print('Number of unique obstructions = ', num_obstructions)