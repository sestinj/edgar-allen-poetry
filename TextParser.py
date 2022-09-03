def stringToDict(string):
    #Parse text
    letters = "abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'"
    string = string + " "
    words = {}
    currentWord = ""
    wordIsStarted = False
    for i in range(0, len(string)):
        character = string[i]
        if character in letters:
            wordIsStarted = True
            currentWord += character
        else:
            if wordIsStarted:
                if currentWord in words:
                    words[currentWord] += 1
                else:
                    words[currentWord] = 1
                currentWord = ""
            wordIsStarted = False

    return sortDictReverse(words)

def stringToList(string):
    letters = "abcdefghijklmnopqrstuvwzyzABCDEFGHIJKLMNOPQRSTUVWXYZ-',"
    string = string + " "
    words = []
    currentWord = ""
    wordIsStarted = False
    for i in range(0, len(string)):
        character = string[i]
        if character in letters:
            wordIsStarted = True
            currentWord += character
        elif character == ".":
            if wordIsStarted:
                words.append(currentWord)
            words.append(".")
            currentWord = ""
            wordIsStarted = False
        else:
            if wordIsStarted:
                words.append(currentWord)
                currentWord = ""
            wordIsStarted = False

    return words
            
                


def sortDictReverse(dictionary):
    
    #Sort dictionary in reverse number order
    newDict = {}
    for i in range(0, len(sorted(dictionary.values()))):
        for key in dictionary.keys():
            if dictionary[key] == sorted(dictionary.values())[len(sorted(dictionary.values())) - i - 1]:
                newDict[key] = sorted(dictionary.values())[len(sorted(dictionary.values())) - i - 1]
    
    return newDict

def combineDix(dict1, dict2):
    #This adds together two dictionaries whose values are integers
    for key, value in dict1.items():
        if key in dict2.keys():
            dict2[key] += value
        else:
            dict2[key] = value

    return sortDictReverse(dict2)

def sentenceBreakdown(sentence):
    words = stringToList(sentence)
    for i in range(0, len(words)):
        if words[i].isNoun:
            if words[i + 1].isVerb:
                noun = words[i]
