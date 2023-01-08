
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
data = open(CURR_DIR+"/input.11","r")

monkeys = {}

monkey_data = data.readline()

def perform_operation(item_value,operation):
    if operation[0] == 'old':
        first_var = item_value
    else:
        first_var = int(operation[0])

    if operation[2] == 'old':
        second_var = item_value
    else:
        second_var = int(operation[2])

    if operation[1] == '+':
        return first_var + second_var
    elif operation[1] == '-':
        return first_var - second_var
    elif operation[1] == '*':
        return first_var * second_var
    elif operation[1] == '/':
        return int(first_var / second_var)

    return 0

while(monkey_data):
    # Get monkey ID
    monkey_data = monkey_data.replace("\n","").replace(":","").replace(",","").split(" ")
    # print(monkey_data)
    id = int(monkey_data[1])
    monkeys[id] = {}

    # Get monkey items
    monkey_data = data.readline()
    monkey_data = monkey_data.replace("\n","").replace(":","").replace(",","").split(" ")

    monkeys[id]['items'] = []
    for i in range(4,len(monkey_data)):
        monkeys[id]['items'].append(int(monkey_data[i]))
    
    # Get monkey operation
    monkey_data = data.readline()
    monkey_data = monkey_data.replace("\n","").replace(":","").replace(",","").split(" ")
    monkeys[id]['op'] = []
    for i in range(5,len(monkey_data)):
        monkeys[id]['op'].append(monkey_data[i])

    # Get test
    monkey_data = data.readline()
    monkey_data = monkey_data.replace("\n","").replace(":","").replace(",","").split(" ")
    monkeys[id]['test'] = int(monkey_data[5])
    
    # Get True/False Data
    monkey_data = data.readline()
    monkey_data = monkey_data.replace("\n","").replace(":","").replace(",","").split(" ")
    monkeys[id]['True'] = int(monkey_data[9])

    monkey_data = data.readline()
    monkey_data = monkey_data.replace("\n","").replace(":","").replace(",","").split(" ")
    monkeys[id]['False'] = int(monkey_data[9])

    monkeys[id]['Number of Inspected Packages'] = 0

    print(monkeys[id])
    # Skip line
    monkey_data = data.readline()
    monkey_data = data.readline()

modulo = 1
for monkey_id in range(len(monkeys)):
    modulo *= monkeys[monkey_id]['test']

for cur_round in range(10000):
    # print('Current Round = ', cur_round)
    for monkey_id in range(len(monkeys)):
        # print('Monkey', monkey_id)
        while(len(monkeys[monkey_id]['items']) > 0):
            inspected_item = monkeys[monkey_id]['items'].pop(0)
            # print('inspected item = ', inspected_item)
            monkeys[monkey_id]['Number of Inspected Packages'] += 1
            worry_level = perform_operation(inspected_item,monkeys[monkey_id]['op'])
            # print('Worry level : ', worry_level)
            # worry_level = int(worry_level / 3)
            worry_level = worry_level % modulo
            # print('Worry level 2 : ', worry_level)
            if worry_level%monkeys[monkey_id]['test'] == 0:
                monkeys[monkeys[monkey_id]['True']]['items'].append(worry_level)
                # print('Throw to monkey ', monkeys[monkey_id]['True'])
            else:
                monkeys[monkeys[monkey_id]['False']]['items'].append(worry_level)
                # print('Throw to monkey ', monkeys[monkey_id]['False'])

        # print("monkey ", monkey_id, ': ', monkeys[monkey_id]['Number of Inspected Packages'])
    # print('****')

monkey_business = []

for id in range(len(monkeys)):
    monkey_business.append(monkeys[id]['Number of Inspected Packages'])
monkey_business.sort(reverse=True)
print('Monkey Business = ', monkey_business[0]*monkey_business[1])