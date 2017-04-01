import math
class Entropy(object):
	# entropy calculation
	@classmethod
	def calcEntropy(self, datasetMatrix, columnIndex, value, classColumnIndex):
		zeroCount, oneCount = 0, 0

		for i in range (len(datasetMatrix)):
			if(datasetMatrix[i][columnIndex] == value):
				if(datasetMatrix[i][classColumnIndex] == 0):
					zeroCount = zeroCount + 1
				else:
					oneCount = oneCount + 1
		total = zeroCount + oneCount

		term1, term2 = 0, 0
		if(zeroCount == 0):
			term1 = 0
		else:
			term1 = (zeroCount / float(total)) * math.log(zeroCount / float(total), 2)
		if(oneCount == 0):
			term2 = 0
		else:
			term2 = (oneCount / float(total)) * math.log(oneCount / float(total), 2)
		return -(term1 + term2)

	# initial entropy calculation
	@classmethod
	def calcInitialEntropy(self, datasetMatrix, classColumnIndex):
		zeroCount, oneCount = 0, 0
		for i in range (len(datasetMatrix)):
			if(datasetMatrix[i][classColumnIndex] == 0):
				zeroCount = zeroCount + 1
			else:
				oneCount = oneCount + 1
		total = zeroCount + oneCount

		term1, term2 = 0, 0
		if(zeroCount == 0):
			term1 = 0
		else:
			term1 = (zeroCount / float(total)) * math.log(zeroCount / float(total), 2)
		if(oneCount == 0):
			term2 = 0
		else:
			term2 = (oneCount / float(total)) * math.log(oneCount / float(total), 2)
		return -(term1 + term2)

	# gain calculation
	@classmethod
	def calcGain(self, datasetMatrix, entropy, columnIndex, classColumnIndex):
		zeroCount, oneCount = 0, 0
		for i in range(len(datasetMatrix)):
			if(datasetMatrix[i][columnIndex] == 0):
				zeroCount = zeroCount + 1
			else:
				oneCount = oneCount + 1
		total = zeroCount + oneCount
		term1 = (zeroCount / float(total) * self.calcEntropy(datasetMatrix, columnIndex, 0, classColumnIndex))
		term2 = (oneCount / float(total) * self.calcEntropy(datasetMatrix, columnIndex, 1, classColumnIndex))
		gain = entropy - term1 - term2
		return gain
