# import modules
import csv, math, copy, sys

# class to store nodes of the tree
class Node(object):
	columnNames = None
	label = ""
	level = 0
	value = ""
	leaf = None
	label = None
	decision = None
	children = []
	sam = None

	def __init__(self, columnNames=[], leaf=False, label="", decision=0, children=[]):
		self.columnNames = columnNames
		self.leaf = False
		self.label = ""
		self.decision = 0
		self.children = []

# selecting the best attribute to split on
def selectBestAttribute(examples, targetAttribute, attributes, kind):
	gain = []
	# calculating gain of first (n - 1) columns
	if(kind == "entropy"):
		kindValue = calcInitialEntropy(examples, targetAttribute)
		for i in range (len(examples[0]) - 1):
			gain.append(calcGain(copy.deepcopy(examples), kindValue, i, targetAttribute))
	if(kind == "variance"):
		kindValue = calcInitialVariance(examples, targetAttribute)
		for i in range (len(examples[0]) - 1):
			gain.append(calcVarianceGain(copy.deepcopy(examples), kindValue, i, targetAttribute))
	index = gain.index(max(gain))
	return index

# algorithm to build decision tree
def id3(examples, targetAttribute, attributes, level, kind):
	root = Node(attributes)
	root.level = level
	# print ""
	columnData = zip(*examples)
	columnData = list(columnData.pop(len(columnData) - 1))
	countZero = columnData.count(0)
	countOne = columnData.count(1)
	if(countZero == 0):
		root.level = level
		root.label = 1
		root.leaf = True
		root.value = 1
		root.sam = 1
		return root
	elif(countOne == 0):
		root.level = level
		root.label = 0
		root.leaf = True
		root.value = 0
		root.sam = 0
		return root
	else:
		if(len(examples[0]) <= 1):
			if(countOne > countZero):
				root.level = level
				root.leaf = True
				root.label = 1
				root.value = 1
				root.sam = 1
			else:
				root.level = level
				root.leaf = True
				root.label = 0
				root.value = 0
				root.sam = 0
			return root
		else:
			index = selectBestAttribute(copy.deepcopy(examples), targetAttribute, copy.deepcopy(attributes), kind)
			root.attribute = index

			if(len(attributes) > index):
				root.decision = dictionary[attributes[index]]
				root.label = attributes[index]
				root.level = level
				attributes.pop(index)
			examplesZero, examplesOne = [], []

			for i in range(len(examples)):
				if(examples[i][index] == 0):
					examplesZero.append(examples[i])
				else:
					examplesOne.append(examples[i])

			# zero
			if(not examplesZero):
				leaf = Node(attributes)
				if(countZero > countOne):
					leaf.label = 0
					leaf.level = level
					leaf.leaf = True
					leaf.value = 0
					leaf.sam = 0
					root.children.append(leaf)
				else:
					leaf.label = 1
					leaf.level = level
					leaf.leaf = True
					leaf.value = 0
					leaf.sam = 0
					root.children.append(leaf)
			else:
				newExample = zip(*examplesZero)
				dummy = newExample.pop(index)
				examplesZero = zip(*newExample)
				element = id3(copy.deepcopy(examplesZero), targetAttribute - 1, copy.deepcopy(attributes), level + 1, kind)
				root.children.append(element)
				root.children[root.children.index(element)].sam = 0
			# one
			if(not examplesOne):
				leaf = Node(attributes)
				if(countZero > countOne):
					leaf.label = 0
					leaf.level = level
					leaf.leaf = True
					leaf.value = 0
					leaf.sam = 0
					root.children.append(leaf)
				else:
					leaf.label = 1
					leaf.level = level
					leaf.leaf = True
					leaf.value = 1
					leaf.sam = 1
					root.children.append(leaf)
			else:
				newExample = zip(*examplesOne)
				dummy = newExample.pop(index)
				examplesOne = zip(*newExample)
				# root.value = 1
				element = id3(copy.deepcopy(examplesOne), targetAttribute - 1, copy.deepcopy(attributes), level + 1, kind)
				root.children.append(element)
				root.children[root.children.index(element)].sam = 1
	return root

# read data from csv
def readDataMatrix(path):
	datafile = open(path, 'r')
	datareader = csv.reader(datafile, delimiter=';')
	data = []
	count = 0

	# read csv file into columns
	for row in datareader:
	    if(count != 0):
	    	dataRow = map(int, row[0].split(','))
	    	data.append(dataRow)
	    else:
	    	dataRow = map(str, row[0].split(','))
	    	data.append(dataRow)
	    count = count + 1
	return data

# entropy calculation
def calcEntropy(datasetMatrix, columnIndex, value, classColumnIndex):
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

# variance calculation
def calcVariance(datasetMatrix, columnIndex, value, classColumnIndex):
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


# initial entropy calculation
def calcInitialEntropy(datasetMatrix, classColumnIndex):
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

# initial variance calculation
def calcInitialVariance(datasetMatrix, classColumnIndex):
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

# gain calculation
def calcGain(datasetMatrix, entropy, columnIndex, classColumnIndex):
	zeroCount, oneCount = 0, 0
	for i in range(len(datasetMatrix)):
		if(datasetMatrix[i][columnIndex] == 0):
			zeroCount = zeroCount + 1
		else:
			oneCount = oneCount + 1
	total = zeroCount + oneCount
	term1 = (zeroCount / float(total) * calcEntropy(datasetMatrix, columnIndex, 0, classColumnIndex))
	term2 = (oneCount / float(total) * calcEntropy(datasetMatrix, columnIndex, 1, classColumnIndex))
	gain = entropy - term1 - term2
	return gain

# variance gain calculation
def calcVarianceGain(datasetMatrix, entropy, columnIndex, classColumnIndex):
	zeroCount, oneCount = 0, 0
	for i in range(len(datasetMatrix)):
		if(datasetMatrix[i][columnIndex] == 0):
			zeroCount = zeroCount + 1
		else:
			oneCount = oneCount + 1
	total = zeroCount + oneCount
	term1 = (zeroCount / float(total) * calcVariance(datasetMatrix, columnIndex, 0, classColumnIndex))
	term2 = (oneCount / float(total) * calcVariance(datasetMatrix, columnIndex, 1, classColumnIndex))
	gain = entropy - term1 - term2
	return gain

# accuracy calculation
def calculateAccuracy(datasetMatrix, root):
	count = 0
	for i in range(len(datasetMatrix)):
		predictionValue = getPrediction(datasetMatrix[i], root)
		if(predictionValue == datasetMatrix[i][len(datasetMatrix[i]) - 1]):
			count = count + 1
	return (count * 100 / float(len(datasetMatrix)))

def getPrediction(row, root):
	if root.leaf:
	 	return root.value
	else:
		return getPrediction(row, root.children[row[root.decision]])

# print data in a given list - dataset
def printData(dataset):
	print "Printing Dataset: "
	for i in range(len(dataset)):
		print dataset[i]

# flow
if(len(sys.argv) != 4):
	print "Please provide correct number of arguments"
	sys.exit()
trainingDatasetMatrix = readDataMatrix(sys.argv[1])
testDatasetMatrix = readDataMatrix(sys.argv[2])
classColumnIndex = len(trainingDatasetMatrix[0]) - 1
attributes = trainingDatasetMatrix.pop(0)
attributes.pop(len(attributes) - 1)
dictionary = {}

indices = []
for i in range (len(attributes)):
	indices.append(i)
	dictionary[attributes[i]] = i

entropyRoot = Node()
varianceRoot = Node()
entropyRoot = id3(trainingDatasetMatrix, classColumnIndex, copy.deepcopy(attributes), 0, "entropy")
varianceRoot = id3(trainingDatasetMatrix, classColumnIndex, copy.deepcopy(attributes), 0, "variance")

def printTree(temp, root, i):
	if(temp == "none"):
		pass
	else:
		if(root.leaf == True):
			print temp, "=", root.sam, ":", root.label
		else:
			print temp, "=", root.sam, ":"
	for i in range(len(root.children)):
		printTree((root.level * "| ") + root.label, root.children[i], i + 1)

arg = sys.argv[3].lower()
testDatasetMatrix.pop(0)
entropyAcc = calculateAccuracy(testDatasetMatrix, entropyRoot)
if(arg == "yes"):
	printTree("none", entropyRoot, 0)
	print "Information Gain Heuristic Accuracy: ", entropyAcc

varianceAcc = calculateAccuracy(testDatasetMatrix, varianceRoot)
if(arg == "yes"):
 	printTree("none", varianceRoot, 0)
	print "Variance Impurity Heuristic Accuracy: ", varianceAcc

target = open("accuracy.txt", "w")
target.write("Information Gain Heuristic Accuracy: " + str(entropyAcc))
target.write("\n")
target.write("Variance Impurity Heuristic Accuracy: " + str(varianceAcc))
target.write("\n")
