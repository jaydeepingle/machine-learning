import sys
import os
import re
from trainMultiNB import Train
from applyMultiNB import Apply 
from condProb import CondProb
import string

def process(self):
	return 0

if __name__ == '__main__':
	if(len(sys.argv) != 5):
		print "Enter correct number of arguments"
		sys.exit()
	c = 2
	d = [sys.argv[1] + "/spam/", sys.argv[1] + "/ham/"]
	td = [sys.argv[2] + "/spam/", sys.argv[2] + "/ham/"]
	
	if(sys.argv[4].lower() == "yes"):
		v, prior, spamCondProbDict, hamCondProbDict = Train.trainMultinomialNB(c, d, sys.argv[3])

	else:	
		v, prior, spamCondProbDict, hamCondProbDict = Train.trainMultinomialNB(c, d)
		
	spamCount, hamCount = len(os.listdir(td[0])), len(os.listdir(td[1])) 
	spam, ham = 0, 0
	pred = 0
	totalCount = spamCount + hamCount

	for i in range(len(td)):
		vocab = []
		dlist = os.listdir(td[i])
		for j in range (len(dlist)):
			filePath = td[i] + dlist[j]
			with open(filePath,'r') as f:
				for line in f:
					line = line.translate(None, string.punctuation)
					for word in line.split():
						vocab.append(word)  	
			index = Apply.applyMultinomialNB(c, v, prior, spamCondProbDict, hamCondProbDict, vocab)
			if(index == i):
				pred = pred + 1
		break
	print "Accuracy: ", (pred * 100) / float(totalCount)