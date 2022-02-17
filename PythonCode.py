import re
import string
import os 


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v


def loadData():
    myfile = open(os.path.join(os.path.dirname(__file__), "items.txt"))
    return myfile

def countNumberOfItems():
    data = loadData()
    myItems = {}
    for line in data:
        line = line.replace("\n", "")
        if(line not in myItems):
            myItems[line] = 1
        else: 
            myItems[line] += 1

    for item, count in myItems.items():
        print("{0}: {1}".format(item, count))


def findSpecificItem(itemToFind):
    data = loadData()
    itemCount = 0
    for line in data:
        line = line.replace("\n", "")
        if(line == itemToFind):
            itemCount += 1
    return itemCount


def generateGraph():
    data = loadData()
    myItems = {}
    for line in data:
        line = line.replace("\n", "")
        if(line not in myItems):
            myItems[line] = 1
        else: 
            myItems[line] += 1

    for item, count in myItems.items():
        print("{0}: {1}".format(item, "*" * count))