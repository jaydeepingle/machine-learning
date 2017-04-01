class Tree(object):
	# accuracy calculation
	@staticmethod
	def calculateAccuracy(datasetMatrix, root):
		count = 0
		for i in range(len(datasetMatrix)):
			predictionValue = Tree.getPrediction(datasetMatrix[i], root)
			if(predictionValue == datasetMatrix[i][len(datasetMatrix[i]) - 1]):
				count = count + 1
		return (count * 100 / float(len(datasetMatrix)))

	#get prediction
	@staticmethod
	def getPrediction(row, root):
		if root.leaf:
		 	return root.value
		else:
			return Tree.getPrediction(row, root.children[row[root.decision]])

	# print data in a given list - dataset
	@staticmethod
	def printData(dataset):
		print "Printing Dataset: "
		for i in range(len(dataset)):
			print dataset[i]

	# print tree
	@staticmethod
	def printTree(temp, root, i):
		if(temp == "none"):
			pass
		else:
			if(root.leaf == True):
				print temp, "=", root.sam, ":", root.label
			else:
				print temp, "=", root.sam, ":"
		for i in range(len(root.children)):
			Tree.printTree((root.level * "| ") + root.label, root.children[i], i + 1)