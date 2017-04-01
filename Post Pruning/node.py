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
	parent = None
	sam = None

	def __init__(self, columnNames=[], parent=None, leaf=False, label="", decision=0, children=[]):
		self.columnNames = columnNames
		self.parent = parent
		self.leaf = False
		self.label = ""
		self.decision = 0
		self.children = []
		