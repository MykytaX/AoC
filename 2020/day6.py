import os
def clear():
    os.system( 'cls' )

f = open("input6.txt")

fishtext = f.readlines()
fish = fishtext[0].split(",")
babyfishlist = [0,0,0,0,0,0,0,0,0]
adultfishlist = [0,0,0,0,0,0,0]
for x in range(0, len(fish)):
    fish[x] = int(fish[x])
    adultfishlist[fish[x]] += 1
day = 1
while day != 257:
    copyadultlist = list(adultfishlist)
    copybabylist = list(babyfishlist)

    adultfishlist[0] = copyadultlist[1]
    adultfishlist[1] = copyadultlist[2]
    adultfishlist[2] = copyadultlist[3]
    adultfishlist[3] = copyadultlist[4]
    adultfishlist[4] = copyadultlist[5]
    adultfishlist[5] = copyadultlist[6]
    adultfishlist[6] = copyadultlist[0] + copybabylist[0]
    
    
    babyfishlist[8] = copyadultlist[0] + copybabylist[0]
    babyfishlist[7] = copybabylist[8]
    babyfishlist[6] = copybabylist[7]
    babyfishlist[5] = copybabylist[6]
    babyfishlist[4] = copybabylist[5]
    babyfishlist[3] = copybabylist[4]
    babyfishlist[2] = copybabylist[3]
    babyfishlist[1] = copybabylist[2]
    babyfishlist[0] = copybabylist[1]

    print ("Adults: " , adultfishlist, "Babies: " , babyfishlist)
    
    day += 1
print(sum(adultfishlist)+sum(babyfishlist))
