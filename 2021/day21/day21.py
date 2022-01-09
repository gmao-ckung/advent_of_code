import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")
start_positions = fopen.readlines()

player_1_pos = int(start_positions[0].split(" ")[-1].replace("\n", ""))
player_2_pos = int(start_positions[1].split(" ")[-1].replace("\n", ""))

# *** Part 1 ***

player_1_score = 0
player_2_score = 0

die_max_val = 100

def check_die(current_number, die_max_val):
    if current_number > die_max_val:
        return current_number - die_max_val
    else:
        return current_number

def check_pos(current_pos, max_pos):
    if current_pos > max_pos:
        return current_pos - max_pos
    else:
        return current_pos

current_die_value = 0
num_die_rolls = 0
while True:

    for i in range(3):
        current_die_value += 1
        current_die_value = check_die(current_die_value, die_max_val)
        player_1_pos += current_die_value%10
        player_1_pos = check_pos(player_1_pos,10)

    num_die_rolls += 3
    player_1_score += player_1_pos
    print("Player 1 Score =", player_1_score)
    if player_1_score >= 1000:
        print("Player 1 wins with score of", player_1_score)
        print("Weird calculation =", player_2_score*num_die_rolls)
        break

    for i in range(3):
        current_die_value += 1
        current_die_value = check_die(current_die_value, die_max_val)
        player_2_pos += current_die_value%10
        player_2_pos = check_pos(player_2_pos, 10)

    num_die_rolls += 3
    player_2_score += player_2_pos

    print("Player 2 Score =", player_2_score)
    if player_2_score >= 1000:
        print("Player 2 wins with score of", player_2_score)
        print("Weird calculation =", player_1_score*num_die_rolls)
        break

# *** Part 2 ***
player_1_pos = int(start_positions[0].split(" ")[-1].replace("\n", ""))
player_2_pos = int(start_positions[1].split(" ")[-1].replace("\n", ""))

player_1_win_cnt = 0
player_2_win_cnt = 0

p1_curr_pos_dict = {player_1_pos : 1} 
p2_curr_pos_dict = {player_2_pos : 1}
p1_score_dict = {0 : 1}
p2_score_dict = {0 : 1}

p1_curr_pos_and_score_dict = {str(player_1_pos)+",0" : 1}
p2_curr_pos_and_score_dict = {str(player_2_pos)+",0" : 1}

scale_factor_const = [1, 3, 6, 7, 6, 3, 1]
possible_roll_results = [3, 4, 5, 6, 7, 8, 9]

# Frequency of roll results if die is rolled 3 times
# 3 -> 1 time
# 4 -> 3 times
# 5 -> 6 times
# 6 -> 7 times
# 7 -> 6 times
# 8 -> 3 times
# 9 -> 1 time

def roll_dirac_die(previous_player_position_and_score_dict, current_player_position_and_score_dict, current_player_win_count):
    current_p_next_pos_score_dict = {}
    for previous_p_pos_score_key in previous_player_position_and_score_dict.keys():
        for current_p_pos_score_key in current_player_position_and_score_dict.keys():
            curr_p_pos = int(current_p_pos_score_key.split(",")[0])
            curr_p_score = int(current_p_pos_score_key.split(",")[1])
            temp_next_pos_dict = {}
            for i in range(len(possible_roll_results)):
                print("P1 Current Position", curr_p_pos, "occurs", current_player_position_and_score_dict[current_p_pos_score_key], "time(s)")
                print("Rolled a", possible_roll_results[i])
                new_position = curr_p_pos + possible_roll_results[i]
                new_position = check_pos(new_position,10)
                if new_position not in temp_next_pos_dict.keys():
                    temp_next_pos_dict[new_position] = scale_factor_const[i] * current_player_position_and_score_dict[current_p_pos_score_key] * previous_player_position_and_score_dict[previous_p_pos_score_key]
                else:
                    temp_next_pos_dict[new_position] += scale_factor_const[i] * current_player_position_and_score_dict[current_p_pos_score_key] * previous_player_position_and_score_dict[previous_p_pos_score_key]
            for new_position in temp_next_pos_dict.keys():
                if curr_p_score + new_position >= 21:
                    current_player_win_count += temp_next_pos_dict[new_position]
                else:
                    if str(new_position)+","+str(curr_p_score+new_position) not in current_p_next_pos_score_dict.keys():
                        current_p_next_pos_score_dict[str(new_position)+","+str(curr_p_score+new_position)] = temp_next_pos_dict[new_position]
                    else: 
                        current_p_next_pos_score_dict[str(new_position)+","+str(curr_p_score+new_position)] += temp_next_pos_dict[new_position]

    current_player_position_and_score_dict = current_p_next_pos_score_dict
    print("****")
    for current_p_pos_score_key in current_player_position_and_score_dict.keys():
        curr_p_pos = int(current_p_pos_score_key.split(",")[0])
        curr_p_score = int(current_p_pos_score_key.split(",")[1])
        print("Position", curr_p_pos,"has score =", curr_p_score, "occuring", current_player_position_and_score_dict[current_p_pos_score_key], "time(s)")
    print("****")

    return current_player_position_and_score_dict, current_player_win_count

while True:
    p1_curr_pos_and_score_dict, player_1_win_cnt = roll_dirac_die(p2_curr_pos_and_score_dict, p1_curr_pos_and_score_dict, player_1_win_cnt)
    print()
    p2_curr_pos_and_score_dict, player_2_win_cnt = roll_dirac_die(p1_curr_pos_and_score_dict,p2_curr_pos_and_score_dict,player_2_win_cnt)
    print()
    # p1_next_pos_score_dict = {}
    # for p2_pos_score_key in p2_curr_pos_and_score_dict.keys():
    #     for p1_pos_score_key in p1_curr_pos_and_score_dict.keys():
    #         p1_pos = int(p1_pos_score_key.split(",")[0])
    #         p1_score = int(p1_pos_score_key.split(",")[1])
    #         temp_next_pos_dict = {}
    #         for i in range(len(possible_roll_results)):
    #             print("P1 Current Position", p1_pos, "occurs", p1_curr_pos_and_score_dict[p1_pos_score_key], "time(s)")
    #             print("Rolled a", possible_roll_results[i])
    #             new_position = p1_pos + possible_roll_results[i]
    #             new_position = check_pos(new_position,10)
    #             if new_position not in temp_next_pos_dict.keys():
    #                 temp_next_pos_dict[new_position] = scale_factor_const[i] * p1_curr_pos_and_score_dict[p1_pos_score_key] * p2_curr_pos_and_score_dict[p2_pos_score_key]
    #             else:
    #                 temp_next_pos_dict[new_position] += scale_factor_const[i] * p1_curr_pos_and_score_dict[p1_pos_score_key] * p2_curr_pos_and_score_dict[p2_pos_score_key]
    #         for new_position in temp_next_pos_dict.keys():
    #             if p1_score + new_position >= 21:
    #                 player_1_win_cnt += temp_next_pos_dict[new_position]
    #             else:
    #                 if p1_score + new_position not in p1_next_pos_score_dict.keys():
    #                     p1_next_pos_score_dict[str(new_position)+","+str(p1_score+new_position)] = temp_next_pos_dict[new_position]
    #                 else: 
    #                     p1_next_pos_score_dict[str(new_position)+","+str(p1_score+new_position)] += temp_next_pos_dict[new_position]

    # p1_curr_pos_and_score_dict = p1_next_pos_score_dict
    # print("****")
    # for p1_pos_score_key in p1_curr_pos_and_score_dict.keys():
    #     p1_pos = int(p1_pos_score_key.split(",")[0])
    #     p1_score = int(p1_pos_score_key.split(",")[1])
    #     print("Position", p1_pos,"has score =", p1_score)
    # print("****")


while True:
    player_1_next_score_dict = {}
    player_1_next_position_dict = {}
    for p2_pos_key in p2_curr_pos_dict.keys():
        for p1_pos_key in p1_curr_pos_dict.keys():
            temp_next_pos_dict = {}
            for i in range(len(possible_roll_results)):
                print("P1 Current Position", p1_pos_key, "occurs", p1_curr_pos_dict[p1_pos_key], "times")
                print("Rolled a", possible_roll_results[i])
                new_position = p1_pos_key + possible_roll_results[i]
                new_position = check_pos(new_position,10)
                if new_position not in temp_next_pos_dict.keys():
                    temp_next_pos_dict[new_position] = scale_factor_const[i] * p1_curr_pos_dict[p1_pos_key] * p2_curr_pos_dict[p2_pos_key]
                else:
                    temp_next_pos_dict[new_position] += scale_factor_const[i] * p1_curr_pos_dict[p1_pos_key] * p2_curr_pos_dict[p2_pos_key]
                print("P1 New Position at", new_position, "occurs", temp_next_pos_dict[new_position], "times")
            for p1_score_key in p1_score_dict.keys():
                for new_position in temp_next_pos_dict.keys():
                    if p1_score_key + new_position >= 21:
                        player_1_win_cnt += temp_next_pos_dict[new_position]
                    else:
                        if p1_score_key + new_position not in player_1_next_score_dict.keys():
                            player_1_next_score_dict[p1_score_key + new_position] = temp_next_pos_dict[new_position]
                        else: 
                            player_1_next_score_dict[p1_score_key + new_position] += temp_next_pos_dict[new_position]
            for key in temp_next_pos_dict.keys():
                if key not in player_1_next_position_dict.keys():
                    player_1_next_position_dict[key] = temp_next_pos_dict[key]
                else:
                    player_1_next_position_dict[key] += temp_next_pos_dict[key]
        print("****")
        
    p1_score_dict = player_1_next_score_dict
    p1_curr_pos_dict = player_1_next_position_dict

    if len(player_1_next_position_dict) == 0:
        break

    print(p1_score_dict)

    player_2_next_position_dict = {}
    player_2_next_score_dict = {}
    for p1_pos_key in p1_curr_pos_dict.keys():
        for p2_pos_key in p2_curr_pos_dict.keys():
            temp_next_pos_dict = {}
            for i in range(len(possible_roll_results)):
                print("P2 Current Position", p2_pos_key, "occurs", p2_curr_pos_dict[p2_pos_key], "times")
                print("Rolled a", possible_roll_results[i])
                new_position = p2_pos_key + possible_roll_results[i]
                new_position = check_pos(new_position,10)
                if new_position not in temp_next_pos_dict.keys():
                    temp_next_pos_dict[new_position] = scale_factor_const[i] * p2_curr_pos_dict[p2_pos_key] * p1_curr_pos_dict[p1_pos_key]
                else:
                    temp_next_pos_dict[new_position] += scale_factor_const[i] * p2_curr_pos_dict[p2_pos_key] * p1_curr_pos_dict[p1_pos_key]
                print("P2 New Position at", new_position, "occurs", temp_next_pos_dict[new_position], "times")


            for p2_score_key in p2_score_dict.keys():
                for new_position in temp_next_pos_dict.keys():
                    if p2_score_key + new_position >= 21:
                        player_2_win_cnt += temp_next_pos_dict[new_position]
                    else:
                        if p2_score_key + new_position not in player_2_next_score_dict.keys():
                            player_2_next_score_dict[p2_score_key + new_position] = temp_next_pos_dict[new_position]
                        else: 
                            player_2_next_score_dict[p2_score_key + new_position] += temp_next_pos_dict[new_position]
        
            for key in temp_next_pos_dict.keys():
                if key not in player_2_next_position_dict.keys():
                    player_2_next_position_dict[key] = temp_next_pos_dict[key]
                else:
                    player_2_next_position_dict[key] += temp_next_pos_dict[key]
    
    p2_score_dict = player_2_next_score_dict
    p2_curr_pos_dict = player_2_next_position_dict

    if len(player_2_next_position_dict) == 0:
        break

print("Player 1 Win Count = ", player_1_win_cnt)
print("Player 2 Win Count = ", player_2_win_cnt)