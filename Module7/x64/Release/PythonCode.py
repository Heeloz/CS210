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

#loadData function loads the data from the localally saved file
def loadData():
    myfile = open(os.path.join(os.path.dirname(__file__), "items.txt"))
    return myfile

#coutNumberOfItems counts the number of occurrences of an item
def countNumberOfItems():
    myItems = generateDictionary()
    #Print out the contents of the myItems dictionary in a key: value format
    for item, count in myItems.items():
        print("{0}: {1}".format(item, count))


def findSpecificItem(itemToFind):
    #get the items
    items = generateDictionary()
    #return the itemToFind from the dictionary
    if(items.get(itemToFind) is not None):
        return items[itemToFind] 
    else:
        return -1

def generateDictionary():
    #load the data from the loadData function to the data name
    data = loadData()
    #create an empty dictionary to use later then loop through the data 
    myItems = {}
    for line in data:
        #there are newline characters in the string, so remove those 
        line = line.replace("\n", "")
        #check if the line is present in the dictionary. If not, create a new key:value pair and set the value to 1
        if(line not in myItems):
            myItems[line] = 1
        else: 
            #if the item is found in the dictionary, add 1 to the value
            myItems[line] += 1
    #return dictionary
    return myItems

def generateGraph():
    #Print myItems in a format that repeats the star character for the number "count"
    myItems = generateDictionary()
    for item, count in myItems.items():
        print("{0}: {1}".format(item, "*" * count))