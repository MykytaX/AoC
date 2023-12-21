import sys
from pathlib import Path
from itertools import cycle


current_file_path = Path(__file__).resolve()
parent_dir = current_file_path.parent.parent
sys.path.append(str(parent_dir))

from utils import parseinput

lines = [x.strip() for x in parseinput('inputs/2023-9.txt')]

# def godown(numseq):
#     newseq = []
#         difference = numseq[i+1] - numseq[i]
#     for i in range(0, len(numseq)-1):
#         newseq.append(difference)
#     if set(newseq) != {0}:
#         return numseq[-1]+godown(newseq)

#     else: #         return numseq[-1]
def godown2(numseq):
    newseq = []
    for i in range(0, len(numseq)-1):
        difference = numseq[i+1] - numseq[i]
        newseq.append(difference)
    if set(newseq) != {0}:
        return newseq[0]-godown2(newseq)
    else:
        return 0

print(lines)
sum = 0
for line in lines:
    numseq = [int(x) for x in line.split(' ')]

    sum += numseq[0] - godown2(numseq)
    
print(sum)