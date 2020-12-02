f1 = open("/home/ckung/Code/advent_of_code/2015/input.day5")

test_strings = f1.readlines()

vowel_list = ['a','e','i','o','u']
bad_list = ['ab', 'cd', 'pq', 'xy']
nice_count = 0

# *** Part 1 ***
for single_str in test_strings:

    test = single_str.replace("\n","")

    vowel_count = 0
    for vowel in vowel_list:
        vowel_count = vowel_count + test.count(vowel)

    #print(vowel_count)

    double = False

    for i in range(1,len(test)):
        if test[i-1] == test[i]:
            double = True
            break
    
    #print(double)

    contain_test = False

    for bad in bad_list:
        if bad in test:
            contain_test = True
            break

    #print(contain_test)

    if vowel_count >= 3 and double and not contain_test:
        nice_count = nice_count + 1

print("Part 1 Nice Count =", nice_count)

nice_count = 0

# *** Part 2 ***
for single_str in test_strings:

    test = single_str.replace("\n","")

    pair_exist = False
    for i in range(0,len(test)-1):
        l_pair = test[i]+test[i+1]
        if test.count(l_pair) > 1:
            pair_exist = True
            break
    
    three_pattern_exist = False
    for i in range(0,len(test)-2):
        if test[i] == test[i+2]:
            three_pattern_exist = True
            break

    if pair_exist and three_pattern_exist:
        nice_count = nice_count + 1

print("Part Two: Nice Count =", nice_count)