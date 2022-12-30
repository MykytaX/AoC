f = open("day4/input.txt")
pairs = f.readlines()
total = 0
totalp2 = 0
for pair in pairs:
    pair = pair.rstrip()
    range1, range2 = pair.split(",")
    range1num1, range1num2 = range1.split("-")
    range2num1, range2num2 = range2.split("-")
    if int(range1num1) <= int(range2num1) and int(range1num2) >= int(range2num2):
        total+= 1.
        print(range1num1, "-", range1num2, "and", range2num1, "-", range2num2)
        continue
    if int(range2num1) <= int(range1num1) and int(range2num2) >= int(range1num2):
        total+= 1
        print(range1num1, "-", range1num2, "and", range2num1, "-", range2num2)
        continue
print(total)

for pair in pairs:
    pair = pair.rstrip()
    range1, range2 = pair.split(",")
    range1num1, range1num2 = range1.split("-")
    range2num1, range2num2 = range2.split("-")
    range1set = set(range(int(range1num1), int(range1num2)+1))
    range2set = set(range(int(range2num1), int(range2num2)+1))
    if len(range1set.intersection(range2set)) > 0:
        totalp2 += 1
        continue
print(range1set)
print(totalp2)