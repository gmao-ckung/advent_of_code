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
                pal_list.append([L_P_position,'L'])
                pal_list.append([curr_position,'R'])
                curr_position += 1
            else:
                curr_position += 1
                pal_list.append([L_P_position,'L'])
                p_result, curr_position = find_plus_paranthesis(curr_position,expression,pal_list)
                pal_list.append([curr_position-1,'R'])
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

    list_of_paranthesis.sort()
    list_of_paranthesis.reverse()
    #print(list_of_paranthesis)

    for add_paran in list_of_paranthesis:
        #print(add_paran)
        p_type = add_paran[1]
        p_location = add_paran[0]
        if p_type == 'R':
            expression = expression[:p_location+1] + ')' + expression[p_location+1:]
        elif p_type == 'L':
            expression = expression[:p_location] + '(' + expression[p_location:]
    #print(expression)
    return expression

# *** Part 1 ***

total_sum = 0

for expression in expressions:
    expression = expression.replace("\n","")
    expression = expression.replace(" ","")
    #print(expression)
    curr_position = 0
    while(curr_position < len(expression)):
        result, curr_position = compute_expression(curr_position, expression)
        total_sum += result

print("Part 1: Sum of resulting expressions =", total_sum)

# # *** Part 2 ***

total_sum = 0

for expression in expressions:
    expression = expression.replace("\n","")
    expression = expression.replace(" ","")
    #print(expression)
    curr_position = 0
    paranthesis_add_locations_list = []
    while(curr_position < len(expression)):
        paranthesis_add_locations_list, curr_position = find_plus_paranthesis(curr_position, expression, \
                                                                              paranthesis_add_locations_list)
    #print(paranthesis_add_locations_list)
    new_equation = append_paranthesis(expression, paranthesis_add_locations_list)
    result, curr_position = compute_expression(0,new_equation)
    #print('Sum =', result)
    total_sum += result

print("Part 2: Sum of resulting expressions =", total_sum)