print(sum(len(s[:-1]) - len(eval(s)) for s in open('2015/input8.txt')))