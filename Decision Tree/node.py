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