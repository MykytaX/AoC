
def run(input):
    totaldistance = 0
    similarty_score_total = 0
    with open(input, 'r') as file:
        data = file.readlines()
        leftnumbers = list()
        rightnumbers =  list()
        for line in data:
            leftnumber, rightnumber = line.split('  ')
            leftnumber = int(leftnumber)
            rightnumber = int(rightnumber)
            leftnumbers.append(leftnumber)
            rightnumbers.append(rightnumber)
        sorted_left = sorted(leftnumbers)
        sorted_right = sorted(rightnumbers)
        
        for x, y in zip(sorted_left, sorted_right):
            distance = abs(x-y)
            totaldistance += distance

        for x in sorted_left:
            times_appear = rightnumbers.count(x)
            similarty_score = x*times_appear
            similarty_score_total += similarty_score

    return {"Star 1: " : totaldistance, "Star 2: " : similarty_score_total }

print(run('inputs/2024/Day1.txt'))