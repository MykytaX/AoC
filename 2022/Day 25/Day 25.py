f = open("./2022/day25/test.txt")
numbers = [(x.rstrip()) for x in f.readlines()]
print(numbers)
total = 0
for number in numbers:
    decnumber = 0
    for i in range(1, len(number)+1):
        if number[-i] == "=":
            decnumber += pow(5,i-1)*(-2)
        elif number[-i] == "-":
            decnumber += pow(5,i-1)*(-1)
        else:
            decnumber += pow(5,i-1)*int(number[-i])
    print(decnumber)
    total += decnumber

print(total)

order = []

snafunum = {}
for k in range(0,25):
    snafunum.update({str(pow(5,k)): 0})
    order.append(pow(5,k))

neworder = sorted(order,reverse=True)
print(neworder)


for position in neworder:
    if total//position > 0:
        snafunum.update({str(position): total//position})
        total = total%position

for k in range(0,len(order)):
    if snafunum[str(order[k])] == 3:
        snafunum[str(order[k])] = "="
        snafunum[str(order[k+1])] += 1
    elif snafunum[str(order[k])] == 4:
        snafunum[str(order[k])] = "-"
        snafunum[str(order[k+1])] += 1
    elif snafunum[str(order[k])] == 5:
        snafunum[str(order[k])] = 0
        snafunum[str(order[k+1])] += 1


for k in range(0,len(neworder)):
    print(snafunum[str(neworder[k])], end="")