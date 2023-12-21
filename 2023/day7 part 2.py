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

CARDVALUES = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']


class Card():
    def __init__(self, line) -> None:
        self.cardstr, self.bid = line.split(' ')
        self.hand = Counter(self.cardstr)
        if 5 in self.hand.values():
            self.power = 'FIVEOFAKIND'
        elif 4 in self.hand.values():
            self.power = 'FOUROFAKIND'
            if self.hand['J'] == 1 or self.hand['J'] == 4:
                self.power = 'FIVEOFAKIND'
        elif 3 in self.hand.values() and 2 in self.hand.values():
            self.power = 'FULLHOUSE'
            if self.hand['J'] == 3:
                self.power = 'FIVEOFAKIND'
            if self.hand['J'] == 2:
                self.power = 'FIVEOFAKIND'
            if self.hand['J'] == 1:
                self.power = 'FOUROFAKIND'
        elif 3 in self.hand.values():
            self.power = 'THREEOFAKIND'
            if self.hand['J'] == 1 or self.hand['J'] == 3:
                self.power = 'FOUROFAKIND'
        elif list(self.hand.values()).count(2) == 2: 
            self.power = 'TWOPAIR'
            if self.hand['J'] == 2:
                self.power = 'FOUROFAKIND'
            if self.hand['J'] == 1:
                self.power = 'FULLHOUSE'
        elif 2 in self.hand.values():
            self.power = 'ONEPAIR'
            if self.hand['J'] >= 1:
                self.power = 'THREEOFAKIND'
        else:
            self.power = 'HIGHCARD'
            if self.hand['J'] == 1:
                self.power = 'ONEPAIR'
            
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
for card in Cards:
    print(card)