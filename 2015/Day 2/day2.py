

f = open("input2.txt")
presents = f.readlines()
total = 0
for present in presents:
    present = present.rstrip()
    l, w, h = map(int, present.split("x"))
    total += 2*l*w + 2*w*h + 2*h*l
    total += min(l*w, w*h, h*l)

print(total)
ribbon = 0
#part 2
f = open("input2.txt")
presents = f.readlines()
total = 0
for present in presents:
    present = present.rstrip()
    l, w, h = map(int, present.split("x"))
    sorted = [l, w, h]
    sorted.sort()
    ribbon += sorted[0]*2 + sorted[1]*2
    ribbon += l*w*h

print(total)
print(ribbon)