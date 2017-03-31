# import modules
import csv, math, copy, sys
from tree import Tree
from entropy import Entropy
from readData import ReadData
from variance import Variance
from node import Node
from postPruning import PostPruning

# selecting the best attribute to split on
def selectBestAttribute(examples, targetAttribute, attributes, kind):
	gain = []
	# calculating gain of first (n - 1) columns
	if(kind == "entropy"):
		kindValue = Entropy.calcInitialEntropy(examples, targetAttribute)
		for i in range (len(examples[0]) - 1):
			gain.append(Entropy.calcGain(copy.deepcopy(examples), kindValue, i, targetAttribute))
	if(kind == "variance"):
		kindValue = Variance.calcInitialVariance(examples, targetAttribute)
		for i in range (len(examples[0]) - 1):
			gain.append(Variance.calcVarianceGain(copy.deepcopy(examples), kindValue, i, targetAttribute))
	index = gain.index(max(gain))
	return index

# algorithm to build decision tree
def id3(examples, targetAttribute, attributes, level, kind, parent=None):
	root = Node(attributes)
	if(level == 0):
		root.parent = None
	else:
		root.parent = parent
	root.level = level
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
				element = id3(copy.deepcopy(examplesZero), targetAttribute - 1, copy.deepcopy(attributes), level + 1, kind, root)
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
				element = id3(copy.deepcopy(examplesOne), targetAttribute - 1, copy.deepcopy(attributes), level + 1, kind, root)
				root.children.append(element)
				root.children[root.children.index(element)].sam = 1
	return root

# flow
if __name__ == '__main__':
	if(len(sys.argv) != 7):
		print "Please provide correct number of arguments"
		sys.exit()
	trainingDatasetMatrix = ReadData.readDataMatrix(sys.argv[3])
	validationDatasetMatrix = ReadData.readDataMatrix(sys.argv[4])
	validationDatasetMatrix.pop(0);
	testDatasetMatrix = ReadData.readDataMatrix(sys.argv[5])
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
	
	entropyRoot = id3(trainingDatasetMatrix, classColumnIndex, copy.deepcopy(attributes), 0, "entropy", None)
	varianceRoot = id3(trainingDatasetMatrix, classColumnIndex, copy.deepcopy(attributes), 0, "variance", None)

	arg = sys.argv[6].lower()
	testDatasetMatrix.pop(0)
	
	entropyAcc = Tree.calculateAccuracy(testDatasetMatrix, entropyRoot)
	if(arg == "yes"):
		Tree.printTree("none", entropyRoot, 0)
		print "Information Gain Heuristic Accuracy: ", entropyAcc

	varianceAcc = Tree.calculateAccuracy(testDatasetMatrix, varianceRoot)
	if(arg == "yes"):
	 	Tree.printTree("none", varianceRoot, 0)
		print "Variance Impurity Heuristic Accuracy: ", varianceAcc

	target = open("accuracy.txt", "w")
	target.write("Information Gain Heuristic Accuracy: " + str(entropyAcc))
	target.write("\n")
	target.write("Variance Impurity Heuristic Accuracy: " + str(varianceAcc))
	target.write("\n")

	bestNode = PostPruning.postPruningAlgorithm(int(sys.argv[1]), int(sys.argv[2]), copy.deepcopy(entropyRoot), validationDatasetMatrix)
	if(arg == "yes"):
		print "Post Pruning Information Gain Heuristic Accuracy: ", Tree.calculateAccuracy(testDatasetMatrix, bestNode)
	target.write("Post Pruning Information Gain Heuristic Accuracy: " + str(Tree.calculateAccuracy(testDatasetMatrix, bestNode)) + "\n")

	bestNode = PostPruning.postPruningAlgorithm(int(sys.argv[1]), int(sys.argv[2]), copy.deepcopy(varianceRoot), validationDatasetMatrix)
	if(arg == "yes"):
		print "Post Pruning Variance Impurity Heuristic Accuracy: ", Tree.calculateAccuracy(testDatasetMatrix, bestNode)
	target.write("Post Pruning Variance Impurity Heuristic Accuracy: " + str(Tree.calculateAccuracy(testDatasetMatrix, bestNode)) + "\n")