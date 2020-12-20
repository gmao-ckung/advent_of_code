import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.test")
expressions = f1.readlines()

def compute_expression(start_position, expression):
    result = 0
    curr_position = start_position

    while(curr_position < len(expression)):
        if(start_position == curr_position):
            result += int(expression[curr_position])
            curr_position += 1
        if expression[curr_position] == ')':
            return result, curr_position
        operator = expression[curr_position]
        curr_position += 1
        if operator == '+':
            if expression[curr_position] != '(':
                result += int(expression[curr_position])
            else:
                curr_position += 1
                p_result, curr_position = compute_expression(curr_position,expression)
                result += p_result
        elif operator == '-':
            if expression[curr_position] != '(':
                result -= int(expression[curr_position])
            else:
                curr_position += 1
                p_result, curr_position = compute_expression(curr_position,expression)
                result -= p_result
        elif operator == "*":
            if expression[curr_position] != '(':
                result *= int(expression[curr_position])
            else:
                curr_position += 1
                p_result, curr_position = compute_expression(curr_position,expression)
                result *= p_result
        curr_position += 1

    return result, curr_position
        
total_sum = 0

for expression in expressions:
    expression = expression.replace(" ","")
    print(expression)
    curr_position = 0
    while(curr_position < len(expression)):
        result, curr_position = compute_expression(curr_position, expression)
        total_sum += result

print("Sum of resulting expressions =", total_sum)