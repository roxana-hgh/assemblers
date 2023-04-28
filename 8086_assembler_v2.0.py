# 8086 assembler version 2.0
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

# Memorry encodings 
Mem = {
    '[BX][SI]' : '000',
    '[BX][DI]' : '001',
    '[BP][SI]' : '010',
    '[BP][DI]' : '011',
    '[SI]'     : '100',
    '[DI]'     : '101',
    '[BX]'     : '111',
}

# get assembly instruction from user and check if anything is wrong
def get_input():
    run = True
    while run:
        user_input = str(input("Enter instruction: "))
        try:
            parts = user_input.split()
            if len(parts) != 3:
                raise ValueError   # the input instruction is not correct (wrong format)
            if parts[0] not in opcodes.keys():
                raise ValueError   # the input operation is not correct (it's not in the opcodes dictionary)
            if not (all(x in list(Registers.keys()) + list(Mem.keys()) for x in [parts[1][:-1] , parts[2]])):
                raise ValueError   # registers name or memory name is not correct (check if the input names is in dictionaries or not)
            if parts[1][-1] != ',':
                raise ValueError   # the input instruction is not correct (not seprated by ',')
            else:
                run = False
        except:
            print("\n> Something went wrong, Please try again! \n")
    return parts

input_instruction_parts = get_input()

# Quantify every part of 8086 instruction format (16 bit)
opcode = opcodes[input_instruction_parts[0]] # 6 bits from 0 to 5 is opcode that specifies the instruction

d = '0' # 1 bit 6th (0 if reg is source, 1 if destination)

# mod 2 bit from 8 to 9 (memory mode or register mode)
if not set([input_instruction_parts[1][:-1] , input_instruction_parts[2]]).isdisjoint(list(Mem.keys())):
   
    mod = '00' # 00 = memory mode no displacement 

    #find reg index (reg is source or destination)
    if input_instruction_parts[1][:-1] in Registers.keys(): #reg index is 1 (destination) 
        rm = Mem[input_instruction_parts[2]] #Register/Memory field (R/M field), 3 bit from 13 to 15
        reg = Registers[input_instruction_parts[1][:-1]][0] # register code, 3 bit from 10 to 12
        w = str(Registers[input_instruction_parts[1][:-1]][1]) # 1 bit 7th (1 if reg is word, 0 if byte)
        d = '1' # register is destination
    
    elif input_instruction_parts[2] in Registers.keys(): #reg index is 2 (source)
        rm = Mem[input_instruction_parts[1][:-1]] 
        reg = Registers[input_instruction_parts[2]][0]
        w = str(Registers[input_instruction_parts[2]][1])

else:
    mod = '11' # 11 = register mode
    rm = Registers[input_instruction_parts[1][:-1]][0]
    reg = Registers[input_instruction_parts[2]][0]
    w = str(Registers[input_instruction_parts[2]][1]) 

# join all 16 bits in order
machine_code = opcode + d + w + mod + reg + rm

# display the result
print(f'>> {machine_code}')

