# UCInetId: tranjt7
# Author: Jonathan Tran


import sys
from PartA import tokenize, computeWordFrequencies


''' intersection Time Complexity: O(N^2)
    The intersection function below runs the computeWordFrequencies and tokenize functions once for each input file
    which is O(N) and O(N^2) time respectively. Afterwards, we iterate through the tokens of the the first input file
    and check if the second input contains the same tokens, incrementing along the way which runs in O(N) because of the for loop
    and counting and dictionary contains being constant operations. As a result, the time complexity can be described as 
    O(N^2 + N + N^2 + N + N) or more simply put O(N^2) because it dominates.
'''
def intersection(textFile1, textFile2):
    intersectCount = 0
    file1Dict = computeWordFrequencies(tokenize(textFile1))
    file2Dict = computeWordFrequencies(tokenize(textFile2))
    for token in file1Dict:
        if token in file2Dict:
            intersectCount += 1
    
    return intersectCount


if __name__ == '__main__':
    try:
        print(intersection(sys.argv[1], sys.argv[2]))
        
    except IndexError:
        print("Incorrect number of inputs.")