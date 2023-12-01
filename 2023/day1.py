from utils import parseinput

lines = parseinput("inputs/2023-1.txt")

def findfirstnum(line):
    for i in range(0, len(line)):
        if line[i].isdigit():
            return line[i]
def findsecondnum(line):
    for i in range(1, len(line)+1):
        if line[-i].isdigit():
            return line[-i]
Totalsum = 0
for line in lines:
    print(line)
    number1 = findfirstnum(line)
    number2 = findsecondnum(line)
    sum = number1 + number2
    print(str(number1) + ' ' + str(number2) + ' '+ str(sum))
    Totalsum += int(sum)
print(Totalsum)


