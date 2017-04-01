import os
import string
from collections import Counter
class TestPerceptron(object):
    @staticmethod
    def test(testData, weightVector):
        spamList = []  # list of dictionaries for spam
        hamList = []  # list of dictionaries for ham
        i = 0
        for folder in testData:
            dirList = os.listdir(folder)
            for file in dirList:
                wordCount = Counter()
                filePath = folder + file
                with open(filePath,'r') as f:
                    for line in f:
                        line = line.translate(None, string.punctuation)
                        for word in line.split():
                            temp = word.lower()
                            wordCount[temp] += 1
                    if(i == 0):
                        spamList.append(wordCount)
                    else:
                        hamList.append(wordCount)
            i += 1

        totalCount = len(spamList) + len(hamList)
        value = 0

        identifier = 0
        for item in spamList:
            o = TestPerceptron.getPrediction(item, weightVector)
            if(o == 0):
                value += 1

        identifier = 1
        for item in hamList:
            o = TestPerceptron.getPrediction(item, weightVector)
            if(o == 1):
                value += 1

        return ((value * 100 )/ float(totalCount))

    @staticmethod
    def getPrediction(wordCount, weightVector):
        sum = 0
        wordList = list(wordCount)
        for word in wordList:
            if word in weightVector:
                sum = sum + (weightVector[word] * wordCount[word])
        if sum >= 0:
            return 1
        else:
            return 0
        return None
