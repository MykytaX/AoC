# just lists
f = open("day3/input3.txt")
rucksacks = f.readlines()
listofbaditems = []
elfgroups = []
elfgroup = []
count = 0
for rucksack in rucksacks:
    rucksack = rucksack.rstrip()
    elfgroup.append(rucksack)
    count += 1
    if count == 3:
        count = 0
        elfgroups.append(elfgroup)
        elfgroup = []
print(elfgroups)
for elfgroup in elfgroups:
    doneflag = 0
    for char1 in elfgroup[0]:
        if doneflag == 1:
            break
        for char2 in elfgroup[1]:
            if char1 == char2:
                for char3 in elfgroup[2]:
                    if char1 == char3:
                        doneflag = 1
                        listofbaditems.append(char1)
                        break
            if doneflag == 1:
                break
    
    
total = 0
print(listofbaditems)
for item in listofbaditems:
    if item.islower():
        total += ord(item)-96
        print(item + str(ord(item)-96))
    else:
        total += ord(item)-38
        print(item + str(ord(item)-38))
    
print(total)
# do sets

f = open("day3/input3.txt")
rucksacks = f.readlines()
listofbaditems = []
elfgroups = []
elfgroup = []
count = 0
for rucksack in rucksacks:
    rucksack = rucksack.rstrip()
    elfgroup.append(set(rucksack))
    count += 1
    if count == 3:
        count = 0
        elfgroups.append(elfgroup)
        elfgroup = []
print(elfgroups)
    
for elfgroup in elfgroups:
    for char1 in elfgroup[0]:
        if char1 in elfgroup[1] and char1 in elfgroup[2]:
            listofbaditems.append(char1)
            break
    
print(listofbaditems)
total = 0
print(listofbaditems)
for item in listofbaditems:
    if item.islower():
        total += ord(item)-96
        print(item + str(ord(item)-96))
    else:
        total += ord(item)-38
        print(item + str(ord(item)-38))
print(total)