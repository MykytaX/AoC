import numpy as np

f = open("2022/input10.txt")
instructions = f.readlines()

currentcommand = None
currentline = 0
clock = 0
remembervalue = 0

x = 1
log = []
CRT = []
for i in range(0,6):
    CRT.append([])
    for j in range(0,40):
        CRT[i].append(".")
while currentline <= 139:
    log.append((clock, x))
    clock += 1
    row = 0
    pixeldraw = clock
    while pixeldraw > 40:
        pixeldraw -= 40
        row += 1
    pixeldraw -= 1
    if pixeldraw in [x-1, x, x+1]:
        CRT[row][pixeldraw] = "#"
    for i in range(0,6):
        print("\n")
        for j in range(0,40):
            print(CRT[i][j], end=" ")
    
    if currentcommand == None:
        currentcommand = instructions[currentline].rstrip()
        currentline += 1
        if currentcommand == "noop":
            currentcommand = None
            continue
        if currentcommand[:3] == "add":
            command, value = currentcommand.split(" ")
            remembervalue = value
            continue
    elif currentcommand[:3] == "add":
        x = x + int(remembervalue)
        currentcommand = None
        continue

for i in range(0,6):
    print("\n")
    for j in range(0,40):
        print(CRT[i][j], end=" ")
    

