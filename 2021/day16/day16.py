import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.test","r")
hex_codes = fopen.readlines()

for hex_code in hex_codes:
    hex_code = hex_code.replace("\n", "")
    print("Hex Code = ", hex_code)
    bin_code = str(bin(int(hex_code, base=16)))[2:]
    if len(bin_code)%4 != 0:
        if len(bin_code)%4 == 1:
            bin_code = "000"+bin_code
        elif len(bin_code)%4 == 2:
            bin_code = "00"+bin_code
        elif len(bin_code)%4 == 3:
            bin_code = "0"+bin_code

    curr_bit = 0
    # while len(bin_code) > curr_bit:
    print("Binary Code = ", bin_code)
    packet_version = int(bin_code[0:3], base=2)
    print("Packet Version = ", packet_version)
    packet_type = int(bin_code[3:6],base=2)
    print("Packet Type ID = ", packet_type)

    curr_bit += 6

    if packet_type == 4:
        print("Type ID 4 Packet found!")
        bin_value = ""
        bin_value += bin_code[curr_bit+1:curr_bit+5]

        print(bin_value)
        while (bin_code[curr_bit] == '1'):
            curr_bit += 5
            bin_value += bin_code[curr_bit+1:curr_bit+5]
            
        print("Type 4 packet value (binary) =", bin_value)
        print("Type 4 packet value (dec) =", int(bin_value,base=2))

        curr_bit += 5

        
    else:
        print("Other packet type ID found = ", packet_type)
        length_type = bin_code[curr_bit]
        print("Length type = ", length_type)
        if length_type == '0':
            curr_bit += 1
            total_len_subpackets = int(bin_code[curr_bit:curr_bit+15],base=2)
            curr_bit += 15
            print("Length of Subpackets in bits = ", total_len_subpackets)

            curr_bit += total_len_subpackets

        elif length_type == '1':
            print("New type")
            curr_bit += 1
            number_of_11_len_subpackets = int(bin_code[curr_bit:curr_bit+11], base=2)
            print("Number of 11 bit subpackets = ", number_of_11_len_subpackets)
            curr_bit += 11*(number_of_11_len_subpackets+1)
                
    print("Length of bit code = ", len(bin_code))
    print("curr_bit = ", curr_bit)