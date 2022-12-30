import matplotlib.pyplot as pyp

f = open("input7.txt")
crabs = [int(x) for x in f.readlines()[0].split(",")]
bestmin = 1000000000
bestpos = 0
for position in range (400,500):
    print("Testing position " + str(position))
    totalcost = 0
    for crab in crabs:
        cost = 0
        steps = abs(crab - position)
        for step in range(0, steps+1):
            cost += step
        totalcost += cost
    print("For position " + str(position) + " we need " + str(totalcost) + " fuel cells.")
    if totalcost < bestmin:
        bestmin = totalcost
        bestpos = position

print("At position " + str(bestpos) + " it only takes " + str(bestmin) + " fuel cells.")



