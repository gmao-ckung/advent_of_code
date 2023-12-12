import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/input.test","r")

card_hands = file.read().splitlines()


parsed_hands = {}

# Sort hands into types
for hand_bid in card_hands:
    hand_bid_split = hand_bid.split()

    if hand_bid_split[0] not in parsed_hands:
        parsed_hands[hand_bid_split[0]] = {}
        parsed_hands[hand_bid_split[0]]['bid'] = int(hand_bid_split[1])

for hand in parsed_hands:
    hand_maker = {}
    max_group = 0
    for i in range(len(hand)):
        if hand[i] not in hand_maker:
            hand_maker[hand[i]] = 1
        else:
            hand_maker[hand[i]] += 1
        if hand_maker[hand[i]] > max_group:
            max_group = hand_maker[hand[i]]

    match max_group:
        case 1:
            parsed_hands[hand]['type'] = 0 #'High card'
        case 2:
            if len(hand_maker) == 4:
                parsed_hands[hand]['type'] = 1 #'One pair'
            else:
                parsed_hands[hand]['type'] = 2 #'Two pair'
        case 3:
            if len(hand_maker) == 3:
                parsed_hands[hand]['type'] = 3 # 'Three of a kind'
            else:
                parsed_hands[hand]['type'] = 4 # 'Full house'
        case 4:
            parsed_hands[hand]['type'] = 5 # 'Four of a kind'
        case 5:
            parsed_hands[hand]['type'] = 6 # 'Five of a kind'
        case default:
            parsed_hands[hand]['type'] = 'Something wrong happened'
print(parsed_hands)

sorted_hands = {}

def merge_sort_hands(parsed_hands):

    left_hands = {}
    right_hands = {}

    length_parsed_hands = len(parsed_hands)

    if length_parsed_hands == 1:
        return parsed_hands

    index = 0
    for hand in parsed_hands:
        if(index < length_parsed_hands/2):
            left_hands[hand] = parsed_hands[hand]
            index += 1
        else:
            right_hands[hand] = parsed_hands[hand]
            index += 1
    
    left_hands = merge_sort_hands(left_hands)
    right_hands = merge_sort_hands(right_hands)

    left_keys = [key for key in left_hands]
    right_keys = [key for key in right_hands]

    sorted_hands = {}

    while len(left_keys) > 0 and len(right_keys) > 0:
        if left_hands[left_keys[0]]['type'] > right_hands[right_keys[0]]['type']:
            sorted_hands[right_keys[0]] = right_hands[right_keys[0]]
            right_keys.pop(0)
        else:
            sorted_hands[left_keys[0]] = left_hands[left_keys[0]]
            left_keys.pop(0)

    while len(left_keys) > 0:
        sorted_hands[left_keys[0]] = left_hands[left_keys[0]]
        left_keys.pop(0)

    while len(right_keys) > 0:
        sorted_hands[right_keys[0]] = right_hands[right_keys[0]]
        right_keys.pop(0)

    return sorted_hands

merge_sort_hands(parsed_hands)