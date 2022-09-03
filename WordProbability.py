#Currently using data structure #1, as shown on back of Chapter 9 AP Bio notes
import io

##textFile = io.open("confederacy_of_dunces.txt", "r", encoding="utf-8")
textFile = open("confederacy_of_dunces.txt", "r", -1, "utf-8", "ignore")
fileString = textFile.read()
textFile.close()


import random

from TextParser import *

masterDict = {}

wordsList = stringToList(str(fileString))


# n = 4 (take three words after into account)

number = 6

def listToMasterDict(wordsList):
    for i in range(len(wordsList)):
        if not wordsList[i] in masterDict:
            masterDict[wordsList[i]] = []
            for k in range(0, number):
                masterDict[wordsList[i]].append({})
        for n in range(0, number):
            if len(wordsList) > i + n + 1:
                subDict = masterDict[wordsList[i]][n]
                if wordsList[i + n + 1] in subDict:
                    subDict[wordsList[i+n+1]] += 1
                else:
                    subDict[wordsList[i+n+1]] = 1
                if "#" in masterDict[wordsList[i]][n]:
                    masterDict[wordsList[i]][n]["#"] += 1
                else:
                    masterDict[wordsList[i]][n]["#"] = 1
 
listToMasterDict(wordsList)

##currentWord = "after"
##for i in range(35):
##    print(currentWord)
##    highest = 0
##    for key in masterDict[currentWord][0]:
##        if key in masterDict[currentWord][0] and key != "#":
##            if masterDict[currentWord][0][key] > highest:
##                highest = masterDict[currentWord][0][key]
##                currentWord = key
##    if highest == 0 or len(masterDict[currentWord][0]) < 2:
##        randomNum = random.randint(0, int(len(masterDict)))
##        count = 0
##        for key in masterDict:
##            if count == randomNum:
##                currentWord = key
##            count += 1
##print("""
##
##
##""")



currentWords = ["."]
for k in range(0, number - 1):
    currentWords.append("")
for i in range(40):
    print(currentWords[0])
    probTotal = 0.0
    done = False
    currentWord = currentWords[0]
    #go on until a word has been chosen(this is necessary because of the line below with the *)
    while currentWord == currentWords[0]:
        #go through all possible words that could come after the current word
        for key in masterDict[currentWords[0]][0]:
            # *only do choose a new word if not done, the # key wasn't chosen, and the key exists(it always should)
            if not done and key != "#" and key != currentWords[0]:
                #add up probabilities
                if currentWords[0] in masterDict:
                    prob = masterDict[currentWords[0]][0][key]/masterDict[currentWords[0]][0]["#"]
                for j in range(1, number):
                    if currentWords[j] in masterDict and key in masterDict[currentWords[j]][j]:
                        prob += (2^(-1*j))*(masterDict[currentWords[j]][j][key]/masterDict[currentWords[j]][j]["#"])
                #pick a random word(based on the probabilities)
                if random.randint(0, number * 1000)/1000 <= prob:
                    for k in range(0, number - 1):
                        if 3 - k >= 0 and 2-k >= 0 and 3 - k < len(currentWords) and 2-k< len(currentWords):
                            currentWords[3 - k] = currentWords[2 - k]
                    currentWords[0] = key
                    done = True
                probTotal += prob
