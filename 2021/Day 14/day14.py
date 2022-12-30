from collections import Counter


f = open("input14.txt")

lines = f.readlines()

input = lines[0].replace("\n", "")

rules = lines[2:]
tomeofrules = {}
for line in rules:
    key, letter = line.replace("\n", "").split(" -> ")
    tomeofrules.update({key:letter})
bucket = tomeofrules.copy()
for key in bucket:
    bucket[key] = 0
for i in range(0, len(input)-1):
    bucket[input[i]+input[i+1]] += 1
print(bucket) 

counter = {}
for key, value in tomeofrules:
    counter.update({value:0})
for letter in input:
    counter[letter] += 1
print(counter)
newbucket = bucket.copy()
for i in range(0,40):
    for key in newbucket:
        newbucket[key] = 0
    for pair in bucket:
        counter[tomeofrules[pair]] += bucket[pair]
        newpair1 = pair[0]+tomeofrules[pair]
        newpair2 = tomeofrules[pair]+pair[1]
        newbucket[newpair1] += bucket[pair]
        newbucket[newpair2] += bucket[pair]
    bucket = newbucket.copy()

print(max(counter.values())-min(counter.values()))