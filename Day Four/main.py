import pandas as pd

def preprocess(data):
    for x in range(len(data[0])):
        data[0][x] = data[0][x].replace("\r", "")
        data[0][x] = data[0][x].split("-")
        data[0][x][0] = int(data[0][x][0])
        data[0][x][1] = int(data[0][x][1])
        data[1][x] = data[1][x].replace("\r", "")
        data[1][x] = data[1][x].split("-")
        data[1][x][0] = int(data[1][x][0])
        data[1][x][1] = int(data[1][x][1])    

def findOverlap(data):
    num = 0

    preprocess(data)

    for i in range(len(data[0])):
        L1 = data[0][i][0]
        H1 = data[0][i][1]
        L2 = data[1][i][0]
        H2 = data[1][i][1]

        if L1 >= L2 and H1 <= H2 or L2 >= L1 and H2 <= H1:
            num = num + 1

    print(num)
    return num

def partialOverlap(data):
    num = 0

    preprocess(data)

    for i in range(len(data[0])):
        L1 = data[0][i][0]
        H1 = data[0][i][1]
        L2 = data[1][i][0]
        H2 = data[1][i][1]

        if L1 in range(L2, H2+1, 1):
            num = num + 1
            continue
        if H1 in range(L2, H2+1, 1):
            num = num + 1
            continue
        if L2 in range(L1, H1+1, 1):
            num = num + 1
            continue
        if H2 in range(L1, H1+1, 1):
            num = num + 1
            continue
    
    print(num)
    return num

df = pd.read_csv("Day Four\data.csv", lineterminator="\n", header=None)
#findOverlap(df)
partialOverlap(df)