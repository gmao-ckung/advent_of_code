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

def find_explosion_or_split(snailfish_string):
    new_sf_string_list = []
    curr_index = 0
    number = ""
    levels = 0
    explosion_found = False
    split_found = False
    while curr_index < len(snailfish_string) and explosion_found == False and split_found == False:
        if snailfish_string[curr_index] == "[":
            new_sf_string_list.append("[")
            levels += 1
        elif snailfish_string[curr_index] == ",":
            if number != "":
                if int(number) > 10:
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
                    # if snailfish_string[curr_index] != ",":
                    #     L_number_in_pair += snailfish_string[curr_index]
                    #     curr_index += 1
                    # else:
                    #     L_number_in_pair = int(L_number_in_pair)
                    #     curr_index += 1
                    #     break

                    if snailfish_string[curr_index] == ",":
                        L_number_in_pair = int(L_number_in_pair)
                        curr_index += 1
                        break
                    elif snailfish_string[curr_index] == "[":
                        levels += 1
                        curr_index += 1
                        new_sf_string_list.append("[")
                    else:
                        L_number_in_pair += snailfish_string[curr_index]
                        curr_index += 1
                
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
                            new_sf_string_list.append(int(number)+R_number_in_pair)
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
                            if int(number) > 10:
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
                            new_sf_string_list.append("]")
                            levels -= 1
                            curr_index += 1
                            number = ""
                            break

    for index in range(curr_index,len(snailfish_string)):
        new_sf_string_list.append(snailfish_string[index])

    print(new_sf_string_list)
    return new_sf_string_list, explosion_found, split_found

def find_explosion_or_split_v2(snailfish_string):
    new_sf_string_list = []
    curr_index = 0
    number = ""
    levels = 0
    explosion_found = False
    split_found = False
    while curr_index < len(snailfish_string) and explosion_found == False and split_found == False:
        if snailfish_string[curr_index] == "[":
            new_sf_string_list.append("[")
            levels += 1
            curr_index += 1
        elif snailfish_string[curr_index] == ",":
            if number != "":
                if int(number) > 10:
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
                if int(number) > 10:
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
            levels -= 1
            curr_index += 1
        else:
            if levels >= 5:
                print("Explosion found?")
                L_number_in_pair = snailfish_string[curr_index]
                curr_index += 1

                # Look at Left entry pair nexted inside (at least) 4 paris
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

                    # Testing this line below
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
                    # new_sf_string_list.append(",")

                    # Advance past ,
                    # curr_index += 1

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

    print(new_sf_string_list)
    return new_sf_string_list, explosion_found, split_found 

while True:
    updated_sf_string_list, explosion_found, split_found = find_explosion_or_split_v2(snailfish_string)

    snailfish_string = ""
    for index in range(len(updated_sf_string_list)):
        if isinstance(updated_sf_string_list[index], int):
            snailfish_string += str(updated_sf_string_list[index])
        else:
            snailfish_string += updated_sf_string_list[index]
    print(snailfish_string)
    if explosion_found == False and split_found == False:
        break



print(snailfish_string)