import os
import numpy as np

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

possible_roll_results = [3, 4, 5, 6, 7, 8, 9]

def score_player_1(possible_roll_results, player_1_pos, player_1_score, player_1_win_cnt, player_2_pos, player_2_score, player_2_win_cnt, scale_factor):
    for i in range(len(possible_roll_results)):
        player_1_pos_next = player_1_pos + possible_roll_results[i]
        player_1_pos_next = check_pos(player_1_pos_next,10)

        player_1_score_next = player_1_score + player_1_pos_next
        print("Player 1 Current Position =", player_1_pos)
        print("Player 1 rolled number =", possible_roll_results[i])
        print("Player 1 Next Position =", player_1_pos_next)
        print("Player 1 Score =", player_1_score_next)
        print("Currrent Scale Factor =", scale_factor)
        if player_1_score_next >= 21:
            if possible_roll_results[i] == 3 or possible_roll_results[i] == 9:
                player_1_win_cnt += 1 * scale_factor
            elif possible_roll_results[i] == 4 or possible_roll_results[i] == 8:
                player_1_win_cnt += 3 * scale_factor
            elif possible_roll_results[i] == 5 or possible_roll_results[i] == 7:
                player_1_win_cnt += 6 * scale_factor
            elif possible_roll_results[i] == 6:
                player_1_win_cnt += 6 * scale_factor
           
        else:
            if possible_roll_results[i] == 3 or possible_roll_results[i] == 9:
                next_scale_factor = 1 * scale_factor
            elif possible_roll_results[i] == 4 or possible_roll_results[i] == 8:
                next_scale_factor = 3 * scale_factor
            elif possible_roll_results[i] == 5 or possible_roll_results[i] == 7:
                next_scale_factor = 6 * scale_factor
            elif possible_roll_results[i] == 6:
                next_scale_factor = 7 * scale_factor
            player_1_win_cnt, player_2_win_cnt = score_player_2(possible_roll_results, 
                                                                player_1_pos_next, player_1_score_next, player_1_win_cnt, 
                                                                player_2_pos, player_2_score, player_2_win_cnt,
                                                                next_scale_factor)

    return player_1_win_cnt, player_2_win_cnt

def score_player_2(possible_roll_results, player_1_pos, player_1_score, player_1_win_cnt, player_2_pos, player_2_score, player_2_win_cnt, scale_factor):
    for i in range(len(possible_roll_results)):
        player_2_pos_next = player_2_pos + possible_roll_results[i]
        player_2_pos_next = check_pos(player_2_pos_next,10)

        player_2_score_next = player_2_score + player_2_pos_next
        print("Player 2 Current Position =", player_2_pos)
        print("Player 2 rolled number =", possible_roll_results[i])
        print("Player 2 Next Position =", player_2_pos_next)        
        print("Player 2 Score =", player_2_score_next)
        print("Currrent Scale Factor =", scale_factor)
        if player_2_score_next >= 21:
            if possible_roll_results[i] == 3 or possible_roll_results[i] == 9:
                player_2_win_cnt += 1 * scale_factor
            elif possible_roll_results[i] == 4 or possible_roll_results[i] == 8:
                player_2_win_cnt += 3 * scale_factor
            elif possible_roll_results[i] == 5 or possible_roll_results[i] == 7:
                player_2_win_cnt += 6 * scale_factor
            elif possible_roll_results[i] == 6:
                player_2_win_cnt += 7 * scale_factor
        else:
            if possible_roll_results[i] == 3 or possible_roll_results[i] == 9:
                next_scale_factor = 1 * scale_factor
            elif possible_roll_results[i] == 4 or possible_roll_results[i] == 8:
                next_scale_factor = 3 * scale_factor
            elif possible_roll_results[i] == 5 or possible_roll_results[i] == 7:
                next_scale_factor = 6 * scale_factor
            elif possible_roll_results[i] == 6:
                next_scale_factor = 7 * scale_factor
            player_1_win_cnt, player_2_win_cnt = score_player_1(possible_roll_results, 
                                                                player_1_pos, player_1_score, player_1_win_cnt, 
                                                                player_2_pos_next, player_2_score_next, player_2_win_cnt,
                                                                next_scale_factor)

    return player_1_win_cnt, player_2_win_cnt

# Frequency of roll results if die is rolled 3 times
# 3 -> 1 time
# 4 -> 3 times
# 5 -> 6 times
# 6 -> 7 times
# 7 -> 6 times
# 8 -> 3 times
# 9 -> 1 time
player_1_pos = int(start_positions[0].split(" ")[-1].replace("\n", ""))
player_2_pos = int(start_positions[1].split(" ")[-1].replace("\n", ""))

player_1_win_cnt = 0
player_1_score = 0
player_2_win_cnt = 0
player_2_score = 0

# player_1_win_cnt, player_2_win_cnt = score_player_1(possible_roll_results, player_1_pos, player_1_score, player_1_win_cnt, player_2_pos, player_2_score, player_2_win_cnt, 1)

player_1_pos_list = [player_1_pos] * 7
player_1_score_list = [0] * 7
player_2_pos_list = [player_2_pos] * 7
player_2_score_list = [0] * 7
scale_factor_const = [1, 3, 6, 7, 6, 3, 1]
scale_factor_list = [1] * 7
while True:
    for i in range(len(possible_roll_results)):
        player_1_pos_list[i] += possible_roll_results[i]
        player_1_pos_list[i] = check_pos(player_1_pos_list[i],10)
        player_1_score_list[i] += player_1_pos_list[i]
        if player_1_score_list[i] >= 21:
            
    print(player_1_score_list)

print("Player 1 Win Count = ", player_1_win_cnt)
print("Player 2 Win Count = ", player_2_win_cnt)