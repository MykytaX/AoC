import re

def solution_part1(input):
    with open(input, 'r') as file:
        data = file.read()
        matches = re.finditer(r'mul\(\d{1,3},\d{1,3}\)', data)
        sum = 0
        for match in matches:
            two_numbers = match.group(0)[4:-1]
            x, y = [int(num) for num in two_numbers.split(',')]
            multiply = x*y
            sum += multiply
        return sum
    
def re_calc(string):
    matches = re.finditer(r'mul\(\d{1,3},\d{1,3}\)', string)
    sum = 0
    for match in matches:
        two_numbers = match.group(0)[4:-1]
        x, y = [int(num) for num in two_numbers.split(',')]
        multiply = x*y
        sum += multiply
    return sum

def solution_part2(input):
    sum = 0
    with open(input, 'r') as file:
        data = file.read()
    sum = splitter(data)
    return sum
        
def splitter(code):
    try:
        goodcode, garbageandrest = code.split(r"don't()", maxsplit=1)
    except:
        return re_calc(code)
    try:
        _ , rest = garbageandrest.split("do()", maxsplit=1)
    except:
        return 0
    return re_calc(goodcode) + splitter(rest)


print(solution_part2('inputs/2024-3.txt'))
    