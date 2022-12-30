import numpy as ny

f = open("input4.txt")
sequencestring = f.readline()
seq = sequencestring.split(",")
seq[-1] = '89'
print(len(seq))
WINNERCARD = 0
WINNERNUM = 0
for i in range(0, len(seq)):
    seq[i] = int(seq[i])

bingocards = [x for x in range(0,100)]

for i in range(0, 100):
    bingocards[i] = ny.loadtxt("input4.txt", dtype=int, max_rows=5, skiprows=2+6*i)

bingocards2 = ny.copy(bingocards)
###     for h in range(0,5):
###    bingocards[0][0][h] = -1
break_out_flag = False
WINNERSET = set()
for drawnnumber in seq:
    for i in range(0,100):
        for row in bingocards[i]:
            for y in range(0,5):
                if row[y] == drawnnumber:
                    row[y] = -1
    for i in range(0,100):
        for row in bingocards[i]:
            if all(num == -1 for num in row):
                WINNERSET.add(i)
                if len(WINNERSET) == 100:
                    WINNERCARD = i
                    WINNERNUM = drawnnumber
                    break_out_flag = True
                    break
        for column in bingocards[i].T:
            if all(num == -1 for num in column):
                WINNERSET.add(i)
                if len(WINNERSET) == 100:
                    WINNERCARD = i
                    WINNERNUM = drawnnumber
                    break_out_flag = True
                    break
        if break_out_flag: break
    if break_out_flag: break    

SUM = 0
for row in bingocards[WINNERCARD]:
    for x in row:
        if x != -1: 
            SUM += x

print(SUM*WINNERNUM, bingocards[WINNERCARD], WINNERNUM)

