import os

# Read input file from current directory
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
file = open(CURR_DIR+"/in.07","r")

equations = file.read().splitlines()

total_sum = 0

for equation in equations:
    print(equation)
    value = int(equation.split(':')[0])
    factors = equation.split(':')[1].split()
    # print(value)
    # print(factors)

    curr_value = value

    if '1' not in factors:
        for i in range(len(factors)-1, 0, -1):
            factor = int(factors[i])

            if value % factor == 0:
                value = value / factor
            else:
                value = value - factor

        if(value == int(factors[0])):
            print('curr_value is value')
            total_sum += curr_value

    else:
        one_count = factors.count('1')
        if one_count > 1:
            print()
        for sub_one in range(one_count+1):
            value = curr_value - sub_one
            print("trying value ", value)
            for i in range(len(factors)-1, 0, -1):
                factor = int(factors[i])

                if value % factor == 0:
                    value = value / factor
                else:
                    value = value - factor
            if(value == int(factors[0])):
                total_sum += curr_value
                print('curr_value is', curr_value,' : sub_one = ', sub_one)
                break



print("Part 1 : Total calibration result = ", total_sum)