# R_type to Risc_V assembler v.1
# Author: Roxana Haghgoo

# RISC-V instruction encodings => 'instruction' : (funct3,funct7) | FIGURE 2.18 Computer Organization and Design book
encodings = {
    'add': (0,0), 'sub': (0,32),
    'sll': (1,0), 'xor': (4,0),
    'srl': (5,0), 'sra': (5,32), 
    'or' : (6,0), 'and': (7,0),
    'lr.d': (3,8),'sc.d': (3,12)
}

# get R_type code from user
def get_rtype():
    run = True
    while run:
        user_input = str(input('>>> Enter R_type code: '))
        try:
            for i in user_input:
                num = int(i)
                if num not in [0,1]:
                    raise ValueError
            if len(user_input) == 32:
                run = False
            else:
                raise ValueError
        except:
            print("\n> Something went wrong, Please try again! \n")
    return user_input

rtype = get_rtype()

# slice 32bit r_type code and convert each of them from binary to decimal 
funct7 = int(rtype[0:7],2)
rs2 = int(rtype[7:12],2)
rs1 = int(rtype[12:17],2)
funct3 = int(rtype[17:20],2)
rd = int(rtype[20:25],2)

# find risc_v instructions
for encode, code in encodings.items():
    if code == (funct3,funct7):
        instruction = encode

# display result
result = f'>>> {instruction} x{rd}, x{rs1}, x{rs2}'
print(result)

