#It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
#It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
#It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

f = open("./day5.py/INPUT.txt")
lines = f.readlines()
badchars = {"ab", "cd", "pq", "xy"}
vowels = {"a", "i", "o", "u", "e"}
nicestring = 0

for string in lines:
    string = string.rstrip()
    res = any(badduo in string for badduo in badchars)
    if res == True:
        continue
    count = 0
    doubleflag = 0
    buffer = "2"
    for char in string:
        if char == buffer:
            doubleflag = 1
        if char in vowels:
            count += 1
        buffer = char
    if count < 3:
        continue
    if doubleflag == 0:
        continue
    nicestring += 1

print(nicestring)