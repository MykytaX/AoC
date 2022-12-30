f = open("2015/input8.txt")

strings = f.readlines()
betterstrings = []
for string in strings:
    string = string.rstrip()
    betterstrings.append(string)
    print(string)
totallist = []

for string in betterstrings:
    length = len(repr(string))-2
    memstring = string[1:-1]
    
    hexflag = 0
    doubleskip = 0
    charcount = 0
    expectbrace = 0
    for char in memstring:
        if doubleskip > 0:
            doubleskip -= 1
            continue
        elif char == "\\" and expectbrace == 1:
            charcount += 1
            expectbrace = 0
            length -= 1
            hexflag = 0
            continue
        elif char == "\\":
            hexflag = 1
            expectbrace = 1
            length -= 1
            continue
        elif char == "x" and hexflag == 1:
            doubleskip = 2
            charcount += 1
            hexflag = 0
            continue
        else:
            charcount += 1 
            expectbrace = 0
    total = length - charcount
    totallist.append(total)

print(sum(totallist))

newtotal = []

for string in betterstrings:
    length = len(repr(string))-2
    memstring = string[1:-1]
    total = memstring.count("\\x")*3+memstring.count("\\\\")*1+memstring.count('\\"')+2
    if total != (len(string) - len(eval(string))):
        print(memstring, total, "OR", len(string) - len(eval(string)))
    newtotal.append(total)


print(sum(newtotal))
print(newtotal)
print(len(newtotal))
    