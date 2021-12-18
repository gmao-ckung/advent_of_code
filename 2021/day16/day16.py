import os

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.day16","r")
hex_codes = fopen.readlines()

def generate_binary_code(hex_code):
    binary_code = ""
    for i in range(len(hex_code)):
        bin_code_part = str(bin(int(hex_code[i], base=16)))[2:]
        if len(bin_code_part)%4 != 0:
            if len(bin_code_part)%4 == 1:
                bin_code_part = "000"+bin_code_part
            elif len(bin_code_part)%4 == 2:
                bin_code_part = "00"+bin_code_part
            elif len(bin_code_part)%4 == 3:
                bin_code_part = "0"+bin_code_part
        binary_code += bin_code_part
    return binary_code

def parse_packet_and_type_ID(binary_code, curr_bit):
    packet_version = int(binary_code[curr_bit:curr_bit+3], base=2)
    packet_ID = int(binary_code[curr_bit+3:curr_bit+6],base=2)
    curr_bit += 6
    return packet_version, packet_ID, curr_bit 

def parse_packet_ID_4(binary_code, curr_bit):
    bin_value = ""
    bin_value += binary_code[curr_bit+1:curr_bit+5]

    while (binary_code[curr_bit] == '1'):
        curr_bit += 5
        bin_value += binary_code[curr_bit+1:curr_bit+5]
        
    print("Type 4 packet value (binary) =", bin_value)
    print("Type 4 packet value (dec) =", int(bin_value,base=2))

    curr_bit += 5

    return int(bin_value,base=2), curr_bit

def operator_packet(binary_code, curr_bit, packet_version_sum, operators, packet_literals):
    print("Operator packet type found")
    length_type = binary_code[curr_bit]
    print("Length type = ", length_type)
    if length_type == '0':
        curr_bit += 1
        total_len_subpackets = int(binary_code[curr_bit:curr_bit+15],base=2)
        curr_bit += 15
        print("Length of Subpackets in bits = ", total_len_subpackets)
        bit_counter = 0
        new_packet_literals = []
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
                new_packet_literals.append(literal_value)
                print("literal value = ", literal_value)
            else:
                operators.append(packet_ID)
                prev_bit = curr_bit
                curr_bit, packet_version_sum, new_packet_literals = operator_packet(binary_code, curr_bit, packet_version_sum, operators, new_packet_literals)
                bit_counter += curr_bit - prev_bit
        # curr_bit += total_len_subpackets

    elif length_type == '1':
        curr_bit += 1
        number_of_11_len_subpackets = int(binary_code[curr_bit:curr_bit+11], base=2)
        print("Number of 11 bit subpackets = ", number_of_11_len_subpackets)
        curr_bit += 11
        new_packet_literals = []
        for i in range(number_of_11_len_subpackets):
            packet_version, packet_ID, curr_bit = parse_packet_and_type_ID(binary_code, curr_bit)
            print("Packet Version =", packet_version)
            print("Packet ID =", packet_ID)
            packet_version_sum += packet_version
            if packet_ID == 4:
                literal_value, curr_bit = parse_packet_ID_4(binary_code, curr_bit)
                print("literal value = ", literal_value)
                new_packet_literals.append(literal_value)
            else:
                operators.append(packet_ID)
                curr_bit, packet_version_sum, new_packet_literals = operator_packet(binary_code, curr_bit, packet_version_sum, operators, new_packet_literals)
    
    curr_operation = operators.pop()

    if curr_operation == 0:
        packet_literals.append(sum(new_packet_literals))
        
    elif curr_operation == 1:
        mult_tot = 1
        for i in range(len(new_packet_literals)):
            mult_tot *= new_packet_literals[i]
        packet_literals.append(mult_tot)
    elif curr_operation == 2:
       packet_literals.append(min(new_packet_literals))
    elif curr_operation == 3:
        packet_literals.append(max(new_packet_literals))
    elif curr_operation == 5:
        if new_packet_literals[0] > new_packet_literals[1]:
            packet_literals.append(1)
        else:
            packet_literals.append(0)
    elif curr_operation == 6:
        if new_packet_literals[0] < new_packet_literals[1]:
            packet_literals.append(1)
        else:
            packet_literals.append(0)
    elif curr_operation == 7:
        if new_packet_literals[0] == new_packet_literals[1]:
            packet_literals.append(1)
        else:
            packet_literals.append(0)

    return curr_bit, packet_version_sum, packet_literals

for hex_code in hex_codes:
    hex_code = hex_code.replace("\n", "")
    print("Hex Code = ", hex_code)
    bin_code = generate_binary_code(hex_code)

    curr_bit = 0
    operators = []
    print("Binary Code = ", bin_code)
    packet_version, packet_ID, curr_bit = parse_packet_and_type_ID(bin_code, curr_bit)
    print("Packet Version =", packet_version)
    print("Packet Type ID = ", packet_ID)

    packet_version_sum = packet_version
    packet_literals = []
    
    if packet_ID == 4:
        literal_value, curr_bit = parse_packet_ID_4(bin_code, curr_bit)

    else:
        operators.append(packet_ID)
        curr_bit, packet_version_sum, packet_literals = operator_packet(bin_code, curr_bit, packet_version_sum, operators, packet_literals)
                
    print("Version Sum = ", packet_version_sum)
    print("Value = ", packet_literals[0])