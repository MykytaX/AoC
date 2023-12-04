import sys
from pathlib import Path

current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput

lines = parseinput("inputs/2023-4.txt")

#Part1
class Card():
    def __init__(self, id, winningnumberlist, mynumberlist):
        self.id = id
        self.winningnumbers = set([number.strip() for number in winningnumberlist.strip().split(' ')])
        self.winningnumbers.discard('')
        self.mynumbers = set([number.strip() for number in mynumberlist.strip().split(' ')])
        self.mynumbers.discard('')
        self.number = 1
        self.power = len(self.winningnumbers.intersection(self.mynumbers))
        if self.power == 0:
            self.points = 0
        elif self.power == 1:
            self.points = 1
        else:
            self.points = pow(2, self.power-1)
    def __str__(self):
        return (f'This is card {self.id}. It has {self.points} points. There are {self.power} common elements.')

Cards = []

for line in lines:
    idstr, numbers = line.split(':')
    _, *_, id = idstr.split(' ')
    winningnumberlist, mynumberlist = numbers.split('|')
    thisCard = Card(id, winningnumberlist, mynumberlist)
    Cards.append(thisCard)

total = 0
for crd in Cards:
    print(crd)
    total += crd.points

print(total)

#Part2
class Card():
    def __init__(self, id, winningnumberlist, mynumberlist):
        self.id = id
        self.winningnumbers = set([number.strip() for number in winningnumberlist.strip().split(' ')])
        self.winningnumbers.discard('')
        self.mynumbers = set([number.strip() for number in mynumberlist.strip().split(' ')])
        self.mynumbers.discard('')
        self.number = 1
        self.power = len(self.winningnumbers.intersection(self.mynumbers))
        if self.power == 0:
            self.points = 0
        elif self.power == 1:
            self.points = 1
        else:
            self.points = pow(2, self.power-1)
    def __str__(self):
        return (f'This is card {self.id}. It has {self.points} points. There are {self.power} common elements.')

Cards = []
for line in lines:
    idstr, numbers = line.split(':')
    _, *_, id = idstr.split(' ')
    winningnumberlist, mynumberlist = numbers.split('|')
    thisCard = Card(id, winningnumberlist, mynumberlist)
    Cards.append(thisCard)
total = 0

for crd in Cards:
    print(f'Procession Card {crd.id} with the power of {crd.power}')
    number_of_cards_won = crd.power
    while number_of_cards_won > 0:
        Cards[int(crd.id) + number_of_cards_won - 1].number += crd.number
        number_of_cards_won -= 1

total = 0
for crd in Cards:
    print(f'Card {crd.id} has number {crd.number}')
    total += crd.number

print(total)

