import sys
from pathlib import Path
from itertools import product


current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput

lines = [x.strip() for x in parseinput('inputs/2023-12.txt')]

class Spring():
    
    def __init__(self, array, code):
        self.array = array
        self.code = code.split(',')
        self.unknowns = array.count('?')
        self.possibilities = []
        for combo in product({'#','.'}, repeat=self.unknowns):
            newarray = ''
            j = 0
            for char in self.array:
                if char == '?':
                    newarray = newarray + combo[j]
                    j = j + 1
                else:
                    newarray = newarray + char
            self.possibilities.append(newarray)    
            
    
    def validate(self, possibility):
        generated_code = []
        counting = False
        countlength = 0
        for char in possibility:
            if char == '#':
                counting = True
                countlength += 1
            if char == '.' and counting == True:
                generated_code.append(str(countlength))
                countlength = 0
                counting = False
        if counting == True:
            generated_code.append(str(countlength))
        if self.code == generated_code:
            return True
        else:
            return False

Springs = []
for line in lines:
    array, code = line.split()
    newspring = Spring(array, code)
    Springs.append(newspring)
totalpossibilities = 0

for spring in Springs:
    for possibility in spring.possibilities:
        if spring.validate(possibility):
            totalpossibilities += 1

print(totalpossibilities)

    