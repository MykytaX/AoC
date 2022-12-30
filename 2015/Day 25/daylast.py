import numpy as geek

column = 1
pos = 1
while column <= 3083:
    column += 1
    pos = pos + column 
    print(column, " ", pos)
pos = 4753986
mypostop = pos
row = 1
while row < 2978:
    mypostop = mypostop + 3083 + row - 1
    row += 1
    print(row , " " , mypostop)

print(mypostop)

code = 20151125
for i in range(1,mypostop):
    code = (code*252533)%33554393

print(code)
