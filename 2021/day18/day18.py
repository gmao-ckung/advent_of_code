import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day18","r")
snailfishes = fopen.readlines()

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
            curr_index += 1
        elif snailfish_string[curr_index] == ",":
            if number != "":
                new_sf_string_list.append(int(number))
                number = ""
            new_sf_string_list.append(",")
            curr_index += 1
        elif snailfish_string[curr_index] == "]":
            if number != "":              
                new_sf_string_list.append(int(number))
                number = ""
            new_sf_string_list.append("]")
            levels -= 1
            curr_index += 1
        else:
            if levels >= 5:
                L_number_in_pair = snailfish_string[curr_index]
                curr_index += 1
                # Look at Left entry pair nested inside (at least) 4 pairs
                while(True):
                    if snailfish_string[curr_index] == ",":
                        L_number_in_pair = int(L_number_in_pair)
                        curr_index += 1
                        break
                    else:
                        L_number_in_pair += snailfish_string[curr_index]
                        curr_index += 1

                # Look at right entry
                if snailfish_string[curr_index] == "[": # The right entry is a pair
                    explosion_found = True
                    new_sf_string_list.append(L_number_in_pair)
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

                    new_sf_string_list.append(",")
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
                    R_number_in_pair = ""
                    while(True):
                        if snailfish_string[curr_index] != "]":
                            R_number_in_pair += snailfish_string[curr_index]
                            curr_index += 1
                        else:
                            R_number_in_pair = int(R_number_in_pair)
                            # Advance past ]
                            curr_index += 1
                            break

                    # Get rid of extraneous [
                    new_sf_string_list.pop()

                    for index in range(len(new_sf_string_list)-1,-1,-1):
                        if isinstance(new_sf_string_list[index], int):
                            new_sf_string_list[index] += L_number_in_pair
                            break

                    new_sf_string_list.append(0)

                    number = ""
                    number_found = False
                    explosion_found = True
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

                    levels -= 1
                    number = ""
                    break
                    
            else:
                number += snailfish_string[curr_index]
                curr_index += 1
        
    for index in range(curr_index,len(snailfish_string)):
        new_sf_string_list.append(snailfish_string[index])

    return new_sf_string_list, explosion_found

def find_split(snailfish_string):
    new_sf_string_list = []
    curr_index = 0
    number = ""
    split_found = False
    while curr_index < len(snailfish_string) and split_found == False:
        if snailfish_string[curr_index] == "[":
            new_sf_string_list.append("[")
            curr_index += 1
        elif snailfish_string[curr_index] == ",":
            if number != "":
                if int(number) >= 10:
                    split_found = True
                    number = int(number)
                    L_number = int(number/2)
                    R_number = int(number/2) + number%2
                    new_sf_string_list.append("[")
                    new_sf_string_list.append(L_number)
                    new_sf_string_list.append(",")
                    new_sf_string_list.append(R_number)
                    new_sf_string_list.append("]")
                else:
                    new_sf_string_list.append(int(number))
                number = ""
            new_sf_string_list.append(",")
            curr_index += 1
        elif snailfish_string[curr_index] == "]":
            if number != "":              
                if int(number) >= 10:
                    split_found = True
                    number = int(number)
                    L_number = int(number/2)
                    R_number = int(number/2) + number%2
                    new_sf_string_list.append("[")
                    new_sf_string_list.append(L_number)
                    new_sf_string_list.append(",")
                    new_sf_string_list.append(R_number)
                    new_sf_string_list.append("]")
                else:
                    new_sf_string_list.append(int(number))
                number = ""
            new_sf_string_list.append("]")
            curr_index += 1
        else:
            number += snailfish_string[curr_index]
            curr_index += 1 

    for index in range(curr_index,len(snailfish_string)):
        new_sf_string_list.append(snailfish_string[index])

    return new_sf_string_list, split_found

def magnitude_compute(snailfish_string, curr_index):
    number = ""
    while curr_index < len(snailfish_string):
        if snailfish_string[curr_index] == "[":            
            curr_index += 1
            number, curr_index = magnitude_compute(snailfish_string, curr_index)            
        elif snailfish_string[curr_index] == ",":
            L_number = 3*int(number)
            curr_index += 1
            number = ""
        elif snailfish_string[curr_index] == "]":
            R_number = 2*int(number)
            curr_index += 1
            return L_number + R_number, curr_index
        else:
            number += snailfish_string[curr_index]
            curr_index += 1

    return number, curr_index

def reduce_snailfish_sum(snailfish_string):
    while True:
        updated_sf_string_list, explosion_found = find_explosion(snailfish_string)

        snailfish_string = ""
        for index in range(len(updated_sf_string_list)):
            if isinstance(updated_sf_string_list[index], int):
                snailfish_string += str(updated_sf_string_list[index])
            else:
                snailfish_string += updated_sf_string_list[index]

        if explosion_found == True:
            continue

        updated_sf_string_list, split_found = find_split(snailfish_string)

        snailfish_string = ""
        for index in range(len(updated_sf_string_list)):
            if isinstance(updated_sf_string_list[index], int):
                snailfish_string += str(updated_sf_string_list[index])
            else:
                snailfish_string += updated_sf_string_list[index]

        if explosion_found == False and split_found == False:
            break

    return snailfish_string

snailfish_string = ""
for snailfish in snailfishes:
    snailfish = snailfish.replace("\n","")
    if snailfish_string == "":
        snailfish_string += snailfish
    else:
        snailfish_string = "[" + snailfish_string + "," + snailfish + "]"

    snailfish_string = reduce_snailfish_sum(snailfish_string)

magnitude, curr_index = magnitude_compute(snailfish_string,0)
print("Part 1 : Magnitude = ", magnitude)

snailfish_list = []
for snailfish in snailfishes:
    snailfish = snailfish.replace("\n","")
    snailfish_list.append(snailfish)

max_mag = 0
for i in range(len(snailfish_list)):
    for j in range(i+1,len(snailfish_list)):
        snailfish_x = snailfish_list[i]
        snailfish_y = snailfish_list[j]

        add1 = "[" + snailfish_x + "," + snailfish_y + "]"
        add2 = "[" + snailfish_y + "," + snailfish_x + "]"

        add1 = reduce_snailfish_sum(add1)
        add2 = reduce_snailfish_sum(add2)

        magnitude1, curr_index = magnitude_compute(add1, 0)
        magnitude2, curr_index = magnitude_compute(add2, 0)

        if magnitude1 > max_mag:
            max_mag = magnitude1

        if magnitude2 > max_mag:
            max_mag = magnitude2

print("Part 2 : Largest Magnitude =", max_mag)