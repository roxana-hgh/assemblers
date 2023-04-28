# 8086 assembler version 1.0
# Author: Roxana Haghgoo

#opcodes encoding for each instruction
opcodes = {
    'ADD' : '000000',
    'OR'  : '000010',
    'AND' : '100000',
    'SUB' : '001010',
    'ADC' : '000100',
    'MOV' : '100010',
}

# register encodings and w bit 
Registers = {
    'AL': ('000', 0), 'AX': ('000', 1),
    'CL': ('001', 0), 'CX': ('001', 1),
    'DL': ('010', 0), 'DX': ('010', 1),
    'BL': ('011', 0), 'BX': ('011', 1),
    'AH': ('100', 0), 'SP': ('100', 1),
    'CH': ('101', 0), 'BP': ('101', 1),
    'DH': ('110', 0), 'SI': ('110', 1),
    'BH': ('111', 0), 'DI': ('111', 1),
}

# get assembly instruction from user and check if anything is wrong
def get_input():
    run = True
    while run:
        user_input = str(input("Enter instruction: "))
        try:
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError
            if parts[0] not in opcodes.keys():
                raise ValueError
            if (parts[1][:-1] and parts[2]) not in Registers.keys():
                raise ValueError
            else:
                run = False
        except:
            print("\n> Something went wrong, Please try again! \n")
    return parts

input_instruction_parts = get_input()

# Quantify every part of 8086 instruction format (16 bit)
opcode = opcodes[input_instruction_parts[0]] # 6 bits from 0 to 5 is opcode that specifies the instruction
d = '0' # 1 bit 6th
w = str(Registers[input_instruction_parts[2]][1]) # 1 bit 7th
mod = '11' # 2 bit from 8 to 9, 11 = register mode 
reg = Registers[input_instruction_parts[2]][0] # reg register for the first operand (source), 3 bit from 10 to 12 
rm = Registers[input_instruction_parts[1][:-1]][0] #Register/Memory field (R/M field), 3 bit from 13 to 15

# join all 16 bits in order
machine_code = opcode + d + w + mod + reg + rm

# display the result
print(f'>> {machine_code}')

