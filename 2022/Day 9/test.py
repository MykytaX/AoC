def oo(number = 2):
    newnumber = int(number) + 3
    return newnumber

listofitems = []
for i in range(0,3):
    newitem = oo(i)
    listofitems.append(newitem)

print(listofitems)
