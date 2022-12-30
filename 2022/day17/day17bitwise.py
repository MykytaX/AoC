f = open("./day17/input17.txt")

commands = list(f.read())
print(commands)

lineblock = [int("0011110", 2)]
plusblock = [int("0001000", 2), int("0011100", 2), int("0001000", 2)]

otherLshape = [int("0000100", 2), int("0000100", 2), int("0011100", 2)]
vertline =[int("0010000", 2), int("0010000", 2), int("0010000", 2), int("0010000", 2)]
square = [int("0011000", 2), int("0011000", 2)]
figures = [lineblock, plusblock, otherLshape, vertline, square]


numberofpiece = 0
i = 0
floor = [int("1111111", 2)]
well = [floor]
currentpiece = figures[0]
GenerateNewFlag = True
step = -1
prevheight = 0

while numberofpiece + 1 < 1000000000001:
    step += 1
    command = commands[step%len(commands)]
    if GenerateNewFlag == True:
#        for k in range(1,len(well)+1):
#            print("\n", end="")
#            for j in range(0,7):
#                print(well[-k][j], end="")
        height = abs(min(currentpiece, key=lambda x: x[0])[0])
        currentpiecePOS = [len(well)+3+height, 2]
        GenerateNewFlag = False
    if command == ">":                  
        currentpiecePOS[1] += 1
        for block in currentpiece:
            if block[1] + currentpiecePOS[1] == 7:
                currentpiecePOS[1] -= 1
                
                break
            try:
                if well[currentpiecePOS[0]+block[0]][currentpiecePOS[1]+block[1]] == 1:
                    currentpiecePOS[1] -= 1
                     
                    break
            except:
                continue
    elif command == "<":
        currentpiecePOS[1] -= 1
        for block in currentpiece:
            if block[1] + currentpiecePOS[1] == -1:
                currentpiecePOS[1] += 1
                 
                break
            try:
                if well[currentpiecePOS[0]+block[0]][currentpiecePOS[1]+block[1]] == 1:
                    currentpiecePOS[1] += 1
                    break
            except:
                continue
            
    
    currentpiecePOS[0] -= 1
    for block in currentpiece:
        if block[0] + currentpiecePOS[0] <= len(well)-1:
            if well[currentpiecePOS[0]+block[0]][currentpiecePOS[1]+block[1]] == 1:
                currentpiecePOS[0] += 1
                difference = 0
                for block in currentpiece:
                    if block[0]+currentpiecePOS[0] > len(well)-1:
                        difference = max(block[0]+currentpiecePOS[0] - len(well)+1, difference)
                for i in range(0,difference):
                    well.append([0,0,0,0,0,0,0])
                for block in currentpiece:
                    well[currentpiecePOS[0]+block[0]][currentpiecePOS[1]+block[1]] = 1
                for level in range(1,len(well)):
                    if well[level] == [1,1,1,1,1,1,1]:
                        prevheight += level
                        well = well[level:]
                        break
                GenerateNewFlag = True
                numberofpiece += 1 
                currentpiece = figures[numberofpiece%5]
                if numberofpiece%10000 == 0:
                    print(numberofpiece, len(well), prevheight)
                break
    continue

print(prevheight+len(well)-1)

