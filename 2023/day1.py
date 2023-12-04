import sys
from pathlib import Path

current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput

lines = parseinput("inputs/2023-1.txt")

# Part 1 Solution 1
def findfirstnum(line):
    for i in range(0, len(line)):
        if line[i].isdigit():
            return line[i]
    return '0'

def findsecondnum(line):
    for i in range(1, len(line)+1):
        if line[-i].isdigit():
            return line[-i]
    return '0'

total_sum = 0
for line in lines:
    print(line)
    number1 = findfirstnum(line)
    number2 = findsecondnum(line)
    sum = number1 + number2
    print(f'{number1} {number2} {sum}')
    total_sum += int(sum)

print(total_sum)

# Part 2 Solution 2

NUMBERS = {'one' : 1,'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7 ,'eight': 8,'nine': 9}



def findfirstnum2(line):
    for i in range(0, len(line)):
        if line[i].isdigit():
            return line[i]
        else:
            for number in NUMBERS.keys():
                if line[i:i+len(number)] == number:
                    return NUMBERS[number]
    return '0'

def findsecondnum2(line):
    for i in range(1, len(line)+1):
        if line[-i].isdigit():
            return line[-i]
        else:
            for number in NUMBERS.keys():
                if line[-i:-i-len(number):-1][::-1] == number:
                    return NUMBERS[number]
    return '0'

total_sum = 0
for line in lines:
    if line == 'tkmfour8fivevl9one':
        pass
    print(line)
    number1 = findfirstnum2(line)
    number2 = findsecondnum2(line)
    sum = str(number1) + str(number2)
    print(f'{number1} {number2} {sum}')
    total_sum += int(sum)

print(f'Solution part 2 {total_sum}')
