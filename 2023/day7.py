import sys
from pathlib import Path
from functools import reduce
from collections import Counter

current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput

lines = parseinput('inputs/2023-7.txt')

POWERLEVEL = ['HIGHCARD', 'ONEPAIR', 'TWOPAIR', 'THREEOFAKIND', 'FULLHOUSE', 'FOUROFAKIND', 'FIVEOFAKIND']

CARDVALUES = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']


class Card():
    def __init__(self, line) -> None:
        self.cardstr, self.bid = line.split(' ')
        self.hand = Counter(self.cardstr)
        if 5 in self.hand.values():
            self.power = 'FIVEOFAKIND'
        elif 4 in self.hand.values():
            self.power = 'FOUROFAKIND'
        elif 3 in self.hand.values() and 2 in self.hand.values():
            self.power = 'FULLHOUSE'
        elif 3 in self.hand.values():
            self.power = 'THREEOFAKIND'
        elif list(self.hand.values()).count(2) == 2: 
            self.power = 'TWOPAIR'
        elif 2 in self.hand.values():
            self.power = 'ONEPAIR'
        else:
            self.power = 'HIGHCARD'
            
    def __repr__(self):
        return str(self.cardstr) + f' {self.power}'
    
    def __gt__(self, other):
        if isinstance(other, Card):
            if POWERLEVEL.index(self.power) > POWERLEVEL.index(other.power):
                return True
            elif POWERLEVEL.index(self.power) == POWERLEVEL.index(other.power):
                for char1, char2 in zip(self.cardstr,other.cardstr):
                    if CARDVALUES.index(char1) > CARDVALUES.index(char2):
                        return True
                    elif CARDVALUES.index(char1) == CARDVALUES.index(char2):
                        continue
                    else:
                        return False
                return False

Cards = []

for line in lines:
    newcard = Card(line)
    Cards.append(newcard)

Cards.sort()
winnings = 0
for i, card in enumerate(Cards):   
    winnings += (i+1)*int(card.bid)
    
print(winnings)
        