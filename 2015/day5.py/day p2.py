#It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

f = open("./day5.py/INPUT.txt")
lines = f.readlines()
nicestring = 0
doubles = set()
window = []

for string in lines:
    print("Checking string: ", string)
    tripleflag = 0
    doubleflag = 0
    window=[]
    doubles = set()
    string = string.rstrip()

    for char in string:
        if len(window) == 0:
            window.append(char)
            continue
        if len(window) == 1:
            window.append(char)
            doubles.add(window[0]+window[1])
            continue
        if len(window) == 2:    
            window.append(char)
            doubles.add(window[1]+window[2])
            if window[0] == window[2]:
                tripleflag = 1
            continue
        if len(window) == 3:
            window.append(char)
            window.pop(0)
            if window[0] == window[2]:
                tripleflag = 1
            if string.count(window[1]+window[2])>=2:
                    doubleflag = 1
            else:
                doubles.add(window[1]+window[2])
        if [doubleflag, tripleflag] == [1, 1]:
            nicestring += 1
            print(string)
            break
    
print(nicestring)
