import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")
snailfishes = fopen.readlines()

# Sum up initial snailfishes into a string
snailfish_string = ""
for snailfish in snailfishes:
    snailfish = snailfish.replace("\n","")
    if snailfish_string == "":
        snailfish_string += snailfish
    else:
        snailfish_string = "[" + snailfish_string + "," + snailfish + "]"

print(snailfish_string)

def find_explosion(snailfish_string):
    new_sf_string_list = []
    curr_index = 0
    number = ""
    levels = 0
    explosion_found = False
    while curr_index < len(snailfish_string) and explosion_found == False:
        if snailfish_string[curr_index] == "[":
            new_sf_string_list.append("[")
            levels += 1
        elif snailfish_string[curr_index] == ",":
            if number != "":
                new_sf_string_list.append(int(number))
                number = ""
            new_sf_string_list.append(",")
        elif snailfish_string[curr_index] == "]":
            if number != "":
                new_sf_string_list.append(int(number))
                number = ""
            new_sf_string_list.append("]")
            levels -= 1
        else:
            number += snailfish_string[curr_index]
        curr_index += 1

        if levels == 4:
            print("Explosion found?")

            if snailfish_string[curr_index] == "[": # Left entry is a pair
                explosion_found = True
                curr_index += 1
                L_number_in_pair = ""
                R_number_in_pair = ""
                while(True):
                    if snailfish_string[curr_index] != ",":
                        L_number_in_pair += snailfish_string[curr_index]
                        curr_index += 1
                    else:
                        L_number_in_pair = int(L_number_in_pair)
                        curr_index += 1
                        break
                
                while(True):
                    if snailfish_string[curr_index] != "]":
                        R_number_in_pair += snailfish_string[curr_index]
                        curr_index += 1
                    else:
                        R_number_in_pair = int(R_number_in_pair)
                        curr_index += 1
                        break

                curr_index += 1 # Advance past comma

                # Look leftward to see whether there is a number to add from the explosion
                for index in range(len(new_sf_string_list)-1,-1,-1):
                    if isinstance(new_sf_string_list[index], int):
                        new_sf_string_list[index] += L_number_in_pair
                        break

                # Look at right entry
                if snailfish_string[curr_index] == "[": # The right entry also has a pair
                    new_sf_string_list.append(0)
                    new_sf_string_list.append(",")
                    new_sf_string_list.append("[")
                    curr_index += 1
                    
                    number = ""
                    while(True):
                        if snailfish_string[curr_index] != ",":
                            number += snailfish_string[curr_index]
                            curr_index += 1
                        else:
                            new_sf_string_list.append(int(number))
                            new_sf_string_list.append(",")
                            curr_index += 1
                            break
                    

                else:
                    R_number = ""
                    while(True):
                        if snailfish_string[curr_index] != "]":
                            R_number += snailfish_string[curr_index]
                            curr_index += 1
                        else:
                            new_sf_string_list.append(0)
                            new_sf_string_list.append(",")
                            new_sf_string_list.append(int(R_number) + R_number_in_pair)
                            new_sf_string_list.append("]")
                            curr_index += 1
                            break
            elif snailfish_string[curr_index] != "]": # Left entry is a number
                number = ""
                while(True):
                    if snailfish_string[curr_index] != ",":
                        number += snailfish_string[curr_index]
                        curr_index += 1
                    else:
                        new_sf_string_list.append(int(number))
                        new_sf_string_list.append(",")
                        number = ""
                        curr_index += 1
                        break
                # Look at right entry
                if snailfish_string[curr_index] == "[": # The right entry is a pair
                    explosion_found = True
                    curr_index += 1
                    L_number_in_pair = ""
                    R_number_in_pair = ""
                    while(True):
                        if snailfish_string[curr_index] != ",":
                            L_number_in_pair += snailfish_string[curr_index]
                            curr_index += 1
                        else:
                            L_number_in_pair = int(L_number_in_pair)
                            curr_index += 1
                            break

                    for index in range(len(new_sf_string_list)-1,-1,-1):
                        if isinstance(new_sf_string_list[index], int):
                            new_sf_string_list[index] += L_number_in_pair
                            break

                    new_sf_string_list.append(0)
                    
                    while(True):
                        if snailfish_string[curr_index] != "]":
                            R_number_in_pair += snailfish_string[curr_index]
                            curr_index += 1
                        else:
                            R_number_in_pair = int(R_number_in_pair)
                            curr_index += 1
                            break

                    number = ""
                    number_found = False
                    while(curr_index < len(snailfish_string)):
                        if snailfish_string[curr_index] == "]":
                            if number_found == True:
                                new_sf_string_list.append(int(number) + R_number_in_pair)
                                new_sf_string_list.append("]")
                                curr_index += 1
                                break
                            new_sf_string_list.append("]")
                        elif snailfish_string[curr_index] == "[":
                            if number_found == True:
                                new_sf_string_list.append(int(number) + R_number_in_pair)
                                new_sf_string_list.append("[")
                                curr_index += 1
                                break
                            new_sf_string_list.append("[")
                        elif snailfish_string[curr_index] == ",":
                            if number_found == True:
                                new_sf_string_list.append(int(number) + R_number_in_pair)
                                new_sf_string_list.append(",")
                                curr_index += 1
                                break
                            new_sf_string_list.append(",")
                        else:
                            number_found = True
                            number += snailfish_string[curr_index]
                        
                        curr_index += 1

                else:
                    # This is for a potentially detected explosion within four nested pair, but we find
                    # that the two nested parts are both numbers
                    number = ""
                    while(True):
                        if snailfish_string[curr_index] != "]":
                            number += snailfish_string[curr_index]
                            curr_index += 1
                        else:
                            new_sf_string_list.append(int(number))
                            new_sf_string_list.append("]")
                            levels -= 1
                            curr_index += 1
                            number = ""
                            break

    for index in range(curr_index,len(snailfish_string)):
        new_sf_string_list.append(snailfish_string[index])

    print(new_sf_string_list)
    return new_sf_string_list

updated_sf_string_list = find_explosion(snailfish_string)

snailfish_string = ""
for index in range(len(updated_sf_string_list)):
    if isinstance(updated_sf_string_list[index], int):
        snailfish_string += str(updated_sf_string_list[index])
    else:
        snailfish_string += updated_sf_string_list[index]

print(snailfish_string)