# Binary Addition and Subtraction
# Author: Roxana Haghgoo

#get the opration from user
run = True
while run:
    opration = str(input(">>> Please enter the opration (example 1 + 2 or 5 - 3): "))
    try:
        parts = opration.split()
        num1 = int(parts[0])
        num2 = int(parts[2])
        func = parts[1]
        if func in ['+','-']:
            run = False
        else:
            print("\n> please only enter + or - \n")
    except:
        print("\n> please try again! Make sure to enter the numbers and the operation correctly \n")

# A - B --> A + (-B)
if func == '-':
    num2 = -num2

# function to convert number to 2'compliment binary form
def bin2comp(n, bits):
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

# function to add two number bit by bit from rightmost digit to left
def addition(num1, num2, bit_len):
    bin_num1 = bin2comp(num1,bit_len)
    bin_num2 = bin2comp(num2,bit_len)

    result = ''
    carry = 0
    for i in range(bit_len-1, -1, -1):  #add numbers bit by bit from right to left
        r = carry
        r += 1 if bin_num1[i] == '1' else 0 #add carry if result is > 1 
        r += 1 if bin_num2[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1

    # convert result 2'compliment binary form to decimal
    while len(result) < bit_len:
        result = '0'+ result
    if result[0] == '0':
        return int(result, 2)
    else:
        return -1 * (int(''.join('1' if x == '0' else '0' for x in result), 2) + 1)


# run function above and check if it occurs an overflow and add more bits if overflow happen    
bit_len = 32   #start with 32bit    
overflow = True
while overflow:  
    final = addition(num1,num2,bit_len)
    if num1 >= 0 and num2 >= 0 and final < 0:
        bit_len = bit_len * 2
        overflow = True
    elif num1 < 0 and num2 < 0 and final >= 0:
        bit_len = bit_len * 2
        overflow = True
    else:
        overflow = False

#display final decimal result
print(f'{opration} = {final}')
