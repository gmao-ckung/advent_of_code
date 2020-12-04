f1 = open('/home/ckung/Code/advent_of_code/2015/input.day7')

#class Wire:
    

logic_commands = f1.readlines()

circuit_dictionary = {}
variable_dictionary = {}

for logic_command in logic_commands:
    logic_command = logic_command.replace("\n","")
    logic_command_s = logic_command.split(" ")
    if(len(logic_command_s) == 3):
        if logic_command_s[0][0].isalpha():
            print("***This is a wire***")
            print("Input Variable =", logic_command_s[0])
            print("Output Variable =",logic_command_s[2])
        else:
            print("***This is an input***")
            print("Input Value =", logic_command_s[0])
            print("Output Variable =", logic_command_s[2])

    if(len(logic_command_s) == 4):
        print("***This is a negation***")
        print("Input Variable =", logic_command_s[1])
        print("Output Variable=", logic_command_s[3])

    if len(logic_command_s) == 5:
        print("***This is a logic gate***")
        if logic_command_s[0] > logic_command_s[2]:
            i0 = logic_command_s[2]
            i1 = logic_command_s[0]
        else:
            i0 = logic_command_s[0]
            i1 = logic_command_s[2]
        print(i0,"and",i1, "are the inputs")
        logic_gate_input = i0 + " and " + i1
        print(logic_gate_input)
        print(logic_command_s[4],"is the output")

    print(logic_command)
