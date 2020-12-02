import hashlib

input_str = "bgvyzdsv"
i = 1

# *** Part 1 ***
while i > 0:
    str_append = str(i)
    
    str_test = input_str + str_append

    result = hashlib.md5(str_test.encode())

    if result.hexdigest()[0:5] == "00000":
        print(result.hexdigest())
        print("Number = ", i)
        break

    i = i + 1

# *** Part 2 ***
i = 1
while i > 0:
    str_append = str(i)
    
    str_test = input_str + str_append

    result = hashlib.md5(str_test.encode())

    if result.hexdigest()[0:6] == "000000":
        print(result.hexdigest())
        print("Number = ", i)
        break

    i = i + 1