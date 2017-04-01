class CondProb(object):
	term = ""
	className = 0
	def __init__(self, term, className):
		self.term = term
		self.className = className
	def __eq__(self, other):
		return self.__dict__ == other.__dict__
	def __str__(self):
		return str(self.__dict__)