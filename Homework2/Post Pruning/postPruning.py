from tree import Tree
from readData import ReadData
import copy
from node import Node
import random
class PostPruning(object):
	@staticmethod
	def addNonLeaf(root, count, q):
		if(root.leaf == False):
			q.append(root)
		else:
			return q
		for i in range(len(root.children)):
			q = PostPruning.addNonLeaf(root.children[i], count + 1, q)
		return q
	
	@staticmethod
	def orderNodes():
		orderedNodes = []
		return orderedNodes
	
	@staticmethod
	def getLeafCount(root, count, value):
		if(root.leaf == True):
			if(root.value == value):
				count = count + 1
				return count
		for i in range(len(root.children)):
			count = PostPruning.getLeafCount(root.children[i], count, value)
		return count

	@staticmethod
	def getMajority(node):
		one = PostPruning.getLeafCount(node, 0, 1)
		zero = PostPruning.getLeafCount(node, 0, 0)
		if(zero > one):
			return 0
		else:
			return 1

	@staticmethod
	def replaceData(tree, node, maj):
		if tree == node:
			tree.children = []
			tree.value = maj
			tree.label = maj
			tree.leaf = True
			tree.sam = maj
			return
		for i in range(len(tree.children)):
			PostPruning.replaceData(tree.children[i], node, maj)

	@staticmethod
	def postPruningAlgorithm(l, k, root, validationDatasetMatrix):
		# build a decision tree using all training data, call it as D
		# Let Dbest = D
		nodeBest = copy.deepcopy(root)
		queue = []
		for i in range(1, l + 1):
			# copy a tree into a new tree D'
			nodeTemp = copy.deepcopy(root)
			# M = a random number between 1 and k
			m = random.randint(2, k + 1)
			for j in range(1, m + 1):
				# queue consists of non-leaf nodes and we can find its length
				queue = PostPruning.addNonLeaf(nodeTemp, 0, queue)
				# nonLeafNodes = PostPruning.orderNodes(nodeTemp)
				# P = a random number between 1 and N
				p = random.randint(1, (len(queue) - 1))
				maj = PostPruning.getMajority(queue[p])
				PostPruning.replaceData(nodeTemp, queue[p], maj)
				# Tree.printTree("none", nodeTemp, 0)
			tempAccuracy = Tree.calculateAccuracy(validationDatasetMatrix, nodeTemp)
			bestAccuracy = Tree.calculateAccuracy(validationDatasetMatrix, nodeBest)
			if(tempAccuracy > bestAccuracy):
				nodeBest = copy.deepcopy(nodeTemp)
		return nodeBest
