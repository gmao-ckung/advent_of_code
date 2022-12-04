import os
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
fopen = open(CURR_DIR+"/input.04","r")

assignments = fopen.readlines()

pairs_1 = 0
pairs_2 = 0

# *** Part 1 and 2 ***

for assignment in assignments:
    assignment = assignment.replace("\n","").split(",")
    # print(assignment)
    assign_1st = assignment[0].split("-")
    assign_2nd = assignment[1].split("-")
    # print(assign_1st)
    # print(assign_2nd)
    assign_1st_list = []
    assign_2nd_list = []
    for i in range(int(assign_1st[0]), int(assign_1st[1])+1):
        assign_1st_list.append(i)
    # print(assign_1st_list)
    for i in range(int(assign_2nd[0]), int(assign_2nd[1])+1):
        assign_2nd_list.append(i)
    
    if(len(assign_2nd_list) < len(assign_1st_list)):
        check1 = all(item in assign_1st_list for item in assign_2nd_list)
        check2 = any(item in assign_1st_list for item in assign_2nd_list)
    else:
        check1 = all(item in assign_2nd_list for item in assign_1st_list)
        check2 = any(item in assign_2nd_list for item in assign_1st_list)

    if(check1):
        pairs_1 += 1
    if(check2):
        pairs_2 += 1

print("Pairs found in Part 1 = ", pairs_1)
print("Pairs found in Part 2 = ", pairs_2)