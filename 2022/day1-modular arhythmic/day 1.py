## my solution
f = open("day1-modular arhythmic/input1.txt")
games = f.readlines()
score = 0
for game in games:
    game = game.rstrip()
    if game[2] == "X":
        if game[0] == "A":
            game = game.rstrip("X").join(" C")
        if game[0] == "B":
            game = game.rstrip("X").join(" A")
        if game[0] == "C":
            game = game.rstrip("X").join(" B")

    elif game[2] == "Y":
            game = game.rstrip("Y").join(" "+ game[0])
    else :
        if game[0] == "A":
            game = game.rstrip("Z").join(" B")
        if game[0] == "B":
            game = game.rstrip("Z").join(" C")
        if game[0] == "C":
            game = game.rstrip("Z").join(" A")
    game = game.lstrip()
    if game[0] == game[2]:
        score += 3
    if game[2]== "A":
        score += 1
        if game[0] == "C":
            score += 6
    if game[2]== "B":
        score += 2
        if game[0] == "A":
            score += 6
    if game[2]== "C":
        score += 3
        if game[0] == "B":
            score += 6
print(score)

## more elegant brute force solution with a lookup
newscore = 0
for game in games:
    game = game.rstrip()
    rules = {"A X": 4, "A Y": 8, "A Z": 3,
             "B X": 1, "B Y": 5, "B Z": 9,
             "C X": 7, "C Y": 2, "C Z": 6}
    newscore += rules[game]
print(newscore)

newscore = 0
for game in games:
    game = game.rstrip()
    rules = {"A X": 4, "A Y": 8, "A Z": 3,
             "B X": 1, "B Y": 5, "B Z": 9,
             "C X": 7, "C Y": 2, "C Z": 6}
    newscore += rules[game]
print(newscore)

## modular arythmetic
score = 0
for game in games:
    game = game.rstrip()
    opp, me = game.split(" ")
    opp = ord(opp) - ord("A")
    me = ord(me) - ord("X")
    eval = (me - opp)%3
    if eval == 0:
        score += 3;
    elif eval == 1:
        score += 6
    score += me + 1
print(score)
