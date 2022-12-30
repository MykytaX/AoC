f = open("day3/input3.txt")
rucksacks = f.readlines()
print(rucksacks)
listofbaditems = []
for rucksack in rucksacks:
    doneflag = 0
    rucksack = rucksack.rstrip()
    comp1slice = slice(0, int(len(rucksack)/2))
    comp2slice = slice(int(len(rucksack)/2), len(rucksack))
    comp1 = rucksack[comp1slice]
    comp2 = rucksack[comp2slice]
    for char in comp1:
        for char2 in comp2:
            if char == char2:
                listofbaditems.append(char)
                doneflag = 1
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



    
