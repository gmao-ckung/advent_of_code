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

def integer_to_base3_list(n, num_digits):
    if n == 0:
        base3 = "0"
    else:
        base3 = ""
        while n > 0:
            base3 = str(n % 3) + base3
            n = n // 3
    # Pad the base3 string with leading zeros to ensure it has num_digits length
    base3 = base3.zfill(num_digits)
    base3_list = [int(digit) for digit in base3]
    return base3_list

total_sum = 0

equations_copy = equations.copy()

for equation in equations:
    value = int(equation.split(':')[0])
    factors = equation.split(':')[1].split()

    for combination in range(2**(len(factors)-1)):
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
            equations_copy.remove(equation)
            break

print("Part 1 : Total calibration result = ", total_sum)

total_number = len(equations_copy)
curr_number = 0

for equation in equations_copy:
    print(curr_number, " of ", total_number)
    curr_number += 1
    value = int(equation.split(':')[0])
    factors = equation.split(':')[1].split()

    for combination in range(3**(len(factors)-1)):
        computation = 0
        base3_operators = integer_to_base3_list(combination,len(factors)-1)
        if 2 in base3_operators:
            for i in range(len(factors)):
                if i == 0:
                    computation = int(factors[i])
                else:
                    operator = base3_operators[i-1]
                    if operator == 0:
                        computation += int(factors[i])
                    elif operator == 1:
                        computation *= int(factors[i])
                    else:
                        computation = int(str(computation)+factors[i])
                
            if computation == value:
                total_sum += value
                break

print("Part 2 : Total calibration result = ", total_sum)