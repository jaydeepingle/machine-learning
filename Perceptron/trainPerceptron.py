import os
import string
import random
from collections import Counter
class TrainPerceptron(object):
    @staticmethod
    def train(trainData, eta, iterations, stopFile=None):
        spamList = [] # list of dictionaries for spam
        hamList = [] # list of dictionaries for ham
        weightVector = {}
        flag = 0

        vocab = TrainPerceptron.preProcessing(trainData)
        if(stopFile != None):
            flag = 1
            stopwords = TrainPerceptron.readStopWords(stopFile)

        # to handle stop words
        if flag == 1:
            vocab = [x for x in vocab if x not in stopwords]

        for word in vocab:
        	weightVector[word] = random.uniform(0, 1)
        
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
                    	spamList.append(wordCount)
                    else:
                		hamList.append(wordCount)
            i += 1
        
        for i in range(iterations):
	        identifier = 0   	
	        for item in spamList:
	        	o = TrainPerceptron.getPrediction(item, weightVector)
	        	wordList = list(item)
	        	for word in wordList:
	    			weightVector[word] = float(eta) * (identifier - o) * item[word]

	    	identifier = 1
	    	for item in hamList:
	    		o = TrainPerceptron.getPrediction(item, weightVector)
	        	wordList = list(item)
	        	for word in wordList:
	    			weightVector[word] = float(eta) * (identifier - o) * item[word]
        return weightVector

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
    def getPrediction(wordCount, weightVector):
    	sum = 0
    	wordList = list(wordCount)
    	for word in wordList:
    		sum = sum + (weightVector[word] * wordCount[word])
    	if sum >= 0:
    		return 1
    	else:
    		return 0
        return None

    @staticmethod
    def preProcessing(trainData):
        vocabulary = []
        countDocsInClass = []
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