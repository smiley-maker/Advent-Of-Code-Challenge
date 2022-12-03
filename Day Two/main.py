import pandas as pd

#Part One
def getScore(key):
    oppMoves = key[0]
    myMoves = key[1]
    score = 0
    rock = 1
    paper = 2
    scissors = 3
    for i in range(len(key)):
        if oppMoves[i] == "A":
            if myMoves[i] == "Y":
                score += (paper + 6)
                continue
            elif myMoves[i] == "X":
                score += (rock + 3)
                continue
            elif myMoves[i] == "Z":
                score += scissors
                continue
            continue
        elif oppMoves[i] == "B":
            if myMoves[i] == "Z":
                score += (scissors + 6)
                continue
            elif myMoves[i] == "Y":
                score += (paper + 3)
                continue
            elif myMoves[i] == "X":
                score += rock
                continue
            continue
        elif oppMoves[i] == "C":
            if myMoves[i] == "X":
                score += (rock + 6)
                continue
            elif myMoves[i] == "Z":
                score += (scissors + 3)
                continue
            elif myMoves[i] == "Y":
                score += paper
                continue
            continue
    print(score)
    return score


#Part Two
def calcNewScore(key):
    oppMoves = key[0]
    myMoves = key[1]
    score = 0
    rock = 1
    paper = 2
    scissors = 3
    for i in range(len(key)):
        if myMoves[i] == "X":
            if oppMoves[i] == "A":
                score += scissors
                continue
            elif oppMoves[i] == "B":
                score += rock
                continue
            elif oppMoves[i] == "C":
                score += paper
                continue
        elif myMoves[i] == "Y":
            if oppMoves[i] == "A":
                score += (3 + rock)
                continue
            elif oppMoves[i] == "B":
                score += (3+paper)
                continue
            elif oppMoves[i] == "C":
                score += (3 + scissors)
                continue
        elif myMoves[i] == "Z":
            if oppMoves[i] == "A":
                score += (6+paper)
                continue
            elif oppMoves[i] == "B":
                score += (6 + scissors)
                continue
            elif oppMoves[i] == "C":
                score += (6 + rock)
                continue
    print(score)
    return score



df = pd.read_csv("..\Advent-of-Code\Day Two\data.csv", sep=" ", header=None)
#getScore(df)
calcNewScore(df)