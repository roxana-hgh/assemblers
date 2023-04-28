# R_type to Risc_V assembler
# Author: Roxana Haghgoo

# RISC-V instruction encodings => 'instruction' : (funct3,funct7,opcode) | FIGURE 2.18 Computer Organization and Design book
encodings = {
    'add': (0,0,51), 'sub': (0,32,51),
    'sll': (1,0,51), 'xor': (4,0,51),
    'srl': (5,0,51), 'sra': (5,32,51), 
    'or' : (6,0,51), 'and': (7,0,51),
    'lr.d': (3,8,51),'sc.d': (3,12,51)
}

# get R_type code from user and check if anything is wrong
def get_rtype():
    run = True
    while run:
        user_input = str(input('> Enter R_type code: '))
        try:
            parts = user_input.split()
            if len(parts) != 4:
                raise ValueError
            if parts[0] not in encodings.keys():
                raise ValueError
            else:
                run = False
        except:
            print("\n> Something went wrong, Please try again! \n")
    return parts

instruction = get_rtype()


#find r_type code diffrent parts from dictionary above and convert them to binary and fill them to their bit lenght
funct3 = bin(encodings[instruction[0]][0])[2:].zfill(3)
funct7 = bin(encodings[instruction[0]][1])[2:].zfill(7)
opcode = bin(encodings[instruction[0]][2])[2:].zfill(7)
rs2 = bin(int(instruction[3][1]))[2:].zfill(5)
rs1 = bin(int(instruction[2][1]))[2:].zfill(5)
rd = bin(int(instruction[1][1]))[2:].zfill(5)

# disply the result
result = funct7 + rs2 + rs1 + funct3 + rd + opcode
print(f">>> {result}  |  {' '.join(instruction)}")