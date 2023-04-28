# find data dependencies on RISC-v instructions
# Author: Roxana Haghgoo  9811309

''' NOTE: the program input as default is "instructions.txt" with some test instructions,
please make sure both files and terminal are in the same directory 
you can change instructions on "instructions.txt" for other tests '''

import itertools

# open and read file
f = open("instructions.txt","r")
instructions = f.readlines()
lines = {}
for i in instructions:
    lines[instructions.index(i)+1] = [x.replace(',','') for x in i.split()]

raw = []  # Read after write dependencies
war = []  # write after Read dependencies
waw = []  # write after write dependencies
rar = []  # Read after Read dependencies

# check for dependencies and add them in list like => [lines number that have dependency] , the dependency , if is hazard 
for a, b in itertools.combinations(lines.items(), 2):   # a is instruction1 and b is instruction2 that compares together 
    i1 = set(a[1][2:])  # i is the set of memory locations read for instruction
    i2 = set(b[1][2:])
    o1 = {a[1][1]}      # o is the set of memory locations written by instruction
    o2 = {b[1][1]}

    if (o1 & i2):
        raw.append([(a[0],b[0]), o1 & i2, 1])
    elif(i1 & o2):
        war.append([(a[0],b[0]), i1 & o2, 1])
    elif(o1 & o2):
        waw.append([(a[0],b[0]), o1 & o2, 1])
    elif(i1 & i2):
        rar.append([(a[0],b[0]), i1 & i2, 0])  # RAR dependencies never causing a hazard


# dependencies that is 3 or more line betwwen them will not causing a hazard
for i in war + raw + waw :
    if abs(i[0][1] - i[0][0]) >= 3:
        i[2] = 0

# display the results
is_hazard = 'and it may causing a hazard'
not_hazard = 'but its NOT causing a hazard'

for i in raw:
    print(f'{i[1]} in lines {i[0][0]} and {i[0][1]} have a RAW dependency, {is_hazard if i[2] else not_hazard}')
    
for i in war:
    print(f'{i[1]} in lines {i[0][0]} and {i[0][1]} have a WAR dependency, {is_hazard if i[2] else not_hazard}')

for i in waw:
    print(f'{i[1]} in lines {i[0][0]} and {i[0][1]} have a WAW dependency, {is_hazard if i[2] else not_hazard}')

for i in rar:
    print(f'{i[1]} in lines {i[0][0]} and {i[0][1]} have a RAR dependency, but its NOT causing a hazard')

