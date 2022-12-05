import pandas as pd


def sort(data):
    dummyList = {}
    for i in range(len(data[0])):
        data[0][i] = data[0][i].replace("\r", "")
        data[0][i] = data[0][i].split(" ")
        dummyList[i] = [int(data[0][i][1]), int(data[0][i][3]), int(data[0][i][5])]
    return dummyList

def stacking(data):
    order = sort(data)
    letters = []
    boxes = {
        1: ["T", "R", "G", "W", "Q", "M", "F", "P"],
        2: ["R", "F", "H"],
        3: ["D", "S", "H", "G", "V", "R", "Z", "P"], 
        4: ["G", "W", "F", "B", "P", "H", "Q"],
        5: ["H", "J", "M", "S", "P"],
        6: ["L", "P", "R", "S", "H", "T", "Z", "M"],
        7: ["L", "M", "N", "H", "T", "P"],
        8: ["R", "Q", "D", "F"],
        9: ["H", "P", "L", "N", "C", "S", "D"]
    }

    for nums in order.items():
        amount = nums[1][0]
        current = nums[1][1]
        newSpot = nums[1][2]

        for i in range(1, amount+1, 1):
            x = boxes[current].pop(0)
            boxes[newSpot].insert(0, x)

    letters = "".join([boxes[i][0] for i in range(1, len(boxes)+1, 1)])
    print(letters)
    return letters

def stackMultiple(data):
    order = sort(data)
    letters = []
    a = []
    boxes = {
        1: ["T", "R", "G", "W", "Q", "M", "F", "P"],
        2: ["R", "F", "H"],
        3: ["D", "S", "H", "G", "V", "R", "Z", "P"], 
        4: ["G", "W", "F", "B", "P", "H", "Q"],
        5: ["H", "J", "M", "S", "P"],
        6: ["L", "P", "R", "S", "H", "T", "Z", "M"],
        7: ["L", "M", "N", "H", "T", "P"],
        8: ["R", "Q", "D", "F"],
        9: ["H", "P", "L", "N", "C", "S", "D"]
    }

    for nums in order.items():
        amount = nums[1][0] 
        current = nums[1][1] 
        newSpot = nums[1][2] 

        for i in range(1, amount+1, 1):
            p = boxes[current].pop(0)
            a.append(p)

        boxes[newSpot] = a + boxes[newSpot]
        a = []

    letters = "".join([boxes[i][0] for i in range(1, len(boxes)+1, 1)])
    print(letters)
    return letters


df = pd.read_csv("Day Five\data.csv", lineterminator="\n", header=None)
stackMultiple(df)