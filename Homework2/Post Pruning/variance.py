class Variance(object):
	# variance calculation
	@classmethod
	def calcVariance(self, datasetMatrix, columnIndex, value, classColumnIndex):
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
			term1 = (zeroCount / float(total))
		if(oneCount == 0):
			term2 = 0
		else:
			term2 = (oneCount / float(total))
		return (term1 * term2)

	# initial variance calculation
	@classmethod
	def calcInitialVariance(self, datasetMatrix, classColumnIndex):
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
			term1 = (zeroCount / float(total))
		if(oneCount == 0):
			term2 = 0
		else:
			term2 = oneCount / float(total)
		return (term1 * term2)

	# variance gain calculation
	@classmethod
	def calcVarianceGain(self, datasetMatrix, entropy, columnIndex, classColumnIndex):
		zeroCount, oneCount = 0, 0
		for i in range(len(datasetMatrix)):
			if(datasetMatrix[i][columnIndex] == 0):
				zeroCount = zeroCount + 1
			else:
				oneCount = oneCount + 1
		total = zeroCount + oneCount
		term1 = (zeroCount / float(total) * self.calcVariance(datasetMatrix, columnIndex, 0, classColumnIndex))
		term2 = (oneCount / float(total) * self.calcVariance(datasetMatrix, columnIndex, 1, classColumnIndex))
		gain = entropy - term1 - term2
		return gain