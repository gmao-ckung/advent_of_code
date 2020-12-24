import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)
f1 = open(CURR_DIR+"/input.day18")
expressions = f1.readlines()

def compute_expression(start_position, expression):
    result = 0
    curr_position = start_position

    while(curr_position < len(expression)):
        if(start_position == curr_position):
            if expression[curr_position] != '(':
                result += int(expression[curr_position])
                curr_position += 1
            else:
                curr_position += 1
                result, curr_position = compute_expression(curr_position,expression)
                if(curr_position >= len(expression)):
                    break
        if expression[curr_position] == ')':
            curr_position += 1
            return result, curr_position
        operator = expression[curr_position]
        curr_position += 1
        if operator == '+':
            if expression[curr_position] != '(':
                result += int(expression[curr_position])
                curr_position += 1
            else:
                curr_position += 1
                p_result, curr_position = compute_expression(curr_position,expression)
                result += p_result
        elif operator == '-':
            if expression[curr_position] != '(':
                result -= int(expression[curr_position])
                curr_position += 1
            else:
                curr_position += 1
                p_result, curr_position = compute_expression(curr_position,expression)
                result -= p_result
        elif operator == "*":
            if expression[curr_position] != '(':
                result *= int(expression[curr_position])
                curr_position += 1
            else:
                curr_position += 1
                p_result, curr_position = compute_expression(curr_position,expression)
                result *= p_result
        
    return result, curr_position
        
def find_plus_paranthesis(curr_position, expression, pal_list):
    while(curr_position < len(expression)):
        if expression[curr_position] == '(':
            L_P_position = curr_position             
            curr_position += 1
            pal_list, curr_position = find_plus_paranthesis(curr_position,expression,pal_list)
        elif expression[curr_position] == ')':
            curr_position += 1
            return pal_list, curr_position
        elif expression[curr_position] == '+':
            curr_position += 1
            if expression[curr_position] != '(':
                pal_list.append(L_P_position)
                pal_list.append(curr_position)
                curr_position += 1
            else:
                curr_position += 1
                pal_list.append(L_P_position)
                p_result, curr_position = find_plus_paranthesis(curr_position,expression,pal_list)
                pal_list.append(curr_position-1)              
        elif expression[curr_position] == '-':
            curr_position += 1
            if expression[curr_position] != '(':
                L_P_position = curr_position
                curr_position += 1
            else:
                L_P_position = curr_position
                curr_position += 1
                pal_list, curr_position = find_plus_paranthesis(curr_position,expression,pal_list) 
        elif expression[curr_position] == "*":
            curr_position += 1
            if expression[curr_position] != '(':
                L_P_position = curr_position
                curr_position += 1
            else:
                L_P_position = curr_position
                curr_position += 1
                pal_list, curr_position = find_plus_paranthesis(curr_position,expression,pal_list)
        else:
            L_P_position = curr_position
            curr_position += 1
        
    return pal_list, curr_position

def append_paranthesis(expression, list_of_paranthesis):
    new_equation = []
    type_par = 'R'
    pal_index = len(list_of_paranthesis) - 1
    for i in range(len(expression)-1,-1,-1):
        #print(expression[i])
        if list_of_paranthesis[pal_index] == i:
            #print(type_par)
            if type_par == 'L':
                new_equation.append(expression[i])
                new_equation.append('(')
                type_par = 'R'
            else:
                new_equation.append(')')
                new_equation.append(expression[i])
                type_par = 'L'
            pal_index -= 1
        else:
            new_equation.append(expression[i])

    new_equation.reverse()

    return new_equation

# *** Part 1 ***

total_sum = 0

for expression in expressions:
    expression = expression.replace("\n","")
    expression = expression.replace(" ","")
    print(expression)
    curr_position = 0
    while(curr_position < len(expression)):
        result, curr_position = compute_expression(curr_position, expression)
        total_sum += result

print("Part 1: Sum of resulting expressions =", total_sum)

# # *** Part 2 ***

# total_sum = 0

# for expression in expressions:
#     expression = expression.replace("\n","")
#     expression = expression.replace(" ","")
#     print(expression)
#     curr_position = 0
#     paranthesis_add_locations_list = []
#     while(curr_position < len(expression)):
#         paranthesis_add_locations_list, curr_position = find_plus_paranthesis(curr_position, expression, \
#                                                                               paranthesis_add_locations_list)
#     print(paranthesis_add_locations_list)
#     new_equation = append_paranthesis(expression, paranthesis_add_locations_list)
#     result, curr_position = compute_expression(0,new_equation)
#     print('Sum =', result)