import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.07","r")

equations = file.read().splitlines()

def integer_to_binary_list(n, num_digits):
    # Convert integer to binary string
    binary_str = bin(n)[2:]
    # Pad the binary string with leading zeros to ensure it has num_digits length
    binary_str = binary_str.zfill(num_digits)
    # Convert binary string to list of digits
    binary_list = [int(digit) for digit in binary_str]
    return binary_list

total_sum = 0

for equation in equations:
    print(equation)
    value = int(equation.split(':')[0])
    factors = equation.split(':')[1].split()
    # print(value)
    # print(factors)

    curr_value = value

    for combination in range(2**len(factors)):
        computation = 0
        binary_operators = integer_to_binary_list(combination,len(factors)-1)
        for i in range(len(factors)):
            if i == 0:
                computation = int(factors[i])
            else:
                operator = binary_operators[i-1]
                if operator == 0:
                    computation += int(factors[i])
                else:
                    computation *= int(factors[i])
            
        if computation == value:
            total_sum += value
            break

print("Part 1 : Total calibration result = ", total_sum)