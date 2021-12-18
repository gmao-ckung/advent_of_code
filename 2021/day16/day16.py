import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day16","r")
hex_codes = fopen.readlines()

def parse_packet_and_type_ID(binary_code, curr_bit):
    packet_version = int(binary_code[curr_bit:curr_bit+3], base=2)
    packet_ID = int(binary_code[curr_bit+3:curr_bit+6],base=2)
    curr_bit += 6
    return packet_version, packet_ID, curr_bit 

def parse_packet_ID_4(binary_code, curr_bit):
    print("Type ID 4 Packet found!")
    bin_value = ""
    bin_value += binary_code[curr_bit+1:curr_bit+5]

    # print(bin_value)
    while (binary_code[curr_bit] == '1'):
        curr_bit += 5
        bin_value += binary_code[curr_bit+1:curr_bit+5]
        
    print("Type 4 packet value (binary) =", bin_value)
    print("Type 4 packet value (dec) =", int(bin_value,base=2))

    curr_bit += 5

    return int(bin_value,base=2), curr_bit

def operator_packet(binary_code, curr_bit, packet_version_sum):
    print("Other packet type ID found")
    length_type = binary_code[curr_bit]
    print("Length type = ", length_type)
    if length_type == '0':
        curr_bit += 1
        total_len_subpackets = int(binary_code[curr_bit:curr_bit+15],base=2)
        curr_bit += 15
        print("Length of Subpackets in bits = ", total_len_subpackets)
        bit_counter = 0
        while(bit_counter < total_len_subpackets):
            packet_version, packet_ID, curr_bit = parse_packet_and_type_ID(binary_code, curr_bit)
            print("Packet Version =", packet_version)
            print("Packet ID =", packet_ID)
            packet_version_sum += packet_version
            bit_counter += 6
            if packet_ID == 4:
                prev_bit = curr_bit
                literal_value, curr_bit = parse_packet_ID_4(binary_code, curr_bit)
                bit_counter += curr_bit-prev_bit
                print("literal value = ", literal_value)
            else:
                prev_bit = curr_bit
                curr_bit, packet_version_sum = operator_packet(binary_code, curr_bit, packet_version_sum)
                bit_counter += curr_bit - prev_bit

        # curr_bit += total_len_subpackets

    elif length_type == '1':
        print("New type")
        curr_bit += 1
        number_of_11_len_subpackets = int(binary_code[curr_bit:curr_bit+11], base=2)
        print("Number of 11 bit subpackets = ", number_of_11_len_subpackets)
        curr_bit += 11
        for i in range(number_of_11_len_subpackets):
            packet_version, packet_ID, curr_bit = parse_packet_and_type_ID(binary_code, curr_bit)
            print("Packet Version =", packet_version)
            print("Packet ID =", packet_ID)
            packet_version_sum += packet_version
            if packet_ID == 4:
                literal_value, curr_bit = parse_packet_ID_4(binary_code, curr_bit)
                print("literal value = ", literal_value)
            else:
                curr_bit, packet_version_sum = operator_packet(binary_code, curr_bit, packet_version_sum)
                
    return curr_bit, packet_version_sum

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
    packet_version, packet_ID, curr_bit = parse_packet_and_type_ID(bin_code, curr_bit)
    print("Packet Version =", packet_version)
    print("Packet Type ID = ", packet_ID)

    packet_version_sum = packet_version

    if packet_ID == 4:
        literal_value, curr_bit = parse_packet_ID_4(bin_code, curr_bit)

    else:
        curr_bit, packet_version_sum = operator_packet(bin_code, curr_bit, packet_version_sum)
                
    print("Version Sum = ", packet_version_sum)