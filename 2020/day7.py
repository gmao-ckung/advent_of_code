f1 = open("/home/ckung/Code/advent_of_code/2020/input.day7")

# Import the bag rules
bag_rules = f1.readlines()

bag_dictionary = {}

# Go through each rule and establish the bag_dictionary
# The key for the dictionary is the "input" bag
# The value associated with each key are the bags contained inside the "input" bag
for bag_rule in bag_rules:
    bag_rule = bag_rule.replace("\n", "")
    bag_rule_s = bag_rule.split("contain ")
    start_bag_color = bag_rule_s[0].replace(" bags ", "")
    inside_bag_colors = bag_rule_s[1]
    #print(start_bag)
    #print(start_bag_color)
    if start_bag_color not in bag_dictionary:
        # Get rid of "bag"/"bags" wording and punctuation
        inside_bag_colors = inside_bag_colors.replace(" bag, ", " ")
        inside_bag_colors = inside_bag_colors.replace(" bags, ", " ")
        inside_bag_colors = inside_bag_colors.replace(" bags.", "")
        inside_bag_colors = inside_bag_colors.replace(" bag.", "")
        bag_dictionary[start_bag_color] = inside_bag_colors

# A recursive routine to look inside a bag (current_bag_key) using bag_dictonary and find whether it has a shiny gold bag
def find_gold_bag(current_bag_key, bag_dictionary):
    find_gold_bag_flag = False
    bag_parse = bag_dictionary[current_bag_key].split(" ")
    #print(bag_parse)
    
    # This if statement means a bag contains more bags to examine
    if bag_parse[0] != 'no':
        # Parse the dictionary value to examine the bags that are "inside" current_bag_key
        for i in range(0,len(bag_parse),3):
            inside_bag_color = bag_parse[i+1] + " " + bag_parse[i+2]
            #print(inside_bag_color)
            if inside_bag_color == "shiny gold":
                #print("Found Shiny Gold Bag!")
                return True
            else:
                find_gold_bag_flag = find_gold_bag(inside_bag_color, bag_dictionary) or find_gold_bag_flag

        return find_gold_bag_flag
    else:
        #print("No shiny gold bag down this rabbit hole")
        return False

def bag_counter(current_bag_key, bag_dictionary):
    bag_parse = bag_dictionary[current_bag_key].split(" ")
    count = 0
    print("Looking inside", current_bag_key)
    if bag_parse[0] != 'no':
        for i in range(0, len(bag_parse),3):        
            inside_bag_color = bag_parse[i+1] + " " + bag_parse[i+2]
            print("Examining", inside_bag_color)
            bags_found = bag_counter(inside_bag_color, bag_dictionary)
            count = count + int(bag_parse[i]) + int(bag_parse[i]) * bags_found
        print(current_bag_key, "has", count,"bags")
        return count
    else:
        print("No more bags found inside",current_bag_key,"...going back up...")
        return 0

# *** Part 1 ***
bag_count = 0
for bag in bag_dictionary:
    if bag != "shiny gold":
        print("***Searching",bag, "***")
        if find_gold_bag(bag, bag_dictionary) == True:
            bag_count = bag_count + 1

print("Bag Colors containing a gold bag =", bag_count)

# *** Part 2 ***
print("***Checking shiny gold Bag***")
bag_counter("shiny gold", bag_dictionary)