import sys


# This allows me to declare my own function named 'print' whilst retaining the original print function.
originalPrint = print 


def tokenize(textFilePath):
    allTokensList = []
    with open(textFilePath, 'r', encoding = 'utf-8') as file:
        for line in file:
            lineString = line.strip()
            for character in lineString:
                if (not character.isalnum()):
                    lineString = lineString.replace(character, " ")
            lineString = lineString.lower()
            for word in lineString.split():
                allTokensList.append(word)

    return allTokensList


def computeWordFrequencies(tokenList):
    wordFreqDict = {}
    for token in tokenList:
        wordFreqDict.setdefault(token, 0)
        wordFreqDict[token] += 1

    return wordFreqDict


def print(wordFrequencyDict):
    for w, f in sorted(sorted(wordFrequencyDict.items()), key = lambda entry:  entry[1], reverse = True):
        originalPrint(w + "\t" + str(f))


if __name__ == '__main__':
    tkList = tokenize(sys.argv[1])
    wfDict = computeWordFrequencies(tkList)
    print(wfDict)

                
        

