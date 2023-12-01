def parseinput(url: str):
    f = open(url, encoding="utf-8")
    lines = f.readlines()
    newlines = []
    for line in lines:
        line = line.strip()
        newlines.append(line)
    return newlines
