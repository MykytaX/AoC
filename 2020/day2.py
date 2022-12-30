f = open("input3.txt")
oxy = f.read().splitlines()
f = open("input3.txt")
c02 = f.read().splitlines()
onecount = 0
i = 0
print(len(oxy))
while len(oxy) > 1:
    onecount = 0
    for number in oxy:
        if number[i] == "1":
                onecount += 1
    if onecount < len(oxy)/2:
        for number in list(oxy):
            if number[i] == "1":
                oxy.remove(number)
    else:
        for number in list(oxy):
            if number[i] == "0":
                oxy.remove(number)
    i += 1
i = 0
while len(c02) > 1:
    onecount = 0
    for number in c02:
        if number[i] == "1":
                onecount += 1
    if onecount >= len(c02)/2:
        for number in list(c02):
            if number[i] == "1":
                c02.remove(number)
    else:
        for number in list(c02):
            if number[i] == "0":
                c02.remove(number)
    i += 1

print(int(oxy[0],2)*int(c02[0],2))

    
            