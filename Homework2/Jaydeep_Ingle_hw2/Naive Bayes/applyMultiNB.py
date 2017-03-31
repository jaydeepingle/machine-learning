from condProb import CondProb
import math
class Apply(object):
	@staticmethod
	def extractTokensFromDoc(v, d):
		newArr = []
		for i in range(len(d)):
			if(d[i] in v):
				newArr.append(d[i])
		return newArr

	@staticmethod
	def applyMultinomialNB(c, v, prior, spamCondProbDict, hamCondProbDict, d):
		spamScore = 0
		hamScore = 0
		w = Apply.extractTokensFromDoc(v, d)
		for i in range (c):
			if(i == 0):
				spamScore = math.log(prior[i], 2)
			else:
				hamScore = math.log(prior[i], 2)
			for j in range(len(w)):
				if(i == 0):
					spamScore = spamScore + math.log(spamCondProbDict[str(w[j])], 2) # row 2 column # of words in vocab
				else:
					hamScore = spamScore + math.log(hamCondProbDict[str(w[j])], 2) # row 2 column # of words in vocab
		value = 0
		if(spamScore > hamScore):
			value = 0
		else:
			value = 1
		return value