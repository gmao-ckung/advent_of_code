import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/input.in","r")

# Read lines within input file and remove new line character at the line's end
card_pile = file.read().splitlines()

card_number = 0
points = 0
total_num_scratchcards = 0

card_dictionary = {}

for cardNum in range(len(card_pile)):
    # For each card, first number is number of cards, and second number is number of winning numbers
    card_dictionary[cardNum+1] = [1, 0]

# Parse data from each card
for card in card_pile:
    card_number += 1
    card_data = card.split(": ")[1].split(" | ")

    # Extract winning numbers and our numbers
    winning_numbers = card_data[0].split()
    our_numbers = card_data[1].split()
    
    num_of_winners = 0

    # Go through winning numbers and match to our numbers
    for number in winning_numbers:
        if number in our_numbers:
            num_of_winners += 1

    if num_of_winners > 0:
        points += 2**(num_of_winners-1)

    card_dictionary[card_number][1] = num_of_winners

    # Add in number of winning numbers towards card count of "future" cards
    for future_card in range(card_number+1, card_number+1+num_of_winners):
        if future_card in card_dictionary:
            card_dictionary[future_card][0] += card_dictionary[card_number][0]

    total_num_scratchcards += card_dictionary[card_number][0]

print("Part 1 : Cards are worth", points, "points")
print("Part 2 : Total number of scratchcards =", total_num_scratchcards)