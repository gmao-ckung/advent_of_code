import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day21","r")
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