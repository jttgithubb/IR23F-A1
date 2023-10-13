import sys
from PartA import tokenize, computeWordFrequencies


def intersection(textFile1, textFile2):
    intersectCount = 0
    file1Dict = computeWordFrequencies(tokenize(textFile1))
    file2Dict = computeWordFrequencies(tokenize(textFile2))
    for token in file1Dict:
        if token in file2Dict:
            intersectCount += 1
    
    return intersectCount


if __name__ == '__main__':
    print(intersection(sys.argv[1], sys.argv[2]))