import sys
from pathlib import Path
from itertools import cycle


current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput

lines = parseinput('inputs/2023-8.txt')

instructions = cycle(list(lines[0].strip()))

map = {}
for line in lines[2:]:
    node, directions = line.split(' = ')
    leftdir, rightdir = directions.split(', ')
    map.update({node: (leftdir[1:], rightdir[:3])})

endinglocations = set()
currentlocations = []
for location in map.keys():
    if location[-1] == 'A':
        currentlocations.append(location)
    elif location[-1] == 'Z':
        endinglocations.add(location)


allsteps = []

location = 'DRA'

for location in currentlocations:
    steps = 0
    for instruction in instructions:
        steps += 1
        if instruction == 'R':
            location = map[location][1]
        else: 
            location = map[location][0]
        if location[-1] == 'Z':
            print(f'At {steps} found {location}')
            allsteps.append(steps)
            break
        
print(allsteps)       

def gcd(a,b):
    while b != 0:
        a,b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
result = allsteps[0]
for i in range(1, len(allsteps)):
    # Update the LCM to be the LCM of the current LCM and the next number in the list
    result = lcm(result, allsteps[i])
    
print(result)