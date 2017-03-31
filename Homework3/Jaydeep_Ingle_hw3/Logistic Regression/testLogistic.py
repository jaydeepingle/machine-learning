import os
import string
import random
import math
from collections import Counter
import numpy
class TestLogistic(object):
    @staticmethod
    def preProcessing(trainData):
        vocabulary = []
        countDocsInClass = []
        weightVector = {}
        for i in range (len(trainData)):
            dirList = os.listdir(trainData[i])
            countDocsInClass.append(len(dirList))
            for j in range (countDocsInClass[i]):
                filePath = trainData[i] + dirList[j]
                with open(filePath,'r') as f:
                    for line in f:
                        line = line.translate(None, string.punctuation)
                        for word in line.split():
                            vocabulary.append(word.lower())
            vocabulary = list(set(vocabulary))
        vocabulary.sort()
        return vocabulary

    @staticmethod
    def returnData(trainData, vocab):
        spamList = []
        hamList = []
        spamFileList = []
        hamFileList = []
        totalFileList = []
        spamDict = {}
        hamDict = {}
        i = 0
        for folder in trainData:
            dirList = os.listdir(folder)
            for file in dirList:
                wordCount = Counter()
                filePath = folder + file
                with open(filePath,'r') as f:
                    for line in f:
                        line = line.translate(None, string.punctuation)
                        for word in line.split():
                            temp = word.lower()
                            if(temp in vocab):
                                wordCount[temp] += 1
                    if(i == 0):
                        spamDict[file] = wordCount
                        spamList.append(wordCount)
                        spamFileList.append(file)
                    else:
                        hamDict[file] = wordCount
                        hamList.append(wordCount)
                        hamFileList.append(file)
            i += 1
        totalFileList = spamFileList + hamFileList
        return spamList, hamList, spamFileList, hamFileList, totalFileList, spamDict, hamDict

    @staticmethod
    def readStopWords(stopFile):
        stopwords = []
        filePath = stopFile
        with open(filePath,'r') as f:
            for line in f:
                line = line.translate(None, string.punctuation)
                for word in line.split():
                    stopwords.append(word.lower())
        return stopwords

    @staticmethod
    def initializeData(m, n):
        data = []
        for i in range(m):
            row = []
            for j in range(n + 2):
                if(j == 0):
                    row.append(1)
                else:
                    row.append(0)
            data.append(row)
        return data

    @staticmethod
    def computeP(w, row):
        temp = w[0]
        for i in range(1, (len(row) - 1)):
            temp = temp + (w[i] * row[i])
        value = 0
        if(temp > 0):
            value = 1
        else:
            value = 0
        return value

    @staticmethod
    def insertData(totalFileList, vocabulary, totalDict, data):
        for i in range(len(totalFileList)):
            for j in range(1, len(data[0]) - 1):
                data[i][j] = totalDict[totalFileList[i]][vocabulary[j - 1]]
            if("spam" in totalFileList[i]):
                data[i][len(data[0]) - 1] = 0
            else:
                data[i][len(data[0]) - 1] = 1
        return data

    @staticmethod
    def test(testData, weightVector, vocabulary):
        vocab, convergence, spamDict, hamDict, spamList, hamList = [], 0, {}, {}, [], []
        vocab = TestLogistic.preProcessing(testData)
        spamList, hamList, spamFileList, hamFileList, totalFileList, spamDict, hamDict = TestLogistic.returnData(testData, vocab)
        totalDict = dict(spamDict.items() + hamDict.items())

        n = len(vocabulary)
        m = len(spamList) + len(hamList)

        data = TestLogistic.initializeData(len(totalFileList), len(vocabulary))
        data = TestLogistic.insertData(totalFileList, vocabulary, totalDict, data)

        count = 0
        for i in range (len(data)):
            temp = weightVector[0]
            for j in range (1, len(data[0]) - 11):
                temp = temp + (data[i][j] * weightVector[j])
            value = 0
            if(temp > 0):
                value = 1
            else:
                value = 0
            if(value == data[i][len(data[0]) - 1]):
                count += 1
        return ((count * 100) / float(len(data)))
