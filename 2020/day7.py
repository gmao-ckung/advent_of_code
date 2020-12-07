f1 = open("/home/ckung/Code/advent_of_code/2020/input.test")

# Import the bag rules
bag_rules = f1.readlines()

bag_dictionary = {}

# Go through each rule and establish the bag_dictionary
# The key for the dictionary is the "input" bag
# The value associated with each key are the bags contained by the "input" bag
for bag_rule in bag_rules:
    bag_rule = bag_rule.replace("\n", "")
    bag_rule_s = bag_rule.split("contain ")
    start_bag_color = bag_rule_s[0]
    inside_bag_colors = bag_rule_s[1]
    #print(start_bag)
    #print(inside_bags)
    if start_bag_color not in bag_dictionary:
        inside_bag_colors = inside_bag_colors.replace(" bag, ", " ")
        inside_bag_colors = inside_bag_colors.replace(" bags, ", " ")
        inside_bag_colors = inside_bag_colors.replace(" bags.", "")
        inside_bag_colors = inside_bag_colors.replace(" bag.", "")
        bag_dictionary[start_bag_color.replace(" bags ", "")] = inside_bag_colors

for bag in bag_dictionary:
    print(bag.split(" "))
    print(bag_dictionary[bag].split(" "))