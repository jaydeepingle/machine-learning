from condProb import CondProb
import os
import re
import string  

class Train(object):
	@staticmethod
	def preProcessing(d):
		extractVocabulary = []
		countDocs = 0
		countDocsInClass = []
		concatenateTextOfAllDocsInClass = []
		for i in range (len(d)):
			concatenateTextOfAllDocsInClass.append([])
			dlist = os.listdir(d[i])
			countDocsInClass.append(len(dlist))
			countDocs = countDocs + len(dlist)
			for j in range (countDocsInClass[i]):
				filePath = d[i] + dlist[j]
				with open(filePath,'r') as f:
					for line in f:
						line = line.translate(None, string.punctuation)
						for word in line.split():

							concatenateTextOfAllDocsInClass[i].append(word.lower())
							extractVocabulary.append(word.lower())

		extractVocabulary = list(set(extractVocabulary))
		extractVocabulary.sort()
		return extractVocabulary, countDocs, countDocsInClass, concatenateTextOfAllDocsInClass

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
	def trainMultinomialNB(c, d, stopFile=None):
		# to handle stop words
		flag = 0
		stopwords = []
		if(stopFile != None):
			flag = 1
			stopwords = Train.readStopWords(stopFile)
		
		extractVocabulary, countDocs, countDocsInClass, concatenateTextOfAllDocsInClass = Train.preProcessing(d);
		extractVocabularyLength = len(extractVocabulary)
		
		# to handle stop words
		if flag == 1:
			extractVocabulary = [x for x in vocab if x not in stopwords]
		
		spamVocabCountDict = {}
		hamVocabCountDict = {}
		vocabCountDict, denominator, condProbDict, prior = {}, 0, {}, []
		spamCondProbDict, hamCondProbDict = {}, {}
		for i in range (c):
			nc = countDocsInClass[i]
			prior.append(nc / float(countDocs)) # prior calculation
			textc = concatenateTextOfAllDocsInClass[i]
			
			# to handle stop words
			if flag == 1:
				textc = [x for x in textc if x not in stopwords]
			
			denominator = 0
			for j in range (extractVocabularyLength):
				if(i == 0):
					tct = textc.count(extractVocabulary[j])
					spamVocabCountDict[extractVocabulary[j]] = tct
					denominator = denominator + tct + 1
				else:
					tct = textc.count(extractVocabulary[j])
					hamVocabCountDict[extractVocabulary[j]] = tct
					denominator = denominator + tct + 1

			for k in range (extractVocabularyLength):
				if(i == 0):
					temp = (spamVocabCountDict[extractVocabulary[k]] + 1) / float(denominator)
					spamCondProbDict[str(extractVocabulary[k])] = temp
				else:
					temp = (hamVocabCountDict[extractVocabulary[k]] + 1) / float(denominator)
					hamCondProbDict[str(extractVocabulary[k])] = temp

		return extractVocabulary, prior, spamCondProbDict, hamCondProbDict