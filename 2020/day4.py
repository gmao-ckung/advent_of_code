import string # string has a hexidecimal compare type
f1 = open("/home/ckung/Code/advent_of_code/2020/input.day4")

# Required fields for passport
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

passport_batch = f1.readlines()

# I assign a value to each required field: byr = 1, iyr = 2, ...
# If the field is found, the field's assigned value is added to 'checkSum'
# checkSum will equal 28 if all fields except for 'cid' are found
# checkSum will equal 36 is all fields including 'cid' are found
checkSum = 0
validPP_count = 0

for passport_data_line in passport_batch:
    passport_data_line = passport_data_line.replace("\n","")
    if passport_data_line == "":
        #print("CheckSum = ", checkSum)
        if checkSum == 28 or checkSum == 36:            
            validPP_count = validPP_count + 1
        checkSum = 0
    else:
        passport_data_line_s = passport_data_line.split()
        for field in passport_data_line_s:
            field_s = field.split(":")
            checkSum = checkSum + required_fields.index(field_s[0])+1

#print("CheckSum = ", checkSum)
if checkSum == 28 or checkSum == 36:            
    validPP_count = validPP_count + 1

print("Part 1: Number of Valid Passports =", validPP_count)

checkSum = 0
validPP_count = 0

for passport_data_line in passport_batch:
    passport_data_line = passport_data_line.replace("\n","")
    if passport_data_line == "":
        #print("CheckSum = ", checkSum)
        if checkSum == 28 or checkSum == 36:            
            validPP_count = validPP_count + 1
        checkSum = 0
    else:
        passport_data_line_s = passport_data_line.split()
        for field in passport_data_line_s:
            field_s = field.split(":")
            # The if statements perform all the passport value validation checks
            if field_s[0] == 'byr':
               if int(field_s[1]) < 1920 or int(field_s[1]) > 2002:
                   checkSum = checkSum + 100
                   break
            elif field_s[0] == 'iyr':
                if int(field_s[1]) < 2010 or int(field_s[1]) > 2020:
                   checkSum = checkSum + 100
                   break
            elif field_s[0] == 'eyr':
                if int(field_s[1]) < 2020 or int(field_s[1]) > 2030:
                   checkSum = checkSum + 100
                   break
            elif field_s[0] == 'hgt':
                unit = field_s[1][-2] + field_s[1][-1]
                if unit == 'cm':
                    if int(field_s[1][0:-2]) < 150 or int(field_s[1][0:-2]) > 193:
                        checkSum = checkSum + 100
                        break
                elif unit == 'in':
                    if int(field_s[1][0:-2]) < 59 or int(field_s[1][0:-2]) > 76:
                        checkSum = checkSum + 100
                        break
                else:
                    checkSum = checkSum + 100
                    break
            elif field_s[0] == 'hcl':
                if field_s[1][0] != '#' or len(field_s[1]) != 7 or not all(c in string.hexdigits for c in field_s[1][1:]):
                    checkSum = checkSum + 100
                    break
            elif field_s[0] == 'ecl':
                if field_s[1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    checkSum = checkSum + 100
                    break
            elif field_s[0] == 'pid':
                if len(field_s[1]) != 9 or not field_s[1].isnumeric:
                    checkSum = checkSum + 100
                    break
            checkSum = checkSum + required_fields.index(field_s[0])+1

if checkSum == 28 or checkSum == 36:            
    validPP_count = validPP_count + 1

print("Part 2: Number of Valid Passports =", validPP_count)