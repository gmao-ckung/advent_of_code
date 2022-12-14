
import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
data = open(CURR_DIR+"/input.test","r")

monkeys = {}

monkey_data = data.readline()

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

    print(monkeys[id])
    # Skip line
    monkey_data = data.readline()
    monkey_data = data.readline()