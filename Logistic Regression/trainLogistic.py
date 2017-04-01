import os
import string
import random
import math
from collections import Counter
import numpy
class TrainLogistic(object):
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
    def train(trainData, eta, lambdaVar, iterations, stopFile=None):
        vocab, convergence, spamDict, hamDict, spamList, hamList = [], 0, {}, {}, [], []
        flag = 0
        if(stopFile != None):
            flag = 1
            stopwords = TrainLogistic.readStopWords(stopFile)

        vocab = TrainLogistic.preProcessing(trainData)
        
        # to handle stop words
        if flag == 1:
            vocab = [x for x in vocab if x not in stopwords]

        spamList, hamList, spamFileList, hamFileList, totalFileList, spamDict, hamDict = TrainLogistic.returnData(trainData, vocab)
        totalDict = dict(spamDict.items() + hamDict.items())

        n = len(vocab)
        m = len(spamList) + len(hamList)

        data = TrainLogistic.initializeData(len(totalFileList), len(vocab))
        data = TrainLogistic.insertData(totalFileList, vocab, totalDict, data)
        pr = []
        w = []

        for i in range(m):
            pr.append(random.randint(0, 1))
        for i in range(n + 1):
            w.append(random.randint(0, 1))

        m = len(totalFileList)

        vocabDict = {}

        while(convergence < iterations):
            for i in range(len(pr)):
                pr[i] = TrainLogistic.computeP(w, data[i])
            dw = [0] * (n + 1)
            for i in range(n + 1):
                for j in range(m):
                    dw[i] = dw[i] + data[j][i] * (data[j][n + 1] - pr[j])
            for i in range(n + 1):
                w[i] = w[i] + eta * (dw[i] - (lambdaVar * w[i]))
            convergence += 1
        return w, vocab