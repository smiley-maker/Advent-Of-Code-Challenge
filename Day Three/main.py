import pandas as pd
import numpy as np

def getPriority(df):
    letters = []
    lets = []
    for i in df[0]:
        newEntry1 = i[0:(len(i)//2)]
        newEntry2 = i[(len(i)//2):]
        lets += list(set([j for j in newEntry1 for k in newEntry2 if j==k]))
        print(lets)
    points = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
            "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T":46, "U":47, "V":48, "W":49, "X":50,"Y":51, "Z":52}
    values = list(map(points.get, lets))
    print(values)
    total = sum(values)
    print(total)
    return total

def getBadge(df):
    letters = []
    for i, g in df.groupby(np.arange(len(df)) // 3):
        newDF = pd.DataFrame(g)
        lists = newDF.values
        string1 = lists[0][0].strip()
        string2 = lists[1][0].strip()
        string3 = lists[2][0].strip()
        letters += list(set([x for x in string1 for y in string2 for z in string3 if z==y and y==x]))

    points = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26,
            "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T":46, "U":47, "V":48, "W":49, "X":50,"Y":51, "Z":52}
    values = list(map(points.get, letters))
    print(values)
    total = sum(values)
    print(total)
    return total


df = pd.read_csv("..\Advent-of-Code\Day Three\data.csv", lineterminator="\r", header=None)
#getPriority(df)
getBadge(df)