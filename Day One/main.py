import pandas as pd
import numpy as np

def calculateCalories(key):
    calories = key[0]
    currentSum = 0
    maxVals = []
    totalSum = []
    
    for i in range(len(calories)):
#        print(calories[i])
        if calories[i] == "\r":
            totalSum.append(currentSum)
#            print("inside")
            currentSum = 0
        else:
            currentSum += int(calories[i])

    maxVals.append(np.max(totalSum))
    totalSum.pop(np.argmax(totalSum))
    maxVals.append(np.max(totalSum))
    totalSum.pop(np.argmax(totalSum))
    maxVals.append(np.max(totalSum))
    totalSum.pop(np.argmax(totalSum))

    print(np.sum(maxVals))
    return np.sum(maxVals)

df = pd.read_csv("..\Advent-of-Code\Day One\data.csv", lineterminator="\n", header=None)
calculateCalories(df)