def solution (file):
    with open(file, 'r') as file:
        reports = file.readlines()
        safereports = 0
        for report in reports:
            increasing = False
            decreasing = False
            safe = True
            numbers = [ int(x) for x in report.split() ]
            
            if numbers[0] < numbers[1]:
                increasing = True
            elif numbers[1] < numbers[0]:
                decreasing = True
            else:
                safe = checkwithoutalevel(numbers)
                if safe:
                    print(numbers, '...is SAFE!')
                    safereports += 1
                    continue
                else:
                    continue
            for i in range(0,len(numbers)-1):
                if abs(numbers[i]-numbers[i+1]) > 3:
                    safe = checkwithoutalevel(numbers)
                    break
                if increasing and numbers[i] > numbers[i+1]:
                    safe = checkwithoutalevel(numbers)
                    break
                if decreasing and numbers[i] < numbers[i+1]:
                    safe = checkwithoutalevel(numbers)
                    break
                if numbers[i] == numbers[i+1]:
                    safe = checkwithoutalevel(numbers)
                    break
            if safe: 
                print(numbers, 'is SAFE!')
                safereports += 1
            else:
                print(numbers, 'NoT')
        return safereports        

def checkwithoutalevel(numbers):
    for i  in range (0,len(numbers)):
        newnumbers = numbers.copy()
        newnumbers.pop(i)
        decreasing = False
        increasing = False
        safe = True
        if newnumbers[0] < newnumbers[1]:
            increasing = True
        elif newnumbers[1] < newnumbers[0]:
            decreasing = True
        else:
            continue
        for i in range(0,len(newnumbers)-1):
            if abs(newnumbers[i]-newnumbers[i+1]) > 3:
                safe = False
                break
            if increasing and newnumbers[i] > newnumbers[i+1]:
                safe = False
                break
            if decreasing and newnumbers[i] < newnumbers[i+1]:
                safe = False
                break
            if newnumbers[i] == newnumbers[i+1]:
                safe = False
                break
        if safe == False:
            continue
        else:
            return True
    return False

print(solution('inputs/2024-2.txt'))
                