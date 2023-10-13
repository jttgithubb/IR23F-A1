import sys


# This allows me to declare my own function named 'print' whilst retaining the original print function.
originalPrint = print 


''' tokenize Time Complexity: O(N^2)
    The tokenize function below contains a main loop which iterates through each line of the file, two inner loops that process 
    the current line to either remove invalid characters or access the words in that line, and two string functions that process the 
    current line in O(n) time. Because the function only contains one main loop and the nested loops and functions that process the 
    current line, the time complexity of this function can be described as O(N(N + N + N + N)) or more simply put O(N^2).
'''
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


''' computeWordFrequencies Time Complexity: O(N)
    The computeWordFrequencies function below only comprises of a single loop that iterates through the list of tokens argument.
    Within the loop, tokens are added to the dictionary if not yet seen and their count value is incremented in constant time. Thus, 
    the time complexity of this function can be described as O(N(1 + 1)) or more simply put O(N).
'''
def computeWordFrequencies(tokenList):
    wordFreqDict = {}
    for token in tokenList:
        wordFreqDict.setdefault(token, 0)
        wordFreqDict[token] += 1

    return wordFreqDict


''' print Time Complexity: O(NlogN)
    The print function below comprises of two instances of sorting through the sorted function to create a descending frequency list 
    that is also alphabetical in order. Additionally, the final list is iterated to print the results to the console. Therefore, the time
    complexity of this function can be described as O(NlogN + NlogN + N) which can be simplified to O(NlogN). 
'''
def print(wordFrequencyDict):
    for w, f in sorted(sorted(wordFrequencyDict.items()), key = lambda entry:  entry[1], reverse = True):
        originalPrint(w + "\t" + str(f))


if __name__ == '__main__':
    tkList = tokenize(sys.argv[1])
    wfDict = computeWordFrequencies(tkList)
    print(wfDict)

                
        

