targetx = set(range(247,286))
targety = set(range(-84, -55))

class probe:
    velocityX = 0
    velocityY = 0
    position = [0,0]

dooper = probe()
champY = 0
winnerflag = 0

for velocityX in range(1,287):
    for velocityY in range(1,1000):
        dooper.position[0] = 0
        dooper.position[1] = 0
        dooper.velocityX = velocityX
        dooper.velocityY = velocityY
        winnerflag = 0
        maxY = 0
        print("Testing velocities ", velocityX, velocityY)
        while dooper.position[0] < 248 and dooper.position[1] > -85:
            dooper.position[0] += dooper.velocityX
            dooper.position[1] += dooper.velocityY
            if dooper.position[1] > maxY:
                maxY = dooper.position[1]
            if dooper.velocityX > 0:
                dooper.velocityX -= 1
            dooper.velocityY -= 1
            if dooper.position[0] in targetx and dooper.position[1] in targety:
                winnerflag = 1
                print("landed!!!"*1000, maxY*10000)
 #           print(dooper.position[0], dooper.position[1])
            
        if winnerflag == 1 and maxY > champY:
            champY = maxY
            print("New champion...", maxY, " with velocities ", velocityX, velocityY)

print(champY)