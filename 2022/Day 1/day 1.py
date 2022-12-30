f = open("inputdayone2022")
alldata = f.read()
elves = alldata.split("\n\n")
count =0
curchamp = 0
podium=[0, 0, 0]
for elf in elves:
	total = 0
	goodelf = elf.split("\n")
	for food in goodelf:
		total += int(food)	
	if total > podium[2]:
		podium[0] = podium[1]
		podium[1] = podium[2]
		podium[2] = total
		continue
	if total > podium[1]:
		podium[0]= podium[1]
		podium[1]= total
		continue
	if total > podium[0]:
		podium[0]= total
		continue
		
	
print(sum(podium))

		