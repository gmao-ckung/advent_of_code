import os
import math
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.test")
data = f1.readlines()

# *** Part 1 ***

field_dict = {}
ticket_dict = {}

YT = False # Flag for "your ticket" info
NT = False # Flag for "nearby tickets" info

ticket_ID = 0
for line in data:
    line=line.replace("\n","")

    if YT:
        your_ticket_numbers = [int(i) for i in line.split(",")]
        ticket_dict[ticket_ID] = your_ticket_numbers
        ticket_ID += 1
        YT = False

    elif NT:
        nearby_ticket_numbers = [int(i) for i in line.split(",")]
        ticket_dict[ticket_ID] = nearby_ticket_numbers
        ticket_ID += 1

    elif line == "your ticket:":
        YT = True
    elif line == "nearby tickets:":
        NT = True
    elif line != "":
        field_s = line.split(" ")
        if(len(field_s) == 4):
            field_type = field_s[0].replace(":","")
            low_0 = int(field_s[1].split("-")[0])
            high_0 = int(field_s[1].split("-")[1])
            low_1 = int(field_s[3].split("-")[0])
            high_1 = int(field_s[3].split("-")[1])
        else:
            field_type = field_s[0] + " " + field_s[1].replace(":","")
            low_0 = int(field_s[2].split("-")[0])
            high_0 = int(field_s[2].split("-")[1])
            low_1 = int(field_s[4].split("-")[0])
            high_1 = int(field_s[4].split("-")[1])
        field_range = [low_0, high_0, low_1, high_1]
        field_dict[field_type] = field_range

invalid_check_dict = {}
for nb_ticket in range(1,len(ticket_dict)):
    nb_ticket_field_values = list(ticket_dict[nb_ticket])
    for value in nb_ticket_field_values:
        valid = False
        for field_name in field_dict:
            if (field_dict[field_name][0] > value) or \
               (field_dict[field_name][1] < value and field_dict[field_name][2] > value) or \
               (field_dict[field_name][3] < value):
                valid |= False
            else:
                valid |= True
                break
    
        if not valid:
            invalid_check_dict[nb_ticket] = value
            break

#print(invalid_check_dict)

error_rate = 0
for i in invalid_check_dict.keys():
    error_rate += invalid_check_dict[i]

print("Ticket Scanning Error Rate =", error_rate)

ticket_to_field_position_match = {}

# *** Looping region to sort out matches to fields for each entry
for nb_ticket in range(1,len(ticket_dict)):
    if nb_ticket not in invalid_check_dict.keys():
        nb_ticket_field_values = list(ticket_dict[nb_ticket])
        occur_list = []
        for value in nb_ticket_field_values:
            location_match_list = []
            for field_name in field_dict:
                if ((field_dict[field_name][0] <= value) and (field_dict[field_name][1] >= value)) or \
                   ((field_dict[field_name][2] <= value) and (field_dict[field_name][3] >= value)):
                   location_match_list.append(field_name)
            #print(location_match_list)
            occur_list.append(location_match_list)
        #print(occur_list)
        ticket_to_field_position_match[nb_ticket] = occur_list

#print(ticket_to_field_position_match)

for field_name in field_dict:
    for ticket in ticket_to_field_position_match.keys():

